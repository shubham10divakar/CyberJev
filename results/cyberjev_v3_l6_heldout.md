## Cyber-Jev — `runs/cyber-jev-v3-l6` on `data_heldout`

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 10320 | 1.81 | 0.881 | 0.879 | 0.949 | 0.030 | 0.007 | 0.737 → 0.438 | 0.215 → 0.200 | 0.103 → 0.083 | 1.0 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| dvwa-juiceshop | 4320 | 0.73 | 0.852 | 0.001 | 0.308 | 0.974 | 0.859 |
| sqli-queries | 6000 | 0.36 | 0.988 | 0.794 | 0.203 | 0.993 | 0.865 |
