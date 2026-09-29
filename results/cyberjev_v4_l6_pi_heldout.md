## Cyber-Jev — `runs/cyber-jev-v4-l6-pi` on `data_heldout`

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| prompt_injection | 1951 | 1.71 | 0.656 | 0.631 | 0.715 | 0.018 | 0.011 | 1.540 → 0.992 | 0.603 → 0.549 | 0.288 → 0.233 | 1.3 |

**prompt_injection by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| deepset | 662 | 0.40 | 0.725 | 0.038 | 0.411 | 0.935 | 0.727 |
| jackhhao | 1289 | 0.51 | 0.714 | 0.014 | 0.759 | 0.989 | 0.555 |
