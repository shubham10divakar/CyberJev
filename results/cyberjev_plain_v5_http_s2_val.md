## Plain classifier (http_attack, seed 2) on_val

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 3563 | 1.59 | 0.830 | 0.827 | 0.922 | 0.342 | 0.045 | 0.841 → 0.560 | 0.310 → 0.289 | 0.152 → 0.132 | 0.6 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| spider | 563 | 0.00 | - | - | 0.011 | - | 0.497 |
| waf-v2 | 3000 | 0.50 | 0.895 | 0.315 | 0.223 | 0.824 | 0.800 |
