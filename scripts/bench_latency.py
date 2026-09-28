"""Latency of one decision, as a caller sees it (tokenise + encode + softmax).

    python scripts/bench_latency.py --model runs/cyber-jev-dev
    python scripts/bench_latency.py --model runs/cyber-jev-dev --threads 1   # one CPU core
    python scripts/bench_latency.py --model runs/cyber-jev-v2 --max-length 128 --out results/latency_v2_128.md

Reports median and p95 ms for batch size 1 on CPU and GPU, and ms per decision when a
batch of requests is scored together on GPU.
"""

import argparse
import random
import statistics
import sys
import time
from pathlib import Path

import torch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from cyberjev.decider import Decider  # noqa: E402
from cyberjev.report import read_jsonl  # noqa: E402


def timings(fn, inputs, warmup=10):
    for x in inputs[:warmup]:
        fn(x)
    out = []
    for x in inputs:
        t0 = time.perf_counter()
        fn(x)
        out.append(1000 * (time.perf_counter() - t0))
    return out


def row(name, ms):
    ms = sorted(ms)
    return f"| {name} | {statistics.median(ms):.2f} | {ms[int(0.95 * (len(ms) - 1))]:.2f} |"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", default="runs/cyber-jev-dev")
    ap.add_argument("--data", default="data")
    ap.add_argument("--n", type=int, default=300)
    ap.add_argument("--batch", type=int, default=64)
    ap.add_argument("--threads", type=int, help="CPU threads (default: torch's choice)")
    ap.add_argument("--max-length", type=int, help="override the model's max_length")
    ap.add_argument("--no-gpu", action="store_true")
    ap.add_argument("--out", help="also write the table to this .md file")
    args = ap.parse_args()
    if args.threads:
        torch.set_num_threads(args.threads)

    states = [ex["state"] for ex in read_jsonl(Path(args.data) / "test.jsonl")
              if ex["decision"] == "http_attack"]
    states = random.Random(0).sample(states, min(args.n, len(states)))  # test.jsonl is grouped by source
    ml = f", max_length {args.max_length}" if args.max_length else ""
    lines = [f"## Latency — `{args.model}`{ml}, http_attack, {len(states)} requests", "",
             "| setting | median ms | p95 ms |", "|---|---|---|"]

    devices = ["cpu"] + (["cuda"] if torch.cuda.is_available() and not args.no_gpu else [])
    for device in devices:
        d = Decider.from_pretrained(args.model, device=device)
        if args.max_length:
            d.max_length = args.max_length
        label = f"CPU ({torch.get_num_threads()} threads)" if device == "cpu" else "GPU"
        lines.append(row(f"{label}, batch 1", timings(d.http_attack, states)))
        if device == "cuda":
            batches = [states[i: i + args.batch] for i in range(0, len(states), args.batch)] * 5
            per = [ms / len(b) for ms, b in zip(timings(d.http_attack, batches, warmup=2), batches)]
            lines.append(row(f"GPU, batch {args.batch} (per decision)", per))
    print("\n".join(lines))
    if args.out:
        Path(args.out).write_text("\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
