## Cyber-Jev — `runs/cyber-jev-v2-s1` on `data_heldout`

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 10320 | 1.59 | 0.722 | 0.701 | 0.864 | 0.077 | 0.000 | 2.015 → 1.284 | 0.544 → 0.530 | 0.269 → 0.257 | 1.7 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| dvwa-juiceshop | 4320 | 0.73 | 0.826 | 0.523 | 0.575 | 0.925 | 0.695 |
| sqli-queries | 6000 | 0.36 | 0.939 | 0.163 | 0.513 | 0.998 | 0.672 |
