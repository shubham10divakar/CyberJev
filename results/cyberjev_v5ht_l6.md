## Cyber-Jev — `runs/cyber-jev-v5ht-l6` on `data_v5`

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 4700 | 1.59 | 0.972 | 0.972 | 0.995 | 0.950 | 0.908 | 0.113 → 0.087 | 0.051 → 0.048 | 0.023 → 0.011 | 1.2 |
| phishing_url | 1998 | 2.00 | 0.894 | 0.894 | 0.969 | 0.711 | 0.357 | 0.311 → 0.247 | 0.168 → 0.152 | 0.061 → 0.017 | 0.8 |
| prompt_injection | 2500 | 1.74 | 0.964 | 0.964 | 0.994 | 0.903 | 0.472 | 0.148 → 0.105 | 0.063 → 0.057 | 0.029 → 0.013 | 1.3 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| ai-waf | 1200 | 0.28 | 0.996 | 0.970 | 0.006 | 0.955 | 0.979 |
| csic2010 | 1500 | 0.60 | 0.972 | 0.865 | 0.045 | 0.910 | 0.926 |
| gretel-sql | 500 | 0.00 | - | - | 0.000 | - | 1.000 |
| web-attacks | 1500 | 0.80 | 1.000 | 0.998 | 0.003 | 0.997 | 0.996 |

**prompt_injection by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| awesome-prompts | 71 | 0.00 | - | - | 0.014 | - | 0.496 |
| dolly | 222 | 0.00 | - | - | 0.005 | - | 0.499 |
| mosscap | 53 | 1.00 | - | - | - | 0.962 | 0.490 |
| neuralchemy | 900 | 0.59 | 0.993 | 0.915 | 0.051 | 0.973 | 0.962 |
| s-labs | 1000 | 0.47 | 0.995 | 0.953 | 0.006 | 0.917 | 0.958 |
| simsonsun | 128 | 1.00 | - | - | - | 0.977 | 0.494 |
| wildjailbreak | 126 | 0.93 | 0.890 | 0.359 | 0.667 | 0.983 | 0.697 |
