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

**Fast CPU inference.** With `pip install -e ".[onnx]"`, a Decider on CPU uses the model
folder's `model.int8.onnx` (else `model.onnx`) instead of PyTorch: about 4.4 ms per
`http_attack` decision on 8 threads vs 9.8 ms. Force a backend with
`cyberjev.Decider.from_pretrained(path, backend="torch" | "onnx")`; `d.backend` shows which
one is in use. When the folder has `one_pass.json`, built-in decisions need one encoder pass.

## Build, train, evaluate

```bash
pip install -e ".[train,test]"
pip install -e ".[export]"                                    # only for scripts/onnx_cpu.py
set PYTHONUTF8=1                                              # Windows console: tables use →

python scripts/prepare_data.py            # data/{train,calib,test}.jsonl + data_heldout/test.jsonl
python scripts/train.py --base <nano-jev v0.1 folder> --out runs/cyber-jev-v2-l6 --max-length 256 --epochs 4
python scripts/evaluate.py --model runs/cyber-jev-v2-l6 --max-length 256 --results-dir results --name cyberjev_v2_l6
python scripts/evaluate.py --model runs/cyber-jev-v2-l6 --no-save --max-length 256     --test-data data_heldout --results-dir results --name cyberjev_v2_l6_heldout
python scripts/baselines.py                                   # TF-IDF + LR
python scripts/baselines.py --test-data data_heldout --name tfidf_heldout
python scripts/bench_latency.py --model runs/cyber-jev-v2-l6
python scripts/single_pass.py --model runs/cyber-jev-v2-l6 --save --out results/single_pass_v2_l6.md   # one_pass.json
python scripts/onnx_cpu.py --model runs/cyber-jev-v2-l6 --save --out results/onnx_v2_l6.md
python scripts/onnx_cpu.py --model runs/cyber-jev-v2-l6 --one-pass --save --out results/onnx_v2_l6_one_pass.md
pytest
```

The 6-layer base is Nano-Jev v0.1 (`../nano_jev/runs/nano-jev-v0.1`); the 12-layer
`cyber-jev-v2` used Nano-Jev v1.0. Weights live in `runs/` (git-ignored).

## Data (`http_attack` v2)

| | Source | Size |
|---|---|---|
| train / calib / test | CSIC 2010 ([`bridge4/CSIC2010_dataset_classification`](https://huggingface.co/datasets/bridge4/CSIC2010_dataset_classification)) | 6000 / 500 / 1500 |
| train / calib / test | payloads ([`shengqin/web-attacks`](https://huggingface.co/datasets/shengqin/web-attacks)) | 6000 / 500 / 1500 |
| train / calib / test | full requests, many hosts ([`notesbymuneeb/ai-waf-dataset`](https://huggingface.co/datasets/notesbymuneeb/ai-waf-dataset)) | 9550 / 600 / 1200 |
| held-out | SQL queries and SQLi ([`zrmarine/sql_injection`](https://huggingface.co/datasets/zrmarine/sql_injection)) | 6000 |
| held-out | DVWA + Juice Shop requests ([`vyykaaa/dataset-web-attack`](https://huggingface.co/datasets/vyykaaa/dataset-web-attack)) | 4320 |

Details, text format and caveats: [`plan/03_data.md`](plan/03_data.md).

## Results

See [`results/`](results/) and [`plan/07_status.md`](plan/07_status.md).

## Licence

Code Apache-2.0 (copied from and adapted from Nano-Jev). Dataset licences are still to be
checked before any weights are released.
