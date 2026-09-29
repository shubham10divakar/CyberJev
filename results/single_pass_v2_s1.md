## One pass vs two — `runs/cyber-jev-v2-s1`, max_length 256

| decision | test set | variant | T | b | calib NLL | AUROC | DR@1%FPR | NLL | ECE |
|---|---|---|---|---|---|---|---|---|---|
| http_attack | in-domain | two-pass | 1.59 | 0.00 | 0.065 | 0.997 | 0.977 | 0.060 | 0.008 |
| http_attack | in-domain | threat-only | 0.73 | -0.12 | 0.064 | 0.997 | 0.977 | 0.057 | 0.005 |
| http_attack | in-domain | safe-only | 0.85 | -0.14 | 0.071 | 0.997 | 0.977 | 0.067 | 0.004 |
| http_attack | held-out | two-pass | 1.59 | 0.00 | 0.065 | 0.864 | 0.077 | 1.284 | 0.257 |
| http_attack | held-out | threat-only | 0.73 | -0.12 | 0.064 | 0.848 | 0.000 | 1.346 | 0.245 |
| http_attack | held-out | safe-only | 0.85 | -0.14 | 0.071 | 0.853 | 0.000 | 1.360 | 0.267 |

One-pass variant picked by calib NLL: http_attack → threat-only

## http_attack, in-domain — two-pass (b = 0.00)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 4200 | 1.59 | 0.983 | 0.982 | 0.997 | 0.977 | 0.962 | 0.072 → 0.060 | 0.032 → 0.030 | 0.014 → 0.008 | 0.0 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| ai-waf | 1200 | 0.28 | 0.997 | 0.979 | 0.006 | 0.970 | 0.984 |
| csic2010 | 1500 | 0.60 | 0.987 | 0.945 | 0.018 | 0.948 | 0.960 |
| web-attacks | 1500 | 0.80 | 1.000 | 1.000 | 0.000 | 1.000 | 1.000 |

## http_attack, in-domain — threat-only (b = -0.12)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 4200 | 0.73 | 0.983 | 0.982 | 0.997 | 0.977 | 0.964 | 0.069 → 0.057 | 0.031 → 0.029 | 0.023 → 0.005 | 0.0 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| ai-waf | 1200 | 0.28 | 0.996 | 0.976 | 0.005 | 0.964 | 0.983 |
| csic2010 | 1500 | 0.60 | 0.986 | 0.946 | 0.013 | 0.947 | 0.961 |
| web-attacks | 1500 | 0.80 | 1.000 | 1.000 | 0.000 | 1.000 | 1.000 |

## http_attack, in-domain — safe-only (b = -0.14)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 4200 | 0.85 | 0.982 | 0.982 | 0.997 | 0.977 | 0.906 | 0.071 → 0.067 | 0.032 → 0.032 | 0.015 → 0.004 | 0.0 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| ai-waf | 1200 | 0.28 | 0.996 | 0.979 | 0.007 | 0.970 | 0.983 |
| csic2010 | 1500 | 0.60 | 0.986 | 0.947 | 0.020 | 0.948 | 0.959 |
| web-attacks | 1500 | 0.80 | 1.000 | 1.000 | 0.000 | 1.000 | 1.000 |

## http_attack, held-out — two-pass (b = 0.00)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 10320 | 1.59 | 0.722 | 0.701 | 0.864 | 0.077 | 0.000 | 2.015 → 1.284 | 0.544 → 0.530 | 0.269 → 0.257 | 0.0 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| dvwa-juiceshop | 4320 | 0.73 | 0.826 | 0.523 | 0.575 | 0.925 | 0.695 |
| sqli-queries | 6000 | 0.36 | 0.939 | 0.163 | 0.513 | 0.998 | 0.672 |

## http_attack, held-out — threat-only (b = -0.12)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 10320 | 0.73 | 0.722 | 0.700 | 0.848 | 0.000 | 0.000 | 1.020 → 1.346 | 0.506 → 0.523 | 0.224 → 0.245 | 0.0 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| dvwa-juiceshop | 4320 | 0.73 | 0.816 | 0.024 | 0.603 | 0.923 | 0.677 |
| sqli-queries | 6000 | 0.36 | 0.926 | 0.000 | 0.505 | 0.998 | 0.677 |

## http_attack, held-out — safe-only (b = -0.14)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 10320 | 0.85 | 0.720 | 0.698 | 0.853 | 0.000 | 0.000 | 1.161 → 1.360 | 0.536 → 0.545 | 0.258 → 0.267 | 0.0 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| dvwa-juiceshop | 4320 | 0.73 | 0.856 | 0.428 | 0.571 | 0.925 | 0.696 |
| sqli-queries | 6000 | 0.36 | 0.886 | 0.000 | 0.522 | 0.999 | 0.666 |
