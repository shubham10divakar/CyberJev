## Plain classifier (prompt_injection, seed 2) on in-domain

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| prompt_injection | 2500 | 1.49 | 0.959 | 0.959 | 0.994 | 0.880 | 0.758 | 0.181 → 0.139 | 0.075 → 0.070 | 0.034 → 0.020 | 0.5 |

**prompt_injection by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| awesome-prompts | 71 | 0.00 | - | - | 0.014 | - | 0.496 |
| dolly | 222 | 0.00 | - | - | 0.014 | - | 0.497 |
| mosscap | 53 | 1.00 | - | - | - | 1.000 | 1.000 |
| neuralchemy | 900 | 0.59 | 0.996 | 0.898 | 0.062 | 0.975 | 0.959 |
| s-labs | 1000 | 0.47 | 0.992 | 0.909 | 0.002 | 0.885 | 0.944 |
| simsonsun | 128 | 1.00 | - | - | - | 1.000 | 1.000 |
| wildjailbreak | 126 | 0.93 | 0.930 | 0.786 | 0.667 | 0.991 | 0.716 |
