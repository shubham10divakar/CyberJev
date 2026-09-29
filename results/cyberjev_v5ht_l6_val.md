## Cyber-Jev — `runs/cyber-jev-v5ht-l6` on `data_val`

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 3563 | 1.59 | 0.869 | 0.865 | 0.922 | 0.303 | 0.075 | 0.698 → 0.473 | 0.245 → 0.231 | 0.114 → 0.092 | 1.7 |
| phishing_url | 3000 | 2.00 | 0.851 | 0.850 | 0.946 | 0.551 | 0.321 | 0.532 → 0.363 | 0.250 → 0.224 | 0.100 → 0.047 | 0.7 |
| prompt_injection | 1500 | 1.74 | 0.713 | 0.711 | 0.787 | 0.072 | 0.009 | 1.386 → 0.870 | 0.518 → 0.476 | 0.241 → 0.198 | 3.8 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| spider | 563 | 0.00 | - | - | 0.007 | - | 0.498 |
| waf-v2 | 3000 | 0.50 | 0.894 | 0.251 | 0.140 | 0.831 | 0.846 |
