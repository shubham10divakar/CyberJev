## Cyber-Jev — `runs/cyber-jev-v5-l6` on `data`

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 4700 | 1.83 | 0.975 | 0.975 | 0.995 | 0.960 | 0.873 | 0.113 → 0.081 | 0.047 → 0.043 | 0.021 → 0.007 | 0.8 |
| phishing_url | 1998 | 1.82 | 0.895 | 0.895 | 0.966 | 0.670 | 0.358 | 0.295 → 0.248 | 0.165 → 0.153 | 0.058 → 0.025 | 0.6 |
| prompt_injection | 2500 | 1.60 | 0.960 | 0.960 | 0.994 | 0.886 | 0.527 | 0.164 → 0.122 | 0.069 → 0.065 | 0.031 → 0.017 | 0.9 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| ai-waf | 1200 | 0.28 | 0.993 | 0.949 | 0.002 | 0.931 | 0.974 |
| csic2010 | 1500 | 0.60 | 0.976 | 0.870 | 0.025 | 0.919 | 0.940 |
| gretel-sql | 500 | 0.00 | - | - | 0.000 | - | 1.000 |
| web-attacks | 1500 | 0.80 | 1.000 | 0.998 | 0.003 | 0.998 | 0.997 |

**prompt_injection by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| awesome-prompts | 71 | 0.00 | - | - | 0.028 | - | 0.493 |
| dolly | 222 | 0.00 | - | - | 0.000 | - | 1.000 |
| mosscap | 53 | 1.00 | - | - | - | 0.962 | 0.490 |
| neuralchemy | 900 | 0.59 | 0.992 | 0.911 | 0.040 | 0.964 | 0.961 |
| s-labs | 1000 | 0.47 | 0.996 | 0.934 | 0.008 | 0.909 | 0.953 |
| simsonsun | 128 | 1.00 | - | - | - | 0.961 | 0.490 |
| wildjailbreak | 126 | 0.93 | 0.906 | 0.402 | 0.556 | 0.966 | 0.716 |
