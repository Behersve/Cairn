#!/usr/bin/env bash
set -e
for data in HH60 NZUT PSMH TT60 TN15; do
  python train.py --data "$data" "$@"
done
