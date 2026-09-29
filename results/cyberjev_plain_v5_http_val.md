## Plain classifier (http_attack, seed 0) on_val

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 3563 | 1.51 | 0.820 | 0.818 | 0.905 | 0.208 | 0.026 | 0.994 → 0.681 | 0.340 → 0.325 | 0.165 → 0.150 | 0.6 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| spider | 563 | 0.00 | - | - | 0.007 | - | 0.498 |
| waf-v2 | 3000 | 0.50 | 0.873 | 0.119 | 0.274 | 0.849 | 0.787 |
