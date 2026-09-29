## One pass vs two — `runs/cyber-jev-v4-l6-pi`, max_length 256

| decision | test set | variant | T | b | calib NLL | AUROC | DR@1%FPR | NLL | ECE |
|---|---|---|---|---|---|---|---|---|---|
| prompt_injection | in-domain | two-pass | 1.71 | 0.00 | 0.090 | 0.993 | 0.887 | 0.141 | 0.021 |
| prompt_injection | in-domain | threat-only | 1.57 | -1.72 | 0.089 | 0.993 | 0.884 | 0.133 | 0.020 |
| prompt_injection | in-domain | safe-only | 0.14 | 0.65 | 0.106 | 0.984 | 0.725 | 0.168 | 0.020 |
| prompt_injection | held-out | two-pass | 1.71 | 0.00 | 0.090 | 0.715 | 0.018 | 0.992 | 0.233 |
| prompt_injection | held-out | threat-only | 1.57 | -1.72 | 0.089 | 0.721 | 0.004 | 1.137 | 0.268 |
| prompt_injection | held-out | safe-only | 0.14 | 0.65 | 0.106 | 0.619 | 0.077 | 1.948 | 0.376 |
| prompt_injection | val | two-pass | 1.71 | 0.00 | 0.090 | 0.558 | 0.017 | 1.165 | 0.345 |
| prompt_injection | val | threat-only | 1.57 | -1.72 | 0.089 | 0.652 | 0.011 | 1.232 | 0.379 |
| prompt_injection | val | safe-only | 0.14 | 0.65 | 0.106 | 0.331 | 0.013 | 3.772 | 0.524 |

One-pass variant picked: prompt_injection → threat-only (by val AUROC)

## prompt_injection, in-domain — two-pass (b = 0.00)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| prompt_injection | 1900 | 1.71 | 0.952 | 0.952 | 0.993 | 0.887 | 0.612 | 0.196 → 0.141 | 0.084 → 0.077 | 0.037 → 0.021 | 0.0 |

**prompt_injection by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| neuralchemy | 900 | 0.59 | 0.995 | 0.913 | 0.059 | 0.972 | 0.958 |
| s-labs | 1000 | 0.47 | 0.992 | 0.870 | 0.011 | 0.898 | 0.945 |

## prompt_injection, in-domain — threat-only (b = -1.72)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| prompt_injection | 1900 | 1.57 | 0.952 | 0.952 | 0.993 | 0.884 | 0.664 | 0.172 → 0.133 | 0.081 → 0.075 | 0.036 → 0.020 | 0.0 |

**prompt_injection by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| neuralchemy | 900 | 0.59 | 0.994 | 0.899 | 0.070 | 0.972 | 0.953 |
| s-labs | 1000 | 0.47 | 0.992 | 0.868 | 0.015 | 0.911 | 0.950 |

## prompt_injection, in-domain — safe-only (b = 0.65)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| prompt_injection | 1900 | 0.14 | 0.937 | 0.937 | 0.984 | 0.725 | 0.180 | 0.421 → 0.168 | 0.247 → 0.097 | 0.264 → 0.020 | 0.0 |

**prompt_injection by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| neuralchemy | 900 | 0.59 | 0.991 | 0.873 | 0.062 | 0.966 | 0.953 |
| s-labs | 1000 | 0.47 | 0.976 | 0.609 | 0.047 | 0.885 | 0.920 |

## prompt_injection, held-out — two-pass (b = 0.00)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| prompt_injection | 1951 | 1.71 | 0.656 | 0.631 | 0.715 | 0.018 | 0.011 | 1.540 → 0.992 | 0.603 → 0.549 | 0.288 → 0.233 | 0.0 |

**prompt_injection by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| deepset | 662 | 0.40 | 0.725 | 0.038 | 0.411 | 0.935 | 0.727 |
| jackhhao | 1289 | 0.51 | 0.714 | 0.014 | 0.759 | 0.989 | 0.555 |

## prompt_injection, held-out — threat-only (b = -1.72)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| prompt_injection | 1951 | 1.57 | 0.646 | 0.617 | 0.721 | 0.004 | 0.000 | 1.683 → 1.137 | 0.635 → 0.587 | 0.309 → 0.268 | 0.0 |

**prompt_injection by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| deepset | 662 | 0.40 | 0.699 | 0.008 | 0.426 | 0.954 | 0.725 |
| jackhhao | 1289 | 0.51 | 0.739 | 0.008 | 0.790 | 0.992 | 0.531 |

## prompt_injection, held-out — safe-only (b = 0.65)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| prompt_injection | 1951 | 0.14 | 0.537 | 0.508 | 0.619 | 0.077 | 0.027 | 0.714 → 1.948 | 0.519 → 0.803 | 0.108 → 0.376 | 0.0 |

**prompt_injection by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| deepset | 662 | 0.40 | 0.867 | 0.186 | 0.401 | 0.939 | 0.734 |
| jackhhao | 1289 | 0.51 | 0.497 | 0.069 | 0.922 | 0.785 | 0.352 |

## prompt_injection, val — two-pass (b = 0.00)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| prompt_injection | 1500 | 1.71 | 0.521 | 0.393 | 0.558 | 0.017 | 0.000 | 1.798 → 1.165 | 0.853 → 0.743 | 0.420 → 0.345 | 0.0 |

## prompt_injection, val — threat-only (b = -1.72)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| prompt_injection | 1500 | 1.57 | 0.521 | 0.391 | 0.652 | 0.011 | 0.000 | 1.809 → 1.232 | 0.863 → 0.768 | 0.433 → 0.379 | 0.0 |

## prompt_injection, val — safe-only (b = 0.65)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| prompt_injection | 1500 | 0.14 | 0.428 | 0.331 | 0.331 | 0.013 | 0.000 | 0.903 → 3.772 | 0.677 → 1.065 | 0.265 → 0.524 | 0.0 |
