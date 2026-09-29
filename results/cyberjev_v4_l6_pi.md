## Cyber-Jev — `runs/cyber-jev-v4-l6-pi` on `data`

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| prompt_injection | 1900 | 1.71 | 0.952 | 0.952 | 0.993 | 0.887 | 0.612 | 0.196 → 0.141 | 0.084 → 0.077 | 0.037 → 0.021 | 0.7 |

**prompt_injection by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| neuralchemy | 900 | 0.59 | 0.995 | 0.913 | 0.059 | 0.972 | 0.958 |
| s-labs | 1000 | 0.47 | 0.992 | 0.870 | 0.011 | 0.898 | 0.945 |
