"""Mean ± std over seeds of AUROC (and per-source AUROC / FPR@0.5) from results/*.json.

    python scripts/seed_summary.py --runs v5_l6 v5_l6_s1 v5_l6_s2 --runs v6_l6 v6_l6_s1 v6_l6_s2 \
        --out results/seeds_v5_v6.md

Each --runs group is one setup (its seeds); tags are results/cyberjev_<tag>{,_heldout,_val}.json.
"""

import argparse
import json
import statistics
from pathlib import Path

SETS = [("", "in-domain"), ("_heldout", "held-out"), ("_val", "val")]


def load(tag: str, suffix: str) -> dict:
    p = Path("results") / f"cyberjev_{tag}{suffix}.json"
    return json.loads(p.read_text()) if p.exists() else {}


def fmt(values: list) -> str:
    values = [v for v in values if v is not None]
    if not values:
        return "-"
    if len(values) == 1:
        return f"{values[0]:.3f}"
    return f"{statistics.mean(values):.3f} ± {statistics.stdev(values):.3f}"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--runs", nargs="+", action="append", required=True,
                    help="result tags of one setup's seeds (repeat for each setup)")
    ap.add_argument("--out")
    args = ap.parse_args()

    groups = {g[0].rsplit("_s", 1)[0] if "_s" in g[0] else g[0]: g for g in args.runs}
    decisions = sorted({d for g in args.runs for t in g for d in load(t, "")})
    lines = ["## Seeds: mean ± std of calibrated AUROC (two-pass)", "",
             "| decision | set | " + " | ".join(f"{k} (n={len(g)})" for k, g in groups.items()) + " |",
             "|---|---|" + "---|" * len(groups)]
    for dec in decisions:
        for suffix, name in SETS:
            cells = [fmt([load(t, suffix).get(dec, {}).get("calibrated", {}).get("auroc")
                          for t in g]) for g in groups.values()]
            lines.append(f"| {dec} | {name} | " + " | ".join(cells) + " |")
    lines += ["", "### By source (held-out and val): AUROC, and FPR@0.5 on safe examples", "",
              "| decision | source | " + " | ".join(f"{k} AUROC | {k} FPR@0.5" for k in groups) + " |",
              "|---|---|" + "---|---|" * len(groups)]
    for dec in decisions:
        for suffix in ("_heldout", "_val"):
            sources = sorted({s for g in groups.values() for t in g
                              for s in load(t, suffix).get(dec, {}).get("by_source", {})})
            for src in sources:
                cells = []
                for g in groups.values():
                    ms = [load(t, suffix).get(dec, {}).get("by_source", {}).get(src, {}) for t in g]
                    cells += [fmt([m.get("auroc") for m in ms]), fmt([m.get("fpr_at_0.5") for m in ms])]
                lines.append(f"| {dec} | {src} | " + " | ".join(cells) + " |")
    table = "\n".join(lines)
    print(table)
    if args.out:
        Path(args.out).write_text(table + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
