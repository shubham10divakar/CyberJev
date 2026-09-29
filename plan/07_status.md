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

### ONNX backend in the Decider (2026-09-29)

On CPU, `Decider.from_pretrained` now loads `model.int8.onnx` when `onnxruntime` is
installed (`backend="auto"`), with calibration refitted on the int8 logits by
`onnx_cpu.py --save` (`one_pass.model.int8.json`: T 1.26, b −3.25 vs PyTorch 1.32, −3.10).
End to end, as a caller sees it (`results/latency_v2-l6_onnx.md`, 8 threads, batch 1):
**4.3–4.5 ms** median over three runs, p95 12.7–13.8 ms; PyTorch 9.8 ms. The two-pass
`onnx_cpu.py` rerun reproduced 8.0 ms; a one-pass rerun gave 5.6 ms int8 (vs 4.2 before)
with identical accuracy, so single runs vary by up to ~1.5 ms with other programs open.

## M2 step 2 — second seed and 3 epochs (2026-09-29)

`scripts/seed_runs.sh`: same settings as before (batch 16, lr 3e-5, max_length 256, best epoch
by dev NLL). Two-pass, calibrated, full test sets:

| model | layers | seed | epochs (best) | in-domain AUROC | held-out AUROC | held-out DR@1%FPR | held-out ECE | sqli FPR@0.5 |
|---|---|---|---|---|---|---|---|---|
| v2-l6 | 6 | 0 | 4 (3) | 0.995 | **0.953** | 0.457 | 0.145 | 0.41 |
| v2-l6-s1 | 6 | 1 | 4 (2) | 0.994 | 0.944 | 0.264 | 0.119 | 0.32 |
| v2-l6-e3 | 6 | 0 | 3 (2) | 0.995 | 0.905 | 0.305 | 0.175 | 0.52 |
| v2 | 12 | 0 | 4 (3) | 0.996 | 0.881 | 0.343 | 0.240 | 0.59 |
| v2-s1 | 12 | 1 | 4 (4) | 0.997 | 0.864 | 0.077 | 0.257 | 0.51 |

- **The 6-layer lead holds** across seeds (0.953 / 0.944 vs 0.881 / 0.864). Keep v2-l6.
- **3 epochs is not better** (0.905): keep 4 epochs with best-epoch selection.
- **Held-out is noisy.** In-domain barely moves (0.994–0.997), but held-out AUROC spans
  0.905–0.953 for the same 6-layer recipe and DR@1%FPR spans 0.26–0.46. Treat single-run
  held-out differences below ~0.05 AUROC as noise.

One pass (`results/single_pass_*.md`), held-out AUROC:

| model | two-pass | threat-only | safe-only | calib NLL picks |
|---|---|---|---|---|
| v2-l6 | 0.953 | 0.945 | **0.958** | threat-only |
| v2-l6-s1 | 0.944 | 0.913 | **0.963** | threat-only |
| v2-l6-e3 | 0.905 | 0.847 | **0.949** | threat-only |
| v2-s1 (12 layers) | 0.864 | 0.848 | 0.853 | threat-only |

On all three 6-layer models, safe-only beats both threat-only and two-pass held-out, while
threat-only can fall far (0.847). Calib NLL (in-domain) picks threat-only every time, so
in-domain calibration does not predict out-of-domain robustness here. This is still read off
the held-out test, so confirm on the out-of-domain validation set (step 3b) before switching.

## Data v3 and the out-of-domain validation set (2026-09-29)

Data v3 adds 3000 benign SQL queries (gretel, synthetic) to training and builds
`data_val/val.jsonl` (waf-v2 requests + Spider SQL); details in `03_data.md`.

**One-pass variant on val** (`results/single_pass_v2_l6*_val.md`, v2 models, v2 calib):

| model | val: two-pass | threat-only | safe-only | held-out: threat-only | safe-only |
|---|---|---|---|---|---|
| v2-l6 | 0.856 | **0.866** | 0.830 | 0.945 | **0.958** |
| v2-l6-s1 | 0.833 | **0.834** | 0.817 | 0.913 | **0.963** |
| v2-l6-e3 | 0.823 | **0.829** | 0.796 | 0.847 | **0.949** |

Val picks threat-only on all three; held-out favoured safe-only. The better variant depends
on the data, and both fixed rules (calib NLL, val AUROC) pick threat-only, so **threat-only
stays**. Switching on the held-out numbers alone would have been a mistake.

Val is much harder than held-out (AUROC 0.82–0.87 vs 0.90–0.95; waf-v2 alone 0.86–0.89), and
v2 models flag about half of benign Spider SQL at 0.5 (FPR 0.47–0.63), the problem data v3
is meant to fix.

## M2 step 3 — data v3 results, `runs/cyber-jev-v3-l6` (2026-09-29)

`scripts/v3_runs.sh`: 6-layer, from Nano-Jev v0.1, 4 epochs (best epoch 3 for both seeds),
max_length 256, 24.5k examples, ~101 s/epoch. v2-l6 re-scored on the same sets (temperature
refitted on v3 calib) as the baseline. Two-pass, calibrated:

| model | in-domain AUROC | held-out AUROC | held-out DR@1%FPR | val AUROC | val DR@1%FPR |
|---|---|---|---|---|---|
| v2-l6 (baseline) | 0.970 | 0.953 | 0.457 | 0.856 | 0.229 |
| **v3-l6** (seed 0) | **0.997** | 0.949 | 0.030 | **0.909** | 0.169 |
| v3-l6-s1 | 0.996 | 0.985 | 0.824 | 0.903 | 0.326 |

By source, at the 0.5 threshold (FPR = safe flagged, DR = attacks caught):

| source | v2-l6 | v3-l6 | v3-l6-s1 |
|---|---|---|---|
| gretel-sql (in-domain, all safe) FPR | 0.788 | **0.002** | **0.002** |
| spider (val, all safe) FPR | 0.549 | **0.000** | **0.000** |
| sqli-queries (held-out) FPR / DR | 0.413 / 0.999 | **0.203** / 0.993 | **0.159** / 0.995 |
| sqli-queries AUROC | 0.992 | 0.988 | 0.996 |
| dvwa-juiceshop AUROC | 0.975 | 0.852 | 0.956 |
| waf-v2 (val) AUROC | 0.885 | 0.875 | 0.867 |
| waf-v2 FPR / DR | 0.398 / 0.909 | 0.451 / 0.893 | 0.477 / 0.898 |

- **Benign SQL is fixed.** False alarms on benign SQL drop to ~0 on both gretel and the
  unseen, human-written Spider, and halve on held-out sqli-queries, while SQLi detection at
  0.5 stays at 0.99.
- **Small cost on waf-v2 web requests:** AUROC 0.885 → 0.867–0.875. The three v2-l6 runs
  scored 0.882–0.885 there, so the ~0.01–0.02 drop looks real, not noise.
- **Pooled numbers mislead.** Val AUROC rises mainly because Spider is now scored safe. The
  pooled held-out DR@1%FPR swings 0.03 ↔ 0.82 between seeds (a few confidently flagged safe
  examples decide the 1% threshold), and dvwa-juiceshop AUROC 0.852 ↔ 0.956. Read
  per-source numbers.
- **Working model: v3-l6 (seed 0)**, picked by val AUROC (0.909 vs 0.903), not by held-out.
- One pass: val picks threat-only for both (v3-l6: 0.910 vs safe-only 0.893). Held-out again
  favoured safe-only (0.980 vs 0.928): the same split as with v2.

### v3-l6 on ONNX (2026-09-29)

`onnx_cpu.py --save` (two-pass and `--one-pass`) wrote `model.onnx`, `model.int8.onnx` and
their calibration files into `runs/cyber-jev-v3-l6`. `results/onnx_v3_l6*.md`,
`results/latency_v3-l6_onnx.md`:

| path | in-domain AUROC | held-out AUROC (3000 sample) | median ms | p95 ms |
|---|---|---|---|---|
| two-pass, ONNX int8 | 0.997 | 0.951 | 7.05 | 22.8 |
| one-pass, ONNX int8 | 0.995 | 0.934 | 3.90 | 13.6 |
| **Decider, one-pass, ONNX int8** (3 runs) | | | **3.77–3.97** | 12.3–12.8 |
| Decider, one-pass, PyTorch | | | 9.58 | 16.1 |

int8 costs no accuracy. On val the int8 Decider scores AUROC 0.914 (PyTorch 0.910), waf-v2
0.883, and still flags **0** Spider queries. Latency ≤ 5 ms holds with the v3 model.
One-pass costs held-out AUROC here (0.934 vs 0.951 two-pass on the sample), within the
noise seen across seeds, and val picked it.
