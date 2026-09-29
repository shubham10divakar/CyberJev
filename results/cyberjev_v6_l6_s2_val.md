## Cyber-Jev — `runs/cyber-jev-v6-l6-s2` on `data_val`

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 3563 | 1.72 | 0.804 | 0.804 | 0.919 | 0.301 | 0.123 | 1.174 → 0.726 | 0.354 → 0.333 | 0.168 → 0.143 | 1.2 |
| phishing_url | 3000 | 2.07 | 0.880 | 0.880 | 0.942 | 0.615 | 0.160 | 0.506 → 0.339 | 0.214 → 0.199 | 0.086 → 0.040 | 0.5 |
| prompt_injection | 1500 | 2.06 | 0.708 | 0.708 | 0.776 | 0.079 | 0.019 | 1.548 → 0.834 | 0.532 → 0.476 | 0.257 → 0.202 | 1.7 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| spider | 563 | 0.00 | - | - | 0.000 | - | 1.000 |
| waf-v2 | 3000 | 0.50 | 0.888 | 0.275 | 0.382 | 0.916 | 0.762 |
