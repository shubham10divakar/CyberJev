## Cyber-Jev — `runs/cyber-jev-v4-l6` on `data_heldout`

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 10320 | 1.69 | 0.875 | 0.873 | 0.956 | 0.619 | 0.418 | 0.676 → 0.429 | 0.233 → 0.218 | 0.110 → 0.090 | 1.0 |
| phishing_url | 5000 | 2.02 | 0.699 | 0.687 | 0.798 | 0.184 | 0.060 | 0.910 → 0.605 | 0.500 → 0.414 | 0.228 → 0.133 | 0.3 |
| prompt_injection | 1951 | 1.64 | 0.674 | 0.655 | 0.766 | 0.044 | 0.025 | 1.461 → 0.963 | 0.582 → 0.534 | 0.279 → 0.236 | 1.3 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| dvwa-juiceshop | 4320 | 0.73 | 0.961 | 0.678 | 0.140 | 0.932 | 0.890 |
| sqli-queries | 6000 | 0.36 | 0.988 | 0.883 | 0.231 | 0.985 | 0.845 |

**phishing_url by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| destroylist | 2000 | 1.00 | - | - | - | 0.574 | 0.365 |
| phishtrap | 3000 | 0.50 | 0.844 | 0.306 | 0.162 | 0.727 | 0.782 |

**prompt_injection by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| deepset | 662 | 0.40 | 0.835 | 0.095 | 0.363 | 0.909 | 0.745 |
| jackhhao | 1289 | 0.51 | 0.727 | 0.023 | 0.721 | 0.988 | 0.583 |
