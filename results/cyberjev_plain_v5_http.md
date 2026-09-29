## Plain classifier (http_attack, seed 0) on in-domain

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 4700 | 1.51 | 0.982 | 0.982 | 0.997 | 0.973 | 0.942 | 0.076 → 0.064 | 0.034 → 0.032 | 0.015 → 0.008 | 0.4 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| ai-waf | 1200 | 0.28 | 1.000 | 0.991 | 0.003 | 0.985 | 0.992 |
| csic2010 | 1500 | 0.60 | 0.981 | 0.920 | 0.025 | 0.935 | 0.949 |
| gretel-sql | 500 | 0.00 | - | - | 0.000 | - | 1.000 |
| web-attacks | 1500 | 0.80 | 1.000 | 0.999 | 0.007 | 0.998 | 0.996 |
