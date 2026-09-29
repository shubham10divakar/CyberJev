## One pass vs two — `runs/cyber-jev-v2-l6-s1`, max_length 256

| decision | test set | variant | T | b | calib NLL | AUROC | DR@1%FPR | NLL | ECE |
|---|---|---|---|---|---|---|---|---|---|
| http_attack | in-domain | two-pass | 1.70 | 0.00 | 0.089 | 0.994 | 0.949 | 0.095 | 0.005 |
| http_attack | in-domain | threat-only | 1.14 | -5.20 | 0.117 | 0.976 | 0.945 | 0.126 | 0.009 |
| http_attack | in-domain | safe-only | 0.77 | 5.51 | 0.183 | 0.991 | 0.924 | 0.191 | 0.071 |
| http_attack | held-out | two-pass | 1.70 | 0.00 | 0.089 | 0.944 | 0.264 | 0.581 | 0.119 |
| http_attack | held-out | threat-only | 1.14 | -5.20 | 0.117 | 0.913 | 0.162 | 0.935 | 0.183 |
| http_attack | held-out | safe-only | 0.77 | 5.51 | 0.183 | 0.963 | 0.487 | 0.276 | 0.048 |
| http_attack | val | two-pass | 1.70 | 0.00 | 0.089 | 0.833 | 0.135 | 0.828 | 0.153 |
| http_attack | val | threat-only | 1.14 | -5.20 | 0.117 | 0.834 | 0.123 | 0.925 | 0.164 |
| http_attack | val | safe-only | 0.77 | 5.51 | 0.183 | 0.817 | 0.093 | 0.622 | 0.105 |

One-pass variant picked: http_attack → threat-only (by val AUROC)

## http_attack, in-domain — two-pass (b = 0.00)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 4200 | 1.70 | 0.966 | 0.965 | 0.994 | 0.949 | 0.923 | 0.118 → 0.095 | 0.058 → 0.055 | 0.022 → 0.005 | 0.0 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| ai-waf | 1200 | 0.28 | 0.995 | 0.952 | 0.007 | 0.949 | 0.976 |
| csic2010 | 1500 | 0.60 | 0.970 | 0.859 | 0.032 | 0.889 | 0.919 |
| web-attacks | 1500 | 0.80 | 1.000 | 1.000 | 0.003 | 0.999 | 0.998 |

## http_attack, in-domain — threat-only (b = -5.20)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 4200 | 1.14 | 0.964 | 0.963 | 0.976 | 0.945 | 0.881 | 0.130 → 0.126 | 0.065 → 0.064 | 0.018 → 0.009 | 0.0 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| ai-waf | 1200 | 0.28 | 0.988 | 0.949 | 0.013 | 0.949 | 0.971 |
| csic2010 | 1500 | 0.60 | 0.954 | 0.859 | 0.025 | 0.884 | 0.918 |
| web-attacks | 1500 | 0.80 | 1.000 | 1.000 | 0.010 | 1.000 | 0.997 |

## http_attack, in-domain — safe-only (b = 5.51)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 4200 | 0.77 | 0.923 | 0.919 | 0.991 | 0.924 | 0.855 | 0.201 → 0.191 | 0.110 → 0.111 | 0.095 → 0.071 | 0.0 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| ai-waf | 1200 | 0.28 | 0.996 | 0.955 | 0.003 | 0.934 | 0.974 |
| csic2010 | 1500 | 0.60 | 0.962 | 0.805 | 0.461 | 0.979 | 0.772 |
| web-attacks | 1500 | 0.80 | 1.000 | 0.999 | 0.000 | 0.996 | 0.995 |

## http_attack, held-out — two-pass (b = 0.00)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 10320 | 1.70 | 0.832 | 0.827 | 0.944 | 0.264 | 0.031 | 0.920 → 0.581 | 0.301 → 0.283 | 0.141 → 0.119 | 0.0 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| dvwa-juiceshop | 4320 | 0.73 | 0.921 | 0.312 | 0.311 | 0.954 | 0.841 |
| sqli-queries | 6000 | 0.36 | 0.981 | 0.321 | 0.320 | 0.998 | 0.795 |

## http_attack, held-out — threat-only (b = -5.20)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 10320 | 1.14 | 0.750 | 0.733 | 0.913 | 0.162 | 0.008 | 1.042 → 0.935 | 0.437 → 0.430 | 0.192 → 0.183 | 0.0 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| dvwa-juiceshop | 4320 | 0.73 | 0.885 | 0.166 | 0.337 | 0.946 | 0.823 |
| sqli-queries | 6000 | 0.36 | 0.970 | 0.233 | 0.529 | 1.000 | 0.662 |

## http_attack, held-out — safe-only (b = 5.51)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 10320 | 0.77 | 0.888 | 0.887 | 0.963 | 0.487 | 0.037 | 0.269 → 0.276 | 0.162 → 0.167 | 0.049 → 0.048 | 0.0 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| dvwa-juiceshop | 4320 | 0.73 | 0.956 | 0.678 | 0.231 | 0.932 | 0.855 |
| sqli-queries | 6000 | 0.36 | 0.990 | 0.806 | 0.174 | 0.997 | 0.885 |

## http_attack, val — two-pass (b = 0.00)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 3563 | 1.70 | 0.777 | 0.775 | 0.833 | 0.135 | 0.041 | 1.308 → 0.828 | 0.410 → 0.391 | 0.188 → 0.153 | 0.0 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| spider | 563 | 0.00 | - | - | 0.526 | - | 0.322 |
| waf-v2 | 3000 | 0.50 | 0.884 | 0.187 | 0.143 | 0.811 | 0.834 |

## http_attack, val — threat-only (b = -5.20)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 3563 | 1.14 | 0.774 | 0.772 | 0.834 | 0.123 | 0.061 | 1.029 → 0.925 | 0.407 → 0.401 | 0.176 → 0.164 | 0.0 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| spider | 563 | 0.00 | - | - | 0.558 | - | 0.307 |
| waf-v2 | 3000 | 0.50 | 0.892 | 0.197 | 0.137 | 0.810 | 0.836 |

## http_attack, val — safe-only (b = 5.51)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 3563 | 0.77 | 0.749 | 0.747 | 0.817 | 0.093 | 0.024 | 0.562 → 0.622 | 0.360 → 0.373 | 0.072 → 0.105 | 0.0 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| spider | 563 | 0.00 | - | - | 0.448 | - | 0.356 |
| waf-v2 | 3000 | 0.50 | 0.857 | 0.182 | 0.206 | 0.777 | 0.786 |
