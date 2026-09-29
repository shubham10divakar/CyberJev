## Cyber-Jev — `runs/cyber-jev-v6-l6-s1` on `data`

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 4700 | 1.98 | 0.980 | 0.980 | 0.997 | 0.970 | 0.942 | 0.091 → 0.065 | 0.038 → 0.034 | 0.017 → 0.006 | 0.9 |
| phishing_url | 1998 | 2.45 | 0.907 | 0.907 | 0.971 | 0.721 | 0.572 | 0.323 → 0.227 | 0.154 → 0.134 | 0.066 → 0.026 | 0.6 |
| prompt_injection | 2773 | 2.07 | 0.957 | 0.957 | 0.994 | 0.884 | 0.534 | 0.193 → 0.120 | 0.077 → 0.068 | 0.035 → 0.015 | 0.9 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| ai-waf | 1200 | 0.28 | 0.998 | 0.967 | 0.005 | 0.961 | 0.982 |
| csic2010 | 1500 | 0.60 | 0.983 | 0.928 | 0.030 | 0.938 | 0.949 |
| gretel-sql | 500 | 0.00 | - | - | 0.000 | - | 1.000 |
| web-attacks | 1500 | 0.80 | 1.000 | 0.998 | 0.007 | 0.997 | 0.995 |

**prompt_injection by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| awesome-prompts | 71 | 0.00 | - | - | 0.028 | - | 0.493 |
| dolly | 222 | 0.00 | - | - | 0.005 | - | 0.499 |
| mkqa-de | 13 | 0.00 | - | - | 0.000 | - | 1.000 |
| mkqa-es | 9 | 0.00 | - | - | 0.000 | - | 1.000 |
| mkqa-fr | 14 | 0.00 | - | - | 0.000 | - | 1.000 |
| mkqa-it | 18 | 0.00 | - | - | 0.000 | - | 1.000 |
| mkqa-pt | 19 | 0.00 | - | - | 0.105 | - | 0.472 |
| mkqa-ru | 68 | 0.00 | - | - | 0.029 | - | 0.493 |
| mosscap | 53 | 1.00 | - | - | - | 0.962 | 0.490 |
| neuralchemy | 900 | 0.59 | 0.994 | 0.861 | 0.054 | 0.966 | 0.956 |
| ru-injections | 54 | 1.00 | - | - | - | 0.852 | 0.460 |
| s-labs | 1000 | 0.47 | 0.995 | 0.909 | 0.002 | 0.896 | 0.949 |
| simsonsun | 128 | 1.00 | - | - | - | 0.938 | 0.484 |
| wildjailbreak | 126 | 0.93 | 0.915 | 0.573 | 0.556 | 0.983 | 0.752 |
| yanismiraoui | 78 | 1.00 | - | - | - | 1.000 | 1.000 |
