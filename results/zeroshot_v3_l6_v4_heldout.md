## Cyber-Jev — `runs/cyber-jev-v3-l6` on `data_heldout`

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| phishing_url | 5000 | 5.71 | 0.329 | 0.284 | 0.535 | 0.020 | 0.003 | 1.763 → 0.792 | 1.123 → 0.597 | 0.577 → 0.278 | 0.3 |
| prompt_injection | 1951 | 8.41 | 0.534 | 0.389 | 0.493 | 0.019 | 0.010 | 2.188 → 0.719 | 0.878 → 0.524 | 0.421 → 0.122 | 1.3 |

**phishing_url by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| destroylist | 2000 | 1.00 | - | - | - | 0.041 | 0.039 |
| phishtrap | 3000 | 0.50 | 0.595 | 0.031 | 0.035 | 0.077 | 0.404 |

**prompt_injection by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| deepset | 662 | 0.40 | 0.439 | 0.023 | 0.093 | 0.099 | 0.442 |
| jackhhao | 1289 | 0.51 | 0.571 | 0.038 | 0.008 | 0.031 | 0.362 |
