## CPU inference — `runs/cyber-jev-v5-l6`, 8 threads, max_length 256, held-out sample ≤ 3000 per decision, two passes

| decision | variant | size MB | in-domain AUROC | held-out AUROC | held-out DR@1%FPR | median ms | p95 ms |
|---|---|---|---|---|---|---|---|
| http_attack | PyTorch fp32 | 87 | 0.995 | 0.956 | 0.674 | 13.16 | 26.25 |
| phishing_url | PyTorch fp32 | 87 | 0.966 | 0.812 | 0.170 | 8.27 | 12.73 |
| prompt_injection | PyTorch fp32 | 87 | 0.994 | 0.829 | 0.165 | 8.91 | 33.86 |
| http_attack | ONNX fp32 | 87 | 0.995 | 0.956 | 0.674 | 10.09 | 28.56 |
| phishing_url | ONNX fp32 | 87 | 0.966 | 0.812 | 0.170 | 4.74 | 9.14 |
| prompt_injection | ONNX fp32 | 87 | 0.994 | 0.829 | 0.165 | 5.83 | 41.22 |
| http_attack | ONNX int8 | 22 | 0.995 | 0.958 | 0.665 | 7.44 | 24.99 |
| phishing_url | ONNX int8 | 22 | 0.966 | 0.815 | 0.155 | 3.31 | 6.63 |
| prompt_injection | ONNX int8 | 22 | 0.993 | 0.822 | 0.126 | 3.96 | 33.91 |
