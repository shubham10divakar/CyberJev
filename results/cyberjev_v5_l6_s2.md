## Cyber-Jev — `runs/cyber-jev-v5-l6-s2` on `data_v5`

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 4700 | 1.49 | 0.968 | 0.968 | 0.995 | 0.947 | 0.919 | 0.095 → 0.085 | 0.053 → 0.049 | 0.018 → 0.008 | 0.9 |
| phishing_url | 1998 | 1.73 | 0.905 | 0.905 | 0.968 | 0.727 | 0.513 | 0.251 → 0.227 | 0.144 → 0.139 | 0.039 → 0.014 | 0.6 |
| prompt_injection | 2500 | 1.75 | 0.962 | 0.962 | 0.994 | 0.902 | 0.744 | 0.154 → 0.111 | 0.066 → 0.061 | 0.029 → 0.013 | 0.9 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| ai-waf | 1200 | 0.28 | 0.994 | 0.946 | 0.008 | 0.946 | 0.974 |
| csic2010 | 1500 | 0.60 | 0.972 | 0.863 | 0.015 | 0.879 | 0.920 |
| gretel-sql | 500 | 0.00 | - | - | 0.002 | - | 0.499 |
| web-attacks | 1500 | 0.80 | 1.000 | 0.996 | 0.007 | 0.996 | 0.993 |

**prompt_injection by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| awesome-prompts | 71 | 0.00 | - | - | 0.014 | - | 0.496 |
| dolly | 222 | 0.00 | - | - | 0.000 | - | 1.000 |
| mosscap | 53 | 1.00 | - | - | - | 0.962 | 0.490 |
| neuralchemy | 900 | 0.59 | 0.993 | 0.909 | 0.046 | 0.973 | 0.964 |
| s-labs | 1000 | 0.47 | 0.995 | 0.909 | 0.006 | 0.902 | 0.950 |
| simsonsun | 128 | 1.00 | - | - | - | 0.969 | 0.492 |
| wildjailbreak | 126 | 0.93 | 0.913 | 0.521 | 0.556 | 0.974 | 0.733 |
