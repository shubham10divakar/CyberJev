# 06 — Risks and open questions

## Risks

| Risk | Mitigation |
|---|---|
| TF-IDF+LR matches Cyber-Jev on SQLi/XSS at 1000× the speed | Measure it first (M1–M2). Cyber-Jev's case then rests on held-out robustness, calibration, and decisions where n-grams fail (prompt injection). |
| CSIC is one synthetic shop; in-domain scores look great but don't transfer | Report held-out results first. Add a second HTTP source if held-out results are poor. |
| Adversarial evasion (encoding tricks, padding past max_length) | URL-decode inputs; test with obfuscated payloads; say clearly in the README that it's one layer, not a sole defence. |
| Calibration drifts on new traffic | Ship `evaluate.py` so users refit temperatures on their own labelled traffic. |
| Accidentally committing into the nano-jev repo | Separate `git init` + `.git/info/exclude` (M0). |

## Licences to check before release

- CSIC 2010: published for research; check redistribution terms before shipping derived data or weights commercially.
- HF datasets: check each dataset card's licence.
- Nano-Jev v1.0 weights: MIT (fine to fine-tune and relicense).

## Open questions (for you)

1. **Name**: package `cyber-jev` / import `cyberjev` / HF `sdmlai/cyber-jev`. OK?
2. **Decisions for v0.1**: `http_attack`, `prompt_injection`, `phishing_url`. Add or drop any?
3. **Keep the Nano-Jev decisions** (relevance / sufficient / grounded) in Cyber-Jev too, or security only? (Plan: security only.)
4. **Where it runs**: is the target CPU-only servers, or GPU? That sets the latency budget and whether ONNX/int8 is needed early.
