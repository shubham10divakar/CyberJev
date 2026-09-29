## Latency — Decider, `runs/cyber-jev-v2-l6`, http_attack, 300 requests, one pass, CPU 8 threads, batch 1

Three runs of `scripts/bench_latency.py --no-gpu --threads 8` (backend auto → ONNX int8,
calibration from `one_pass.model.int8.json`), one with `--backend torch`. 2026-09-29.

| backend | run | median ms | p95 ms |
|---|---|---|---|
| ONNX int8 | 1 | 4.27 | 12.67 |
| ONNX int8 | 2 | 4.46 | 12.71 |
| ONNX int8 | 3 | 4.55 | 13.84 |
| PyTorch fp32 | 1 | 9.77 | 16.37 |
