## Plain classifier (phishing_url, seed 1) on_heldout

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| phishing_url | 5000 | 1.42 | 0.728 | 0.711 | 0.819 | 0.107 | 0.016 | 0.660 → 0.567 | 0.405 → 0.376 | 0.149 → 0.101 | 0.1 |

**phishing_url by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| destroylist | 2000 | 1.00 | - | - | - | 0.633 | 0.388 |
| phishtrap | 3000 | 0.50 | 0.860 | 0.175 | 0.189 | 0.771 | 0.791 |
