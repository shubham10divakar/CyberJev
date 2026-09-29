## Length only on `data_heldout/test.jsonl`

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| phishing_url | 5000 | 0.86 | 0.420 | 0.404 | 0.800 | 0.121 | 0.071 | 0.699 → 0.700 | 0.506 → 0.507 | 0.129 → 0.144 | 0.0 |
| prompt_injection | 1951 | 1.32 | 0.595 | 0.556 | 0.798 | 0.162 | 0.014 | 0.953 → 0.818 | 0.589 → 0.550 | 0.238 → 0.203 | 0.0 |

**phishing_url by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| destroylist | 2000 | 1.00 | - | - | - | 0.103 | 0.093 |
| phishtrap | 3000 | 0.50 | 0.861 | 0.204 | 0.027 | 0.289 | 0.582 |

**prompt_injection by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| deepset | 662 | 0.40 | 0.813 | 0.190 | 0.336 | 0.844 | 0.735 |
| jackhhao | 1289 | 0.51 | 0.868 | 0.104 | 0.956 | 0.991 | 0.380 |
