## Cyber-Jev — `runs/cyber-jev-v5-l6-s1` on `data_val`

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 3563 | 1.20 | 0.796 | 0.795 | 0.905 | 0.348 | 0.141 | 0.728 → 0.633 | 0.325 → 0.315 | 0.142 → 0.129 | 1.3 |
| phishing_url | 3000 | 1.46 | 0.879 | 0.879 | 0.946 | 0.582 | 0.058 | 0.378 → 0.325 | 0.204 → 0.195 | 0.070 → 0.033 | 0.5 |
| prompt_injection | 1500 | 1.31 | 0.701 | 0.699 | 0.783 | 0.101 | 0.005 | 0.964 → 0.795 | 0.483 → 0.458 | 0.210 → 0.183 | 1.8 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| spider | 563 | 0.00 | - | - | 0.000 | - | 1.000 |
| waf-v2 | 3000 | 0.50 | 0.870 | 0.318 | 0.355 | 0.871 | 0.755 |
