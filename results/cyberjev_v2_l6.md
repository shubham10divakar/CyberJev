## Cyber-Jev — `runs/cyber-jev-v2-l6` on `data`

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 4200 | 1.88 | 0.975 | 0.975 | 0.995 | 0.968 | 0.928 | 0.103 → 0.077 | 0.045 → 0.041 | 0.020 → 0.003 | 0.9 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| ai-waf | 1200 | 0.28 | 0.994 | 0.946 | 0.018 | 0.955 | 0.968 |
| csic2010 | 1500 | 0.60 | 0.984 | 0.930 | 0.028 | 0.939 | 0.950 |
| web-attacks | 1500 | 0.80 | 1.000 | 1.000 | 0.003 | 1.000 | 0.999 |
