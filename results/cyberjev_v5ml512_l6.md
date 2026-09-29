## Cyber-Jev — `runs/cyber-jev-v5ml512-l6` on `data_v5`

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 4700 | 1.71 | 0.970 | 0.970 | 0.995 | 0.953 | 0.903 | 0.111 → 0.086 | 0.054 → 0.048 | 0.024 → 0.011 | 1.0 |
| phishing_url | 1998 | 1.91 | 0.901 | 0.901 | 0.969 | 0.722 | 0.520 | 0.278 → 0.238 | 0.154 → 0.145 | 0.049 → 0.013 | 0.6 |
| prompt_injection | 2500 | 1.68 | 0.964 | 0.964 | 0.995 | 0.917 | 0.656 | 0.137 → 0.101 | 0.062 → 0.056 | 0.028 → 0.015 | 1.5 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| ai-waf | 1200 | 0.28 | 0.995 | 0.964 | 0.006 | 0.949 | 0.977 |
| csic2010 | 1500 | 0.60 | 0.969 | 0.853 | 0.020 | 0.886 | 0.922 |
| gretel-sql | 500 | 0.00 | - | - | 0.000 | - | 1.000 |
| web-attacks | 1500 | 0.80 | 1.000 | 0.998 | 0.003 | 0.997 | 0.996 |

**prompt_injection by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| awesome-prompts | 71 | 0.00 | - | - | 0.014 | - | 0.496 |
| dolly | 222 | 0.00 | - | - | 0.005 | - | 0.499 |
| mosscap | 53 | 1.00 | - | - | - | 0.943 | 0.485 |
| neuralchemy | 900 | 0.59 | 0.994 | 0.896 | 0.070 | 0.979 | 0.957 |
| s-labs | 1000 | 0.47 | 0.997 | 0.941 | 0.008 | 0.936 | 0.966 |
| simsonsun | 128 | 1.00 | - | - | - | 0.953 | 0.488 |
| wildjailbreak | 126 | 0.93 | 0.906 | 0.427 | 0.556 | 0.966 | 0.716 |
