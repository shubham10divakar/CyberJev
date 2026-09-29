## One pass vs two — `runs/cyber-jev-v2-l6`, max_length 256

| decision | test set | variant | T | b | calib NLL | AUROC | DR@1%FPR | NLL | ECE |
|---|---|---|---|---|---|---|---|---|---|
| http_attack | in-domain | two-pass | 1.88 | 0.00 | 0.084 | 0.995 | 0.968 | 0.077 | 0.003 |
| http_attack | in-domain | threat-only | 1.32 | -3.10 | 0.099 | 0.990 | 0.968 | 0.091 | 0.003 |
| http_attack | in-domain | safe-only | 0.65 | 4.73 | 0.110 | 0.995 | 0.968 | 0.096 | 0.010 |
| http_attack | held-out | two-pass | 1.88 | 0.00 | 0.084 | 0.953 | 0.457 | 0.680 | 0.145 |
| http_attack | held-out | threat-only | 1.32 | -3.10 | 0.099 | 0.945 | 0.393 | 0.640 | 0.148 |
| http_attack | held-out | safe-only | 0.65 | 4.73 | 0.110 | 0.958 | 0.572 | 0.399 | 0.100 |
| http_attack | val | two-pass | 1.88 | 0.00 | 0.084 | 0.856 | 0.229 | 0.910 | 0.223 |
| http_attack | val | threat-only | 1.32 | -3.10 | 0.099 | 0.866 | 0.249 | 0.869 | 0.226 |
| http_attack | val | safe-only | 0.65 | 4.73 | 0.110 | 0.830 | 0.131 | 0.673 | 0.131 |

One-pass variant picked: http_attack → threat-only (by val AUROC)

## http_attack, in-domain — two-pass (b = 0.00)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 4200 | 1.88 | 0.975 | 0.975 | 0.995 | 0.968 | 0.928 | 0.103 → 0.077 | 0.045 → 0.041 | 0.020 → 0.003 | 0.0 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| ai-waf | 1200 | 0.28 | 0.994 | 0.946 | 0.018 | 0.955 | 0.968 |
| csic2010 | 1500 | 0.60 | 0.984 | 0.930 | 0.028 | 0.939 | 0.950 |
| web-attacks | 1500 | 0.80 | 1.000 | 1.000 | 0.003 | 1.000 | 0.999 |

## http_attack, in-domain — threat-only (b = -3.10)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 4200 | 1.32 | 0.976 | 0.975 | 0.990 | 0.968 | 0.800 | 0.099 → 0.091 | 0.044 → 0.043 | 0.016 → 0.003 | 0.0 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| ai-waf | 1200 | 0.28 | 0.988 | 0.946 | 0.020 | 0.955 | 0.967 |
| csic2010 | 1500 | 0.60 | 0.982 | 0.932 | 0.018 | 0.937 | 0.953 |
| web-attacks | 1500 | 0.80 | 1.000 | 1.000 | 0.007 | 1.000 | 0.998 |

## http_attack, in-domain — safe-only (b = 4.73)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 4200 | 0.65 | 0.972 | 0.971 | 0.995 | 0.968 | 0.897 | 0.123 → 0.096 | 0.054 → 0.046 | 0.051 → 0.010 | 0.0 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| ai-waf | 1200 | 0.28 | 0.994 | 0.943 | 0.007 | 0.943 | 0.974 |
| csic2010 | 1500 | 0.60 | 0.983 | 0.905 | 0.080 | 0.949 | 0.935 |
| web-attacks | 1500 | 0.80 | 1.000 | 1.000 | 0.000 | 1.000 | 1.000 |

## http_attack, held-out — two-pass (b = 0.00)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 10320 | 1.88 | 0.812 | 0.805 | 0.953 | 0.457 | 0.196 | 1.208 → 0.680 | 0.352 → 0.330 | 0.169 → 0.145 | 0.0 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| dvwa-juiceshop | 4320 | 0.73 | 0.975 | 0.823 | 0.212 | 0.965 | 0.891 |
| sqli-queries | 6000 | 0.36 | 0.992 | 0.811 | 0.413 | 0.999 | 0.737 |

## http_attack, held-out — threat-only (b = -3.10)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 10320 | 1.32 | 0.803 | 0.794 | 0.945 | 0.393 | 0.111 | 0.805 → 0.640 | 0.353 → 0.338 | 0.166 → 0.148 | 0.0 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| dvwa-juiceshop | 4320 | 0.73 | 0.965 | 0.684 | 0.209 | 0.961 | 0.888 |
| sqli-queries | 6000 | 0.36 | 0.987 | 0.678 | 0.437 | 0.999 | 0.721 |

## http_attack, held-out — safe-only (b = 4.73)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 10320 | 0.65 | 0.850 | 0.846 | 0.958 | 0.572 | 0.406 | 0.331 → 0.399 | 0.213 → 0.238 | 0.081 → 0.100 | 0.0 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| dvwa-juiceshop | 4320 | 0.73 | 0.981 | 0.876 | 0.110 | 0.936 | 0.904 |
| sqli-queries | 6000 | 0.36 | 0.995 | 0.888 | 0.319 | 0.998 | 0.795 |

## http_attack, val — two-pass (b = 0.00)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 3563 | 1.88 | 0.707 | 0.706 | 0.856 | 0.229 | 0.064 | 1.596 → 0.910 | 0.525 → 0.474 | 0.260 → 0.223 | 0.0 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| spider | 563 | 0.00 | - | - | 0.549 | - | 0.311 |
| waf-v2 | 3000 | 0.50 | 0.885 | 0.305 | 0.398 | 0.909 | 0.749 |

## http_attack, val — threat-only (b = -3.10)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 3563 | 1.32 | 0.710 | 0.709 | 0.866 | 0.249 | 0.087 | 1.094 → 0.869 | 0.505 → 0.477 | 0.248 → 0.226 | 0.0 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| spider | 563 | 0.00 | - | - | 0.538 | - | 0.316 |
| waf-v2 | 3000 | 0.50 | 0.886 | 0.266 | 0.399 | 0.912 | 0.750 |

## http_attack, val — safe-only (b = 4.73)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 3563 | 0.65 | 0.779 | 0.776 | 0.830 | 0.131 | 0.055 | 0.540 → 0.673 | 0.333 → 0.357 | 0.074 → 0.131 | 0.0 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| spider | 563 | 0.00 | - | - | 0.471 | - | 0.346 |
| waf-v2 | 3000 | 0.50 | 0.878 | 0.271 | 0.139 | 0.789 | 0.825 |
