## Cyber-Jev — `runs/cyber-jev-v2` on `data_heldout`

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 10320 | 2.27 | 0.607 | 0.596 | 0.763 | 0.351 | 0.181 | 2.066 → 1.004 | 0.740 → 0.626 | 0.367 → 0.298 | 2.7 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| dvwa-juiceshop | 4320 | 0.73 | 0.695 | 0.153 | 0.393 | 0.580 | 0.557 |
| sqli-queries | 6000 | 0.36 | 0.991 | 0.848 | 0.593 | 0.999 | 0.618 |
