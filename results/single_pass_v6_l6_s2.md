## One pass vs two — `runs/cyber-jev-v6-l6-s2`, max_length 256

| decision | test set | variant | T | b | calib NLL | AUROC | DR@1%FPR | NLL | ECE |
|---|---|---|---|---|---|---|---|---|---|
| http_attack | in-domain | two-pass | 1.72 | 0.00 | 0.064 | 0.996 | 0.966 | 0.073 | 0.006 |
| http_attack | in-domain | threat-only | 1.08 | -1.70 | 0.065 | 0.996 | 0.965 | 0.074 | 0.006 |
| http_attack | in-domain | safe-only | 0.70 | 1.93 | 0.068 | 0.996 | 0.966 | 0.074 | 0.004 |
| http_attack | held-out | two-pass | 1.72 | 0.00 | 0.064 | 0.973 | 0.693 | 0.661 | 0.128 |
| http_attack | held-out | threat-only | 1.08 | -1.70 | 0.065 | 0.960 | 0.491 | 0.669 | 0.130 |
| http_attack | held-out | safe-only | 0.70 | 1.93 | 0.068 | 0.981 | 0.825 | 0.575 | 0.114 |
| http_attack | val | two-pass | 1.72 | 0.00 | 0.064 | 0.919 | 0.301 | 0.726 | 0.143 |
| http_attack | val | threat-only | 1.08 | -1.70 | 0.065 | 0.920 | 0.298 | 0.711 | 0.143 |
| http_attack | val | safe-only | 0.70 | 1.93 | 0.068 | 0.913 | 0.185 | 0.684 | 0.136 |
| phishing_url | in-domain | two-pass | 2.07 | 0.00 | 0.254 | 0.968 | 0.701 | 0.234 | 0.014 |
| phishing_url | in-domain | threat-only | 1.34 | -2.18 | 0.264 | 0.965 | 0.700 | 0.238 | 0.013 |
| phishing_url | in-domain | safe-only | 0.82 | 2.49 | 0.252 | 0.969 | 0.670 | 0.234 | 0.014 |
| phishing_url | held-out | two-pass | 2.07 | 0.00 | 0.254 | 0.782 | 0.117 | 0.592 | 0.121 |
| phishing_url | held-out | threat-only | 1.34 | -2.18 | 0.264 | 0.769 | 0.095 | 0.614 | 0.131 |
| phishing_url | held-out | safe-only | 0.82 | 2.49 | 0.252 | 0.794 | 0.131 | 0.590 | 0.130 |
| phishing_url | val | two-pass | 2.07 | 0.00 | 0.254 | 0.942 | 0.615 | 0.339 | 0.040 |
| phishing_url | val | threat-only | 1.34 | -2.18 | 0.264 | 0.936 | 0.596 | 0.338 | 0.041 |
| phishing_url | val | safe-only | 0.82 | 2.49 | 0.252 | 0.945 | 0.578 | 0.333 | 0.039 |
| prompt_injection | in-domain | two-pass | 2.06 | 0.00 | 0.086 | 0.994 | 0.896 | 0.109 | 0.012 |
| prompt_injection | in-domain | threat-only | 1.36 | -2.80 | 0.092 | 0.993 | 0.889 | 0.114 | 0.010 |
| prompt_injection | in-domain | safe-only | 0.68 | 1.97 | 0.086 | 0.993 | 0.869 | 0.101 | 0.007 |
| prompt_injection | held-out | two-pass | 2.06 | 0.00 | 0.086 | 0.849 | 0.085 | 0.664 | 0.156 |
| prompt_injection | held-out | threat-only | 1.36 | -2.80 | 0.092 | 0.840 | 0.065 | 0.750 | 0.174 |
| prompt_injection | held-out | safe-only | 0.68 | 1.97 | 0.086 | 0.852 | 0.048 | 0.681 | 0.160 |
| prompt_injection | val | two-pass | 2.06 | 0.00 | 0.086 | 0.776 | 0.079 | 0.834 | 0.202 |
| prompt_injection | val | threat-only | 1.36 | -2.80 | 0.092 | 0.761 | 0.081 | 0.939 | 0.222 |
| prompt_injection | val | safe-only | 0.68 | 1.97 | 0.086 | 0.788 | 0.047 | 0.792 | 0.187 |

One-pass variant picked: http_attack → threat-only (by val AUROC), phishing_url → safe-only (by val AUROC), prompt_injection → safe-only (by val AUROC)

## http_attack, in-domain — two-pass (b = 0.00)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 4700 | 1.72 | 0.977 | 0.977 | 0.996 | 0.966 | 0.932 | 0.094 → 0.073 | 0.041 → 0.038 | 0.018 → 0.006 | 0.0 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| ai-waf | 1200 | 0.28 | 0.994 | 0.940 | 0.014 | 0.952 | 0.971 |
| csic2010 | 1500 | 0.60 | 0.983 | 0.925 | 0.022 | 0.931 | 0.948 |
| gretel-sql | 500 | 0.00 | - | - | 0.000 | - | 1.000 |
| web-attacks | 1500 | 0.80 | 1.000 | 0.998 | 0.007 | 0.998 | 0.996 |

## http_attack, in-domain — threat-only (b = -1.70)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 4700 | 1.08 | 0.976 | 0.976 | 0.996 | 0.965 | 0.881 | 0.075 → 0.074 | 0.039 → 0.039 | 0.005 → 0.006 | 0.0 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| ai-waf | 1200 | 0.28 | 0.994 | 0.940 | 0.017 | 0.955 | 0.969 |
| csic2010 | 1500 | 0.60 | 0.982 | 0.921 | 0.023 | 0.931 | 0.948 |
| gretel-sql | 500 | 0.00 | - | - | 0.000 | - | 1.000 |
| web-attacks | 1500 | 0.80 | 0.999 | 0.998 | 0.007 | 0.997 | 0.995 |

## http_attack, in-domain — safe-only (b = 1.93)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 4700 | 0.70 | 0.978 | 0.978 | 0.996 | 0.966 | 0.936 | 0.084 → 0.074 | 0.040 → 0.039 | 0.023 → 0.004 | 0.0 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| ai-waf | 1200 | 0.28 | 0.992 | 0.943 | 0.016 | 0.955 | 0.970 |
| csic2010 | 1500 | 0.60 | 0.980 | 0.918 | 0.018 | 0.932 | 0.951 |
| gretel-sql | 500 | 0.00 | - | - | 0.000 | - | 1.000 |
| web-attacks | 1500 | 0.80 | 1.000 | 0.998 | 0.007 | 0.998 | 0.996 |

## http_attack, held-out — two-pass (b = 0.00)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 10320 | 1.72 | 0.852 | 0.847 | 0.973 | 0.693 | 0.389 | 1.105 → 0.661 | 0.285 → 0.272 | 0.140 → 0.128 | 0.0 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| dvwa-juiceshop | 4320 | 0.73 | 0.915 | 0.499 | 0.535 | 0.990 | 0.764 |
| sqli-queries | 6000 | 0.36 | 0.991 | 0.931 | 0.222 | 0.986 | 0.851 |

## http_attack, held-out — threat-only (b = -1.70)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 10320 | 1.08 | 0.852 | 0.848 | 0.960 | 0.491 | 0.216 | 0.717 → 0.669 | 0.278 → 0.275 | 0.132 → 0.130 | 0.0 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| dvwa-juiceshop | 4320 | 0.73 | 0.864 | 0.301 | 0.536 | 0.985 | 0.759 |
| sqli-queries | 6000 | 0.36 | 0.987 | 0.886 | 0.216 | 0.985 | 0.854 |

## http_attack, held-out — safe-only (b = 1.93)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 10320 | 0.70 | 0.856 | 0.851 | 0.981 | 0.825 | 0.644 | 0.440 → 0.575 | 0.241 → 0.254 | 0.090 → 0.114 | 0.0 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| dvwa-juiceshop | 4320 | 0.73 | 0.949 | 0.669 | 0.523 | 0.991 | 0.771 |
| sqli-queries | 6000 | 0.36 | 0.994 | 0.960 | 0.219 | 0.992 | 0.855 |

## http_attack, val — two-pass (b = 0.00)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 3563 | 1.72 | 0.804 | 0.804 | 0.919 | 0.301 | 0.123 | 1.174 → 0.726 | 0.354 → 0.333 | 0.168 → 0.143 | 0.0 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| spider | 563 | 0.00 | - | - | 0.000 | - | 1.000 |
| waf-v2 | 3000 | 0.50 | 0.888 | 0.275 | 0.382 | 0.916 | 0.762 |

## http_attack, val — threat-only (b = -1.70)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 3563 | 1.08 | 0.816 | 0.815 | 0.920 | 0.298 | 0.157 | 0.758 → 0.711 | 0.329 → 0.325 | 0.147 → 0.143 | 0.0 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| spider | 563 | 0.00 | - | - | 0.000 | - | 1.000 |
| waf-v2 | 3000 | 0.50 | 0.891 | 0.266 | 0.353 | 0.915 | 0.777 |

## http_attack, val — safe-only (b = 1.93)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 3563 | 0.70 | 0.793 | 0.793 | 0.913 | 0.185 | 0.027 | 0.547 → 0.684 | 0.321 → 0.341 | 0.105 → 0.136 | 0.0 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| spider | 563 | 0.00 | - | - | 0.000 | - | 1.000 |
| waf-v2 | 3000 | 0.50 | 0.880 | 0.164 | 0.411 | 0.919 | 0.747 |

## phishing_url, in-domain — two-pass (b = 0.00)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| phishing_url | 1998 | 2.07 | 0.914 | 0.914 | 0.968 | 0.701 | 0.405 | 0.295 → 0.234 | 0.144 → 0.137 | 0.050 → 0.014 | 0.0 |

## phishing_url, in-domain — threat-only (b = -2.18)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| phishing_url | 1998 | 1.34 | 0.911 | 0.911 | 0.965 | 0.700 | 0.450 | 0.243 → 0.238 | 0.141 → 0.140 | 0.023 → 0.013 | 0.0 |

## phishing_url, in-domain — safe-only (b = 2.49)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| phishing_url | 1998 | 0.82 | 0.907 | 0.907 | 0.969 | 0.670 | 0.257 | 0.242 → 0.234 | 0.139 → 0.138 | 0.032 → 0.014 | 0.0 |

## phishing_url, held-out — two-pass (b = 0.00)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| phishing_url | 5000 | 2.07 | 0.719 | 0.701 | 0.782 | 0.117 | 0.026 | 0.921 → 0.592 | 0.463 → 0.390 | 0.206 → 0.121 | 0.0 |

**phishing_url by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| destroylist | 2000 | 1.00 | - | - | - | 0.627 | 0.385 |
| phishtrap | 3000 | 0.50 | 0.832 | 0.195 | 0.209 | 0.771 | 0.781 |

## phishing_url, held-out — threat-only (b = -2.18)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| phishing_url | 5000 | 1.34 | 0.704 | 0.688 | 0.769 | 0.095 | 0.026 | 0.708 → 0.614 | 0.441 → 0.410 | 0.171 → 0.131 | 0.0 |

**phishing_url by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| destroylist | 2000 | 1.00 | - | - | - | 0.604 | 0.376 |
| phishtrap | 3000 | 0.50 | 0.818 | 0.153 | 0.205 | 0.749 | 0.772 |

## phishing_url, held-out — safe-only (b = 2.49)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| phishing_url | 5000 | 0.82 | 0.721 | 0.704 | 0.794 | 0.131 | 0.024 | 0.555 → 0.590 | 0.376 → 0.392 | 0.099 → 0.130 | 0.0 |

**phishing_url by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| destroylist | 2000 | 1.00 | - | - | - | 0.619 | 0.383 |
| phishtrap | 3000 | 0.50 | 0.844 | 0.221 | 0.201 | 0.779 | 0.789 |

## phishing_url, val — two-pass (b = 0.00)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| phishing_url | 3000 | 2.07 | 0.880 | 0.880 | 0.942 | 0.615 | 0.160 | 0.506 → 0.339 | 0.214 → 0.199 | 0.086 → 0.040 | 0.0 |

## phishing_url, val — threat-only (b = -2.18)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| phishing_url | 3000 | 1.34 | 0.876 | 0.876 | 0.936 | 0.596 | 0.195 | 0.374 → 0.338 | 0.206 → 0.201 | 0.061 → 0.041 | 0.0 |

## phishing_url, val — safe-only (b = 2.49)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| phishing_url | 3000 | 0.82 | 0.876 | 0.876 | 0.945 | 0.578 | 0.115 | 0.324 → 0.333 | 0.194 → 0.195 | 0.025 → 0.039 | 0.0 |

## prompt_injection, in-domain — two-pass (b = 0.00)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| prompt_injection | 2773 | 2.06 | 0.961 | 0.961 | 0.994 | 0.896 | 0.496 | 0.169 → 0.109 | 0.067 → 0.060 | 0.030 → 0.012 | 0.0 |

**prompt_injection by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| awesome-prompts | 71 | 0.00 | - | - | 0.028 | - | 0.493 |
| dolly | 222 | 0.00 | - | - | 0.000 | - | 1.000 |
| mkqa-de | 13 | 0.00 | - | - | 0.000 | - | 1.000 |
| mkqa-es | 9 | 0.00 | - | - | 0.000 | - | 1.000 |
| mkqa-fr | 14 | 0.00 | - | - | 0.000 | - | 1.000 |
| mkqa-it | 18 | 0.00 | - | - | 0.000 | - | 1.000 |
| mkqa-pt | 19 | 0.00 | - | - | 0.000 | - | 1.000 |
| mkqa-ru | 68 | 0.00 | - | - | 0.029 | - | 0.493 |
| mosscap | 53 | 1.00 | - | - | - | 0.943 | 0.485 |
| neuralchemy | 900 | 0.59 | 0.994 | 0.867 | 0.043 | 0.972 | 0.965 |
| ru-injections | 54 | 1.00 | - | - | - | 0.870 | 0.465 |
| s-labs | 1000 | 0.47 | 0.994 | 0.924 | 0.004 | 0.896 | 0.948 |
| simsonsun | 128 | 1.00 | - | - | - | 0.969 | 0.492 |
| wildjailbreak | 126 | 0.93 | 0.928 | 0.598 | 0.556 | 0.983 | 0.752 |
| yanismiraoui | 78 | 1.00 | - | - | - | 1.000 | 1.000 |

## prompt_injection, in-domain — threat-only (b = -2.80)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| prompt_injection | 2773 | 1.36 | 0.961 | 0.961 | 0.993 | 0.889 | 0.614 | 0.129 → 0.114 | 0.065 → 0.061 | 0.024 → 0.010 | 0.0 |

**prompt_injection by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| awesome-prompts | 71 | 0.00 | - | - | 0.028 | - | 0.493 |
| dolly | 222 | 0.00 | - | - | 0.000 | - | 1.000 |
| mkqa-de | 13 | 0.00 | - | - | 0.000 | - | 1.000 |
| mkqa-es | 9 | 0.00 | - | - | 0.000 | - | 1.000 |
| mkqa-fr | 14 | 0.00 | - | - | 0.000 | - | 1.000 |
| mkqa-it | 18 | 0.00 | - | - | 0.000 | - | 1.000 |
| mkqa-pt | 19 | 0.00 | - | - | 0.000 | - | 1.000 |
| mkqa-ru | 68 | 0.00 | - | - | 0.029 | - | 0.493 |
| mosscap | 53 | 1.00 | - | - | - | 0.962 | 0.490 |
| neuralchemy | 900 | 0.59 | 0.993 | 0.880 | 0.051 | 0.973 | 0.962 |
| ru-injections | 54 | 1.00 | - | - | - | 0.852 | 0.460 |
| s-labs | 1000 | 0.47 | 0.992 | 0.915 | 0.009 | 0.909 | 0.952 |
| simsonsun | 128 | 1.00 | - | - | - | 0.969 | 0.492 |
| wildjailbreak | 126 | 0.93 | 0.944 | 0.735 | 0.556 | 0.974 | 0.733 |
| yanismiraoui | 78 | 1.00 | - | - | - | 1.000 | 1.000 |

## prompt_injection, in-domain — safe-only (b = 1.97)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| prompt_injection | 2773 | 0.68 | 0.966 | 0.966 | 0.993 | 0.869 | 0.392 | 0.117 → 0.101 | 0.056 → 0.054 | 0.033 → 0.007 | 0.0 |

**prompt_injection by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| awesome-prompts | 71 | 0.00 | - | - | 0.028 | - | 0.493 |
| dolly | 222 | 0.00 | - | - | 0.000 | - | 1.000 |
| mkqa-de | 13 | 0.00 | - | - | 0.000 | - | 1.000 |
| mkqa-es | 9 | 0.00 | - | - | 0.000 | - | 1.000 |
| mkqa-fr | 14 | 0.00 | - | - | 0.000 | - | 1.000 |
| mkqa-it | 18 | 0.00 | - | - | 0.000 | - | 1.000 |
| mkqa-pt | 19 | 0.00 | - | - | 0.053 | - | 0.486 |
| mkqa-ru | 68 | 0.00 | - | - | 0.088 | - | 0.477 |
| mosscap | 53 | 1.00 | - | - | - | 0.943 | 0.485 |
| neuralchemy | 900 | 0.59 | 0.993 | 0.871 | 0.046 | 0.977 | 0.967 |
| ru-injections | 54 | 1.00 | - | - | - | 0.889 | 0.471 |
| s-labs | 1000 | 0.47 | 0.995 | 0.930 | 0.009 | 0.930 | 0.962 |
| simsonsun | 128 | 1.00 | - | - | - | 0.984 | 0.496 |
| wildjailbreak | 126 | 0.93 | 0.847 | 0.120 | 0.667 | 0.983 | 0.697 |
| yanismiraoui | 78 | 1.00 | - | - | - | 1.000 | 1.000 |

## prompt_injection, held-out — two-pass (b = 0.00)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| prompt_injection | 1951 | 2.06 | 0.763 | 0.763 | 0.849 | 0.085 | 0.009 | 1.216 → 0.664 | 0.423 → 0.375 | 0.203 → 0.156 | 0.0 |

**prompt_injection by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| deepset | 662 | 0.40 | 0.840 | 0.110 | 0.128 | 0.589 | 0.738 |
| jackhhao | 1289 | 0.51 | 0.867 | 0.020 | 0.378 | 0.905 | 0.760 |

## prompt_injection, held-out — threat-only (b = -2.80)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| prompt_injection | 1951 | 1.36 | 0.756 | 0.755 | 0.840 | 0.065 | 0.001 | 0.965 → 0.750 | 0.423 → 0.401 | 0.198 → 0.174 | 0.0 |

**prompt_injection by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| deepset | 662 | 0.40 | 0.839 | 0.122 | 0.130 | 0.616 | 0.749 |
| jackhhao | 1289 | 0.51 | 0.849 | 0.009 | 0.408 | 0.902 | 0.742 |

## prompt_injection, held-out — safe-only (b = 1.97)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| prompt_injection | 1951 | 0.68 | 0.750 | 0.750 | 0.852 | 0.048 | 0.010 | 0.554 → 0.681 | 0.351 → 0.382 | 0.109 → 0.160 | 0.0 |

**prompt_injection by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| deepset | 662 | 0.40 | 0.827 | 0.061 | 0.168 | 0.639 | 0.739 |
| jackhhao | 1289 | 0.51 | 0.881 | 0.052 | 0.448 | 0.940 | 0.737 |

## prompt_injection, val — two-pass (b = 0.00)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| prompt_injection | 1500 | 2.06 | 0.708 | 0.708 | 0.776 | 0.079 | 0.019 | 1.548 → 0.834 | 0.532 → 0.476 | 0.257 → 0.202 | 0.0 |

## prompt_injection, val — threat-only (b = -2.80)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| prompt_injection | 1500 | 1.36 | 0.701 | 0.701 | 0.761 | 0.081 | 0.024 | 1.217 → 0.939 | 0.532 → 0.505 | 0.247 → 0.222 | 0.0 |

## prompt_injection, val — safe-only (b = 1.97)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| prompt_injection | 1500 | 0.68 | 0.700 | 0.697 | 0.788 | 0.047 | 0.012 | 0.644 → 0.792 | 0.421 → 0.459 | 0.131 → 0.187 | 0.0 |
