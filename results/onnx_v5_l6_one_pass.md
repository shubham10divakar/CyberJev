## CPU inference — `runs/cyber-jev-v5-l6`, 8 threads, max_length 256, held-out sample ≤ 3000 per decision, one pass

| decision | variant | size MB | in-domain AUROC | held-out AUROC | held-out DR@1%FPR | median ms | p95 ms |
|---|---|---|---|---|---|---|---|
| http_attack | PyTorch fp32 | 87 | 0.995 | 0.940 | 0.575 | 8.81 | 15.11 |
| phishing_url | PyTorch fp32 | 87 | 0.963 | 0.803 | 0.125 | 6.18 | 8.25 |
| prompt_injection | PyTorch fp32 | 87 | 0.992 | 0.837 | 0.082 | 6.75 | 19.20 |
| http_attack | ONNX fp32 | 87 | 0.995 | 0.940 | 0.575 | 5.44 | 15.89 |
| phishing_url | ONNX fp32 | 87 | 0.963 | 0.803 | 0.125 | 2.65 | 5.02 |
| prompt_injection | ONNX fp32 | 87 | 0.992 | 0.837 | 0.082 | 3.44 | 21.97 |
| http_attack | ONNX int8 | 22 | 0.994 | 0.942 | 0.568 | 3.73 | 12.68 |
| phishing_url | ONNX int8 | 22 | 0.963 | 0.807 | 0.112 | 1.87 | 3.59 |
| prompt_injection | ONNX int8 | 22 | 0.991 | 0.833 | 0.066 | 2.30 | 17.72 |
