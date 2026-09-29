## TF-IDF + LR on `data/test.jsonl`

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| prompt_injection | 2500 | 0.79 | 0.958 | 0.958 | 0.992 | 0.870 | 0.511 | 0.122 → 0.115 | 0.067 → 0.064 | 0.025 → 0.009 | 0.5 |

**prompt_injection by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| awesome-prompts | 71 | 0.00 | - | - | 0.014 | - | 0.496 |
| dolly | 222 | 0.00 | - | - | 0.000 | - | 1.000 |
| mosscap | 53 | 1.00 | - | - | - | 0.962 | 0.490 |
| neuralchemy | 900 | 0.59 | 0.994 | 0.879 | 0.051 | 0.954 | 0.951 |
| s-labs | 1000 | 0.47 | 0.990 | 0.926 | 0.008 | 0.911 | 0.954 |
| simsonsun | 128 | 1.00 | - | - | - | 0.984 | 0.496 |
| wildjailbreak | 126 | 0.93 | 0.866 | 0.385 | 0.667 | 0.966 | 0.666 |
