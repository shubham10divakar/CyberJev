# Cyber-Jev

> Jev-style decision model for security checks. Built on [Nano-Jev](https://github.com/shubham10divakar/nano-jev).
> Independent; not affiliated with TypeSafe AI.

**Status: alpha, not published.** Weights exist only as local training runs.

A small (33M parameter) **calibrated decision model** for text-like security data. Give it
an HTTP request, a prompt or a URL; it returns a **probability per option** in a few
milliseconds. It never generates text.

| Decision | Options | Input | Status |
|---|---|---|---|
| `http_attack` | safe / attack | request line + body | first dev run: good in-domain, fails on unseen sources (see plan/07) |
| `prompt_injection` | safe / injection | text sent to an LLM | planned |
| `phishing_url` | legitimate / phishing | URL | planned |
| `decide` | your own | any | untrained |

**What it is for:** a second-stage check behind rules or a WAF, with calibrated
probabilities so that "block above 0.9, review between 0.2 and 0.9" means something.
**What it is not for:** packet- or flow-level intrusion detection (use gradient-boosted
trees on numeric flow features), or as the only defence.

## Use

```bash
pip install -e .
cyber-jev http_attack --model runs/cyber-jev-dev "GET /login?user=admin' OR '1'='1' -- HTTP/1.1"
cyber-jev http_attack --model runs/cyber-jev-dev --json "GET /a HTTP/1.1" "GET /b HTTP/1.1"
cyber-jev decide --model runs/cyber-jev-dev --question "Which attack?" -o sqli -o xss -o other --state "..."
```

```python
import cyberjev
d = cyberjev.load("runs/cyber-jev-dev")
d.http_attack("GET /search?q=<script>alert(1)</script> HTTP/1.1")        # one -> one dict
d.http_attack(["GET /a HTTP/1.1", "GET /b HTTP/1.1"])                    # many -> list, batched
```

Inputs are URL-decoded before scoring, the same way the training data was prepared.

## Build, train, evaluate

```bash
pip install -e ".[train,test]"
set PYTHONUTF8=1                                              # Windows console: tables use →

python scripts/prepare_data.py                                # data/{train,calib,test}.jsonl
python scripts/prepare_data.py --heldout --out data_heldout   # data_heldout/test.jsonl
python scripts/train.py --base <nano-jev v1.0 folder> --out runs/cyber-jev-dev --max-length 256
python scripts/evaluate.py --model runs/cyber-jev-dev --max-length 256
python scripts/evaluate.py --model runs/cyber-jev-dev --no-save --max-length 256 \
    --test-data data_heldout --results-dir results --name cyberjev_heldout
python scripts/baselines.py                                   # TF-IDF + LR
python scripts/baselines.py --test-data data_heldout --name tfidf_heldout
python scripts/bench_latency.py --model runs/cyber-jev-dev
pytest
```

## Data

| | Source | Size |
|---|---|---|
| train / calib / test | CSIC 2010 HTTP requests ([`bridge4/CSIC2010_dataset_classification`](https://huggingface.co/datasets/bridge4/CSIC2010_dataset_classification)); headers dropped, URL-decoded, deduplicated, no train/test overlap | 10000 / 1500 / 3000 |
| held-out | SQLi / XSS / normal payloads from a different source ([`shengqin/web-attacks`](https://huggingface.co/datasets/shengqin/web-attacks)) | 5523 |

## Results

See [`results/`](results/) and [`plan/07_status.md`](plan/07_status.md).

## Licence

Code Apache-2.0 (copied from and adapted from Nano-Jev). Dataset licences are still to be
checked before any weights are released.
