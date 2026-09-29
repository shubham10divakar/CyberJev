## Cyber-Jev — `runs/cyber-jev-v5ml512-l6` on `data_heldout`

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 10320 | 1.71 | 0.846 | 0.843 | 0.953 | 0.632 | 0.533 | 0.881 → 0.545 | 0.286 → 0.268 | 0.137 → 0.117 | 1.1 |
| phishing_url | 5000 | 1.91 | 0.753 | 0.725 | 0.814 | 0.138 | 0.065 | 0.688 → 0.507 | 0.376 → 0.332 | 0.152 → 0.075 | 0.3 |
| prompt_injection | 1951 | 1.68 | 0.704 | 0.700 | 0.799 | 0.083 | 0.026 | 1.512 → 0.959 | 0.537 → 0.499 | 0.257 → 0.222 | 2.3 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| dvwa-juiceshop | 4320 | 0.73 | 0.934 | 0.569 | 0.355 | 0.943 | 0.813 |
| sqli-queries | 6000 | 0.36 | 0.981 | 0.808 | 0.253 | 0.987 | 0.832 |

**phishing_url by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| destroylist | 2000 | 1.00 | - | - | - | 0.705 | 0.413 |
| phishtrap | 3000 | 0.50 | 0.865 | 0.236 | 0.277 | 0.847 | 0.784 |

**prompt_injection by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| deepset | 662 | 0.40 | 0.765 | 0.133 | 0.391 | 0.772 | 0.673 |
| jackhhao | 1289 | 0.51 | 0.820 | 0.057 | 0.486 | 0.922 | 0.707 |
