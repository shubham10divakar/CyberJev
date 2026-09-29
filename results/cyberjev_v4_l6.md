## Cyber-Jev — `runs/cyber-jev-v4-l6` on `data`

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 4700 | 1.69 | 0.968 | 0.968 | 0.994 | 0.943 | 0.799 | 0.114 → 0.095 | 0.053 → 0.051 | 0.018 → 0.008 | 0.8 |
| phishing_url | 1998 | 2.02 | 0.897 | 0.896 | 0.966 | 0.727 | 0.539 | 0.298 → 0.248 | 0.166 → 0.149 | 0.067 → 0.029 | 0.6 |
| prompt_injection | 1900 | 1.64 | 0.966 | 0.966 | 0.995 | 0.898 | 0.602 | 0.125 → 0.097 | 0.058 → 0.054 | 0.023 → 0.010 | 0.7 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| ai-waf | 1200 | 0.28 | 0.993 | 0.952 | 0.003 | 0.913 | 0.966 |
| csic2010 | 1500 | 0.60 | 0.975 | 0.866 | 0.085 | 0.935 | 0.924 |
| gretel-sql | 500 | 0.00 | - | - | 0.000 | - | 1.000 |
| web-attacks | 1500 | 0.80 | 1.000 | 0.996 | 0.010 | 0.994 | 0.990 |

**prompt_injection by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| neuralchemy | 900 | 0.59 | 0.995 | 0.915 | 0.059 | 0.975 | 0.960 |
| s-labs | 1000 | 0.47 | 0.996 | 0.947 | 0.011 | 0.949 | 0.970 |
