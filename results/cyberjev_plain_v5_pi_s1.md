## Plain classifier (prompt_injection, seed 1) on in-domain

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| prompt_injection | 2500 | 1.48 | 0.961 | 0.961 | 0.993 | 0.890 | 0.552 | 0.167 → 0.133 | 0.072 → 0.068 | 0.031 → 0.015 | 0.5 |

**prompt_injection by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| awesome-prompts | 71 | 0.00 | - | - | 0.000 | - | 1.000 |
| dolly | 222 | 0.00 | - | - | 0.009 | - | 0.498 |
| mosscap | 53 | 1.00 | - | - | - | 0.943 | 0.485 |
| neuralchemy | 900 | 0.59 | 0.993 | 0.901 | 0.043 | 0.964 | 0.960 |
| s-labs | 1000 | 0.47 | 0.993 | 0.902 | 0.011 | 0.907 | 0.950 |
| simsonsun | 128 | 1.00 | - | - | - | 0.984 | 0.496 |
| wildjailbreak | 126 | 0.93 | 0.946 | 0.641 | 0.556 | 0.991 | 0.773 |
