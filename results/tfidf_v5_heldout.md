## TF-IDF + LR on `data_heldout/test.jsonl`

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| prompt_injection | 1951 | 0.79 | 0.777 | 0.777 | 0.880 | 0.556 | 0.399 | 0.456 → 0.492 | 0.304 → 0.318 | 0.071 → 0.097 | 1.1 |

**prompt_injection by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| deepset | 662 | 0.40 | 0.859 | 0.319 | 0.033 | 0.445 | 0.712 |
| jackhhao | 1289 | 0.51 | 0.939 | 0.670 | 0.381 | 0.949 | 0.779 |
