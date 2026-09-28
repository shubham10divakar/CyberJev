## Cyber-Jev — `runs/cyber-jev-v2` on `data_heldout`

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 10320 | 1.51 | 0.723 | 0.699 | 0.881 | 0.343 | 0.174 | 1.628 → 1.108 | 0.527 → 0.506 | 0.258 → 0.240 | 1.7 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| dvwa-juiceshop | 4320 | 0.73 | 0.853 | 0.084 | 0.392 | 0.958 | 0.809 |
| sqli-queries | 6000 | 0.36 | 0.991 | 0.840 | 0.593 | 0.999 | 0.618 |
