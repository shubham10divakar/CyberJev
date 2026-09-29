## TF-IDF + LR on `data_heldout/test.jsonl`

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| phishing_url | 5000 | 0.89 | 0.641 | 0.619 | 0.710 | 0.072 | 0.003 | 0.701 → 0.731 | 0.478 → 0.489 | 0.141 → 0.156 | 0.0 |
| prompt_injection | 1951 | 0.71 | 0.734 | 0.731 | 0.887 | 0.580 | 0.328 | 0.546 → 0.644 | 0.362 → 0.388 | 0.105 → 0.142 | 1.1 |

**phishing_url by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| destroylist | 2000 | 1.00 | - | - | - | 0.548 | 0.354 |
| phishtrap | 3000 | 0.50 | 0.780 | 0.122 | 0.336 | 0.743 | 0.703 |

**prompt_injection by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| deepset | 662 | 0.40 | 0.904 | 0.361 | 0.063 | 0.650 | 0.805 |
| jackhhao | 1289 | 0.51 | 0.952 | 0.727 | 0.613 | 0.983 | 0.656 |
