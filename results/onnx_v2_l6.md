## CPU inference — `runs/cyber-jev-v2-l6`, 8 threads, max_length 256, held-out sample 3000

| variant | size MB | in-domain AUROC | in-domain DR@1%FPR | held-out AUROC | held-out DR@1%FPR | median ms | p95 ms |
|---|---|---|---|---|---|---|---|
| PyTorch fp32 | 87 | 0.995 | 0.968 | 0.958 | 0.517 | 12.71 | 24.95 |
| ONNX fp32 | 87 | 0.995 | 0.968 | 0.958 | 0.517 | 11.03 | 29.44 |
| ONNX int8 | 22 | 0.995 | 0.966 | 0.960 | 0.495 | 8.06 | 23.35 |
