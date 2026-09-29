## Plain classifier (http_attack, seed 1) on_heldout

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 10320 | 1.52 | 0.796 | 0.785 | 0.940 | 0.579 | 0.439 | 1.283 → 0.859 | 0.397 → 0.384 | 0.196 → 0.184 | 0.5 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| dvwa-juiceshop | 4320 | 0.73 | 0.814 | 0.382 | 0.890 | 0.975 | 0.517 |
| sqli-queries | 6000 | 0.36 | 0.992 | 0.892 | 0.260 | 0.996 | 0.831 |
