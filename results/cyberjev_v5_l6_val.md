## Cyber-Jev — `runs/cyber-jev-v5-l6` on `data_val`

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 3563 | 1.83 | 0.851 | 0.843 | 0.940 | 0.348 | 0.163 | 0.720 → 0.436 | 0.273 → 0.247 | 0.130 → 0.101 | 1.2 |
| phishing_url | 3000 | 1.82 | 0.863 | 0.863 | 0.947 | 0.610 | 0.303 | 0.456 → 0.340 | 0.227 → 0.208 | 0.085 → 0.033 | 0.5 |
| prompt_injection | 1500 | 1.60 | 0.734 | 0.734 | 0.813 | 0.088 | 0.020 | 1.086 → 0.746 | 0.464 → 0.424 | 0.217 → 0.178 | 1.7 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| spider | 563 | 0.00 | - | - | 0.000 | - | 1.000 |
| waf-v2 | 3000 | 0.50 | 0.919 | 0.331 | 0.102 | 0.747 | 0.822 |
