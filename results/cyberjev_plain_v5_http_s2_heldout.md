## Plain classifier (http_attack, seed 2) on_heldout

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 10320 | 1.59 | 0.856 | 0.852 | 0.970 | 0.669 | 0.186 | 0.866 → 0.565 | 0.274 → 0.262 | 0.135 → 0.122 | 0.5 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| dvwa-juiceshop | 4320 | 0.73 | 0.947 | 0.586 | 0.434 | 0.980 | 0.807 |
| sqli-queries | 6000 | 0.36 | 0.990 | 0.790 | 0.238 | 0.996 | 0.845 |
