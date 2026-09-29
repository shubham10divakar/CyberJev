## Cyber-Jev — `runs/cyber-jev-v6-l6-s2` on `data`

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 4700 | 1.72 | 0.977 | 0.977 | 0.996 | 0.966 | 0.932 | 0.094 → 0.073 | 0.041 → 0.038 | 0.018 → 0.006 | 0.8 |
| phishing_url | 1998 | 2.07 | 0.914 | 0.914 | 0.968 | 0.701 | 0.405 | 0.295 → 0.234 | 0.144 → 0.137 | 0.050 → 0.014 | 0.6 |
| prompt_injection | 2773 | 2.06 | 0.961 | 0.961 | 0.994 | 0.896 | 0.496 | 0.169 → 0.109 | 0.067 → 0.060 | 0.030 → 0.012 | 0.9 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| ai-waf | 1200 | 0.28 | 0.994 | 0.940 | 0.014 | 0.952 | 0.971 |
| csic2010 | 1500 | 0.60 | 0.983 | 0.925 | 0.022 | 0.931 | 0.948 |
| gretel-sql | 500 | 0.00 | - | - | 0.000 | - | 1.000 |
| web-attacks | 1500 | 0.80 | 1.000 | 0.998 | 0.007 | 0.998 | 0.996 |

**prompt_injection by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| awesome-prompts | 71 | 0.00 | - | - | 0.028 | - | 0.493 |
| dolly | 222 | 0.00 | - | - | 0.000 | - | 1.000 |
| mkqa-de | 13 | 0.00 | - | - | 0.000 | - | 1.000 |
| mkqa-es | 9 | 0.00 | - | - | 0.000 | - | 1.000 |
| mkqa-fr | 14 | 0.00 | - | - | 0.000 | - | 1.000 |
| mkqa-it | 18 | 0.00 | - | - | 0.000 | - | 1.000 |
| mkqa-pt | 19 | 0.00 | - | - | 0.000 | - | 1.000 |
| mkqa-ru | 68 | 0.00 | - | - | 0.029 | - | 0.493 |
| mosscap | 53 | 1.00 | - | - | - | 0.943 | 0.485 |
| neuralchemy | 900 | 0.59 | 0.994 | 0.867 | 0.043 | 0.972 | 0.965 |
| ru-injections | 54 | 1.00 | - | - | - | 0.870 | 0.465 |
| s-labs | 1000 | 0.47 | 0.994 | 0.924 | 0.004 | 0.896 | 0.948 |
| simsonsun | 128 | 1.00 | - | - | - | 0.969 | 0.492 |
| wildjailbreak | 126 | 0.93 | 0.928 | 0.598 | 0.556 | 0.983 | 0.752 |
| yanismiraoui | 78 | 1.00 | - | - | - | 1.000 | 1.000 |
