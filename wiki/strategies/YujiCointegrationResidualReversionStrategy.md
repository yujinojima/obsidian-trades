---
title: YujiCointegrationResidualReversionStrategy
type: strategy
updated: 2026-04-25
status: active
total_trades: 8
win_rate: 0.75
profit_sum_pct: 54.373
confidence: LOW
---

# YujiCointegrationResidualReversionStrategy

> [!caution] Provisional — sample size = 8
> Results are statistically fragile. Treat all claims below as hypotheses, not conclusions.

## One-line summary

Long / short ETH and LINK against a cointegration partner when the residual z-score stretches,
exit when the residual reverts to the mean.

## Headline numbers (full set, not compounded)

| Metric | Value |
|---|---|
| Total trades | **8** |
| Wins / Losses / Zero | 6 / 2 / 0 |
| Win rate | 75.00% |
| Cumulative profit_ratio | +54.373% |
| Average profit_ratio | +6.797% |
| Median profit_ratio | +5.957% |
| Worst / Best | -4.373% / +26.574% |
| Average MFE | +13.60% |
| Average MAE | -5.94% |
| MFE capture ratio (winners) | 62.83% |
| Missed-continuation rate | 16.67% |
| Sample-size confidence | **LOW** |

## Dominance

- **Pair:** ETH/USDT at **88%** of trades (7/8) — pair-dependent. See [[../concepts/mean-reversion]] for the signal family.
- **Year:** 2024 at **50%** of trades (4/8) — spread across years.
- **Exit reason:** `coint_z_reverted` at **100%** — exit is entirely concentrated. See [[../exit-analysis/coint-z-reverted]].

## Outcome distribution (this export)

| Outcome | Count | Page |
|---|---:|---|
| missed_continuation | 4 | [[../concepts/missed-continuation]] |
| slow_loss | 1 | [[../concepts/slow-loss]] |
| noisy_win | 1 | [[../concepts/noisy-win]] |
| bad_entry_good_idea | 1 | [[../concepts/bad-entry-good-idea]] |
| clean_win | 1 | [[../concepts/clean-win]] |

## Exit diagnosis distribution

| Diagnosis | Count | % | Page |
|---|---:|---:|---|
| premature_exit | 5 | 62.5% | [[../exit-analysis/premature-exit]] |
| efficient_exit | 1 | 12.5% | [[../exit-analysis/efficient-exit]] |
| poor_entry | 1 | 12.5% | [[../exit-analysis/poor-entry]] |
| missed_continuation | 1 | 12.5% | [[../concepts/missed-continuation]] |

## Most informative finding

**Exits are leaving continuation on the table.** Median capture = realised / MFE = 64.51% across
6 winners; 4 of those 6 winners carry the `missed_continuation` label. The signal is correct
more often than not, but the `coint_z_reverted` exit trigger fires before the move completes.

## What should be tested next

1. **Trailing stop vs coint_z_reverted** on the same signal set.
2. **Partial take-profit + runner** — scale 50% at 1R, trail remainder.
3. **Time-based exit** at median winner duration.
4. **Wider reversion threshold** — loosen the exit gate.
5. **Portability** — does the strategy hold on non-ETH pairs at useful sample size?
6. **Grow N to > 20** — relax entry filter or widen universe.

## Trade index

| # | Pair | Opened | Closed | PnL % | Outcome | Page |
|---:|---|---|---|---:|---|---|
| 0001 | ETH/USDT | 2022-11-09 | 2022-11-30 | +9.39 | missed_continuation | [[../trades/YujiCointegrationResidualReversionStrategy/trade_0001]] |
| 0002 | ETH/USDT | 2023-06-10 | 2023-06-21 | +5.42 | missed_continuation | [[../trades/YujiCointegrationResidualReversionStrategy/trade_0002]] |
| 0003 | ETH/USDT | 2023-08-17 | 2023-08-29 | -2.65 | slow_loss | [[../trades/YujiCointegrationResidualReversionStrategy/trade_0003]] |
| 0004 | ETH/USDT | 2024-02-14 | 2024-02-19 | +5.49 | noisy_win | [[../trades/YujiCointegrationResidualReversionStrategy/trade_0004]] |
| 0005 | ETH/USDT | 2024-02-19 | 2024-03-15 | +26.57 | missed_continuation | [[../trades/YujiCointegrationResidualReversionStrategy/trade_0005]] |
| 0006 | ETH/USDT | 2024-05-21 | 2024-06-11 | -4.37 | bad_entry_good_idea | [[../trades/YujiCointegrationResidualReversionStrategy/trade_0006]] |
| 0007 | ETH/USDT | 2024-11-04 | 2024-11-06 | +8.10 | clean_win | [[../trades/YujiCointegrationResidualReversionStrategy/trade_0007]] |
| 0008 | LINK/USDT | 2025-10-10 | 2025-10-29 | +6.43 | missed_continuation | [[../trades/YujiCointegrationResidualReversionStrategy/trade_0008]] |

## Related pages

- Concepts: [[../concepts/mean-reversion]] · [[../concepts/missed-continuation]] · [[../concepts/mfe-capture-ratio]]
- Exit analysis: [[../exit-analysis/coint-z-reverted]] · [[../exit-analysis/premature-exit]]
- Primitives (signal-level unavailable in v1): [[../primitives/bollinger-squeeze-breakout]]
- Market states (unlabelled until Phase 1): [[../market-states/compression]] · [[../market-states/trending-down]]
- Synthesis: [[../synthesis/current-trading-thesis]]
- Raw source: `raw/journals/YujiCointegrationResidualReversionStrategy-20260424/`
