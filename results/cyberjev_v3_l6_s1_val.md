## Cyber-Jev — `runs/cyber-jev-v3-l6-s1` on `data_val`

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 3563 | 1.78 | 0.756 | 0.756 | 0.903 | 0.326 | 0.142 | 1.281 → 0.759 | 0.462 → 0.418 | 0.229 → 0.201 | 1.2 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| spider | 563 | 0.00 | - | - | 0.000 | - | 1.000 |
| waf-v2 | 3000 | 0.50 | 0.867 | 0.277 | 0.477 | 0.898 | 0.700 |
