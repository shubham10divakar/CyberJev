## Cyber-Jev — `runs/cyber-jev-v2-l6-s1` on `data`

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 4200 | 1.70 | 0.966 | 0.965 | 0.994 | 0.949 | 0.923 | 0.118 → 0.095 | 0.058 → 0.055 | 0.022 → 0.005 | 0.9 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| ai-waf | 1200 | 0.28 | 0.995 | 0.952 | 0.007 | 0.949 | 0.976 |
| csic2010 | 1500 | 0.60 | 0.970 | 0.859 | 0.032 | 0.889 | 0.919 |
| web-attacks | 1500 | 0.80 | 1.000 | 1.000 | 0.003 | 0.999 | 0.998 |
