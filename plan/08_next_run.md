# 08 — Next run (written 2026-09-28, updated 2026-09-29)

Start here. Full numbers are in `07_status.md`; data details in `03_data.md`.

## Where things stand

- **Working model: `runs/cyber-jev-v3-l6`** (data v3, since 2026-09-29; see step 3 below).
  Before that: `runs/cyber-jev-v2-l6` (6 layers, from Nano-Jev v0.1 =
  `../nano_jev/runs/nano-jev-v0.1`). Trained on data v2, 4 epochs (best epoch 3), max_length 256.
  In-domain AUROC 0.995, held-out AUROC 0.953. Also has `model.onnx` and `model.int8.onnx`.
- `runs/cyber-jev-v2` (12 layers, from Nano-Jev v1.0): same in-domain, worse held-out (0.881).
- `runs/cyber-jev-dev`: the M1 model (CSIC only); kept only for comparison.
- CPU latency (8 threads, batch 1, median), one pass, v3-l6: Decider on ONNX int8 **3.8–4.0 ms**
  (v2-l6: 4.3–4.5); PyTorch 9.6 ms. v2-l6 via onnx_cpu.py: PyTorch 8.7 ms, ONNX int8 4.2 ms
  (two passes: 12.7 / 8.1). Target ≤ 5 ms met with ONNX int8; the Decider uses it on CPU (4.3–4.5 ms end to end).
  `one_pass.json` and the ONNX calibration files are in the run folder.
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
- ✅ **Decider on ONNX** (done 2026-09-29). On CPU the Decider now loads `model.int8.onnx`
  with its own calibration (`one_pass.model.int8.json`): **4.3–4.5 ms** median over three
  runs, p95 ~13 ms (PyTorch 9.8 ms). `results/latency_v2-l6_onnx.md`. Latency varies run to
  run by up to ~1.5 ms with other programs open: one `onnx_cpu.py` rerun gave 5.6 ms.

### 2. ✅ Second seed (done 2026-09-29)

6-layer lead confirmed (held-out 0.953 / 0.944 vs 12-layer 0.881 / 0.864); 3 epochs worse
(0.905). Held-out varies a lot run to run (DR@1%FPR 0.26–0.46). Safe-only one-pass beat
threat-only held-out on all three 6-layer runs (threat-only as low as 0.847), though calib NLL
always picked threat-only. Details in `07_status.md`. Next: confirm safe-only on the
out-of-domain validation set (3b). **Settled:** val picks threat-only on all three runs, so
threat-only stays (`07_status.md`).

### 3. ✅ Hard benign negatives (done 2026-09-29: data v3, working model now `runs/cyber-jev-v3-l6`)

Benign-SQL false alarms: Spider 0.55 → 0.00, held-out sqli-queries 0.41 → 0.20, SQLi detection
unchanged; small cost on waf-v2 requests (AUROC 0.885 → 0.875). Details in `07_status.md`.
✅ v3-l6 exported to ONNX with its own calibration: Decider **3.8–4.0 ms** CPU median,
Spider false alarms still 0 on int8. Left open: look at why waf-v2 dropped (what normal
requests are now flagged).

### 3 (original note)

Both models flag benign SQL queries (sqli-queries FPR@0.5: 0.41 for v2-l6) even though the
ranking is good (AUROC 0.99). Add benign SQL-like / code-like text to **training** from a
source that isn't the held-out one (e.g. a text-to-SQL dataset such as Spider or WikiSQL
queries, labelled safe), then re-check held-out FPR. Don't train on `zrmarine/sql_injection`:
it's held-out.

### 3b. ✅ Out-of-domain validation set (done 2026-09-29: `data_val/`, see `03_data.md`)

Calib is in-domain and held-out is test-only, so there's nothing to make out-of-domain
choices on (threat-only vs safe-only, thresholds). Add a small `data_val/` from a source that
is neither training nor held-out, used only for such choices. Also look for a harder held-out
web-request source: `dvwa-juiceshop` can be separated by path alone.

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
