## One pass vs two — `runs/cyber-jev-v2-l6-e3`, max_length 256

| decision | test set | variant | T | b | calib NLL | AUROC | DR@1%FPR | NLL | ECE |
|---|---|---|---|---|---|---|---|---|---|
| http_attack | in-domain | two-pass | 1.89 | 0.00 | 0.096 | 0.995 | 0.956 | 0.085 | 0.010 |
| http_attack | in-domain | threat-only | 1.25 | -4.42 | 0.123 | 0.984 | 0.954 | 0.108 | 0.004 |
| http_attack | in-domain | safe-only | 0.65 | 4.89 | 0.127 | 0.993 | 0.942 | 0.117 | 0.013 |
| http_attack | held-out | two-pass | 1.89 | 0.00 | 0.096 | 0.905 | 0.305 | 0.793 | 0.175 |
| http_attack | held-out | threat-only | 1.25 | -4.42 | 0.123 | 0.847 | 0.135 | 1.090 | 0.222 |
| http_attack | held-out | safe-only | 0.65 | 4.89 | 0.127 | 0.949 | 0.483 | 0.401 | 0.104 |
| http_attack | val | two-pass | 1.89 | 0.00 | 0.096 | 0.823 | 0.088 | 0.834 | 0.170 |
| http_attack | val | threat-only | 1.25 | -4.42 | 0.123 | 0.829 | 0.100 | 0.894 | 0.171 |
| http_attack | val | safe-only | 0.65 | 4.89 | 0.127 | 0.796 | 0.064 | 0.690 | 0.130 |

One-pass variant picked: http_attack → threat-only (by val AUROC)

## http_attack, in-domain — two-pass (b = 0.00)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 4200 | 1.89 | 0.971 | 0.970 | 0.995 | 0.956 | 0.921 | 0.110 → 0.085 | 0.052 → 0.047 | 0.024 → 0.010 | 0.0 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| ai-waf | 1200 | 0.28 | 0.995 | 0.949 | 0.008 | 0.946 | 0.974 |
| csic2010 | 1500 | 0.60 | 0.978 | 0.895 | 0.032 | 0.914 | 0.934 |
| web-attacks | 1500 | 0.80 | 1.000 | 1.000 | 0.003 | 1.000 | 0.999 |

## http_attack, in-domain — threat-only (b = -4.42)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 4200 | 1.25 | 0.969 | 0.968 | 0.984 | 0.954 | 0.904 | 0.112 → 0.108 | 0.055 → 0.054 | 0.014 → 0.004 | 0.0 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| ai-waf | 1200 | 0.28 | 0.987 | 0.946 | 0.010 | 0.946 | 0.972 |
| csic2010 | 1500 | 0.60 | 0.973 | 0.894 | 0.025 | 0.906 | 0.932 |
| web-attacks | 1500 | 0.80 | 1.000 | 1.000 | 0.016 | 1.000 | 0.995 |

## http_attack, in-domain — safe-only (b = 4.89)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 4200 | 0.65 | 0.957 | 0.955 | 0.993 | 0.942 | 0.582 | 0.142 → 0.117 | 0.069 → 0.064 | 0.050 → 0.013 | 0.0 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| ai-waf | 1200 | 0.28 | 0.995 | 0.940 | 0.007 | 0.928 | 0.968 |
| csic2010 | 1500 | 0.60 | 0.974 | 0.736 | 0.193 | 0.960 | 0.892 |
| web-attacks | 1500 | 0.80 | 1.000 | 1.000 | 0.000 | 0.999 | 0.999 |

## http_attack, held-out — two-pass (b = 0.00)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 10320 | 1.89 | 0.771 | 0.759 | 0.905 | 0.305 | 0.076 | 1.409 → 0.793 | 0.429 → 0.399 | 0.205 → 0.175 | 0.0 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| dvwa-juiceshop | 4320 | 0.73 | 0.957 | 0.606 | 0.154 | 0.938 | 0.890 |
| sqli-queries | 6000 | 0.36 | 0.986 | 0.590 | 0.519 | 0.999 | 0.668 |

## http_attack, held-out — threat-only (b = -4.42)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 10320 | 1.25 | 0.720 | 0.698 | 0.847 | 0.135 | 0.013 | 1.327 → 1.090 | 0.515 → 0.502 | 0.237 → 0.222 | 0.0 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| dvwa-juiceshop | 4320 | 0.73 | 0.932 | 0.274 | 0.163 | 0.923 | 0.874 |
| sqli-queries | 6000 | 0.36 | 0.950 | 0.197 | 0.643 | 1.000 | 0.582 |

## http_attack, held-out — safe-only (b = 4.89)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 10320 | 0.65 | 0.834 | 0.830 | 0.949 | 0.483 | 0.330 | 0.343 → 0.401 | 0.224 → 0.250 | 0.075 → 0.104 | 0.0 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| dvwa-juiceshop | 4320 | 0.73 | 0.974 | 0.815 | 0.140 | 0.927 | 0.886 |
| sqli-queries | 6000 | 0.36 | 0.994 | 0.882 | 0.343 | 0.998 | 0.780 |

## http_attack, val — two-pass (b = 0.00)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 3563 | 1.89 | 0.750 | 0.750 | 0.823 | 0.088 | 0.007 | 1.425 → 0.834 | 0.463 → 0.436 | 0.208 → 0.170 | 0.0 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| spider | 563 | 0.00 | - | - | 0.615 | - | 0.278 |
| waf-v2 | 3000 | 0.50 | 0.882 | 0.226 | 0.243 | 0.881 | 0.818 |

## http_attack, val — threat-only (b = -4.42)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 3563 | 1.25 | 0.743 | 0.743 | 0.829 | 0.100 | 0.044 | 1.066 → 0.894 | 0.452 → 0.441 | 0.190 → 0.171 | 0.0 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| spider | 563 | 0.00 | - | - | 0.627 | - | 0.272 |
| waf-v2 | 3000 | 0.50 | 0.884 | 0.233 | 0.254 | 0.879 | 0.812 |

## http_attack, val — safe-only (b = 4.89)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 3563 | 0.65 | 0.757 | 0.756 | 0.796 | 0.064 | 0.048 | 0.575 → 0.690 | 0.372 → 0.396 | 0.099 → 0.130 | 0.0 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| spider | 563 | 0.00 | - | - | 0.577 | - | 0.297 |
| waf-v2 | 3000 | 0.50 | 0.867 | 0.175 | 0.183 | 0.822 | 0.819 |
