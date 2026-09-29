## Calibration and triage — `runs/cyber-jev-v5-l6-s1` (Decider path: torch, one pass: http_attack=threat-only, phishing_url=safe-only, prompt_injection=safe-only)

Policy: block if P(threat) ≥ 0.9, allow if ≤ 0.2, otherwise review.

| decision | set | n | ECE | reviewed | error on auto-decided | missed threats | false blocks | error @ review 0% / 10% / 20% |
|---|---|---|---|---|---|---|---|---|
| http_attack | in-domain | 4700 | 0.014 | 8.4% | 0.9% | 1.5% | 0.1% | 3.1% / 0.8% / 0.4% |
| http_attack | held-out | 10320 | 0.107 | 7.4% | 10.7% | 1.8% | 18.5% | 13.8% / 10.6% / 7.6% |
| http_attack | val | 3563 | 0.107 | 15.3% | 12.7% | 12.5% | 9.4% | 15.6% / 13.3% / 12.2% |
| prompt_injection | in-domain | 2500 | 0.009 | 7.6% | 1.8% | 2.0% | 1.2% | 3.7% / 1.4% / 0.8% |
| prompt_injection | held-out | 1951 | 0.221 | 21.0% | 24.9% | 5.8% | 31.9% | 28.7% / 27.0% / 25.7% |
| prompt_injection | val | 1500 | 0.187 | 37.5% | 20.6% | 8.0% | 17.7% | 30.7% / 28.1% / 26.1% |
| phishing_url | in-domain | 1998 | 0.030 | 16.4% | 5.3% | 6.5% | 2.3% | 10.3% / 6.6% / 5.0% |
| phishing_url | held-out | 5000 | 0.147 | 26.5% | 21.9% | 19.5% | 8.1% | 25.3% / 23.4% / 20.4% |
| phishing_url | val | 3000 | 0.059 | 15.7% | 7.2% | 5.5% | 6.5% | 12.9% / 9.3% / 7.4% |
