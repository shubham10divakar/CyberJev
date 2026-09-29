## Calibration and triage — `runs/cyber-jev-v5-l6` (Decider path: torch, one pass: http_attack=threat-only, phishing_url=threat-only, prompt_injection=safe-only)

Policy: block if P(threat) ≥ 0.9, allow if ≤ 0.2, otherwise review.

| decision | set | n | ECE | reviewed | error on auto-decided | missed threats | false blocks | error @ review 0% / 10% / 20% |
|---|---|---|---|---|---|---|---|---|
| http_attack | in-domain | 4700 | 0.009 | 6.4% | 1.2% | 1.6% | 0.7% | 2.6% / 1.0% / 0.4% |
| http_attack | held-out | 10320 | 0.132 | 9.4% | 13.3% | 3.0% | 21.9% | 16.6% / 13.6% / 11.1% |
| http_attack | val | 3563 | 0.109 | 6.6% | 12.5% | 19.3% | 6.2% | 14.7% / 10.9% / 7.3% |
| prompt_injection | in-domain | 2500 | 0.021 | 5.4% | 2.5% | 3.4% | 1.3% | 4.1% / 1.3% / 0.8% |
| prompt_injection | held-out | 1951 | 0.198 | 24.0% | 21.0% | 7.8% | 23.2% | 27.1% / 25.5% / 23.9% |
| prompt_injection | val | 1500 | 0.160 | 31.6% | 17.8% | 8.8% | 15.6% | 26.6% / 24.1% / 22.5% |
| phishing_url | in-domain | 1998 | 0.034 | 26.4% | 3.7% | 4.0% | 1.4% | 10.8% / 7.3% / 4.2% |
| phishing_url | held-out | 5000 | 0.100 | 42.5% | 17.7% | 11.3% | 7.6% | 24.7% / 22.6% / 19.9% |
| phishing_url | val | 3000 | 0.065 | 26.1% | 5.8% | 4.8% | 3.7% | 14.1% / 10.5% / 8.0% |
