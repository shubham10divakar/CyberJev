# 08 — Next run (written 2026-09-28, updated 2026-09-29)

Start here. Full numbers are in `07_status.md`; data details in `03_data.md`.

## Where things stand

- **Working model: `runs/cyber-jev-v2-l6`** (6 layers, from Nano-Jev v0.1 =
  `../nano_jev/runs/nano-jev-v0.1`). Trained on data v2, 4 epochs (best epoch 3), max_length 256.
  In-domain AUROC 0.995, held-out AUROC 0.953. Also has `model.onnx` and `model.int8.onnx`.
- `runs/cyber-jev-v2` (12 layers, from Nano-Jev v1.0): same in-domain, worse held-out (0.881).
- `runs/cyber-jev-dev`: the M1 model (CSIC only); kept only for comparison.
- CPU latency (8 threads, batch 1, median), one pass: PyTorch 8.7 ms, ONNX int8 **4.2 ms**
  (two passes: 12.7 / 8.1). Target ≤ 5 ms met with ONNX int8. `one_pass.json` is in the run folder.
- Weights are in `runs/` (git-ignored, local only). Nothing is pushed to HF or PyPI.
- `data/` and `data_heldout/` are committed; rebuild with `python scripts/prepare_data.py`.

## Machine limits (this desktop)

Ryzen 7 5800X (8 cores / 16 threads), RTX 3060 12 GB, 16 GB RAM (about 5–7 GB free with a
browser open). Enough for everything planned; the models are small (22M parameters).

- Run **one heavy job at a time**. Don't train on the GPU while a CPU benchmark runs (it skews
  timings), and keep one model per process: an all-in-one ONNX run was stopped once for low
  memory.
- Close Firefox for long runs if memory is tight.
- Use `python -u` when logging to a file, or the log stays empty until the end.
- Windows console: set `PYTHONIOENCODING=utf-8` (tables use →).
- Timings: 6-layer training ≈ 1.5 min/epoch on 21.5k examples; 12-layer ≈ 2.8 min/epoch;
  `onnx_cpu.py` ≈ 8–10 min for all three variants.

## Next steps, in order

### 1. ✅ One encoder pass per binary decision (done 2026-09-29, option b)

Inference-only: `scripts/single_pass.py --save` writes `one_pass.json`; the Decider uses it.
ONNX int8 CPU median **4.2 ms** (target ≤ 5), held-out AUROC 0.945–0.950 vs 0.953. Details in
`07_status.md`. Left open:

- **Threat-only vs safe-only.** Calib NLL picked threat-only; safe-only is better on every
  held-out metric (AUROC 0.958, DR@1%FPR 0.572). Settle it with step 2's second seed and/or a
  separate out-of-domain *validation* set, not the held-out test.
- **Decider on ONNX.** The ≤ 5 ms is ONNX int8 in `onnx_cpu.py`; the Decider still runs
  PyTorch (9.6 ms CPU). Add an ONNX int8 backend to the Decider (load `model.int8.onnx` when
  present, `onnxruntime` as an optional extra).

### 2. Second seed

Retrain `v2` and `v2-l6` with `--seed 1` to confirm the 6-layer model's held-out lead
(0.953 vs 0.881) is not noise. Also try `--epochs 3`, since epoch 4 was worse for both.

### 3. Hard benign negatives

Both models flag benign SQL queries (sqli-queries FPR@0.5: 0.41 for v2-l6) even though the
ranking is good (AUROC 0.99). Add benign SQL-like / code-like text to **training** from a
source that isn't the held-out one (e.g. a text-to-SQL dataset such as Spider or WikiSQL
queries, labelled safe), then re-check held-out FPR. Don't train on `zrmarine/sql_injection`:
it's held-out.

### 4. Then M3: `prompt_injection` and `phishing_url`

Verify the candidate datasets listed in `03_data.md` (existence, size, labels, licence),
add builders to `cyberjev/data.py`, and give each a held-out source from a different origin.

## Open issues to remember

- Licences: `shengqin/web-attacks`, `zrmarine/sql_injection` and `vyykaaa/dataset-web-attack`
  state none. They're fine for research evaluation; check before any release that ships them.
- `dvwa-juiceshop` held-out can be partly separated by path (attacks mostly on DVWA, normal
  all on Juice Shop), so its AUROC flatters every model.
- `ai-waf` looks synthetic (TF-IDF AUROC 1.000). It adds variety to safe traffic, not
  difficulty; CSIC is the informative in-domain source.
- max_length 128 was tested and rejected (it truncates payloads in full requests).
- p95 latency (~23 ms) is set by long requests. After step 1, look at the p95 again.
