## Latency — Decider, `runs/cyber-jev-v3-l6`, http_attack, 300 requests, one pass, CPU 8 threads, batch 1

Three runs of `scripts/bench_latency.py --no-gpu --threads 8` (backend auto → ONNX int8,
calibration from `one_pass.model.int8.json`), one with `--backend torch`. 2026-09-29.

| backend | run | median ms | p95 ms |
|---|---|---|---|
| ONNX int8 | 1 | 3.97 | 12.32 |
| ONNX int8 | 2 | 3.82 | 12.30 |
| ONNX int8 | 3 | 3.77 | 12.76 |
| PyTorch fp32 | 1 | 9.58 | 16.05 |

Decider on the validation set (`data_val/val.jsonl`, one pass, CPU):

| backend | val AUROC | waf-v2 AUROC | waf-v2 FPR@0.5 | waf-v2 DR@0.5 | spider FPR@0.5 |
|---|---|---|---|---|---|
| ONNX int8 | 0.914 | 0.883 | 0.251 | 0.875 | 0.000 |
| PyTorch fp32 | 0.910 | 0.876 | 0.376 | 0.883 | 0.000 |
