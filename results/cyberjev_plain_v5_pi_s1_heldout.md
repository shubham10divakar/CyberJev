## Plain classifier (prompt_injection, seed 1) on_heldout

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| prompt_injection | 1951 | 1.48 | 0.693 | 0.686 | 0.778 | 0.030 | 0.002 | 1.486 → 1.040 | 0.575 → 0.544 | 0.281 → 0.255 | 0.7 |

**prompt_injection by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| deepset | 662 | 0.40 | 0.712 | 0.038 | 0.431 | 0.833 | 0.674 |
| jackhhao | 1289 | 0.51 | 0.832 | 0.009 | 0.528 | 0.929 | 0.685 |
