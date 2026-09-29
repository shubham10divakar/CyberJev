## Plain classifier (http_attack, seed 1) on in-domain

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 4700 | 1.52 | 0.981 | 0.981 | 0.998 | 0.973 | 0.959 | 0.074 → 0.064 | 0.034 → 0.032 | 0.014 → 0.006 | 0.4 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| ai-waf | 1200 | 0.28 | 1.000 | 0.991 | 0.006 | 0.988 | 0.991 |
| csic2010 | 1500 | 0.60 | 0.983 | 0.921 | 0.032 | 0.934 | 0.946 |
| gretel-sql | 500 | 0.00 | - | - | 0.000 | - | 1.000 |
| web-attacks | 1500 | 0.80 | 1.000 | 1.000 | 0.003 | 0.999 | 0.998 |
