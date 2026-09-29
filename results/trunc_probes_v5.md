## Seeds: mean ± std of calibrated AUROC (two-pass)

| decision | set | v5_l6 (n=1) | v5ht_l6 (n=1) | v5ml512_l6 (n=1) |
|---|---|---|---|---|
| http_attack | in-domain | 0.995 | 0.995 | 0.995 |
| http_attack | held-out | 0.955 | 0.960 | 0.953 |
| http_attack | val | 0.940 | 0.922 | 0.906 |
| phishing_url | in-domain | 0.966 | 0.969 | 0.969 |
| phishing_url | held-out | 0.817 | 0.821 | 0.814 |
| phishing_url | val | 0.947 | 0.946 | 0.947 |
| prompt_injection | in-domain | 0.994 | 0.994 | 0.995 |
| prompt_injection | held-out | 0.829 | 0.828 | 0.799 |
| prompt_injection | val | 0.813 | 0.787 | 0.808 |

### By source (held-out and val): AUROC, and FPR@0.5 on safe examples

| decision | source | v5_l6 AUROC | v5_l6 FPR@0.5 | v5ht_l6 AUROC | v5ht_l6 FPR@0.5 | v5ml512_l6 AUROC | v5ml512_l6 FPR@0.5 |
|---|---|---|---|---|---|---|---|
| http_attack | dvwa-juiceshop | 0.933 | 0.305 | 0.955 | 0.288 | 0.934 | 0.355 |
| http_attack | sqli-queries | 0.991 | 0.235 | 0.985 | 0.238 | 0.981 | 0.253 |
| http_attack | spider | - | 0.000 | - | 0.007 | - | 0.002 |
| http_attack | waf-v2 | 0.919 | 0.102 | 0.894 | 0.140 | 0.872 | 0.269 |
| phishing_url | destroylist | - | - | - | - | - | - |
| phishing_url | phishtrap | 0.874 | 0.265 | 0.872 | 0.302 | 0.865 | 0.277 |
| prompt_injection | deepset | 0.747 | 0.358 | 0.756 | 0.388 | 0.765 | 0.391 |
| prompt_injection | jackhhao | 0.870 | 0.398 | 0.867 | 0.476 | 0.820 | 0.486 |
