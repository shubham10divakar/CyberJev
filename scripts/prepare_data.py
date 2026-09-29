"""Download datasets and write the in-domain splits and the held-out test set.

    python scripts/prepare_data.py --preset default
        # -> data/{train,calib,test}.jsonl, data_heldout/test.jsonl, data_val/val.jsonl
    python scripts/prepare_data.py --preset v2 --out data_v2   # data v2 exactly (no SQL, no val)

Both are built in one run so held-out examples that also occur in training can be dropped.
"""

import argparse
import json
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from cyberjev.data import build_all  # noqa: E402

PRESETS = {
    "smoke": dict(csic_train=300, csic_calib=100, csic_test=100,
                  web_train=300, web_calib=100, web_test=100,
                  waf_train=300, waf_calib=100, waf_test=100,
                  sqli_heldout=200, reqs_heldout=200),
    # ai-waf has ~9.5k train / 1.2k calib+test after the 80/10/10 split, so it takes them all.
    "v2": dict(csic_train=6000, csic_calib=500, csic_test=1500,
               web_train=6000, web_calib=500, web_test=1500,
               waf_train=10000, waf_calib=600, waf_test=1200,
               sqli_heldout=6000, reqs_heldout=6000),
}
# v3 = v2 + benign SQL (gretel) in train / calib / test + the out-of-domain validation set.
PRESETS["default"] = PRESETS["v3"] = dict(
    PRESETS["v2"], sql_train=3000, sql_calib=200, sql_test=500,
    val_waf_per_class=750, val_spider=1034)
PRESETS["smoke"].update(sql_train=100, sql_calib=50, sql_test=50,
                        val_waf_per_class=50, val_spider=100)


def write(path: Path, examples: list[dict]):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        for ex in examples:
            f.write(json.dumps(ex, ensure_ascii=False) + "\n")
    counts = Counter((ex["source"].split("/")[0], ex["options"][ex["label"]]) for ex in examples)
    print(f"{path}: {len(examples)} examples")
    for (src, lab), c in sorted(counts.items()):
        print(f"    {src:<16} {lab:<8} {c}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--preset", default="default", choices=PRESETS)
    ap.add_argument("--out", default="data")
    ap.add_argument("--heldout-out", default="data_heldout")
    ap.add_argument("--val-out", default="data_val")
    ap.add_argument("--seed", type=int, default=0)
    args = ap.parse_args()

    splits = build_all(PRESETS[args.preset], seed=args.seed)
    for name in ("train", "calib", "test"):
        write(Path(args.out) / f"{name}.jsonl", splits[name])
    write(Path(args.heldout_out) / "test.jsonl", splits["heldout"])
    if "val" in splits:
        write(Path(args.val_out) / "val.jsonl", splits["val"])


if __name__ == "__main__":
    main()
