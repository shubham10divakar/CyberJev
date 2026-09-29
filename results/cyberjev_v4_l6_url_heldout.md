## Cyber-Jev — `runs/cyber-jev-v4-l6-url` on `data_heldout`

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| phishing_url | 5000 | 1.36 | 0.711 | 0.698 | 0.814 | 0.132 | 0.045 | 0.658 → 0.581 | 0.418 → 0.390 | 0.150 → 0.106 | 0.3 |

**phishing_url by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| destroylist | 2000 | 1.00 | - | - | - | 0.579 | 0.367 |
| phishtrap | 3000 | 0.50 | 0.862 | 0.226 | 0.157 | 0.756 | 0.799 |
