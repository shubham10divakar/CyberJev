#!/usr/bin/env bash
# Data v3 (benign SQL + validation set): train the 6-layer model with seeds 0 and 1, evaluate
# in-domain, held-out and val, pick the one-pass variant on val. One GPU job at a time.
#   bash scripts/v3_runs.sh
set -e
export PYTHONIOENCODING=utf-8
L6=../nano_jev/runs/nano-jev-v0.1

evaluate() {  # model-folder results-tag [--no-save]
    local model=$1 tag=$2; shift 2
    python -u scripts/evaluate.py --model "$model" --max-length 256 "$@" \
        --results-dir results --name "$tag"
    python -u scripts/evaluate.py --model "$model" --no-save --max-length 256 \
        --test-data data_heldout --results-dir results --name "${tag}_heldout"
    python -u scripts/evaluate.py --model "$model" --no-save --max-length 256 \
        --test-data data_val --test-file val.jsonl --results-dir results --name "${tag}_val"
}

# Baseline: the v2 model on the v3 test sets (temperature refitted on v3 calib, not saved).
evaluate runs/cyber-jev-v2-l6 cyberjev_v2_l6_on_v3 --no-save

for seed in 0 1; do
    name=cyber-jev-v3-l6$([ $seed = 0 ] || echo "-s$seed")
    python -u scripts/train.py --data data --base "$L6" --out "runs/$name" --max-length 256 \
        --epochs 4 --seed $seed > "runs/train_${name#cyber-jev-}.log" 2>&1
    tag=cyberjev_${name#cyber-jev-}; tag=${tag//-/_}
    evaluate "runs/$name" "$tag"
    python -u scripts/single_pass.py --model "runs/$name" --save \
        --out "results/single_pass_${tag#cyberjev_}.md"
done
echo ALL DONE
