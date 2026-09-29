## One pass vs two — `runs/cyber-jev-v5-l6`, max_length 256

| decision | test set | variant | T | b | calib NLL | AUROC | DR@1%FPR | NLL | ECE |
|---|---|---|---|---|---|---|---|---|---|
| http_attack | in-domain | two-pass | 1.83 | 0.00 | 0.075 | 0.995 | 0.960 | 0.081 | 0.007 |
| http_attack | in-domain | threat-only | 1.01 | -2.82 | 0.075 | 0.995 | 0.961 | 0.086 | 0.009 |
| http_attack | in-domain | safe-only | 0.52 | 1.47 | 0.076 | 0.993 | 0.958 | 0.088 | 0.007 |
| http_attack | held-out | two-pass | 1.83 | 0.00 | 0.075 | 0.955 | 0.652 | 0.435 | 0.100 |
| http_attack | held-out | threat-only | 1.01 | -2.82 | 0.075 | 0.939 | 0.574 | 0.623 | 0.125 |
| http_attack | held-out | safe-only | 0.52 | 1.47 | 0.076 | 0.965 | 0.693 | 0.591 | 0.096 |
| http_attack | val | two-pass | 1.83 | 0.00 | 0.075 | 0.940 | 0.348 | 0.436 | 0.101 |
| http_attack | val | threat-only | 1.01 | -2.82 | 0.075 | 0.940 | 0.385 | 0.469 | 0.108 |
| http_attack | val | safe-only | 0.52 | 1.47 | 0.076 | 0.929 | 0.268 | 0.485 | 0.066 |
| phishing_url | in-domain | two-pass | 1.82 | 0.00 | 0.260 | 0.966 | 0.670 | 0.248 | 0.025 |
| phishing_url | in-domain | threat-only | 1.19 | -2.33 | 0.272 | 0.963 | 0.659 | 0.255 | 0.025 |
| phishing_url | in-domain | safe-only | 0.68 | 2.86 | 0.260 | 0.964 | 0.679 | 0.249 | 0.032 |
| phishing_url | held-out | two-pass | 1.82 | 0.00 | 0.260 | 0.817 | 0.201 | 0.525 | 0.093 |
| phishing_url | held-out | threat-only | 1.19 | -2.33 | 0.272 | 0.811 | 0.133 | 0.545 | 0.088 |
| phishing_url | held-out | safe-only | 0.68 | 2.86 | 0.260 | 0.816 | 0.133 | 0.580 | 0.124 |
| phishing_url | val | two-pass | 1.82 | 0.00 | 0.260 | 0.947 | 0.610 | 0.340 | 0.033 |
| phishing_url | val | threat-only | 1.19 | -2.33 | 0.272 | 0.944 | 0.567 | 0.334 | 0.030 |
| phishing_url | val | safe-only | 0.68 | 2.86 | 0.260 | 0.943 | 0.414 | 0.325 | 0.029 |
| prompt_injection | in-domain | two-pass | 1.60 | 0.00 | 0.069 | 0.994 | 0.886 | 0.122 | 0.017 |
| prompt_injection | in-domain | threat-only | 1.12 | -2.86 | 0.067 | 0.994 | 0.894 | 0.111 | 0.017 |
| prompt_injection | in-domain | safe-only | 0.47 | 1.92 | 0.077 | 0.992 | 0.856 | 0.118 | 0.016 |
| prompt_injection | held-out | two-pass | 1.60 | 0.00 | 0.069 | 0.829 | 0.165 | 0.787 | 0.192 |
| prompt_injection | held-out | threat-only | 1.12 | -2.86 | 0.067 | 0.813 | 0.128 | 0.908 | 0.210 |
| prompt_injection | held-out | safe-only | 0.47 | 1.92 | 0.077 | 0.837 | 0.074 | 0.833 | 0.181 |
| prompt_injection | val | two-pass | 1.60 | 0.00 | 0.069 | 0.813 | 0.088 | 0.746 | 0.178 |
| prompt_injection | val | threat-only | 1.12 | -2.86 | 0.067 | 0.802 | 0.063 | 0.824 | 0.196 |
| prompt_injection | val | safe-only | 0.47 | 1.92 | 0.077 | 0.826 | 0.124 | 0.705 | 0.146 |

One-pass variant picked: http_attack → threat-only (by val AUROC), phishing_url → threat-only (by val AUROC), prompt_injection → safe-only (by val AUROC)

## http_attack, in-domain — two-pass (b = 0.00)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 4700 | 1.83 | 0.975 | 0.975 | 0.995 | 0.960 | 0.873 | 0.113 → 0.081 | 0.047 → 0.043 | 0.021 → 0.007 | 0.0 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| ai-waf | 1200 | 0.28 | 0.993 | 0.949 | 0.002 | 0.931 | 0.974 |
| csic2010 | 1500 | 0.60 | 0.976 | 0.870 | 0.025 | 0.919 | 0.940 |
| gretel-sql | 500 | 0.00 | - | - | 0.000 | - | 1.000 |
| web-attacks | 1500 | 0.80 | 1.000 | 0.998 | 0.003 | 0.998 | 0.997 |

## http_attack, in-domain — threat-only (b = -2.82)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 4700 | 1.01 | 0.974 | 0.974 | 0.995 | 0.961 | 0.855 | 0.086 → 0.086 | 0.044 → 0.044 | 0.009 → 0.009 | 0.0 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| ai-waf | 1200 | 0.28 | 0.992 | 0.946 | 0.006 | 0.934 | 0.972 |
| csic2010 | 1500 | 0.60 | 0.975 | 0.821 | 0.034 | 0.924 | 0.939 |
| gretel-sql | 500 | 0.00 | - | - | 0.000 | - | 1.000 |
| web-attacks | 1500 | 0.80 | 1.000 | 0.998 | 0.010 | 0.998 | 0.995 |

## http_attack, in-domain — safe-only (b = 1.47)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 4700 | 0.52 | 0.975 | 0.975 | 0.993 | 0.958 | 0.898 | 0.116 → 0.088 | 0.053 → 0.044 | 0.050 → 0.007 | 0.0 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| ai-waf | 1200 | 0.28 | 0.992 | 0.952 | 0.010 | 0.952 | 0.974 |
| csic2010 | 1500 | 0.60 | 0.961 | 0.886 | 0.027 | 0.919 | 0.939 |
| gretel-sql | 500 | 0.00 | - | - | 0.002 | - | 0.499 |
| web-attacks | 1500 | 0.80 | 1.000 | 1.000 | 0.013 | 1.000 | 0.996 |

## http_attack, held-out — two-pass (b = 0.00)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 10320 | 1.83 | 0.849 | 0.847 | 0.955 | 0.652 | 0.515 | 0.718 → 0.435 | 0.272 → 0.245 | 0.128 → 0.100 | 0.0 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| dvwa-juiceshop | 4320 | 0.73 | 0.933 | 0.582 | 0.305 | 0.908 | 0.807 |
| sqli-queries | 6000 | 0.36 | 0.991 | 0.924 | 0.235 | 0.992 | 0.845 |

## http_attack, held-out — threat-only (b = -2.82)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 10320 | 1.01 | 0.834 | 0.830 | 0.939 | 0.574 | 0.424 | 0.631 → 0.623 | 0.287 → 0.287 | 0.126 → 0.125 | 0.0 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| dvwa-juiceshop | 4320 | 0.73 | 0.915 | 0.421 | 0.342 | 0.921 | 0.801 |
| sqli-queries | 6000 | 0.36 | 0.987 | 0.896 | 0.273 | 0.989 | 0.820 |

## http_attack, held-out — safe-only (b = 1.47)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 10320 | 0.52 | 0.844 | 0.840 | 0.965 | 0.693 | 0.436 | 0.412 → 0.591 | 0.243 → 0.257 | 0.063 → 0.096 | 0.0 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| dvwa-juiceshop | 4320 | 0.73 | 0.949 | 0.714 | 0.386 | 0.956 | 0.810 |
| sqli-queries | 6000 | 0.36 | 0.993 | 0.908 | 0.266 | 0.996 | 0.828 |

## http_attack, val — two-pass (b = 0.00)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 3563 | 1.83 | 0.851 | 0.843 | 0.940 | 0.348 | 0.163 | 0.720 → 0.436 | 0.273 → 0.247 | 0.130 → 0.101 | 0.0 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| spider | 563 | 0.00 | - | - | 0.000 | - | 1.000 |
| waf-v2 | 3000 | 0.50 | 0.919 | 0.331 | 0.102 | 0.747 | 0.822 |

## http_attack, val — threat-only (b = -2.82)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 3563 | 1.01 | 0.853 | 0.846 | 0.940 | 0.385 | 0.192 | 0.474 → 0.469 | 0.248 → 0.248 | 0.109 → 0.108 | 0.0 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| spider | 563 | 0.00 | - | - | 0.000 | - | 1.000 |
| waf-v2 | 3000 | 0.50 | 0.918 | 0.358 | 0.113 | 0.763 | 0.824 |

## http_attack, val — safe-only (b = 1.47)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| http_attack | 3563 | 0.52 | 0.862 | 0.857 | 0.929 | 0.268 | 0.033 | 0.394 → 0.485 | 0.223 → 0.222 | 0.073 → 0.066 | 0.0 |

**http_attack by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| spider | 563 | 0.00 | - | - | 0.018 | - | 0.496 |
| waf-v2 | 3000 | 0.50 | 0.908 | 0.231 | 0.131 | 0.810 | 0.839 |

## phishing_url, in-domain — two-pass (b = 0.00)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| phishing_url | 1998 | 1.82 | 0.895 | 0.895 | 0.966 | 0.670 | 0.358 | 0.295 → 0.248 | 0.165 → 0.153 | 0.058 → 0.025 | 0.0 |

## phishing_url, in-domain — threat-only (b = -2.33)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| phishing_url | 1998 | 1.19 | 0.892 | 0.892 | 0.963 | 0.659 | 0.360 | 0.257 → 0.255 | 0.158 → 0.156 | 0.029 → 0.025 | 0.0 |

## phishing_url, in-domain — safe-only (b = 2.86)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| phishing_url | 1998 | 0.68 | 0.894 | 0.894 | 0.964 | 0.679 | 0.128 | 0.275 → 0.249 | 0.155 → 0.151 | 0.064 → 0.032 | 0.0 |

## phishing_url, held-out — two-pass (b = 0.00)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| phishing_url | 5000 | 1.82 | 0.749 | 0.723 | 0.817 | 0.201 | 0.065 | 0.717 → 0.525 | 0.392 → 0.345 | 0.163 → 0.093 | 0.0 |

**phishing_url by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| destroylist | 2000 | 1.00 | - | - | - | 0.678 | 0.404 |
| phishtrap | 3000 | 0.50 | 0.874 | 0.311 | 0.265 | 0.857 | 0.796 |

## phishing_url, held-out — threat-only (b = -2.33)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| phishing_url | 5000 | 1.19 | 0.754 | 0.726 | 0.811 | 0.133 | 0.043 | 0.582 → 0.545 | 0.367 → 0.355 | 0.115 → 0.088 | 0.0 |

**phishing_url by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| destroylist | 2000 | 1.00 | - | - | - | 0.699 | 0.411 |
| phishtrap | 3000 | 0.50 | 0.865 | 0.211 | 0.271 | 0.851 | 0.789 |

## phishing_url, held-out — safe-only (b = 2.86)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| phishing_url | 5000 | 0.68 | 0.732 | 0.714 | 0.816 | 0.133 | 0.031 | 0.529 → 0.580 | 0.358 → 0.387 | 0.073 → 0.124 | 0.0 |

**phishing_url by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| destroylist | 2000 | 1.00 | - | - | - | 0.616 | 0.381 |
| phishtrap | 3000 | 0.50 | 0.875 | 0.189 | 0.203 | 0.822 | 0.810 |

## phishing_url, val — two-pass (b = 0.00)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| phishing_url | 3000 | 1.82 | 0.863 | 0.863 | 0.947 | 0.610 | 0.303 | 0.456 → 0.340 | 0.227 → 0.208 | 0.085 → 0.033 | 0.0 |

## phishing_url, val — threat-only (b = -2.33)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| phishing_url | 3000 | 1.19 | 0.859 | 0.859 | 0.944 | 0.567 | 0.259 | 0.349 → 0.334 | 0.210 → 0.205 | 0.050 → 0.030 | 0.0 |

## phishing_url, val — safe-only (b = 2.86)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| phishing_url | 3000 | 0.68 | 0.879 | 0.879 | 0.943 | 0.414 | 0.144 | 0.329 → 0.325 | 0.193 → 0.193 | 0.038 → 0.029 | 0.0 |

## prompt_injection, in-domain — two-pass (b = 0.00)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| prompt_injection | 2500 | 1.60 | 0.960 | 0.960 | 0.994 | 0.886 | 0.527 | 0.164 → 0.122 | 0.069 → 0.065 | 0.031 → 0.017 | 0.0 |

**prompt_injection by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| awesome-prompts | 71 | 0.00 | - | - | 0.028 | - | 0.493 |
| dolly | 222 | 0.00 | - | - | 0.000 | - | 1.000 |
| mosscap | 53 | 1.00 | - | - | - | 0.962 | 0.490 |
| neuralchemy | 900 | 0.59 | 0.992 | 0.911 | 0.040 | 0.964 | 0.961 |
| s-labs | 1000 | 0.47 | 0.996 | 0.934 | 0.008 | 0.909 | 0.953 |
| simsonsun | 128 | 1.00 | - | - | - | 0.961 | 0.490 |
| wildjailbreak | 126 | 0.93 | 0.906 | 0.402 | 0.556 | 0.966 | 0.716 |

## prompt_injection, in-domain — threat-only (b = -2.86)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| prompt_injection | 2500 | 1.12 | 0.964 | 0.964 | 0.994 | 0.894 | 0.631 | 0.116 → 0.111 | 0.061 → 0.059 | 0.021 → 0.017 | 0.0 |

**prompt_injection by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| awesome-prompts | 71 | 0.00 | - | - | 0.028 | - | 0.493 |
| dolly | 222 | 0.00 | - | - | 0.000 | - | 1.000 |
| mosscap | 53 | 1.00 | - | - | - | 0.981 | 0.495 |
| neuralchemy | 900 | 0.59 | 0.993 | 0.918 | 0.043 | 0.972 | 0.965 |
| s-labs | 1000 | 0.47 | 0.996 | 0.932 | 0.008 | 0.921 | 0.959 |
| simsonsun | 128 | 1.00 | - | - | - | 0.961 | 0.490 |
| wildjailbreak | 126 | 0.93 | 0.917 | 0.521 | 0.667 | 0.974 | 0.681 |

## prompt_injection, in-domain — safe-only (b = 1.92)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| prompt_injection | 2500 | 0.47 | 0.959 | 0.959 | 0.992 | 0.856 | 0.340 | 0.158 → 0.118 | 0.072 → 0.064 | 0.068 → 0.016 | 0.0 |

**prompt_injection by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| awesome-prompts | 71 | 0.00 | - | - | 0.028 | - | 0.493 |
| dolly | 222 | 0.00 | - | - | 0.005 | - | 0.499 |
| mosscap | 53 | 1.00 | - | - | - | 0.943 | 0.485 |
| neuralchemy | 900 | 0.59 | 0.990 | 0.875 | 0.046 | 0.966 | 0.960 |
| s-labs | 1000 | 0.47 | 0.995 | 0.941 | 0.008 | 0.911 | 0.954 |
| simsonsun | 128 | 1.00 | - | - | - | 0.945 | 0.486 |
| wildjailbreak | 126 | 0.93 | 0.849 | 0.137 | 0.444 | 0.957 | 0.744 |

## prompt_injection, held-out — two-pass (b = 0.00)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| prompt_injection | 1951 | 1.60 | 0.726 | 0.725 | 0.829 | 0.165 | 0.023 | 1.157 → 0.787 | 0.486 → 0.446 | 0.229 → 0.192 | 0.0 |

**prompt_injection by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| deepset | 662 | 0.40 | 0.747 | 0.118 | 0.358 | 0.677 | 0.651 |
| jackhhao | 1289 | 0.51 | 0.870 | 0.180 | 0.398 | 0.920 | 0.756 |

## prompt_injection, held-out — threat-only (b = -2.86)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| prompt_injection | 1951 | 1.12 | 0.715 | 0.712 | 0.813 | 0.128 | 0.061 | 0.998 → 0.908 | 0.492 → 0.482 | 0.221 → 0.210 | 0.0 |

**prompt_injection by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| deepset | 662 | 0.40 | 0.734 | 0.080 | 0.391 | 0.745 | 0.661 |
| jackhhao | 1289 | 0.51 | 0.857 | 0.152 | 0.442 | 0.922 | 0.732 |

## prompt_injection, held-out — safe-only (b = 1.92)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| prompt_injection | 1951 | 0.47 | 0.729 | 0.727 | 0.837 | 0.074 | 0.009 | 0.574 → 0.833 | 0.383 → 0.445 | 0.084 → 0.181 | 0.0 |

**prompt_injection by source** (calibrated; at the default 0.5 threshold, FPR = safe examples flagged, DR = threats caught)

| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |
|---|---|---|---|---|---|---|---|
| deepset | 662 | 0.40 | 0.756 | 0.099 | 0.348 | 0.700 | 0.666 |
| jackhhao | 1289 | 0.51 | 0.873 | 0.061 | 0.428 | 0.942 | 0.749 |

## prompt_injection, val — two-pass (b = 0.00)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| prompt_injection | 1500 | 1.60 | 0.734 | 0.734 | 0.813 | 0.088 | 0.020 | 1.086 → 0.746 | 0.464 → 0.424 | 0.217 → 0.178 | 0.0 |

## prompt_injection, val — threat-only (b = -2.86)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| prompt_injection | 1500 | 1.12 | 0.729 | 0.728 | 0.802 | 0.063 | 0.019 | 0.902 → 0.824 | 0.461 → 0.450 | 0.206 → 0.196 | 0.0 |

## prompt_injection, val — safe-only (b = 1.92)

| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR | NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| prompt_injection | 1500 | 0.47 | 0.734 | 0.731 | 0.826 | 0.124 | 0.023 | 0.542 → 0.705 | 0.360 → 0.403 | 0.043 → 0.146 | 0.0 |
