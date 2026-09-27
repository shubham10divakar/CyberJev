# 02 — Architecture

## Same model as Nano-Jev

```
[CLS] question: <q> option: <opt> [SEP] <state> [SEP] → MiniLM encoder → linear → logit
```

Options are scored independently and softmaxed, with a fitted temperature per decision.
Nothing about the model changes; only the schema, data and weights do.

## What is copied from nano_jev

Copy (then rename `nanojev` → `cyberjev`, `NANOJEV_*` → `CYBERJEV_*`, `~/.nanojev` → `~/.cyberjev`):

| From nano_jev | Change |
|---|---|
| `nanojev/model.py`, `calibration.py`, `report.py` | none |
| `nanojev/decider.py` | built-in wrappers become `http_attack`, `prompt_injection`, `phishing_url` |
| `nanojev/schema.py` | new `DECISIONS` table (see 01) |
| `nanojev/registry.py` | `DEFAULT_REPO = "sdmlai/cyber-jev"` (placeholder until published) |
| `nanojev/__main__.py` | CLI `cyber-jev` with the new decision commands |
| `nanojev/data.py` | rewritten: security dataset builders |
| `scripts/train.py`, `evaluate.py`, `cascade.py` | none / small path changes |
| `scripts/prepare_data.py` | new presets for security data |
| `scripts/baselines.py` | replace bge/Qwen baselines with TF-IDF + LR (+ optional Qwen cascade) |
| `tests/` | adapted to the new decisions |
| `pyproject.toml`, `LICENSE`, `.gitignore` | name `cyber-jev`, Apache-2.0 |

Not copied: `data/`, `runs/`, `dist/`, `results/`, `model_cards/`, the paper.

## Initial weights

Fine-tune **from Nano-Jev v1.0** (MIT, already knows the question/option format).
Ablation: also train from plain `microsoft/MiniLM-L12-H384-uncased` and keep whichever
is better on held-out sets.

## Repo and git

`code_repo/` is the nano-jev git repo (remote: github.com/shubham10divakar/nano-jev).
So Cyber-Jev must not be committed there:

1. `git init` inside `cyber_jev/` (its own repo, no remote yet).
2. Add `cyber_jev/` to `code_repo/.git/info/exclude` (local-only, changes no tracked file).

## Layout

```
cyber_jev/
  plan/                 this plan
  cyberjev/             package (copied + adapted)
  scripts/              prepare_data, train, evaluate, baselines, cascade, bench_latency
  tests/
  data/                 train / calib / test (all decisions)
  data_heldout/         out-of-domain test sets
  runs/                 trained models (git-ignored)
  results/              metrics tables
  README.md  CHANGELOG.md  pyproject.toml  LICENSE
```
