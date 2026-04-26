---
title: Missed Continuation
type: concept
updated: 2026-04-25
status: active
evidence_count: 524
evidence_count_total_trades: 3300
evidence_strategies: 14
evidence_exit_diag_count: 326
cross_strategy_source: data/all_trades_dataset.csv (3300 trades, 15 strategies)
prior_source: reports/strategy_diagnosis.md (batch-20260424T123546Z)
---

# Missed Continuation

## Definition

A winning trade where realised PnL is substantially below the position's Max Favourable Excursion (MFE).
The direction was right, the entry was viable, but the exit fired before the move completed — leaving
follow-through profit on the table.

Operational threshold (v1 export): `realised_pnl / MFE < ~0.65` on a winner.

## Why it matters

In a sample with structural positive expectancy, missed continuation is the *modifiable* inefficiency.
You cannot reliably improve the entry without breaking the signal; you *can* redesign the exit to
ride more of the move. This concept is the single biggest lever for this strategy family.

Related: [[mfe-capture-ratio]].

## Evidence (4 trades)

| Strategy | Trade | Pair | Realised | MFE | Capture |
|---|---|---|---:|---:|---:|
| YujiCointegrationResidualReversionStrategy | [[../trades/YujiCointegrationResidualReversionStrategy/trade_0001]] | ETH/USDT | +9.39% | +16.08% | 58.40% |
| YujiCointegrationResidualReversionStrategy | [[../trades/YujiCointegrationResidualReversionStrategy/trade_0002]] | ETH/USDT | +5.42% | ~11% | ~49% |
| YujiCointegrationResidualReversionStrategy | [[../trades/YujiCointegrationResidualReversionStrategy/trade_0005]] | ETH/USDT | +26.57% | (see trade) | (see trade) |
| YujiCointegrationResidualReversionStrategy | [[../trades/YujiCointegrationResidualReversionStrategy/trade_0008]] | LINK/USDT | +6.43% | (see trade) | (see trade) |

## Linked strategies

- [[../strategies/YujiCointegrationResidualReversionStrategy]] — 4/6 winners carry this label (67%).

## Open questions

- Is missed-continuation regime-conditional? Do the 4 trades share a [[../market-states/compression|compression]] → expansion signature?
- Does a trailing stop beat `coint_z_reverted` on the same entries? See [[../questions/trailing-stop-vs-coint-z-reverted]].
- Would partial take-profit + runner outperform a single-target exit?

## Full-library evidence (added 2026-04-25)

Source: `data/all_trades_dataset.csv` — the complete 3,300-trade library exported from Ben's
all-trades build, covering 15 strategies across 2022-05-02 → 2026-04-20.

- **`outcome = missed_continuation`:** 524 trades (15.9% of the full library)
- **`exit_diagnosis = missed_continuation`:** 326 trades (9.9% of the full library)
- **Union (either label):** trades across 14/15 strategies (YujiSmartMoneyStrategy at N=4 has zero)
- Representative sample of 10 trades is embedded in
  [[cross-strategy-trade-library#Missed Continuations|Cross-Strategy Trade Library § Missed Continuations]]

The `outcome` and `exit_diagnosis` labels are not identical — the outcome label flags a trade
whose realised PnL fell well short of its MFE regardless of the exit type, while the exit
diagnosis flags a trade where the specific diagnostic rule attributed the shortfall to a
missed continuation (as distinct from `premature_exit`). They overlap heavily but are not
equivalent.

## Earlier batch evidence (reports/strategy_diagnosis.md, 15 strategies)

Top 5 by missed-continuation rate (missed_cont / trades, higher = worse):

| # | Strategy | Trades | Missed-cont | Rate |
|---:|---|---:|---:|---:|
| 1 | YujiVWAPMeanReversionStrategy | 920 | 7 | 0.76% |
| 2 | YujiRegimeStrategy | 219 | 53 | 24.20% |
| 3 | YujiStrategyV3 | 126 | 42 | 33.33% |
| 4 | YujiTrendRiderStrategy | 322 | 53 | 16.46% |
| 5 | YujiScalperStrategy | 288 | 89 | 30.90% |

Note: YujiVWAPMeanReversionStrategy shows the lowest missed-cont rate not because its exits are
efficient (they aren't — it has the worst MFE capture at 37.5%), but because it has a near-zero
win rate (1.8%) so almost no trades reach a favourable excursion large enough to register as
missed-continuation. Low missed-continuation rate in a losing strategy is **not** evidence of
good exits.

Top 5 by absolute missed-continuation count (raw volume, more trades affected):

| # | Strategy | Missed-cont |
|---:|---|---:|
| 1 | YujiScalperStrategy | 89 |
| 2 | YujiStrategyV2 | 87 |
| 3 | YujiMoneyMakerStrategy | 70 |
| 4 | YujiRegimeStrategy | 53 |
| 4 | YujiTrendRiderStrategy | 53 |

Missed-continuation is a **system-level** phenomenon, not a strategy-specific one. Exits
under-capture across the entire Yuji strategy family.

## Next tests

1. Replay the 4 Coint trades with a 1.5R-scale-out + trailing-remainder exit rule.
2. Cross-check MFE capture by market state once Phase 1 labeller ships (see [[CLAUDE|CLAUDE.md §8]]).
3. Apply the partial-take-profit-and-runner exit variant to the top-3 highest-count strategies
   (Scalper, V2, MoneyMaker) — largest absolute potential PnL recovery if it works.
