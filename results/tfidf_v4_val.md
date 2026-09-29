## TF-IDF + LR on `data_val/val.jsonl`

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| phishing_url | 3000 | 0.89 | 0.860 | 0.860 | 0.927 | 0.436 | 0.173 | 0.340 → 0.341 | 0.211 → 0.211 | 0.016 → 0.018 | 0.1 |
| prompt_injection | 1500 | 0.71 | 0.561 | 0.484 | 0.740 | 0.089 | 0.011 | 1.238 → 1.652 | 0.695 → 0.751 | 0.328 → 0.358 | 3.7 |
