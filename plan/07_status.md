# 07 — Status (updated 2026-09-28)

## Done

- **M0 setup.** `cyber_jev/` is its own git repo and is listed in
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

Full tables: `results/m1_csic_only/*.md` (M1 data; not comparable with the v2 tables below).

## What went wrong on held-out

Per source, Cyber-Jev flags as attack: SQLi 99%, XSS 100%, **normal 100%**. The held-out
"normal" payloads are JSON snippets and prose; every "safe" training example is a request
to CSIC's one web shop (`/tienda1/...`). Both models learned "safe = looks like a CSIC
request", not "attack = contains an attack". That's a **training-data diversity problem**,
not a model-size or epochs problem. Cyber-Jev's higher held-out AUROC (0.81 vs 0.71) shows
it ranks better, but no threshold fitted on CSIC transfers.

## Latency, M1 model (`results/m1_csic_only/latency_dev.md`)

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

1. ✅ **Diverse training data** (done 2026-09-28, see below). Add `shengqin/web-attacks` *train* split (normal JSON/text +
   SQLi + XSS payloads) to training, and find a **new** held-out source (candidates to verify:
   `Kaveny/sql-injection`, `srimathi2026/sql-injection-datasets`, an XSS set, HttpParamsDataset).
   Also add benign non-shop requests so "safe" isn't one site.
2. ✅ **Train longer** (done: 4 epochs, best at epoch 3). Dev NLL was still falling fast (0.56 → 0.22 in epoch 2); try 4 epochs.
3. **Latency.** (a) Compare against a 6-layer base (the Nano-Jev v0.1 backbone, about 2× faster);
   (b) ONNX + int8 on CPU; (c) cap max_length at 128 for HTTP.
4. Only then M3 (prompt_injection, phishing_url).

## M2 step 1–2 results — data v2, `runs/cyber-jev-v2` (2026-09-28)

Data v2 (see `03_data.md`): train on CSIC + `shengqin/web-attacks` + `ai-waf`; held-out is
new: `sqli-queries` (`zrmarine/sql_injection`) and `dvwa-juiceshop` (`vyykaaa/dataset-web-attack`).
Training: from Nano-Jev v1.0, 4 epochs, max_length 256, 21.5k examples, ~11 min. Dev NLL by
epoch 0.236 → 0.114 → **0.092** → 0.097; epoch 3 kept. Temperatures fitted on v2 calib.

| Model | Test set | acc | macro-F1 | AUROC | DR@1%FPR | ECE (cal) |
|---|---|---|---|---|---|---|
| TF-IDF + LR | in-domain (3 sources) | 0.963 | 0.962 | 0.996 | 0.938 | 0.006 |
| Cyber-Jev v2 | in-domain | **0.977** | **0.977** | 0.996 | **0.971** | 0.011 |
| TF-IDF + LR | held-out | 0.519 | 0.459 | 0.657 | **0.354** | 0.392 |
| Cyber-Jev M1 (`cyber-jev-dev`) | held-out | 0.520 | 0.346 | 0.702 | 0.043 | 0.106 |
| Cyber-Jev v2 | held-out | **0.723** | **0.699** | **0.881** | 0.343 | 0.240 |

Held-out by source (calibrated; FPR / DR at the default 0.5 threshold):

| Model | Source | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 |
|---|---|---|---|---|---|
| TF-IDF + LR | dvwa-juiceshop | 0.347 | 0.003 | 0.853 | 0.704 |
| Cyber-Jev M1 | dvwa-juiceshop | 0.150 | 0.005 | 1.000 | 1.000 |
| Cyber-Jev v2 | dvwa-juiceshop | **0.853** | 0.084 | **0.392** | 0.958 |
| TF-IDF + LR | sqli-queries | **0.992** | 0.889 | 0.795 | 0.999 |
| Cyber-Jev M1 | sqli-queries | 0.869 | 0.190 | 0.994 | 1.000 |
| Cyber-Jev v2 | sqli-queries | 0.991 | 0.840 | **0.593** | 0.999 |

Tables: `results/cyberjev_v2*.md`, `results/tfidf*.md`, `results/m1model_v2_heldout.md`.

What this says:

- **Diversity fixed the "flag everything" failure.** The M1 model flags 100% / 99% of held-out
  safe traffic; v2 flags 39% / 59%. On full requests from unseen apps (dvwa-juiceshop) v2 ranks
  well (AUROC 0.85) where TF-IDF is worse than chance (0.35): this is where the encoder
  earns its place.
- **Still too many false alarms off-domain.** Benign SQL queries look like SQLi to both
  models (59% flagged at 0.5), and ranking is fine (AUROC 0.99) but the threshold isn't.
  The in-domain calibration does not transfer; a deployment would need per-site threshold
  tuning, or training data with benign SQL-like / code-like text.
- In-domain, v2 now beats TF-IDF on accuracy and DR@1%FPR (0.971 vs 0.938); ai-waf and
  web-attacks are near-trivially separable, so CSIC (0.983 AUROC) is the informative source.
- Caveat: dvwa-juiceshop is partly separable by path (attacks mostly on DVWA, normal all on
  Juice Shop), so its AUROC flatters every model somewhat.

## M2 step 3 — latency (2026-09-28)

### 6-layer base (`runs/cyber-jev-v2-l6`, from the Nano-Jev v0.1 backbone, MiniLM-L6)

Same data and recipe as v2 (4 epochs, max_length 256; best dev NLL 0.114 at epoch 3,
~6.5 min). One seed each, so small differences are noise; the held-out gap is not small.

| Model | layers | in-domain AUROC | in-domain DR@1%FPR | held-out AUROC | held-out DR@1%FPR | dvwa FPR@0.5 | sqli FPR@0.5 |
|---|---|---|---|---|---|---|---|
| Cyber-Jev v2 | 12 | 0.996 | 0.971 | 0.881 | 0.343 | 0.392 | 0.593 |
| Cyber-Jev v2-l6 | 6 | 0.995 | 0.968 | **0.953** | **0.457** | **0.212** | **0.413** |

| Setting (median ms, 300 random test requests) | v2 (12 layers) | v2-l6 (6 layers) |
|---|---|---|
| CPU 8 threads, batch 1 | 27.8 | **14.3** |
| CPU 1 thread, batch 1 | 75.5 | 37.2 |
| GPU, batch 1 | 13.6 | 7.8 |
| GPU, batch 64 (per decision) | 2.1 | 1.2 |

The 6-layer model is 2× faster and **generalises better** held-out (AUROC 0.95 vs 0.88)
with no in-domain loss. Plausible reason: the v0.1 backbone started from an MS MARCO
cross-encoder; the 12-layer one may overfit the three training sources more. Worth a
second seed before relying on it. **v2-l6 is the working model from here.**

### max_length 128 (v2, no retraining): rejected

Capping inputs at inference costs a lot on full requests: ai-waf DR@0.5 0.970 → 0.743,
dvwa-juiceshop AUROC 0.853 → 0.695 (`results/cyberjev_v2_len128*.md`). Full requests are
~140 tokens median plus ~25 for the question and option, so attacks in later headers or the
body get cut. Keep 256.

### ONNX on CPU (v2-l6, 8 threads)

`scripts/onnx_cpu.py` exports `model.onnx` (87 MB) and a dynamic-int8 `model.int8.onnx`
(22 MB) into the model folder and compares them with PyTorch, one variant per process
(a first all-in-one run was stopped for low system memory). Held-out is a fixed random
sample of 3000, so its numbers differ slightly from the full-set tables above.
`results/onnx_v2_l6.md`:

| variant | size MB | in-domain AUROC | in-domain DR@1%FPR | held-out AUROC | held-out DR@1%FPR | median ms | p95 ms |
|---|---|---|---|---|---|---|---|
| PyTorch fp32 | 87 | 0.995 | 0.968 | 0.958 | 0.517 | 12.7 | 25.0 |
| ONNX fp32 | 87 | 0.995 | 0.968 | 0.958 | 0.517 | 11.0 | 29.4 |
| ONNX int8 | 22 | 0.995 | 0.966 | 0.960 | 0.495 | **8.1** | 23.4 |

int8 costs nothing measurable in accuracy, is 4× smaller and 1.6× faster than PyTorch.
Still ~1.6× off the ≤ 5 ms CPU target at the median, and p95 (~23 ms) is dominated by long
requests.

Next:
1. **One pass per binary decision.** Each decision scores both options (two encoder
   passes). Scoring only the threat option against a fixed zero, or caching, would roughly
   halve latency: the most likely route to ≤ 5 ms.
2. **Second seed** for v2 vs v2-l6 before relying on the 6-layer model's held-out lead.
3. **Hard benign negatives** (SQL-like text, code snippets) to cut off-domain false alarms.
4. Then M3 (prompt_injection, phishing_url).

## M2 step 4 — one encoder pass per binary decision (2026-09-29)

Inference only, no retraining. `scripts/single_pass.py` scores both options once and
compares the two-pass softmax with one-pass `sigmoid((s·z − b) / T)`, b and T fitted on
calib, for the threat option (s = +1) and the safe option (s = −1). The variant is picked
by **calib NLL**, never by test results; `--save` writes it to `<model>/one_pass.json`,
which the Decider then uses for built-in decisions asked with their own two options.
`results/single_pass_v2_l6.md` (full test sets, GPU):

| test set | variant | calib NLL | AUROC | DR@1%FPR | NLL | ECE |
|---|---|---|---|---|---|---|
| in-domain | two-pass | 0.084 | 0.995 | 0.968 | 0.077 | 0.003 |
| in-domain | threat-only (picked) | 0.099 | 0.990 | 0.968 | 0.091 | 0.003 |
| in-domain | safe-only | 0.110 | 0.995 | 0.968 | 0.096 | 0.010 |
| held-out | two-pass | 0.084 | 0.953 | 0.457 | 0.680 | 0.145 |
| held-out | threat-only (picked) | 0.099 | 0.945 | 0.393 | 0.640 | 0.148 |
| held-out | safe-only | 0.110 | **0.958** | **0.572** | **0.399** | **0.100** |

Calib NLL picks threat-only, which is within the 0.01 AUROC budget held-out (0.945 vs
0.953) but loses DR@1%FPR (0.457 → 0.393). Safe-only is better held-out on every metric
(and cuts FPR@0.5: dvwa-juiceshop 0.21 → 0.11, sqli-queries 0.41 → 0.32), but choosing it
from these numbers would be selecting on the test set. Decide with a second seed or a
separate out-of-domain validation set.

CPU latency, one pass (`results/onnx_v2_l6_one_pass.md`, 8 threads, held-out sample 3000;
compare with the two-pass table above):

| variant | in-domain AUROC | held-out AUROC | held-out DR@1%FPR | median ms | p95 ms |
|---|---|---|---|---|---|
| PyTorch fp32 | 0.990 | 0.950 | 0.455 | 8.7 | 15.3 |
| ONNX fp32 | 0.990 | 0.950 | 0.455 | 5.3 | 16.0 |
| ONNX int8 | 0.989 | 0.950 | 0.477 | **4.2** | **13.2** |

**The ≤ 5 ms CPU median is met with ONNX int8** (8.1 → 4.2 ms; p95 23.4 → 13.2 ms). On the
same held-out sample the two-pass int8 AUROC was 0.960, so one pass costs 0.010 there.
The Decider itself still runs PyTorch: `results/latency_v2-l6_one_pass.md` has CPU 14.3 →
9.6 ms median, GPU batch 64 1.24 → 0.69 ms per decision.
