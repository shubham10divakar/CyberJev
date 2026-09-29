## Cyber-Jev — `runs/cyber-jev-v6-l6-s2` on `data_heldout`

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 10320 | 1.72 | 0.852 | 0.847 | 0.973 | 0.693 | 0.389 | 1.105 → 0.661 | 0.285 → 0.272 | 0.140 → 0.128 | 1.0 |
| phishing_url | 5000 | 2.07 | 0.719 | 0.701 | 0.782 | 0.117 | 0.026 | 0.921 → 0.592 | 0.463 → 0.390 | 0.206 → 0.121 | 0.3 |
| prompt_injection | 1951 | 2.06 | 0.763 | 0.763 | 0.849 | 0.085 | 0.009 | 1.216 → 0.664 | 0.423 → 0.375 | 0.203 → 0.156 | 1.3 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| dvwa-juiceshop | 4320 | 0.73 | 0.915 | 0.499 | 0.535 | 0.990 | 0.764 |
| sqli-queries | 6000 | 0.36 | 0.991 | 0.931 | 0.222 | 0.986 | 0.851 |

**phishing_url by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| destroylist | 2000 | 1.00 | - | - | - | 0.627 | 0.385 |
| phishtrap | 3000 | 0.50 | 0.832 | 0.195 | 0.209 | 0.771 | 0.781 |

**prompt_injection by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| deepset | 662 | 0.40 | 0.840 | 0.110 | 0.128 | 0.589 | 0.738 |
| jackhhao | 1289 | 0.51 | 0.867 | 0.020 | 0.378 | 0.905 | 0.760 |
