# 03 — Data

Every example uses Nano-Jev's format:

```json
{"decision": "http_attack", "question": "Is this HTTP request a web attack ...?",
 "options": ["safe", "attack"], "state": "GET /tienda1/... HTTP/1.1", "label": 1,
 "source": "csic2010"}
```

## Sources

### `http_attack` (v2, 2026-09-28)

M1 trained only on CSIC, whose "safe" requests all come from one shop, so the model learned
"safe = looks like CSIC". v2 trains on three sources and tests on two new ones.

| Role | Source | What it is | License |
|---|---|---|---|
| train / calib / test | CSIC 2010 — `bridge4/CSIC2010_dataset_classification` | requests to one synthetic shop, normal / anomalous | (CSIC terms) |
| train / calib / test | `shengqin/web-attacks` (train split → train, test split → calib/test) | bare payloads: normal text/JSON, XSS, SQLi | none stated |
| train / calib / test | `notesbymuneeb/ai-waf-dataset` (80/10/10) | full requests to ~7.7k hosts, benign / malicious (XSS, SQLi, SSTI, traversal, header attacks, ...) | MIT |
| held-out | `zrmarine/sql_injection` (6000 sampled) | SQL queries and SQLi payloads; benign side includes ordinary SQL, a hard negative | none stated |
| held-out | `vyykaaa/dataset-web-attack` test split | DVWA + Juice Shop requests, 20 attack types | none stated |

Checked and **not used**: `YangYang-Research/web-attack-detection` / `truongp/...` (identical
copies; contain CSIC, and many rows are headers only), `Kaveny/sql-injection` (chat-formatted),
`srimathi2026/sql-injection-datasets` (empty repo), `darkknight25/WAF_DETECTION_DATASET` (broken
JSONL), and the many `*xss-probe*` repos (they probe the HF viewer, not datasets).

Held-out caveats: in `dvwa-juiceshop` most attacks target DVWA's `/vulnerabilities/sqli/`
while all normal traffic is Juice Shop, so path alone separates much of it; read its
per-source numbers with that in mind. Licences marked "none stated" are used for research
evaluation only; check before any release that ships data.

Current sizes (`python scripts/prepare_data.py`):

```
data/train.jsonl        21550  csic 6000 · web-attacks 6000 · ai-waf 9550   (attack 52%)
data/calib.jsonl         1600  csic 500  · web-attacks 500  · ai-waf 600
data/test.jsonl          4200  csic 1500 · web-attacks 1500 · ai-waf 1200
data_heldout/test.jsonl 10320  sqli-queries 6000 (attack 36%) · dvwa-juiceshop 4320 (attack 73%)
```

No text occurs in more than one split; held-out examples that match any in-domain text
are dropped.

### Data v3 (2026-09-29): benign SQL + out-of-domain validation set

`python scripts/prepare_data.py` (preset `default` = `v3`; `--preset v2` rebuilds v2 exactly).
The new sources use their own rng and skip any text already in a split, so v2's splits and
the held-out set are byte-identical.

| Role | Source | What it is | Size | License |
|---|---|---|---|---|
| train / calib / test | `gretelai/synthetic_text_to_sql` | synthetic benign SQL (SELECT, plus INSERT / UPDATE / DELETE / DDL), labelled safe | 3000 / 200 / 500 | Apache-2.0 |
| **validation** | `puyang2025/waf_data_v2` test split | full HTTP requests (WordPress site + a local app), normal / anomalous | 750 attack + 750 normal per host, 3000 | MIT |
| **validation** | `xlangai/spider` dev split | human-written benign SQL, labelled safe | 563 (unique of 1034) | CC-BY-SA-4.0 |

```
data/train.jsonl        24550  (v2 + gretel-sql 3000)
data/calib.jsonl         1800  (v2 + gretel-sql 200)
data/test.jsonl          4700  (v2 + gretel-sql 500)
data_heldout/test.jsonl 10320  (unchanged)
data_val/val.jsonl       3563  waf-v2 3000 (attack 50%) · spider 563 (all safe)
```

**Validation set rules.** Only for out-of-domain *choices* (one-pass variant, thresholds,
model selection); never for final reporting, which stays on the held-out set. The rule for
each choice is fixed before looking (one-pass variant: highest val AUROC).

Checks done:
- `waf_data_v2` has a Host confound (test-site.com is 40% attacks, localhost:8080 5%), so
  val samples each class equally *within* each host. Its texts don't overlap train or held-out.
- No Spider query (train or dev) is in the held-out set; Spider dev repeats queries (563 unique).
- Rejected as validation sources: `AmirAliGharesoufloo/SqlInjection` and
  `firdhokk/autotrain-data-sql-injection` (hundreds of rows shared with held-out
  `zrmarine/sql_injection`), `kblanchfield/web-attacks-multiclass` (CSIC again),
  `grantabejar/payloadsallthethings` (225 markdown files, not examples),
  `darkknight25/Web_Application_Payloads_Dataset` (fails to load).
- Also available, unused: `b-mc2/sql-create-context` (CC-BY-4.0, built from WikiSQL + Spider:
  don't use next to Spider), `Salesforce/wikisql` (no licence: skip).

### Data v4 (M3, 2026-09-29): `prompt_injection` and `phishing_url`

`python scripts/prepare_data.py` (preset `default` = `v4`; `--preset v3` still builds v3).
Each new decision has its own rng; http_attack examples are unchanged (checked).
Held-out and val are built first; training drops anything they contain (for URLs: any
URL on the same **host**, not just the same URL).

#### `prompt_injection`

| Role | Source | What it is | Size | License |
|---|---|---|---|---|
| train / calib / test | `S-Labs/prompt-injection-dataset` | direct injections, "reveal your guidelines" vs ordinary questions | 6000 / 400 / 1000 | MIT |
| train / calib / test | `neuralchemy/Prompt-injection-dataset` (own grouped splits) | injections incl. HackAPrompt, encodings, jailbreaks, hard benign | 4390 / 400 / 900 | Apache-2.0 |
| held-out | `deepset/prompt-injections` (all) | small, multilingual (en / de) | 662 | Apache-2.0 |
| held-out | `jackhhao/jailbreak-classification` (all) | role-play jailbreaks vs benign role-play personas | 1289 | Apache-2.0 |
| validation | `TrustAIRLab/in-the-wild-jailbreak-prompts` (2023-12-25) | in-the-wild jailbreak vs regular prompts, **length-matched** | 750 + 750 | MIT |

Checks: `xTRam1/safe-guard-prompt-injection` and `jayavibhav/prompt-injection` (no licence)
are aggregations (jayavibhav contains all of deepset; xTRam1 contains jackhhao and
TrustAIRLab): not used. `reshabhs/SPML_Chatbot_Prompt_Injection` (MIT) rejected for val:
its injections are the benign prompt plus an appended attack, so **length alone gives AUROC
1.00**. TrustAIRLab is sampled with equal counts per length band (length-only AUROC 0.50).

Length is a shortcut everywhere else (length-only AUROC): train 0.72–0.74, held-out deepset
0.81, jackhhao 0.87 (jailbreaks median 1561 chars vs 232). Injections really are longer,
but compare the model with this baseline. Held-out jailbreaks are longer than max_length
256, so the model sees only their start.

#### Data v5 (2026-09-29): long, length-matched `prompt_injection` training prompts

Why: the M4 joint model was below TF-IDF out of domain on prompt_injection (held-out 0.766,
val 0.676) and flagged 72% of jackhhao's benign role-play prompts. v4 training prompts were
short and templated (median ~50 chars) while held-out / val prompts are long and in-the-wild.

`prompt_injection_extra` (preset `v5` = default) adds 6000 prompts, 5100 / 300 / 600 to
train / calib / test:

| Side | Source | License | In v5 |
|---|---|---|---|
| injection | `Simsonsun/JailbreakPrompts` (DAN-style jailbreaks) | MIT | 1377 |
| injection | `walledai/WildJailbreak` adversarial_harmful (WildJailbreak eval split) | ODC-BY | 1040 |
| injection | `Lakera/mosscap_prompt_injection` (Gandalf password attempts) | MIT | 583 |
| safe | `databricks/databricks-dolly-15k` instruction + context | CC-BY-SA-3.0 | 2122 |
| safe | `saidutta69/awesome-chatgpt-prompts-clean` ("act as …" role-play) | CC0 | 783 |
| safe | `walledai/WildJailbreak` adversarial_benign (jailbreak-style framing, harmless ask) | ODC-BY | 95 |

(Also loaded but not selected after length matching: `Lakera/gandalf_ignore_instructions`,
`garak-llm/tm-system_prompt`: too short or too few.)

- **Length-matched:** equal counts per label in each length band (0/50/100/200/400/800/
  1600/3200 chars), longest bands first. The additions are median 1006 chars, all ≥ 200;
  length-only AUROC 0.494. Over all PI training data, length-only AUROC 0.72 → 0.61.
- **Near-duplicate filter:** besides exact matches, drop any prompt whose first or last 100
  normalised characters (lower-case, letters and digits) match a held-out, val or existing
  prompt. Needed because Simsonsun had 97 exact copies of held-out and 69 of val prompts
  (renamed DAN variants circulate widely).
- Held-out, val and the other decisions are unchanged (diffed against v4).
- **Label caveat:** WildJailbreak adversarial_benign and awesome-chatgpt role-play are
  labelled safe (role-play framing without an attempt to override the model), matching how
  jackhhao and TrustAIRLab label benign personas.
- **Not available yet:** the full `allenai/wildjailbreak` (262k train, adversarial harmful
  and benign) is gated; access needs the account owner to accept its terms on the website.

#### Data v6 (2026-09-29): short, non-English `prompt_injection` prompts

Why: after v5, held-out deepset fell (0.835 → 0.747). deepset is short (median ~60 chars) and
partly German; all v5 additions were long and English.

`prompt_injection_multi` (preset `v6` = default) adds 2736 prompts (2327 / 136 / 273 to
train / calib / test):

| Side | Source | License | In v6 |
|---|---|---|---|
| injection | `yanismiraoui/prompt_injections` (pt / de / fr / es / it / ro / en) | Apache-2.0 | 926 |
| injection | `dmtrdr/russian_prompt_injections` `prompt_ru` (rows from jackhhao dropped) | Apache-2.0 | ~580 |
| safe | MKQA questions de / fr / es / it / pt / ru via `mteb/MKQARetrieval` | CC-BY-3.0 | ~1368 |

- **Script- and length-matched:** two groups (Latin: de/fr/es/it/pt; Cyrillic: ru), each with
  equal counts per label in fine length bands (15–800 chars). Length-only AUROC 0.505,
  Cyrillic flag 0.497.
- MKQA is (nearly) parallel across languages with per-language ids, so each language takes a
  contiguous block of rows: the same question never appears in two languages.
- **Rejected:** `rikka-snow/prompt-injection-multilingual` = deepset + translations (662 exact
  and ~3000 near copies of held-out). `dmtrdr` rows translated from jackhhao (1168) dropped;
  its other sources (Mosscap, SaladBench, JailBreakV, Aegis, disaster tweets) kept.
  `darkknight25/Multilingual_Jailbreak_Dataset` is harmful requests, not injections.
  `deepset/germanquad`, `apple/mkqa`: loading scripts, no longer supported.
- **Caveat:** a translation of a held-out prompt can't be caught by character matching.
  yanismiraoui states "original" and shares no exact or near copy with deepset.

**Reproducibility fix:** `phishdestroy/destroylist` syncs hourly, so a rebuild changed 1063
held-out destroylist URLs and, via host exclusion, 3085 flwrlabs training rows. Pinned to
revision `42163edf` (2026-09-29 06:30 UTC), which reproduces the committed data exactly.

#### `phishing_url`

| Role | Source | What it is | Size | License |
|---|---|---|---|---|
| train / calib / test | `flwrlabs/fed-phishing-urls` (train split → train / calib, test → test) | 1.1M merged URLs, legitimate / phishing | 10000 / 800 / 1998 | Apache-2.0 |
| held-out | `saidutta69/PhishTrap` | Tranco top domains vs Phishing.Database, **collected Aug–Sep 2026** | 1500 + 1500 | MIT |
| held-out | `phishdestroy/destroylist` `urls.txt` | phishing domains only (report DR) | 2000 | MIT |
| validation | `JPxxx/url-benchmark-dataset` (300k sampled) | benign / malicious URLs | 3000 | Apache-2.0 |

- **Format shortcut removed:** in flwrlabs, 70% of bare domains are phishing and 63% of
  URLs with a path are legitimate. Train / calib / test / val take equal counts per label
  within "has a path" and "bare domain".
- **One URL format:** `normalize_url` drops the scheme and trailing `/` (datasets add
  "http://" wholesale: PhishTrap on every row, JPxxx on none). `Decider.phishing_url` applies it.
- **Merged sources:** flwrlabs contains nearly all of Mitake, alexkstern, kmack and
  pirocheto (11064 of 11070); surajshelke (no licence) overlaps them all. None of those can
  be held-out. JPxxx overlaps flwrlabs too (437k URLs), so val drops shared hosts.
- Rejected: `Anvilogic/URL-Guardian-Dataset` (gated), `phl-ldm/tranco_top_million` (57 GB of
  crawl data, not a domain list), `imanoop7/...` (looks synthetic), `Rishik001/...` (features only).
- Shortcut baselines (AUROC): length 0.55 train, **0.86 PhishTrap**, 0.66 val; dot count 0.67
  train, 0.71 PhishTrap, 0.76 val. PhishTrap benign are short popular domains, so length does
  well there; the model must beat it.

```
data/train.jsonl        44940  http_attack 24550 · prompt_injection 10390 · phishing_url 10000
data/calib.jsonl         3400  1800 · 800 · 800
data/test.jsonl          8598  4700 · 1900 · 1998
data_heldout/test.jsonl 17271  10320 · 1951 · 5000
data_val/val.jsonl       8063  3563 · 1500 · 3000
```

## Text format

`cyberjev.schema.normalize_http` is used for training data and at inference:

- **Full requests:** request line (scheme and host stripped), then every header except
  content-negotiation boilerplate (`Accept*`, `Connection`, `Cache-Control`, `Pragma`,
  `Content-Length`, `Sec-CH-*`, `Sec-Fetch-*`, ...), then `body: ...`; URL-decoded. Headers
  that can carry payloads (User-Agent, Referer, Cookie, Host, X-*) are kept.
- **CSIC:** request line and body only (its headers are identical on every request, bar a
  random session cookie that would defeat deduplication).
- **Bare payloads:** URL-decoded only.
- **Prompts:** raw text, truncated to max_length. **URLs:** raw URL string.
- Token lengths: payloads ~40, requests median 80–160, ~5% of full requests exceed 256.

## Splits

- Train from each dataset's train split. Calib and test from its test split, with
  anything that also appears in train removed (CSIC had 43 overlapping requests).
- Balance decisions so none dominates training (cap each at ~10k train examples).
- Held-out sets are only used for final reporting, never for choosing a model.

## Known data caveats

- CSIC "anomalous" includes odd-but-harmless-looking requests (e.g. a tampered parameter
  name `B1A=`), so it is harder than spotting obvious SQLi.
- After deduplication CSIC is ~63% attack. Report balanced metrics (macro-F1, detection
  rate at fixed FPR), not only accuracy.
- CSIC comes from a single synthetic web shop, so held-out results matter more than
  in-domain ones.
- ai-waf looks synthetic: TF-IDF separates it perfectly (AUROC 1.000). It adds diversity of
  safe traffic, not difficulty.
- Reports break every test set down by source (`by_source`), since a pooled number can hide
  a source where all safe examples are flagged.
