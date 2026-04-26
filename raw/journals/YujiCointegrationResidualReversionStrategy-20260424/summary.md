# YujiCointegrationResidualReversionStrategy — Summary

- Trades in strategy (full): **8**
- Trades exported (mixed selection): **8**
- Wins / Losses / Zero (full): 6 / 2 / 0
- Cumulative profit_ratio sum (full, not compounded): +54.373%
- Average profit_ratio (full): +6.797%
- Median profit_ratio (full): +5.957%
- Worst / Best (full): -4.373% / +26.574%

## Outcome histogram (exported sample)

| Outcome | Count |
|---|---:|
| missed_continuation | 4 |
| slow_loss | 1 |
| noisy_win | 1 |
| bad_entry_good_idea | 1 |
| clean_win | 1 |

## Per-pair (full)

| Pair | Trades | Sum profit_ratio |
|---|---:|---:|
| ETH/USDT | 7 | +47.947% |
| LINK/USDT | 1 | +6.426% |

## Exit Analysis

- Trade count: **8**
- Average MFE: **13.60%**
- Average MAE: **-5.94%**
- Average realised profit: **6.80%**
- Average MFE capture ratio (wins only, N=6): **62.83%**
- % of trades where MFE > 2× realised: **12.50%**
- % of stop-outs where price moved favourably first: no stop exits in set

### Exit reason distribution

| Exit reason | Count | % |
|---|---:|---:|
| coint_z_reverted | 8 | 100.0% |

## Exit Efficiency

- Average MFE: **13.60%**
- Average realised profit: **6.80%**
- MFE capture ratio: **62.83%**
- Missed continuation rate: **16.67%**

## Exit Diagnosis

| Diagnosis | Count | % |
|---|---:|---:|
| efficient_exit | 1 | 12.5% |
| premature_exit | 5 | 62.5% |
| poor_entry | 1 | 12.5% |
| noise_trade | 0 | 0.0% |
| stop_loss_failure | 0 | 0.0% |
| missed_continuation | 1 | 12.5% |

## Strategy Diagnosis

### 1. Sample size
- **LOW** confidence — Only 8 trades — strategy may be selective but sample size is weak; results are statistically fragile.

### 2. Dominant exit reason
- `coint_z_reverted` accounts for 8 / 8 trades (100%).

### 3. Winners — exited too early?
- Median capture = realised PnL / MFE = **64.51%** across 6 winners → **YES — exits are leaving continuation on the table**
- `missed_continuation` count: **4** (out of 6 winners).

### 4. Losers — fast or slow?
- Not enough losers (2) to profile.

### 5. Pair / period dependence
- Top pair: **ETH/USDT** at 88% of trades → **dependent**.
- Top year: **2024** at 50% of trades → spread across years.

### 6. What should be tested next?
- Compare current `coint_z_reverted` exit against a **trailing stop**
- **Partial take-profit + runner** — scale out 50% at 1R, trail remainder
- **Time-based exit** at the median winner duration
- **Wider exit threshold** (e.g. loosen the reversion / confirmation gate)
- Generalise signal — **88%** of trades on ETH/USDT; test over the full universe to confirm portability
- Relax entry filter or widen the universe to grow sample size above 20

