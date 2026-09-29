## Plain classifier (prompt_injection, seed 0) on in-domain

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| prompt_injection | 2500 | 1.31 | 0.951 | 0.951 | 0.993 | 0.894 | 0.590 | 0.178 → 0.156 | 0.085 → 0.081 | 0.034 → 0.020 | 0.5 |

**prompt_injection by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| awesome-prompts | 71 | 0.00 | - | - | 0.000 | - | 1.000 |
| dolly | 222 | 0.00 | - | - | 0.000 | - | 1.000 |
| mosscap | 53 | 1.00 | - | - | - | 0.925 | 0.480 |
| neuralchemy | 900 | 0.59 | 0.993 | 0.903 | 0.038 | 0.958 | 0.959 |
| s-labs | 1000 | 0.47 | 0.992 | 0.866 | 0.008 | 0.860 | 0.929 |
| simsonsun | 128 | 1.00 | - | - | - | 0.977 | 0.494 |
| wildjailbreak | 126 | 0.93 | 0.906 | 0.650 | 0.778 | 0.974 | 0.622 |
