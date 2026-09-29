"""Inference API: typed decisions with calibrated probabilities."""

import json
from pathlib import Path

import torch

from . import model as M
from . import registry
from .schema import DECISIONS, normalize_http


class Decider:
    def __init__(self, model, tok, max_length: int, temperatures: dict[str, float], device,
                 config: dict | None = None, path: Path | None = None,
                 one_pass: dict[str, dict] | None = None):
        self.model, self.tok, self.max_length = model, tok, max_length
        self.temperatures, self.device = temperatures, device
        self.config = config or {}  # cyberjev_config.json: version, base, params, ...
        self.path = path  # local folder the weights were loaded from
        # one_pass.json (scripts/single_pass.py): per built-in binary decision, which option
        # to score alone ({option, sign, temperature, shift}). Set to {} to always use two passes.
        self.one_pass = one_pass or {}

    @property
    def version(self) -> str:
        return self.config.get("version", "unknown")

    @classmethod
    def from_pretrained(cls, path: str | None = None, device: str | None = None,
                        revision: str | None = None) -> "Decider":
        """Load weights, downloading them from the Hub on first use.

        path: a version ("v0.1"), a Hub repo id ("user/cyber-jev", optionally "@v0.1"),
        or a local folder. None uses the selected model (see `cyberjev.registry`).
        Hub repos are downloaded whole, so the calibration temperatures come along.
        """
        device = device or ("cuda" if torch.cuda.is_available() else "cpu")
        if path and Path(path).is_dir():
            target = path
        elif revision:
            target = f"{path or registry.DEFAULT_REPO}@{revision}"
        else:
            target = path
        local = registry.resolve(target)
        model, tok = M.load(str(local), device)
        cfg_path = local / "cyberjev_config.json"
        cfg = json.loads(cfg_path.read_text(encoding="utf-8")) if cfg_path.exists() else {}
        cal_path = local / "calibration.json"
        temps = json.loads(cal_path.read_text(encoding="utf-8")) if cal_path.exists() else {}
        one_path = local / "one_pass.json"
        one = json.loads(one_path.read_text(encoding="utf-8")) if one_path.exists() else {}
        return cls(model, tok, cfg.get("max_length", 512), temps, device, cfg, local, one)

    def _fast(self, item: dict) -> dict | None:
        """The one-pass setting for this item, or None to score every option."""
        fast = self.one_pass.get(item.get("decision", ""))
        d = DECISIONS.get(item.get("decision", ""))
        return fast if fast and d and list(item["options"]) == list(d.options) else None

    def decide_many(self, items: list[dict]) -> list[dict[str, float]]:
        """items: {question, options, state, decision?} -> [{option: probability}].

        Built-in binary decisions with their own options are scored in one encoder pass
        when the model folder has one_pass.json; everything else scores each option.
        """
        fast = [self._fast(it) for it in items]
        slow_idx = [i for i, f in enumerate(fast) if f is None]
        fast_idx = [i for i, f in enumerate(fast) if f is not None]
        out: list[dict | None] = [None] * len(items)

        logits = M.score(self.model, self.tok, [items[i] for i in slow_idx], self.max_length,
                         self.device)
        for i, lg in zip(slow_idx, logits):
            t = self.temperatures.get(items[i].get("decision", ""), 1.0)
            out[i] = dict(zip(items[i]["options"], torch.softmax(lg / t, dim=0).tolist()))

        single = [{**items[i], "options": [items[i]["options"][fast[i]["option"]]]}
                  for i in fast_idx]
        logits = M.score(self.model, self.tok, single, self.max_length, self.device)
        for i, lg in zip(fast_idx, logits):
            f = fast[i]
            p = float(torch.sigmoid((f["sign"] * lg[0] - f["shift"]) / f["temperature"]))
            safe, threat = items[i]["options"]
            out[i] = {safe: 1.0 - p, threat: p}
        return out

    def decide(self, question: str, options: list[str], state: str,
               decision: str | None = None) -> dict[str, float]:
        return self.decide_many([{"question": question, "options": options, "state": state,
                                  "decision": decision or ""}])[0]

    # Convenience wrappers for the built-in decisions --------------------------------

    # Each takes one string (-> one result) or a list of strings (-> a list, scored in batches).

    def _builtin(self, decision: str, states: str | list[str]):
        d = DECISIONS[decision]
        batch = [states] if isinstance(states, str) else states
        out = self.decide_many([{"decision": decision, "question": d.question,
                                 "options": list(d.options), "state": s} for s in batch])
        return out[0] if isinstance(states, str) else out

    def http_attack(self, request: str | list[str]):
        """request: request line and body, e.g. "GET /search?q=shoes HTTP/1.1"."""
        if isinstance(request, str):
            return self._builtin("http_attack", normalize_http(request))
        return self._builtin("http_attack", [normalize_http(r) for r in request])

    def prompt_injection(self, text: str | list[str]):
        return self._builtin("prompt_injection", text)

    def phishing_url(self, url: str | list[str]):
        return self._builtin("phishing_url", url)
