# 01 — Goal and scope

## Goal

A fast, calibrated second-stage security check for **application-layer text**:

```
traffic ──► rules / WAF / cheap model (µs) ──► suspicious? ──► Cyber-Jev (ms, calibrated)
                                                                   │
                                  confident: block / allow ◄───────┤
                                  unsure (e.g. 0.2 < p < 0.8): LLM or human review
```

Calibrated probabilities are the product: they make "block above 0.9, review between
0.2 and 0.9" a meaningful policy, and let the cascade send only unsure cases upward.

## Decisions (v0.1)

| Decision | Options | State | Asks |
|---|---|---|---|
| `http_attack` | safe / attack | HTTP request line + body | Is this request a web attack (SQLi, XSS, traversal, command injection)? |
| `prompt_injection` | safe / injection | text sent to an LLM | Is this trying to override the model's instructions or jailbreak it? |
| `phishing_url` | legitimate / phishing | a URL | Is this URL phishing or malicious? |
| `decide` | your own | any | Anything else (weak until trained, as in Nano-Jev) |

Later candidates (v0.2+): `attack_type` (choice: sqli / xss / traversal / cmdi / other),
`log_anomaly` (normal / anomalous, LogHub), `command_risk` (safe / dangerous shell command),
`phishing_email`.

## Not in scope

- **Packet- or flow-level intrusion detection.** It needs microsecond latency on numeric
  features. Gradient-boosted trees on CIC-IDS2017 / UNSW-NB15 are the right tool there.
  Cyber-Jev only works on text-like payloads.
- Replacing a WAF or signature rules. It sits behind them.
- Generating explanations or remediation text.

## Targets for v0.1

| | Target |
|---|---|
| Size | ≤ 33M params (the Nano-Jev v1.0 backbone) |
| Latency | ≤ 5 ms per decision on CPU at max_length 256; ≤ 1 ms batched on RTX 3060 |
| Quality | Beat a TF-IDF + logistic-regression baseline on **held-out** sets, not only in-domain |
| Calibration | ECE ≤ 0.05 in-domain after temperature fitting |
| Security metric | Report detection rate at 1% and 0.1% false-positive rate |
