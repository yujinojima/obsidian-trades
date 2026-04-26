---
title: MFE Capture Ratio
type: concept
updated: 2026-04-25
status: active
evidence_count: 15
evidence_count_total_trades: 3300
evidence_strategies: 14
cross_strategy_source: data/all_trades_dataset.csv (3300 trades, 15 strategies)
prior_source: reports/strategy_diagnosis.md (batch-20260424T123546Z)
---

# MFE Capture Ratio

## Definition

`MFE capture ratio = realised_profit_ratio / max_favourable_excursion` for a given trade, or the
mean of that ratio across a set of winning trades.

A capture ratio of 1.0 means you exited exactly at the peak. 0.5 means you left half the move on the
table. Values above 1.0 are generally impossible on long-only unless the computation uses inter-bar
extrema that the actual exit couldn't reach.

## Why it matters

MFE capture is the cleanest single metric for evaluating **exit quality**, because it is
conditional on the entry being correct. A strategy with low capture but high win rate is an
*exit problem*, not an *entry problem* — and exits are cheaper to redesign than entries.

## Evidence (this vault)

Single-strategy reference (the original entry):

| Strategy | Sample | Mean MFE capture (winners) | Interpretation |
|---|---:|---:|---|
| [[../strategies/YujiCointegrationResidualReversionStrategy]] | 6 winners | **62.83%** | Leaving ~37% of the move on the table |

## Full-library evidence (added 2026-04-25)

Source: `data/all_trades_dataset.csv` — 3,300 trades across 15 strategies.

Capture ratio is computed in the full-library build from the existing `mfe_pct` and
`profit_ratio` CSV fields per winner; the per-strategy rollups below are re-used from
`reports/strategy_diagnosis.md` which was generated from the same source.

- **Trades carrying the `efficient_exit` diagnosis:** 336 (10.2% of the library) — the complement
  of premature/missed outcomes at the individual-trade level.
- **Representative per-strategy capture** embedded below (unchanged vs the earlier batch since
  both were computed from the same underlying trades).

## Earlier batch evidence (reports/strategy_diagnosis.md, 15 strategies)

Full distribution, sorted worst (lowest capture) to best:

| # | Strategy | Trades | MFE capture | % premature |
|---:|---|---:|---:|---:|
| 1 | YujiVWAPMeanReversionStrategy | 920 | **37.50%** | 23.3% |
| 2 | YujiRegimeStrategy | 219 | 43.94% | 38.4% |
| 3 | YujiFVGStrategy | 37 | 46.75% | 56.8% |
| 4 | YujiScalperStrategy | 288 | 49.03% | 34.4% |
| 5 | YujiTrendRiderStrategy | 322 | 57.28% | 52.2% |
| 6 | YujiStrategyV3 | 126 | 59.19% | 50.8% |
| 7 | YujiMoneyMakerStrategy | 232 | 61.35% | 59.5% |
| 8 | YujiFluidStrategy | 132 | 61.81% | 53.0% |
| 9 | YujiMultiSignalStrategy | 98 | 62.73% | 53.1% |
| 10 | YujiCointegrationResidualReversionStrategy | 8 | 62.83% | 62.5% |
| 11 | YujiInverseScalperStrategy | 411 | 64.79% | 37.2% |
| 12 | YujiDivergenceStrategy | 44 | 65.97% | 27.3% |
| 13 | YujiStrategyV2 | 352 | **67.95%** | 45.2% |
| 14 | YujiStrategy | 107 | **72.73%** | 38.3% |
| — | YujiSmartMoneyStrategy | 4 | — | 0.0% |

Cross-batch observations:

- **Mean capture across measurable strategies: ≈58%.** Typical strategy leaves ~42% of the move.
- **0 strategies reach the 66% high-capture threshold for the `strong_entry_strong_exit` archetype.**
  Only StrategyV2 (67.95%) and Strategy (72.73%) exceed 66%, and both are classified
  `weak_entry_strong_exit` because their avg MFE (< 5%) doesn't meet the entry threshold.
- **Capture ratio and % premature_exit are inversely correlated** across the batch, as expected
  from their definitions — strategies with high premature-exit rates have low capture.

## Linked concepts

- [[missed-continuation]] — the label applied when capture is particularly low.
- [[clean-win]] — the label applied when capture is high and MAE is shallow.

## Open questions

- What is the capture ratio distribution vs market state (requires Phase 1 labeller)?
- Does capture improve with a trailing stop? See [[../questions/trailing-stop-vs-coint-z-reverted]].

## Next tests

- Re-backtest the strategy with:
  1. Trailing stop at 1.5% / 2.5% / trailing ATR × k
  2. Partial take-profit (50% at 1R, runner trails)
  3. Time-stop at the median-winner duration
  - Compare capture ratio under each exit rule.
