## Plain classifier (phishing_url, seed 2) on_heldout

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| phishing_url | 5000 | 1.45 | 0.752 | 0.730 | 0.829 | 0.114 | 0.029 | 0.634 → 0.531 | 0.381 → 0.349 | 0.153 → 0.101 | 0.1 |

**phishing_url by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| destroylist | 2000 | 1.00 | - | - | - | 0.676 | 0.403 |
| phishtrap | 3000 | 0.50 | 0.874 | 0.196 | 0.221 | 0.825 | 0.802 |
