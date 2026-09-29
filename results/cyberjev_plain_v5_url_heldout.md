## Plain classifier (phishing_url, seed 0) on_heldout

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| phishing_url | 5000 | 1.16 | 0.741 | 0.722 | 0.822 | 0.083 | 0.011 | 0.562 → 0.533 | 0.363 → 0.352 | 0.112 → 0.090 | 0.1 |

**phishing_url by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| destroylist | 2000 | 1.00 | - | - | - | 0.643 | 0.392 |
| phishtrap | 3000 | 0.50 | 0.871 | 0.151 | 0.200 | 0.812 | 0.806 |
