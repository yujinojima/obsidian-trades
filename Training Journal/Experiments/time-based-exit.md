---
title: "Experiment — Time-based exit at median winner duration"
type: journal-experiment
updated: 2026-04-25
status: queued
priority: MEDIUM
originating_pattern: missed-continuation
target_strategies: [YujiCointegrationResidualReversionStrategy, YujiScalperStrategy, YujiStrategyV2, YujiMoneyMakerStrategy]
cycle_mode: REFINE
---

# Experiment — Time-based exit at median winner duration

## Hypothesis

Adding a hard time-stop at the median winner duration reduces `slow_loss` bleed without
cutting too many winners short. Applied across target strategies, it should compress the
loss-side distribution without materially shrinking the win-side.

## Originating observation

- **Pattern:** [[../Patterns/missed-continuation|Missed Continuation]] (secondary:
  [[../Mistakes|Mistakes]] § 4 slow_loss)
- **Evidence:** 565 `slow_loss` trades across the library (17.1%) — second-largest outcome
  bucket. Strategies with material slow_loss counts: V2 (25), Strategy (20), V3 (6),
  Regime (21), MoneyMaker (24), Scalper (40). These are trades that drift negative over
  long duration without tripping stops.

## Test setup

- **Time-stop values to sweep:**
  1. Median winner duration per strategy (from the library)
  2. Median winner duration × 0.75 (tighter)
  3. Median winner duration × 1.25 (looser)
  4. Fixed 24 bars (absolute reference)
- **Entry rule:** unchanged per target strategy
- **Other exits:** kept as-is (this test adds a time-based exit layered on existing logic)
- **Data:** `freqtrade/user_data/data/binance/*.feather`, 4-year backtest window

## Success criteria

- `slow_loss` count drops **by ≥ 30%** in each target strategy
- `missed_continuation` count does **not rise by more than 10%** (i.e., we're not closing
  winners that would have continued)
- Cumulative profit_ratio sum improves or stays flat
- Max DD does not worsen

## Failure / not-success

- If time-stop cuts winners and ROI drops — the median-winner duration is a lagging stat; a
  trade *becoming* a winner often takes longer than the average already-complete winner.
  Fallback: switch to an adverse-excursion-AND-time-based compound rule.

## Data sources

- `data/all_trades_dataset.csv` — median duration calculable from `trade_duration_min` for
  winners (`profit_ratio > 0`), per strategy
- Strategies: four `Yuji*Strategy.py` files listed in frontmatter

## Result

(pending — not yet run)

## Linked pages

- [[../Patterns/missed-continuation]]
- [[../Patterns/premature-exit]]
- [[../master|Training Journal master]]
- [[../Control Signals]]
