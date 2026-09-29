# 03 — Data

Every example uses Nano-Jev's format:

```json
{"decision": "http_attack", "question": "Is this HTTP request a web attack ...?",
 "options": ["safe", "attack"], "state": "GET /tienda1/... HTTP/1.1", "label": 1,
 "source": "csic2010"}
```

## Sources

### `http_attack` (v2, 2026-09-28)

M1 trained only on CSIC, whose "safe" requests all come from one shop, so the model learned
"safe = looks like CSIC". v2 trains on three sources and tests on two new ones.

| Role | Source | What it is | License |
|---|---|---|---|
| train / calib / test | CSIC 2010 — `bridge4/CSIC2010_dataset_classification` | requests to one synthetic shop, normal / anomalous | (CSIC terms) |
| train / calib / test | `shengqin/web-attacks` (train split → train, test split → calib/test) | bare payloads: normal text/JSON, XSS, SQLi | none stated |
| train / calib / test | `notesbymuneeb/ai-waf-dataset` (80/10/10) | full requests to ~7.7k hosts, benign / malicious (XSS, SQLi, SSTI, traversal, header attacks, ...) | MIT |
| held-out | `zrmarine/sql_injection` (6000 sampled) | SQL queries and SQLi payloads; benign side includes ordinary SQL, a hard negative | none stated |
| held-out | `vyykaaa/dataset-web-attack` test split | DVWA + Juice Shop requests, 20 attack types | none stated |

Checked and **not used**: `YangYang-Research/web-attack-detection` / `truongp/...` (identical
copies; contain CSIC, and many rows are headers only), `Kaveny/sql-injection` (chat-formatted),
`srimathi2026/sql-injection-datasets` (empty repo), `darkknight25/WAF_DETECTION_DATASET` (broken
JSONL), and the many `*xss-probe*` repos (they probe the HF viewer, not datasets).

Held-out caveats: in `dvwa-juiceshop` most attacks target DVWA's `/vulnerabilities/sqli/`
while all normal traffic is Juice Shop, so path alone separates much of it; read its
per-source numbers with that in mind. Licences marked "none stated" are used for research
evaluation only; check before any release that ships data.

Current sizes (`python scripts/prepare_data.py`):

```
data/train.jsonl        21550  csic 6000 · web-attacks 6000 · ai-waf 9550   (attack 52%)
data/calib.jsonl         1600  csic 500  · web-attacks 500  · ai-waf 600
data/test.jsonl          4200  csic 1500 · web-attacks 1500 · ai-waf 1200
data_heldout/test.jsonl 10320  sqli-queries 6000 (attack 36%) · dvwa-juiceshop 4320 (attack 73%)
```

No text occurs in more than one split; held-out examples that match any in-domain text
are dropped.

### Benign SQL candidates (for step 3, checked 2026-09-29 from Hub metadata only)

| Dataset | Licence | Size | Notes |
|---|---|---|---|
| `gretelai/synthetic_text_to_sql` | Apache-2.0 | 100k+ | synthetic; varied SQL incl. INSERT / UPDATE / DDL. Candidate for **training** benign SQL |
| `xlangai/spider` | CC-BY-SA-4.0 | ~8k train + 1k val | human-written queries over 200 DBs. Candidate for the **out-of-domain validation** set |
| `b-mc2/sql-create-context` | CC-BY-4.0 | ~78k | built from WikiSQL + Spider: don't use it next to Spider (overlap) |
| `Salesforce/wikisql` | unknown | ~80k | loading script only, no licence: skip |

Not downloaded yet: check columns, query styles and overlap with `zrmarine/sql_injection`
(held-out) before use.

### Other decisions

| Decision | In-domain | Held-out |
|---|---|---|
| `prompt_injection` | `deepset/prompt-injections`, `xTRam1/safe-guard-prompt-injection` (to verify) | `jackhhao/jailbreak-classification` (to verify) |
| `phishing_url` | a malicious-URL set, e.g. `surajshelke/malicious_url` (to verify) | a second URL set from a different source (to pick) |

"To verify" = check it exists, its size, its labels and its licence before use.

## Text format

`cyberjev.schema.normalize_http` is used for training data and at inference:

- **Full requests:** request line (scheme and host stripped), then every header except
  content-negotiation boilerplate (`Accept*`, `Connection`, `Cache-Control`, `Pragma`,
  `Content-Length`, `Sec-CH-*`, `Sec-Fetch-*`, ...), then `body: ...`; URL-decoded. Headers
  that can carry payloads (User-Agent, Referer, Cookie, Host, X-*) are kept.
- **CSIC:** request line and body only (its headers are identical on every request, bar a
  random session cookie that would defeat deduplication).
- **Bare payloads:** URL-decoded only.
- **Prompts:** raw text, truncated to max_length. **URLs:** raw URL string.
- Token lengths: payloads ~40, requests median 80–160, ~5% of full requests exceed 256.

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
- ai-waf looks synthetic: TF-IDF separates it perfectly (AUROC 1.000). It adds diversity of
  safe traffic, not difficulty.
- Reports break every test set down by source (`by_source`), since a pooled number can hide
  a source where all safe examples are flagged.
