"""Export a Cyber-Jev model to ONNX (fp32 and dynamic int8) and check it on CPU.

    python scripts/onnx_cpu.py --model runs/cyber-jev-v2-l6 --out results/onnx_v2_l6.md

Writes model.onnx and model.int8.onnx into the model folder, then reports, for PyTorch,
ONNX fp32 and ONNX int8 on CPU: http_attack AUROC / DR@1%FPR on the in-domain test set and
a fixed random sample of the held-out set (temperature refitted on calib for each), and
batch-1 latency.

Each variant runs in its own process (--variant), so only one model is in memory at a
time; without --variant the script runs all three that way and then merges the rows.
"""

import argparse
import json
import random
import statistics
import subprocess
import sys
import time
from pathlib import Path

import onnxruntime as ort
import torch
from onnxruntime.quantization import QuantType, quantize_dynamic

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from cyberjev import model as M  # noqa: E402
from cyberjev.calibration import fit_temperature, metrics  # noqa: E402
from cyberjev.report import labels_of, read_jsonl  # noqa: E402


def export(model, tok, path: Path):
    enc = tok(["question: q option: o"], ["GET / HTTP/1.1"], return_tensors="pt")
    names = ["input_ids", "attention_mask", "token_type_ids"]
    dyn = {n: {0: "batch", 1: "seq"} for n in names} | {"logits": {0: "batch"}}
    torch.onnx.export(model.cpu().eval(), tuple(enc[n] for n in names), str(path),
                      input_names=names, output_names=["logits"], dynamic_axes=dyn,
                      opset_version=17, dynamo=False)


def ort_session(path: Path, threads: int) -> ort.InferenceSession:
    so = ort.SessionOptions()
    so.intra_op_num_threads = threads
    so.graph_optimization_level = ort.GraphOptimizationLevel.ORT_ENABLE_ALL
    return ort.InferenceSession(str(path), so, providers=["CPUExecutionProvider"])


def make_scorer(kind, model, tok, sess, max_length):
    """Return f(items) -> [n, 2] logits, scoring one batch of items."""
    def run(items):
        enc, g, p = M.encode(tok, items, max_length)
        if kind == "torch":
            with torch.no_grad():
                flat = model(**enc).logits.squeeze(-1).float()
        else:
            flat = torch.from_numpy(sess.run(None, {k: v.numpy() for k, v in enc.items()})[0]
                                    ).squeeze(-1).float()
        out = torch.zeros(len(items), int(p.max()) + 1)
        out[g, p] = flat
        return out
    return run


def score_all(run, items, batch=32):
    return torch.cat([run(items[i: i + batch]) for i in range(0, len(items), batch)])


def latency(run, items, warmup=10):
    for it in items[:warmup]:
        run([it])
    ms = []
    for it in items:
        t0 = time.perf_counter()
        run([it])
        ms.append(1000 * (time.perf_counter() - t0))
    ms.sort()
    return statistics.median(ms), ms[int(0.95 * (len(ms) - 1))]


VARIANTS = {"torch": "PyTorch fp32", "fp32": "ONNX fp32", "int8": "ONNX int8"}


def run_variant(args, folder: Path) -> dict:
    fp32, int8 = folder / "model.onnx", folder / "model.int8.onnx"
    if args.variant == "torch":
        model, tok = M.load(args.model, "cpu")
        run, size = make_scorer("torch", model, tok, None, args.max_length), folder / "model.safetensors"
    else:
        from transformers import AutoTokenizer
        tok = AutoTokenizer.from_pretrained(args.model)
        path = fp32 if args.variant == "fp32" else int8
        run = make_scorer("ort", None, tok, ort_session(path, args.threads), args.max_length)
        size = path

    calib = read_jsonl(Path(args.data) / "calib.jsonl")
    heldout = read_jsonl(Path(args.heldout) / "test.jsonl")
    tests = {"in-domain": read_jsonl(Path(args.data) / "test.jsonl"),
             "held-out": random.Random(0).sample(heldout, min(args.heldout_n, len(heldout)))}
    lat_items = random.Random(0).sample(tests["in-domain"], args.n_latency)

    t = fit_temperature(score_all(run, calib), labels_of(calib))
    m = {k: metrics(score_all(run, ex), labels_of(ex), t) for k, ex in tests.items()}
    med, p95 = latency(run, lat_items)
    return {"temperature": t, "metrics": m, "median_ms": med, "p95_ms": p95,
            "size_mb": size.stat().st_size / 2**20}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", default="runs/cyber-jev-v2-l6")
    ap.add_argument("--data", default="data")
    ap.add_argument("--heldout", default="data_heldout")
    ap.add_argument("--heldout-n", type=int, default=3000, help="held-out examples to score")
    ap.add_argument("--max-length", type=int, default=256)
    ap.add_argument("--threads", type=int, default=8)
    ap.add_argument("--n-latency", type=int, default=300)
    ap.add_argument("--variant", choices=VARIANTS, help="run one variant, print its JSON row")
    ap.add_argument("--out")
    args = ap.parse_args()
    torch.set_num_threads(args.threads)
    folder = Path(args.model)

    if args.variant:
        print("ROW " + json.dumps(run_variant(args, folder)), flush=True)
        return

    fp32, int8 = folder / "model.onnx", folder / "model.int8.onnx"
    if not fp32.exists():
        model, tok = M.load(args.model, "cpu")
        export(model, tok, fp32)
        del model
    if not int8.exists():
        quantize_dynamic(str(fp32), str(int8), weight_type=QuantType.QInt8)

    lines = [f"## CPU inference — `{args.model}`, {args.threads} threads, max_length "
             f"{args.max_length}, held-out sample {args.heldout_n}", "",
             "| variant | size MB | in-domain AUROC | in-domain DR@1%FPR | held-out AUROC "
             "| held-out DR@1%FPR | median ms | p95 ms |", "|---|---|---|---|---|---|---|---|"]
    report = {}
    passthrough = [a for a in sys.argv[1:] if a not in ("--out", args.out)]
    for key, name in VARIANTS.items():
        proc = subprocess.run([sys.executable, __file__, *passthrough, "--variant", key],
                              capture_output=True, text=True, encoding="utf-8")
        rows = [ln for ln in proc.stdout.splitlines() if ln.startswith("ROW ")]
        if proc.returncode or not rows:
            sys.exit(f"{name} failed:\n{proc.stderr[-2000:]}")
        r = report[name] = json.loads(rows[-1][4:])
        m = r["metrics"]
        lines.append(f"| {name} | {r['size_mb']:.0f} | {m['in-domain']['auroc']:.3f} "
                     f"| {m['in-domain']['dr_at_1pct_fpr']:.3f} | {m['held-out']['auroc']:.3f} "
                     f"| {m['held-out']['dr_at_1pct_fpr']:.3f} | {r['median_ms']:.2f} "
                     f"| {r['p95_ms']:.2f} |")
        print(lines[-1], flush=True)
    table = "\n".join(lines)
    print(table)
    if args.out:
        Path(args.out).write_text(table + "\n", encoding="utf-8")
        Path(args.out).with_suffix(".json").write_text(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
