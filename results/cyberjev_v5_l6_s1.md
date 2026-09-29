## Cyber-Jev — `runs/cyber-jev-v5-l6-s1` on `data_v5`

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 4700 | 1.20 | 0.970 | 0.970 | 0.995 | 0.951 | 0.930 | 0.088 → 0.087 | 0.049 → 0.049 | 0.013 → 0.010 | 0.9 |
| phishing_url | 1998 | 1.46 | 0.909 | 0.909 | 0.967 | 0.685 | 0.457 | 0.252 → 0.238 | 0.147 → 0.142 | 0.040 → 0.017 | 0.6 |
| prompt_injection | 2500 | 1.31 | 0.967 | 0.967 | 0.994 | 0.893 | 0.554 | 0.122 → 0.108 | 0.059 → 0.057 | 0.023 → 0.014 | 0.9 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| ai-waf | 1200 | 0.28 | 0.993 | 0.955 | 0.005 | 0.946 | 0.977 |
| csic2010 | 1500 | 0.60 | 0.972 | 0.868 | 0.028 | 0.889 | 0.920 |
| gretel-sql | 500 | 0.00 | - | - | 0.000 | - | 1.000 |
| web-attacks | 1500 | 0.80 | 1.000 | 0.998 | 0.003 | 0.998 | 0.997 |

**prompt_injection by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| awesome-prompts | 71 | 0.00 | - | - | 0.028 | - | 0.493 |
| dolly | 222 | 0.00 | - | - | 0.000 | - | 1.000 |
| mosscap | 53 | 1.00 | - | - | - | 0.962 | 0.490 |
| neuralchemy | 900 | 0.59 | 0.991 | 0.894 | 0.046 | 0.975 | 0.966 |
| s-labs | 1000 | 0.47 | 0.996 | 0.936 | 0.006 | 0.924 | 0.961 |
| simsonsun | 128 | 1.00 | - | - | - | 0.984 | 0.496 |
| wildjailbreak | 126 | 0.93 | 0.917 | 0.735 | 0.556 | 0.974 | 0.733 |
