"""Shared evaluation flow: fit temperature on calib, report test metrics, render tables."""

import json
from pathlib import Path

import torch

from .calibration import fit_temperature, metrics


def read_jsonl(path) -> list[dict]:
    with open(path, encoding="utf-8") as f:
        return [json.loads(line) for line in f]


def by_decision(examples: list[dict]) -> dict[str, list[dict]]:
    groups = {}
    for ex in examples:
        groups.setdefault(ex["decision"], []).append(ex)
    return groups


def labels_of(examples: list[dict]) -> torch.Tensor:
    return torch.tensor([ex["label"] for ex in examples])


def sources_of(examples: list[dict]) -> list[str]:
    """Dataset part of each example's source ("web-attacks/SQLi" -> "web-attacks")."""
    return [ex.get("source", "?").split("/")[0] for ex in examples]


def decision_report(calib_logits, calib_labels, test_logits, test_labels, ms: float,
                    sources: list[str] | None = None) -> dict:
    t = fit_temperature(calib_logits, calib_labels)
    report = {
        "temperature": t,
        "raw": metrics(test_logits, test_labels),
        "calibrated": metrics(test_logits, test_labels, t),
        "ms_per_decision": ms,
    }
    if sources is not None and len(set(sources)) > 1:
        report["by_source"] = {}
        for src in sorted(set(sources)):
            idx = torch.tensor([i for i, s in enumerate(sources) if s == src])
            logits, labels = test_logits[idx], test_labels[idx]
            m = metrics(logits, labels, t)
            flagged = torch.softmax(logits / t, dim=1)[:, 1] > 0.5
            # At the default 0.5 threshold: share of safe examples flagged, of attacks caught.
            m["fpr_at_0.5"] = float(flagged[labels == 0].float().mean()) if (labels == 0).any() else None
            m["dr_at_0.5"] = float(flagged[labels == 1].float().mean()) if (labels == 1).any() else None
            m["threat_share"] = float(labels.float().mean())
            report["by_source"][src] = m
    return report


def render_table(title: str, report: dict) -> str:
    lines = [f"## {title}", "",
             "| decision | n | T | acc | macro-F1 | AUROC | DR@1%FPR | DR@0.1%FPR "
             "| NLL raw → cal | Brier raw → cal | ECE raw → cal | ms/decision |",
             "|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for dec, r in report.items():
        raw, cal = r["raw"], r["calibrated"]
        sec = [f"{cal[k]:.3f}" if k in cal else "-"
               for k in ("auroc", "dr_at_1pct_fpr", "dr_at_0.1pct_fpr")]
        lines.append(
            f"| {dec} | {raw['n']} | {r['temperature']:.2f} | {cal['accuracy']:.3f} "
            f"| {cal['macro_f1']:.3f} | {' | '.join(sec)} | {raw['nll']:.3f} → {cal['nll']:.3f} "
            f"| {raw['brier']:.3f} → {cal['brier']:.3f} | {raw['ece']:.3f} → {cal['ece']:.3f} "
            f"| {r['ms_per_decision']:.1f} |")
    fmt = lambda v: "-" if v is None else f"{v:.3f}"  # noqa: E731
    for dec, r in report.items():
        if "by_source" not in r:
            continue
        lines += ["", f"**{dec} by source** (calibrated; at the default 0.5 threshold, "
                      "FPR = safe examples flagged, DR = threats caught)", "",
                  "| source | n | threat share | AUROC | DR@1%FPR | FPR@0.5 | DR@0.5 | macro-F1 |",
                  "|---|---|---|---|---|---|---|---|"]
        for src, m in r["by_source"].items():
            lines.append(f"| {src} | {m['n']} | {m['threat_share']:.2f} | {fmt(m.get('auroc'))} "
                         f"| {fmt(m.get('dr_at_1pct_fpr'))} | {fmt(m['fpr_at_0.5'])} "
                         f"| {fmt(m['dr_at_0.5'])} | {m['macro_f1']:.3f} |")
    return "\n".join(lines)


def save(report: dict, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(report, indent=2))
