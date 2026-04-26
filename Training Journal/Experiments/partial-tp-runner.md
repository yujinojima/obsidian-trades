---
title: "Experiment — Partial take-profit + runner"
type: journal-experiment
updated: 2026-04-25
status: queued
priority: HIGH
originating_pattern: missed-continuation
target_strategies: [YujiScalperStrategy, YujiStrategyV2, YujiMoneyMakerStrategy, YujiCointegrationResidualReversionStrategy]
cycle_mode: REFINE
---

# Experiment — Partial take-profit + runner

## Hypothesis

Exit 50% of position at 1R, trail the remainder with a 1.5%–2.5% trailing stop. This
preserves the positive expectancy of reaching 1R while giving the remainder room to capture
continuation moves. Should specifically reduce the `missed_continuation` outcome count.

## Originating observation

- **Pattern:** [[../Patterns/missed-continuation|Missed Continuation]]
- **Evidence:** `missed_continuation` outcome = 524 trades across the library (15.9%).
  Top-volume contributors: Scalper 89, V2 87, MoneyMaker 70. These three strategies combined
  have 246 `missed_continuation` trades — nearly half the library's total for this outcome.

## Test setup

- **Position-adjustment logic** (uses freqtrade's `adjust_trade_position` or manual partial-exit):
  1. At trade PnL = 1 × initial stop distance (1R), close 50% of position
  2. On remainder, set trailing stop to 1.5% (tight variant) or 2.5% (loose variant)
- **Entry rule:** unchanged per target strategy
- **Baseline exit:** strategy's current ROI / signal-based / stop_loss rules

## Success criteria

- **`missed_continuation` count drops by ≥ 25%** on each target strategy
- **MFE capture ratio rises** past the 66% archetype threshold for at least one target,
  potentially moving it out of the `fully_inefficient` archetype
- Cumulative profit_ratio sum improves (or at minimum stays within 10% of baseline)
- Max DD does not materially increase

## Failure / not-success

- If partial exit at 1R reduces expectancy — the winners are so few that taking half off
  early starves the runner. Fallback: try 2R partial instead, or pure trailing.
- If runner gets stopped out on pullbacks before continuation materialises — trail distance
  is too tight; widen to ATR-scaled trail.

## Data sources

- `data/all_trades_dataset.csv` — baseline `missed_continuation` counts per strategy
- Strategies: four `Yuji*Strategy.py` files listed in frontmatter
- `freqtrade/user_data/data/binance/*.feather`

## Result

(pending — not yet run)

## Linked pages

- [[../Patterns/missed-continuation]]
- [[../Patterns/premature-exit]]
- [[../Patterns/low-mfe-capture]]
- [[../master|Training Journal master]]
- [[../Control Signals]]
