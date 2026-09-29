## One pass vs two — `runs/cyber-jev-v5ht-l6`, max_length 256

| decision | test set | variant | T | b | calib NLL | AUROC | DR@1%FPR | NLL | ECE |
|---|---|---|---|---|---|---|---|---|---|
| http_attack | in-domain | two-pass | 1.59 | 0.00 | 0.067 | 0.995 | 0.950 | 0.087 | 0.011 |
| http_attack | in-domain | threat-only | 1.08 | -2.47 | 0.067 | 0.995 | 0.950 | 0.091 | 0.007 |
| http_attack | in-domain | safe-only | 0.40 | 1.94 | 0.077 | 0.995 | 0.956 | 0.097 | 0.010 |
| http_attack | held-out | two-pass | 1.59 | 0.00 | 0.067 | 0.960 | 0.666 | 0.531 | 0.110 |
| http_attack | held-out | threat-only | 1.08 | -2.47 | 0.067 | 0.948 | 0.485 | 0.648 | 0.118 |
| http_attack | held-out | safe-only | 0.40 | 1.94 | 0.077 | 0.971 | 0.793 | 0.516 | 0.100 |
| http_attack | val | two-pass | 1.59 | 0.00 | 0.067 | 0.922 | 0.303 | 0.473 | 0.092 |
| http_attack | val | threat-only | 1.08 | -2.47 | 0.067 | 0.918 | 0.298 | 0.524 | 0.100 |
| http_attack | val | safe-only | 0.40 | 1.94 | 0.077 | 0.926 | 0.228 | 0.477 | 0.074 |
| phishing_url | in-domain | two-pass | 2.00 | 0.00 | 0.258 | 0.969 | 0.711 | 0.247 | 0.017 |
| phishing_url | in-domain | threat-only | 1.40 | -1.37 | 0.253 | 0.969 | 0.731 | 0.233 | 0.015 |
| phishing_url | in-domain | safe-only | 0.62 | 2.61 | 0.268 | 0.961 | 0.503 | 0.263 | 0.035 |
| phishing_url | held-out | two-pass | 2.00 | 0.00 | 0.258 | 0.821 | 0.156 | 0.505 | 0.071 |
| phishing_url | held-out | threat-only | 1.40 | -1.37 | 0.253 | 0.814 | 0.148 | 0.546 | 0.076 |
| phishing_url | held-out | safe-only | 0.62 | 2.61 | 0.268 | 0.832 | 0.183 | 0.630 | 0.137 |
| phishing_url | val | two-pass | 2.00 | 0.00 | 0.258 | 0.946 | 0.551 | 0.363 | 0.047 |
| phishing_url | val | threat-only | 1.40 | -1.37 | 0.253 | 0.942 | 0.527 | 0.328 | 0.029 |
| phishing_url | val | safe-only | 0.62 | 2.61 | 0.268 | 0.941 | 0.464 | 0.341 | 0.039 |
| prompt_injection | in-domain | two-pass | 1.74 | 0.00 | 0.074 | 0.994 | 0.903 | 0.105 | 0.013 |
| prompt_injection | in-domain | threat-only | 1.35 | -1.98 | 0.076 | 0.994 | 0.896 | 0.111 | 0.014 |
| prompt_injection | in-domain | safe-only | 0.40 | 2.06 | 0.083 | 0.993 | 0.901 | 0.108 | 0.009 |
| prompt_injection | held-out | two-pass | 1.74 | 0.00 | 0.074 | 0.828 | 0.123 | 0.910 | 0.215 |
| prompt_injection | held-out | threat-only | 1.35 | -1.98 | 0.076 | 0.824 | 0.143 | 0.903 | 0.217 |
| prompt_injection | held-out | safe-only | 0.40 | 2.06 | 0.083 | 0.823 | 0.100 | 0.939 | 0.220 |
| prompt_injection | val | two-pass | 1.74 | 0.00 | 0.074 | 0.787 | 0.072 | 0.870 | 0.198 |
| prompt_injection | val | threat-only | 1.35 | -1.98 | 0.076 | 0.777 | 0.057 | 0.904 | 0.217 |
| prompt_injection | val | safe-only | 0.40 | 2.06 | 0.083 | 0.802 | 0.061 | 0.805 | 0.182 |

One-pass variant picked: http_attack → safe-only (by val AUROC), phishing_url → threat-only (by val AUROC), prompt_injection → safe-only (by val AUROC)

## http_attack, in-domain — two-pass (b = 0.00)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 4700 | 1.59 | 0.972 | 0.972 | 0.995 | 0.950 | 0.908 | 0.113 → 0.087 | 0.051 → 0.048 | 0.023 → 0.011 | 0.0 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| ai-waf | 1200 | 0.28 | 0.996 | 0.970 | 0.006 | 0.955 | 0.979 |
| csic2010 | 1500 | 0.60 | 0.972 | 0.865 | 0.045 | 0.910 | 0.926 |
| gretel-sql | 500 | 0.00 | - | - | 0.000 | - | 1.000 |
| web-attacks | 1500 | 0.80 | 1.000 | 0.998 | 0.003 | 0.997 | 0.996 |

## http_attack, in-domain — threat-only (b = -2.47)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 4700 | 1.08 | 0.970 | 0.970 | 0.995 | 0.950 | 0.901 | 0.093 → 0.091 | 0.048 → 0.048 | 0.010 → 0.007 | 0.0 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| ai-waf | 1200 | 0.28 | 0.995 | 0.973 | 0.006 | 0.955 | 0.979 |
| csic2010 | 1500 | 0.60 | 0.971 | 0.865 | 0.059 | 0.911 | 0.921 |
| gretel-sql | 500 | 0.00 | - | - | 0.000 | - | 1.000 |
| web-attacks | 1500 | 0.80 | 1.000 | 0.998 | 0.007 | 0.997 | 0.995 |

## http_attack, in-domain — safe-only (b = 1.94)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 4700 | 0.40 | 0.971 | 0.971 | 0.995 | 0.956 | 0.897 | 0.167 → 0.097 | 0.071 → 0.050 | 0.094 → 0.010 | 0.0 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| ai-waf | 1200 | 0.28 | 0.995 | 0.967 | 0.012 | 0.970 | 0.979 |
| csic2010 | 1500 | 0.60 | 0.972 | 0.877 | 0.045 | 0.907 | 0.924 |
| gretel-sql | 500 | 0.00 | - | - | 0.002 | - | 0.499 |
| web-attacks | 1500 | 0.80 | 1.000 | 1.000 | 0.010 | 0.999 | 0.996 |

## http_attack, held-out — two-pass (b = 0.00)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 10320 | 1.59 | 0.859 | 0.857 | 0.960 | 0.666 | 0.435 | 0.805 → 0.531 | 0.261 → 0.248 | 0.125 → 0.110 | 0.0 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| dvwa-juiceshop | 4320 | 0.73 | 0.955 | 0.733 | 0.288 | 0.944 | 0.843 |
| sqli-queries | 6000 | 0.36 | 0.985 | 0.832 | 0.238 | 0.985 | 0.840 |

## http_attack, held-out — threat-only (b = -2.47)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 10320 | 1.08 | 0.857 | 0.854 | 0.948 | 0.485 | 0.206 | 0.692 → 0.648 | 0.262 → 0.260 | 0.121 → 0.118 | 0.0 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| dvwa-juiceshop | 4320 | 0.73 | 0.944 | 0.607 | 0.302 | 0.944 | 0.836 |
| sqli-queries | 6000 | 0.36 | 0.976 | 0.685 | 0.240 | 0.984 | 0.839 |

## http_attack, held-out — safe-only (b = 1.94)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 10320 | 0.40 | 0.858 | 0.855 | 0.971 | 0.793 | 0.676 | 0.358 → 0.516 | 0.220 → 0.245 | 0.074 → 0.100 | 0.0 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| dvwa-juiceshop | 4320 | 0.73 | 0.973 | 0.830 | 0.283 | 0.965 | 0.862 |
| sqli-queries | 6000 | 0.36 | 0.994 | 0.950 | 0.265 | 0.994 | 0.827 |

## http_attack, val — two-pass (b = 0.00)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 3563 | 1.59 | 0.869 | 0.865 | 0.922 | 0.303 | 0.075 | 0.698 → 0.473 | 0.245 → 0.231 | 0.114 → 0.092 | 0.0 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| spider | 563 | 0.00 | - | - | 0.007 | - | 0.498 |
| waf-v2 | 3000 | 0.50 | 0.894 | 0.251 | 0.140 | 0.831 | 0.846 |

## http_attack, val — threat-only (b = -2.47)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 3563 | 1.08 | 0.867 | 0.863 | 0.918 | 0.298 | 0.110 | 0.556 → 0.524 | 0.240 → 0.238 | 0.104 → 0.100 | 0.0 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| spider | 563 | 0.00 | - | - | 0.007 | - | 0.498 |
| waf-v2 | 3000 | 0.50 | 0.888 | 0.229 | 0.141 | 0.827 | 0.843 |

## http_attack, val — safe-only (b = 1.94)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 3563 | 0.40 | 0.866 | 0.863 | 0.926 | 0.228 | 0.056 | 0.389 → 0.477 | 0.231 → 0.229 | 0.067 → 0.074 | 0.0 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| spider | 563 | 0.00 | - | - | 0.011 | - | 0.497 |
| waf-v2 | 3000 | 0.50 | 0.900 | 0.171 | 0.186 | 0.871 | 0.842 |

## phishing_url, in-domain — two-pass (b = 0.00)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| phishing_url | 1998 | 2.00 | 0.894 | 0.894 | 0.969 | 0.711 | 0.357 | 0.311 → 0.247 | 0.168 → 0.152 | 0.061 → 0.017 | 0.0 |

## phishing_url, in-domain — threat-only (b = -1.37)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| phishing_url | 1998 | 1.40 | 0.900 | 0.900 | 0.969 | 0.731 | 0.354 | 0.240 → 0.233 | 0.146 → 0.142 | 0.033 → 0.015 | 0.0 |

## phishing_url, in-domain — safe-only (b = 2.61)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| phishing_url | 1998 | 0.62 | 0.900 | 0.900 | 0.961 | 0.503 | 0.220 | 0.299 → 0.263 | 0.164 → 0.154 | 0.076 → 0.035 | 0.0 |

## phishing_url, held-out — two-pass (b = 0.00)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| phishing_url | 5000 | 2.00 | 0.764 | 0.732 | 0.821 | 0.156 | 0.017 | 0.718 → 0.505 | 0.378 → 0.331 | 0.153 → 0.071 | 0.0 |

**phishing_url by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| destroylist | 2000 | 1.00 | - | - | - | 0.735 | 0.424 |
| phishtrap | 3000 | 0.50 | 0.872 | 0.247 | 0.302 | 0.867 | 0.781 |

## phishing_url, held-out — threat-only (b = -1.37)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| phishing_url | 5000 | 1.40 | 0.746 | 0.719 | 0.814 | 0.148 | 0.008 | 0.624 → 0.546 | 0.377 → 0.356 | 0.121 → 0.076 | 0.0 |

**phishing_url by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| destroylist | 2000 | 1.00 | - | - | - | 0.692 | 0.409 |
| phishtrap | 3000 | 0.50 | 0.864 | 0.228 | 0.273 | 0.836 | 0.781 |

## phishing_url, held-out — safe-only (b = 2.61)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| phishing_url | 5000 | 0.62 | 0.726 | 0.711 | 0.832 | 0.183 | 0.062 | 0.557 → 0.630 | 0.375 → 0.411 | 0.072 → 0.137 | 0.0 |

**phishing_url by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| destroylist | 2000 | 1.00 | - | - | - | 0.600 | 0.375 |
| phishtrap | 3000 | 0.50 | 0.885 | 0.306 | 0.179 | 0.801 | 0.811 |

## phishing_url, val — two-pass (b = 0.00)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| phishing_url | 3000 | 2.00 | 0.851 | 0.850 | 0.946 | 0.551 | 0.321 | 0.532 → 0.363 | 0.250 → 0.224 | 0.100 → 0.047 | 0.0 |

## phishing_url, val — threat-only (b = -1.37)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| phishing_url | 3000 | 1.40 | 0.864 | 0.864 | 0.942 | 0.527 | 0.301 | 0.366 → 0.328 | 0.211 → 0.201 | 0.062 → 0.029 | 0.0 |

## phishing_url, val — safe-only (b = 2.61)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| phishing_url | 3000 | 0.62 | 0.868 | 0.867 | 0.941 | 0.464 | 0.064 | 0.348 → 0.341 | 0.204 → 0.204 | 0.057 → 0.039 | 0.0 |

## prompt_injection, in-domain — two-pass (b = 0.00)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| prompt_injection | 2500 | 1.74 | 0.964 | 0.964 | 0.994 | 0.903 | 0.472 | 0.148 → 0.105 | 0.063 → 0.057 | 0.029 → 0.013 | 0.0 |

**prompt_injection by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| awesome-prompts | 71 | 0.00 | - | - | 0.014 | - | 0.496 |
| dolly | 222 | 0.00 | - | - | 0.005 | - | 0.499 |
| mosscap | 53 | 1.00 | - | - | - | 0.962 | 0.490 |
| neuralchemy | 900 | 0.59 | 0.993 | 0.915 | 0.051 | 0.973 | 0.962 |
| s-labs | 1000 | 0.47 | 0.995 | 0.953 | 0.006 | 0.917 | 0.958 |
| simsonsun | 128 | 1.00 | - | - | - | 0.977 | 0.494 |
| wildjailbreak | 126 | 0.93 | 0.890 | 0.359 | 0.667 | 0.983 | 0.697 |

## prompt_injection, in-domain — threat-only (b = -1.98)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| prompt_injection | 2500 | 1.35 | 0.964 | 0.964 | 0.994 | 0.896 | 0.602 | 0.129 → 0.111 | 0.063 → 0.060 | 0.026 → 0.014 | 0.0 |

**prompt_injection by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| awesome-prompts | 71 | 0.00 | - | - | 0.014 | - | 0.496 |
| dolly | 222 | 0.00 | - | - | 0.005 | - | 0.499 |
| mosscap | 53 | 1.00 | - | - | - | 0.981 | 0.495 |
| neuralchemy | 900 | 0.59 | 0.993 | 0.913 | 0.048 | 0.972 | 0.962 |
| s-labs | 1000 | 0.47 | 0.994 | 0.943 | 0.004 | 0.913 | 0.957 |
| simsonsun | 128 | 1.00 | - | - | - | 0.977 | 0.494 |
| wildjailbreak | 126 | 0.93 | 0.890 | 0.350 | 0.667 | 0.983 | 0.697 |

## prompt_injection, in-domain — safe-only (b = 2.06)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| prompt_injection | 2500 | 0.40 | 0.965 | 0.965 | 0.993 | 0.901 | 0.549 | 0.191 → 0.108 | 0.081 → 0.057 | 0.108 → 0.009 | 0.0 |

**prompt_injection by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| awesome-prompts | 71 | 0.00 | - | - | 0.056 | - | 0.486 |
| dolly | 222 | 0.00 | - | - | 0.000 | - | 1.000 |
| mosscap | 53 | 1.00 | - | - | - | 0.943 | 0.485 |
| neuralchemy | 900 | 0.59 | 0.992 | 0.884 | 0.043 | 0.972 | 0.965 |
| s-labs | 1000 | 0.47 | 0.995 | 0.943 | 0.008 | 0.934 | 0.965 |
| simsonsun | 128 | 1.00 | - | - | - | 0.969 | 0.492 |
| wildjailbreak | 126 | 0.93 | 0.861 | 0.359 | 0.667 | 0.966 | 0.666 |

## prompt_injection, held-out — two-pass (b = 0.00)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| prompt_injection | 1951 | 1.74 | 0.716 | 0.711 | 0.828 | 0.123 | 0.020 | 1.478 → 0.910 | 0.526 → 0.485 | 0.251 → 0.215 | 0.0 |

**prompt_injection by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| deepset | 662 | 0.40 | 0.756 | 0.057 | 0.388 | 0.795 | 0.683 |
| jackhhao | 1289 | 0.51 | 0.867 | 0.161 | 0.476 | 0.935 | 0.719 |

## prompt_injection, held-out — threat-only (b = -1.98)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| prompt_injection | 1951 | 1.35 | 0.713 | 0.709 | 0.824 | 0.143 | 0.022 | 1.166 → 0.903 | 0.511 → 0.485 | 0.240 → 0.217 | 0.0 |

**prompt_injection by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| deepset | 662 | 0.40 | 0.758 | 0.087 | 0.378 | 0.783 | 0.685 |
| jackhhao | 1289 | 0.51 | 0.859 | 0.157 | 0.480 | 0.929 | 0.714 |

## prompt_injection, held-out — safe-only (b = 2.06)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| prompt_injection | 1951 | 0.40 | 0.701 | 0.695 | 0.823 | 0.100 | 0.027 | 0.593 → 0.939 | 0.402 → 0.493 | 0.087 → 0.220 | 0.0 |

**prompt_injection by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| deepset | 662 | 0.40 | 0.750 | 0.011 | 0.416 | 0.806 | 0.672 |
| jackhhao | 1289 | 0.51 | 0.864 | 0.195 | 0.506 | 0.934 | 0.701 |

## prompt_injection, val — two-pass (b = 0.00)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| prompt_injection | 1500 | 1.74 | 0.713 | 0.711 | 0.787 | 0.072 | 0.009 | 1.386 → 0.870 | 0.518 → 0.476 | 0.241 → 0.198 | 0.0 |

## prompt_injection, val — threat-only (b = -1.98)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| prompt_injection | 1500 | 1.35 | 0.716 | 0.715 | 0.777 | 0.057 | 0.008 | 1.159 → 0.904 | 0.514 → 0.489 | 0.238 → 0.217 | 0.0 |

## prompt_injection, val — safe-only (b = 2.06)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| prompt_injection | 1500 | 0.40 | 0.709 | 0.704 | 0.802 | 0.061 | 0.011 | 0.567 → 0.805 | 0.384 → 0.454 | 0.049 → 0.182 | 0.0 |
