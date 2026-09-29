#!/usr/bin/env bash
# M4: one 6-layer model on all three decisions (data v4) vs single-decision models.
# http_attack's single-decision model is v3-l6 (same http_attack data). One GPU job at a time.
#   bash scripts/m4_runs.sh [seed]
set -e
export PYTHONIOENCODING=utf-8
L6=../nano_jev/runs/nano-jev-v0.1
SEED=${1:-0}
SUF=$([ "$SEED" = 0 ] || echo "-s$SEED")

run() {  # name decisions...
    local name=$1; shift
    local dec=(); [ $# -gt 0 ] && dec=(--decisions "$@")
    python -u scripts/train.py --data data --base "$L6" --out "runs/$name" --max-length 256 \
        --epochs 4 --seed "$SEED" "${dec[@]}" > "runs/train_${name#cyber-jev-}.log" 2>&1
    local tag=cyberjev_${name#cyber-jev-}; tag=${tag//-/_}
    python -u scripts/evaluate.py --model "runs/$name" --max-length 256 "${dec[@]}" \
        --results-dir results --name "$tag"
    python -u scripts/evaluate.py --model "runs/$name" --no-save --max-length 256 "${dec[@]}" \
        --test-data data_heldout --results-dir results --name "${tag}_heldout"
    python -u scripts/evaluate.py --model "runs/$name" --no-save --max-length 256 "${dec[@]}" \
        --test-data data_val --test-file val.jsonl --results-dir results --name "${tag}_val"
    python -u scripts/single_pass.py --model "runs/$name" --save "${dec[@]}" \
        --out "results/single_pass_${tag#cyberjev_}.md"
}

run "cyber-jev-v4-l6$SUF"
run "cyber-jev-v4-l6-pi$SUF" prompt_injection
run "cyber-jev-v4-l6-url$SUF" phishing_url
echo ALL DONE
