# Standard Deviations of Reported Results

- All standard deviations (SD) are computed over five runs with different random seeds.
- Part 1 corresponds to Table 2 of the paper; each cell reports **SD of MSE / SD of MAE**.
- Part 2 corresponds to Table 3 of the paper; each cell reports the SD of MSE.
- *Landslide*: the six landslide monitoring datasets; *Public*: the nine public datasets.
- For point-wise missingness, MSE and MAE are first averaged over the four test-time rates (0.2, 0.4, 0.6, and 0.8) within each run, and the SD is computed over runs.
- ETTh Avg. and ETTm Avg. average their two member datasets within each run before the SD is computed.

## Part 1. SD for Table 2 of the paper

### Point-wise missingness (average over rates 0.2, 0.4, 0.6, and 0.8)

| Dataset | Cairn (Ours) | HELIX | PSW-I | TimeMixer++ | ImputeFormer | ModernTCN | iTransformer | SAITS | PatchTST | TimesNet | DLinear | BRITS |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| ***Landslide*** | | | | | | | | | | | | |
| TN15 | 0.000&nbsp;/&nbsp;0.001 | 0.001&nbsp;/&nbsp;0.002 | 0.000&nbsp;/&nbsp;0.000 | 0.003&nbsp;/&nbsp;0.004 | 0.005&nbsp;/&nbsp;0.004 | 0.000&nbsp;/&nbsp;0.000 | 0.000&nbsp;/&nbsp;0.000 | 0.013&nbsp;/&nbsp;0.007 | 0.000&nbsp;/&nbsp;0.001 | 0.002&nbsp;/&nbsp;0.002 | 0.001&nbsp;/&nbsp;0.001 | 0.008&nbsp;/&nbsp;0.005 |
| HH60 | 0.001&nbsp;/&nbsp;0.000 | 0.002&nbsp;/&nbsp;0.001 | 0.002&nbsp;/&nbsp;0.001 | 0.004&nbsp;/&nbsp;0.004 | 0.002&nbsp;/&nbsp;0.001 | 0.001&nbsp;/&nbsp;0.000 | 0.002&nbsp;/&nbsp;0.001 | 0.046&nbsp;/&nbsp;0.023 | 0.001&nbsp;/&nbsp;0.001 | 0.001&nbsp;/&nbsp;0.001 | 0.002&nbsp;/&nbsp;0.002 | 0.072&nbsp;/&nbsp;0.029 |
| TT60 | 0.004&nbsp;/&nbsp;0.001 | 0.022&nbsp;/&nbsp;0.002 | 0.004&nbsp;/&nbsp;0.001 | 0.023&nbsp;/&nbsp;0.004 | 0.113&nbsp;/&nbsp;0.009 | 0.003&nbsp;/&nbsp;0.001 | 0.002&nbsp;/&nbsp;0.000 | 0.198&nbsp;/&nbsp;0.039 | 0.002&nbsp;/&nbsp;0.001 | 0.005&nbsp;/&nbsp;0.001 | 0.005&nbsp;/&nbsp;0.001 | 0.153&nbsp;/&nbsp;0.034 |
| XP60 | 0.022&nbsp;/&nbsp;0.003 | 0.009&nbsp;/&nbsp;0.001 | 0.022&nbsp;/&nbsp;0.002 | 0.004&nbsp;/&nbsp;0.001 | 0.006&nbsp;/&nbsp;0.001 | 0.019&nbsp;/&nbsp;0.002 | 0.019&nbsp;/&nbsp;0.003 | 0.009&nbsp;/&nbsp;0.002 | 0.002&nbsp;/&nbsp;0.000 | 0.009&nbsp;/&nbsp;0.001 | 0.007&nbsp;/&nbsp;0.001 | 0.029&nbsp;/&nbsp;0.006 |
| NZUT | 0.021&nbsp;/&nbsp;0.008 | 0.041&nbsp;/&nbsp;0.016 | 0.030&nbsp;/&nbsp;0.010 | 0.020&nbsp;/&nbsp;0.009 | 0.020&nbsp;/&nbsp;0.007 | 0.006&nbsp;/&nbsp;0.002 | 0.007&nbsp;/&nbsp;0.003 | 0.067&nbsp;/&nbsp;0.026 | 0.005&nbsp;/&nbsp;0.002 | 0.013&nbsp;/&nbsp;0.005 | 0.004&nbsp;/&nbsp;0.002 | 0.054&nbsp;/&nbsp;0.022 |
| PSMH | 0.003&nbsp;/&nbsp;0.003 | 0.007&nbsp;/&nbsp;0.003 | 0.003&nbsp;/&nbsp;0.002 | 0.017&nbsp;/&nbsp;0.007 | 0.012&nbsp;/&nbsp;0.004 | 0.002&nbsp;/&nbsp;0.002 | 0.002&nbsp;/&nbsp;0.002 | 0.131&nbsp;/&nbsp;0.038 | 0.012&nbsp;/&nbsp;0.011 | 0.001&nbsp;/&nbsp;0.001 | 0.010&nbsp;/&nbsp;0.009 | 0.016&nbsp;/&nbsp;0.005 |
| ***Public*** | | | | | | | | | | | | |
| ETTh&nbsp;Avg. | 0.006&nbsp;/&nbsp;0.007 | 0.003&nbsp;/&nbsp;0.003 | 0.007&nbsp;/&nbsp;0.005 | 0.002&nbsp;/&nbsp;0.002 | 0.005&nbsp;/&nbsp;0.005 | 0.004&nbsp;/&nbsp;0.005 | 0.006&nbsp;/&nbsp;0.005 | 0.003&nbsp;/&nbsp;0.003 | 0.008&nbsp;/&nbsp;0.009 | 0.013&nbsp;/&nbsp;0.012 | 0.013&nbsp;/&nbsp;0.010 | 0.010&nbsp;/&nbsp;0.005 |
| ETTm&nbsp;Avg. | 0.001&nbsp;/&nbsp;0.002 | 0.003&nbsp;/&nbsp;0.005 | 0.004&nbsp;/&nbsp;0.005 | 0.001&nbsp;/&nbsp;0.001 | 0.002&nbsp;/&nbsp;0.003 | 0.001&nbsp;/&nbsp;0.002 | 0.001&nbsp;/&nbsp;0.001 | 0.007&nbsp;/&nbsp;0.006 | 0.001&nbsp;/&nbsp;0.001 | 0.002&nbsp;/&nbsp;0.003 | 0.011&nbsp;/&nbsp;0.010 | 0.009&nbsp;/&nbsp;0.006 |
| ECL | 0.002&nbsp;/&nbsp;0.002 | 0.001&nbsp;/&nbsp;0.002 | 0.008&nbsp;/&nbsp;0.006 | 0.009&nbsp;/&nbsp;0.009 | 0.002&nbsp;/&nbsp;0.002 | 0.011&nbsp;/&nbsp;0.010 | 0.020&nbsp;/&nbsp;0.018 | 0.015&nbsp;/&nbsp;0.010 | 0.003&nbsp;/&nbsp;0.003 | 0.007&nbsp;/&nbsp;0.007 | 0.003&nbsp;/&nbsp;0.002 | 0.020&nbsp;/&nbsp;0.013 |
| Exchange | 0.000&nbsp;/&nbsp;0.000 | 0.002&nbsp;/&nbsp;0.003 | 0.000&nbsp;/&nbsp;0.001 | 0.005&nbsp;/&nbsp;0.006 | 0.000&nbsp;/&nbsp;0.001 | 0.000&nbsp;/&nbsp;0.000 | 0.001&nbsp;/&nbsp;0.002 | 0.003&nbsp;/&nbsp;0.002 | 0.000&nbsp;/&nbsp;0.001 | 0.000&nbsp;/&nbsp;0.002 | 0.000&nbsp;/&nbsp;0.001 | 0.004&nbsp;/&nbsp;0.002 |
| ILI | 0.002&nbsp;/&nbsp;0.002 | 0.003&nbsp;/&nbsp;0.002 | 0.003&nbsp;/&nbsp;0.002 | 0.030&nbsp;/&nbsp;0.011 | 0.043&nbsp;/&nbsp;0.016 | 0.007&nbsp;/&nbsp;0.004 | 0.033&nbsp;/&nbsp;0.020 | 0.008&nbsp;/&nbsp;0.004 | 0.003&nbsp;/&nbsp;0.002 | 0.012&nbsp;/&nbsp;0.007 | 0.033&nbsp;/&nbsp;0.015 | 0.008&nbsp;/&nbsp;0.003 |
| PEMS03 | 0.000&nbsp;/&nbsp;0.001 | 0.002&nbsp;/&nbsp;0.004 | 0.002&nbsp;/&nbsp;0.003 | 0.003&nbsp;/&nbsp;0.005 | 0.001&nbsp;/&nbsp;0.001 | 0.005&nbsp;/&nbsp;0.006 | 0.002&nbsp;/&nbsp;0.003 | 0.016&nbsp;/&nbsp;0.013 | 0.002&nbsp;/&nbsp;0.004 | 0.005&nbsp;/&nbsp;0.006 | 0.006&nbsp;/&nbsp;0.006 | 0.004&nbsp;/&nbsp;0.004 |
| ItalyAir | 0.003&nbsp;/&nbsp;0.004 | 0.003&nbsp;/&nbsp;0.004 | 0.024&nbsp;/&nbsp;0.017 | 0.006&nbsp;/&nbsp;0.005 | 0.005&nbsp;/&nbsp;0.006 | 0.009&nbsp;/&nbsp;0.009 | 0.004&nbsp;/&nbsp;0.003 | 0.005&nbsp;/&nbsp;0.005 | 0.002&nbsp;/&nbsp;0.002 | 0.005&nbsp;/&nbsp;0.004 | 0.019&nbsp;/&nbsp;0.013 | 0.016&nbsp;/&nbsp;0.010 |

### Block missingness

| Dataset | Cairn (Ours) | HELIX | PSW-I | TimeMixer++ | ImputeFormer | ModernTCN | iTransformer | SAITS | PatchTST | TimesNet | DLinear | BRITS |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| ***Landslide*** | | | | | | | | | | | | |
| TN15 | 0.001&nbsp;/&nbsp;0.001 | 0.002&nbsp;/&nbsp;0.004 | 0.001&nbsp;/&nbsp;0.001 | 0.006&nbsp;/&nbsp;0.005 | 0.002&nbsp;/&nbsp;0.001 | 0.001&nbsp;/&nbsp;0.001 | 0.002&nbsp;/&nbsp;0.002 | 0.028&nbsp;/&nbsp;0.014 | 0.001&nbsp;/&nbsp;0.001 | 0.002&nbsp;/&nbsp;0.002 | 0.001&nbsp;/&nbsp;0.001 | 0.063&nbsp;/&nbsp;0.030 |
| HH60 | 0.003&nbsp;/&nbsp;0.001 | 0.001&nbsp;/&nbsp;0.001 | 0.004&nbsp;/&nbsp;0.001 | 0.002&nbsp;/&nbsp;0.002 | 0.000&nbsp;/&nbsp;0.000 | 0.001&nbsp;/&nbsp;0.001 | 0.001&nbsp;/&nbsp;0.001 | 0.009&nbsp;/&nbsp;0.005 | 0.002&nbsp;/&nbsp;0.002 | 0.001&nbsp;/&nbsp;0.000 | 0.001&nbsp;/&nbsp;0.000 | 0.051&nbsp;/&nbsp;0.018 |
| TT60 | 0.007&nbsp;/&nbsp;0.002 | 0.063&nbsp;/&nbsp;0.008 | 0.014&nbsp;/&nbsp;0.002 | 0.022&nbsp;/&nbsp;0.005 | 0.052&nbsp;/&nbsp;0.005 | 0.001&nbsp;/&nbsp;0.000 | 0.007&nbsp;/&nbsp;0.002 | 0.054&nbsp;/&nbsp;0.011 | 0.004&nbsp;/&nbsp;0.001 | 0.003&nbsp;/&nbsp;0.001 | 0.002&nbsp;/&nbsp;0.001 | 0.079&nbsp;/&nbsp;0.017 |
| XP60 | 0.002&nbsp;/&nbsp;0.000 | 0.011&nbsp;/&nbsp;0.002 | 0.036&nbsp;/&nbsp;0.004 | 0.004&nbsp;/&nbsp;0.001 | 0.032&nbsp;/&nbsp;0.008 | 0.013&nbsp;/&nbsp;0.002 | 0.012&nbsp;/&nbsp;0.002 | 0.012&nbsp;/&nbsp;0.003 | 0.003&nbsp;/&nbsp;0.000 | 0.006&nbsp;/&nbsp;0.001 | 0.018&nbsp;/&nbsp;0.003 | 0.011&nbsp;/&nbsp;0.002 |
| NZUT | 0.014&nbsp;/&nbsp;0.005 | 0.008&nbsp;/&nbsp;0.003 | 0.028&nbsp;/&nbsp;0.009 | 0.019&nbsp;/&nbsp;0.008 | 0.039&nbsp;/&nbsp;0.015 | 0.022&nbsp;/&nbsp;0.008 | 0.027&nbsp;/&nbsp;0.010 | 0.016&nbsp;/&nbsp;0.006 | 0.028&nbsp;/&nbsp;0.011 | 0.012&nbsp;/&nbsp;0.005 | 0.007&nbsp;/&nbsp;0.003 | 0.008&nbsp;/&nbsp;0.003 |
| PSMH | 0.002&nbsp;/&nbsp;0.001 | 0.009&nbsp;/&nbsp;0.003 | 0.008&nbsp;/&nbsp;0.006 | 0.057&nbsp;/&nbsp;0.021 | 0.024&nbsp;/&nbsp;0.009 | 0.004&nbsp;/&nbsp;0.003 | 0.013&nbsp;/&nbsp;0.009 | 0.136&nbsp;/&nbsp;0.036 | 0.009&nbsp;/&nbsp;0.008 | 0.008&nbsp;/&nbsp;0.006 | 0.009&nbsp;/&nbsp;0.007 | 0.013&nbsp;/&nbsp;0.004 |
| ***Public*** | | | | | | | | | | | | |
| ETTh&nbsp;Avg. | 0.006&nbsp;/&nbsp;0.005 | 0.011&nbsp;/&nbsp;0.007 | 0.005&nbsp;/&nbsp;0.003 | 0.008&nbsp;/&nbsp;0.005 | 0.013&nbsp;/&nbsp;0.009 | 0.007&nbsp;/&nbsp;0.005 | 0.016&nbsp;/&nbsp;0.011 | 0.015&nbsp;/&nbsp;0.010 | 0.001&nbsp;/&nbsp;0.001 | 0.003&nbsp;/&nbsp;0.002 | 0.006&nbsp;/&nbsp;0.004 | 0.023&nbsp;/&nbsp;0.009 |
| ETTm&nbsp;Avg. | 0.001&nbsp;/&nbsp;0.001 | 0.003&nbsp;/&nbsp;0.003 | 0.009&nbsp;/&nbsp;0.008 | 0.016&nbsp;/&nbsp;0.012 | 0.010&nbsp;/&nbsp;0.010 | 0.002&nbsp;/&nbsp;0.002 | 0.012&nbsp;/&nbsp;0.009 | 0.009&nbsp;/&nbsp;0.006 | 0.006&nbsp;/&nbsp;0.005 | 0.005&nbsp;/&nbsp;0.004 | 0.010&nbsp;/&nbsp;0.008 | 0.060&nbsp;/&nbsp;0.026 |
| ECL | 0.005&nbsp;/&nbsp;0.005 | 0.001&nbsp;/&nbsp;0.001 | 0.014&nbsp;/&nbsp;0.008 | 0.009&nbsp;/&nbsp;0.008 | 0.002&nbsp;/&nbsp;0.002 | 0.010&nbsp;/&nbsp;0.010 | 0.014&nbsp;/&nbsp;0.010 | 0.010&nbsp;/&nbsp;0.007 | 0.006&nbsp;/&nbsp;0.005 | 0.012&nbsp;/&nbsp;0.011 | 0.008&nbsp;/&nbsp;0.007 | 0.007&nbsp;/&nbsp;0.004 |
| Exchange | 0.001&nbsp;/&nbsp;0.002 | 0.000&nbsp;/&nbsp;0.001 | 0.001&nbsp;/&nbsp;0.003 | 0.003&nbsp;/&nbsp;0.003 | 0.003&nbsp;/&nbsp;0.005 | 0.001&nbsp;/&nbsp;0.003 | 0.000&nbsp;/&nbsp;0.001 | 0.015&nbsp;/&nbsp;0.011 | 0.001&nbsp;/&nbsp;0.003 | 0.001&nbsp;/&nbsp;0.002 | 0.001&nbsp;/&nbsp;0.004 | 0.055&nbsp;/&nbsp;0.026 |
| ILI | 0.003&nbsp;/&nbsp;0.001 | 0.036&nbsp;/&nbsp;0.013 | 0.028&nbsp;/&nbsp;0.009 | 0.023&nbsp;/&nbsp;0.006 | 0.059&nbsp;/&nbsp;0.015 | 0.060&nbsp;/&nbsp;0.018 | 0.033&nbsp;/&nbsp;0.010 | 0.019&nbsp;/&nbsp;0.005 | 0.012&nbsp;/&nbsp;0.004 | 0.056&nbsp;/&nbsp;0.016 | 0.013&nbsp;/&nbsp;0.004 | 0.049&nbsp;/&nbsp;0.015 |
| PEMS03 | 0.001&nbsp;/&nbsp;0.002 | 0.002&nbsp;/&nbsp;0.003 | 0.000&nbsp;/&nbsp;0.001 | 0.002&nbsp;/&nbsp;0.002 | 0.001&nbsp;/&nbsp;0.002 | 0.006&nbsp;/&nbsp;0.008 | 0.011&nbsp;/&nbsp;0.008 | 0.004&nbsp;/&nbsp;0.004 | 0.001&nbsp;/&nbsp;0.001 | 0.001&nbsp;/&nbsp;0.002 | 0.004&nbsp;/&nbsp;0.005 | 0.003&nbsp;/&nbsp;0.003 |
| ItalyAir | 0.004&nbsp;/&nbsp;0.003 | 0.006&nbsp;/&nbsp;0.005 | 0.010&nbsp;/&nbsp;0.005 | 0.019&nbsp;/&nbsp;0.010 | 0.007&nbsp;/&nbsp;0.006 | 0.014&nbsp;/&nbsp;0.010 | 0.013&nbsp;/&nbsp;0.008 | 0.003&nbsp;/&nbsp;0.002 | 0.025&nbsp;/&nbsp;0.017 | 0.011&nbsp;/&nbsp;0.006 | 0.011&nbsp;/&nbsp;0.006 | 0.007&nbsp;/&nbsp;0.003 |

### Subsequence missingness

| Dataset | Cairn (Ours) | HELIX | PSW-I | TimeMixer++ | ImputeFormer | ModernTCN | iTransformer | SAITS | PatchTST | TimesNet | DLinear | BRITS |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| ***Landslide*** | | | | | | | | | | | | |
| TN15 | 0.001&nbsp;/&nbsp;0.000 | 0.004&nbsp;/&nbsp;0.003 | 0.003&nbsp;/&nbsp;0.002 | 0.028&nbsp;/&nbsp;0.012 | 0.006&nbsp;/&nbsp;0.003 | 0.007&nbsp;/&nbsp;0.005 | 0.005&nbsp;/&nbsp;0.003 | 0.018&nbsp;/&nbsp;0.008 | 0.004&nbsp;/&nbsp;0.003 | 0.001&nbsp;/&nbsp;0.001 | 0.005&nbsp;/&nbsp;0.003 | 0.055&nbsp;/&nbsp;0.022 |
| HH60 | 0.003&nbsp;/&nbsp;0.002 | 0.014&nbsp;/&nbsp;0.008 | 0.003&nbsp;/&nbsp;0.001 | 0.023&nbsp;/&nbsp;0.011 | 0.020&nbsp;/&nbsp;0.010 | 0.001&nbsp;/&nbsp;0.001 | 0.006&nbsp;/&nbsp;0.004 | 0.042&nbsp;/&nbsp;0.018 | 0.001&nbsp;/&nbsp;0.001 | 0.004&nbsp;/&nbsp;0.002 | 0.005&nbsp;/&nbsp;0.004 | 0.014&nbsp;/&nbsp;0.004 |
| TT60 | 0.008&nbsp;/&nbsp;0.002 | 0.133&nbsp;/&nbsp;0.016 | 0.015&nbsp;/&nbsp;0.003 | 0.090&nbsp;/&nbsp;0.017 | 0.073&nbsp;/&nbsp;0.006 | 0.007&nbsp;/&nbsp;0.002 | 0.003&nbsp;/&nbsp;0.001 | 0.053&nbsp;/&nbsp;0.010 | 0.015&nbsp;/&nbsp;0.004 | 0.002&nbsp;/&nbsp;0.001 | 0.004&nbsp;/&nbsp;0.001 | 0.379&nbsp;/&nbsp;0.064 |
| XP60 | 0.005&nbsp;/&nbsp;0.001 | 0.001&nbsp;/&nbsp;0.000 | 0.043&nbsp;/&nbsp;0.005 | 0.062&nbsp;/&nbsp;0.020 | 0.009&nbsp;/&nbsp;0.003 | 0.022&nbsp;/&nbsp;0.004 | 0.016&nbsp;/&nbsp;0.003 | 0.003&nbsp;/&nbsp;0.001 | 0.020&nbsp;/&nbsp;0.003 | 0.015&nbsp;/&nbsp;0.002 | 0.025&nbsp;/&nbsp;0.004 | 0.010&nbsp;/&nbsp;0.002 |
| NZUT | 0.005&nbsp;/&nbsp;0.002 | 0.018&nbsp;/&nbsp;0.007 | 0.017&nbsp;/&nbsp;0.005 | 0.061&nbsp;/&nbsp;0.022 | 0.018&nbsp;/&nbsp;0.007 | 0.024&nbsp;/&nbsp;0.009 | 0.011&nbsp;/&nbsp;0.004 | 0.095&nbsp;/&nbsp;0.037 | 0.033&nbsp;/&nbsp;0.013 | 0.028&nbsp;/&nbsp;0.011 | 0.019&nbsp;/&nbsp;0.007 | 0.017&nbsp;/&nbsp;0.006 |
| PSMH | 0.003&nbsp;/&nbsp;0.002 | 0.006&nbsp;/&nbsp;0.002 | 0.006&nbsp;/&nbsp;0.004 | 0.156&nbsp;/&nbsp;0.045 | 0.046&nbsp;/&nbsp;0.015 | 0.008&nbsp;/&nbsp;0.006 | 0.035&nbsp;/&nbsp;0.020 | 0.034&nbsp;/&nbsp;0.009 | 0.001&nbsp;/&nbsp;0.001 | 0.014&nbsp;/&nbsp;0.010 | 0.005&nbsp;/&nbsp;0.004 | 0.029&nbsp;/&nbsp;0.008 |
| ***Public*** | | | | | | | | | | | | |
| ETTh&nbsp;Avg. | 0.007&nbsp;/&nbsp;0.006 | 0.016&nbsp;/&nbsp;0.010 | 0.033&nbsp;/&nbsp;0.013 | 0.055&nbsp;/&nbsp;0.019 | 0.014&nbsp;/&nbsp;0.006 | 0.009&nbsp;/&nbsp;0.006 | 0.026&nbsp;/&nbsp;0.015 | 0.014&nbsp;/&nbsp;0.007 | 0.026&nbsp;/&nbsp;0.016 | 0.002&nbsp;/&nbsp;0.001 | 0.020&nbsp;/&nbsp;0.012 | 0.050&nbsp;/&nbsp;0.017 |
| ETTm&nbsp;Avg. | 0.009&nbsp;/&nbsp;0.006 | 0.008&nbsp;/&nbsp;0.004 | 0.007&nbsp;/&nbsp;0.003 | 0.063&nbsp;/&nbsp;0.019 | 0.046&nbsp;/&nbsp;0.019 | 0.021&nbsp;/&nbsp;0.011 | 0.015&nbsp;/&nbsp;0.007 | 0.014&nbsp;/&nbsp;0.007 | 0.008&nbsp;/&nbsp;0.004 | 0.009&nbsp;/&nbsp;0.005 | 0.015&nbsp;/&nbsp;0.007 | 0.077&nbsp;/&nbsp;0.026 |
| ECL | 0.008&nbsp;/&nbsp;0.007 | 0.020&nbsp;/&nbsp;0.016 | 0.030&nbsp;/&nbsp;0.012 | 0.004&nbsp;/&nbsp;0.003 | 0.011&nbsp;/&nbsp;0.008 | 0.013&nbsp;/&nbsp;0.009 | 0.054&nbsp;/&nbsp;0.028 | 0.023&nbsp;/&nbsp;0.016 | 0.003&nbsp;/&nbsp;0.002 | 0.010&nbsp;/&nbsp;0.008 | 0.011&nbsp;/&nbsp;0.008 | 0.021&nbsp;/&nbsp;0.014 |
| Exchange | 0.001&nbsp;/&nbsp;0.001 | 0.004&nbsp;/&nbsp;0.002 | 0.005&nbsp;/&nbsp;0.005 | 0.052&nbsp;/&nbsp;0.018 | 0.029&nbsp;/&nbsp;0.017 | 0.002&nbsp;/&nbsp;0.003 | 0.008&nbsp;/&nbsp;0.012 | 0.010&nbsp;/&nbsp;0.006 | 0.001&nbsp;/&nbsp;0.002 | 0.004&nbsp;/&nbsp;0.005 | 0.000&nbsp;/&nbsp;0.001 | 0.091&nbsp;/&nbsp;0.027 |
| ILI | 0.014&nbsp;/&nbsp;0.007 | 0.006&nbsp;/&nbsp;0.003 | 0.023&nbsp;/&nbsp;0.006 | 0.104&nbsp;/&nbsp;0.025 | 0.021&nbsp;/&nbsp;0.009 | 0.128&nbsp;/&nbsp;0.039 | 0.102&nbsp;/&nbsp;0.026 | 0.005&nbsp;/&nbsp;0.002 | 0.013&nbsp;/&nbsp;0.004 | 0.096&nbsp;/&nbsp;0.029 | 0.064&nbsp;/&nbsp;0.019 | 0.089&nbsp;/&nbsp;0.030 |
| PEMS03 | 0.001&nbsp;/&nbsp;0.002 | 0.005&nbsp;/&nbsp;0.006 | 0.005&nbsp;/&nbsp;0.003 | 0.019&nbsp;/&nbsp;0.013 | 0.001&nbsp;/&nbsp;0.001 | 0.007&nbsp;/&nbsp;0.004 | 0.009&nbsp;/&nbsp;0.005 | 0.008&nbsp;/&nbsp;0.009 | 0.010&nbsp;/&nbsp;0.007 | 0.003&nbsp;/&nbsp;0.002 | 0.013&nbsp;/&nbsp;0.008 | 0.005&nbsp;/&nbsp;0.005 |
| ItalyAir | 0.009&nbsp;/&nbsp;0.007 | 0.008&nbsp;/&nbsp;0.006 | 0.053&nbsp;/&nbsp;0.023 | 0.013&nbsp;/&nbsp;0.005 | 0.017&nbsp;/&nbsp;0.012 | 0.009&nbsp;/&nbsp;0.006 | 0.013&nbsp;/&nbsp;0.007 | 0.006&nbsp;/&nbsp;0.005 | 0.012&nbsp;/&nbsp;0.008 | 0.047&nbsp;/&nbsp;0.028 | 0.022&nbsp;/&nbsp;0.013 | 0.033&nbsp;/&nbsp;0.015 |

### Mixed random missingness

| Dataset | Cairn (Ours) | HELIX | PSW-I | TimeMixer++ | ImputeFormer | ModernTCN | iTransformer | SAITS | PatchTST | TimesNet | DLinear | BRITS |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| ***Landslide*** | | | | | | | | | | | | |
| TN15 | 0.002&nbsp;/&nbsp;0.001 | 0.013&nbsp;/&nbsp;0.008 | 0.010&nbsp;/&nbsp;0.005 | 0.017&nbsp;/&nbsp;0.007 | 0.002&nbsp;/&nbsp;0.001 | 0.005&nbsp;/&nbsp;0.004 | 0.005&nbsp;/&nbsp;0.003 | 0.024&nbsp;/&nbsp;0.011 | 0.006&nbsp;/&nbsp;0.004 | 0.004&nbsp;/&nbsp;0.003 | 0.006&nbsp;/&nbsp;0.004 | 0.015&nbsp;/&nbsp;0.009 |
| HH60 | 0.002&nbsp;/&nbsp;0.001 | 0.003&nbsp;/&nbsp;0.002 | 0.004&nbsp;/&nbsp;0.002 | 0.066&nbsp;/&nbsp;0.030 | 0.023&nbsp;/&nbsp;0.011 | 0.002&nbsp;/&nbsp;0.001 | 0.001&nbsp;/&nbsp;0.000 | 0.049&nbsp;/&nbsp;0.020 | 0.002&nbsp;/&nbsp;0.001 | 0.002&nbsp;/&nbsp;0.001 | 0.004&nbsp;/&nbsp;0.003 | 0.095&nbsp;/&nbsp;0.027 |
| TT60 | 0.004&nbsp;/&nbsp;0.001 | 0.246&nbsp;/&nbsp;0.030 | 0.002&nbsp;/&nbsp;0.000 | 0.147&nbsp;/&nbsp;0.027 | 0.124&nbsp;/&nbsp;0.011 | 0.003&nbsp;/&nbsp;0.001 | 0.004&nbsp;/&nbsp;0.001 | 0.114&nbsp;/&nbsp;0.023 | 0.009&nbsp;/&nbsp;0.002 | 0.004&nbsp;/&nbsp;0.001 | 0.003&nbsp;/&nbsp;0.001 | 0.042&nbsp;/&nbsp;0.008 |
| XP60 | 0.011&nbsp;/&nbsp;0.002 | 0.024&nbsp;/&nbsp;0.003 | 0.032&nbsp;/&nbsp;0.003 | 0.034&nbsp;/&nbsp;0.009 | 0.008&nbsp;/&nbsp;0.002 | 0.003&nbsp;/&nbsp;0.000 | 0.006&nbsp;/&nbsp;0.001 | 0.010&nbsp;/&nbsp;0.002 | 0.028&nbsp;/&nbsp;0.004 | 0.011&nbsp;/&nbsp;0.002 | 0.010&nbsp;/&nbsp;0.001 | 0.004&nbsp;/&nbsp;0.001 |
| NZUT | 0.009&nbsp;/&nbsp;0.004 | 0.008&nbsp;/&nbsp;0.003 | 0.013&nbsp;/&nbsp;0.005 | 0.024&nbsp;/&nbsp;0.008 | 0.027&nbsp;/&nbsp;0.010 | 0.030&nbsp;/&nbsp;0.012 | 0.023&nbsp;/&nbsp;0.009 | 0.105&nbsp;/&nbsp;0.040 | 0.013&nbsp;/&nbsp;0.005 | 0.011&nbsp;/&nbsp;0.004 | 0.026&nbsp;/&nbsp;0.010 | 0.048&nbsp;/&nbsp;0.020 |
| PSMH | 0.011&nbsp;/&nbsp;0.007 | 0.026&nbsp;/&nbsp;0.010 | 0.004&nbsp;/&nbsp;0.003 | 0.062&nbsp;/&nbsp;0.019 | 0.015&nbsp;/&nbsp;0.005 | 0.010&nbsp;/&nbsp;0.007 | 0.006&nbsp;/&nbsp;0.003 | 0.021&nbsp;/&nbsp;0.006 | 0.009&nbsp;/&nbsp;0.006 | 0.013&nbsp;/&nbsp;0.009 | 0.026&nbsp;/&nbsp;0.017 | 0.027&nbsp;/&nbsp;0.007 |
| ***Public*** | | | | | | | | | | | | |
| ETTh&nbsp;Avg. | 0.008&nbsp;/&nbsp;0.008 | 0.006&nbsp;/&nbsp;0.005 | 0.007&nbsp;/&nbsp;0.004 | 0.062&nbsp;/&nbsp;0.020 | 0.024&nbsp;/&nbsp;0.010 | 0.003&nbsp;/&nbsp;0.002 | 0.009&nbsp;/&nbsp;0.006 | 0.005&nbsp;/&nbsp;0.003 | 0.004&nbsp;/&nbsp;0.003 | 0.011&nbsp;/&nbsp;0.008 | 0.015&nbsp;/&nbsp;0.010 | 0.025&nbsp;/&nbsp;0.012 |
| ETTm&nbsp;Avg. | 0.004&nbsp;/&nbsp;0.004 | 0.008&nbsp;/&nbsp;0.004 | 0.017&nbsp;/&nbsp;0.010 | 0.057&nbsp;/&nbsp;0.017 | 0.029&nbsp;/&nbsp;0.011 | 0.002&nbsp;/&nbsp;0.001 | 0.011&nbsp;/&nbsp;0.005 | 0.010&nbsp;/&nbsp;0.007 | 0.015&nbsp;/&nbsp;0.008 | 0.022&nbsp;/&nbsp;0.013 | 0.024&nbsp;/&nbsp;0.013 | 0.014&nbsp;/&nbsp;0.007 |
| ECL | 0.003&nbsp;/&nbsp;0.003 | 0.007&nbsp;/&nbsp;0.007 | 0.027&nbsp;/&nbsp;0.015 | 0.004&nbsp;/&nbsp;0.003 | 0.007&nbsp;/&nbsp;0.006 | 0.022&nbsp;/&nbsp;0.016 | 0.006&nbsp;/&nbsp;0.003 | 0.013&nbsp;/&nbsp;0.009 | 0.007&nbsp;/&nbsp;0.006 | 0.013&nbsp;/&nbsp;0.011 | 0.026&nbsp;/&nbsp;0.014 | 0.028&nbsp;/&nbsp;0.019 |
| Exchange | 0.001&nbsp;/&nbsp;0.001 | 0.023&nbsp;/&nbsp;0.011 | 0.003&nbsp;/&nbsp;0.002 | 0.030&nbsp;/&nbsp;0.009 | 0.063&nbsp;/&nbsp;0.027 | 0.002&nbsp;/&nbsp;0.004 | 0.002&nbsp;/&nbsp;0.003 | 0.047&nbsp;/&nbsp;0.026 | 0.001&nbsp;/&nbsp;0.001 | 0.001&nbsp;/&nbsp;0.002 | 0.004&nbsp;/&nbsp;0.006 | 0.025&nbsp;/&nbsp;0.009 |
| ILI | 0.001&nbsp;/&nbsp;0.001 | 0.003&nbsp;/&nbsp;0.001 | 0.029&nbsp;/&nbsp;0.008 | 0.113&nbsp;/&nbsp;0.028 | 0.014&nbsp;/&nbsp;0.008 | 0.026&nbsp;/&nbsp;0.013 | 0.058&nbsp;/&nbsp;0.019 | 0.004&nbsp;/&nbsp;0.002 | 0.017&nbsp;/&nbsp;0.010 | 0.029&nbsp;/&nbsp;0.015 | 0.092&nbsp;/&nbsp;0.039 | 0.010&nbsp;/&nbsp;0.004 |
| PEMS03 | 0.001&nbsp;/&nbsp;0.001 | 0.002&nbsp;/&nbsp;0.002 | 0.009&nbsp;/&nbsp;0.009 | 0.005&nbsp;/&nbsp;0.003 | 0.003&nbsp;/&nbsp;0.003 | 0.011&nbsp;/&nbsp;0.007 | 0.011&nbsp;/&nbsp;0.006 | 0.011&nbsp;/&nbsp;0.013 | 0.005&nbsp;/&nbsp;0.003 | 0.005&nbsp;/&nbsp;0.003 | 0.017&nbsp;/&nbsp;0.010 | 0.001&nbsp;/&nbsp;0.001 |
| ItalyAir | 0.005&nbsp;/&nbsp;0.003 | 0.006&nbsp;/&nbsp;0.005 | 0.011&nbsp;/&nbsp;0.006 | 0.011&nbsp;/&nbsp;0.005 | 0.008&nbsp;/&nbsp;0.005 | 0.011&nbsp;/&nbsp;0.008 | 0.026&nbsp;/&nbsp;0.014 | 0.006&nbsp;/&nbsp;0.006 | 0.015&nbsp;/&nbsp;0.011 | 0.003&nbsp;/&nbsp;0.002 | 0.030&nbsp;/&nbsp;0.017 | 0.009&nbsp;/&nbsp;0.006 |

## Part 2. SD for Table 3 (ablation) of the paper

Each dataset entry is the SD of the MSE averaged over the four missingness patterns; Avg. is the SD of the MSE averaged over the six landslide datasets.

| Variant | TN15 | TT60 | XP60 | HH60 | NZUT | PSMH | Avg. |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| ***Component*** | | | | | | | |
| Backbone&nbsp;only | 0.001 | 0.010 | 0.020 | 0.004 | 0.051 | 0.009 | 0.009 |
| w/o&nbsp;MAA | 0.002 | 0.007 | 0.016 | 0.001 | 0.024 | 0.007 | 0.003 |
| w/o&nbsp;MCE&nbsp;and&nbsp;CPF | 0.002 | 0.019 | 0.020 | 0.000 | 0.025 | 0.002 | 0.004 |
| Cairn&nbsp;(Ours) | 0.001 | 0.005 | 0.003 | 0.001 | 0.007 | 0.002 | 0.001 |
| ***Individual*** | | | | | | | |
| w/o&nbsp;anchoring&nbsp;(MAA) | 0.002 | 0.009 | 0.017 | 0.001 | 0.017 | 0.004 | 0.004 |
| w/o&nbsp;screening&nbsp;(MCE) | 0.005 | 0.014 | 0.007 | 0.002 | 0.032 | 0.006 | 0.007 |
| w/o&nbsp;calibration&nbsp;(CPF) | 0.002 | 0.007 | 0.015 | 0.003 | 0.022 | 0.004 | 0.004 |
| w/&nbsp;learned&nbsp;gating&nbsp;(CPF) | 0.004 | 0.010 | 0.006 | 0.001 | 0.013 | 0.008 | 0.003 |
| w/o&nbsp;variogram&nbsp;(CPF) | 0.001 | 0.005 | 0.003 | 0.004 | 0.008 | 0.012 | 0.004 |
| w/&nbsp;prior&nbsp;(CPF) | 0.005 | 0.009 | 0.006 | 0.001 | 0.022 | 0.005 | 0.004 |
