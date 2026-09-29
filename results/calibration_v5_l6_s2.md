## Calibration and triage — `runs/cyber-jev-v5-l6-s2` (Decider path: torch, one pass: http_attack=safe-only, phishing_url=safe-only, prompt_injection=threat-only)

Policy: block if P(threat) ≥ 0.9, allow if ≤ 0.2, otherwise review.

| decision | set | n | ECE | reviewed | error on auto-decided | missed threats | false blocks | error @ review 0% / 10% / 20% |
|---|---|---|---|---|---|---|---|---|
| http_attack | in-domain | 4700 | 0.049 | 17.9% | 1.0% | 1.3% | 0.3% | 6.9% / 2.2% / 0.8% |
| http_attack | held-out | 10320 | 0.078 | 27.8% | 2.7% | 2.7% | 1.1% | 14.4% / 10.5% / 6.2% |
| http_attack | val | 3563 | 0.091 | 37.9% | 11.2% | 15.0% | 1.1% | 18.1% / 16.6% / 14.6% |
| prompt_injection | in-domain | 2500 | 0.020 | 4.1% | 2.8% | 3.6% | 1.7% | 3.8% / 1.2% / 0.6% |
| prompt_injection | held-out | 1951 | 0.242 | 17.6% | 26.8% | 7.8% | 34.6% | 30.8% / 28.5% / 27.2% |
| prompt_injection | val | 1500 | 0.175 | 22.4% | 21.6% | 16.8% | 16.7% | 26.1% / 24.7% / 22.8% |
| phishing_url | in-domain | 1998 | 0.017 | 23.1% | 3.0% | 2.8% | 1.8% | 9.5% / 6.0% / 3.7% |
| phishing_url | held-out | 5000 | 0.117 | 45.9% | 14.4% | 7.1% | 9.4% | 25.4% / 22.6% / 19.9% |
| phishing_url | val | 3000 | 0.062 | 25.5% | 7.2% | 5.0% | 5.7% | 13.0% / 10.3% / 8.8% |
