import json
import random

import numpy as np
import torch
from torch.utils.data import DataLoader

from .data import LENGTH, build, hide, read_series
from .model import Cairn

EVALUATIONS = (('point', 0.2), ('point', 0.4), ('point', 0.6), ('point', 0.8),
               ('block', 0.5), ('subsequence', 0.5), ('mixed', 0.5))


def seed_all(seed):
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)


def predict(model, x, device):
    model.eval()
    with torch.no_grad():
        mask = torch.from_numpy(np.isfinite(x)).float().to(device)
        values = torch.from_numpy(np.nan_to_num(x)).to(device)
        return model(values, mask).float().cpu().numpy()


def score(model, x, truth, target, device, batch_size):
    squared, absolute, total = 0.0, 0.0, 0
    for start in range(0, len(x), batch_size):
        end = start + batch_size
        prediction = predict(model, x[start:end], device)
        hidden = target[start:end]
        delta = prediction[hidden].astype(np.float64) - truth[start:end][hidden]
        squared += float(np.square(delta).sum())
        absolute += float(np.abs(delta).sum())
        total += delta.size
    return dict(mse=squared / total, mae=absolute / total)


def train(root, name, output, device, seed=2026, rate=0.5, epochs=300, patience=30,
          batch_size=16, learning_rate=1e-3):
    seed_all(seed)
    train_x = build(root, name, 'train', seed)
    val_x, val_truth, val_target = build(root, name, 'val', seed, 'point', rate)
    seed_all(seed)
    model = Cairn(train_x.shape[2], LENGTH).to(device)
    optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate, weight_decay=0.0)
    loader = DataLoader(torch.from_numpy(train_x), batch_size=batch_size, shuffle=True)
    rng = np.random.default_rng(seed + 2000)
    best, stale, history = float('inf'), 0, []
    for epoch in range(epochs):
        model.train()
        squared, total = 0.0, 0
        for x in loader:
            observed = torch.isfinite(x)
            target = torch.from_numpy(np.stack([hide(m.numpy(), rng, 'point', rate) for m in observed]))
            mask = (observed & ~target).to(device)
            original = torch.nan_to_num(x).to(device)
            target = target.to(device)
            optimizer.zero_grad()
            prediction = model(original * mask, mask.float())
            loss = (prediction[target] - original[target]).square().mean()
            loss.backward()
            optimizer.step()
            count = int(target.sum())
            squared += loss.item() * count
            total += count
        val = score(model, val_x, val_truth, val_target, device, batch_size)
        record = dict(epoch=epoch + 1, train_mse=squared / total, val_mse=val['mse'], val_mae=val['mae'])
        history.append(record)
        print(json.dumps(record), flush=True)
        if val['mse'] < best:
            best, stale = val['mse'], 0
            torch.save(model.state_dict(), output / 'checkpoint.pth')
        else:
            stale += 1
        if stale >= patience:
            break
    (output / 'history.json').write_text(json.dumps(history, indent=2))


def evaluate(root, name, checkpoint, device, seed=2026, batch_size=16, evaluations=EVALUATIONS):
    features = read_series(root, name).shape[1]
    model = Cairn(features, LENGTH).to(device)
    model.load_state_dict(torch.load(checkpoint, map_location=device, weights_only=True))
    results = {}
    for pattern, rate in evaluations:
        x, truth, target = build(root, name, 'test', seed, pattern, rate)
        key = f'{pattern}_{rate}' if pattern == 'point' else pattern
        results[key] = score(model, x, truth, target, device, batch_size)
        print(name, key, json.dumps(results[key]), flush=True)
    return results
