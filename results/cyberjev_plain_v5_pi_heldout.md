## Plain classifier (prompt_injection, seed 0) on_heldout

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| prompt_injection | 1951 | 1.31 | 0.691 | 0.689 | 0.744 | 0.025 | 0.005 | 1.199 → 0.956 | 0.557 → 0.531 | 0.262 → 0.237 | 0.7 |

**prompt_injection by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| deepset | 662 | 0.40 | 0.742 | 0.061 | 0.388 | 0.783 | 0.679 |
| jackhhao | 1289 | 0.51 | 0.760 | 0.012 | 0.458 | 0.848 | 0.689 |
