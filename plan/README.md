# Cyber-Jev — plan

A small, calibrated, **decision-only** model for security checks on text-like traffic,
built on the Nano-Jev code and weights. It is given a question, some options and a
piece of state (an HTTP request, a prompt, a URL, a log line) and returns a
probability per option in a few milliseconds. It never generates text.

```python
import cyberjev
d = cyberjev.load()
d.http_attack("GET /login?user=admin' OR '1'='1' -- HTTP/1.1")
# {'safe': 0.02, 'attack': 0.98}
```

## Files

| File | What it covers |
|---|---|
| [01_goal_and_scope.md](01_goal_and_scope.md) | What it is for, and what it is **not** for (packet-level IDS) |
| [02_architecture.md](02_architecture.md) | How an input becomes a probability; what is copied from Nano-Jev; repo layout |
| [03_data.md](03_data.md) | Public datasets per decision, text format, splits, held-out sets |
| [04_training_and_eval.md](04_training_and_eval.md) | Training recipe, baselines, security metrics, latency |
| [05_milestones.md](05_milestones.md) | Ordered steps with done-criteria |
| [06_risks_and_open_questions.md](06_risks_and_open_questions.md) | Risks, licences, decisions still open |
| [07_status.md](07_status.md) | Latest results and the M2 go/no-go decision |
| [08_next_run.md](08_next_run.md) | **Start here next session**: where things stand, what to run next |
| [09_paper_readiness.md](09_paper_readiness.md) | What a paper needs and where we stand (checklist) |

## Status

| Date | Step |
|---|---|
| 2026-09-27 | Plan written. `http_attack` data prototype built. |
| 2026-09-27 | M0 done (package, tests pass). M1 done: first `http_attack` model. M2: continue, fix training-data diversity first (see 07). |
| 2026-09-28 | M2 steps 1–3: data v2 (3 train sources, new held-out), 4-epoch runs, 6-layer model `v2-l6` (held-out AUROC 0.95), ONNX int8 8.1 ms CPU. Next: one pass per decision (see 08). |

## Origin

Zero-shot Nano-Jev v1.0 can't tell attacks from normal requests: on
`GET /login?user=admin' OR '1'='1' --` it said 74% safe, and v0.1 called every request
an attack. The architecture is fine; it has just never seen security data. Cyber-Jev is
Nano-Jev fine-tuned on security decisions, with its own schema, package and weights.
