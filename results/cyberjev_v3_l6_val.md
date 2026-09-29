## Cyber-Jev — `runs/cyber-jev-v3-l6` on `data_val`

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 3563 | 1.81 | 0.765 | 0.765 | 0.909 | 0.169 | 0.035 | 1.003 → 0.611 | 0.399 → 0.346 | 0.202 → 0.167 | 1.2 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| spider | 563 | 0.00 | - | - | 0.000 | - | 1.000 |
| waf-v2 | 3000 | 0.50 | 0.875 | 0.129 | 0.451 | 0.893 | 0.713 |
