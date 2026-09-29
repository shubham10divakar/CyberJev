## TF-IDF + LR on `data/test.jsonl`

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| phishing_url | 1998 | 0.89 | 0.891 | 0.891 | 0.960 | 0.692 | 0.517 | 0.255 → 0.251 | 0.156 → 0.155 | 0.023 → 0.009 | 0.1 |
| prompt_injection | 1900 | 0.71 | 0.955 | 0.955 | 0.992 | 0.899 | 0.541 | 0.128 → 0.122 | 0.071 → 0.070 | 0.023 → 0.012 | 0.1 |

**prompt_injection by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| neuralchemy | 900 | 0.59 | 0.994 | 0.924 | 0.051 | 0.962 | 0.955 |
| s-labs | 1000 | 0.47 | 0.991 | 0.926 | 0.008 | 0.909 | 0.953 |
