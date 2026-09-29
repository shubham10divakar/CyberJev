## Cyber-Jev — `runs/cyber-jev-v3-l6-s1` on `data`

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 4700 | 1.78 | 0.977 | 0.977 | 0.996 | 0.963 | 0.937 | 0.097 → 0.071 | 0.043 → 0.039 | 0.020 → 0.010 | 0.8 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| ai-waf | 1200 | 0.28 | 0.995 | 0.958 | 0.010 | 0.958 | 0.976 |
| csic2010 | 1500 | 0.60 | 0.981 | 0.914 | 0.022 | 0.925 | 0.944 |
| gretel-sql | 500 | 0.00 | - | - | 0.002 | - | 0.499 |
| web-attacks | 1500 | 0.80 | 1.000 | 0.997 | 0.007 | 0.997 | 0.995 |
