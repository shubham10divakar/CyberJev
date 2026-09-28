## Cyber-Jev — `runs/cyber-jev-dev` on `data_heldout`

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 10320 | 9.98 | 0.520 | 0.346 | 0.702 | 0.043 | 0.004 | 2.257 → 0.694 | 0.905 → 0.501 | 0.459 → 0.106 | 1.7 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| dvwa-juiceshop | 4320 | 0.73 | 0.150 | 0.005 | 1.000 | 1.000 | 0.423 |
| sqli-queries | 6000 | 0.36 | 0.869 | 0.190 | 0.994 | 1.000 | 0.273 |
