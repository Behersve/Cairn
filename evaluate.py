import argparse
import json
from pathlib import Path

from cairn.data import DATASETS
from cairn.engine import evaluate


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--data', required=True, choices=DATASETS)
    parser.add_argument('--checkpoint', required=True)
    parser.add_argument('--root', default='dataset')
    parser.add_argument('--device', default='cuda:0')
    parser.add_argument('--seed', type=int, default=2026)
    parser.add_argument('--batch_size', type=int, default=16)
    args = parser.parse_args()
    results = evaluate(args.root, args.data, args.checkpoint, args.device, args.seed, args.batch_size)
    path = Path(args.checkpoint).with_name('results.json')
    path.write_text(json.dumps(results, indent=2))


if __name__ == '__main__':
    main()
