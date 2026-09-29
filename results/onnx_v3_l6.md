## CPU inference — `runs/cyber-jev-v3-l6`, 8 threads, max_length 256, held-out sample 3000, two passes

| variant | size MB | in-domain AUROC | in-domain DR@1%FPR | held-out AUROC | held-out DR@1%FPR | median ms | p95 ms |
|---|---|---|---|---|---|---|---|
| PyTorch fp32 | 87 | 0.997 | 0.968 | 0.947 | 0.035 | 13.98 | 28.21 |
| ONNX fp32 | 87 | 0.997 | 0.968 | 0.947 | 0.035 | 9.72 | 29.27 |
| ONNX int8 | 22 | 0.997 | 0.967 | 0.951 | 0.087 | 7.05 | 22.76 |
