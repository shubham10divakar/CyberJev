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

## M3 — data v4 baselines (2026-09-29)

`scripts/baselines.py` on the two new decisions (`results/tfidf_v4*.md`, `results/length_v4*.md`;
`--length` = text length alone). AUROC, calibrated on v4 calib; destroylist is phishing-only,
so its column is the share caught at 0.5.

| decision | set | TF-IDF + LR | length only |
|---|---|---|---|
| prompt_injection | in-domain (S-Labs, neuralchemy) | 0.992 | 0.579 |
| | held-out deepset | 0.904 | 0.813 |
| | held-out jackhhao | 0.952 | **0.868** |
| | **val (in-the-wild, length-matched)** | **0.740** | 0.502 |
| phishing_url | in-domain (flwrlabs) | 0.960 | 0.544 |
| | held-out PhishTrap | 0.780 | **0.861** |
| | held-out destroylist (DR@0.5) | 0.354 | 0.093 |
| | **val (JPxxx)** | **0.927** | 0.660 |

- **Held-out is length-flattered for both new decisions.** On PhishTrap, length alone beats
  TF-IDF (0.861 vs 0.780); on jackhhao it gets 0.868. Every held-out result for these
  decisions must be read next to the length baseline.
- **Val is the harder, cleaner check:** in-the-wild prompts have no length signal and TF-IDF
  only reaches 0.740; JPxxx is closer to training (TF-IDF 0.927).
- In-domain is easy for TF-IDF (0.96–0.99), as it was for http_attack. The M4 model has to
  beat TF-IDF out of domain, where M2 showed the cross-encoder's advantage.

## M4 — joint model on all three decisions, seed 0 (2026-09-29)

`bash scripts/m4_runs.sh 0`: 6-layer from Nano-Jev v0.1, data v4, 4 epochs, best epoch by dev
NLL. Joint `v4-l6` (44.9k examples, 172 s/epoch, best epoch 2) vs single-decision models
(`v3-l6` for http, `v4-l6-pi` best epoch 2, `v4-l6-url` best epoch 1: dev NLL rose after).
AUROC, two-pass, calibrated (in-domain / held-out / val):

| decision | model | in-domain | held-out | val |
|---|---|---|---|---|
| http_attack | **joint v4-l6** | 0.994 | **0.956** | **0.911** |
| | single v3-l6 | 0.997 | 0.949 | 0.909 |
| prompt_injection | **joint v4-l6** | 0.995 | 0.766 | 0.676 |
| | single v4-l6-pi | 0.993 | 0.715 | 0.558 |
| | TF-IDF | 0.992 | **0.887** | **0.740** |
| | length only | 0.579 | 0.798 | 0.502 |
| | zero-shot (v3-l6) | 0.786 | 0.493 | 0.651 |
| phishing_url | **joint v4-l6** | 0.966 | 0.798 | **0.940** |
| | single v4-l6-url | 0.958 | **0.814** | 0.935 |
| | TF-IDF | 0.960 | 0.710 | 0.927 |
| | length only | 0.544 | 0.800 | 0.660 |

By source (held-out; FPR / DR at 0.5):

| source | joint | single | TF-IDF | length |
|---|---|---|---|---|
| dvwa-juiceshop AUROC (FPR) | **0.961** (0.14) | 0.852 (0.31) | | |
| sqli-queries AUROC (FPR) | 0.988 (0.23) | 0.988 (0.20) | | |
| waf-v2 (val) AUROC (FPR) | 0.878 (**0.16**) | 0.875 (0.45) | | |
| deepset AUROC | 0.835 | 0.725 | **0.904** | 0.813 |
| jackhhao AUROC (FPR) | 0.727 (0.72) | 0.714 (0.76) | **0.952** (0.61) | 0.868 (0.96) |
| phishtrap AUROC | 0.844 | **0.862** | 0.780 | 0.861 |
| destroylist DR@0.5 | 0.57 | 0.58 | 0.55 | 0.10 |

One pass (`results/single_pass_v4_l6*.md`), AUROC held-out / val:

| decision | two-pass | threat-only | safe-only | val picks |
|---|---|---|---|---|
| http_attack (joint) | 0.956 / 0.911 | 0.951 / 0.907 | 0.956 / 0.912 | safe-only (by 0.005) |
| prompt_injection (joint) | 0.766 / 0.676 | **0.861 / 0.749** | 0.672 / 0.578 | threat-only |
| phishing_url (joint) | 0.798 / 0.940 | 0.789 / 0.937 | 0.802 / 0.939 | safe-only |

**Findings (one seed):**
- **Joint ≥ single.** http_attack is as good or better (dvwa 0.852 → 0.961, waf-v2 FPR@0.5
  0.45 → 0.16); prompt_injection gains a lot from joint training (held-out +0.05, val +0.12);
  phishing_url is within ~0.02. The plan's M4 bar (joint within ~1 point) is met or beaten.
- **prompt_injection does not generalise yet.** Out of domain it is below TF-IDF (held-out
  0.766 vs 0.887, val 0.676 vs 0.740) and flags 72% of jackhhao's benign role-play personas.
  Its one-pass threat-only score is much better (0.861 / 0.749, level with TF-IDF on val):
  the "safe" logit is what breaks out of domain. Likely causes: short, templated training
  prompts (median ~50 chars; S-Labs "reveal your guidelines" patterns) vs long in-the-wild
  prompts, and the 256-token cut. Same story as http_attack M1 → data diversity problem.
- **phishing_url beats TF-IDF but not length on PhishTrap** (0.844–0.862 vs length 0.861);
  on val it is best (0.940). The URL model overfits fast (best epoch 1).
- The val-picked one-pass variant differs per decision and model now (safe-only for http and
  URL on the joint model), so one_pass.json is per decision, as built.

## Data v5 — joint `v5-l6`, seed 0 (2026-09-29)

`bash scripts/m4_runs.sh 0 v5 joint`: same recipe as v4-l6 on data v5 (50.0k examples,
215 s/epoch, best epoch 2 by dev NLL 0.131). TF-IDF refitted on v5 for a fair comparison.
AUROC, two-pass, calibrated:

| decision | set | joint v4-l6 | **joint v5-l6** | TF-IDF v5 | length only |
|---|---|---|---|---|---|
| prompt_injection | in-domain | 0.995 | 0.994 | — | — |
| | held-out | 0.766 | **0.829** | **0.880** | 0.798 |
| | · deepset | 0.835 | 0.747 | 0.859 | 0.813 |
| | · jackhhao (FPR@0.5) | 0.727 (0.72) | **0.870 (0.40)** | 0.939 (0.38) | 0.868 |
| | val (in-the-wild) | 0.676 | **0.813** | 0.791 | 0.502 |
| http_attack | held-out | 0.956 | 0.955 | | |
| | val (waf-v2 AUROC / FPR@0.5) | 0.911 (0.878 / 0.16) | **0.940 (0.919 / 0.10)** | | |
| phishing_url | held-out (PhishTrap) | 0.798 (0.844) | **0.817 (0.874)** | | 0.800 (0.861) |
| | val | 0.940 | 0.947 | | |

One pass, prompt_injection held-out / val: two-pass 0.829 / 0.813, threat-only 0.813 / 0.802,
safe-only 0.837 / **0.826**. Val now picks threat-only for http and URL, safe-only for PI.

**Findings (one seed):**
- **The long, length-matched data fixed most of the PI gap.** Val +0.14 (0.676 → 0.813), now
  above TF-IDF (0.791; one-pass 0.826). jackhhao false alarms on benign role-play 0.72 → 0.40.
- **Held-out PI is still below TF-IDF** (0.829 vs 0.880), because **deepset dropped**
  (0.835 → 0.747): deepset is short and partly German; all v5 additions are long English.
  jackhhao (0.870) is only level with length alone (0.868).
- **Other decisions did not suffer, and improved on val:** waf-v2 0.878 → 0.919, PhishTrap
  0.844 → 0.874 (now above length 0.861). Could be seed noise; needs seeds.
- Next for PI: short / multilingual variety (e.g. non-English benign and injection prompts
  from a non-held-out source), then seeds. WildJailbreak full (gated) would add many more
  long adversarial prompts on both sides.

## Data v6 — joint `v6-l6`, seed 0 (2026-09-29)

Same recipe on data v6 (52.4k examples, best epoch 2). AUROC, two-pass:

| decision | set | v5-l6 | v6-l6 | TF-IDF v6 |
|---|---|---|---|---|
| prompt_injection | held-out | 0.829 | 0.824 | 0.885 |
| | · deepset (FPR@0.5) | 0.747 (0.36) | **0.787 (0.28)** | 0.873 (0.03) |
| | · jackhhao | 0.870 | 0.848 | 0.942 |
| | val | 0.813 | 0.796 | 0.795 |
| http_attack | held-out / val | 0.955 / 0.940 | 0.982 / 0.907 | |
| phishing_url | held-out / val | 0.817 / 0.947 | 0.776 / 0.934 | |

- The short / non-English data moved deepset the intended way (+0.04, fewer false alarms).
- **http_attack moved ±0.03 with identical http data**, so one-run differences of this size
  are noise. Seeds 1 and 2 for both v5 and v6 are running (`DATA=data_v5 bash
  scripts/m4_runs.sh 1 v5 joint`, …); compare with `scripts/seed_summary.py`.

## Seeds 0–2: joint v5-l6 vs v6-l6 (2026-09-29)

`results/seeds_v5_v6.md` (`scripts/seed_summary.py`), calibrated AUROC, two-pass, mean ± std
over 3 seeds. TF-IDF (deterministic) for reference.

| decision | set | v5-l6 | v6-l6 | TF-IDF |
|---|---|---|---|---|
| http_attack | held-out | 0.962 ± 0.009 | 0.969 ± 0.015 | |
| | val | 0.915 ± 0.022 | 0.915 ± 0.007 | |
| phishing_url | held-out | **0.808 ± 0.012** | 0.782 ± 0.007 | 0.710 |
| | val | 0.944 ± 0.005 | 0.939 ± 0.005 | 0.927 |
| prompt_injection | held-out | 0.812 ± 0.026 | **0.839 ± 0.013** | **0.880 / 0.885** (v5 / v6) |
| | · deepset (FPR@0.5) | 0.755 ± 0.012 (0.39) | **0.823 ± 0.032 (0.19)** | 0.859 / 0.873 |
| | · jackhhao | 0.849 ± 0.033 | 0.856 ± 0.010 | 0.939 / 0.942 |
| | val | 0.799 ± 0.015 | 0.786 ± 0.010 | 0.791 / 0.795 |

**Pick by the fixed rule (mean val AUROC over decisions): v5** (0.886 vs 0.880). The
difference is within one std, so v5 and v6 are effectively tied on val.

- **v6 did what it was built for:** deepset +0.07 (> 2 std) and its false alarms halve
  (0.39 → 0.19). It is not used for the choice because held-out is test-only.
- **v6 costs phishing_url held-out** (0.808 → 0.782, ~2 std) with unchanged URL data:
  possible interference from the extra PI data, or noise.
- **Seed 0 was a lucky run for v5 PI val** (0.813 vs mean 0.799). Over seeds, **PI is level
  with TF-IDF on val and below it on held-out** (0.81–0.84 vs 0.88). phishing_url beats
  TF-IDF on both; http_attack is strong (no TF-IDF refit on v5/v6; v3 TF-IDF held-out 0.657).
- Run-to-run spread is large for some sources (dvwa ± 0.05, waf-v2 FPR ± 0.15): any paper
  table needs ≥ 3 seeds.

## Spot check: sample inputs through joint `v5-l6` (2026-09-29, CPU, PyTorch)

Clear cases are right with high confidence: SQLi / XSS / traversal → attack ≥ 0.999, benign
SQL → safe 0.997; "Ignore all previous instructions…" 0.999, German "Vergiss alle
vorherigen Anweisungen…" 0.96, DAN 0.998, "act as a travel guide" safe 0.99; lookalike /
IP / free-hosting phishing URLs ≥ 0.95. **Known issues found:**
1. **Benign search request borderline:** `GET /search?q=running+shoes&page=2` → attack 0.53.
2. **Legitimate URL on a free-hosting domain flagged:** `github.com/shubham10divakar/CyberJev`
   → phishing 0.93 (github.com / web.app user paths are common in phishing data).
   wikipedia.org → legitimate 0.74 only.
3. **`normalize_http` decodes `+` to a space everywhere**, also in raw (not URL-encoded)
   POST bodies: `'+document.cookie` became `' document.cookie`. Should only unquote_plus
   query strings / form-encoded bodies.

## PI truncation probes, data v5, seed 0 (2026-09-29)

`results/trunc_probes_v5.md`. AUROC, two-pass:

| decision | set | v5-l6 (head, 256) | v5ht-l6 (head_tail, 256) | v5ml512-l6 (head, 512) |
|---|---|---|---|---|
| prompt_injection | held-out | 0.829 | 0.828 | 0.799 |
| | · jackhhao | 0.870 | 0.867 | 0.820 |
| | · deepset | 0.747 | 0.756 | 0.765 |
| | val | 0.813 | 0.787 | 0.808 |
| http_attack | val (waf-v2 FPR@0.5) | 0.940 (0.10) | 0.922 (0.14) | 0.906 (0.27) |
| phishing_url | held-out / val | 0.817 / 0.947 | 0.821 / 0.946 | 0.814 / 0.947 |

**Neither helps** (both within or below v5's 3-seed range, PI val 0.799 ± 0.015), so they
did not get more seeds. Seeing the end of long prompts, or twice as much of them, does not
improve PI out of domain: **truncation is not the bottleneck.** 512 also costs ~1.3× training
time and up to 2× inference on long inputs. Keep head / 256. `head_tail` stays available
(`--truncation`) but is not the default.

What's left for PI points at the model or the labels rather than the input window:
TF-IDF still leads on held-out (0.88), i.e. lexical cues transfer across these datasets
better than what the 6-layer cross-encoder learns; and the datasets disagree on what counts
as an "injection" (jackhhao role-play jailbreaks vs deepset instruction overrides vs
in-the-wild prompts).

## v5-l6 (joint) on ONNX, per decision (2026-09-29)

`onnx_cpu.py` now works per decision; `--save` wrote `calibration.model*.json` and
`one_pass.model*.json` for all three decisions. `results/onnx_v5_l6*.md`,
`results/latency_v5-l6_onnx.md`. int8 costs no accuracy (held-out AUROC within ±0.007 of
PyTorch). **Decider, one pass, ONNX int8, CPU 8 threads, batch 1** (3 runs, median / p95):

| decision | ONNX int8 median | p95 | PyTorch median |
|---|---|---|---|
| http_attack | **3.8–4.1 ms** | 11.9–13.7 | 9.5 |
| prompt_injection | **2.3–2.5 ms** | 17.4–18.2 | 7.7 |
| phishing_url | **1.8–1.9 ms** | 3.6–3.9 | 7.3 |

All three meet ≤ 5 ms at the median. PI's p95 (~18 ms) comes from long prompts (256 tokens).
One pass vs two on the 3000 held-out sample (int8): http 0.942 vs 0.958, URL 0.807 vs 0.815,
PI 0.833 vs 0.822 — val picked these variants; the held-out cost for http is ~0.016.

## Paper items 5, 8, 9: plain classifier baseline, calibration, triage (2026-09-29)

### Plain classifier vs joint cross-encoder (3 seeds each, data v5)

`scripts/train_plain.py`: same 6-layer backbone and recipe, **input text only** (no question /
option), fresh 2-class head, one model per decision. `results/seeds_joint_vs_plain_v5.md`.
AUROC mean ± std:

| decision | set | joint v5-l6 | plain (per decision) |
|---|---|---|---|
| http_attack | held-out | 0.962 ± 0.009 | 0.964 ± 0.021 |
| | val | 0.915 ± 0.022 | 0.905 ± 0.017 |
| | FPR@0.5 dvwa / waf-v2 | **0.42 / 0.28** | 0.60 / 0.42 |
| prompt_injection | held-out | **0.812 ± 0.026** | 0.760 ± 0.018 |
| | val | **0.799 ± 0.015** | 0.748 ± 0.014 |
| phishing_url | held-out | 0.808 ± 0.012 | **0.823 ± 0.005** |
| | val | 0.944 ± 0.005 | 0.943 ± 0.002 |

- **The typed-decision joint model clearly beats a plain classifier on prompt_injection**
  (+0.05 held-out and val, > 2 std), ties on http_attack (with fewer false alarms at 0.5),
  and is slightly behind on phishing_url held-out (−0.015). Caveat: joint vs plain changes
  two things at once (question/option input and multi-task training); a single-decision
  cross-encoder on v5 would separate them.

### Calibration and triage (Decider path, one pass; 3 seeds)

`scripts/calibration_report.py` → `results/calibration_v5_l6*.{md,json,png}` (reliability
diagram and risk-coverage curve per decision). Policy: block ≥ 0.9, allow ≤ 0.2, else review.
Mean over 3 seeds:

| decision | set | ECE | reviewed | error on auto-decided | error, review 0% → 20% most uncertain |
|---|---|---|---|---|---|
| http_attack | in-domain | 0.024 | 11% | 1.1% | 4.2% → 0.5% |
| | held-out | 0.106 | 15% | 8.9% | 14.9% → 8.3% |
| | val | 0.102 | 20% | 12.1% | 16.1% → 11.4% |
| phishing_url | in-domain | 0.027 | 22% | 4.0% | 10.2% → 4.3% |
| | held-out | 0.121 | 38% | 18.0% | 25.1% → 20.0% |
| | val | 0.062 | 23% | 6.7% | 13.3% → 8.1% |
| prompt_injection | in-domain | 0.017 | 6% | 2.4% | 3.9% → 0.7% |
| | held-out | 0.220 | 21% | 24.2% | 28.9% → 25.6% |
| | val | 0.174 | 31% | 20.0% | 27.8% → 23.8% |

- **Calibrated in domain, not out of domain.** In-domain ECE 0.02–0.03; out of domain
  0.06–0.22. The temperature fitted on in-domain calib does not transfer: on http held-out
  the model is over-confident about attacks (false blocks at 0.9: 13.8% of safe requests on
  average, up to 22%), on http val it under-predicts them (missed threats 15.6%).
- **Uncertainty still ranks errors out of domain:** sending the 20% most uncertain to review
  roughly halves http errors (held-out 14.9 → 8.3%, val 16.1 → 11.4%) and URL val errors
  (13.3 → 8.1%). For PI the gain is small (28.9 → 25.6%), consistent with PI being weak.
- **Paper framing:** "calibrated probabilities" hold in domain; out of domain the probability
  *ranking* supports triage but thresholds need recalibration on target-like data. Next test:
  fit the calibration on `data_val` (out-of-domain, never test) and re-check held-out ECE.
