## Seeds: mean ± std of calibrated AUROC (two-pass)

| decision | set | v5_l6 (n=3) | plain_v5_http (n=3) | plain_v5_pi (n=3) | plain_v5_url (n=3) |
|---|---|---|---|---|---|
| http_attack | in-domain | 0.995 ± 0.000 | 0.997 ± 0.000 | - | - |
| http_attack | held-out | 0.962 ± 0.009 | 0.964 ± 0.021 | - | - |
| http_attack | val | 0.915 ± 0.022 | 0.905 ± 0.017 | - | - |
| phishing_url | in-domain | 0.967 ± 0.001 | - | - | 0.970 ± 0.001 |
| phishing_url | held-out | 0.808 ± 0.012 | - | - | 0.823 ± 0.005 |
| phishing_url | val | 0.944 ± 0.005 | - | - | 0.943 ± 0.002 |
| prompt_injection | in-domain | 0.994 ± 0.000 | - | 0.994 ± 0.001 | - |
| prompt_injection | held-out | 0.812 ± 0.026 | - | 0.760 ± 0.018 | - |
| prompt_injection | val | 0.799 ± 0.015 | - | 0.748 ± 0.014 | - |

### By source (held-out and val): AUROC, and FPR@0.5 on safe examples

| decision | source | v5_l6 AUROC | v5_l6 FPR@0.5 | plain_v5_http AUROC | plain_v5_http FPR@0.5 | plain_v5_pi AUROC | plain_v5_pi FPR@0.5 | plain_v5_url AUROC | plain_v5_url FPR@0.5 |
|---|---|---|---|---|---|---|---|---|---|
| http_attack | dvwa-juiceshop | 0.916 ± 0.047 | 0.417 ± 0.152 | 0.916 ± 0.090 | 0.596 ± 0.255 | - | - | - | - |
| http_attack | sqli-queries | 0.993 ± 0.001 | 0.241 ± 0.006 | 0.992 ± 0.001 | 0.244 ± 0.015 | - | - | - | - |
| http_attack | spider | - | 0.002 ± 0.003 | - | 0.010 ± 0.003 | - | - | - | - |
| http_attack | waf-v2 | 0.884 ± 0.030 | 0.284 ± 0.159 | 0.872 ± 0.024 | 0.424 ± 0.304 | - | - | - | - |
| phishing_url | destroylist | - | - | - | - | - | - | - | - |
| phishing_url | phishtrap | 0.857 ± 0.015 | 0.244 ± 0.025 | - | - | - | - | 0.868 ± 0.007 | 0.203 ± 0.016 |
| prompt_injection | deepset | 0.755 ± 0.012 | 0.388 ± 0.027 | - | - | 0.718 ± 0.022 | 0.410 ± 0.021 | - | - |
| prompt_injection | jackhhao | 0.849 ± 0.033 | 0.440 ± 0.054 | - | - | 0.801 ± 0.037 | 0.533 ± 0.078 | - | - |
