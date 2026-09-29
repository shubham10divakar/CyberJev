## One pass vs two — `runs/cyber-jev-v5-l6-s1`, max_length 256

| decision | test set | variant | T | b | calib NLL | AUROC | DR@1%FPR | NLL | ECE |
|---|---|---|---|---|---|---|---|---|---|
| http_attack | in-domain | two-pass | 1.20 | 0.00 | 0.083 | 0.995 | 0.951 | 0.087 | 0.010 |
| http_attack | in-domain | threat-only | 0.92 | -2.71 | 0.090 | 0.994 | 0.951 | 0.090 | 0.011 |
| http_attack | in-domain | safe-only | 0.40 | 3.09 | 0.089 | 0.992 | 0.950 | 0.097 | 0.009 |
| http_attack | held-out | two-pass | 1.20 | 0.00 | 0.083 | 0.973 | 0.819 | 0.541 | 0.112 |
| http_attack | held-out | threat-only | 0.92 | -2.71 | 0.090 | 0.970 | 0.809 | 0.448 | 0.104 |
| http_attack | held-out | safe-only | 0.40 | 3.09 | 0.089 | 0.978 | 0.818 | 0.544 | 0.105 |
| http_attack | val | two-pass | 1.20 | 0.00 | 0.083 | 0.905 | 0.348 | 0.633 | 0.129 |
| http_attack | val | threat-only | 0.92 | -2.71 | 0.090 | 0.906 | 0.351 | 0.529 | 0.093 |
| http_attack | val | safe-only | 0.40 | 3.09 | 0.089 | 0.895 | 0.287 | 0.823 | 0.186 |
| phishing_url | in-domain | two-pass | 1.46 | 0.00 | 0.257 | 0.967 | 0.685 | 0.238 | 0.017 |
| phishing_url | in-domain | threat-only | 1.02 | -3.68 | 0.264 | 0.964 | 0.716 | 0.243 | 0.020 |
| phishing_url | in-domain | safe-only | 0.51 | 3.88 | 0.276 | 0.959 | 0.451 | 0.261 | 0.030 |
| phishing_url | held-out | two-pass | 1.46 | 0.00 | 0.257 | 0.811 | 0.121 | 0.546 | 0.108 |
| phishing_url | held-out | threat-only | 1.02 | -3.68 | 0.264 | 0.795 | 0.101 | 0.556 | 0.097 |
| phishing_url | held-out | safe-only | 0.51 | 3.88 | 0.276 | 0.828 | 0.037 | 0.581 | 0.128 |
| phishing_url | val | two-pass | 1.46 | 0.00 | 0.257 | 0.946 | 0.582 | 0.325 | 0.033 |
| phishing_url | val | threat-only | 1.02 | -3.68 | 0.264 | 0.940 | 0.597 | 0.329 | 0.028 |
| phishing_url | val | safe-only | 0.51 | 3.88 | 0.276 | 0.941 | 0.351 | 0.334 | 0.035 |
| prompt_injection | in-domain | two-pass | 1.31 | 0.00 | 0.072 | 0.994 | 0.893 | 0.108 | 0.014 |
| prompt_injection | in-domain | threat-only | 1.04 | -3.25 | 0.076 | 0.993 | 0.894 | 0.110 | 0.012 |
| prompt_injection | in-domain | safe-only | 0.30 | 3.00 | 0.091 | 0.991 | 0.865 | 0.113 | 0.006 |
| prompt_injection | held-out | two-pass | 1.31 | 0.00 | 0.072 | 0.825 | 0.085 | 0.807 | 0.182 |
| prompt_injection | held-out | threat-only | 1.04 | -3.25 | 0.076 | 0.841 | 0.136 | 0.760 | 0.182 |
| prompt_injection | held-out | safe-only | 0.30 | 3.00 | 0.091 | 0.768 | 0.030 | 1.108 | 0.206 |
| prompt_injection | val | two-pass | 1.31 | 0.00 | 0.072 | 0.783 | 0.101 | 0.795 | 0.183 |
| prompt_injection | val | threat-only | 1.04 | -3.25 | 0.076 | 0.773 | 0.113 | 0.831 | 0.194 |
| prompt_injection | val | safe-only | 0.30 | 3.00 | 0.091 | 0.786 | 0.041 | 0.793 | 0.171 |

One-pass variant picked: http_attack → threat-only (by val AUROC), phishing_url → safe-only (by val AUROC), prompt_injection → safe-only (by val AUROC)

## http_attack, in-domain — two-pass (b = 0.00)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 4700 | 1.20 | 0.970 | 0.970 | 0.995 | 0.951 | 0.930 | 0.088 → 0.087 | 0.049 → 0.049 | 0.013 → 0.010 | 0.0 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| ai-waf | 1200 | 0.28 | 0.993 | 0.955 | 0.005 | 0.946 | 0.977 |
| csic2010 | 1500 | 0.60 | 0.972 | 0.868 | 0.028 | 0.889 | 0.920 |
| gretel-sql | 500 | 0.00 | - | - | 0.000 | - | 1.000 |
| web-attacks | 1500 | 0.80 | 1.000 | 0.998 | 0.003 | 0.998 | 0.997 |

## http_attack, in-domain — threat-only (b = -2.71)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 4700 | 0.92 | 0.969 | 0.969 | 0.994 | 0.951 | 0.926 | 0.091 → 0.090 | 0.050 → 0.050 | 0.012 → 0.011 | 0.0 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| ai-waf | 1200 | 0.28 | 0.992 | 0.949 | 0.002 | 0.937 | 0.976 |
| csic2010 | 1500 | 0.60 | 0.969 | 0.874 | 0.028 | 0.886 | 0.918 |
| gretel-sql | 500 | 0.00 | - | - | 0.000 | - | 1.000 |
| web-attacks | 1500 | 0.80 | 0.999 | 0.998 | 0.003 | 0.998 | 0.997 |

## http_attack, in-domain — safe-only (b = 3.09)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 4700 | 0.40 | 0.969 | 0.969 | 0.992 | 0.950 | 0.918 | 0.176 → 0.097 | 0.077 → 0.053 | 0.101 → 0.009 | 0.0 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| ai-waf | 1200 | 0.28 | 0.991 | 0.958 | 0.013 | 0.961 | 0.975 |
| csic2010 | 1500 | 0.60 | 0.953 | 0.868 | 0.025 | 0.887 | 0.920 |
| gretel-sql | 500 | 0.00 | - | - | 0.000 | - | 1.000 |
| web-attacks | 1500 | 0.80 | 1.000 | 0.998 | 0.007 | 0.998 | 0.996 |

## http_attack, held-out — two-pass (b = 0.00)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 10320 | 1.20 | 0.858 | 0.855 | 0.973 | 0.819 | 0.757 | 0.635 → 0.541 | 0.255 → 0.250 | 0.119 → 0.112 | 0.0 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| dvwa-juiceshop | 4320 | 0.73 | 0.952 | 0.714 | 0.357 | 0.971 | 0.836 |
| sqli-queries | 6000 | 0.36 | 0.994 | 0.962 | 0.246 | 0.990 | 0.838 |

## http_attack, held-out — threat-only (b = -2.71)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 10320 | 0.92 | 0.862 | 0.859 | 0.970 | 0.809 | 0.745 | 0.421 → 0.448 | 0.232 → 0.236 | 0.100 → 0.104 | 0.0 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| dvwa-juiceshop | 4320 | 0.73 | 0.946 | 0.681 | 0.318 | 0.953 | 0.837 |
| sqli-queries | 6000 | 0.36 | 0.993 | 0.962 | 0.231 | 0.989 | 0.846 |

## http_attack, held-out — safe-only (b = 3.09)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 10320 | 0.40 | 0.856 | 0.852 | 0.978 | 0.818 | 0.746 | 0.368 → 0.544 | 0.226 → 0.252 | 0.065 → 0.105 | 0.0 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| dvwa-juiceshop | 4320 | 0.73 | 0.963 | 0.767 | 0.419 | 0.986 | 0.820 |
| sqli-queries | 6000 | 0.36 | 0.994 | 0.944 | 0.248 | 0.995 | 0.838 |

## http_attack, val — two-pass (b = 0.00)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 3563 | 1.20 | 0.796 | 0.795 | 0.905 | 0.348 | 0.141 | 0.728 → 0.633 | 0.325 → 0.315 | 0.142 → 0.129 | 0.0 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| spider | 563 | 0.00 | - | - | 0.000 | - | 1.000 |
| waf-v2 | 3000 | 0.50 | 0.870 | 0.318 | 0.355 | 0.871 | 0.755 |

## http_attack, val — threat-only (b = -2.71)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 3563 | 0.92 | 0.844 | 0.841 | 0.906 | 0.351 | 0.160 | 0.501 → 0.529 | 0.263 → 0.265 | 0.085 → 0.093 | 0.0 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| spider | 563 | 0.00 | - | - | 0.000 | - | 1.000 |
| waf-v2 | 3000 | 0.50 | 0.871 | 0.341 | 0.204 | 0.833 | 0.815 |

## http_attack, val — safe-only (b = 3.09)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 3563 | 0.40 | 0.751 | 0.751 | 0.895 | 0.287 | 0.098 | 0.526 → 0.823 | 0.348 → 0.420 | 0.064 → 0.186 | 0.0 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| spider | 563 | 0.00 | - | - | 0.000 | - | 1.000 |
| waf-v2 | 3000 | 0.50 | 0.856 | 0.255 | 0.508 | 0.917 | 0.691 |

## phishing_url, in-domain — two-pass (b = 0.00)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| phishing_url | 1998 | 1.46 | 0.909 | 0.909 | 0.967 | 0.685 | 0.457 | 0.252 → 0.238 | 0.147 → 0.142 | 0.040 → 0.017 | 0.0 |

## phishing_url, in-domain — threat-only (b = -3.68)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| phishing_url | 1998 | 1.02 | 0.903 | 0.903 | 0.964 | 0.716 | 0.485 | 0.243 → 0.243 | 0.146 → 0.146 | 0.019 → 0.020 | 0.0 |

## phishing_url, in-domain — safe-only (b = 3.88)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| phishing_url | 1998 | 0.51 | 0.897 | 0.897 | 0.959 | 0.451 | 0.205 | 0.331 → 0.261 | 0.182 → 0.153 | 0.121 → 0.030 | 0.0 |

## phishing_url, held-out — two-pass (b = 0.00)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| phishing_url | 5000 | 1.46 | 0.747 | 0.726 | 0.811 | 0.121 | 0.026 | 0.659 → 0.546 | 0.393 → 0.359 | 0.159 → 0.108 | 0.0 |

**phishing_url by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| destroylist | 2000 | 1.00 | - | - | - | 0.680 | 0.405 |
| phishtrap | 3000 | 0.50 | 0.850 | 0.215 | 0.215 | 0.800 | 0.792 |

## phishing_url, held-out — threat-only (b = -3.68)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| phishing_url | 5000 | 1.02 | 0.740 | 0.718 | 0.795 | 0.101 | 0.033 | 0.559 → 0.556 | 0.366 → 0.364 | 0.100 → 0.097 | 0.0 |

**phishing_url by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| destroylist | 2000 | 1.00 | - | - | - | 0.680 | 0.405 |
| phishtrap | 3000 | 0.50 | 0.833 | 0.182 | 0.231 | 0.791 | 0.780 |

## phishing_url, held-out — safe-only (b = 3.88)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| phishing_url | 5000 | 0.51 | 0.747 | 0.729 | 0.828 | 0.037 | 0.013 | 0.522 → 0.581 | 0.346 → 0.381 | 0.061 → 0.128 | 0.0 |

**phishing_url by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| destroylist | 2000 | 1.00 | - | - | - | 0.655 | 0.396 |
| phishtrap | 3000 | 0.50 | 0.870 | 0.059 | 0.188 | 0.804 | 0.808 |

## phishing_url, val — two-pass (b = 0.00)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| phishing_url | 3000 | 1.46 | 0.879 | 0.879 | 0.946 | 0.582 | 0.058 | 0.378 → 0.325 | 0.204 → 0.195 | 0.070 → 0.033 | 0.0 |

## phishing_url, val — threat-only (b = -3.68)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| phishing_url | 3000 | 1.02 | 0.870 | 0.870 | 0.940 | 0.597 | 0.121 | 0.330 → 0.329 | 0.200 → 0.199 | 0.031 → 0.028 | 0.0 |

## phishing_url, val — safe-only (b = 3.88)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| phishing_url | 3000 | 0.51 | 0.870 | 0.870 | 0.941 | 0.351 | 0.038 | 0.367 → 0.334 | 0.212 → 0.197 | 0.093 → 0.035 | 0.0 |

## prompt_injection, in-domain — two-pass (b = 0.00)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| prompt_injection | 2500 | 1.31 | 0.967 | 0.967 | 0.994 | 0.893 | 0.554 | 0.122 → 0.108 | 0.059 → 0.057 | 0.023 → 0.014 | 0.0 |

**prompt_injection by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| awesome-prompts | 71 | 0.00 | - | - | 0.028 | - | 0.493 |
| dolly | 222 | 0.00 | - | - | 0.000 | - | 1.000 |
| mosscap | 53 | 1.00 | - | - | - | 0.962 | 0.490 |
| neuralchemy | 900 | 0.59 | 0.991 | 0.894 | 0.046 | 0.975 | 0.966 |
| s-labs | 1000 | 0.47 | 0.996 | 0.936 | 0.006 | 0.924 | 0.961 |
| simsonsun | 128 | 1.00 | - | - | - | 0.984 | 0.496 |
| wildjailbreak | 126 | 0.93 | 0.917 | 0.735 | 0.556 | 0.974 | 0.733 |

## prompt_injection, in-domain — threat-only (b = -3.25)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| prompt_injection | 2500 | 1.04 | 0.965 | 0.965 | 0.993 | 0.894 | 0.619 | 0.112 → 0.110 | 0.058 → 0.058 | 0.014 → 0.012 | 0.0 |

**prompt_injection by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| awesome-prompts | 71 | 0.00 | - | - | 0.028 | - | 0.493 |
| dolly | 222 | 0.00 | - | - | 0.000 | - | 1.000 |
| mosscap | 53 | 1.00 | - | - | - | 0.981 | 0.495 |
| neuralchemy | 900 | 0.59 | 0.991 | 0.909 | 0.048 | 0.975 | 0.964 |
| s-labs | 1000 | 0.47 | 0.995 | 0.934 | 0.004 | 0.913 | 0.957 |
| simsonsun | 128 | 1.00 | - | - | - | 0.984 | 0.496 |
| wildjailbreak | 126 | 0.93 | 0.937 | 0.855 | 0.667 | 0.974 | 0.681 |

## prompt_injection, in-domain — safe-only (b = 3.00)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| prompt_injection | 2500 | 0.30 | 0.963 | 0.963 | 0.991 | 0.865 | 0.427 | 0.240 → 0.113 | 0.112 → 0.059 | 0.152 → 0.006 | 0.0 |

**prompt_injection by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| awesome-prompts | 71 | 0.00 | - | - | 0.042 | - | 0.489 |
| dolly | 222 | 0.00 | - | - | 0.005 | - | 0.499 |
| mosscap | 53 | 1.00 | - | - | - | 0.906 | 0.475 |
| neuralchemy | 900 | 0.59 | 0.990 | 0.884 | 0.046 | 0.972 | 0.963 |
| s-labs | 1000 | 0.47 | 0.996 | 0.919 | 0.025 | 0.951 | 0.964 |
| simsonsun | 128 | 1.00 | - | - | - | 0.953 | 0.488 |
| wildjailbreak | 126 | 0.93 | 0.816 | 0.043 | 0.556 | 0.966 | 0.716 |

## prompt_injection, held-out — two-pass (b = 0.00)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| prompt_injection | 1951 | 1.31 | 0.737 | 0.734 | 0.825 | 0.085 | 0.028 | 1.000 → 0.807 | 0.454 → 0.433 | 0.205 → 0.182 | 0.0 |

**prompt_injection by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| deepset | 662 | 0.40 | 0.769 | 0.137 | 0.398 | 0.829 | 0.692 |
| jackhhao | 1289 | 0.51 | 0.866 | 0.060 | 0.422 | 0.939 | 0.752 |

## prompt_injection, held-out — threat-only (b = -3.25)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| prompt_injection | 1951 | 1.04 | 0.734 | 0.731 | 0.841 | 0.136 | 0.032 | 0.783 → 0.760 | 0.429 → 0.426 | 0.186 → 0.182 | 0.0 |

**prompt_injection by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| deepset | 662 | 0.40 | 0.789 | 0.217 | 0.398 | 0.825 | 0.690 |
| jackhhao | 1289 | 0.51 | 0.869 | 0.045 | 0.429 | 0.940 | 0.748 |

## prompt_injection, held-out — safe-only (b = 3.00)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| prompt_injection | 1951 | 0.30 | 0.713 | 0.708 | 0.768 | 0.030 | 0.004 | 0.620 → 1.108 | 0.417 → 0.491 | 0.069 → 0.206 | 0.0 |

**prompt_injection by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| deepset | 662 | 0.40 | 0.707 | 0.015 | 0.449 | 0.821 | 0.659 |
| jackhhao | 1289 | 0.51 | 0.827 | 0.029 | 0.458 | 0.937 | 0.730 |

## prompt_injection, val — two-pass (b = 0.00)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| prompt_injection | 1500 | 1.31 | 0.701 | 0.699 | 0.783 | 0.101 | 0.005 | 0.964 → 0.795 | 0.483 → 0.458 | 0.210 → 0.183 | 0.0 |

## prompt_injection, val — threat-only (b = -3.25)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| prompt_injection | 1500 | 1.04 | 0.696 | 0.693 | 0.773 | 0.113 | 0.009 | 0.855 → 0.831 | 0.480 → 0.476 | 0.199 → 0.194 | 0.0 |

## prompt_injection, val — safe-only (b = 3.00)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| prompt_injection | 1500 | 0.30 | 0.693 | 0.687 | 0.786 | 0.041 | 0.011 | 0.577 → 0.793 | 0.392 → 0.452 | 0.035 → 0.171 | 0.0 |
