# 07 — Status (2026-09-27)

## Done

- **M0 setup.** `cyber_jev/` is its own git repo (no commits yet) and is listed in
  `code_repo/.git/info/exclude`, so it can't be committed into nano-jev. Package copied and
  renamed; schema, decider, CLI, data, tests adapted. `pytest`: 36 passed, 4 skipped
  (network tests: no published weights yet).
- **M1 http_attack prototype.** Data built, TF-IDF baseline, zero-shot baseline, one
  training run (from Nano-Jev v1.0, 2 epochs, max_length 256, about 2 min on the RTX 3060).

## M1 results — `http_attack`

Temperatures fitted on CSIC calib. DR = detection rate at a fixed false-positive rate.

| Model | Test set | acc | macro-F1 | AUROC | DR@1%FPR | ECE (cal) |
|---|---|---|---|---|---|---|
| TF-IDF + LR | CSIC (in-domain) | **0.952** | **0.951** | **0.989** | **0.926** | 0.010 |
| Nano-Jev v1.0 zero-shot | CSIC | 0.385 | 0.278 | 0.495 | 0.002 | 0.120 |
| Cyber-Jev dev | CSIC | 0.924 | 0.922 | 0.967 | 0.870 | 0.031 |
| TF-IDF + LR | web-attacks (held-out) | 0.817 | 0.450 | 0.709 | 0.000 | 0.183 |
| Nano-Jev v1.0 zero-shot | web-attacks | 0.370 | 0.370 | 0.493 | 0.237 | 0.138 |
| Cyber-Jev dev | web-attacks | 0.814 | 0.450 | **0.810** | 0.040 | 0.161 |

Full tables: `results/*.md`.

## What went wrong on held-out

Per source, Cyber-Jev flags as attack: SQLi 99%, XSS 100%, **normal 100%**. The held-out
"normal" payloads are JSON snippets and prose; every "safe" training example is a request
to CSIC's one web shop (`/tienda1/...`). Both models learned "safe = looks like a CSIC
request", not "attack = contains an attack". That's a **training-data diversity problem**,
not a model-size or epochs problem. Cyber-Jev's higher held-out AUROC (0.81 vs 0.71) shows
it ranks better, but no threshold fitted on CSIC transfers.

## Latency (`results/latency_dev.md`)

| Setting | Median ms |
|---|---|
| CPU 8 threads, batch 1 | 26.1 |
| CPU 1 thread, batch 1 | 73.8 |
| GPU, batch 1 | 13.0 |
| GPU, batch 64 (per decision) | 1.7 |

Far from the ≤ 5 ms CPU target. Two encoder passes per decision (one per option) × 12 layers.

## M2 go/no-go: **continue, with changes**

Not a "no-go": the architecture learns (in-domain 0.92, better held-out ranking), and the
failure has a clear cause. Next steps, in order:

1. **Diverse training data.** Add `shengqin/web-attacks` *train* split (normal JSON/text +
   SQLi + XSS payloads) to training, and find a **new** held-out source (candidates to verify:
   `Kaveny/sql-injection`, `srimathi2026/sql-injection-datasets`, an XSS set, HttpParamsDataset).
   Also add benign non-shop requests so "safe" isn't one site.
2. **Train longer.** Dev NLL was still falling fast (0.56 → 0.22 in epoch 2); try 4 epochs.
3. **Latency.** (a) Compare against a 6-layer base (the Nano-Jev v0.1 backbone, about 2× faster);
   (b) ONNX + int8 on CPU; (c) cap max_length at 128 for HTTP.
4. Only then M3 (prompt_injection, phishing_url).
