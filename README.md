# Cyber-Jev

> Jev-style decision model for security checks. Built on [Nano-Jev](https://github.com/shubham10divakar/nano-jev).
> Independent; not affiliated with TypeSafe AI.

**Status: alpha, research in progress.** Weights exist only as local training runs; a paper
is in preparation (see [Citation](#citation)).

A small (22M parameter, 6-layer) **calibrated decision model** for text-like security data. Give it
an HTTP request, a prompt or a URL; it returns a **probability per option** in a few
milliseconds. It never generates text.

| Decision | Options | Input | Status |
|---|---|---|---|
| `http_attack` | safe / attack | request line + body | strong: held-out AUROC 0.96, val 0.92 (3 seeds) |
| `prompt_injection` | safe / injection | text sent to an LLM | in progress: level with TF-IDF on val (0.80), below it on held-out |
| `phishing_url` | legitimate / phishing | URL | beats TF-IDF: held-out 0.81 (vs 0.71), val 0.94 |
| `decide` | your own | any | untrained |

One joint model answers all three (`runs/cyber-jev-v5-l6`); on CPU with ONNX int8 a decision
takes about 4 ms. Numbers and caveats: [`plan/07_status.md`](plan/07_status.md).

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

## Data

`python scripts/prepare_data.py` downloads the public sources and builds the current data
(v6): `data/` (train / calib / in-domain test), `data_heldout/` (out-of-domain test, never
trained on) and `data_val/` (out-of-domain validation, only for choices). The built files
are committed so results can be reproduced; they are derived from third-party datasets,
each under its own licence. **Sources, licences and attribution: [`DATA.md`](DATA.md).**
Details, checks and caveats: [`plan/03_data.md`](plan/03_data.md).

## Results

See [`results/`](results/) and [`plan/07_status.md`](plan/07_status.md).

## Citation

A paper describing Cyber-Jev (the typed-decision model, the out-of-domain evaluation and the
dataset-hygiene findings) is **in progress**. If you use this code, the built data or the
results, please cite it; until it is out, cite this repository:

```bibtex
@misc{cyberjev2026,
  title  = {Cyber-Jev: a small calibrated decision model for application-layer security checks},
  author = {Subham},
  year   = {2026},
  note   = {Paper in preparation. Code and data: https://github.com/shubham10divakar/CyberJev}
}
```

<!-- Paper reference goes here once available: venue, arXiv id, BibTeX. -->
*Paper: to be added.*

Please also cite the original datasets you use (listed in [`DATA.md`](DATA.md)).

## Licence

Code: Apache-2.0 (adapted from Nano-Jev). Built data in `data*/`: derived from third-party
datasets that keep their own licences; see [`DATA.md`](DATA.md) before any use beyond research.
