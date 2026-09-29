## Plain classifier (http_attack, seed 1) on_val

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 3563 | 1.52 | 0.656 | 0.648 | 0.888 | 0.255 | 0.050 | 1.952 → 1.307 | 0.659 → 0.631 | 0.327 → 0.311 | 0.6 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| spider | 563 | 0.00 | - | - | 0.012 | - | 0.497 |
| waf-v2 | 3000 | 0.50 | 0.847 | 0.168 | 0.773 | 0.962 | 0.531 |
