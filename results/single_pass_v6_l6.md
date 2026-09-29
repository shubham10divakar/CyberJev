## One pass vs two — `runs/cyber-jev-v6-l6`, max_length 256

| decision | test set | variant | T | b | calib NLL | AUROC | DR@1%FPR | NLL | ECE |
|---|---|---|---|---|---|---|---|---|---|
| http_attack | in-domain | two-pass | 1.69 | 0.00 | 0.091 | 0.994 | 0.941 | 0.092 | 0.004 |
| http_attack | in-domain | threat-only | 0.83 | -4.84 | 0.102 | 0.994 | 0.942 | 0.108 | 0.010 |
| http_attack | in-domain | safe-only | 0.59 | 4.21 | 0.102 | 0.994 | 0.941 | 0.104 | 0.010 |
| http_attack | held-out | two-pass | 1.69 | 0.00 | 0.091 | 0.982 | 0.861 | 0.326 | 0.071 |
| http_attack | held-out | threat-only | 0.83 | -4.84 | 0.102 | 0.976 | 0.723 | 0.560 | 0.092 |
| http_attack | held-out | safe-only | 0.59 | 4.21 | 0.102 | 0.985 | 0.879 | 0.269 | 0.064 |
| http_attack | val | two-pass | 1.69 | 0.00 | 0.091 | 0.907 | 0.302 | 0.656 | 0.175 |
| http_attack | val | threat-only | 0.83 | -4.84 | 0.102 | 0.900 | 0.295 | 1.106 | 0.220 |
| http_attack | val | safe-only | 0.59 | 4.21 | 0.102 | 0.909 | 0.295 | 0.561 | 0.125 |
| phishing_url | in-domain | two-pass | 1.73 | 0.00 | 0.259 | 0.963 | 0.624 | 0.254 | 0.029 |
| phishing_url | in-domain | threat-only | 0.80 | -3.71 | 0.265 | 0.961 | 0.640 | 0.256 | 0.014 |
| phishing_url | in-domain | safe-only | 0.89 | 3.08 | 0.254 | 0.962 | 0.608 | 0.258 | 0.012 |
| phishing_url | held-out | two-pass | 1.73 | 0.00 | 0.259 | 0.776 | 0.156 | 0.690 | 0.162 |
| phishing_url | held-out | threat-only | 0.80 | -3.71 | 0.265 | 0.756 | 0.118 | 0.655 | 0.137 |
| phishing_url | held-out | safe-only | 0.89 | 3.08 | 0.254 | 0.789 | 0.185 | 0.627 | 0.145 |
| phishing_url | val | two-pass | 1.73 | 0.00 | 0.259 | 0.934 | 0.519 | 0.329 | 0.027 |
| phishing_url | val | threat-only | 0.80 | -3.71 | 0.265 | 0.928 | 0.555 | 0.348 | 0.031 |
| phishing_url | val | safe-only | 0.89 | 3.08 | 0.254 | 0.934 | 0.492 | 0.344 | 0.032 |
| prompt_injection | in-domain | two-pass | 1.71 | 0.00 | 0.101 | 0.991 | 0.833 | 0.145 | 0.017 |
| prompt_injection | in-domain | threat-only | 1.12 | -3.32 | 0.113 | 0.989 | 0.836 | 0.148 | 0.015 |
| prompt_injection | in-domain | safe-only | 0.71 | 2.43 | 0.136 | 0.984 | 0.796 | 0.164 | 0.019 |
| prompt_injection | held-out | two-pass | 1.71 | 0.00 | 0.101 | 0.824 | 0.149 | 0.702 | 0.167 |
| prompt_injection | held-out | threat-only | 1.12 | -3.32 | 0.113 | 0.830 | 0.232 | 0.764 | 0.202 |
| prompt_injection | held-out | safe-only | 0.71 | 2.43 | 0.136 | 0.799 | 0.031 | 0.769 | 0.154 |
| prompt_injection | val | two-pass | 1.71 | 0.00 | 0.101 | 0.796 | 0.067 | 0.853 | 0.186 |
| prompt_injection | val | threat-only | 1.12 | -3.32 | 0.113 | 0.791 | 0.045 | 0.768 | 0.183 |
| prompt_injection | val | safe-only | 0.71 | 2.43 | 0.136 | 0.789 | 0.013 | 0.896 | 0.189 |

One-pass variant picked: http_attack → safe-only (by val AUROC), phishing_url → safe-only (by val AUROC), prompt_injection → threat-only (by val AUROC)

## http_attack, in-domain — two-pass (b = 0.00)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 4700 | 1.69 | 0.967 | 0.967 | 0.994 | 0.941 | 0.913 | 0.113 → 0.092 | 0.056 → 0.052 | 0.021 → 0.004 | 0.0 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| ai-waf | 1200 | 0.28 | 0.994 | 0.949 | 0.008 | 0.946 | 0.974 |
| csic2010 | 1500 | 0.60 | 0.968 | 0.836 | 0.039 | 0.884 | 0.913 |
| gretel-sql | 500 | 0.00 | - | - | 0.000 | - | 1.000 |
| web-attacks | 1500 | 0.80 | 1.000 | 0.998 | 0.003 | 0.998 | 0.997 |

## http_attack, in-domain — threat-only (b = -4.84)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 4700 | 0.83 | 0.966 | 0.966 | 0.994 | 0.942 | 0.911 | 0.110 → 0.108 | 0.055 → 0.055 | 0.016 → 0.010 | 0.0 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| ai-waf | 1200 | 0.28 | 0.991 | 0.946 | 0.012 | 0.949 | 0.972 |
| csic2010 | 1500 | 0.60 | 0.968 | 0.834 | 0.037 | 0.885 | 0.914 |
| gretel-sql | 500 | 0.00 | - | - | 0.004 | - | 0.499 |
| web-attacks | 1500 | 0.80 | 1.000 | 0.998 | 0.007 | 0.998 | 0.996 |

## http_attack, in-domain — safe-only (b = 4.21)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 4700 | 0.59 | 0.963 | 0.963 | 0.994 | 0.941 | 0.904 | 0.129 → 0.104 | 0.064 → 0.058 | 0.048 → 0.010 | 0.0 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| ai-waf | 1200 | 0.28 | 0.994 | 0.952 | 0.005 | 0.937 | 0.974 |
| csic2010 | 1500 | 0.60 | 0.966 | 0.839 | 0.094 | 0.901 | 0.900 |
| gretel-sql | 500 | 0.00 | - | - | 0.000 | - | 1.000 |
| web-attacks | 1500 | 0.80 | 1.000 | 0.998 | 0.007 | 0.997 | 0.995 |

## http_attack, held-out — two-pass (b = 0.00)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 10320 | 1.69 | 0.894 | 0.893 | 0.982 | 0.861 | 0.717 | 0.501 → 0.326 | 0.194 → 0.180 | 0.089 → 0.071 | 0.0 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| dvwa-juiceshop | 4320 | 0.73 | 0.966 | 0.788 | 0.221 | 0.963 | 0.886 |
| sqli-queries | 6000 | 0.36 | 0.997 | 0.969 | 0.187 | 0.996 | 0.877 |

## http_attack, held-out — threat-only (b = -4.84)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 10320 | 0.83 | 0.871 | 0.868 | 0.976 | 0.723 | 0.623 | 0.486 → 0.560 | 0.224 → 0.228 | 0.079 → 0.092 | 0.0 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| dvwa-juiceshop | 4320 | 0.73 | 0.933 | 0.506 | 0.310 | 0.964 | 0.850 |
| sqli-queries | 6000 | 0.36 | 0.997 | 0.965 | 0.223 | 0.996 | 0.854 |

## http_attack, held-out — safe-only (b = 4.21)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 10320 | 0.59 | 0.905 | 0.904 | 0.985 | 0.879 | 0.753 | 0.225 → 0.269 | 0.137 → 0.156 | 0.056 → 0.064 | 0.0 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| dvwa-juiceshop | 4320 | 0.73 | 0.984 | 0.908 | 0.157 | 0.966 | 0.913 |
| sqli-queries | 6000 | 0.36 | 0.996 | 0.969 | 0.177 | 0.992 | 0.881 |

## http_attack, val — two-pass (b = 0.00)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 3563 | 1.69 | 0.774 | 0.774 | 0.907 | 0.302 | 0.098 | 1.036 → 0.656 | 0.410 → 0.371 | 0.202 → 0.175 | 0.0 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| spider | 563 | 0.00 | - | - | 0.004 | - | 0.499 |
| waf-v2 | 3000 | 0.50 | 0.873 | 0.291 | 0.435 | 0.900 | 0.725 |

## http_attack, val — threat-only (b = -4.84)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 3563 | 0.83 | 0.749 | 0.749 | 0.900 | 0.295 | 0.091 | 0.940 → 1.106 | 0.451 → 0.464 | 0.206 → 0.220 | 0.0 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| spider | 563 | 0.00 | - | - | 0.014 | - | 0.496 |
| waf-v2 | 3000 | 0.50 | 0.866 | 0.262 | 0.504 | 0.914 | 0.692 |

## http_attack, val — safe-only (b = 4.21)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 3563 | 0.59 | 0.812 | 0.811 | 0.909 | 0.295 | 0.103 | 0.425 → 0.561 | 0.272 → 0.303 | 0.076 → 0.125 | 0.0 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| spider | 563 | 0.00 | - | - | 0.000 | - | 1.000 |
| waf-v2 | 3000 | 0.50 | 0.875 | 0.267 | 0.322 | 0.875 | 0.774 |

## phishing_url, in-domain — two-pass (b = 0.00)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| phishing_url | 1998 | 1.73 | 0.894 | 0.894 | 0.963 | 0.624 | 0.434 | 0.299 → 0.254 | 0.166 → 0.153 | 0.060 → 0.029 | 0.0 |

## phishing_url, in-domain — threat-only (b = -3.71)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| phishing_url | 1998 | 0.80 | 0.893 | 0.893 | 0.961 | 0.640 | 0.330 | 0.266 → 0.256 | 0.156 → 0.154 | 0.037 → 0.014 | 0.0 |

## phishing_url, in-domain — safe-only (b = 3.08)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| phishing_url | 1998 | 0.89 | 0.893 | 0.893 | 0.962 | 0.608 | 0.440 | 0.260 → 0.258 | 0.155 → 0.155 | 0.015 → 0.012 | 0.0 |

## phishing_url, held-out — two-pass (b = 0.00)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| phishing_url | 5000 | 1.73 | 0.675 | 0.665 | 0.776 | 0.156 | 0.063 | 0.966 → 0.690 | 0.530 → 0.462 | 0.237 → 0.162 | 0.0 |

**phishing_url by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| destroylist | 2000 | 1.00 | - | - | - | 0.518 | 0.341 |
| phishtrap | 3000 | 0.50 | 0.835 | 0.257 | 0.159 | 0.717 | 0.778 |

## phishing_url, held-out — threat-only (b = -3.71)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| phishing_url | 5000 | 0.80 | 0.692 | 0.674 | 0.756 | 0.118 | 0.033 | 0.609 → 0.655 | 0.417 → 0.437 | 0.100 → 0.137 | 0.0 |

**phishing_url by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| destroylist | 2000 | 1.00 | - | - | - | 0.587 | 0.370 |
| phishtrap | 3000 | 0.50 | 0.815 | 0.201 | 0.232 | 0.754 | 0.761 |

## phishing_url, held-out — safe-only (b = 3.08)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| phishing_url | 5000 | 0.89 | 0.691 | 0.679 | 0.789 | 0.185 | 0.061 | 0.603 → 0.627 | 0.412 → 0.423 | 0.126 → 0.145 | 0.0 |

**phishing_url by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| destroylist | 2000 | 1.00 | - | - | - | 0.549 | 0.354 |
| phishtrap | 3000 | 0.50 | 0.848 | 0.291 | 0.173 | 0.745 | 0.786 |

## phishing_url, val — two-pass (b = 0.00)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| phishing_url | 3000 | 1.73 | 0.876 | 0.876 | 0.934 | 0.519 | 0.082 | 0.424 → 0.329 | 0.210 → 0.196 | 0.076 → 0.027 | 0.0 |

## phishing_url, val — threat-only (b = -3.71)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| phishing_url | 3000 | 0.80 | 0.862 | 0.862 | 0.928 | 0.555 | 0.043 | 0.340 → 0.348 | 0.207 → 0.209 | 0.019 → 0.031 | 0.0 |

## phishing_url, val — safe-only (b = 3.08)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| phishing_url | 3000 | 0.89 | 0.874 | 0.874 | 0.934 | 0.492 | 0.103 | 0.338 → 0.344 | 0.201 → 0.202 | 0.025 → 0.032 | 0.0 |

## prompt_injection, in-domain — two-pass (b = 0.00)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| prompt_injection | 2773 | 1.71 | 0.950 | 0.950 | 0.991 | 0.833 | 0.692 | 0.198 → 0.145 | 0.086 → 0.079 | 0.037 → 0.017 | 0.0 |

**prompt_injection by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| awesome-prompts | 71 | 0.00 | - | - | 0.000 | - | 1.000 |
| dolly | 222 | 0.00 | - | - | 0.000 | - | 1.000 |
| mkqa-de | 13 | 0.00 | - | - | 0.077 | - | 0.480 |
| mkqa-es | 9 | 0.00 | - | - | 0.000 | - | 1.000 |
| mkqa-fr | 14 | 0.00 | - | - | 0.000 | - | 1.000 |
| mkqa-it | 18 | 0.00 | - | - | 0.000 | - | 1.000 |
| mkqa-pt | 19 | 0.00 | - | - | 0.105 | - | 0.472 |
| mkqa-ru | 68 | 0.00 | - | - | 0.103 | - | 0.473 |
| mosscap | 53 | 1.00 | - | - | - | 0.925 | 0.480 |
| neuralchemy | 900 | 0.59 | 0.993 | 0.907 | 0.048 | 0.973 | 0.963 |
| ru-injections | 54 | 1.00 | - | - | - | 0.926 | 0.481 |
| s-labs | 1000 | 0.47 | 0.993 | 0.917 | 0.000 | 0.858 | 0.932 |
| simsonsun | 128 | 1.00 | - | - | - | 0.906 | 0.475 |
| wildjailbreak | 126 | 0.93 | 0.850 | 0.470 | 0.556 | 0.957 | 0.701 |
| yanismiraoui | 78 | 1.00 | - | - | - | 1.000 | 1.000 |

## prompt_injection, in-domain — threat-only (b = -3.32)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| prompt_injection | 2773 | 1.12 | 0.954 | 0.954 | 0.989 | 0.836 | 0.463 | 0.153 → 0.148 | 0.079 → 0.078 | 0.023 → 0.015 | 0.0 |

**prompt_injection by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| awesome-prompts | 71 | 0.00 | - | - | 0.000 | - | 1.000 |
| dolly | 222 | 0.00 | - | - | 0.000 | - | 1.000 |
| mkqa-de | 13 | 0.00 | - | - | 0.077 | - | 0.480 |
| mkqa-es | 9 | 0.00 | - | - | 0.000 | - | 1.000 |
| mkqa-fr | 14 | 0.00 | - | - | 0.000 | - | 1.000 |
| mkqa-it | 18 | 0.00 | - | - | 0.000 | - | 1.000 |
| mkqa-pt | 19 | 0.00 | - | - | 0.105 | - | 0.472 |
| mkqa-ru | 68 | 0.00 | - | - | 0.088 | - | 0.477 |
| mosscap | 53 | 1.00 | - | - | - | 1.000 | 1.000 |
| neuralchemy | 900 | 0.59 | 0.992 | 0.844 | 0.059 | 0.985 | 0.965 |
| ru-injections | 54 | 1.00 | - | - | - | 0.870 | 0.465 |
| s-labs | 1000 | 0.47 | 0.992 | 0.913 | 0.000 | 0.860 | 0.933 |
| simsonsun | 128 | 1.00 | - | - | - | 0.953 | 0.488 |
| wildjailbreak | 126 | 0.93 | 0.863 | 0.513 | 0.667 | 0.966 | 0.666 |
| yanismiraoui | 78 | 1.00 | - | - | - | 1.000 | 1.000 |

## prompt_injection, in-domain — safe-only (b = 2.43)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| prompt_injection | 2773 | 0.71 | 0.931 | 0.931 | 0.984 | 0.796 | 0.603 | 0.173 → 0.164 | 0.096 → 0.096 | 0.040 → 0.019 | 0.0 |

**prompt_injection by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| awesome-prompts | 71 | 0.00 | - | - | 0.000 | - | 1.000 |
| dolly | 222 | 0.00 | - | - | 0.000 | - | 1.000 |
| mkqa-de | 13 | 0.00 | - | - | 0.077 | - | 0.480 |
| mkqa-es | 9 | 0.00 | - | - | 0.000 | - | 1.000 |
| mkqa-fr | 14 | 0.00 | - | - | 0.071 | - | 0.481 |
| mkqa-it | 18 | 0.00 | - | - | 0.111 | - | 0.471 |
| mkqa-pt | 19 | 0.00 | - | - | 0.158 | - | 0.457 |
| mkqa-ru | 68 | 0.00 | - | - | 0.426 | - | 0.364 |
| mosscap | 53 | 1.00 | - | - | - | 0.887 | 0.470 |
| neuralchemy | 900 | 0.59 | 0.992 | 0.903 | 0.032 | 0.945 | 0.953 |
| ru-injections | 54 | 1.00 | - | - | - | 1.000 | 1.000 |
| s-labs | 1000 | 0.47 | 0.991 | 0.898 | 0.009 | 0.890 | 0.942 |
| simsonsun | 128 | 1.00 | - | - | - | 0.789 | 0.441 |
| wildjailbreak | 126 | 0.93 | 0.831 | 0.419 | 0.333 | 0.829 | 0.618 |
| yanismiraoui | 78 | 1.00 | - | - | - | 0.987 | 0.497 |

## prompt_injection, held-out — two-pass (b = 0.00)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| prompt_injection | 1951 | 1.71 | 0.731 | 0.731 | 0.824 | 0.149 | 0.081 | 1.060 → 0.702 | 0.454 → 0.410 | 0.212 → 0.167 | 0.0 |

**prompt_injection by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| deepset | 662 | 0.40 | 0.787 | 0.137 | 0.276 | 0.722 | 0.717 |
| jackhhao | 1289 | 0.51 | 0.848 | 0.181 | 0.398 | 0.866 | 0.730 |

## prompt_injection, held-out — threat-only (b = -3.32)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| prompt_injection | 1951 | 1.12 | 0.711 | 0.709 | 0.830 | 0.232 | 0.011 | 0.832 → 0.764 | 0.473 → 0.459 | 0.215 → 0.202 | 0.0 |

**prompt_injection by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| deepset | 662 | 0.40 | 0.828 | 0.247 | 0.263 | 0.745 | 0.734 |
| jackhhao | 1289 | 0.51 | 0.831 | 0.138 | 0.506 | 0.896 | 0.683 |

## prompt_injection, held-out — safe-only (b = 2.43)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| prompt_injection | 1951 | 0.71 | 0.743 | 0.743 | 0.799 | 0.031 | 0.012 | 0.639 → 0.769 | 0.390 → 0.412 | 0.109 → 0.154 | 0.0 |

**prompt_injection by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| deepset | 662 | 0.40 | 0.724 | 0.034 | 0.363 | 0.696 | 0.656 |
| jackhhao | 1289 | 0.51 | 0.848 | 0.055 | 0.277 | 0.846 | 0.784 |

## prompt_injection, val — two-pass (b = 0.00)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| prompt_injection | 1500 | 1.71 | 0.736 | 0.735 | 0.796 | 0.067 | 0.003 | 1.346 → 0.853 | 0.478 → 0.446 | 0.225 → 0.186 | 0.0 |

## prompt_injection, val — threat-only (b = -3.32)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| prompt_injection | 1500 | 1.12 | 0.737 | 0.737 | 0.791 | 0.045 | 0.000 | 0.835 → 0.768 | 0.455 → 0.444 | 0.195 → 0.183 | 0.0 |

## prompt_injection, val — safe-only (b = 2.43)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| prompt_injection | 1500 | 0.71 | 0.738 | 0.735 | 0.789 | 0.013 | 0.005 | 0.709 → 0.896 | 0.427 → 0.454 | 0.152 → 0.189 | 0.0 |
