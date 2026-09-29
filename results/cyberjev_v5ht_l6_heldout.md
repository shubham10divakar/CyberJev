## Cyber-Jev — `runs/cyber-jev-v5ht-l6` on `data_heldout`

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 10320 | 1.59 | 0.859 | 0.857 | 0.960 | 0.666 | 0.435 | 0.805 → 0.531 | 0.261 → 0.248 | 0.125 → 0.110 | 1.3 |
| phishing_url | 5000 | 2.00 | 0.764 | 0.732 | 0.821 | 0.156 | 0.017 | 0.718 → 0.505 | 0.378 → 0.331 | 0.153 → 0.071 | 0.5 |
| prompt_injection | 1951 | 1.74 | 0.716 | 0.711 | 0.828 | 0.123 | 0.020 | 1.478 → 0.910 | 0.526 → 0.485 | 0.251 → 0.215 | 2.0 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| dvwa-juiceshop | 4320 | 0.73 | 0.955 | 0.733 | 0.288 | 0.944 | 0.843 |
| sqli-queries | 6000 | 0.36 | 0.985 | 0.832 | 0.238 | 0.985 | 0.840 |

**phishing_url by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| destroylist | 2000 | 1.00 | - | - | - | 0.735 | 0.424 |
| phishtrap | 3000 | 0.50 | 0.872 | 0.247 | 0.302 | 0.867 | 0.781 |

**prompt_injection by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| deepset | 662 | 0.40 | 0.756 | 0.057 | 0.388 | 0.795 | 0.683 |
| jackhhao | 1289 | 0.51 | 0.867 | 0.161 | 0.476 | 0.935 | 0.719 |
