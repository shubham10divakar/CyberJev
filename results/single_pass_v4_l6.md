## One pass vs two — `runs/cyber-jev-v4-l6`, max_length 256

| decision | test set | variant | T | b | calib NLL | AUROC | DR@1%FPR | NLL | ECE |
|---|---|---|---|---|---|---|---|---|---|
| http_attack | in-domain | two-pass | 1.69 | 0.00 | 0.094 | 0.994 | 0.943 | 0.095 | 0.008 |
| http_attack | in-domain | threat-only | 1.06 | -2.08 | 0.103 | 0.993 | 0.938 | 0.102 | 0.007 |
| http_attack | in-domain | safe-only | 0.72 | 2.53 | 0.094 | 0.994 | 0.942 | 0.094 | 0.007 |
| http_attack | held-out | two-pass | 1.69 | 0.00 | 0.094 | 0.956 | 0.619 | 0.429 | 0.090 |
| http_attack | held-out | threat-only | 1.06 | -2.08 | 0.103 | 0.951 | 0.560 | 0.398 | 0.092 |
| http_attack | held-out | safe-only | 0.72 | 2.53 | 0.094 | 0.956 | 0.617 | 0.430 | 0.084 |
| http_attack | val | two-pass | 1.69 | 0.00 | 0.094 | 0.911 | 0.227 | 0.490 | 0.096 |
| http_attack | val | threat-only | 1.06 | -2.08 | 0.103 | 0.907 | 0.199 | 0.497 | 0.102 |
| http_attack | val | safe-only | 0.72 | 2.53 | 0.094 | 0.912 | 0.233 | 0.463 | 0.087 |
| phishing_url | in-domain | two-pass | 2.02 | 0.00 | 0.283 | 0.966 | 0.727 | 0.248 | 0.029 |
| phishing_url | in-domain | threat-only | 0.99 | -3.05 | 0.282 | 0.963 | 0.714 | 0.247 | 0.025 |
| phishing_url | in-domain | safe-only | 0.79 | 1.93 | 0.269 | 0.965 | 0.701 | 0.245 | 0.017 |
| phishing_url | held-out | two-pass | 2.02 | 0.00 | 0.283 | 0.798 | 0.184 | 0.605 | 0.133 |
| phishing_url | held-out | threat-only | 0.99 | -3.05 | 0.282 | 0.789 | 0.160 | 0.550 | 0.084 |
| phishing_url | held-out | safe-only | 0.79 | 1.93 | 0.269 | 0.802 | 0.188 | 0.583 | 0.131 |
| phishing_url | val | two-pass | 2.02 | 0.00 | 0.283 | 0.940 | 0.557 | 0.306 | 0.013 |
| phishing_url | val | threat-only | 0.99 | -3.05 | 0.282 | 0.937 | 0.555 | 0.330 | 0.032 |
| phishing_url | val | safe-only | 0.79 | 1.93 | 0.269 | 0.939 | 0.569 | 0.337 | 0.026 |
| prompt_injection | in-domain | two-pass | 1.64 | 0.00 | 0.074 | 0.995 | 0.898 | 0.097 | 0.010 |
| prompt_injection | in-domain | threat-only | 1.05 | -2.30 | 0.087 | 0.991 | 0.833 | 0.108 | 0.008 |
| prompt_injection | in-domain | safe-only | 0.59 | 1.95 | 0.077 | 0.995 | 0.909 | 0.102 | 0.014 |
| prompt_injection | held-out | two-pass | 1.64 | 0.00 | 0.074 | 0.766 | 0.044 | 0.963 | 0.236 |
| prompt_injection | held-out | threat-only | 1.05 | -2.30 | 0.087 | 0.861 | 0.171 | 1.050 | 0.281 |
| prompt_injection | held-out | safe-only | 0.59 | 1.95 | 0.077 | 0.672 | 0.037 | 1.133 | 0.221 |
| prompt_injection | val | two-pass | 1.64 | 0.00 | 0.074 | 0.676 | 0.019 | 1.193 | 0.354 |
| prompt_injection | val | threat-only | 1.05 | -2.30 | 0.087 | 0.749 | 0.032 | 1.586 | 0.425 |
| prompt_injection | val | safe-only | 0.59 | 1.95 | 0.077 | 0.578 | 0.007 | 1.043 | 0.238 |

One-pass variant picked: http_attack → safe-only (by val AUROC), phishing_url → safe-only (by val AUROC), prompt_injection → threat-only (by val AUROC)

## http_attack, in-domain — two-pass (b = 0.00)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 4700 | 1.69 | 0.968 | 0.968 | 0.994 | 0.943 | 0.799 | 0.114 → 0.095 | 0.053 → 0.051 | 0.018 → 0.008 | 0.0 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| ai-waf | 1200 | 0.28 | 0.993 | 0.952 | 0.003 | 0.913 | 0.966 |
| csic2010 | 1500 | 0.60 | 0.975 | 0.866 | 0.085 | 0.935 | 0.924 |
| gretel-sql | 500 | 0.00 | - | - | 0.000 | - | 1.000 |
| web-attacks | 1500 | 0.80 | 1.000 | 0.996 | 0.010 | 0.994 | 0.990 |

## http_attack, in-domain — threat-only (b = -2.08)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 4700 | 1.06 | 0.967 | 0.967 | 0.993 | 0.938 | 0.760 | 0.102 → 0.102 | 0.055 → 0.055 | 0.010 → 0.007 | 0.0 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| ai-waf | 1200 | 0.28 | 0.992 | 0.949 | 0.002 | 0.913 | 0.967 |
| csic2010 | 1500 | 0.60 | 0.972 | 0.852 | 0.085 | 0.932 | 0.922 |
| gretel-sql | 500 | 0.00 | - | - | 0.000 | - | 1.000 |
| web-attacks | 1500 | 0.80 | 0.999 | 0.995 | 0.003 | 0.990 | 0.987 |

## http_attack, in-domain — safe-only (b = 2.53)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 4700 | 0.72 | 0.970 | 0.970 | 0.994 | 0.942 | 0.834 | 0.106 → 0.094 | 0.051 → 0.049 | 0.028 → 0.007 | 0.0 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| ai-waf | 1200 | 0.28 | 0.993 | 0.952 | 0.006 | 0.928 | 0.969 |
| csic2010 | 1500 | 0.60 | 0.975 | 0.842 | 0.062 | 0.927 | 0.929 |
| gretel-sql | 500 | 0.00 | - | - | 0.000 | - | 1.000 |
| web-attacks | 1500 | 0.80 | 1.000 | 0.989 | 0.020 | 0.996 | 0.989 |

## http_attack, held-out — two-pass (b = 0.00)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 10320 | 1.69 | 0.875 | 0.873 | 0.956 | 0.619 | 0.418 | 0.676 → 0.429 | 0.233 → 0.218 | 0.110 → 0.090 | 0.0 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| dvwa-juiceshop | 4320 | 0.73 | 0.961 | 0.678 | 0.140 | 0.932 | 0.890 |
| sqli-queries | 6000 | 0.36 | 0.988 | 0.883 | 0.231 | 0.985 | 0.845 |

## http_attack, held-out — threat-only (b = -2.08)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 10320 | 1.06 | 0.869 | 0.868 | 0.951 | 0.560 | 0.278 | 0.414 → 0.398 | 0.220 → 0.217 | 0.096 → 0.092 | 0.0 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| dvwa-juiceshop | 4320 | 0.73 | 0.942 | 0.532 | 0.140 | 0.895 | 0.861 |
| sqli-queries | 6000 | 0.36 | 0.980 | 0.758 | 0.214 | 0.980 | 0.854 |

## http_attack, held-out — safe-only (b = 2.53)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 10320 | 0.72 | 0.872 | 0.870 | 0.956 | 0.617 | 0.472 | 0.358 → 0.430 | 0.207 → 0.218 | 0.052 → 0.084 | 0.0 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| dvwa-juiceshop | 4320 | 0.73 | 0.977 | 0.778 | 0.139 | 0.947 | 0.904 |
| sqli-queries | 6000 | 0.36 | 0.992 | 0.940 | 0.258 | 0.996 | 0.832 |

## http_attack, val — two-pass (b = 0.00)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 3563 | 1.69 | 0.848 | 0.843 | 0.911 | 0.227 | 0.081 | 0.749 → 0.490 | 0.271 → 0.254 | 0.125 → 0.096 | 0.0 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| spider | 563 | 0.00 | - | - | 0.000 | - | 1.000 |
| waf-v2 | 3000 | 0.50 | 0.878 | 0.205 | 0.157 | 0.796 | 0.820 |

## http_attack, val — threat-only (b = -2.08)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 3563 | 1.06 | 0.845 | 0.840 | 0.907 | 0.199 | 0.079 | 0.516 → 0.497 | 0.265 → 0.263 | 0.108 → 0.102 | 0.0 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| spider | 563 | 0.00 | - | - | 0.000 | - | 1.000 |
| waf-v2 | 3000 | 0.50 | 0.872 | 0.184 | 0.146 | 0.779 | 0.816 |

## http_attack, val — safe-only (b = 2.53)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 3563 | 0.72 | 0.851 | 0.846 | 0.912 | 0.233 | 0.033 | 0.399 → 0.463 | 0.237 → 0.249 | 0.049 → 0.087 | 0.0 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| spider | 563 | 0.00 | - | - | 0.000 | - | 1.000 |
| waf-v2 | 3000 | 0.50 | 0.880 | 0.188 | 0.158 | 0.804 | 0.823 |

## phishing_url, in-domain — two-pass (b = 0.00)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| phishing_url | 1998 | 2.02 | 0.897 | 0.896 | 0.966 | 0.727 | 0.539 | 0.298 → 0.248 | 0.166 → 0.149 | 0.067 → 0.029 | 0.0 |

## phishing_url, in-domain — threat-only (b = -3.05)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| phishing_url | 1998 | 0.99 | 0.905 | 0.905 | 0.963 | 0.714 | 0.503 | 0.247 → 0.247 | 0.149 → 0.149 | 0.026 → 0.025 | 0.0 |

## phishing_url, in-domain — safe-only (b = 1.93)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| phishing_url | 1998 | 0.79 | 0.904 | 0.904 | 0.965 | 0.701 | 0.516 | 0.257 → 0.245 | 0.149 → 0.144 | 0.046 → 0.017 | 0.0 |

## phishing_url, held-out — two-pass (b = 0.00)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| phishing_url | 5000 | 2.02 | 0.699 | 0.687 | 0.798 | 0.184 | 0.060 | 0.910 → 0.605 | 0.500 → 0.414 | 0.228 → 0.133 | 0.0 |

**phishing_url by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| destroylist | 2000 | 1.00 | - | - | - | 0.574 | 0.365 |
| phishtrap | 3000 | 0.50 | 0.844 | 0.306 | 0.162 | 0.727 | 0.782 |

## phishing_url, held-out — threat-only (b = -3.05)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| phishing_url | 5000 | 0.99 | 0.729 | 0.708 | 0.789 | 0.160 | 0.058 | 0.549 → 0.550 | 0.365 → 0.366 | 0.082 → 0.084 | 0.0 |

**phishing_url by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| destroylist | 2000 | 1.00 | - | - | - | 0.656 | 0.396 |
| phishtrap | 3000 | 0.50 | 0.834 | 0.277 | 0.227 | 0.781 | 0.777 |

## phishing_url, held-out — safe-only (b = 1.93)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| phishing_url | 5000 | 0.79 | 0.719 | 0.703 | 0.802 | 0.188 | 0.072 | 0.539 → 0.583 | 0.365 → 0.384 | 0.098 → 0.131 | 0.0 |

**phishing_url by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| destroylist | 2000 | 1.00 | - | - | - | 0.614 | 0.381 |
| phishtrap | 3000 | 0.50 | 0.848 | 0.288 | 0.183 | 0.759 | 0.788 |

## phishing_url, val — two-pass (b = 0.00)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| phishing_url | 3000 | 2.02 | 0.877 | 0.877 | 0.940 | 0.557 | 0.467 | 0.402 → 0.306 | 0.201 → 0.184 | 0.079 → 0.013 | 0.0 |

## phishing_url, val — threat-only (b = -3.05)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| phishing_url | 3000 | 0.99 | 0.872 | 0.872 | 0.937 | 0.555 | 0.386 | 0.330 → 0.330 | 0.201 → 0.201 | 0.032 → 0.032 | 0.0 |

## phishing_url, val — safe-only (b = 1.93)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| phishing_url | 3000 | 0.79 | 0.879 | 0.879 | 0.939 | 0.569 | 0.267 | 0.332 → 0.337 | 0.195 → 0.193 | 0.039 → 0.026 | 0.0 |

## prompt_injection, in-domain — two-pass (b = 0.00)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| prompt_injection | 1900 | 1.64 | 0.966 | 0.966 | 0.995 | 0.898 | 0.602 | 0.125 → 0.097 | 0.058 → 0.054 | 0.023 → 0.010 | 0.0 |

**prompt_injection by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| neuralchemy | 900 | 0.59 | 0.995 | 0.915 | 0.059 | 0.975 | 0.960 |
| s-labs | 1000 | 0.47 | 0.996 | 0.947 | 0.011 | 0.949 | 0.970 |

## prompt_injection, in-domain — threat-only (b = -2.30)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| prompt_injection | 1900 | 1.05 | 0.967 | 0.967 | 0.991 | 0.833 | 0.213 | 0.108 → 0.108 | 0.056 → 0.056 | 0.011 → 0.008 | 0.0 |

**prompt_injection by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| neuralchemy | 900 | 0.59 | 0.988 | 0.620 | 0.067 | 0.983 | 0.961 |
| s-labs | 1000 | 0.47 | 0.996 | 0.949 | 0.011 | 0.951 | 0.971 |

## prompt_injection, in-domain — safe-only (b = 1.95)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| prompt_injection | 1900 | 0.59 | 0.959 | 0.959 | 0.995 | 0.909 | 0.713 | 0.123 → 0.102 | 0.059 → 0.057 | 0.045 → 0.014 | 0.0 |

**prompt_injection by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| neuralchemy | 900 | 0.59 | 0.995 | 0.907 | 0.046 | 0.954 | 0.953 |
| s-labs | 1000 | 0.47 | 0.996 | 0.934 | 0.021 | 0.947 | 0.964 |

## prompt_injection, held-out — two-pass (b = 0.00)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| prompt_injection | 1951 | 1.64 | 0.674 | 0.655 | 0.766 | 0.044 | 0.025 | 1.461 → 0.963 | 0.582 → 0.534 | 0.279 → 0.236 | 0.0 |

**prompt_injection by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| deepset | 662 | 0.40 | 0.835 | 0.095 | 0.363 | 0.909 | 0.745 |
| jackhhao | 1289 | 0.51 | 0.727 | 0.023 | 0.721 | 0.988 | 0.583 |

## prompt_injection, held-out — threat-only (b = -2.30)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| prompt_injection | 1951 | 1.05 | 0.652 | 0.627 | 0.861 | 0.171 | 0.037 | 1.092 → 1.050 | 0.589 → 0.583 | 0.285 → 0.281 | 0.0 |

**prompt_injection by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| deepset | 662 | 0.40 | 0.860 | 0.190 | 0.373 | 0.928 | 0.746 |
| jackhhao | 1289 | 0.51 | 0.879 | 0.163 | 0.793 | 0.992 | 0.529 |

## prompt_injection, held-out — safe-only (b = 1.95)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| prompt_injection | 1951 | 0.59 | 0.651 | 0.647 | 0.672 | 0.037 | 0.013 | 0.823 → 1.133 | 0.519 → 0.564 | 0.145 → 0.221 | 0.0 |

**prompt_injection by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| deepset | 662 | 0.40 | 0.808 | 0.046 | 0.356 | 0.848 | 0.724 |
| jackhhao | 1289 | 0.51 | 0.585 | 0.015 | 0.574 | 0.797 | 0.599 |

## prompt_injection, val — two-pass (b = 0.00)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| prompt_injection | 1500 | 1.64 | 0.538 | 0.427 | 0.676 | 0.019 | 0.003 | 1.813 → 1.193 | 0.812 → 0.724 | 0.408 → 0.354 | 0.0 |

## prompt_injection, val — threat-only (b = -2.30)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| prompt_injection | 1500 | 1.05 | 0.526 | 0.397 | 0.749 | 0.032 | 0.012 | 1.655 → 1.586 | 0.850 → 0.841 | 0.428 → 0.425 | 0.0 |

## prompt_injection, val — safe-only (b = 1.95)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| prompt_injection | 1500 | 0.59 | 0.549 | 0.532 | 0.578 | 0.007 | 0.003 | 0.821 → 1.043 | 0.562 → 0.628 | 0.167 → 0.238 | 0.0 |
