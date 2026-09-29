## Length only on `data_val/val.jsonl`

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| phishing_url | 3000 | 0.86 | 0.654 | 0.653 | 0.660 | 0.000 | 0.000 | 0.675 → 0.673 | 0.482 → 0.480 | 0.129 → 0.129 | 0.0 |
| prompt_injection | 1500 | 1.32 | 0.501 | 0.347 | 0.502 | 0.008 | 0.004 | 2.354 → 1.822 | 0.948 → 0.910 | 0.471 → 0.450 | 0.0 |
