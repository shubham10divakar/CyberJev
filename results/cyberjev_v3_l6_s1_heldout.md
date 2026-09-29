## Cyber-Jev — `runs/cyber-jev-v3-l6-s1` on `data_heldout`

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 10320 | 1.78 | 0.894 | 0.893 | 0.985 | 0.824 | 0.549 | 0.583 → 0.357 | 0.191 → 0.178 | 0.089 → 0.071 | 1.0 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| dvwa-juiceshop | 4320 | 0.73 | 0.956 | 0.678 | 0.364 | 0.984 | 0.843 |
| sqli-queries | 6000 | 0.36 | 0.996 | 0.972 | 0.159 | 0.995 | 0.894 |
