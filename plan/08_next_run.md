# 08 — Next run (written 2026-09-28, updated 2026-09-29)

Start here. Full numbers are in `07_status.md`; data details in `03_data.md`.

## Where things stand

- **Best joint model so far: `runs/cyber-jev-v5-l6`** (all three decisions, data v5, seed 0;
  not yet exported to ONNX). Best http-only model: `runs/cyber-jev-v3-l6` (data v3, ONNX).
  Before that: `runs/cyber-jev-v2-l6` (6 layers, from Nano-Jev v0.1 =
  `../nano_jev/runs/nano-jev-v0.1`). Trained on data v2, 4 epochs (best epoch 3), max_length 256.
  In-domain AUROC 0.995, held-out AUROC 0.953. Also has `model.onnx` and `model.int8.onnx`.
- `runs/cyber-jev-v2` (12 layers, from Nano-Jev v1.0): same in-domain, worse held-out (0.881).
- `runs/cyber-jev-dev`: the M1 model (CSIC only); kept only for comparison.
- CPU latency (8 threads, batch 1, median), one pass, v3-l6: Decider on ONNX int8 **3.8–4.0 ms**
  (v2-l6: 4.3–4.5); PyTorch 9.6 ms. v2-l6 via onnx_cpu.py: PyTorch 8.7 ms, ONNX int8 4.2 ms
  (two passes: 12.7 / 8.1). Target ≤ 5 ms met with ONNX int8; the Decider uses it on CPU (4.3–4.5 ms end to end).
  `one_pass.json` and the ONNX calibration files are in the run folder.
- Weights are in `runs/` (git-ignored, local only). Nothing is pushed to HF or PyPI.
- `data/` and `data_heldout/` are committed; rebuild with `python scripts/prepare_data.py`.

## Machine limits (this desktop)

Ryzen 7 5800X (8 cores / 16 threads), RTX 3060 12 GB, 16 GB RAM (about 5–7 GB free with a
browser open). Enough for everything planned; the models are small (22M parameters).

- Run **one heavy job at a time**. Don't train on the GPU while a CPU benchmark runs (it skews
  timings), and keep one model per process: an all-in-one ONNX run was stopped once for low
  memory.
- Close Firefox for long runs if memory is tight.
- Use `python -u` when logging to a file, or the log stays empty until the end.
- Windows console: set `PYTHONIOENCODING=utf-8` (tables use →).
- Timings: 6-layer training ≈ 1.5 min/epoch on 21.5k examples; 12-layer ≈ 2.8 min/epoch;
  `onnx_cpu.py` ≈ 8–10 min for all three variants.

## Next steps, in order

### 1. ✅ One encoder pass per binary decision (done 2026-09-29, option b)

Inference-only: `scripts/single_pass.py --save` writes `one_pass.json`; the Decider uses it.
ONNX int8 CPU median **4.2 ms** (target ≤ 5), held-out AUROC 0.945–0.950 vs 0.953. Details in
`07_status.md`. Left open:

- **Threat-only vs safe-only.** Calib NLL picked threat-only; safe-only is better on every
  held-out metric (AUROC 0.958, DR@1%FPR 0.572). Settle it with step 2's second seed and/or a
  separate out-of-domain *validation* set, not the held-out test.
- ✅ **Decider on ONNX** (done 2026-09-29). On CPU the Decider now loads `model.int8.onnx`
  with its own calibration (`one_pass.model.int8.json`): **4.3–4.5 ms** median over three
  runs, p95 ~13 ms (PyTorch 9.8 ms). `results/latency_v2-l6_onnx.md`. Latency varies run to
  run by up to ~1.5 ms with other programs open: one `onnx_cpu.py` rerun gave 5.6 ms.

### 2. ✅ Second seed (done 2026-09-29)

6-layer lead confirmed (held-out 0.953 / 0.944 vs 12-layer 0.881 / 0.864); 3 epochs worse
(0.905). Held-out varies a lot run to run (DR@1%FPR 0.26–0.46). Safe-only one-pass beat
threat-only held-out on all three 6-layer runs (threat-only as low as 0.847), though calib NLL
always picked threat-only. Details in `07_status.md`. Next: confirm safe-only on the
out-of-domain validation set (3b). **Settled:** val picks threat-only on all three runs, so
threat-only stays (`07_status.md`).

### 3. ✅ Hard benign negatives (done 2026-09-29: data v3, working model now `runs/cyber-jev-v3-l6`)

Benign-SQL false alarms: Spider 0.55 → 0.00, held-out sqli-queries 0.41 → 0.20, SQLi detection
unchanged; small cost on waf-v2 requests (AUROC 0.885 → 0.875). Details in `07_status.md`.
✅ v3-l6 exported to ONNX with its own calibration: Decider **3.8–4.0 ms** CPU median,
Spider false alarms still 0 on int8. Left open: look at why waf-v2 dropped (what normal
requests are now flagged).

### 3 (original note)

Both models flag benign SQL queries (sqli-queries FPR@0.5: 0.41 for v2-l6) even though the
ranking is good (AUROC 0.99). Add benign SQL-like / code-like text to **training** from a
source that isn't the held-out one (e.g. a text-to-SQL dataset such as Spider or WikiSQL
queries, labelled safe), then re-check held-out FPR. Don't train on `zrmarine/sql_injection`:
it's held-out.

### 3b. ✅ Out-of-domain validation set (done 2026-09-29: `data_val/`, see `03_data.md`)

Calib is in-domain and held-out is test-only, so there's nothing to make out-of-domain
choices on (threat-only vs safe-only, thresholds). Add a small `data_val/` from a source that
is neither training nor held-out, used only for such choices. Also look for a harder held-out
web-request source: `dvwa-juiceshop` can be separated by path alone.

### 4. M3: `prompt_injection` and `phishing_url` (data ✅ 2026-09-29: data v4, see `03_data.md`)

Next: M4, train one 6-layer model on all three decisions (data v4), evaluate each decision
in-domain / held-out / val against its shortcut baselines (length, TF-IDF), and check
http_attack doesn't get worse than v3-l6.

### 5. M4 (started 2026-09-29): `bash scripts/m4_runs.sh [seed]`

Joint `runs/cyber-jev-v4-l6` (all decisions) vs single-decision `v4-l6-pi`, `v4-l6-url`
(http single = v3-l6). Results: `results/cyberjev_v4_l6*`. Zero-shot v3-l6 on the new
decisions for reference: held-out AUROC 0.49 (PI) / 0.54 (URL), val 0.65 / 0.69
(`results/zeroshot_v3_l6_v4*`). Then seeds 1, 2 (`m4_runs.sh 1`, `m4_runs.sh 2`) per the
paper checklist (`09_paper_readiness.md`).

**Seed 0 done (see `07_status.md`):** joint ≥ single for all three; http_attack unchanged or
better; phishing_url beats TF-IDF (not length on PhishTrap); **prompt_injection is below
TF-IDF out of domain** (held-out 0.766 vs 0.887, val 0.676 vs 0.740; one-pass threat-only
0.861 / 0.749). Next, before more seeds:
1. PI data diversity: longer, in-the-wild style prompts on both sides (benign role-play /
   system prompts, long jailbreaks) from sources that are not held-out or val; check the
   length shortcut stays low in training. **Done 2026-09-29: data v5, joint `v5-l6`.** PI val
   0.676 → 0.813 (above TF-IDF 0.791), held-out 0.766 → 0.829 (TF-IDF 0.880; deepset fell
   0.835 → 0.747). Next for PI: short / non-English variety from a non-held-out source.
   Optional: full `allenai/wildjailbreak` once its terms are accepted on the HF account.
2. Consider 2–3 epochs or a lower LR for URL (best epoch 1).
3. Then seeds 1, 2 for the M4 comparison, and ONNX export of the chosen joint model.
   **In progress 2026-09-29:** data v6 (short, non-English PI) built; joint v6-l6 seed 0
   done (deepset 0.747 → 0.787; other numbers within one-run noise). Seeds 1, 2 of v5 and v6
   running; pick v5 or v6 by mean val AUROC (`python scripts/seed_summary.py --runs v5_l6
   v5_l6_s1 v5_l6_s2 --runs v6_l6 v6_l6_s1 v6_l6_s2`). `data_v5/` is a git-ignored rebuild
   (`prepare_data.py --preset v5 --out data_v5`).
   **Done:** val rule picks **v5** (mean val 0.886 vs 0.880, within noise). Over 3 seeds PI
   is level with TF-IDF on val (0.799 vs 0.791) and below on held-out (0.812 vs 0.880); v6
   fixed deepset (+0.07) but cost URL held-out (−0.026). See `07_status.md`.

### 6. Next options (decide)

- PI further: per-decision epochs / loss weighting (PI overfits by epoch 2), longer max_length
  for PI (jailbreaks are cut at 256 tokens), or the full WildJailbreak (user said skip for now).
- ONNX export + calibration of the chosen joint model (`runs/cyber-jev-v5-l6`).
- Paper items 5, 6, 8, 9 (`09_paper_readiness.md`).

#### Original M3 note

Verify the candidate datasets listed in `03_data.md` (existence, size, labels, licence),
add builders to `cyberjev/data.py`, and give each a held-out source from a different origin.

## Open issues to remember

- Licences: `shengqin/web-attacks`, `zrmarine/sql_injection` and `vyykaaa/dataset-web-attack`
  state none. They're fine for research evaluation; check before any release that ships them.
- `dvwa-juiceshop` held-out can be partly separated by path (attacks mostly on DVWA, normal
  all on Juice Shop), so its AUROC flatters every model.
- `ai-waf` looks synthetic (TF-IDF AUROC 1.000). It adds variety to safe traffic, not
  difficulty; CSIC is the informative in-domain source.
- max_length 128 was tested and rejected (it truncates payloads in full requests).
- p95 latency (~23 ms) is set by long requests. After step 1, look at the p95 again.

### Known issues from the spot check (see `07_status.md`)

- Benign search request at attack 0.53; github.com user-repo URL at phishing 0.93.
- `normalize_http` turns `+` into a space in raw bodies (fix: decode `+` only in query
  strings and `application/x-www-form-urlencoded` bodies; needs a data rebuild).

### 7. PI truncation (started 2026-09-29, user chose "improve prompt injection")

At max_length 256, 71–73% of val prompts and 68% of held-out jackhhao jailbreaks are cut;
only their start is seen. Two probes on data v5, seed 0 (`trunc_probe`):
- `v5ht-l6`: `--truncation head_tail` (keep the first and last halves of the budget; same cost).
- `v5ml512-l6`: max_length 512 (46% of val still longer; long inputs cost ~2×).
Then 3 seeds for the better one if it beats v5-l6 on val (v5: PI val 0.799 ± 0.015).
**Done: neither helps** (PI val 0.787 / 0.808 vs 0.813 at seed 0; held-out 0.828 / 0.799).
Truncation is not the bottleneck; keep head / 256. Remaining PI ideas: a multilingual or
larger backbone, a TF-IDF + model ensemble, or report PI as a limitation.

### 8. Decision (2026-09-29): PI is a reported limitation; paper items next

Working joint model: `runs/cyber-jev-v5-l6` (data v5; seeds s1, s2 exist). Next, in order:
1. ONNX int8 export + per-decision calibration + CPU latency for v5-l6 (onnx_cpu.py needs a
   per-decision loop for the joint model).
2. Plain fine-tuned classifier baseline (same 6-layer backbone, input text only, no
   question / option), one per decision, 3 seeds (paper item 5).
3. Calibration and triage analysis: reliability diagrams and block / review / allow
   trade-off per decision (paper items 8, 9).
