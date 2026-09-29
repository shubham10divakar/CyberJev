## TF-IDF + LR on `data_val/val.jsonl`

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| prompt_injection | 1500 | 0.76 | 0.668 | 0.659 | 0.795 | 0.120 | 0.008 | 0.727 → 0.847 | 0.455 → 0.482 | 0.156 → 0.188 | 3.8 |
