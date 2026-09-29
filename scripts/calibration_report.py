"""Calibration and triage report for a Decider (paper items 8 and 9).

    python scripts/calibration_report.py --model runs/cyber-jev-v5-l6 --data data_v5 \
        --out results/calibration_v5_l6

Scores every built-in decision through the Decider exactly as a caller would (its one-pass
path and fitted calibration) on the in-domain test, held-out and val sets, then writes:

- reliability: 10 equal-width bins of P(threat) vs the observed threat rate, and ECE;
- triage at the default policy: block if p >= 0.9, allow if p <= 0.2, else review. Share
  reviewed, error rate on the auto-decided rest, missed threats, false blocks;
- risk-coverage: send the r% most uncertain inputs (p closest to 0.5) to review and report
  the error on the rest, for r = 0, 5, ..., 50 (selective classification).

<out>.json, <out>.md and <out>_<decision>.png (reliability + risk-coverage per set).
"""

import argparse
import json
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from cyberjev.decider import Decider  # noqa: E402
from cyberjev.report import by_decision, read_jsonl  # noqa: E402
from cyberjev.schema import DECISIONS  # noqa: E402

SETS = {"in-domain": ("{data}", "test.jsonl"), "held-out": ("data_heldout", "test.jsonl"),
        "val": ("data_val", "val.jsonl")}
REVIEW = list(range(0, 55, 5))


def reliability(p, y, n_bins=10):
    edges = np.linspace(0, 1, n_bins + 1)
    bins, ece = [], 0.0
    for lo, hi in zip(edges[:-1], edges[1:]):
        m = (p >= lo) & ((p < hi) if hi < 1 else (p <= hi))
        if m.any():
            bins.append({"lo": float(lo), "hi": float(hi), "n": int(m.sum()),
                         "mean_p": float(p[m].mean()), "threat_rate": float(y[m].mean())})
            ece += m.mean() * abs(p[m].mean() - y[m].mean())
    return bins, float(ece)


def triage(p, y, allow=0.2, block=0.9):
    auto = (p <= allow) | (p >= block)
    pred = p >= block
    wrong = auto & (pred != (y == 1))
    return {"reviewed": float(1 - auto.mean()),
            "auto_error": float(wrong.sum() / max(auto.sum(), 1)),
            "missed_threats": float((auto & ~pred & (y == 1)).sum() / max((y == 1).sum(), 1)),
            "false_blocks": float((auto & pred & (y == 0)).sum() / max((y == 0).sum(), 1))}


def risk_coverage(p, y):
    order = np.argsort(-np.abs(p - 0.5))                   # most confident first
    wrong = ((p >= 0.5) != (y == 1))[order]
    out = []
    for r in REVIEW:
        keep = int(round(len(p) * (1 - r / 100)))
        out.append({"reviewed_pct": r, "error_on_rest": float(wrong[:keep].mean()) if keep else 0.0})
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", default="runs/cyber-jev-v5-l6")
    ap.add_argument("--data", default="data")
    ap.add_argument("--device", default=None)
    ap.add_argument("--out", required=True, help="path prefix, e.g. results/calibration_v5_l6")
    args = ap.parse_args()

    d = Decider.from_pretrained(args.model, device=args.device, backend="torch")
    report = {}
    for set_name, (folder, fname) in SETS.items():
        exs = by_decision(read_jsonl(Path(folder.format(data=args.data)) / fname))
        for dec, items in exs.items():
            threat = DECISIONS[dec].options[1]
            probs = d.decide_many([{**ex, "decision": dec} for ex in items])
            p = np.array([pr[threat] for pr in probs])
            y = np.array([ex["label"] for ex in items])
            bins, ece = reliability(p, y)
            report.setdefault(dec, {})[set_name] = {
                "n": len(y), "threat_share": float(y.mean()), "ece": ece, "reliability": bins,
                "triage_0.2_0.9": triage(p, y), "risk_coverage": risk_coverage(p, y)}
            print(f"{dec:17} {set_name:9} n={len(y):5} ECE {ece:.3f} "
                  f"triage {report[dec][set_name]['triage_0.2_0.9']}", flush=True)

    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.with_suffix(".json").write_text(json.dumps(report, indent=2))
    lines = [f"## Calibration and triage — `{args.model}` (Decider path: {d.backend}, "
             f"one pass: {', '.join(f'{k}={v['variant']}' for k, v in d.one_pass.items()) or 'no'})", "",
             "Policy: block if P(threat) ≥ 0.9, allow if ≤ 0.2, otherwise review.", "",
             "| decision | set | n | ECE | reviewed | error on auto-decided | missed threats | false blocks "
             "| error @ review 0% / 10% / 20% |", "|---|---|---|---|---|---|---|---|---|"]
    for dec, sets in report.items():
        for set_name, r in sets.items():
            t, rc = r["triage_0.2_0.9"], {x["reviewed_pct"]: x["error_on_rest"] for x in r["risk_coverage"]}
            lines.append(f"| {dec} | {set_name} | {r['n']} | {r['ece']:.3f} | {t['reviewed']:.1%} "
                         f"| {t['auto_error']:.1%} | {t['missed_threats']:.1%} | {t['false_blocks']:.1%} "
                         f"| {rc[0]:.1%} / {rc[10]:.1%} / {rc[20]:.1%} |")
    out.with_suffix(".md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines))

    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    for dec, sets in report.items():
        fig, (a, b) = plt.subplots(1, 2, figsize=(10, 4.2))
        a.plot([0, 1], [0, 1], color="#999", lw=1, ls="--", label="perfect calibration")
        for set_name, r in sets.items():
            xs = [x["mean_p"] for x in r["reliability"]]
            a.plot(xs, [x["threat_rate"] for x in r["reliability"]], marker="o", ms=4,
                   label=f"{set_name} (ECE {r['ece']:.3f})")
            b.plot([x["reviewed_pct"] for x in r["risk_coverage"]],
                   [100 * x["error_on_rest"] for x in r["risk_coverage"]], marker="o", ms=4,
                   label=set_name)
        a.set(title=f"{dec}: reliability", xlabel="predicted P(threat)", ylabel="observed threat rate",
              xlim=(0, 1), ylim=(0, 1))
        b.set(title=f"{dec}: risk vs review budget", xlabel="% most uncertain sent to review",
              ylabel="% errors on the rest")
        for ax in (a, b):
            ax.grid(alpha=0.3)
            ax.legend(fontsize=8, frameon=False)
        fig.tight_layout()
        fig.savefig(f"{out}_{dec}.png", dpi=130)
        plt.close(fig)


if __name__ == "__main__":
    main()
