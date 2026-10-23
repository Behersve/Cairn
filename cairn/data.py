from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

LENGTH = 96
DATASETS = ('HH60', 'NZUT', 'PSMH', 'TT60', 'TN15', 'XP60')
SPLITS = ('train', 'val', 'test')
PATTERNS = {
    'point': dict(kind='point'),
    'subsequence': dict(kind='rectangle', rate=0.5, length=24, width=1),
    'block': dict(kind='rectangle', rate=0.5, length=6, width=6),
    'mixed': dict(kind='mixed'),
}
MIXED_NOISE = 0.05
MIXED_START = 0.0015
MIXED_LENGTHS = (24, 96)


def read_series(root, name):
    frame = pd.read_csv(Path(root) / f'{name}.csv')
    return frame.drop(columns='date').values


def split_windows(values, split, length=LENGTH):
    n = len(values)
    num_train, num_test = int(n * 0.7), int(n * 0.2)
    num_val = n - num_train - num_test
    starts = [0, num_train - length, n - num_test - length]
    ends = [num_train, num_train + num_val, n]
    scaler = StandardScaler().fit(values[:num_train])
    part = scaler.transform(values)[starts[SPLITS.index(split)]:ends[SPLITS.index(split)]]
    count = len(part) - 2 * length + 1
    return [np.asarray(part[i:i + length], dtype=np.float32) for i in range(count)]


def point_mask(observed, rng, rate):
    return (rng.random(observed.shape) < rate) & observed


def rectangle_mask(observed, rng, rate, length, width):
    n_steps, n_features = observed.shape
    target = np.zeros_like(observed)
    remaining = int(round(rate * int(observed.sum())))
    while remaining > 0:
        available = np.flatnonzero(observed & ~target)
        if not len(available):
            break
        step, variable = np.unravel_index(rng.choice(available), observed.shape)
        step = max(0, int(step) - int(rng.integers(0, length)))
        variable = max(0, int(variable) - int(rng.integers(0, width)))
        window = (slice(step, min(step + length, n_steps)),
                  slice(variable, min(variable + width, n_features)))
        fresh = np.flatnonzero(observed[window] & ~target[window])
        if len(fresh) > remaining:
            fresh = rng.choice(fresh, remaining, replace=False)
        target[window].flat[fresh] = True
        remaining -= len(fresh)
    return target


def mixed_mask(observed, rng):
    target = rng.random(observed.shape) < MIXED_NOISE
    for step, variable in zip(*np.nonzero(rng.random(observed.shape) < MIXED_START)):
        length = int(rng.integers(MIXED_LENGTHS[0], MIXED_LENGTHS[1] + 1))
        target[step:step + length, variable] = True
    return target & observed


def hide(observed, rng, pattern='point', rate=0.5):
    spec = PATTERNS[pattern]
    if spec['kind'] == 'point':
        target = point_mask(observed, rng, rate)
    elif spec['kind'] == 'rectangle':
        target = rectangle_mask(observed, rng, spec['rate'], spec['length'], spec['width'])
    else:
        target = mixed_mask(observed, rng)
    positions = np.flatnonzero(observed)
    if len(positions) < 2:
        raise ValueError('a window has fewer than two observations')
    if not target.any():
        target.flat[rng.choice(positions)] = True
    if target.sum() == len(positions):
        target.flat[rng.choice(positions)] = False
    return target


def build(root, name, split, seed, pattern='point', rate=0.5):
    windows = split_windows(read_series(root, name), split)
    rng = np.random.default_rng(seed + 1000 + SPLITS.index(split))
    x, truth, target = [], [], []
    for window in windows:
        observed = np.isfinite(window)
        original = np.where(observed, window, np.nan).astype(np.float32)
        hidden = np.zeros_like(observed)
        if split != 'train':
            hidden = hide(observed, rng, pattern, rate)
        masked = original.copy()
        masked[hidden] = np.nan
        x.append(masked)
        truth.append(original)
        target.append(hidden)
    if split == 'train':
        return np.stack(x)
    return np.stack(x), np.stack(truth), np.stack(target)
