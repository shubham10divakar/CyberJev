"""Temperature scaling and calibration metrics."""

import numpy as np
import torch
from sklearn.metrics import f1_score, roc_auc_score


def fit_temperature(logits: torch.Tensor, labels: torch.Tensor) -> float:
    """Fit a single temperature T in [0.05, 20] minimising NLL of softmax(logits / T).

    Falls back to T = 1 if the fit does not improve calibration-set NLL.
    """
    nll = lambda t: torch.nn.functional.cross_entropy(logits / t, labels)  # noqa: E731
    log_t = torch.zeros(1, requires_grad=True)
    opt = torch.optim.LBFGS([log_t], lr=1.0, max_iter=100, line_search_fn="strong_wolfe")

    def closure():
        opt.zero_grad()
        loss = nll(log_t.clamp(-3.0, 3.0).exp())
        loss.backward()
        return loss

    opt.step(closure)
    t = float(log_t.detach().clamp(-3.0, 3.0).exp())
    with torch.no_grad():
        return t if nll(t) < nll(1.0) else 1.0


def fit_threat_only(z: torch.Tensor, labels: torch.Tensor) -> tuple[float, float]:
    """Fit (T, b) so that P(threat) = sigmoid((z - b) / T) for one threat-option logit z
    per example (Platt scaling). T is kept in [0.05, 20], like fit_temperature."""
    z, y = z.float(), labels.float()
    log_t = torch.zeros(1, requires_grad=True)
    b = torch.tensor([float(z.median())], requires_grad=True)
    opt = torch.optim.LBFGS([log_t, b], lr=1.0, max_iter=200, line_search_fn="strong_wolfe")

    def closure():
        opt.zero_grad()
        loss = torch.nn.functional.binary_cross_entropy_with_logits(
            (z - b) / log_t.clamp(-3.0, 3.0).exp(), y)
        loss.backward()
        return loss

    opt.step(closure)
    return float(log_t.detach().clamp(-3.0, 3.0).exp()), float(b.detach())


def threat_only_logits(z: torch.Tensor, b: float) -> torch.Tensor:
    """[n, 2] logits whose softmax at temperature T is (1 - p, p), p = sigmoid((z - b) / T),
    so `metrics(threat_only_logits(z, b), labels, T)` scores the one-pass path."""
    z = z.float()
    return torch.stack([torch.zeros_like(z), z - b], dim=1)


def ece(probs: np.ndarray, labels: np.ndarray, n_bins: int = 15) -> float:
    """Expected calibration error of the top-label confidence."""
    conf = probs.max(1)
    correct = probs.argmax(1) == labels
    edges = np.linspace(0, 1, n_bins + 1)
    total = 0.0
    for lo, hi in zip(edges[:-1], edges[1:]):
        mask = (conf > lo) & (conf <= hi)
        if mask.any():
            total += mask.mean() * abs(correct[mask].mean() - conf[mask].mean())
    return float(total)


def detection_rate(scores: np.ndarray, labels: np.ndarray, max_fpr: float) -> float:
    """Share of positives (label 1) caught at the strictest threshold whose false-positive
    rate on the negatives stays <= max_fpr."""
    neg = np.sort(scores[labels == 0])[::-1]
    k = int(np.floor(max_fpr * len(neg)))  # false positives allowed
    threshold = neg[k] if k < len(neg) else -np.inf
    return float((scores[labels == 1] > threshold).mean())


def metrics(logits: torch.Tensor, labels: torch.Tensor, temperature: float = 1.0) -> dict:
    probs = torch.softmax(logits / temperature, dim=1).numpy()
    y = labels.numpy()
    onehot = np.eye(probs.shape[1])[y]
    binary = {}
    if probs.shape[1] == 2 and 0 < y.sum() < len(y):
        # Security view: option 1 is the threat (attack / injection / phishing).
        binary = {"auroc": float(roc_auc_score(y, probs[:, 1])),
                  "dr_at_1pct_fpr": detection_rate(probs[:, 1], y, 0.01),
                  "dr_at_0.1pct_fpr": detection_rate(probs[:, 1], y, 0.001)}
    return {**binary,
        "n": int(len(y)),
        "accuracy": float((probs.argmax(1) == y).mean()),
        "macro_f1": float(f1_score(y, probs.argmax(1), average="macro")),
        "nll": float(-np.log(np.clip(probs[np.arange(len(y)), y], 1e-12, None)).mean()),
        "brier": float(((probs - onehot) ** 2).sum(1).mean()),
        "ece": ece(probs, y),
    }
