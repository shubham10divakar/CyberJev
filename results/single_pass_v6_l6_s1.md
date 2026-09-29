## One pass vs two — `runs/cyber-jev-v6-l6-s1`, max_length 256

| decision | test set | variant | T | b | calib NLL | AUROC | DR@1%FPR | NLL | ECE |
|---|---|---|---|---|---|---|---|---|---|
| http_attack | in-domain | two-pass | 1.98 | 0.00 | 0.068 | 0.997 | 0.970 | 0.065 | 0.006 |
| http_attack | in-domain | threat-only | 1.18 | -3.06 | 0.068 | 0.997 | 0.970 | 0.067 | 0.003 |
| http_attack | in-domain | safe-only | 0.73 | 2.60 | 0.071 | 0.996 | 0.969 | 0.067 | 0.006 |
| http_attack | held-out | two-pass | 1.98 | 0.00 | 0.068 | 0.952 | 0.645 | 0.687 | 0.146 |
| http_attack | held-out | threat-only | 1.18 | -3.06 | 0.068 | 0.950 | 0.609 | 0.803 | 0.151 |
| http_attack | held-out | safe-only | 0.73 | 2.60 | 0.071 | 0.945 | 0.587 | 0.680 | 0.141 |
| http_attack | val | two-pass | 1.98 | 0.00 | 0.068 | 0.919 | 0.330 | 0.489 | 0.093 |
| http_attack | val | threat-only | 1.18 | -3.06 | 0.068 | 0.923 | 0.305 | 0.515 | 0.098 |
| http_attack | val | safe-only | 0.73 | 2.60 | 0.071 | 0.905 | 0.253 | 0.547 | 0.121 |
| phishing_url | in-domain | two-pass | 2.45 | 0.00 | 0.255 | 0.971 | 0.721 | 0.227 | 0.026 |
| phishing_url | in-domain | threat-only | 1.37 | -3.13 | 0.260 | 0.969 | 0.734 | 0.230 | 0.023 |
| phishing_url | in-domain | safe-only | 1.06 | 2.65 | 0.255 | 0.969 | 0.610 | 0.235 | 0.018 |
| phishing_url | held-out | two-pass | 2.45 | 0.00 | 0.255 | 0.789 | 0.143 | 0.615 | 0.139 |
| phishing_url | held-out | threat-only | 1.37 | -3.13 | 0.260 | 0.785 | 0.125 | 0.588 | 0.118 |
| phishing_url | held-out | safe-only | 1.06 | 2.65 | 0.255 | 0.786 | 0.147 | 0.611 | 0.141 |
| phishing_url | val | two-pass | 2.45 | 0.00 | 0.255 | 0.943 | 0.569 | 0.318 | 0.026 |
| phishing_url | val | threat-only | 1.37 | -3.13 | 0.260 | 0.942 | 0.611 | 0.322 | 0.027 |
| phishing_url | val | safe-only | 1.06 | 2.65 | 0.255 | 0.938 | 0.489 | 0.345 | 0.036 |
| prompt_injection | in-domain | two-pass | 2.07 | 0.00 | 0.083 | 0.994 | 0.884 | 0.120 | 0.015 |
| prompt_injection | in-domain | threat-only | 1.27 | -3.42 | 0.083 | 0.994 | 0.882 | 0.119 | 0.016 |
| prompt_injection | in-domain | safe-only | 0.74 | 2.16 | 0.088 | 0.993 | 0.859 | 0.117 | 0.013 |
| prompt_injection | held-out | two-pass | 2.07 | 0.00 | 0.083 | 0.844 | 0.173 | 0.707 | 0.172 |
| prompt_injection | held-out | threat-only | 1.27 | -3.42 | 0.083 | 0.836 | 0.129 | 0.839 | 0.199 |
| prompt_injection | held-out | safe-only | 0.74 | 2.16 | 0.088 | 0.835 | 0.088 | 0.761 | 0.162 |
| prompt_injection | val | two-pass | 2.07 | 0.00 | 0.083 | 0.787 | 0.076 | 0.797 | 0.190 |
| prompt_injection | val | threat-only | 1.27 | -3.42 | 0.083 | 0.773 | 0.053 | 0.917 | 0.210 |
| prompt_injection | val | safe-only | 0.74 | 2.16 | 0.088 | 0.797 | 0.091 | 0.754 | 0.158 |

One-pass variant picked: http_attack → threat-only (by val AUROC), phishing_url → threat-only (by val AUROC), prompt_injection → safe-only (by val AUROC)

## http_attack, in-domain — two-pass (b = 0.00)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 4700 | 1.98 | 0.980 | 0.980 | 0.997 | 0.970 | 0.942 | 0.091 → 0.065 | 0.038 → 0.034 | 0.017 → 0.006 | 0.0 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| ai-waf | 1200 | 0.28 | 0.998 | 0.967 | 0.005 | 0.961 | 0.982 |
| csic2010 | 1500 | 0.60 | 0.983 | 0.928 | 0.030 | 0.938 | 0.949 |
| gretel-sql | 500 | 0.00 | - | - | 0.000 | - | 1.000 |
| web-attacks | 1500 | 0.80 | 1.000 | 0.998 | 0.007 | 0.997 | 0.995 |

## http_attack, in-domain — threat-only (b = -3.06)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 4700 | 1.18 | 0.980 | 0.980 | 0.997 | 0.970 | 0.945 | 0.069 → 0.067 | 0.035 → 0.035 | 0.008 → 0.003 | 0.0 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| ai-waf | 1200 | 0.28 | 0.998 | 0.964 | 0.006 | 0.964 | 0.982 |
| csic2010 | 1500 | 0.60 | 0.983 | 0.920 | 0.032 | 0.939 | 0.949 |
| gretel-sql | 500 | 0.00 | - | - | 0.000 | - | 1.000 |
| web-attacks | 1500 | 0.80 | 1.000 | 0.998 | 0.007 | 0.997 | 0.995 |

## http_attack, in-domain — safe-only (b = 2.60)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 4700 | 0.73 | 0.979 | 0.979 | 0.996 | 0.969 | 0.941 | 0.077 → 0.067 | 0.037 → 0.035 | 0.024 → 0.006 | 0.0 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| ai-waf | 1200 | 0.28 | 0.997 | 0.970 | 0.005 | 0.958 | 0.981 |
| csic2010 | 1500 | 0.60 | 0.982 | 0.922 | 0.028 | 0.935 | 0.948 |
| gretel-sql | 500 | 0.00 | - | - | 0.000 | - | 1.000 |
| web-attacks | 1500 | 0.80 | 1.000 | 0.999 | 0.007 | 0.997 | 0.995 |

## http_attack, held-out — two-pass (b = 0.00)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 10320 | 1.98 | 0.827 | 0.822 | 0.952 | 0.645 | 0.408 | 1.314 → 0.687 | 0.332 → 0.315 | 0.163 → 0.146 | 0.0 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| dvwa-juiceshop | 4320 | 0.73 | 0.849 | 0.233 | 0.594 | 0.955 | 0.705 |
| sqli-queries | 6000 | 0.36 | 0.994 | 0.955 | 0.246 | 0.994 | 0.839 |

## http_attack, held-out — threat-only (b = -3.06)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 10320 | 1.18 | 0.826 | 0.820 | 0.950 | 0.609 | 0.266 | 0.933 → 0.803 | 0.330 → 0.325 | 0.157 → 0.151 | 0.0 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| dvwa-juiceshop | 4320 | 0.73 | 0.820 | 0.212 | 0.616 | 0.960 | 0.696 |
| sqli-queries | 6000 | 0.36 | 0.994 | 0.950 | 0.247 | 0.994 | 0.838 |

## http_attack, held-out — safe-only (b = 2.60)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 10320 | 0.73 | 0.830 | 0.825 | 0.945 | 0.587 | 0.498 | 0.530 → 0.680 | 0.294 → 0.309 | 0.119 → 0.141 | 0.0 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| dvwa-juiceshop | 4320 | 0.73 | 0.871 | 0.287 | 0.555 | 0.950 | 0.723 |
| sqli-queries | 6000 | 0.36 | 0.993 | 0.952 | 0.247 | 0.993 | 0.838 |

## http_attack, val — two-pass (b = 0.00)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 3563 | 1.98 | 0.859 | 0.856 | 0.919 | 0.330 | 0.135 | 0.877 → 0.489 | 0.262 → 0.245 | 0.122 → 0.093 | 0.0 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| spider | 563 | 0.00 | - | - | 0.000 | - | 1.000 |
| waf-v2 | 3000 | 0.50 | 0.889 | 0.279 | 0.175 | 0.841 | 0.833 |

## http_attack, val — threat-only (b = -3.06)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 3563 | 1.18 | 0.863 | 0.860 | 0.923 | 0.305 | 0.099 | 0.587 → 0.515 | 0.246 → 0.241 | 0.107 → 0.098 | 0.0 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| spider | 563 | 0.00 | - | - | 0.007 | - | 0.498 |
| waf-v2 | 3000 | 0.50 | 0.895 | 0.261 | 0.173 | 0.851 | 0.839 |

## http_attack, val — safe-only (b = 2.60)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 3563 | 0.73 | 0.817 | 0.814 | 0.905 | 0.253 | 0.125 | 0.454 → 0.547 | 0.275 → 0.293 | 0.091 → 0.121 | 0.0 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| spider | 563 | 0.00 | - | - | 0.000 | - | 1.000 |
| waf-v2 | 3000 | 0.50 | 0.871 | 0.229 | 0.265 | 0.830 | 0.782 |

## phishing_url, in-domain — two-pass (b = 0.00)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| phishing_url | 1998 | 2.45 | 0.907 | 0.907 | 0.971 | 0.721 | 0.572 | 0.323 → 0.227 | 0.154 → 0.134 | 0.066 → 0.026 | 0.0 |

## phishing_url, in-domain — threat-only (b = -3.13)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| phishing_url | 1998 | 1.37 | 0.904 | 0.904 | 0.969 | 0.734 | 0.562 | 0.235 → 0.230 | 0.140 → 0.137 | 0.030 → 0.023 | 0.0 |

## phishing_url, in-domain — safe-only (b = 2.65)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| phishing_url | 1998 | 1.06 | 0.907 | 0.907 | 0.969 | 0.610 | 0.325 | 0.234 → 0.235 | 0.137 → 0.137 | 0.016 → 0.018 | 0.0 |

## phishing_url, held-out — two-pass (b = 0.00)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| phishing_url | 5000 | 2.45 | 0.707 | 0.692 | 0.789 | 0.143 | 0.047 | 1.124 → 0.615 | 0.512 → 0.413 | 0.243 → 0.139 | 0.0 |

**phishing_url by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| destroylist | 2000 | 1.00 | - | - | - | 0.570 | 0.363 |
| phishtrap | 3000 | 0.50 | 0.852 | 0.250 | 0.181 | 0.777 | 0.798 |

## phishing_url, held-out — threat-only (b = -3.13)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| phishing_url | 5000 | 1.37 | 0.718 | 0.700 | 0.785 | 0.125 | 0.029 | 0.680 → 0.588 | 0.423 → 0.392 | 0.163 → 0.118 | 0.0 |

**phishing_url by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| destroylist | 2000 | 1.00 | - | - | - | 0.604 | 0.377 |
| phishtrap | 3000 | 0.50 | 0.848 | 0.223 | 0.211 | 0.799 | 0.794 |

## phishing_url, held-out — safe-only (b = 2.65)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| phishing_url | 5000 | 1.06 | 0.709 | 0.694 | 0.786 | 0.147 | 0.010 | 0.625 → 0.611 | 0.416 → 0.410 | 0.150 → 0.141 | 0.0 |

**phishing_url by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| destroylist | 2000 | 1.00 | - | - | - | 0.567 | 0.362 |
| phishtrap | 3000 | 0.50 | 0.851 | 0.249 | 0.178 | 0.784 | 0.803 |

## phishing_url, val — two-pass (b = 0.00)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| phishing_url | 3000 | 2.45 | 0.880 | 0.880 | 0.943 | 0.569 | 0.102 | 0.539 → 0.318 | 0.213 → 0.189 | 0.094 → 0.026 | 0.0 |

## phishing_url, val — threat-only (b = -3.13)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| phishing_url | 3000 | 1.37 | 0.879 | 0.879 | 0.942 | 0.611 | 0.170 | 0.358 → 0.322 | 0.199 → 0.192 | 0.056 → 0.027 | 0.0 |

## phishing_url, val — safe-only (b = 2.65)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| phishing_url | 3000 | 1.06 | 0.871 | 0.871 | 0.938 | 0.489 | 0.079 | 0.351 → 0.345 | 0.205 → 0.204 | 0.042 → 0.036 | 0.0 |

## prompt_injection, in-domain — two-pass (b = 0.00)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| prompt_injection | 2773 | 2.07 | 0.957 | 0.957 | 0.994 | 0.884 | 0.534 | 0.193 → 0.120 | 0.077 → 0.068 | 0.035 → 0.015 | 0.0 |

**prompt_injection by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| awesome-prompts | 71 | 0.00 | - | - | 0.028 | - | 0.493 |
| dolly | 222 | 0.00 | - | - | 0.005 | - | 0.499 |
| mkqa-de | 13 | 0.00 | - | - | 0.000 | - | 1.000 |
| mkqa-es | 9 | 0.00 | - | - | 0.000 | - | 1.000 |
| mkqa-fr | 14 | 0.00 | - | - | 0.000 | - | 1.000 |
| mkqa-it | 18 | 0.00 | - | - | 0.000 | - | 1.000 |
| mkqa-pt | 19 | 0.00 | - | - | 0.105 | - | 0.472 |
| mkqa-ru | 68 | 0.00 | - | - | 0.029 | - | 0.493 |
| mosscap | 53 | 1.00 | - | - | - | 0.962 | 0.490 |
| neuralchemy | 900 | 0.59 | 0.994 | 0.861 | 0.054 | 0.966 | 0.956 |
| ru-injections | 54 | 1.00 | - | - | - | 0.852 | 0.460 |
| s-labs | 1000 | 0.47 | 0.995 | 0.909 | 0.002 | 0.896 | 0.949 |
| simsonsun | 128 | 1.00 | - | - | - | 0.938 | 0.484 |
| wildjailbreak | 126 | 0.93 | 0.915 | 0.573 | 0.556 | 0.983 | 0.752 |
| yanismiraoui | 78 | 1.00 | - | - | - | 1.000 | 1.000 |

## prompt_injection, in-domain — threat-only (b = -3.42)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| prompt_injection | 2773 | 1.27 | 0.959 | 0.959 | 0.994 | 0.882 | 0.534 | 0.132 → 0.119 | 0.070 → 0.067 | 0.026 → 0.016 | 0.0 |

**prompt_injection by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| awesome-prompts | 71 | 0.00 | - | - | 0.028 | - | 0.493 |
| dolly | 222 | 0.00 | - | - | 0.009 | - | 0.498 |
| mkqa-de | 13 | 0.00 | - | - | 0.000 | - | 1.000 |
| mkqa-es | 9 | 0.00 | - | - | 0.000 | - | 1.000 |
| mkqa-fr | 14 | 0.00 | - | - | 0.000 | - | 1.000 |
| mkqa-it | 18 | 0.00 | - | - | 0.000 | - | 1.000 |
| mkqa-pt | 19 | 0.00 | - | - | 0.105 | - | 0.472 |
| mkqa-ru | 68 | 0.00 | - | - | 0.044 | - | 0.489 |
| mosscap | 53 | 1.00 | - | - | - | 0.981 | 0.495 |
| neuralchemy | 900 | 0.59 | 0.994 | 0.858 | 0.056 | 0.979 | 0.963 |
| ru-injections | 54 | 1.00 | - | - | - | 0.852 | 0.460 |
| s-labs | 1000 | 0.47 | 0.994 | 0.909 | 0.004 | 0.898 | 0.949 |
| simsonsun | 128 | 1.00 | - | - | - | 0.953 | 0.488 |
| wildjailbreak | 126 | 0.93 | 0.921 | 0.735 | 0.556 | 0.974 | 0.733 |
| yanismiraoui | 78 | 1.00 | - | - | - | 0.987 | 0.497 |

## prompt_injection, in-domain — safe-only (b = 2.16)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| prompt_injection | 2773 | 0.74 | 0.956 | 0.956 | 0.993 | 0.859 | 0.611 | 0.122 → 0.117 | 0.064 → 0.065 | 0.028 → 0.013 | 0.0 |

**prompt_injection by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| awesome-prompts | 71 | 0.00 | - | - | 0.042 | - | 0.489 |
| dolly | 222 | 0.00 | - | - | 0.000 | - | 1.000 |
| mkqa-de | 13 | 0.00 | - | - | 0.077 | - | 0.480 |
| mkqa-es | 9 | 0.00 | - | - | 0.000 | - | 1.000 |
| mkqa-fr | 14 | 0.00 | - | - | 0.000 | - | 1.000 |
| mkqa-it | 18 | 0.00 | - | - | 0.056 | - | 0.486 |
| mkqa-pt | 19 | 0.00 | - | - | 0.053 | - | 0.486 |
| mkqa-ru | 68 | 0.00 | - | - | 0.029 | - | 0.493 |
| mosscap | 53 | 1.00 | - | - | - | 0.943 | 0.485 |
| neuralchemy | 900 | 0.59 | 0.994 | 0.873 | 0.054 | 0.970 | 0.959 |
| ru-injections | 54 | 1.00 | - | - | - | 0.852 | 0.460 |
| s-labs | 1000 | 0.47 | 0.994 | 0.900 | 0.013 | 0.902 | 0.946 |
| simsonsun | 128 | 1.00 | - | - | - | 0.953 | 0.488 |
| wildjailbreak | 126 | 0.93 | 0.863 | 0.162 | 0.667 | 0.974 | 0.681 |
| yanismiraoui | 78 | 1.00 | - | - | - | 1.000 | 1.000 |

## prompt_injection, held-out — two-pass (b = 0.00)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| prompt_injection | 1951 | 2.07 | 0.746 | 0.746 | 0.844 | 0.173 | 0.026 | 1.305 → 0.707 | 0.459 → 0.407 | 0.222 → 0.172 | 0.0 |

**prompt_injection by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| deepset | 662 | 0.40 | 0.843 | 0.186 | 0.163 | 0.669 | 0.757 |
| jackhhao | 1289 | 0.51 | 0.852 | 0.124 | 0.433 | 0.896 | 0.725 |

## prompt_injection, held-out — threat-only (b = -3.42)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| prompt_injection | 1951 | 1.27 | 0.730 | 0.729 | 0.836 | 0.129 | 0.009 | 1.022 → 0.839 | 0.468 → 0.448 | 0.219 → 0.199 | 0.0 |

**prompt_injection by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| deepset | 662 | 0.40 | 0.856 | 0.243 | 0.178 | 0.719 | 0.771 |
| jackhhao | 1289 | 0.51 | 0.831 | 0.032 | 0.506 | 0.909 | 0.689 |

## prompt_injection, held-out — safe-only (b = 2.16)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| prompt_injection | 1951 | 0.74 | 0.753 | 0.753 | 0.835 | 0.088 | 0.035 | 0.633 → 0.761 | 0.386 → 0.410 | 0.127 → 0.162 | 0.0 |

**prompt_injection by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| deepset | 662 | 0.40 | 0.811 | 0.103 | 0.180 | 0.654 | 0.739 |
| jackhhao | 1289 | 0.51 | 0.855 | 0.129 | 0.420 | 0.923 | 0.745 |

## prompt_injection, val — two-pass (b = 0.00)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| prompt_injection | 1500 | 2.07 | 0.726 | 0.726 | 0.787 | 0.076 | 0.017 | 1.480 → 0.797 | 0.504 → 0.452 | 0.240 → 0.190 | 0.0 |

## prompt_injection, val — threat-only (b = -3.42)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| prompt_injection | 1500 | 1.27 | 0.716 | 0.716 | 0.773 | 0.053 | 0.019 | 1.119 → 0.917 | 0.503 → 0.483 | 0.234 → 0.210 | 0.0 |

## prompt_injection, val — safe-only (b = 2.16)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| prompt_injection | 1500 | 0.74 | 0.728 | 0.727 | 0.797 | 0.091 | 0.008 | 0.640 → 0.754 | 0.404 → 0.428 | 0.117 → 0.158 | 0.0 |
