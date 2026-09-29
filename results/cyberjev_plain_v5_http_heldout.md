## Plain classifier (http_attack, seed 0) on_heldout

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 10320 | 1.51 | 0.859 | 0.855 | 0.982 | 0.753 | 0.605 | 0.839 → 0.571 | 0.271 → 0.260 | 0.133 → 0.121 | 0.5 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| dvwa-juiceshop | 4320 | 0.73 | 0.987 | 0.891 | 0.463 | 0.994 | 0.805 |
| sqli-queries | 6000 | 0.36 | 0.993 | 0.936 | 0.233 | 0.996 | 0.848 |
