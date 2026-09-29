## CPU inference — `runs/cyber-jev-v2-l6`, 8 threads, max_length 256, held-out sample 3000, one pass

| variant | size MB | in-domain AUROC | in-domain DR@1%FPR | held-out AUROC | held-out DR@1%FPR | median ms | p95 ms |
|---|---|---|---|---|---|---|---|
| PyTorch fp32 | 87 | 0.990 | 0.968 | 0.950 | 0.455 | 8.68 | 15.30 |
| ONNX fp32 | 87 | 0.990 | 0.968 | 0.950 | 0.455 | 5.26 | 16.00 |
| ONNX int8 | 22 | 0.989 | 0.963 | 0.950 | 0.477 | 4.15 | 13.20 |
