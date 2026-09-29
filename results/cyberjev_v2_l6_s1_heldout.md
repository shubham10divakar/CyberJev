## Cyber-Jev — `runs/cyber-jev-v2-l6-s1` on `data_heldout`

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 10320 | 1.70 | 0.832 | 0.827 | 0.944 | 0.264 | 0.031 | 0.920 → 0.581 | 0.301 → 0.283 | 0.141 → 0.119 | 1.0 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| dvwa-juiceshop | 4320 | 0.73 | 0.921 | 0.312 | 0.311 | 0.954 | 0.841 |
| sqli-queries | 6000 | 0.36 | 0.981 | 0.321 | 0.320 | 0.998 | 0.795 |
