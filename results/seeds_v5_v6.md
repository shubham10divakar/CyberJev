## Seeds: mean ± std of calibrated AUROC (two-pass)

| decision | set | v5_l6 (n=3) | v6_l6 (n=3) |
|---|---|---|---|
| http_attack | in-domain | 0.995 ± 0.000 | 0.996 ± 0.001 |
| http_attack | held-out | 0.962 ± 0.009 | 0.969 ± 0.015 |
| http_attack | val | 0.915 ± 0.022 | 0.915 ± 0.007 |
| phishing_url | in-domain | 0.967 ± 0.001 | 0.967 ± 0.004 |
| phishing_url | held-out | 0.808 ± 0.012 | 0.782 ± 0.007 |
| phishing_url | val | 0.944 ± 0.005 | 0.939 ± 0.005 |
| prompt_injection | in-domain | 0.994 ± 0.000 | 0.993 ± 0.002 |
| prompt_injection | held-out | 0.812 ± 0.026 | 0.839 ± 0.013 |
| prompt_injection | val | 0.799 ± 0.015 | 0.786 ± 0.010 |

### By source (held-out and val): AUROC, and FPR@0.5 on safe examples

| decision | source | v5_l6 AUROC | v5_l6 FPR@0.5 | v6_l6 AUROC | v6_l6 FPR@0.5 |
|---|---|---|---|---|---|
| http_attack | dvwa-juiceshop | 0.916 ± 0.047 | 0.417 ± 0.152 | 0.910 ± 0.059 | 0.450 ± 0.201 |
| http_attack | sqli-queries | 0.993 ± 0.001 | 0.241 ± 0.006 | 0.994 ± 0.003 | 0.218 ± 0.030 |
| http_attack | spider | - | 0.002 ± 0.003 | - | 0.001 ± 0.002 |
| http_attack | waf-v2 | 0.884 ± 0.030 | 0.284 ± 0.159 | 0.883 ± 0.009 | 0.331 ± 0.137 |
| phishing_url | destroylist | - | - | - | - |
| phishing_url | phishtrap | 0.857 ± 0.015 | 0.244 ± 0.025 | 0.839 ± 0.011 | 0.183 ± 0.025 |
| prompt_injection | deepset | 0.755 ± 0.012 | 0.388 ± 0.027 | 0.823 ± 0.032 | 0.189 ± 0.077 |
| prompt_injection | jackhhao | 0.849 ± 0.033 | 0.440 ± 0.054 | 0.856 ± 0.010 | 0.403 ± 0.028 |
