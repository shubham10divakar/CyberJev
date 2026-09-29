## Plain classifier (http_attack, seed 2) on in-domain

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 4700 | 1.59 | 0.980 | 0.980 | 0.997 | 0.969 | 0.936 | 0.088 → 0.071 | 0.039 → 0.036 | 0.017 → 0.011 | 0.4 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| ai-waf | 1200 | 0.28 | 0.999 | 0.985 | 0.005 | 0.979 | 0.989 |
| csic2010 | 1500 | 0.60 | 0.983 | 0.900 | 0.034 | 0.934 | 0.945 |
| gretel-sql | 500 | 0.00 | - | - | 0.000 | - | 1.000 |
| web-attacks | 1500 | 0.80 | 1.000 | 0.999 | 0.003 | 0.997 | 0.995 |
