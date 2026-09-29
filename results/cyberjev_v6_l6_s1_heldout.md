## Cyber-Jev — `runs/cyber-jev-v6-l6-s1` on `data_heldout`

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 10320 | 1.98 | 0.827 | 0.822 | 0.952 | 0.645 | 0.408 | 1.314 → 0.687 | 0.332 → 0.315 | 0.163 → 0.146 | 1.0 |
| phishing_url | 5000 | 2.45 | 0.707 | 0.692 | 0.789 | 0.143 | 0.047 | 1.124 → 0.615 | 0.512 → 0.413 | 0.243 → 0.139 | 0.3 |
| prompt_injection | 1951 | 2.07 | 0.746 | 0.746 | 0.844 | 0.173 | 0.026 | 1.305 → 0.707 | 0.459 → 0.407 | 0.222 → 0.172 | 1.3 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| dvwa-juiceshop | 4320 | 0.73 | 0.849 | 0.233 | 0.594 | 0.955 | 0.705 |
| sqli-queries | 6000 | 0.36 | 0.994 | 0.955 | 0.246 | 0.994 | 0.839 |

**phishing_url by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| destroylist | 2000 | 1.00 | - | - | - | 0.570 | 0.363 |
| phishtrap | 3000 | 0.50 | 0.852 | 0.250 | 0.181 | 0.777 | 0.798 |

**prompt_injection by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| deepset | 662 | 0.40 | 0.843 | 0.186 | 0.163 | 0.669 | 0.757 |
| jackhhao | 1289 | 0.51 | 0.852 | 0.124 | 0.433 | 0.896 | 0.725 |
