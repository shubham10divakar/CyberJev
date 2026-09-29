## Cyber-Jev — `runs/cyber-jev-v2-l6-e3` on `data_heldout`

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 10320 | 1.89 | 0.771 | 0.759 | 0.905 | 0.305 | 0.076 | 1.409 → 0.793 | 0.429 → 0.399 | 0.205 → 0.175 | 1.0 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| dvwa-juiceshop | 4320 | 0.73 | 0.957 | 0.606 | 0.154 | 0.938 | 0.890 |
| sqli-queries | 6000 | 0.36 | 0.986 | 0.590 | 0.519 | 0.999 | 0.668 |
