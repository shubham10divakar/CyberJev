## Cyber-Jev — `runs/cyber-jev-v5-l6-s2` on `data_val`

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 3563 | 1.49 | 0.773 | 0.772 | 0.900 | 0.233 | 0.072 | 0.876 → 0.632 | 0.389 → 0.355 | 0.188 → 0.162 | 1.3 |
| phishing_url | 3000 | 1.73 | 0.872 | 0.872 | 0.938 | 0.579 | 0.308 | 0.434 → 0.337 | 0.216 → 0.203 | 0.078 → 0.036 | 0.5 |
| prompt_injection | 1500 | 1.75 | 0.733 | 0.733 | 0.800 | 0.111 | 0.003 | 1.123 → 0.727 | 0.469 → 0.425 | 0.214 → 0.165 | 1.8 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| spider | 563 | 0.00 | - | - | 0.005 | - | 0.499 |
| waf-v2 | 3000 | 0.50 | 0.864 | 0.201 | 0.395 | 0.857 | 0.727 |
