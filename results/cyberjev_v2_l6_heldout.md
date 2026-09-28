## Cyber-Jev — `runs/cyber-jev-v2-l6` on `data_heldout`

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 10320 | 1.88 | 0.812 | 0.805 | 0.953 | 0.457 | 0.196 | 1.208 → 0.680 | 0.352 → 0.330 | 0.169 → 0.145 | 1.0 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| dvwa-juiceshop | 4320 | 0.73 | 0.975 | 0.823 | 0.212 | 0.965 | 0.891 |
| sqli-queries | 6000 | 0.36 | 0.992 | 0.811 | 0.413 | 0.999 | 0.737 |
