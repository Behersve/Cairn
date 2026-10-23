import argparse
import json
from pathlib import Path

from cairn.data import DATASETS
from cairn.engine import evaluate, train


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--data', required=True, choices=DATASETS)
    parser.add_argument('--root', default='dataset')
    parser.add_argument('--output', default='runs')
    parser.add_argument('--device', default='cuda:0')
    parser.add_argument('--seed', type=int, default=2026)
    parser.add_argument('--epochs', type=int, default=300)
    parser.add_argument('--patience', type=int, default=30)
    parser.add_argument('--batch_size', type=int, default=16)
    parser.add_argument('--learning_rate', type=float, default=1e-3)
    args = parser.parse_args()
    output = Path(args.output) / args.data
    output.mkdir(parents=True, exist_ok=True)
    train(args.root, args.data, output, args.device, args.seed, epochs=args.epochs,
          patience=args.patience, batch_size=args.batch_size, learning_rate=args.learning_rate)
    results = evaluate(args.root, args.data, output / 'checkpoint.pth', args.device, args.seed,
                       args.batch_size)
    (output / 'results.json').write_text(json.dumps(results, indent=2))


if __name__ == '__main__':
    main()
