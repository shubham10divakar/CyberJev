#!/usr/bin/env bash
# M2 step 2: second seed for v2 and v2-l6, and v2-l6 with 3 epochs. One GPU job at a time.
#   bash scripts/seed_runs.sh
set -e
export PYTHONIOENCODING=utf-8
L6=../nano_jev/runs/nano-jev-v0.1
L12=../nano_jev/runs/nano-jev-v1.0

run() {  # name base extra-train-args...
    local name=$1 base=$2; shift 2
    python -u scripts/train.py --data data --base "$base" --out "runs/$name" --max-length 256 \
        --epochs 4 "$@" > "runs/train_${name#cyber-jev-}.log" 2>&1
    local tag=${name#cyber-jev-}; tag=cyberjev_${tag//-/_}
    python -u scripts/evaluate.py --model "runs/$name" --max-length 256 \
        --results-dir results --name "$tag"
    python -u scripts/evaluate.py --model "runs/$name" --no-save --max-length 256 \
        --test-data data_heldout --results-dir results --name "${tag}_heldout"
    python -u scripts/single_pass.py --model "runs/$name" \
        --out "results/single_pass_${tag#cyberjev_}.md"
}

run cyber-jev-v2-l6-s1 "$L6" --seed 1
run cyber-jev-v2-s1 "$L12" --seed 1
run cyber-jev-v2-l6-e3 "$L6" --epochs 3
echo ALL DONE
