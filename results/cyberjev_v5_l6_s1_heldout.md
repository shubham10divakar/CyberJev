## Cyber-Jev — `runs/cyber-jev-v5-l6-s1` on `data_heldout`

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 10320 | 1.20 | 0.858 | 0.855 | 0.973 | 0.819 | 0.757 | 0.635 → 0.541 | 0.255 → 0.250 | 0.119 → 0.112 | 1.0 |
| phishing_url | 5000 | 1.46 | 0.747 | 0.726 | 0.811 | 0.121 | 0.026 | 0.659 → 0.546 | 0.393 → 0.359 | 0.159 → 0.108 | 0.3 |
| prompt_injection | 1951 | 1.31 | 0.737 | 0.734 | 0.825 | 0.085 | 0.028 | 1.000 → 0.807 | 0.454 → 0.433 | 0.205 → 0.182 | 1.3 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| dvwa-juiceshop | 4320 | 0.73 | 0.952 | 0.714 | 0.357 | 0.971 | 0.836 |
| sqli-queries | 6000 | 0.36 | 0.994 | 0.962 | 0.246 | 0.990 | 0.838 |

**phishing_url by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| destroylist | 2000 | 1.00 | - | - | - | 0.680 | 0.405 |
| phishtrap | 3000 | 0.50 | 0.850 | 0.215 | 0.215 | 0.800 | 0.792 |

**prompt_injection by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| deepset | 662 | 0.40 | 0.769 | 0.137 | 0.398 | 0.829 | 0.692 |
| jackhhao | 1289 | 0.51 | 0.866 | 0.060 | 0.422 | 0.939 | 0.752 |
