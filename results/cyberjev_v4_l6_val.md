## Cyber-Jev — `runs/cyber-jev-v4-l6` on `data_val`

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 3563 | 1.69 | 0.848 | 0.843 | 0.911 | 0.227 | 0.081 | 0.749 → 0.490 | 0.271 → 0.254 | 0.125 → 0.096 | 1.2 |
| phishing_url | 3000 | 2.02 | 0.877 | 0.877 | 0.940 | 0.557 | 0.467 | 0.402 → 0.306 | 0.201 → 0.184 | 0.079 → 0.013 | 0.5 |
| prompt_injection | 1500 | 1.64 | 0.538 | 0.427 | 0.676 | 0.019 | 0.003 | 1.813 → 1.193 | 0.812 → 0.724 | 0.408 → 0.354 | 1.7 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| spider | 563 | 0.00 | - | - | 0.000 | - | 1.000 |
| waf-v2 | 3000 | 0.50 | 0.878 | 0.205 | 0.157 | 0.796 | 0.820 |
