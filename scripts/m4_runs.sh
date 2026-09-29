#!/usr/bin/env bash
# M4: one 6-layer model on all three decisions vs single-decision models.
# http_attack's single-decision model is v3-l6 (same http_attack data). One GPU job at a time.
#   bash scripts/m4_runs.sh [seed] [name prefix, default v4] [all | joint]
#   DATA=data_v5 bash scripts/m4_runs.sh 1 v5 joint   # train / calib / in-domain test from another folder
#   MAXLEN=512 TRAIN_ARGS="--truncation head_tail" bash scripts/m4_runs.sh 0 v5ht joint
set -e
export PYTHONIOENCODING=utf-8
L6=../nano_jev/runs/nano-jev-v0.1
SEED=${1:-0}
SUF=$([ "$SEED" = 0 ] || echo "-s$SEED")
PREFIX=${2:-v4}
WHICH=${3:-all}
DATA=${DATA:-data}
MAXLEN=${MAXLEN:-256}
read -r -a EXTRA <<< "${TRAIN_ARGS:-}"

run() {  # name decisions...
    local name=$1; shift
    local dec=(); [ $# -gt 0 ] && dec=(--decisions "$@")
    python -u scripts/train.py --data "$DATA" --base "$L6" --out "runs/$name" --max-length "$MAXLEN" \
        --epochs 4 --seed "$SEED" "${dec[@]}" "${EXTRA[@]}" > "runs/train_${name#cyber-jev-}.log" 2>&1
    local tag=cyberjev_${name#cyber-jev-}; tag=${tag//-/_}
    python -u scripts/evaluate.py --model "runs/$name" --data "$DATA" --max-length "$MAXLEN" "${dec[@]}" \
        --results-dir results --name "$tag"
    python -u scripts/evaluate.py --model "runs/$name" --data "$DATA" --no-save --max-length "$MAXLEN" \
        "${dec[@]}" --test-data data_heldout --results-dir results --name "${tag}_heldout"
    python -u scripts/evaluate.py --model "runs/$name" --data "$DATA" --no-save --max-length "$MAXLEN" \
        "${dec[@]}" --test-data data_val --test-file val.jsonl --results-dir results --name "${tag}_val"
    python -u scripts/single_pass.py --model "runs/$name" --data "$DATA" --max-length "$MAXLEN" \
        --save "${dec[@]}" --out "results/single_pass_${tag#cyberjev_}.md"
}

run "cyber-jev-$PREFIX-l6$SUF"
if [ "$WHICH" = all ]; then
    run "cyber-jev-$PREFIX-l6-pi$SUF" prompt_injection
    run "cyber-jev-$PREFIX-l6-url$SUF" phishing_url
fi
echo ALL DONE
