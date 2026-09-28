# Changelog

## 0.1.0.dev0 (unreleased)

- Forked from Nano-Jev 1.0.0: same model, calibration, registry and CLI; package renamed
  `cyberjev`, command `cyber-jev`, settings in `~/.cyberjev`, env vars `CYBERJEV_*`.
- New schema: `http_attack`, `prompt_injection`, `phishing_url` (replaces relevance /
  sufficient / grounded). Built-in methods take one string or a list.
- `http_attack` data v2: trains on CSIC 2010 + `shengqin/web-attacks` + `notesbymuneeb/ai-waf-dataset`;
  held-out set from `zrmarine/sql_injection` and `vyykaaa/dataset-web-attack` (was: CSIC only,
  held-out `shengqin/web-attacks` test). `prepare_data.py` builds both in one run.
- `normalize_http` handles full requests: drops content-negotiation headers, keeps headers
  that can carry payloads, strips scheme and host.
- Reports add a per-source breakdown (AUROC, and FPR / detection rate at the 0.5 threshold).
- Metrics add AUROC and detection rate at 1% / 0.1% false-positive rate.
- `scripts/baselines.py` is now a TF-IDF + logistic-regression baseline;
  new `scripts/bench_latency.py`.
