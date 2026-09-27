"""Build typed security-decision examples from public datasets.

Each example: {decision, question, options, state, label, source}.
"""

import random

from datasets import load_dataset

from .schema import DECISIONS, normalize_http

CSIC = "bridge4/CSIC2010_dataset_classification"   # HTTP requests, label 0 normal / 1 anomalous
WEB_ATTACKS = "shengqin/web-attacks"                # payloads, label 0 normal / 1 XSS / 2 SQLi


def _example(decision: str, label: int, state: str, source: str) -> dict:
    d = DECISIONS[decision]
    return {"decision": decision, "question": d.question, "options": list(d.options),
            "state": state, "label": label, "source": source}


def _dedup(rows):
    seen, out = set(), []
    for text, label in rows:
        if text not in seen:
            seen.add(text)
            out.append((text, label))
    return out


def csic_to_text(raw: str) -> str:
    """Keep the request line and body; CSIC's headers are identical boilerplate."""
    head, _, body = raw.partition("\n")          # the body follows the only real newline
    request_line = head.split("\\n", 1)[0]       # headers are joined by a literal "\n"
    text = request_line + (f"\nbody: {body}" if body.strip() else "")
    return normalize_http(text).replace("http://localhost:8080", "")


def http_attack_splits(sizes: dict, rng: random.Random) -> dict[str, list[dict]]:
    """CSIC 2010: train from its train split; calib and test from its test split,
    minus any request that also appears in train."""
    csic = load_dataset(CSIC)
    train = _dedup((csic_to_text(r["requests"]), int(r["label"])) for r in csic["train"])
    seen = {t for t, _ in train}
    rest = [r for r in _dedup((csic_to_text(r["requests"]), int(r["label"])) for r in csic["test"])
            if r[0] not in seen]
    rng.shuffle(train)
    rng.shuffle(rest)
    n_cal, n_test = sizes["http_calib"], sizes["http_test"]

    def examples(rows):
        return [_example("http_attack", y, t, "csic2010") for t, y in rows]

    return {"train": examples(train[: sizes["http_train"]]), "calib": examples(rest[:n_cal]),
            "test": examples(rest[n_cal: n_cal + n_test])}


def http_attack_heldout() -> list[dict]:
    """Payloads from a different source: normal -> safe, XSS / SQLi -> attack."""
    rows = load_dataset(WEB_ATTACKS, split="test")
    return [_example("http_attack", int(r["Label"] != 0), normalize_http(r["Payload"]),
                     f"web-attacks/{r['text_label']}") for r in rows]


def build_all(sizes: dict, seed: int = 0) -> dict[str, list[dict]]:
    """Return {"train", "calib", "test"} example lists."""
    rng = random.Random(seed)
    splits = http_attack_splits(sizes, rng)
    rng.shuffle(splits["train"])
    return splits


def build_heldout(seed: int = 0) -> list[dict]:
    """Test examples from datasets never used in training."""
    return http_attack_heldout()
