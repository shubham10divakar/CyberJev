"""Build typed security-decision examples from public datasets.

Each example: {decision, question, options, state, label, source}.
`source` is "<dataset>/<subtype>", e.g. "web-attacks/SQLi"; reports group by <dataset>.
"""

import random

from datasets import load_dataset

from .schema import DECISIONS, normalize_http, normalize_url, url_host

# Training sources: calib and test come from the same sources (in-domain).
CSIC = "bridge4/CSIC2010_dataset_classification"   # HTTP requests to one shop, 0 normal / 1 anomalous
WEB_ATTACKS = "shengqin/web-attacks"                # payloads, text_label normal / XSS / SQLi
AI_WAF = "notesbymuneeb/ai-waf-dataset"             # full HTTP requests, many hosts, benign / malicious
# Held-out sources: never trained on, only for final reporting.
SQLI = "zrmarine/sql_injection"                     # SQL queries and payloads, 0 benign / 1 injection
WEB_ATTACK_REQS = "vyykaaa/dataset-web-attack"      # DVWA + Juice Shop requests, normal / anomalous
# Data v3 additions. Built with their own rng after the sources above, so v2's splits and the
# held-out set stay byte-identical.
GRETEL_SQL = "gretelai/synthetic_text_to_sql"       # benign SQL (training hard negatives), Apache-2.0
# Validation sources: out-of-domain, never trained on or tested on; only for choices.
WAF_V2 = "puyang2025/waf_data_v2"                   # full requests, normal / anomalous, MIT
SPIDER = "xlangai/spider"                           # human-written SQL, all benign, CC-BY-SA-4.0

# prompt_injection (M3). Own rng; held-out and val are built first and training skips their texts.
PI_SLABS = "S-Labs/prompt-injection-dataset"        # direct injections / guideline leaks vs questions, MIT
PI_NEURAL = "neuralchemy/Prompt-injection-dataset"  # incl. HackAPrompt, grouped splits, Apache-2.0
PI_DEEPSET = "deepset/prompt-injections"            # held-out: small, multilingual, Apache-2.0
PI_JACKHHAO = "jackhhao/jailbreak-classification"   # held-out: role-play jailbreaks vs benign personas, Apache-2.0
PI_WILD = "TrustAIRLab/in-the-wild-jailbreak-prompts"  # val: in-the-wild jailbreak vs regular prompts, MIT
# (SPML chatbot prompts were rejected for val: text length alone separates its labels, AUROC 1.00.)

# phishing_url (M3). Hosts in held-out / val are kept out of training (not just exact URLs).
URL_FLWR = "flwrlabs/fed-phishing-urls"             # merged URL sets, 1.1M, 0 legit / 1 phishing, Apache-2.0
URL_PHISHTRAP = "saidutta69/PhishTrap"              # held-out: Tranco top domains vs Phishing.Database, 2026, MIT
URL_DESTROYLIST = "phishdestroy/destroylist"        # held-out: phishing domains only, MIT
URL_JPXXX = "JPxxx/url-benchmark-dataset"           # val: benign / malicious URLs, Apache-2.0


def _example(decision: str, label: int, state: str, source: str) -> dict:
    d = DECISIONS[decision]
    return {"decision": decision, "question": d.question, "options": list(d.options),
            "state": state, "label": label, "source": source}


def _dedup(rows):
    """rows: (text, label, source). Keep the first of each text."""
    seen, out = set(), []
    for row in rows:
        if row[0] not in seen:
            seen.add(row[0])
            out.append(row)
    return out


def csic_to_text(raw: str) -> str:
    """Keep the request line and body. CSIC's headers are the same on every request, bar a
    random session cookie that would make near-duplicate requests look unique."""
    head, _, body = raw.partition("\n")          # the body follows the only real newline
    request_line = head.split("\\n", 1)[0]       # headers are joined by a literal "\n"
    return normalize_http(request_line + ("\n\n" + body if body.strip() else ""))


def _csic(split):
    return [(csic_to_text(r["requests"]), int(r["label"]),
             f"csic2010/{'anomalous' if r['label'] else 'normal'}")
            for r in load_dataset(CSIC, split=split)]


def _web_attacks(split):
    return [(normalize_http(r["Payload"]), int(r["Label"] != 0), f"web-attacks/{r['text_label']}")
            for r in load_dataset(WEB_ATTACKS, split=split)]


def _ai_waf():
    return [(normalize_http(r["text"]), int(r["label"] == "malicious"), f"ai-waf/{r['label']}")
            for r in load_dataset(AI_WAF, split="train")]


def http_attack_splits(sizes: dict, rng: random.Random) -> dict[str, list[tuple]]:
    """Three sources, each split so no text is in more than one split.

    CSIC and web-attacks: train from their train split, calib / test from their test split.
    ai-waf has one split: 80 / 10 / 10 at random.
    """
    out = {"train": [], "calib": [], "test": []}
    seen = set()
    for name, train_rows, rest_rows in [
        ("csic", _csic("train"), _csic("test")),
        ("web", _web_attacks("train"), _web_attacks("test")),
        ("waf", None, None),
    ]:
        if train_rows is None:
            rows = _dedup(r for r in _ai_waf() if r[0] not in seen)
            rng.shuffle(rows)
            n = len(rows)
            train_rows, rest_rows = rows[: int(0.8 * n)], rows[int(0.8 * n):]
        train_rows = _dedup(r for r in train_rows if r[0] not in seen)
        seen |= {r[0] for r in train_rows}
        rest_rows = _dedup(r for r in rest_rows if r[0] not in seen)
        seen |= {r[0] for r in rest_rows}
        rng.shuffle(train_rows)
        rng.shuffle(rest_rows)
        n_cal, n_test = sizes[f"{name}_calib"], sizes[f"{name}_test"]
        out["train"] += train_rows[: sizes[f"{name}_train"]]
        out["calib"] += rest_rows[:n_cal]
        out["test"] += rest_rows[n_cal: n_cal + n_test]
    return out


def http_attack_heldout(sizes: dict, rng: random.Random, exclude: set[str]) -> list[tuple]:
    """Sources never used in training; any text also in `exclude` (the training texts) is dropped."""
    sqli = _dedup((normalize_http(r["Query"]), int(r["Label"]), f"sqli-queries/{r['Label']}")
                  for r in load_dataset(SQLI, split="train"))
    reqs = _dedup((normalize_http(r["raw_request"]), int(r["label"] == "anomalous"),
                   f"dvwa-juiceshop/{r['attack_type'] or 'normal'}")
                  for r in load_dataset(WEB_ATTACK_REQS, split="test")
                  if r["label"] in ("normal", "anomalous") and r["raw_request"]
                  and r["raw_request"][:1].isupper() and " HTTP/" in r["raw_request"])
    out = []
    for rows, n in [(sqli, sizes["sqli_heldout"]), (reqs, sizes["reqs_heldout"])]:
        rows = [r for r in rows if r[0] not in exclude]
        rng.shuffle(rows)
        out += rows[:n]
    return out


def benign_sql_splits(sizes: dict, rng: random.Random, exclude: set[str]) -> dict[str, list]:
    """Benign SQL labelled safe: train from gretel's train split, calib / test from its test split."""
    out = {}
    for split, names in [("train", ["train"]), ("test", ["calib", "test"])]:
        rows = _dedup((normalize_http(r["sql"]), 0, f"gretel-sql/{r['sql_task_type']}")
                      for r in load_dataset(GRETEL_SQL, split=split))
        rows = [r for r in rows if r[0] not in exclude]
        rng.shuffle(rows)
        start = 0
        for name in names:
            n = sizes[f"sql_{name}"]
            out[name], start = rows[start: start + n], start + n
    return out


def _waf_v2_text(r) -> str:
    body = "" if r["body"] in (None, "None") else r["body"]
    return normalize_http(f"{r['method']} {r['url']} {r['protocol']}\n{r['headers']}"
                          + (f"\n\n{body}" if body.strip() else ""))


def validation_set(sizes: dict, rng: random.Random, exclude: set[str]) -> list[tuple]:
    """Out-of-domain validation: waf-v2 requests, balanced per class within each of its two
    main hosts (so the Host header carries no label), and Spider dev queries (all safe)."""
    import re

    per = sizes["val_waf_per_class"]
    ds = load_dataset(WAF_V2, split="test")
    idx = list(range(len(ds)))
    rng.shuffle(idx)
    want = {(h, lab): per for h in ("test-site.com", "localhost:8080") for lab in (0, 1)}
    rows, seen = [], set(exclude)
    for i in idx:
        if not any(want.values()):
            break
        r = ds[i]
        host = re.search(r"^Host: (\S+)", r["headers"] or "", re.M)
        key = (host.group(1) if host else "?", int(r["label"] == "anomalous"))
        if want.get(key):
            text = _waf_v2_text(r)
            if text not in seen:
                seen.add(text)
                rows.append((text, key[1], f"waf-v2/{key[0]}"))
                want[key] -= 1
    spider = _dedup((normalize_http(r["query"]), 0, f"spider/{r['db_id']}")
                    for r in load_dataset(SPIDER, split="validation"))
    spider = [r for r in spider if r[0] not in seen]
    rng.shuffle(spider)
    return rows + spider[: sizes["val_spider"]]


def _prompt(text) -> str:
    return (text or "").strip()


def prompt_injection_all(sizes: dict, rng: random.Random, exclude: set[str]) -> dict[str, list]:
    """{"train", "calib", "test", "heldout", "val"} rows for prompt_injection."""
    def rows(repo, split, text_col, label_fn, name, sub=lambda r: ""):
        return [(_prompt(r[text_col]), label_fn(r), f"{name}/{sub(r) or ('injection' if label_fn(r) else 'safe')}")
                for r in load_dataset(repo, split=split) if _prompt(r[text_col])]

    heldout = _dedup(rows(PI_DEEPSET, "train", "text", lambda r: int(r["label"]), "deepset")
                     + rows(PI_DEEPSET, "test", "text", lambda r: int(r["label"]), "deepset")
                     + rows(PI_JACKHHAO, "train", "prompt", lambda r: int(r["type"] == "jailbreak"), "jackhhao")
                     + rows(PI_JACKHHAO, "test", "prompt", lambda r: int(r["type"] == "jailbreak"), "jackhhao"))
    heldout = [r for r in heldout if r[0] not in exclude]
    used = exclude | {r[0] for r in heldout}

    # Val: jailbreak vs regular prompts, equal counts per length band so length says nothing.
    import bisect

    bands = [0, 100, 200, 400, 800, 1600, 3200, 10**9]
    wild = {}
    for config, label in [("jailbreak_2023_12_25", 1), ("regular_2023_12_25", 0)]:
        for r in load_dataset(PI_WILD, config, split="train"):
            text = _prompt(r["prompt"])
            if text and text not in used and text not in wild:
                wild[text] = label
    by_band = {}
    for text, label in wild.items():
        by_band.setdefault((bisect.bisect_right(bands, len(text)), label), []).append(text)
    val = []
    for band in sorted({b for b, _ in by_band}):
        pos, neg = by_band.get((band, 1), []), by_band.get((band, 0), [])
        rng.shuffle(pos)
        rng.shuffle(neg)
        n = min(len(pos), len(neg))
        val += [(t, 1, "in-the-wild/jailbreak") for t in pos[:n]]
        val += [(t, 0, "in-the-wild/regular") for t in neg[:n]]
    rng.shuffle(val)
    per = sizes["pi_val_per_class"]
    val = [r for r in val if r[1] == 1][:per] + [r for r in val if r[1] == 0][:per]
    used |= {r[0] for r in val}

    out = {"train": [], "calib": [], "test": [], "heldout": heldout, "val": val}
    for repo, name, key in [(PI_SLABS, "s-labs", "slabs"), (PI_NEURAL, "neuralchemy", "neural")]:
        sub = (lambda r: r["category"]) if repo == PI_NEURAL else (lambda r: "")
        for split, target in [("train", "train"), ("validation", "calib"), ("test", "test")]:
            part = _dedup(r for r in rows(repo, split, "text", lambda r: int(r["label"]), name, sub)
                          if r[0] not in used)
            used |= {r[0] for r in part}
            rng.shuffle(part)
            out[target] += part[: sizes[f"pi_{key}_{target}"]]
    return out


def _balanced_by_path(rows, per: int, rng: random.Random, name: str) -> list[tuple]:
    """rows: (url, label). Take `per` of each label among URLs with a path and among bare
    domains, so "has a path" says nothing about the label."""
    rows = list(rows)
    rng.shuffle(rows)
    want = {(p, y): per for p in (False, True) for y in (0, 1)}
    out, seen = [], set()
    for url, y in rows:
        text = normalize_url(url)
        key = ("/" in text, y)
        if want.get(key) and text and text not in seen:
            seen.add(text)
            out.append((text, y, f"{name}/{'phishing' if y else 'legitimate'}"))
            want[key] -= 1
    return out


def phishing_url_all(sizes: dict, rng: random.Random) -> dict[str, list]:
    """{"train", "calib", "test", "heldout", "val"} rows for phishing_url."""
    import pandas as pd
    from huggingface_hub import hf_hub_download

    def fetch(repo, filename):
        return hf_hub_download(repo, filename, repo_type="dataset")

    trap = pd.read_csv(fetch(URL_PHISHTRAP, "data/phishtrap_full.csv"))
    trap_rows = _dedup((normalize_url(u), int(y), f"phishtrap/{'phishing' if y else 'legitimate'}")
                       for u, y in zip(trap["url"], trap["label"]))
    rng.shuffle(trap_rows)
    per = sizes["url_phishtrap_per_class"]
    heldout = [r for r in trap_rows if r[1] == 1][:per] + [r for r in trap_rows if r[1] == 0][:per]
    with open(fetch(URL_DESTROYLIST, "urls.txt"), encoding="utf-8") as f:
        destroy = _dedup((normalize_url(u), 1, "destroylist/phishing") for u in f if u.strip())
    trap_hosts = {url_host(r[0]) for r in trap_rows}
    destroy = [r for r in destroy if url_host(r[0]) not in trap_hosts]
    rng.shuffle(destroy)
    heldout += destroy[: sizes["url_destroylist"]]
    blocked = {url_host(r[0]) for r in heldout}

    jp = pd.read_parquet(fetch(URL_JPXXX, "data/train-00000-of-00001.parquet"))
    jp = jp.sample(n=min(len(jp), 300_000), random_state=rng.randrange(2**31))
    jp_rows = [(u, int(y == "malicious")) for u, y in zip(jp["url"], jp["label"])
               if url_host(u) not in blocked]
    val = _balanced_by_path(jp_rows, sizes["url_val_per_cell"], rng, "jpxxx")
    blocked |= {url_host(r[0]) for r in val}

    out = {"heldout": heldout, "val": val}
    for split, targets in [("train", [("train", "url_train_per_cell"), ("calib", "url_calib_per_cell")]),
                           ("test", [("test", "url_test_per_cell")])]:
        ds = load_dataset(URL_FLWR, split=split)
        rows = [(u, int(y)) for u, y in zip(ds["url"], ds["label"]) if url_host(u) not in blocked]
        for target, key in targets:
            part = _balanced_by_path(rows, sizes[key], rng, "flwrlabs")
            out[target] = part
            used = {r[0] for r in part}
            rows = [r for r in rows if normalize_url(r[0]) not in used]
    # flwrlabs' train and test splits share URLs: keep test and calib apart from train.
    train_texts = {r[0] for r in out["train"]}
    out["calib"] = [r for r in out["calib"] if r[0] not in train_texts]
    out["test"] = [r for r in out["test"] if r[0] not in train_texts | {r[0] for r in out["calib"]}]
    return out


def _examples(rows, decision: str = "http_attack"):
    return [_example(decision, y, t, s) for t, y, s in rows]


def build_all(sizes: dict, seed: int = 0) -> dict[str, list[dict]]:
    """Return {"train", "calib", "test", "heldout"} example lists."""
    rng = random.Random(seed)
    splits = http_attack_splits(sizes, rng)
    exclude = {t for rows in splits.values() for t, _, _ in rows}
    splits["heldout"] = http_attack_heldout(sizes, rng, exclude)
    # v3 sources: their own rng, and nothing that is already in any split (held-out included).
    used = exclude | {t for t, _, _ in splits["heldout"]}
    extra = random.Random(f"{seed}-v3")
    if sizes.get("sql_train"):
        sql = benign_sql_splits(sizes, extra, used)
        for name, rows in sql.items():
            splits[name] += rows
            used |= {t for t, _, _ in rows}
    if sizes.get("val_waf_per_class"):
        splits["val"] = validation_set(sizes, extra, used)
    rng.shuffle(splits["train"])
    out = {name: _examples(rows) for name, rows in splits.items()}

    # Other decisions (M3): each with its own rng, appended after http_attack.
    others = []
    if sizes.get("pi_slabs_train"):
        others.append(("prompt_injection", prompt_injection_all(sizes, random.Random(f"{seed}-pi"), set())))
    if sizes.get("url_train_per_cell"):
        others.append(("phishing_url", phishing_url_all(sizes, random.Random(f"{seed}-url"))))
    for decision, parts in others:
        for name, rows in parts.items():
            out.setdefault(name, []).extend(_examples(rows, decision))
    if others:
        random.Random(f"{seed}-mix").shuffle(out["train"])
    return out
