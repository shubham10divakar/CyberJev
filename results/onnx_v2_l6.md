## CPU inference — `runs/cyber-jev-v2-l6`, 8 threads, max_length 256, held-out sample 3000, two passes

| variant | size MB | in-domain AUROC | in-domain DR@1%FPR | held-out AUROC | held-out DR@1%FPR | median ms | p95 ms |
|---|---|---|---|---|---|---|---|
| PyTorch fp32 | 87 | 0.995 | 0.968 | 0.958 | 0.517 | 13.64 | 26.46 |
| ONNX fp32 | 87 | 0.995 | 0.968 | 0.958 | 0.517 | 12.07 | 32.09 |
| ONNX int8 | 22 | 0.995 | 0.966 | 0.960 | 0.495 | 7.98 | 23.54 |
