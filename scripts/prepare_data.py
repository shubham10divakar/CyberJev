"""Download datasets and write train / calib / test JSONL files.

    python scripts/prepare_data.py --preset default              # -> data/{train,calib,test}.jsonl
    python scripts/prepare_data.py --heldout --out data_heldout  # -> data_heldout/test.jsonl
"""

import argparse
import json
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from cyberjev.data import build_all, build_heldout  # noqa: E402

PRESETS = {
    "smoke": dict(http_train=500, http_calib=200, http_test=200),
    "default": dict(http_train=10000, http_calib=1500, http_test=3000),
}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--preset", default="default", choices=PRESETS)
    ap.add_argument("--out", default="data")
    ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("--heldout", action="store_true",
                    help="build the held-out test set (datasets never used in training)")
    args = ap.parse_args()

    if args.heldout:
        splits = {"test": build_heldout(seed=args.seed)}
    else:
        splits = build_all(PRESETS[args.preset], seed=args.seed)
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    for name, examples in splits.items():
        with open(out / f"{name}.jsonl", "w", encoding="utf-8") as f:
            for ex in examples:
                f.write(json.dumps(ex, ensure_ascii=False) + "\n")
        counts = Counter((ex["decision"], ex["options"][ex["label"]]) for ex in examples)
        print(f"{name}: {len(examples)} examples")
        for (dec, lab), c in sorted(counts.items()):
            print(f"    {dec:<17} {lab:<12} {c}")


if __name__ == "__main__":
    main()
