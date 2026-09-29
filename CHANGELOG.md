# Changelog

## 0.1.0 (2026-09-29)

- First PyPI release as **`cyberjev`** (`pip install cyberjev`). Command `cyberjev`
  (`cyber-jev` still works).
- Default weights `v0.1` are downloaded from Hugging Face (`sdmlai/cyber-jev`) on first use.

## Weights v0.1 (2026-09-29)

- Published on Hugging Face: [`sdmlai/cyber-jev`](https://huggingface.co/sdmlai/cyber-jev),
  tag `v0.1`, CC-BY-NC-4.0. Joint model for `http_attack`, `prompt_injection` and
  `phishing_url` (data v5, 6 layers, 22.7M parameters) with int8 ONNX and per-decision
  calibration; the package default `v0.1` now resolves to it.

## 0.1.0.dev0

- Forked from Nano-Jev 1.0.0: same model, calibration, registry and CLI; package renamed
  `cyberjev`, command `cyber-jev`, settings in `~/.cyberjev`, env vars `CYBERJEV_*`.
- New schema: `http_attack`, `prompt_injection`, `phishing_url` (replaces relevance /
  sufficient / grounded). Built-in methods take one string or a list.
- `http_attack` data v2: trains on CSIC 2010 + `shengqin/web-attacks` + `notesbymuneeb/ai-waf-dataset`;
  held-out set from `zrmarine/sql_injection` and `vyykaaa/dataset-web-attack` (was: CSIC only,
  held-out `shengqin/web-attacks` test). `prepare_data.py` builds both in one run.
- `normalize_http` handles full requests: drops content-negotiation headers, keeps headers
  that can carry payloads, strips scheme and host.
- Reports add a per-source breakdown (AUROC, and FPR / detection rate at the 0.5 threshold).
- Metrics add AUROC and detection rate at 1% / 0.1% false-positive rate.
- `scripts/baselines.py` is now a TF-IDF + logistic-regression baseline;
  new `scripts/bench_latency.py`.
- One encoder pass for built-in binary decisions: when the model folder has `one_pass.json`
  (written by `scripts/single_pass.py --save`), the Decider scores one option and returns
  `sigmoid((sign·z − shift) / T)`; custom option sets still score every option. New
  `fit_threat_only` in `cyberjev.calibration`. `bench_latency.py --two-pass` and
  `onnx_cpu.py --one-pass` compare the two paths.
- ONNX Runtime backend: on CPU the Decider uses `model.int8.onnx` / `model.onnx` when present
  and `onnxruntime` is installed (`backend="auto"`; also `"torch"`, `"onnx"`), with
  calibration fitted on that file (`calibration.<file>.json`, `one_pass.<file>.json`, written
  by `onnx_cpu.py --save`). New extras `onnx` and `export`.
