# Cairn: Observation-Anchored Fusion for Multivariate Time-Series Imputation

## Environment

```bash
pip install -r requirements.txt
```

## Data

`dataset/` contains the six landslide monitoring datasets: HH60, NZUT, PSMH, TT60, TN15 and XP60.

## Usage

Train on one dataset and evaluate it under all missingness patterns:

```bash
python train.py --data TN15
```

Train and evaluate on all six datasets:

```bash
bash run_all.sh
```

Evaluate a trained checkpoint:

```bash
python evaluate.py --data TN15 --checkpoint runs/TN15/checkpoint.pth
```

The model is trained once under point missingness (rate 0.5) and evaluated without retraining under point missingness (rates 0.2, 0.4, 0.6, 0.8), block, subsequence and mixed missingness. Results are written to `runs/<data>/results.json`.
