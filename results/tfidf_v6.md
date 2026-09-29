## TF-IDF + LR on `data/test.jsonl`

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| prompt_injection | 2773 | 0.76 | 0.959 | 0.959 | 0.992 | 0.889 | 0.417 | 0.123 → 0.115 | 0.066 → 0.064 | 0.024 → 0.009 | 0.5 |

**prompt_injection by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| awesome-prompts | 71 | 0.00 | - | - | 0.042 | - | 0.489 |
| dolly | 222 | 0.00 | - | - | 0.000 | - | 1.000 |
| mkqa-de | 13 | 0.00 | - | - | 0.000 | - | 1.000 |
| mkqa-es | 9 | 0.00 | - | - | 0.000 | - | 1.000 |
| mkqa-fr | 14 | 0.00 | - | - | 0.000 | - | 1.000 |
| mkqa-it | 18 | 0.00 | - | - | 0.000 | - | 1.000 |
| mkqa-pt | 19 | 0.00 | - | - | 0.000 | - | 1.000 |
| mkqa-ru | 68 | 0.00 | - | - | 0.059 | - | 0.485 |
| mosscap | 53 | 1.00 | - | - | - | 0.962 | 0.490 |
| neuralchemy | 900 | 0.59 | 0.993 | 0.901 | 0.046 | 0.949 | 0.950 |
| ru-injections | 54 | 1.00 | - | - | - | 0.981 | 0.495 |
| s-labs | 1000 | 0.47 | 0.989 | 0.915 | 0.009 | 0.904 | 0.950 |
| simsonsun | 128 | 1.00 | - | - | - | 0.984 | 0.496 |
| wildjailbreak | 126 | 0.93 | 0.869 | 0.350 | 0.667 | 0.983 | 0.697 |
| yanismiraoui | 78 | 1.00 | - | - | - | 1.000 | 1.000 |
