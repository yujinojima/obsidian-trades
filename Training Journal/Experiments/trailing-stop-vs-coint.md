---
title: "Experiment — Trailing stop vs coint_z_reverted"
type: journal-experiment
updated: 2026-04-25
status: queued
priority: HIGH
originating_pattern: premature-exit
target_strategy: YujiCointegrationResidualReversionStrategy
cycle_mode: REFINE
---

# Experiment — Trailing stop vs `coint_z_reverted`

## Hypothesis

Replacing the `coint_z_reverted` exit with a trailing stop (or hybrid partial + trail) on
`YujiCointegrationResidualReversionStrategy` improves MFE capture without worsening maximum
drawdown, holding the entry rule constant.

## Originating observation

- **Pattern:** [[../Patterns/premature-exit|Premature Exit]]
- **Evidence:** Coint strategy carries the highest premature_exit rate in the 15-strategy library
  (62.5% of trades, n=8), MFE capture 62.83%, and is the single profitable strategy in the
  batch. Fix the exit, keep the entry.

## Test setup

- **Entry rule:** unchanged — strategy's existing `populate_entry_trend`
- **Exit variants:**
  1. Trailing stop at 1.5% (tight)
  2. Trailing stop at 2.5% (medium)
  3. Trailing stop = ATR × 2 (volatility-scaled)
  4. Hybrid: partial take-profit at z=0 (current exit threshold), trail remainder
  5. Time-stop at median winner duration (≈20 hours from the library)
- **Data:** `freqtrade/user_data/data/binance/{BTC,ETH,…}-1h.feather` — 4-year history
- **Backtest runner:** `freqtrade/batch-backtest.sh` with timerange `20220101-`
- **Control:** current `coint_z_reverted` exit on the same entry set

## Success criteria

- Higher **MFE capture ratio** than the 62.83% baseline on winners
- Higher **cumulative profit_ratio sum** than +54.37%
- Same or lower **max drawdown** than the 0.42% baseline
- Same or higher **Sharpe** than 0.08 baseline

## Failure / not-success

- If capture improves but DD blows out → exit is too loose, try tighter variant
- If no variant beats baseline → trailing logic is not the right fix; revisit
  [[../../wiki/synthesis/current-trading-thesis#Low-confidence speculations|the "residual reverts while pair keeps trending" speculation]]
- If n=8 is still too small for any claim → grow sample before reading result

## Data sources (existing, no new generation needed)

- `data/all_trades_dataset.csv` — Coint trades baseline
- `freqtrade/user_data/data/binance/*.feather` — OHLCV for re-backtest
- `freqtrade/user_data/strategies/YujiCointegrationResidualReversionStrategy.py` — strategy source

## Open question

- [[../../wiki/questions/trailing-stop-vs-coint-z-reverted|Trailing stop vs coint_z_reverted (question page)]]

## Result

(pending — not yet run)

## Linked pages

- [[../Patterns/premature-exit]]
- [[../master|Training Journal master]]
- [[../Control Signals]]
