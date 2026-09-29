"""Cyber-Jev scorer: a cross-encoder that gives one logit per (question, option, state).

A decision's options are scored independently and softmaxed together, so option order
does not matter and new option sets work without retraining.
"""

import torch
import torch.nn.functional as F
from transformers import AutoModelForSequenceClassification, AutoTokenizer

DEFAULT_BASE = "cross-encoder/ms-marco-MiniLM-L6-v2"


TRUNCATIONS = ("head", "head_tail")


def load_tokenizer(name_or_path: str, truncation: str | None = None):
    """Tokenizer plus the model's truncation mode (`cyberjev_truncation`), read from
    cyberjev_config.json ("truncation") unless given. Models without it use "head"."""
    import json
    from pathlib import Path

    tok = AutoTokenizer.from_pretrained(name_or_path)
    if truncation is None:
        cfg = Path(name_or_path) / "cyberjev_config.json"
        truncation = json.loads(cfg.read_text()).get("truncation", "head") if cfg.exists() else "head"
    if truncation not in TRUNCATIONS:
        raise ValueError(f"truncation must be one of {TRUNCATIONS}, not {truncation!r}")
    tok.cyberjev_truncation = truncation
    return tok


def _head_tail(tok, first: str, state: str, max_length: int) -> str:
    """If state doesn't fit, keep its first and last halves of the token budget (joined by
    " ... "), so both an opening persona and an appended instruction stay visible."""
    budget = max_length - len(tok(first)["input_ids"]) - 1          # [CLS] first [SEP] state [SEP]
    enc = tok(state, add_special_tokens=False, return_offsets_mapping=True)
    offsets = enc["offset_mapping"]
    if len(offsets) <= budget or budget < 8:
        return state
    head = (budget - 4) // 2                                        # " ... " costs 3 tokens
    tail = budget - 4 - head
    return state[: offsets[head - 1][1]] + " ... " + state[offsets[-tail][0]:]


def load(name_or_path: str, device: str | torch.device, truncation: str | None = None):
    tok = load_tokenizer(name_or_path, truncation)
    model = AutoModelForSequenceClassification.from_pretrained(
        name_or_path, num_labels=1, ignore_mismatched_sizes=True
    )
    return model.to(device), tok


def encode(tok, items: list[dict], max_length: int):
    """Flatten items into (question+option, state) pairs.

    Returns the tokenized batch and, per pair, its item index and option position.
    """
    firsts, seconds, group_idx, pos_idx = [], [], [], []
    head_tail = getattr(tok, "cyberjev_truncation", "head") == "head_tail"
    for g, item in enumerate(items):
        for p, opt in enumerate(item["options"]):
            first = f"question: {item['question']} option: {opt}"
            firsts.append(first)
            seconds.append(_head_tail(tok, first, item["state"], max_length) if head_tail
                           else item["state"])
            group_idx.append(g)
            pos_idx.append(p)
    enc = tok(
        firsts,
        seconds,
        truncation="only_second",
        max_length=max_length,
        padding=True,
        return_tensors="pt",
    )
    return enc, torch.tensor(group_idx), torch.tensor(pos_idx)


def group_logits(model, enc, group_idx, pos_idx, n_groups: int) -> torch.Tensor:
    """Run the encoder and return [n_groups, max_options] logits, padded with -inf."""
    flat = model(**enc).logits.squeeze(-1).float()
    out = torch.full((n_groups, int(pos_idx.max()) + 1), float("-inf"), device=flat.device)
    out[group_idx.to(flat.device), pos_idx.to(flat.device)] = flat
    return out


def grouped_loss(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return F.cross_entropy(logits, labels.to(logits.device))


@torch.no_grad()
def score(model, tok, items: list[dict], max_length: int, device, batch_size: int = 32):
    """Return a list of 1-D logit tensors (CPU), one per item."""
    model.eval()
    results = []
    for i in range(0, len(items), batch_size):
        chunk = items[i : i + batch_size]
        enc, g, p = encode(tok, chunk, max_length)
        enc = {k: v.to(device) for k, v in enc.items()}
        with torch.autocast(device_type=str(device).split(":")[0], dtype=torch.bfloat16,
                            enabled=str(device).startswith("cuda")):
            logits = group_logits(model, enc, g, p, len(chunk))
        for row, item in zip(logits.cpu(), chunk):
            results.append(row[: len(item["options"])])
    return results
