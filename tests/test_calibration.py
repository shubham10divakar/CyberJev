import pytest
import torch

pytest.importorskip("sklearn")  # calibration metrics need the `train` extra

from cyberjev.calibration import (detection_rate, ece, fit_temperature,  # noqa: E402
                                  fit_threat_only, metrics, threat_only_logits)


def test_fit_temperature_recovers_known_temperature():
    # Labels are sampled from softmax(z / 2), so the best temperature for logits z is ~2.
    torch.manual_seed(0)
    z = torch.randn(20000, 3) * 3
    labels = torch.multinomial(torch.softmax(z / 2.0, dim=1), 1).squeeze(1)
    assert fit_temperature(z, labels) == pytest.approx(2.0, rel=0.1)


def test_fit_temperature_falls_back_to_one_on_noise():
    torch.manual_seed(0)
    z = torch.zeros(100, 2)
    labels = torch.randint(0, 2, (100,))
    assert fit_temperature(z, labels) == 1.0


def test_metrics_on_perfect_predictions():
    logits = torch.tensor([[10.0, -10.0], [-10.0, 10.0]] * 50)
    labels = torch.tensor([0, 1] * 50)
    m = metrics(logits, labels)
    assert m["accuracy"] == 1.0 and m["macro_f1"] == 1.0
    assert m["ece"] < 1e-3 and m["nll"] < 1e-3


def test_ece_of_overconfident_model():
    import numpy as np
    probs = np.array([[0.99, 0.01]] * 100)  # 99% confident, right half the time
    labels = np.array([0, 1] * 50)
    assert ece(probs, labels) == pytest.approx(0.49, abs=0.01)


def test_detection_rate_at_fixed_fpr():
    import numpy as np
    neg = np.linspace(0.0, 0.5, 100)           # negatives score 0 .. 0.5
    pos = np.array([0.2, 0.45, 0.6, 0.9])      # half the positives score above every negative
    scores = np.concatenate([neg, pos])
    labels = np.array([0] * 100 + [1] * 4)
    assert detection_rate(scores, labels, 0.0) == 0.5     # no false positives allowed
    assert detection_rate(scores, labels, 0.2) == 0.75    # 20 FPs allowed: threshold ~0.4


def test_metrics_include_security_view_for_binary():
    logits = torch.tensor([[0.0, 3.0], [0.0, -3.0]] * 50)
    m = metrics(logits, torch.tensor([1, 0] * 50))
    assert m["auroc"] == 1.0 and m["dr_at_1pct_fpr"] == 1.0


def test_fit_threat_only_recovers_known_shift_and_temperature():
    # Labels are sampled from sigmoid((z - 1.5) / 2), so the fit should find T ~ 2, b ~ 1.5.
    torch.manual_seed(0)
    z = torch.randn(40000) * 4
    labels = torch.bernoulli(torch.sigmoid((z - 1.5) / 2.0)).long()
    t, b = fit_threat_only(z, labels)
    assert t == pytest.approx(2.0, rel=0.1) and b == pytest.approx(1.5, abs=0.2)
    probs = torch.softmax(threat_only_logits(z, b) / t, dim=1)[:, 1]
    assert torch.allclose(probs, torch.sigmoid((z - b) / t), atol=1e-6)
