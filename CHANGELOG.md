# Changelog

## 0.1.0.dev0 (unreleased)

- Forked from Nano-Jev 1.0.0: same model, calibration, registry and CLI; package renamed
  `cyberjev`, command `cyber-jev`, settings in `~/.cyberjev`, env vars `CYBERJEV_*`.
- New schema: `http_attack`, `prompt_injection`, `phishing_url` (replaces relevance /
  sufficient / grounded). Built-in methods take one string or a list.
- `http_attack` data from CSIC 2010, held-out set from `shengqin/web-attacks`.
- Metrics add AUROC and detection rate at 1% / 0.1% false-positive rate.
- `scripts/baselines.py` is now a TF-IDF + logistic-regression baseline;
  new `scripts/bench_latency.py`.
