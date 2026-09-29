## Cyber-Jev — `runs/cyber-jev-v2-s1` on `data`

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 4200 | 1.59 | 0.983 | 0.982 | 0.997 | 0.977 | 0.962 | 0.072 → 0.060 | 0.032 → 0.030 | 0.014 → 0.008 | 1.4 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| ai-waf | 1200 | 0.28 | 0.997 | 0.979 | 0.006 | 0.970 | 0.984 |
| csic2010 | 1500 | 0.60 | 0.987 | 0.945 | 0.018 | 0.948 | 0.960 |
| web-attacks | 1500 | 0.80 | 1.000 | 1.000 | 0.000 | 1.000 | 1.000 |
