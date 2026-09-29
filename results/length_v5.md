## Length only on `data/test.jsonl`

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| prompt_injection | 2500 | 1.98 | 0.538 | 0.524 | 0.537 | 0.011 | 0.000 | 0.692 → 0.692 | 0.499 → 0.498 | 0.012 → 0.026 | 0.0 |

**prompt_injection by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| awesome-prompts | 71 | 0.00 | - | - | 1.000 | - | 0.000 |
| dolly | 222 | 0.00 | - | - | 1.000 | - | 0.000 |
| mosscap | 53 | 1.00 | - | - | - | 1.000 | 1.000 |
| neuralchemy | 900 | 0.59 | 0.760 | 0.061 | 0.032 | 0.273 | 0.534 |
| s-labs | 1000 | 0.47 | 0.362 | 0.074 | 0.000 | 0.030 | 0.378 |
| simsonsun | 128 | 1.00 | - | - | - | 1.000 | 1.000 |
| wildjailbreak | 126 | 0.93 | 0.397 | 0.171 | 1.000 | 1.000 | 0.481 |
