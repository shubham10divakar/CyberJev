## CPU inference — `runs/cyber-jev-v2-l6`, 8 threads, max_length 256, held-out sample 3000, one pass

| variant | size MB | in-domain AUROC | in-domain DR@1%FPR | held-out AUROC | held-out DR@1%FPR | median ms | p95 ms |
|---|---|---|---|---|---|---|---|
| PyTorch fp32 | 87 | 0.990 | 0.968 | 0.950 | 0.455 | 8.84 | 16.53 |
| ONNX fp32 | 87 | 0.990 | 0.968 | 0.950 | 0.455 | 7.83 | 21.12 |
| ONNX int8 | 22 | 0.989 | 0.963 | 0.950 | 0.477 | 5.63 | 15.50 |
