## Cyber-Jev — `runs/cyber-jev-v6-l6-s1` on `data_val`

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 3563 | 1.98 | 0.859 | 0.856 | 0.919 | 0.330 | 0.135 | 0.877 → 0.489 | 0.262 → 0.245 | 0.122 → 0.093 | 1.3 |
| phishing_url | 3000 | 2.45 | 0.880 | 0.880 | 0.943 | 0.569 | 0.102 | 0.539 → 0.318 | 0.213 → 0.189 | 0.094 → 0.026 | 0.5 |
| prompt_injection | 1500 | 2.07 | 0.726 | 0.726 | 0.787 | 0.076 | 0.017 | 1.480 → 0.797 | 0.504 → 0.452 | 0.240 → 0.190 | 1.8 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| spider | 563 | 0.00 | - | - | 0.000 | - | 1.000 |
| waf-v2 | 3000 | 0.50 | 0.889 | 0.279 | 0.175 | 0.841 | 0.833 |
