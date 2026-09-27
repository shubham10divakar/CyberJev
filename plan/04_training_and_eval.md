# 04 — Training and evaluation

## Training

Reuse Nano-Jev's `scripts/train.py` unchanged:

```bash
python scripts/train.py --data data --base <nano-jev v1.0 path> --out runs/cyber-jev-dev \
    --max-length 256 --epochs 2 --batch-size 16 --lr 3e-5
python scripts/evaluate.py --model runs/cyber-jev-dev                         # fits temperatures
python scripts/evaluate.py --model runs/cyber-jev-dev --no-save --test-data data_heldout --name heldout
```

Order: first `http_attack` alone (fast signal), then all decisions together.

## Baselines

| Baseline | Why |
|---|---|
| Zero-shot Nano-Jev v1.0 | shows what fine-tuning adds |
| **TF-IDF (char 1–5-grams) + logistic regression** | the real bar: very strong and microsecond-fast on SQLi/XSS; if Cyber-Jev can't beat it on held-out sets, it has no reason to exist |
| Cyber-Jev from plain MiniLM | checks whether starting from Nano-Jev helps |
| (optional) Qwen3-4B prompted, and the cascade | same cascade study as Nano-Jev |

## Metrics (per decision, in-domain and held-out)

- accuracy, macro-F1
- **detection rate at 1% and 0.1% false-positive rate** (what security teams use)
- NLL, Brier, ECE before and after temperature scaling
- ms per decision: CPU batch 1, GPU batch 1, GPU batched (new `scripts/bench_latency.py`)

## Latency plan

- max_length 256 (short states; HTTP line + body is usually < 128 tokens)
- only 2 options per built-in decision → 2 encoder passes per decision
- if CPU needs to go faster: ONNX export + int8 dynamic quantisation (v0.2)
