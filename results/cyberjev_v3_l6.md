## Cyber-Jev — `runs/cyber-jev-v3-l6` on `data`

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 4700 | 1.81 | 0.978 | 0.978 | 0.997 | 0.968 | 0.941 | 0.089 → 0.067 | 0.039 → 0.036 | 0.017 → 0.007 | 0.8 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| ai-waf | 1200 | 0.28 | 0.996 | 0.958 | 0.014 | 0.961 | 0.974 |
| csic2010 | 1500 | 0.60 | 0.986 | 0.910 | 0.022 | 0.936 | 0.951 |
| gretel-sql | 500 | 0.00 | - | - | 0.002 | - | 0.499 |
| web-attacks | 1500 | 0.80 | 1.000 | 0.998 | 0.007 | 0.997 | 0.995 |
