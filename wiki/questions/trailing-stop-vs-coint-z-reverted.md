---
title: Trailing Stop vs coint_z_reverted
type: question
updated: 2026-04-25
status: open
---

# Question — Trailing stop vs `coint_z_reverted`

## The question

Does replacing the `coint_z_reverted` exit with a trailing stop (or a hybrid
"partial at z=0, runner trails") produce higher expectancy on the same entry signal set?

## Why it matters

[[../exit-analysis/coint-z-reverted]] accounts for 100% of exits in the sample and produces
[[../exit-analysis/premature-exit|premature_exit]] diagnosis on 5/8 trades. This is the single
most-improvable variable in the strategy.

## How to answer

Re-backtest [[../strategies/YujiCointegrationResidualReversionStrategy]] on the same
entry rule but swap exits through:

1. Trailing stop at 1.5% (tight) / 2.5% (medium) / `trailing ATR × 2` (volatility-scaled).
2. Partial take at z=0, trail remainder.
3. Time-stop at median winner duration.

Compare:

- Per-trade realised PnL
- MFE capture ratio
- Missed-continuation rate
- Max drawdown

## Data available

- 4-year 1h BTC/ETH feathers already present in `freqtrade/user_data/data/binance/`.
- Strategy source at `freqtrade/user_data/strategies/YujiCointegrationResidualReversionStrategy.py`.
- Existing batch runner at `freqtrade/batch-backtest.sh`.

## Status

Open. Not started. Next up after research-pipeline Phases 0–2 ship (Phase 2 outcome labeller
will let us compare exit variants on the same MFE/MAE basis).

## Resolution

(pending)
