## Cyber-Jev — `runs/cyber-jev-v6-l6` on `data_heldout`

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 10320 | 1.69 | 0.894 | 0.893 | 0.982 | 0.861 | 0.717 | 0.501 → 0.326 | 0.194 → 0.180 | 0.089 → 0.071 | 1.0 |
| phishing_url | 5000 | 1.73 | 0.675 | 0.665 | 0.776 | 0.156 | 0.063 | 0.966 → 0.690 | 0.530 → 0.462 | 0.237 → 0.162 | 0.3 |
| prompt_injection | 1951 | 1.71 | 0.731 | 0.731 | 0.824 | 0.149 | 0.081 | 1.060 → 0.702 | 0.454 → 0.410 | 0.212 → 0.167 | 1.3 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| dvwa-juiceshop | 4320 | 0.73 | 0.966 | 0.788 | 0.221 | 0.963 | 0.886 |
| sqli-queries | 6000 | 0.36 | 0.997 | 0.969 | 0.187 | 0.996 | 0.877 |

**phishing_url by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| destroylist | 2000 | 1.00 | - | - | - | 0.518 | 0.341 |
| phishtrap | 3000 | 0.50 | 0.835 | 0.257 | 0.159 | 0.717 | 0.778 |

**prompt_injection by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| deepset | 662 | 0.40 | 0.787 | 0.137 | 0.276 | 0.722 | 0.717 |
| jackhhao | 1289 | 0.51 | 0.848 | 0.181 | 0.398 | 0.866 | 0.730 |
