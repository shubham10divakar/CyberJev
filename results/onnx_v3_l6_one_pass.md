## CPU inference — `runs/cyber-jev-v3-l6`, 8 threads, max_length 256, held-out sample 3000, one pass

| variant | size MB | in-domain AUROC | in-domain DR@1%FPR | held-out AUROC | held-out DR@1%FPR | median ms | p95 ms |
|---|---|---|---|---|---|---|---|
| PyTorch fp32 | 87 | 0.995 | 0.968 | 0.928 | 0.023 | 8.53 | 14.87 |
| ONNX fp32 | 87 | 0.995 | 0.968 | 0.928 | 0.023 | 5.38 | 15.43 |
| ONNX int8 | 22 | 0.995 | 0.966 | 0.934 | 0.049 | 3.90 | 13.64 |
