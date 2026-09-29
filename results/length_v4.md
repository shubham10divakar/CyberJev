## Length only on `data/test.jsonl`

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| phishing_url | 1998 | 0.86 | 0.521 | 0.520 | 0.544 | 0.051 | 0.026 | 0.689 → 0.689 | 0.495 → 0.496 | 0.032 → 0.036 | 0.0 |
| prompt_injection | 1900 | 1.32 | 0.656 | 0.648 | 0.579 | 0.114 | 0.007 | 0.669 → 0.662 | 0.474 → 0.470 | 0.146 → 0.138 | 0.0 |

**prompt_injection by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| neuralchemy | 900 | 0.59 | 0.760 | 0.061 | 0.161 | 0.696 | 0.755 |
| s-labs | 1000 | 0.47 | 0.362 | 0.074 | 0.140 | 0.236 | 0.508 |
