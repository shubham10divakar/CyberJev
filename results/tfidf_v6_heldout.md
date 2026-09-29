## TF-IDF + LR on `data_heldout/test.jsonl`

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| prompt_injection | 1951 | 0.76 | 0.776 | 0.776 | 0.885 | 0.571 | 0.388 | 0.458 → 0.504 | 0.306 → 0.322 | 0.073 → 0.103 | 1.1 |

**prompt_injection by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| deepset | 662 | 0.40 | 0.873 | 0.338 | 0.033 | 0.494 | 0.741 |
| jackhhao | 1289 | 0.51 | 0.942 | 0.677 | 0.411 | 0.955 | 0.766 |
