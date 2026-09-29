## Cyber-Jev — `runs/cyber-jev-v5-l6-s2` on `data_heldout`

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 10320 | 1.49 | 0.831 | 0.825 | 0.959 | 0.695 | 0.546 | 0.986 → 0.684 | 0.314 → 0.301 | 0.151 → 0.138 | 1.0 |
| phishing_url | 5000 | 1.73 | 0.731 | 0.708 | 0.795 | 0.138 | 0.067 | 0.736 → 0.560 | 0.408 → 0.365 | 0.162 → 0.096 | 0.3 |
| prompt_injection | 1951 | 1.75 | 0.704 | 0.698 | 0.782 | 0.046 | 0.008 | 1.533 → 0.944 | 0.544 → 0.502 | 0.260 → 0.217 | 1.3 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| dvwa-juiceshop | 4320 | 0.73 | 0.863 | 0.459 | 0.590 | 0.959 | 0.710 |
| sqli-queries | 6000 | 0.36 | 0.994 | 0.946 | 0.242 | 0.994 | 0.842 |

**phishing_url by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| destroylist | 2000 | 1.00 | - | - | - | 0.661 | 0.398 |
| phishtrap | 3000 | 0.50 | 0.848 | 0.233 | 0.251 | 0.806 | 0.777 |

**prompt_injection by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| deepset | 662 | 0.40 | 0.748 | 0.065 | 0.409 | 0.821 | 0.682 |
| jackhhao | 1289 | 0.51 | 0.811 | 0.023 | 0.502 | 0.926 | 0.700 |
