## One pass vs two — `runs/cyber-jev-v4-l6-url`, max_length 256

| decision | test set | variant | T | b | calib NLL | AUROC | DR@1%FPR | NLL | ECE |
|---|---|---|---|---|---|---|---|---|---|
| phishing_url | in-domain | two-pass | 1.36 | 0.00 | 0.276 | 0.958 | 0.654 | 0.261 | 0.026 |
| phishing_url | in-domain | threat-only | 0.63 | -2.13 | 0.322 | 0.942 | 0.574 | 0.307 | 0.019 |
| phishing_url | in-domain | safe-only | 0.87 | 1.93 | 0.288 | 0.956 | 0.664 | 0.270 | 0.017 |
| phishing_url | held-out | two-pass | 1.36 | 0.00 | 0.276 | 0.814 | 0.132 | 0.581 | 0.106 |
| phishing_url | held-out | threat-only | 0.63 | -2.13 | 0.322 | 0.767 | 0.126 | 0.563 | 0.058 |
| phishing_url | held-out | safe-only | 0.87 | 1.93 | 0.288 | 0.836 | 0.145 | 0.589 | 0.128 |
| phishing_url | val | two-pass | 1.36 | 0.00 | 0.276 | 0.935 | 0.505 | 0.329 | 0.023 |
| phishing_url | val | threat-only | 0.63 | -2.13 | 0.322 | 0.903 | 0.388 | 0.406 | 0.032 |
| phishing_url | val | safe-only | 0.87 | 1.93 | 0.288 | 0.940 | 0.563 | 0.320 | 0.027 |

One-pass variant picked: phishing_url → safe-only (by val AUROC)

## phishing_url, in-domain — two-pass (b = 0.00)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| phishing_url | 1998 | 1.36 | 0.877 | 0.877 | 0.958 | 0.654 | 0.469 | 0.271 → 0.261 | 0.169 → 0.164 | 0.040 → 0.026 | 0.0 |

## phishing_url, in-domain — threat-only (b = -2.13)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| phishing_url | 1998 | 0.63 | 0.854 | 0.854 | 0.942 | 0.574 | 0.431 | 0.334 → 0.307 | 0.204 → 0.195 | 0.070 → 0.019 | 0.0 |

## phishing_url, in-domain — safe-only (b = 1.93)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| phishing_url | 1998 | 0.87 | 0.881 | 0.881 | 0.956 | 0.664 | 0.434 | 0.274 → 0.270 | 0.168 → 0.167 | 0.030 → 0.017 | 0.0 |

## phishing_url, held-out — two-pass (b = 0.00)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| phishing_url | 5000 | 1.36 | 0.711 | 0.698 | 0.814 | 0.132 | 0.045 | 0.658 → 0.581 | 0.418 → 0.390 | 0.150 → 0.106 | 0.0 |

**phishing_url by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| destroylist | 2000 | 1.00 | - | - | - | 0.579 | 0.367 |
| phishtrap | 3000 | 0.50 | 0.862 | 0.226 | 0.157 | 0.756 | 0.799 |

## phishing_url, held-out — threat-only (b = -2.13)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| phishing_url | 5000 | 0.63 | 0.726 | 0.691 | 0.767 | 0.126 | 0.041 | 0.539 → 0.563 | 0.364 → 0.373 | 0.020 → 0.058 | 0.0 |

**phishing_url by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| destroylist | 2000 | 1.00 | - | - | - | 0.721 | 0.419 |
| phishtrap | 3000 | 0.50 | 0.807 | 0.199 | 0.353 | 0.811 | 0.727 |

## phishing_url, held-out — safe-only (b = 1.93)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| phishing_url | 5000 | 0.87 | 0.695 | 0.686 | 0.836 | 0.145 | 0.043 | 0.568 → 0.589 | 0.392 → 0.404 | 0.106 → 0.128 | 0.0 |

**phishing_url by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| destroylist | 2000 | 1.00 | - | - | - | 0.526 | 0.345 |
| phishtrap | 3000 | 0.50 | 0.885 | 0.247 | 0.128 | 0.743 | 0.807 |

## phishing_url, val — two-pass (b = 0.00)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| phishing_url | 3000 | 1.36 | 0.871 | 0.871 | 0.935 | 0.505 | 0.379 | 0.358 → 0.329 | 0.203 → 0.199 | 0.049 → 0.023 | 0.0 |

## phishing_url, val — threat-only (b = -2.13)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| phishing_url | 3000 | 0.63 | 0.822 | 0.822 | 0.903 | 0.388 | 0.247 | 0.403 → 0.406 | 0.255 → 0.255 | 0.039 → 0.032 | 0.0 |

## phishing_url, val — safe-only (b = 1.93)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| phishing_url | 3000 | 0.87 | 0.870 | 0.870 | 0.940 | 0.563 | 0.405 | 0.319 → 0.320 | 0.194 → 0.193 | 0.021 → 0.027 | 0.0 |
