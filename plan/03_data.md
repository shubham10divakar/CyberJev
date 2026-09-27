# 03 — Data

Every example uses Nano-Jev's format:

```json
{"decision": "http_attack", "question": "Is this HTTP request a web attack ...?",
 "options": ["safe", "attack"], "state": "GET /tienda1/... HTTP/1.1", "label": 1,
 "source": "csic2010"}
```

## Sources

| Decision | In-domain (train / calib / test) | Held-out (never trained on) |
|---|---|---|
| `http_attack` | CSIC 2010 — `bridge4/CSIC2010_dataset_classification` (43k train / 18.5k test requests) | `shengqin/web-attacks` test split: 1013 normal, 1986 XSS, 2524 SQLi payloads |
| `prompt_injection` | `deepset/prompt-injections`, `xTRam1/safe-guard-prompt-injection` (to verify) | `jackhhao/jailbreak-classification` (to verify) |
| `phishing_url` | a malicious-URL set, e.g. `surajshelke/malicious_url` (to verify) | a second URL set from a different source (to pick) |

"To verify" = check it exists, its size, its labels and its licence before use.

## Text format

- **HTTP (CSIC):** keep the request line and body, URL-decode them, drop the headers
  (they are identical boilerplate in CSIC, and dropping them keeps inputs short, which
  helps latency). Already implemented in `_staging/prepare_attack_data.py`.
- **Prompts:** raw text, truncated to max_length.
- **URLs:** raw URL string.

## Splits

- Train from each dataset's train split. Calib and test from its test split, with
  anything that also appears in train removed (CSIC had 43 overlapping requests).
- Balance decisions so none dominates training (cap each at ~10k train examples).
- Held-out sets are only used for final reporting, never for choosing a model.

## Known data caveats

- CSIC "anomalous" includes odd-but-harmless-looking requests (e.g. a tampered parameter
  name `B1A=`), so it is harder than spotting obvious SQLi.
- After deduplication CSIC is ~63% attack. Report balanced metrics (macro-F1, detection
  rate at fixed FPR), not only accuracy.
- CSIC comes from a single synthetic web shop, so held-out results matter more than
  in-domain ones.

## Prototype already built (in `_staging/`)

```
data_attack/train.jsonl          10000  (attack 6270 / safe 3730)
data_attack/calib.jsonl           1500  (attack 906 / safe 594)
data_attack/test.jsonl            3000  (attack 1846 / safe 1154)
data_attack_heldout/test.jsonl    5523  (attack 4510 / safe 1013)
```
