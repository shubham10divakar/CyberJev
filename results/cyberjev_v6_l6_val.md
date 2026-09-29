## Cyber-Jev — `runs/cyber-jev-v6-l6` on `data_val`

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 3563 | 1.69 | 0.774 | 0.774 | 0.907 | 0.302 | 0.098 | 1.036 → 0.656 | 0.410 → 0.371 | 0.202 → 0.175 | 1.2 |
| phishing_url | 3000 | 1.73 | 0.876 | 0.876 | 0.934 | 0.519 | 0.082 | 0.424 → 0.329 | 0.210 → 0.196 | 0.076 → 0.027 | 0.5 |
| prompt_injection | 1500 | 1.71 | 0.736 | 0.735 | 0.796 | 0.067 | 0.003 | 1.346 → 0.853 | 0.478 → 0.446 | 0.225 → 0.186 | 1.7 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| spider | 563 | 0.00 | - | - | 0.004 | - | 0.499 |
| waf-v2 | 3000 | 0.50 | 0.873 | 0.291 | 0.435 | 0.900 | 0.725 |
