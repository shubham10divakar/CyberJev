## One pass vs two — `runs/cyber-jev-v3-l6-s1`, max_length 256

| decision | test set | variant | T | b | calib NLL | AUROC | DR@1%FPR | NLL | ECE |
|---|---|---|---|---|---|---|---|---|---|
| http_attack | in-domain | two-pass | 1.78 | 0.00 | 0.066 | 0.996 | 0.963 | 0.071 | 0.010 |
| http_attack | in-domain | threat-only | 1.16 | -3.92 | 0.082 | 0.990 | 0.963 | 0.088 | 0.006 |
| http_attack | in-domain | safe-only | 0.58 | 4.52 | 0.074 | 0.996 | 0.963 | 0.077 | 0.004 |
| http_attack | held-out | two-pass | 1.78 | 0.00 | 0.066 | 0.985 | 0.824 | 0.357 | 0.071 |
| http_attack | held-out | threat-only | 1.16 | -3.92 | 0.082 | 0.968 | 0.481 | 0.433 | 0.072 |
| http_attack | held-out | safe-only | 0.58 | 4.52 | 0.074 | 0.993 | 0.921 | 0.190 | 0.046 |
| http_attack | val | two-pass | 1.78 | 0.00 | 0.066 | 0.903 | 0.326 | 0.759 | 0.201 |
| http_attack | val | threat-only | 1.16 | -3.92 | 0.082 | 0.902 | 0.315 | 0.724 | 0.191 |
| http_attack | val | safe-only | 0.58 | 4.52 | 0.074 | 0.870 | 0.238 | 0.768 | 0.202 |

One-pass variant picked: http_attack → threat-only (by val AUROC)

## http_attack, in-domain — two-pass (b = 0.00)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 4700 | 1.78 | 0.977 | 0.977 | 0.996 | 0.963 | 0.937 | 0.097 → 0.071 | 0.043 → 0.039 | 0.020 → 0.010 | 0.0 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| ai-waf | 1200 | 0.28 | 0.995 | 0.958 | 0.010 | 0.958 | 0.976 |
| csic2010 | 1500 | 0.60 | 0.981 | 0.914 | 0.022 | 0.925 | 0.944 |
| gretel-sql | 500 | 0.00 | - | - | 0.002 | - | 0.499 |
| web-attacks | 1500 | 0.80 | 1.000 | 0.997 | 0.007 | 0.997 | 0.995 |

## http_attack, in-domain — threat-only (b = -3.92)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 4700 | 1.16 | 0.976 | 0.976 | 0.990 | 0.963 | 0.942 | 0.092 → 0.088 | 0.043 → 0.042 | 0.012 → 0.006 | 0.0 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| ai-waf | 1200 | 0.28 | 0.991 | 0.955 | 0.010 | 0.955 | 0.975 |
| csic2010 | 1500 | 0.60 | 0.964 | 0.911 | 0.020 | 0.920 | 0.942 |
| gretel-sql | 500 | 0.00 | - | - | 0.002 | - | 0.499 |
| web-attacks | 1500 | 0.80 | 1.000 | 0.998 | 0.010 | 0.998 | 0.995 |

## http_attack, in-domain — safe-only (b = 4.52)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 4700 | 0.58 | 0.975 | 0.975 | 0.996 | 0.963 | 0.891 | 0.102 → 0.077 | 0.046 → 0.040 | 0.043 → 0.004 | 0.0 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| ai-waf | 1200 | 0.28 | 0.995 | 0.958 | 0.006 | 0.955 | 0.979 |
| csic2010 | 1500 | 0.60 | 0.981 | 0.895 | 0.062 | 0.939 | 0.936 |
| gretel-sql | 500 | 0.00 | - | - | 0.000 | - | 1.000 |
| web-attacks | 1500 | 0.80 | 1.000 | 0.997 | 0.003 | 0.997 | 0.995 |

## http_attack, held-out — two-pass (b = 0.00)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 10320 | 1.78 | 0.894 | 0.893 | 0.985 | 0.824 | 0.549 | 0.583 → 0.357 | 0.191 → 0.178 | 0.089 → 0.071 | 0.0 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| dvwa-juiceshop | 4320 | 0.73 | 0.956 | 0.678 | 0.364 | 0.984 | 0.843 |
| sqli-queries | 6000 | 0.36 | 0.996 | 0.972 | 0.159 | 0.995 | 0.894 |

## http_attack, held-out — threat-only (b = -3.92)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 10320 | 1.16 | 0.889 | 0.887 | 0.968 | 0.481 | 0.255 | 0.486 → 0.433 | 0.197 → 0.194 | 0.081 → 0.072 | 0.0 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| dvwa-juiceshop | 4320 | 0.73 | 0.895 | 0.158 | 0.348 | 0.978 | 0.845 |
| sqli-queries | 6000 | 0.36 | 0.995 | 0.895 | 0.174 | 0.995 | 0.884 |

## http_attack, held-out — safe-only (b = 4.52)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 10320 | 0.58 | 0.919 | 0.918 | 0.993 | 0.921 | 0.844 | 0.174 → 0.190 | 0.106 → 0.119 | 0.051 → 0.046 | 0.0 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| dvwa-juiceshop | 4320 | 0.73 | 0.980 | 0.835 | 0.317 | 0.987 | 0.867 |
| sqli-queries | 6000 | 0.36 | 0.996 | 0.980 | 0.107 | 0.989 | 0.924 |

## http_attack, val — two-pass (b = 0.00)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 3563 | 1.78 | 0.756 | 0.756 | 0.903 | 0.326 | 0.142 | 1.281 → 0.759 | 0.462 → 0.418 | 0.229 → 0.201 | 0.0 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| spider | 563 | 0.00 | - | - | 0.000 | - | 1.000 |
| waf-v2 | 3000 | 0.50 | 0.867 | 0.277 | 0.477 | 0.898 | 0.700 |

## http_attack, val — threat-only (b = -3.92)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 3563 | 1.16 | 0.753 | 0.753 | 0.902 | 0.315 | 0.173 | 0.815 → 0.724 | 0.417 → 0.401 | 0.204 → 0.191 | 0.0 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| spider | 563 | 0.00 | - | - | 0.014 | - | 0.496 |
| waf-v2 | 3000 | 0.50 | 0.868 | 0.227 | 0.469 | 0.888 | 0.700 |

## http_attack, val — safe-only (b = 4.52)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 3563 | 0.58 | 0.754 | 0.754 | 0.870 | 0.238 | 0.062 | 0.532 → 0.768 | 0.358 → 0.423 | 0.143 → 0.202 | 0.0 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| spider | 563 | 0.00 | - | - | 0.000 | - | 1.000 |
| waf-v2 | 3000 | 0.50 | 0.821 | 0.229 | 0.482 | 0.897 | 0.696 |
