## Cyber-Jev — `runs/cyber-jev-v2-l6` on `data_val`

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 3563 | 4.03 | 0.707 | 0.706 | 0.856 | 0.229 | 0.064 | 1.596 → 0.594 | 0.525 → 0.396 | 0.260 → 0.114 | 1.2 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| spider | 563 | 0.00 | - | - | 0.549 | - | 0.311 |
| waf-v2 | 3000 | 0.50 | 0.885 | 0.305 | 0.398 | 0.909 | 0.749 |
