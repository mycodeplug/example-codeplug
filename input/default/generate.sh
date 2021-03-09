#!/usr/bin/env bash

# This generates the same codeplug as generate.py
# using bash scripting. Linux or macOS only.

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
OUTPUT=${OUTPUT:-$DIR/../../OUTPUT}
python -m dzcb \
    --pnwdigital \
    --seattledmr \
    --default-k7abd \
    --k7abd $DIR/k7abd \
    --repeaterbook-proximity-csv "$DIR/prox.csv" \
    --repeaterbook-state washington oregon \
    --scanlists-json "$DIR/scanlists.json" \
    --exclude "$DIR/exclude.csv" \
    --order "$DIR/order.csv" \
    --replacements "$DIR/replacements.csv" \
    --anytone \
    --dmrconfig "$DIR/example-d878uv.conf" \
    --farnsworth-template-json "$DIR/example-md-uv380.json" \
    --gb3gf \
-- "$OUTPUT/$(basename "$DIR")"
