## Cyber-Jev — `runs/cyber-jev-v6-l6` on `data`

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 4700 | 1.69 | 0.967 | 0.967 | 0.994 | 0.941 | 0.913 | 0.113 → 0.092 | 0.056 → 0.052 | 0.021 → 0.004 | 0.8 |
| phishing_url | 1998 | 1.73 | 0.894 | 0.894 | 0.963 | 0.624 | 0.434 | 0.299 → 0.254 | 0.166 → 0.153 | 0.060 → 0.029 | 0.6 |
| prompt_injection | 2773 | 1.71 | 0.950 | 0.950 | 0.991 | 0.833 | 0.692 | 0.198 → 0.145 | 0.086 → 0.079 | 0.037 → 0.017 | 0.9 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| ai-waf | 1200 | 0.28 | 0.994 | 0.949 | 0.008 | 0.946 | 0.974 |
| csic2010 | 1500 | 0.60 | 0.968 | 0.836 | 0.039 | 0.884 | 0.913 |
| gretel-sql | 500 | 0.00 | - | - | 0.000 | - | 1.000 |
| web-attacks | 1500 | 0.80 | 1.000 | 0.998 | 0.003 | 0.998 | 0.997 |

**prompt_injection by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| awesome-prompts | 71 | 0.00 | - | - | 0.000 | - | 1.000 |
| dolly | 222 | 0.00 | - | - | 0.000 | - | 1.000 |
| mkqa-de | 13 | 0.00 | - | - | 0.077 | - | 0.480 |
| mkqa-es | 9 | 0.00 | - | - | 0.000 | - | 1.000 |
| mkqa-fr | 14 | 0.00 | - | - | 0.000 | - | 1.000 |
| mkqa-it | 18 | 0.00 | - | - | 0.000 | - | 1.000 |
| mkqa-pt | 19 | 0.00 | - | - | 0.105 | - | 0.472 |
| mkqa-ru | 68 | 0.00 | - | - | 0.103 | - | 0.473 |
| mosscap | 53 | 1.00 | - | - | - | 0.925 | 0.480 |
| neuralchemy | 900 | 0.59 | 0.993 | 0.907 | 0.048 | 0.973 | 0.963 |
| ru-injections | 54 | 1.00 | - | - | - | 0.926 | 0.481 |
| s-labs | 1000 | 0.47 | 0.993 | 0.917 | 0.000 | 0.858 | 0.932 |
| simsonsun | 128 | 1.00 | - | - | - | 0.906 | 0.475 |
| wildjailbreak | 126 | 0.93 | 0.850 | 0.470 | 0.556 | 0.957 | 0.701 |
| yanismiraoui | 78 | 1.00 | - | - | - | 1.000 | 1.000 |
