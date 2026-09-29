## Cyber-Jev — `runs/cyber-jev-v2-l6-e3` on `data`

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 4200 | 1.89 | 0.971 | 0.970 | 0.995 | 0.956 | 0.921 | 0.110 → 0.085 | 0.052 → 0.047 | 0.024 → 0.010 | 0.9 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| ai-waf | 1200 | 0.28 | 0.995 | 0.949 | 0.008 | 0.946 | 0.974 |
| csic2010 | 1500 | 0.60 | 0.978 | 0.895 | 0.032 | 0.914 | 0.934 |
| web-attacks | 1500 | 0.80 | 1.000 | 1.000 | 0.003 | 1.000 | 0.999 |
