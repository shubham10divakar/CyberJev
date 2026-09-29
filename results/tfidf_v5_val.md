## TF-IDF + LR on `data_val/val.jsonl`

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| prompt_injection | 1500 | 0.79 | 0.691 | 0.687 | 0.791 | 0.104 | 0.003 | 0.689 → 0.780 | 0.430 → 0.451 | 0.134 → 0.162 | 3.7 |
