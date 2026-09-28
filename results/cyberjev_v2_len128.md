## Cyber-Jev — `runs/cyber-jev-v2` on `data`

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 4200 | 2.27 | 0.937 | 0.936 | 0.983 | 0.905 | 0.847 | 0.227 → 0.167 | 0.107 → 0.093 | 0.047 → 0.021 | 2.2 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| ai-waf | 1200 | 0.28 | 0.976 | 0.725 | 0.014 | 0.743 | 0.891 |
| csic2010 | 1500 | 0.60 | 0.962 | 0.829 | 0.084 | 0.874 | 0.888 |
| web-attacks | 1500 | 0.80 | 1.000 | 1.000 | 0.010 | 1.000 | 0.997 |
