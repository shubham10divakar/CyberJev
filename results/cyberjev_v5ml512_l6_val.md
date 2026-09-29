## Cyber-Jev — `runs/cyber-jev-v5ml512-l6` on `data_val`

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 3563 | 1.71 | 0.835 | 0.833 | 0.906 | 0.201 | 0.074 | 0.826 → 0.540 | 0.298 → 0.281 | 0.130 → 0.106 | 2.0 |
| phishing_url | 3000 | 1.91 | 0.868 | 0.868 | 0.947 | 0.597 | 0.385 | 0.450 → 0.331 | 0.219 → 0.203 | 0.080 → 0.034 | 0.6 |
| prompt_injection | 1500 | 1.68 | 0.735 | 0.735 | 0.808 | 0.081 | 0.009 | 1.168 → 0.766 | 0.468 → 0.429 | 0.218 → 0.176 | 3.2 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| spider | 563 | 0.00 | - | - | 0.002 | - | 0.500 |
| waf-v2 | 3000 | 0.50 | 0.872 | 0.181 | 0.269 | 0.878 | 0.803 |
