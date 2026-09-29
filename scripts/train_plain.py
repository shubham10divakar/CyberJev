"""Plain classifier baseline: same backbone and recipe as Cyber-Jev, input text only.

    python scripts/train_plain.py --decision http_attack --data data_v5 --seed 0

No question and no option text: the state alone goes through the encoder and a standard
2-class head (fresh). One model per decision. Trained like train.py (batch 16, lr 3e-5,
4 epochs, 6% warmup, best epoch by dev NLL on a calib slice), then evaluated like
evaluate.py (temperature fitted on calib) on the in-domain test, held-out and val sets.
Weights are not kept. Results: results/cyberjev_plain_<prefix>_<decision>[_s<seed>]{,_heldout,_val}.json,
so scripts/seed_summary.py can compare them with the cross-encoder.
"""

import argparse
import copy
import json
import random
import sys
import time
from pathlib import Path

import torch
from torch.utils.data import DataLoader
from transformers import AutoModelForSequenceClassification, AutoTokenizer, get_linear_schedule_with_warmup

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from cyberjev.report import (by_decision, decision_report, labels_of, read_jsonl,  # noqa: E402
                             render_table, sources_of)


@torch.no_grad()
def logits_of(model, tok, examples, max_length, device, batch_size=64):
    model.eval()
    out = []
    for i in range(0, len(examples), batch_size):
        enc = tok([ex["state"] for ex in examples[i: i + batch_size]], truncation=True,
                  max_length=max_length, padding=True, return_tensors="pt").to(device)
        with torch.autocast(device_type="cuda", dtype=torch.bfloat16, enabled=device == "cuda"):
            out.append(model(**enc).logits.float().cpu())
    return torch.cat(out)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--decision", required=True)
    ap.add_argument("--data", default="data")
    ap.add_argument("--heldout", default="data_heldout")
    ap.add_argument("--val", default="data_val")
    ap.add_argument("--base", default="../nano_jev/runs/nano-jev-v0.1")
    ap.add_argument("--prefix", default="v5", help="data version, used in result names")
    ap.add_argument("--epochs", type=int, default=4)
    ap.add_argument("--batch-size", type=int, default=16)
    ap.add_argument("--lr", type=float, default=3e-5)
    ap.add_argument("--max-length", type=int, default=256)
    ap.add_argument("--dev-size", type=int, default=1500)
    ap.add_argument("--seed", type=int, default=0)
    args = ap.parse_args()

    random.seed(args.seed)
    torch.manual_seed(args.seed)
    device = "cuda" if torch.cuda.is_available() else "cpu"
    dec = args.decision
    take = lambda path: by_decision(read_jsonl(path)).get(dec, [])  # noqa: E731
    train, calib = take(Path(args.data) / "train.jsonl"), take(Path(args.data) / "calib.jsonl")
    tests = {"": take(Path(args.data) / "test.jsonl"),
             "_heldout": take(Path(args.heldout) / "test.jsonl"),
             "_val": take(Path(args.val) / "val.jsonl")}
    dev = random.Random(args.seed).sample(calib, min(args.dev_size, len(calib)))

    tok = AutoTokenizer.from_pretrained(args.base)
    model = AutoModelForSequenceClassification.from_pretrained(
        args.base, num_labels=2, ignore_mismatched_sizes=True).to(device)

    def collate(batch):
        enc = tok([ex["state"] for ex in batch], truncation=True, max_length=args.max_length,
                  padding=True, return_tensors="pt")
        return enc, torch.tensor([ex["label"] for ex in batch])

    loader = DataLoader(train, batch_size=args.batch_size, shuffle=True, collate_fn=collate)
    opt = torch.optim.AdamW(model.parameters(), lr=args.lr, weight_decay=0.01)
    total = len(loader) * args.epochs
    sched = get_linear_schedule_with_warmup(opt, int(0.06 * total), total)
    dev_nll = lambda: float(torch.nn.functional.cross_entropy(  # noqa: E731
        logits_of(model, tok, dev, args.max_length, device), labels_of(dev)))

    best, best_state = float("inf"), None
    print(f"{dec}: {len(train)} train, {total} steps, init dev NLL {dev_nll():.4f}", flush=True)
    for epoch in range(args.epochs):
        model.train()
        t0 = time.time()
        for enc, labels in loader:
            enc = {k: v.to(device) for k, v in enc.items()}
            with torch.autocast(device_type="cuda", dtype=torch.bfloat16, enabled=device == "cuda"):
                logits = model(**enc).logits.float()
            loss = torch.nn.functional.cross_entropy(logits, labels.to(device))
            loss.backward()
            torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0)
            opt.step()
            sched.step()
            opt.zero_grad(set_to_none=True)
        nll = dev_nll()
        print(f"epoch {epoch + 1} done in {time.time() - t0:.0f}s  dev NLL {nll:.4f}", flush=True)
        if nll < best:
            best, best_state = nll, copy.deepcopy(model.state_dict())
    model.load_state_dict(best_state)

    c_logits = logits_of(model, tok, calib, args.max_length, device)
    suffix = "" if args.seed == 0 else f"_s{args.seed}"
    short = {"http_attack": "http", "prompt_injection": "pi", "phishing_url": "url"}[dec]
    for set_suffix, examples in tests.items():
        if not examples:
            continue
        t0 = time.time()
        t_logits = logits_of(model, tok, examples, args.max_length, device)
        ms = 1000 * (time.time() - t0) / len(examples)
        report = {dec: decision_report(c_logits, labels_of(calib), t_logits, labels_of(examples),
                                       ms, sources_of(examples))}
        name = f"cyberjev_plain_{args.prefix}_{short}{suffix}{set_suffix}"
        Path("results", f"{name}.json").write_text(json.dumps(report, indent=2))
        table = render_table(f"Plain classifier ({dec}, seed {args.seed}) on{set_suffix or ' in-domain'}", report)
        Path("results", f"{name}.md").write_text(table + "\n", encoding="utf-8")
        print(table.splitlines()[4], flush=True)


if __name__ == "__main__":
    main()
