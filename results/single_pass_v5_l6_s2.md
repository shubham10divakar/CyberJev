## One pass vs two — `runs/cyber-jev-v5-l6-s2`, max_length 256

| decision | test set | variant | T | b | calib NLL | AUROC | DR@1%FPR | NLL | ECE |
|---|---|---|---|---|---|---|---|---|---|
| http_attack | in-domain | two-pass | 1.49 | 0.00 | 0.081 | 0.995 | 0.947 | 0.085 | 0.008 |
| http_attack | in-domain | threat-only | 1.05 | -4.64 | 0.121 | 0.976 | 0.944 | 0.122 | 0.005 |
| http_attack | in-domain | safe-only | 0.55 | 4.96 | 0.166 | 0.988 | 0.842 | 0.176 | 0.049 |
| http_attack | held-out | two-pass | 1.49 | 0.00 | 0.081 | 0.959 | 0.695 | 0.684 | 0.138 |
| http_attack | held-out | threat-only | 1.05 | -4.64 | 0.121 | 0.956 | 0.609 | 0.860 | 0.135 |
| http_attack | held-out | safe-only | 0.55 | 4.96 | 0.166 | 0.957 | 0.695 | 0.308 | 0.059 |
| http_attack | val | two-pass | 1.49 | 0.00 | 0.081 | 0.900 | 0.233 | 0.632 | 0.162 |
| http_attack | val | threat-only | 1.05 | -4.64 | 0.121 | 0.887 | 0.221 | 0.760 | 0.158 |
| http_attack | val | safe-only | 0.55 | 4.96 | 0.166 | 0.895 | 0.298 | 0.481 | 0.078 |
| phishing_url | in-domain | two-pass | 1.73 | 0.00 | 0.253 | 0.968 | 0.727 | 0.227 | 0.014 |
| phishing_url | in-domain | threat-only | 1.01 | -3.27 | 0.273 | 0.964 | 0.736 | 0.242 | 0.020 |
| phishing_url | in-domain | safe-only | 0.75 | 3.31 | 0.246 | 0.969 | 0.723 | 0.226 | 0.010 |
| phishing_url | held-out | two-pass | 1.73 | 0.00 | 0.253 | 0.795 | 0.138 | 0.560 | 0.096 |
| phishing_url | held-out | threat-only | 1.01 | -3.27 | 0.273 | 0.769 | 0.101 | 0.596 | 0.107 |
| phishing_url | held-out | safe-only | 0.75 | 3.31 | 0.246 | 0.821 | 0.168 | 0.528 | 0.088 |
| phishing_url | val | two-pass | 1.73 | 0.00 | 0.253 | 0.938 | 0.579 | 0.337 | 0.036 |
| phishing_url | val | threat-only | 1.01 | -3.27 | 0.273 | 0.933 | 0.557 | 0.345 | 0.028 |
| phishing_url | val | safe-only | 0.75 | 3.31 | 0.246 | 0.938 | 0.560 | 0.343 | 0.037 |
| prompt_injection | in-domain | two-pass | 1.75 | 0.00 | 0.081 | 0.994 | 0.902 | 0.111 | 0.013 |
| prompt_injection | in-domain | threat-only | 1.26 | -2.38 | 0.091 | 0.993 | 0.890 | 0.122 | 0.013 |
| prompt_injection | in-domain | safe-only | 0.53 | 1.87 | 0.102 | 0.991 | 0.853 | 0.119 | 0.008 |
| prompt_injection | held-out | two-pass | 1.75 | 0.00 | 0.081 | 0.782 | 0.046 | 0.944 | 0.217 |
| prompt_injection | held-out | threat-only | 1.26 | -2.38 | 0.091 | 0.801 | 0.183 | 0.971 | 0.234 |
| prompt_injection | held-out | safe-only | 0.53 | 1.87 | 0.102 | 0.745 | 0.022 | 1.125 | 0.206 |
| prompt_injection | val | two-pass | 1.75 | 0.00 | 0.081 | 0.800 | 0.111 | 0.727 | 0.165 |
| prompt_injection | val | threat-only | 1.26 | -2.38 | 0.091 | 0.801 | 0.079 | 0.747 | 0.169 |
| prompt_injection | val | safe-only | 0.53 | 1.87 | 0.102 | 0.761 | 0.021 | 0.828 | 0.172 |

One-pass variant picked: http_attack → safe-only (by val AUROC), phishing_url → safe-only (by val AUROC), prompt_injection → threat-only (by val AUROC)

## http_attack, in-domain — two-pass (b = 0.00)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 4700 | 1.49 | 0.968 | 0.968 | 0.995 | 0.947 | 0.919 | 0.095 → 0.085 | 0.053 → 0.049 | 0.018 → 0.008 | 0.0 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| ai-waf | 1200 | 0.28 | 0.994 | 0.946 | 0.008 | 0.946 | 0.974 |
| csic2010 | 1500 | 0.60 | 0.972 | 0.863 | 0.015 | 0.879 | 0.920 |
| gretel-sql | 500 | 0.00 | - | - | 0.002 | - | 0.499 |
| web-attacks | 1500 | 0.80 | 1.000 | 0.996 | 0.007 | 0.996 | 0.993 |

## http_attack, in-domain — threat-only (b = -4.64)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 4700 | 1.05 | 0.966 | 0.966 | 0.976 | 0.944 | 0.918 | 0.122 → 0.122 | 0.061 → 0.061 | 0.008 → 0.005 | 0.0 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| ai-waf | 1200 | 0.28 | 0.990 | 0.943 | 0.010 | 0.943 | 0.971 |
| csic2010 | 1500 | 0.60 | 0.953 | 0.856 | 0.015 | 0.872 | 0.915 |
| gretel-sql | 500 | 0.00 | - | - | 0.002 | - | 0.499 |
| web-attacks | 1500 | 0.80 | 0.999 | 0.997 | 0.007 | 0.996 | 0.993 |

## http_attack, in-domain — safe-only (b = 4.96)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 4700 | 0.55 | 0.931 | 0.930 | 0.988 | 0.842 | 0.734 | 0.217 → 0.176 | 0.115 → 0.102 | 0.101 → 0.049 | 0.0 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| ai-waf | 1200 | 0.28 | 0.994 | 0.961 | 0.006 | 0.949 | 0.977 |
| csic2010 | 1500 | 0.60 | 0.933 | 0.540 | 0.459 | 0.978 | 0.772 |
| gretel-sql | 500 | 0.00 | - | - | 0.000 | - | 1.000 |
| web-attacks | 1500 | 0.80 | 1.000 | 0.995 | 0.003 | 0.993 | 0.991 |

## http_attack, held-out — two-pass (b = 0.00)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 10320 | 1.49 | 0.831 | 0.825 | 0.959 | 0.695 | 0.546 | 0.986 → 0.684 | 0.314 → 0.301 | 0.151 → 0.138 | 0.0 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| dvwa-juiceshop | 4320 | 0.73 | 0.863 | 0.459 | 0.590 | 0.959 | 0.710 |
| sqli-queries | 6000 | 0.36 | 0.994 | 0.946 | 0.242 | 0.994 | 0.842 |

## http_attack, held-out — threat-only (b = -4.64)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 10320 | 1.05 | 0.825 | 0.819 | 0.956 | 0.609 | 0.496 | 0.897 → 0.860 | 0.322 → 0.321 | 0.138 → 0.135 | 0.0 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| dvwa-juiceshop | 4320 | 0.73 | 0.842 | 0.346 | 0.599 | 0.960 | 0.706 |
| sqli-queries | 6000 | 0.36 | 0.994 | 0.944 | 0.255 | 0.995 | 0.834 |

## http_attack, held-out — safe-only (b = 4.96)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 10320 | 0.55 | 0.856 | 0.854 | 0.957 | 0.695 | 0.544 | 0.317 → 0.308 | 0.194 → 0.195 | 0.080 → 0.059 | 0.0 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| dvwa-juiceshop | 4320 | 0.73 | 0.883 | 0.539 | 0.430 | 0.896 | 0.744 |
| sqli-queries | 6000 | 0.36 | 0.989 | 0.908 | 0.161 | 0.978 | 0.886 |

## http_attack, val — two-pass (b = 0.00)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 3563 | 1.49 | 0.773 | 0.772 | 0.900 | 0.233 | 0.072 | 0.876 → 0.632 | 0.389 → 0.355 | 0.188 → 0.162 | 0.0 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| spider | 563 | 0.00 | - | - | 0.005 | - | 0.499 |
| waf-v2 | 3000 | 0.50 | 0.864 | 0.201 | 0.395 | 0.857 | 0.727 |

## http_attack, val — threat-only (b = -4.64)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 3563 | 1.05 | 0.768 | 0.768 | 0.887 | 0.221 | 0.065 | 0.787 → 0.760 | 0.389 → 0.385 | 0.163 → 0.158 | 0.0 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| spider | 563 | 0.00 | - | - | 0.007 | - | 0.498 |
| waf-v2 | 3000 | 0.50 | 0.846 | 0.199 | 0.413 | 0.866 | 0.721 |

## http_attack, val — safe-only (b = 4.96)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 3563 | 0.55 | 0.819 | 0.809 | 0.895 | 0.298 | 0.138 | 0.423 → 0.481 | 0.275 → 0.283 | 0.047 → 0.078 | 0.0 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| spider | 563 | 0.00 | - | - | 0.000 | - | 1.000 |
| waf-v2 | 3000 | 0.50 | 0.856 | 0.263 | 0.126 | 0.696 | 0.783 |

## phishing_url, in-domain — two-pass (b = 0.00)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| phishing_url | 1998 | 1.73 | 0.905 | 0.905 | 0.968 | 0.727 | 0.513 | 0.251 → 0.227 | 0.144 → 0.139 | 0.039 → 0.014 | 0.0 |

## phishing_url, in-domain — threat-only (b = -3.27)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| phishing_url | 1998 | 1.01 | 0.903 | 0.903 | 0.964 | 0.736 | 0.501 | 0.241 → 0.242 | 0.146 → 0.146 | 0.019 → 0.020 | 0.0 |

## phishing_url, in-domain — safe-only (b = 3.31)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| phishing_url | 1998 | 0.75 | 0.905 | 0.905 | 0.969 | 0.723 | 0.520 | 0.240 → 0.226 | 0.141 → 0.138 | 0.040 → 0.010 | 0.0 |

## phishing_url, held-out — two-pass (b = 0.00)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| phishing_url | 5000 | 1.73 | 0.731 | 0.708 | 0.795 | 0.138 | 0.067 | 0.736 → 0.560 | 0.408 → 0.365 | 0.162 → 0.096 | 0.0 |

**phishing_url by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| destroylist | 2000 | 1.00 | - | - | - | 0.661 | 0.398 |
| phishtrap | 3000 | 0.50 | 0.848 | 0.233 | 0.251 | 0.806 | 0.777 |

## phishing_url, held-out — threat-only (b = -3.27)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| phishing_url | 5000 | 1.01 | 0.716 | 0.692 | 0.769 | 0.101 | 0.035 | 0.598 → 0.596 | 0.389 → 0.388 | 0.109 → 0.107 | 0.0 |

**phishing_url by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| destroylist | 2000 | 1.00 | - | - | - | 0.649 | 0.393 |
| phishtrap | 3000 | 0.50 | 0.825 | 0.179 | 0.272 | 0.793 | 0.760 |

## phishing_url, held-out — safe-only (b = 3.31)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| phishing_url | 5000 | 0.75 | 0.746 | 0.724 | 0.821 | 0.168 | 0.061 | 0.501 → 0.528 | 0.334 → 0.347 | 0.044 → 0.088 | 0.0 |

**phishing_url by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| destroylist | 2000 | 1.00 | - | - | - | 0.672 | 0.402 |
| phishtrap | 3000 | 0.50 | 0.869 | 0.249 | 0.231 | 0.822 | 0.796 |

## phishing_url, val — two-pass (b = 0.00)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| phishing_url | 3000 | 1.73 | 0.872 | 0.872 | 0.938 | 0.579 | 0.308 | 0.434 → 0.337 | 0.216 → 0.203 | 0.078 → 0.036 | 0.0 |

## phishing_url, val — threat-only (b = -3.27)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| phishing_url | 3000 | 1.01 | 0.865 | 0.865 | 0.933 | 0.557 | 0.243 | 0.345 → 0.345 | 0.210 → 0.210 | 0.028 → 0.028 | 0.0 |

## phishing_url, val — safe-only (b = 3.31)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| phishing_url | 3000 | 0.75 | 0.870 | 0.870 | 0.938 | 0.560 | 0.299 | 0.333 → 0.343 | 0.202 → 0.203 | 0.026 → 0.037 | 0.0 |

## prompt_injection, in-domain — two-pass (b = 0.00)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| prompt_injection | 2500 | 1.75 | 0.962 | 0.962 | 0.994 | 0.902 | 0.744 | 0.154 → 0.111 | 0.066 → 0.061 | 0.029 → 0.013 | 0.0 |

**prompt_injection by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| awesome-prompts | 71 | 0.00 | - | - | 0.014 | - | 0.496 |
| dolly | 222 | 0.00 | - | - | 0.000 | - | 1.000 |
| mosscap | 53 | 1.00 | - | - | - | 0.962 | 0.490 |
| neuralchemy | 900 | 0.59 | 0.993 | 0.909 | 0.046 | 0.973 | 0.964 |
| s-labs | 1000 | 0.47 | 0.995 | 0.909 | 0.006 | 0.902 | 0.950 |
| simsonsun | 128 | 1.00 | - | - | - | 0.969 | 0.492 |
| wildjailbreak | 126 | 0.93 | 0.913 | 0.521 | 0.556 | 0.974 | 0.733 |

## prompt_injection, in-domain — threat-only (b = -2.38)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| prompt_injection | 2500 | 1.26 | 0.962 | 0.962 | 0.993 | 0.890 | 0.488 | 0.135 → 0.122 | 0.065 → 0.064 | 0.023 → 0.013 | 0.0 |

**prompt_injection by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| awesome-prompts | 71 | 0.00 | - | - | 0.014 | - | 0.496 |
| dolly | 222 | 0.00 | - | - | 0.000 | - | 1.000 |
| mosscap | 53 | 1.00 | - | - | - | 0.962 | 0.490 |
| neuralchemy | 900 | 0.59 | 0.992 | 0.759 | 0.048 | 0.977 | 0.966 |
| s-labs | 1000 | 0.47 | 0.995 | 0.917 | 0.006 | 0.898 | 0.948 |
| simsonsun | 128 | 1.00 | - | - | - | 0.969 | 0.492 |
| wildjailbreak | 126 | 0.93 | 0.900 | 0.427 | 0.556 | 0.974 | 0.733 |

## prompt_injection, in-domain — safe-only (b = 1.87)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| prompt_injection | 2500 | 0.53 | 0.955 | 0.955 | 0.991 | 0.853 | 0.723 | 0.157 → 0.119 | 0.076 → 0.067 | 0.063 → 0.008 | 0.0 |

**prompt_injection by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| awesome-prompts | 71 | 0.00 | - | - | 0.028 | - | 0.493 |
| dolly | 222 | 0.00 | - | - | 0.000 | - | 1.000 |
| mosscap | 53 | 1.00 | - | - | - | 0.906 | 0.475 |
| neuralchemy | 900 | 0.59 | 0.991 | 0.907 | 0.035 | 0.947 | 0.953 |
| s-labs | 1000 | 0.47 | 0.990 | 0.879 | 0.036 | 0.943 | 0.954 |
| simsonsun | 128 | 1.00 | - | - | - | 0.938 | 0.484 |
| wildjailbreak | 126 | 0.93 | 0.897 | 0.658 | 0.667 | 0.966 | 0.666 |

## prompt_injection, held-out — two-pass (b = 0.00)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| prompt_injection | 1951 | 1.75 | 0.704 | 0.698 | 0.782 | 0.046 | 0.008 | 1.533 → 0.944 | 0.544 → 0.502 | 0.260 → 0.217 | 0.0 |

**prompt_injection by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| deepset | 662 | 0.40 | 0.748 | 0.065 | 0.409 | 0.821 | 0.682 |
| jackhhao | 1289 | 0.51 | 0.811 | 0.023 | 0.502 | 0.926 | 0.700 |

## prompt_injection, held-out — threat-only (b = -2.38)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| prompt_injection | 1951 | 1.26 | 0.692 | 0.685 | 0.801 | 0.183 | 0.002 | 1.182 → 0.971 | 0.543 → 0.522 | 0.254 → 0.234 | 0.0 |

**prompt_injection by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| deepset | 662 | 0.40 | 0.787 | 0.186 | 0.383 | 0.806 | 0.691 |
| jackhhao | 1289 | 0.51 | 0.807 | 0.149 | 0.547 | 0.926 | 0.673 |

## prompt_injection, held-out — safe-only (b = 1.87)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| prompt_injection | 1951 | 0.53 | 0.700 | 0.694 | 0.745 | 0.022 | 0.005 | 0.755 → 1.125 | 0.463 → 0.507 | 0.122 → 0.206 | 0.0 |

**prompt_injection by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| deepset | 662 | 0.40 | 0.687 | 0.015 | 0.466 | 0.833 | 0.653 |
| jackhhao | 1289 | 0.51 | 0.805 | 0.015 | 0.484 | 0.929 | 0.711 |

## prompt_injection, val — two-pass (b = 0.00)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| prompt_injection | 1500 | 1.75 | 0.733 | 0.733 | 0.800 | 0.111 | 0.003 | 1.123 → 0.727 | 0.469 → 0.425 | 0.214 → 0.165 | 0.0 |

## prompt_injection, val — threat-only (b = -2.38)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| prompt_injection | 1500 | 1.26 | 0.739 | 0.739 | 0.801 | 0.079 | 0.020 | 0.886 → 0.747 | 0.448 → 0.428 | 0.192 → 0.169 | 0.0 |

## prompt_injection, val — safe-only (b = 1.87)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| prompt_injection | 1500 | 0.53 | 0.701 | 0.700 | 0.761 | 0.021 | 0.001 | 0.625 → 0.828 | 0.413 → 0.462 | 0.077 → 0.172 | 0.0 |
