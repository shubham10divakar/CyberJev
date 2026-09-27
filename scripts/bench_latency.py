"""Latency of one decision, as a caller sees it (tokenise + encode + softmax).

    python scripts/bench_latency.py --model runs/cyber-jev-dev
    python scripts/bench_latency.py --model runs/cyber-jev-dev --threads 1   # one CPU core

Reports median and p95 ms for batch size 1 on CPU and GPU, and ms per decision when a
batch of requests is scored together on GPU.
"""

import argparse
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
    args = ap.parse_args()
    if args.threads:
        torch.set_num_threads(args.threads)

    states = [ex["state"] for ex in read_jsonl(Path(args.data) / "test.jsonl")
              if ex["decision"] == "http_attack"][: args.n]
    lines = [f"## Latency — `{args.model}`, http_attack, {len(states)} requests", "",
             "| setting | median ms | p95 ms |", "|---|---|---|"]

    devices = ["cpu"] + (["cuda"] if torch.cuda.is_available() else [])
    for device in devices:
        d = Decider.from_pretrained(args.model, device=device)
        label = f"CPU ({torch.get_num_threads()} threads)" if device == "cpu" else "GPU"
        lines.append(row(f"{label}, batch 1", timings(d.http_attack, states)))
        if device == "cuda":
            batches = [states[i: i + args.batch] for i in range(0, len(states), args.batch)] * 5
            per = [ms / len(b) for ms, b in zip(timings(d.http_attack, batches, warmup=2), batches)]
            lines.append(row(f"GPU, batch {args.batch} (per decision)", per))
    print("\n".join(lines))


if __name__ == "__main__":
    main()
