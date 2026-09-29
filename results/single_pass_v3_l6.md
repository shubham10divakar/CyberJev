## One pass vs two — `runs/cyber-jev-v3-l6`, max_length 256

| decision | test set | variant | T | b | calib NLL | AUROC | DR@1%FPR | NLL | ECE |
|---|---|---|---|---|---|---|---|---|---|
| http_attack | in-domain | two-pass | 1.81 | 0.00 | 0.067 | 0.997 | 0.968 | 0.067 | 0.007 |
| http_attack | in-domain | threat-only | 1.13 | -4.69 | 0.082 | 0.995 | 0.968 | 0.082 | 0.004 |
| http_attack | in-domain | safe-only | 0.64 | 5.30 | 0.077 | 0.997 | 0.968 | 0.070 | 0.008 |
| http_attack | held-out | two-pass | 1.81 | 0.00 | 0.067 | 0.949 | 0.030 | 0.438 | 0.083 |
| http_attack | held-out | threat-only | 1.13 | -4.69 | 0.082 | 0.928 | 0.021 | 0.523 | 0.090 |
| http_attack | held-out | safe-only | 0.64 | 5.30 | 0.077 | 0.980 | 0.620 | 0.278 | 0.054 |
| http_attack | val | two-pass | 1.81 | 0.00 | 0.067 | 0.909 | 0.169 | 0.611 | 0.167 |
| http_attack | val | threat-only | 1.13 | -4.69 | 0.082 | 0.910 | 0.238 | 0.546 | 0.120 |
| http_attack | val | safe-only | 0.64 | 5.30 | 0.077 | 0.893 | 0.164 | 0.691 | 0.183 |

One-pass variant picked: http_attack → threat-only (by val AUROC)

## http_attack, in-domain — two-pass (b = 0.00)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 4700 | 1.81 | 0.978 | 0.978 | 0.997 | 0.968 | 0.941 | 0.089 → 0.067 | 0.039 → 0.036 | 0.017 → 0.007 | 0.0 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| ai-waf | 1200 | 0.28 | 0.996 | 0.958 | 0.014 | 0.961 | 0.974 |
| csic2010 | 1500 | 0.60 | 0.986 | 0.910 | 0.022 | 0.936 | 0.951 |
| gretel-sql | 500 | 0.00 | - | - | 0.002 | - | 0.499 |
| web-attacks | 1500 | 0.80 | 1.000 | 0.998 | 0.007 | 0.997 | 0.995 |

## http_attack, in-domain — threat-only (b = -4.69)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 4700 | 1.13 | 0.978 | 0.978 | 0.995 | 0.968 | 0.881 | 0.084 → 0.082 | 0.040 → 0.039 | 0.009 → 0.004 | 0.0 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| ai-waf | 1200 | 0.28 | 0.991 | 0.958 | 0.012 | 0.958 | 0.975 |
| csic2010 | 1500 | 0.60 | 0.984 | 0.907 | 0.020 | 0.934 | 0.951 |
| gretel-sql | 500 | 0.00 | - | - | 0.002 | - | 0.499 |
| web-attacks | 1500 | 0.80 | 1.000 | 0.997 | 0.007 | 0.997 | 0.995 |

## http_attack, in-domain — safe-only (b = 5.30)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 4700 | 0.64 | 0.979 | 0.979 | 0.997 | 0.968 | 0.931 | 0.090 → 0.070 | 0.041 → 0.036 | 0.037 → 0.008 | 0.0 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| ai-waf | 1200 | 0.28 | 0.995 | 0.961 | 0.010 | 0.961 | 0.977 |
| csic2010 | 1500 | 0.60 | 0.985 | 0.919 | 0.023 | 0.935 | 0.950 |
| gretel-sql | 500 | 0.00 | - | - | 0.002 | - | 0.499 |
| web-attacks | 1500 | 0.80 | 1.000 | 0.998 | 0.000 | 0.997 | 0.996 |

## http_attack, held-out — two-pass (b = 0.00)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 10320 | 1.81 | 0.881 | 0.879 | 0.949 | 0.030 | 0.007 | 0.737 → 0.438 | 0.215 → 0.200 | 0.103 → 0.083 | 0.0 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| dvwa-juiceshop | 4320 | 0.73 | 0.852 | 0.001 | 0.308 | 0.974 | 0.859 |
| sqli-queries | 6000 | 0.36 | 0.988 | 0.794 | 0.203 | 0.993 | 0.865 |

## http_attack, held-out — threat-only (b = -4.69)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 10320 | 1.13 | 0.873 | 0.870 | 0.928 | 0.021 | 0.006 | 0.577 → 0.523 | 0.228 → 0.225 | 0.097 → 0.090 | 0.0 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| dvwa-juiceshop | 4320 | 0.73 | 0.842 | 0.000 | 0.338 | 0.971 | 0.844 |
| sqli-queries | 6000 | 0.36 | 0.974 | 0.589 | 0.215 | 0.994 | 0.858 |

## http_attack, held-out — safe-only (b = 5.30)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 10320 | 0.64 | 0.917 | 0.917 | 0.980 | 0.620 | 0.425 | 0.227 → 0.278 | 0.132 → 0.141 | 0.021 → 0.054 | 0.0 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| dvwa-juiceshop | 4320 | 0.73 | 0.947 | 0.564 | 0.195 | 0.975 | 0.906 |
| sqli-queries | 6000 | 0.36 | 0.994 | 0.937 | 0.138 | 0.991 | 0.905 |

## http_attack, val — two-pass (b = 0.00)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 3563 | 1.81 | 0.765 | 0.765 | 0.909 | 0.169 | 0.035 | 1.003 → 0.611 | 0.399 → 0.346 | 0.202 → 0.167 | 0.0 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| spider | 563 | 0.00 | - | - | 0.000 | - | 1.000 |
| waf-v2 | 3000 | 0.50 | 0.875 | 0.129 | 0.451 | 0.893 | 0.713 |

## http_attack, val — threat-only (b = -4.69)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 3563 | 1.13 | 0.794 | 0.794 | 0.910 | 0.238 | 0.029 | 0.592 → 0.546 | 0.308 → 0.300 | 0.130 → 0.120 | 0.0 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| spider | 563 | 0.00 | - | - | 0.000 | - | 1.000 |
| waf-v2 | 3000 | 0.50 | 0.877 | 0.147 | 0.371 | 0.883 | 0.752 |

## http_attack, val — safe-only (b = 5.30)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 3563 | 0.64 | 0.767 | 0.767 | 0.893 | 0.164 | 0.047 | 0.516 → 0.691 | 0.337 → 0.383 | 0.140 → 0.183 | 0.0 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| spider | 563 | 0.00 | - | - | 0.000 | - | 1.000 |
| waf-v2 | 3000 | 0.50 | 0.853 | 0.164 | 0.445 | 0.891 | 0.715 |
