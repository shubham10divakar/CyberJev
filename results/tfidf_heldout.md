## TF-IDF + LR on `data_heldout`

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 10320 | 0.45 | 0.519 | 0.459 | 0.657 | 0.354 | 0.276 | 1.082 → 2.070 | 0.682 → 0.814 | 0.313 → 0.392 | 0.2 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| dvwa-juiceshop | 4320 | 0.73 | 0.347 | 0.003 | 0.853 | 0.704 | 0.425 |
| sqli-queries | 6000 | 0.36 | 0.992 | 0.889 | 0.795 | 0.999 | 0.465 |
