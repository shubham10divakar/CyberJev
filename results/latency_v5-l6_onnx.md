## Latency — Decider, `runs/cyber-jev-v5-l6` (joint), one pass, CPU 8 threads, batch 1, 300 inputs per decision

Three runs with backend auto (ONNX int8, calibration from `one_pass.model.int8.json`), one with `--backend torch`. 2026-09-29.

| decision | run | backend | median ms | p95 ms |
|---|---|---|---|---|
| http_attack | run1 | onnx:model.int8.onnx | 4.05 | 13.22 |
| http_attack | run2 | onnx:model.int8.onnx | 3.76 | 11.93 |
| http_attack | run3 | onnx:model.int8.onnx | 3.99 | 13.68 |
| http_attack | torch | torch | 9.50 | 15.71 |
| prompt_injection | run1 | onnx:model.int8.onnx | 2.47 | 18.07 |
| prompt_injection | run2 | onnx:model.int8.onnx | 2.29 | 17.41 |
| prompt_injection | run3 | onnx:model.int8.onnx | 2.39 | 18.19 |
| prompt_injection | torch | torch | 7.70 | 20.17 |
| phishing_url | run1 | onnx:model.int8.onnx | 1.89 | 3.59 |
| phishing_url | run2 | onnx:model.int8.onnx | 1.82 | 3.66 |
| phishing_url | run3 | onnx:model.int8.onnx | 1.86 | 3.86 |
| phishing_url | torch | torch | 7.28 | 9.61 |
