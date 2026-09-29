## Plain classifier (prompt_injection, seed 2) on_heldout

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| prompt_injection | 1951 | 1.49 | 0.666 | 0.656 | 0.758 | 0.013 | 0.001 | 1.650 → 1.143 | 0.628 → 0.593 | 0.308 → 0.282 | 0.6 |

**prompt_injection by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| deepset | 662 | 0.40 | 0.700 | 0.004 | 0.411 | 0.783 | 0.666 |
| jackhhao | 1289 | 0.51 | 0.810 | 0.108 | 0.613 | 0.940 | 0.637 |
