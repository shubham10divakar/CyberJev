## Cyber-Jev — `runs/cyber-jev-v3-l6` on `data`

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| phishing_url | 1998 | 5.71 | 0.581 | 0.531 | 0.699 | 0.041 | 0.000 | 1.033 → 0.665 | 0.662 → 0.473 | 0.310 → 0.086 | 0.6 |
| prompt_injection | 1900 | 8.41 | 0.603 | 0.550 | 0.786 | 0.308 | 0.224 | 1.725 → 0.653 | 0.736 → 0.461 | 0.368 → 0.097 | 0.7 |

**prompt_injection by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| neuralchemy | 900 | 0.59 | 0.894 | 0.474 | 0.005 | 0.440 | 0.662 |
| s-labs | 1000 | 0.47 | 0.646 | 0.079 | 0.000 | 0.030 | 0.378 |
