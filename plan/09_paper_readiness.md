# 09 — Paper readiness checklist (written 2026-09-29)

Claim to support: *one small, calibrated, typed-decision cross-encoder handles several
application-layer security checks at CPU speed, and generalises out of domain better than
standard baselines, with calibrated probabilities that make a block / review / allow
policy work.*

Status: ✅ done · ⚠️ partial · ❌ not started

| # | Needed | Status | Notes |
|---|---|---|---|
| 1 | Model for all three decisions (M4, joint) | ⚠️ seed 0 | `v5-l6`: http ✅, URL ✅, PI above TF-IDF on val (0.813 vs 0.791) but **below on held-out** (0.829 vs 0.880, deepset) |
| 2 | Joint vs single-decision models | ⚠️ seed 0 | joint ≥ single (PI +0.05 / +0.12); needs seeds |
| 3 | ≥ 3 seeds per setup, mean ± std | ⚠️ | 2 seeds for http (v2-l6, v3-l6); held-out varies a lot (AUROC 0.905–0.953, DR@1%FPR 0.03–0.82) |
| 4 | Baselines: TF-IDF + LR, length only | ✅ | `results/tfidf*`, `results/length_v4*` |
| 5 | Baseline: plain fine-tuned classifier, same backbone, no question / option text | ❌ | shows whether the typed-decision format helps |
| 6 | Baseline: one public detector per decision | ❌ | e.g. an open prompt-injection classifier; a URL / WAF model; check licences |
| 7 | Out-of-domain protocol: held-out + separate val, overlap and shortcut checks | ✅ | `03_data.md`; val only for choices |
| 8 | Calibration: ECE per set, reliability diagrams | ⚠️ | ECE in every table; no diagrams |
| 9 | Triage / cascade result: share sent to review vs error on the rest | ❌ | the stated product (01_goal) |
| 10 | Ablations: one vs two pass, data v2 → v3, 6 vs 12 layers, path balancing | ⚠️ | first three done (`07_status.md`) |
| 11 | Latency: CPU / GPU, ONNX int8 | ✅ | 3.8–4.0 ms CPU median (v3-l6) |
| 12 | Limitations: length shortcuts, merged public datasets, licences, dvwa path confound | ✅ recorded | write up |
| 13 | Dataset hygiene findings as a contribution (duplicated / shortcut-laden public sets) | ⚠️ | findings in `03_data.md`; needs a table |
| 14 | Release weights / code for reproducibility | ❌ | only when asked (M7) |

Blocking for a paper now: **prompt_injection held-out** (below TF-IDF, mainly deepset: short / German). v5 fixed val.

Order: M4 (1, 2) → PI data diversity → seeds (3) → baselines (5, 6) → calibration and triage (8, 9) → write.
After 9 it's enough for a workshop paper; a main-conference paper also needs 5 and 6 to hold
up clearly out of domain.
