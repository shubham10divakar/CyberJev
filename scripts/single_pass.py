"""Can a binary decision be scored with one encoder pass instead of two? (inference only)

    python scripts/single_pass.py --model runs/cyber-jev-v2-l6 --out results/single_pass_v2_l6.md

Scores both options once, then compares, on the in-domain and held-out test sets:

- two-pass:    softmax([z_safe, z_threat] / T)    (what the Decider does now)
- threat-only: sigmoid((z_threat - b) / T)        (one pass: the threat option)
- safe-only:   sigmoid((-z_safe - b) / T)         (one pass: the safe option)

T (and b) are fitted on <data>/calib.jsonl. No retraining: if AUROC holds, the fast path
needs only the fitted b and T. The one-pass variant is picked by AUROC on the out-of-domain
validation set (--val, default data_val) or, without one, by calib NLL; never by test
results. --save writes it to <model>/one_pass.json for the Decider.
"""

import argparse
import json
import sys
from pathlib import Path

import torch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from cyberjev import model as M  # noqa: E402
from cyberjev.calibration import fit_threat_only, metrics, threat_only_logits  # noqa: E402
from cyberjev.report import (by_decision, decision_report, labels_of, read_jsonl,  # noqa: E402
                            render_table, sources_of)


def variants(logits: torch.Tensor) -> dict[str, torch.Tensor]:
    """Per variant, the score the one-pass path would see (two-pass keeps both logits)."""
    return {"two-pass": logits, "threat-only": logits[:, 1], "safe-only": -logits[:, 0]}


# Option scored and sign of its logit, per one-pass variant (for one_pass.json).
ONE_PASS = {"threat-only": (1, 1.0), "safe-only": (0, -1.0)}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", default="runs/cyber-jev-v2-l6")
    ap.add_argument("--data", default="data")
    ap.add_argument("--heldout", default="data_heldout")
    ap.add_argument("--val", default="data_val", help="folder with val.jsonl ('' for none)")
    ap.add_argument("--max-length", type=int, default=256)
    ap.add_argument("--out", help="write the tables to this .md (and .json)")
    ap.add_argument("--save", action="store_true",
                    help="write the picked one-pass variant to <model>/one_pass.json")
    args = ap.parse_args()

    device = "cuda" if torch.cuda.is_available() else "cpu"
    model, tok = M.load(args.model, device)
    sets = {"calib": Path(args.data) / "calib.jsonl", "in-domain": Path(args.data) / "test.jsonl",
            "held-out": Path(args.heldout) / "test.jsonl"}
    if args.val and (Path(args.val) / "val.jsonl").exists():
        sets["val"] = Path(args.val) / "val.jsonl"
    data = {k: by_decision(read_jsonl(p)) for k, p in sets.items()}

    sections, report, one_pass = [], {}, {}
    for dec in sorted(data["in-domain"]):
        scored = {k: torch.stack(M.score(model, tok, d[dec], args.max_length, device))
                  for k, d in data.items()}
        calib_y = labels_of(data["calib"][dec])
        cal_v = variants(scored["calib"])
        for test in [k for k in sets if k != "calib"]:
            test_v, rows = variants(scored[test]), {}
            for name, c in cal_v.items():
                t = test_v[name]
                b = 0.0
                if c.dim() == 1:
                    _, b = fit_threat_only(c, calib_y)
                    c, t = threat_only_logits(c, b), threat_only_logits(t, b)
                rows[name] = decision_report(c, calib_y, t, labels_of(data[test][dec]), 0.0,
                                             sources_of(data[test][dec]))
                rows[name]["shift_b"] = b
                rows[name]["calib_nll"] = metrics(c, calib_y, rows[name]["temperature"])["nll"]
            report.setdefault(dec, {})[test] = rows
            if test == ("val" if "val" in sets else "in-domain"):
                if test == "val":
                    pick = max(ONE_PASS, key=lambda v: rows[v]["calibrated"]["auroc"])
                else:
                    pick = min(ONE_PASS, key=lambda v: rows[v]["calib_nll"])
                option, sign = ONE_PASS[pick]
                one_pass[dec] = {"variant": pick, "option": option, "sign": sign,
                                 "temperature": rows[pick]["temperature"],
                                 "shift": rows[pick]["shift_b"],
                                 "picked_by": "val AUROC" if test == "val" else "calib NLL"}
            for name, r in rows.items():
                sections.append(render_table(f"{dec}, {test} — {name} (b = {r['shift_b']:.2f})",
                                             {dec: r}))

    summary = [f"## One pass vs two — `{args.model}`, max_length {args.max_length}", "",
               "| decision | test set | variant | T | b | calib NLL | AUROC | DR@1%FPR | NLL | ECE |",
               "|---|---|---|---|---|---|---|---|---|---|"]
    for dec, tests in report.items():
        for test, rows in tests.items():
            for name, r in rows.items():
                c = r["calibrated"]
                summary.append(f"| {dec} | {test} | {name} | {r['temperature']:.2f} "
                               f"| {r['shift_b']:.2f} | {r['calib_nll']:.3f} | {c['auroc']:.3f} "
                               f"| {c['dr_at_1pct_fpr']:.3f} | {c['nll']:.3f} | {c['ece']:.3f} |")
    summary += ["", "One-pass variant picked: " + ", ".join(
        f"{dec} → {p['variant']} (by {p['picked_by']})" for dec, p in one_pass.items())]
    text = "\n".join(summary) + "\n\n" + "\n\n".join(sections)
    print(text)
    if args.out:
        Path(args.out).write_text(text + "\n", encoding="utf-8")
        Path(args.out).with_suffix(".json").write_text(json.dumps(report, indent=2))
    if args.save:
        (Path(args.model) / "one_pass.json").write_text(json.dumps(one_pass, indent=2))
        print(f"saved one_pass.json to {args.model}")


if __name__ == "__main__":
    main()
