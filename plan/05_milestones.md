# 05 — Milestones

| # | Step | Done when |
|---|---|---|
| M0 | **Setup**: `git init` in cyber_jev, exclude it from the nano-jev repo, copy + rename the package, scripts and tests | `pytest` passes on the copied code (with the new schema) |
| M1 | **http_attack prototype**: move `_staging` data in, train on it, evaluate + TF-IDF baseline | results table in `results/http_attack_v0.md`, in-domain and held-out |
| M2 | **Go/no-go**: does Cyber-Jev beat TF-IDF+LR on the held-out set, or add calibration/cascade value it lacks? | a written decision in `plan/07_status.md` |
| M3 | **More decisions**: verify and add `prompt_injection` and `phishing_url` data | `scripts/prepare_data.py` builds all three |
| M4 | **Joint model**: train one model on all decisions, evaluate each | results for all decisions ≥ single-task within ~1 point |
| M5 | **Latency**: `bench_latency.py`, CPU + GPU numbers | targets from 01 met, or documented |
| M6 | **Package**: CLI `cyber-jev`, README, model card, tests, smoke test | `pip install -e .` + `cyber-jev http_attack ...` works |
| M7 | **Release (only when asked)**: HF `sdmlai/cyber-jev` v0.1, PyPI `cyber-jev` 0.1.0 | published |

M0–M2 are the first work session. Nothing gets published or pushed without an explicit go.
