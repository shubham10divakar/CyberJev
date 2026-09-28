## Cyber-Jev — `runs/cyber-jev-v2` on `data`

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 4200 | 1.51 | 0.977 | 0.977 | 0.996 | 0.971 | 0.886 | 0.080 → 0.074 | 0.039 → 0.039 | 0.010 → 0.011 | 1.5 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| ai-waf | 1200 | 0.28 | 0.998 | 0.976 | 0.006 | 0.970 | 0.984 |
| csic2010 | 1500 | 0.60 | 0.983 | 0.913 | 0.039 | 0.940 | 0.947 |
| web-attacks | 1500 | 0.80 | 1.000 | 1.000 | 0.010 | 1.000 | 0.997 |
