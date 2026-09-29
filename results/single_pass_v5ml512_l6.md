## One pass vs two — `runs/cyber-jev-v5ml512-l6`, max_length 512

| decision | test set | variant | T | b | calib NLL | AUROC | DR@1%FPR | NLL | ECE |
|---|---|---|---|---|---|---|---|---|---|
| http_attack | in-domain | two-pass | 1.71 | 0.00 | 0.081 | 0.995 | 0.953 | 0.086 | 0.011 |
| http_attack | in-domain | threat-only | 0.98 | -2.93 | 0.078 | 0.994 | 0.951 | 0.088 | 0.005 |
| http_attack | in-domain | safe-only | 0.51 | 1.97 | 0.098 | 0.993 | 0.952 | 0.100 | 0.016 |
| http_attack | held-out | two-pass | 1.71 | 0.00 | 0.081 | 0.953 | 0.632 | 0.545 | 0.117 |
| http_attack | held-out | threat-only | 0.98 | -2.93 | 0.078 | 0.932 | 0.418 | 0.752 | 0.133 |
| http_attack | held-out | safe-only | 0.51 | 1.97 | 0.098 | 0.971 | 0.808 | 0.644 | 0.117 |
| http_attack | val | two-pass | 1.71 | 0.00 | 0.081 | 0.906 | 0.201 | 0.540 | 0.106 |
| http_attack | val | threat-only | 0.98 | -2.93 | 0.078 | 0.904 | 0.203 | 0.659 | 0.120 |
| http_attack | val | safe-only | 0.51 | 1.97 | 0.098 | 0.905 | 0.219 | 0.678 | 0.149 |
| phishing_url | in-domain | two-pass | 1.91 | 0.00 | 0.263 | 0.969 | 0.722 | 0.238 | 0.013 |
| phishing_url | in-domain | threat-only | 1.24 | -2.28 | 0.264 | 0.967 | 0.743 | 0.232 | 0.017 |
| phishing_url | in-domain | safe-only | 0.78 | 3.13 | 0.274 | 0.962 | 0.476 | 0.253 | 0.028 |
| phishing_url | held-out | two-pass | 1.91 | 0.00 | 0.263 | 0.814 | 0.138 | 0.507 | 0.075 |
| phishing_url | held-out | threat-only | 1.24 | -2.28 | 0.264 | 0.808 | 0.115 | 0.527 | 0.071 |
| phishing_url | held-out | safe-only | 0.78 | 3.13 | 0.274 | 0.818 | 0.135 | 0.571 | 0.108 |
| phishing_url | val | two-pass | 1.91 | 0.00 | 0.263 | 0.947 | 0.597 | 0.331 | 0.034 |
| phishing_url | val | threat-only | 1.24 | -2.28 | 0.264 | 0.943 | 0.597 | 0.314 | 0.021 |
| phishing_url | val | safe-only | 0.78 | 3.13 | 0.274 | 0.941 | 0.388 | 0.324 | 0.027 |
| prompt_injection | in-domain | two-pass | 1.68 | 0.00 | 0.067 | 0.995 | 0.917 | 0.101 | 0.015 |
| prompt_injection | in-domain | threat-only | 1.28 | -2.06 | 0.074 | 0.994 | 0.894 | 0.113 | 0.016 |
| prompt_injection | in-domain | safe-only | 0.43 | 2.03 | 0.080 | 0.993 | 0.893 | 0.106 | 0.008 |
| prompt_injection | held-out | two-pass | 1.68 | 0.00 | 0.067 | 0.799 | 0.083 | 0.959 | 0.222 |
| prompt_injection | held-out | threat-only | 1.28 | -2.06 | 0.074 | 0.816 | 0.160 | 0.907 | 0.225 |
| prompt_injection | held-out | safe-only | 0.43 | 2.03 | 0.080 | 0.756 | 0.046 | 1.127 | 0.217 |
| prompt_injection | val | two-pass | 1.68 | 0.00 | 0.067 | 0.808 | 0.081 | 0.766 | 0.176 |
| prompt_injection | val | threat-only | 1.28 | -2.06 | 0.074 | 0.805 | 0.097 | 0.793 | 0.187 |
| prompt_injection | val | safe-only | 0.43 | 2.03 | 0.080 | 0.803 | 0.064 | 0.717 | 0.146 |

One-pass variant picked: http_attack → safe-only (by val AUROC), phishing_url → threat-only (by val AUROC), prompt_injection → threat-only (by val AUROC)

## http_attack, in-domain — two-pass (b = 0.00)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 4700 | 1.71 | 0.970 | 0.970 | 0.995 | 0.953 | 0.903 | 0.111 → 0.086 | 0.054 → 0.048 | 0.024 → 0.011 | 0.0 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| ai-waf | 1200 | 0.28 | 0.995 | 0.964 | 0.006 | 0.949 | 0.977 |
| csic2010 | 1500 | 0.60 | 0.969 | 0.853 | 0.020 | 0.886 | 0.922 |
| gretel-sql | 500 | 0.00 | - | - | 0.000 | - | 1.000 |
| web-attacks | 1500 | 0.80 | 1.000 | 0.998 | 0.003 | 0.997 | 0.996 |

## http_attack, in-domain — threat-only (b = -2.93)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 4700 | 0.98 | 0.970 | 0.970 | 0.994 | 0.951 | 0.883 | 0.088 → 0.088 | 0.049 → 0.049 | 0.005 → 0.005 | 0.0 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| ai-waf | 1200 | 0.28 | 0.994 | 0.958 | 0.006 | 0.943 | 0.975 |
| csic2010 | 1500 | 0.60 | 0.968 | 0.853 | 0.030 | 0.895 | 0.923 |
| gretel-sql | 500 | 0.00 | - | - | 0.000 | - | 1.000 |
| web-attacks | 1500 | 0.80 | 0.999 | 0.998 | 0.003 | 0.997 | 0.995 |

## http_attack, in-domain — safe-only (b = 1.97)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 4700 | 0.51 | 0.970 | 0.970 | 0.993 | 0.952 | 0.916 | 0.145 → 0.100 | 0.065 → 0.053 | 0.068 → 0.016 | 0.0 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| ai-waf | 1200 | 0.28 | 0.995 | 0.964 | 0.013 | 0.964 | 0.976 |
| csic2010 | 1500 | 0.60 | 0.972 | 0.855 | 0.017 | 0.886 | 0.923 |
| gretel-sql | 500 | 0.00 | - | - | 0.002 | - | 0.499 |
| web-attacks | 1500 | 0.80 | 1.000 | 1.000 | 0.020 | 1.000 | 0.994 |

## http_attack, held-out — two-pass (b = 0.00)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 10320 | 1.71 | 0.846 | 0.843 | 0.953 | 0.632 | 0.533 | 0.881 → 0.545 | 0.286 → 0.268 | 0.137 → 0.117 | 0.0 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| dvwa-juiceshop | 4320 | 0.73 | 0.934 | 0.569 | 0.355 | 0.943 | 0.813 |
| sqli-queries | 6000 | 0.36 | 0.981 | 0.808 | 0.253 | 0.987 | 0.832 |

## http_attack, held-out — threat-only (b = -2.93)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 10320 | 0.98 | 0.840 | 0.836 | 0.932 | 0.418 | 0.300 | 0.740 → 0.752 | 0.292 → 0.292 | 0.133 → 0.133 | 0.0 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| dvwa-juiceshop | 4320 | 0.73 | 0.917 | 0.422 | 0.370 | 0.939 | 0.803 |
| sqli-queries | 6000 | 0.36 | 0.963 | 0.619 | 0.261 | 0.983 | 0.825 |

## http_attack, held-out — safe-only (b = 1.97)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 10320 | 0.51 | 0.831 | 0.825 | 0.971 | 0.808 | 0.723 | 0.438 → 0.644 | 0.272 → 0.296 | 0.072 → 0.117 | 0.0 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| dvwa-juiceshop | 4320 | 0.73 | 0.954 | 0.735 | 0.384 | 0.972 | 0.824 |
| sqli-queries | 6000 | 0.36 | 0.995 | 0.963 | 0.313 | 0.994 | 0.797 |

## http_attack, val — two-pass (b = 0.00)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 3563 | 1.71 | 0.835 | 0.833 | 0.906 | 0.201 | 0.074 | 0.826 → 0.540 | 0.298 → 0.281 | 0.130 → 0.106 | 0.0 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| spider | 563 | 0.00 | - | - | 0.002 | - | 0.500 |
| waf-v2 | 3000 | 0.50 | 0.872 | 0.181 | 0.269 | 0.878 | 0.803 |

## http_attack, val — threat-only (b = -2.93)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 3563 | 0.98 | 0.820 | 0.819 | 0.904 | 0.203 | 0.081 | 0.649 → 0.659 | 0.301 → 0.302 | 0.119 → 0.120 | 0.0 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| spider | 563 | 0.00 | - | - | 0.002 | - | 0.500 |
| waf-v2 | 3000 | 0.50 | 0.869 | 0.173 | 0.313 | 0.886 | 0.785 |

## http_attack, val — safe-only (b = 1.97)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 3563 | 0.51 | 0.770 | 0.770 | 0.905 | 0.219 | 0.047 | 0.495 → 0.678 | 0.310 → 0.347 | 0.072 → 0.149 | 0.0 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| spider | 563 | 0.00 | - | - | 0.018 | - | 0.496 |
| waf-v2 | 3000 | 0.50 | 0.871 | 0.189 | 0.441 | 0.901 | 0.722 |

## phishing_url, in-domain — two-pass (b = 0.00)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| phishing_url | 1998 | 1.91 | 0.901 | 0.901 | 0.969 | 0.722 | 0.520 | 0.278 → 0.238 | 0.154 → 0.145 | 0.049 → 0.013 | 0.0 |

## phishing_url, in-domain — threat-only (b = -2.28)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| phishing_url | 1998 | 1.24 | 0.903 | 0.903 | 0.967 | 0.743 | 0.546 | 0.230 → 0.232 | 0.142 → 0.141 | 0.015 → 0.017 | 0.0 |

## phishing_url, in-domain — safe-only (b = 3.13)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| phishing_url | 1998 | 0.78 | 0.897 | 0.897 | 0.962 | 0.476 | 0.141 | 0.268 → 0.253 | 0.153 → 0.150 | 0.046 → 0.028 | 0.0 |

## phishing_url, held-out — two-pass (b = 0.00)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| phishing_url | 5000 | 1.91 | 0.753 | 0.725 | 0.814 | 0.138 | 0.065 | 0.688 → 0.507 | 0.376 → 0.332 | 0.152 → 0.075 | 0.0 |

**phishing_url by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| destroylist | 2000 | 1.00 | - | - | - | 0.705 | 0.413 |
| phishtrap | 3000 | 0.50 | 0.865 | 0.236 | 0.277 | 0.847 | 0.784 |

## phishing_url, held-out — threat-only (b = -2.28)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| phishing_url | 5000 | 1.24 | 0.746 | 0.722 | 0.808 | 0.115 | 0.047 | 0.563 → 0.527 | 0.360 → 0.348 | 0.101 → 0.071 | 0.0 |

**phishing_url by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| destroylist | 2000 | 1.00 | - | - | - | 0.680 | 0.405 |
| phishtrap | 3000 | 0.50 | 0.857 | 0.199 | 0.251 | 0.831 | 0.790 |

## phishing_url, held-out — safe-only (b = 3.13)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| phishing_url | 5000 | 0.78 | 0.733 | 0.716 | 0.818 | 0.135 | 0.035 | 0.540 → 0.571 | 0.363 → 0.380 | 0.067 → 0.108 | 0.0 |

**phishing_url by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| destroylist | 2000 | 1.00 | - | - | - | 0.624 | 0.384 |
| phishtrap | 3000 | 0.50 | 0.869 | 0.222 | 0.191 | 0.803 | 0.806 |

## phishing_url, val — two-pass (b = 0.00)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| phishing_url | 3000 | 1.91 | 0.868 | 0.868 | 0.947 | 0.597 | 0.385 | 0.450 → 0.331 | 0.219 → 0.203 | 0.080 → 0.034 | 0.0 |

## phishing_url, val — threat-only (b = -2.28)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| phishing_url | 3000 | 1.24 | 0.872 | 0.872 | 0.943 | 0.597 | 0.435 | 0.330 → 0.314 | 0.195 → 0.192 | 0.039 → 0.021 | 0.0 |

## phishing_url, val — safe-only (b = 3.13)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| phishing_url | 3000 | 0.78 | 0.872 | 0.872 | 0.941 | 0.388 | 0.183 | 0.324 → 0.324 | 0.192 → 0.193 | 0.025 → 0.027 | 0.0 |

## prompt_injection, in-domain — two-pass (b = 0.00)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| prompt_injection | 2500 | 1.68 | 0.964 | 0.964 | 0.995 | 0.917 | 0.656 | 0.137 → 0.101 | 0.062 → 0.056 | 0.028 → 0.015 | 0.0 |

**prompt_injection by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| awesome-prompts | 71 | 0.00 | - | - | 0.014 | - | 0.496 |
| dolly | 222 | 0.00 | - | - | 0.005 | - | 0.499 |
| mosscap | 53 | 1.00 | - | - | - | 0.943 | 0.485 |
| neuralchemy | 900 | 0.59 | 0.994 | 0.896 | 0.070 | 0.979 | 0.957 |
| s-labs | 1000 | 0.47 | 0.997 | 0.941 | 0.008 | 0.936 | 0.966 |
| simsonsun | 128 | 1.00 | - | - | - | 0.953 | 0.488 |
| wildjailbreak | 126 | 0.93 | 0.906 | 0.427 | 0.556 | 0.966 | 0.716 |

## prompt_injection, in-domain — threat-only (b = -2.06)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| prompt_injection | 2500 | 1.28 | 0.960 | 0.960 | 0.994 | 0.894 | 0.651 | 0.126 → 0.113 | 0.066 → 0.062 | 0.026 → 0.016 | 0.0 |

**prompt_injection by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| awesome-prompts | 71 | 0.00 | - | - | 0.014 | - | 0.496 |
| dolly | 222 | 0.00 | - | - | 0.005 | - | 0.499 |
| mosscap | 53 | 1.00 | - | - | - | 0.925 | 0.480 |
| neuralchemy | 900 | 0.59 | 0.993 | 0.865 | 0.070 | 0.975 | 0.955 |
| s-labs | 1000 | 0.47 | 0.996 | 0.936 | 0.006 | 0.917 | 0.958 |
| simsonsun | 128 | 1.00 | - | - | - | 0.961 | 0.490 |
| wildjailbreak | 126 | 0.93 | 0.918 | 0.538 | 0.556 | 0.966 | 0.716 |

## prompt_injection, in-domain — safe-only (b = 2.03)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| prompt_injection | 2500 | 0.43 | 0.961 | 0.961 | 0.993 | 0.893 | 0.617 | 0.163 → 0.106 | 0.073 → 0.057 | 0.081 → 0.008 | 0.0 |

**prompt_injection by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| awesome-prompts | 71 | 0.00 | - | - | 0.028 | - | 0.493 |
| dolly | 222 | 0.00 | - | - | 0.000 | - | 1.000 |
| mosscap | 53 | 1.00 | - | - | - | 0.868 | 0.465 |
| neuralchemy | 900 | 0.59 | 0.993 | 0.865 | 0.046 | 0.964 | 0.959 |
| s-labs | 1000 | 0.47 | 0.997 | 0.951 | 0.032 | 0.975 | 0.971 |
| simsonsun | 128 | 1.00 | - | - | - | 0.906 | 0.475 |
| wildjailbreak | 126 | 0.93 | 0.879 | 0.299 | 0.444 | 0.932 | 0.701 |

## prompt_injection, held-out — two-pass (b = 0.00)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| prompt_injection | 1951 | 1.68 | 0.704 | 0.700 | 0.799 | 0.083 | 0.026 | 1.512 → 0.959 | 0.537 → 0.499 | 0.257 → 0.222 | 0.0 |

**prompt_injection by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| deepset | 662 | 0.40 | 0.765 | 0.133 | 0.391 | 0.772 | 0.673 |
| jackhhao | 1289 | 0.51 | 0.820 | 0.057 | 0.486 | 0.922 | 0.707 |

## prompt_injection, held-out — threat-only (b = -2.06)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| prompt_injection | 1951 | 1.28 | 0.709 | 0.705 | 0.816 | 0.160 | 0.019 | 1.112 → 0.907 | 0.520 → 0.497 | 0.243 → 0.225 | 0.0 |

**prompt_injection by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| deepset | 662 | 0.40 | 0.782 | 0.183 | 0.378 | 0.787 | 0.686 |
| jackhhao | 1289 | 0.51 | 0.830 | 0.149 | 0.483 | 0.920 | 0.708 |

## prompt_injection, held-out — safe-only (b = 2.03)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| prompt_injection | 1951 | 0.43 | 0.705 | 0.702 | 0.756 | 0.046 | 0.027 | 0.678 → 1.127 | 0.440 → 0.505 | 0.108 → 0.217 | 0.0 |

**prompt_injection by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| deepset | 662 | 0.40 | 0.721 | 0.065 | 0.424 | 0.738 | 0.639 |
| jackhhao | 1289 | 0.51 | 0.791 | 0.038 | 0.440 | 0.914 | 0.729 |

## prompt_injection, val — two-pass (b = 0.00)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| prompt_injection | 1500 | 1.68 | 0.735 | 0.735 | 0.808 | 0.081 | 0.009 | 1.168 → 0.766 | 0.468 → 0.429 | 0.218 → 0.176 | 0.0 |

## prompt_injection, val — threat-only (b = -2.06)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| prompt_injection | 1500 | 1.28 | 0.730 | 0.730 | 0.805 | 0.097 | 0.011 | 0.962 → 0.793 | 0.460 → 0.440 | 0.209 → 0.187 | 0.0 |

## prompt_injection, val — safe-only (b = 2.03)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| prompt_injection | 1500 | 0.43 | 0.731 | 0.731 | 0.803 | 0.064 | 0.008 | 0.547 → 0.717 | 0.363 → 0.405 | 0.031 → 0.146 | 0.0 |
