"""Shared fixtures: a tiny random model folder (no download) and an isolated config home."""

import json

import pytest

WORDS = ["question", "option", "is", "this", "http", "request", "a", "web", "attack", "safe",
         "text", "injection", "url", "phishing", "legitimate", "or", "malicious", "get", "login",
         "user", "admin", "search", "ignore", "previous", "instructions", "/", "?", "=", "'", "."]


@pytest.fixture(scope="session")
def tiny_model_dir(tmp_path_factory):
    """A 1-layer BERT cross-encoder saved like a real Cyber-Jev release folder."""
    from transformers import BertConfig, BertForSequenceClassification, BertTokenizer

    folder = tmp_path_factory.mktemp("tiny-cyber-jev")
    vocab = ["[PAD]", "[UNK]", "[CLS]", "[SEP]", "[MASK]", *WORDS]
    (folder / "vocab.txt").write_text("\n".join(vocab), encoding="utf-8")
    BertTokenizer(vocab_file=str(folder / "vocab.txt")).save_pretrained(folder)

    config = BertConfig(vocab_size=len(vocab), hidden_size=16, num_hidden_layers=1,
                        num_attention_heads=2, intermediate_size=32, num_labels=1)
    BertForSequenceClassification(config).save_pretrained(folder)

    (folder / "cyberjev_config.json").write_text(json.dumps(
        {"model_name": "cyber-jev", "version": "0.0-test", "max_length": 128}))
    (folder / "calibration.json").write_text(json.dumps(
        {"http_attack": 1.5, "prompt_injection": 1.2, "phishing_url": 1.1}))
    return folder


@pytest.fixture
def isolated_home(tmp_path, monkeypatch):
    """Keep `cyber-jev use` choices out of the real ~/.cyberjev."""
    monkeypatch.setenv("CYBERJEV_HOME", str(tmp_path / "home"))
    monkeypatch.delenv("CYBERJEV_MODEL", raising=False)
    return tmp_path / "home"


@pytest.fixture(scope="session")
def decider(tiny_model_dir):
    from cyberjev import Decider
    return Decider.from_pretrained(str(tiny_model_dir), device="cpu")
