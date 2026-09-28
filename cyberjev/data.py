"""Build typed security-decision examples from public datasets.

Each example: {decision, question, options, state, label, source}.
`source` is "<dataset>/<subtype>", e.g. "web-attacks/SQLi"; reports group by <dataset>.
"""

import random

from datasets import load_dataset

from .schema import DECISIONS, normalize_http

# Training sources: calib and test come from the same sources (in-domain).
CSIC = "bridge4/CSIC2010_dataset_classification"   # HTTP requests to one shop, 0 normal / 1 anomalous
WEB_ATTACKS = "shengqin/web-attacks"                # payloads, text_label normal / XSS / SQLi
AI_WAF = "notesbymuneeb/ai-waf-dataset"             # full HTTP requests, many hosts, benign / malicious
# Held-out sources: never trained on, only for final reporting.
SQLI = "zrmarine/sql_injection"                     # SQL queries and payloads, 0 benign / 1 injection
WEB_ATTACK_REQS = "vyykaaa/dataset-web-attack"      # DVWA + Juice Shop requests, normal / anomalous


def _example(decision: str, label: int, state: str, source: str) -> dict:
    d = DECISIONS[decision]
    return {"decision": decision, "question": d.question, "options": list(d.options),
            "state": state, "label": label, "source": source}


def _dedup(rows):
    """rows: (text, label, source). Keep the first of each text."""
    seen, out = set(), []
    for row in rows:
        if row[0] not in seen:
            seen.add(row[0])
            out.append(row)
    return out


def csic_to_text(raw: str) -> str:
    """Keep the request line and body. CSIC's headers are the same on every request, bar a
    random session cookie that would make near-duplicate requests look unique."""
    head, _, body = raw.partition("\n")          # the body follows the only real newline
    request_line = head.split("\\n", 1)[0]       # headers are joined by a literal "\n"
    return normalize_http(request_line + ("\n\n" + body if body.strip() else ""))


def _csic(split):
    return [(csic_to_text(r["requests"]), int(r["label"]),
             f"csic2010/{'anomalous' if r['label'] else 'normal'}")
            for r in load_dataset(CSIC, split=split)]


def _web_attacks(split):
    return [(normalize_http(r["Payload"]), int(r["Label"] != 0), f"web-attacks/{r['text_label']}")
            for r in load_dataset(WEB_ATTACKS, split=split)]


def _ai_waf():
    return [(normalize_http(r["text"]), int(r["label"] == "malicious"), f"ai-waf/{r['label']}")
            for r in load_dataset(AI_WAF, split="train")]


def http_attack_splits(sizes: dict, rng: random.Random) -> dict[str, list[tuple]]:
    """Three sources, each split so no text is in more than one split.

    CSIC and web-attacks: train from their train split, calib / test from their test split.
    ai-waf has one split: 80 / 10 / 10 at random.
    """
    out = {"train": [], "calib": [], "test": []}
    seen = set()
    for name, train_rows, rest_rows in [
        ("csic", _csic("train"), _csic("test")),
        ("web", _web_attacks("train"), _web_attacks("test")),
        ("waf", None, None),
    ]:
        if train_rows is None:
            rows = _dedup(r for r in _ai_waf() if r[0] not in seen)
            rng.shuffle(rows)
            n = len(rows)
            train_rows, rest_rows = rows[: int(0.8 * n)], rows[int(0.8 * n):]
        train_rows = _dedup(r for r in train_rows if r[0] not in seen)
        seen |= {r[0] for r in train_rows}
        rest_rows = _dedup(r for r in rest_rows if r[0] not in seen)
        seen |= {r[0] for r in rest_rows}
        rng.shuffle(train_rows)
        rng.shuffle(rest_rows)
        n_cal, n_test = sizes[f"{name}_calib"], sizes[f"{name}_test"]
        out["train"] += train_rows[: sizes[f"{name}_train"]]
        out["calib"] += rest_rows[:n_cal]
        out["test"] += rest_rows[n_cal: n_cal + n_test]
    return out


def http_attack_heldout(sizes: dict, rng: random.Random, exclude: set[str]) -> list[tuple]:
    """Sources never used in training; any text also in `exclude` (the training texts) is dropped."""
    sqli = _dedup((normalize_http(r["Query"]), int(r["Label"]), f"sqli-queries/{r['Label']}")
                  for r in load_dataset(SQLI, split="train"))
    reqs = _dedup((normalize_http(r["raw_request"]), int(r["label"] == "anomalous"),
                   f"dvwa-juiceshop/{r['attack_type'] or 'normal'}")
                  for r in load_dataset(WEB_ATTACK_REQS, split="test")
                  if r["label"] in ("normal", "anomalous") and r["raw_request"]
                  and r["raw_request"][:1].isupper() and " HTTP/" in r["raw_request"])
    out = []
    for rows, n in [(sqli, sizes["sqli_heldout"]), (reqs, sizes["reqs_heldout"])]:
        rows = [r for r in rows if r[0] not in exclude]
        rng.shuffle(rows)
        out += rows[:n]
    return out


def _examples(rows):
    return [_example("http_attack", y, t, s) for t, y, s in rows]


def build_all(sizes: dict, seed: int = 0) -> dict[str, list[dict]]:
    """Return {"train", "calib", "test", "heldout"} example lists."""
    rng = random.Random(seed)
    splits = http_attack_splits(sizes, rng)
    exclude = {t for rows in splits.values() for t, _, _ in rows}
    splits["heldout"] = http_attack_heldout(sizes, rng, exclude)
    rng.shuffle(splits["train"])
    return {name: _examples(rows) for name, rows in splits.items()}
