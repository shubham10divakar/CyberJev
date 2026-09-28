## TF-IDF + LR on `data`

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 4200 | 0.45 | 0.963 | 0.962 | 0.996 | 0.938 | 0.890 | 0.108 → 0.081 | 0.058 → 0.050 | 0.040 → 0.006 | 0.3 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| ai-waf | 1200 | 0.28 | 1.000 | 1.000 | 0.000 | 0.982 | 0.994 |
| csic2010 | 1500 | 0.60 | 0.974 | 0.834 | 0.082 | 0.899 | 0.904 |
| web-attacks | 1500 | 0.80 | 1.000 | 1.000 | 0.030 | 1.000 | 0.991 |
