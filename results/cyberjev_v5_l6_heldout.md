## Cyber-Jev — `runs/cyber-jev-v5-l6` on `data_heldout`

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 10320 | 1.83 | 0.849 | 0.847 | 0.955 | 0.652 | 0.515 | 0.718 → 0.435 | 0.272 → 0.245 | 0.128 → 0.100 | 1.0 |
| phishing_url | 5000 | 1.82 | 0.749 | 0.723 | 0.817 | 0.201 | 0.065 | 0.717 → 0.525 | 0.392 → 0.345 | 0.163 → 0.093 | 0.3 |
| prompt_injection | 1951 | 1.60 | 0.726 | 0.725 | 0.829 | 0.165 | 0.023 | 1.157 → 0.787 | 0.486 → 0.446 | 0.229 → 0.192 | 1.3 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| dvwa-juiceshop | 4320 | 0.73 | 0.933 | 0.582 | 0.305 | 0.908 | 0.807 |
| sqli-queries | 6000 | 0.36 | 0.991 | 0.924 | 0.235 | 0.992 | 0.845 |

**phishing_url by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| destroylist | 2000 | 1.00 | - | - | - | 0.678 | 0.404 |
| phishtrap | 3000 | 0.50 | 0.874 | 0.311 | 0.265 | 0.857 | 0.796 |

**prompt_injection by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| deepset | 662 | 0.40 | 0.747 | 0.118 | 0.358 | 0.677 | 0.651 |
| jackhhao | 1289 | 0.51 | 0.870 | 0.180 | 0.398 | 0.920 | 0.756 |
