"""TF-IDF baseline on the same train / calib / test split as Cyber-Jev.

Character 1-5-gram TF-IDF + logistic regression, trained on <data>/train.jsonl, one model
per decision. Its log-odds go through the same temperature scaling and metrics as
Cyber-Jev, so the tables are directly comparable.

    python scripts/baselines.py                                         # in-domain test
    python scripts/baselines.py --test-data data_heldout --name tfidf_heldout
    python scripts/baselines.py --test-data data_val --test-file val.jsonl --name tfidf_val
    python scripts/baselines.py --length --test-data data_heldout --name length_heldout   # shortcut check

--length replaces the model with the text length alone (log characters, LR-fitted on train):
a shortcut baseline that any real model has to beat.
"""

import argparse
import sys
import time
from pathlib import Path

import torch
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from cyberjev.report import (by_decision, decision_report, labels_of, read_jsonl,  # noqa: E402
                             render_table, save, sources_of)


def as_logits(clf, X) -> torch.Tensor:
    """Binary log-odds z -> two-option logits [0, z]."""
    z = torch.tensor(clf.decision_function(X), dtype=torch.float32)
    return torch.stack([torch.zeros_like(z), z], dim=1)


class LengthFeature:
    """log(1 + characters) as the only feature, with the TfidfVectorizer interface we use."""

    def fit_transform(self, texts):
        return self.transform(texts)

    def transform(self, texts):
        import numpy as np
        return np.log1p(np.array([[len(t)] for t in texts], dtype=float))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--data", default="data", help="folder with train.jsonl and calib.jsonl")
    ap.add_argument("--test-data", help="folder with the test.jsonl to report on (default: --data)")
    ap.add_argument("--test-file", default="test.jsonl")
    ap.add_argument("--length", action="store_true", help="length-only baseline instead of TF-IDF")
    ap.add_argument("--decisions", nargs="*", help="only these decisions (default: all in the test set)")
    ap.add_argument("--name", default="tfidf")
    ap.add_argument("--results-dir", default="results")
    args = ap.parse_args()

    train = by_decision(read_jsonl(Path(args.data) / "train.jsonl"))
    calib = by_decision(read_jsonl(Path(args.data) / "calib.jsonl"))
    test = by_decision(read_jsonl(Path(args.test_data or args.data) / args.test_file))

    report = {}
    for dec in sorted(test):
        if args.decisions and dec not in args.decisions:
            continue
        if args.length:
            vec = LengthFeature()
        else:
            vec = TfidfVectorizer(analyzer="char", ngram_range=(1, 5), min_df=2, sublinear_tf=True,
                                  max_features=200_000)
        X = vec.fit_transform([ex["state"] for ex in train[dec]])
        clf = LogisticRegression(C=10.0, max_iter=2000).fit(X, labels_of(train[dec]).numpy())

        states = [ex["state"] for ex in test[dec]]
        t0 = time.time()
        t_logits = as_logits(clf, vec.transform(states))
        ms = 1000 * (time.time() - t0) / len(states)
        c_logits = as_logits(clf, vec.transform([ex["state"] for ex in calib[dec]]))
        report[dec] = decision_report(c_logits, labels_of(calib[dec]),
                                      t_logits, labels_of(test[dec]), ms,
                                      sources_of(test[dec]))

    kind = "Length only" if args.length else "TF-IDF + LR"
    table = render_table(f"{kind} on `{args.test_data or args.data}/{args.test_file}`", report)
    print(table)
    out = Path(args.results_dir)
    save(report, out / f"{args.name}.json")
    (out / f"{args.name}.md").write_text(table + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
