---
title: Current Trading Thesis
type: synthesis
updated: 2026-04-25
status: active
confidence: LOW
cross_strategy_source: reports/strategy_diagnosis.md (batch-20260424T123546Z, 15 strategies)
---

# Current Trading Thesis

> [!caution] This page evolves.
> It is the rolling synthesis of what the evidence in this vault currently supports. Every new
> strategy export or discovery-layer run should update it. Treat it as a hypothesis log, not a conclusion.

## What appears to work (low confidence)

1. **Cointegration residual z-score as an entry signal.** 6 of 8 trades profitable (75% WR),
   cumulative +54% across the 8 trades. The *entries* are viable. Evidence:
   [[../strategies/YujiCointegrationResidualReversionStrategy]].
2. **Mean-reversion signal family on ETH/USDT specifically.** 88% of the positive evidence is
   concentrated on one pair. Evidence: [[../concepts/mean-reversion]].

## What appears weak

1. **Exit logic.** 5 of 8 trades (62.5%) diagnosed [[../exit-analysis/premature-exit|premature_exit]];
   MFE capture ratio 62.83% among winners. The `coint_z_reverted` exit rule is
   leaving ~37% of favourable moves on the table. Evidence: [[../exit-analysis/coint-z-reverted]],
   [[../concepts/missed-continuation]].
2. **Pair diversification.** 88% single-pair dependence. Portability untested.
3. **Sample size.** N = 8 is too small to separate signal from luck. Any claim at this stage is
   provisional.

## What does not yet have enough evidence

- Regime dependence of the signal. The v1 export carries a rough per-trade EMA-stack snapshot but
  not composite market-state labels; until Phase 1 of the research pipeline ships,
  all regime hypotheses are inferred, not tested.
- Primitive firings at entry. Signal-level data not exported; all `wiki/primitives/*.md` pages
  are provisional with respect to this vault's evidence base.
- Walk-forward robustness. The 8 trades are drawn from a single 2022-2025 window. Whether the
  strategy holds across rolling train/test splits is the Phase 4 question.

## Highest-value next tests

1. **Trailing-stop vs `coint_z_reverted`** on the same signal set. Most leverage on expectancy,
   no new data required. See [[../questions/trailing-stop-vs-coint-z-reverted]].
2. **Portability**: run the strategy on the full Binance universe (BTC, SOL, XRP, AVAX, LINK, DOGE, ADA),
   evaluate whether expectancy holds off ETH.
3. **Regime stratification**: once Phase 1 ships, classify the 8 trades by market state — do the
   4 missed-continuation trades cluster in trending-down?
4. **Sample-size growth**: relax entry thresholds enough to get N > 30 before drawing any
   statistical conclusion.

## Low-confidence speculations

- The cointegration signal may be identifying moments of *temporary cross-asset mispricing* that
  resolve through a reversion channel, while the underlying pair continues trending on the
  longer timescale. That would explain why reversion-to-zero exits under-capture: the reversion
  happens, but the leg's own trend carries it further. If true, this strategy's natural exit is
  **not** z-reversion to zero but **z-cross through zero into the opposite extreme**, or a
  trailing stop on the pair itself.
- This is a **testable** hypothesis — see Phase 2 of the research pipeline plan.

## Full Trade Library

Source: `data/all_trades_dataset.csv` (3,300 trades, 15 strategies, 2022-05-02 → 2026-04-20).
The 15-strategy batch previously summarised via `reports/strategy_diagnosis.md` is now backed by
per-trade data with per-trade chart embeds. See [[cross-strategy-trade-library|Cross-Strategy Trade Library]]
for the representative-sample view organised by wins, losses, premature exits, missed
continuations, and stop-loss failures.

Headline distributions (from the CSV, no new metrics computed):

- **Outcomes:** fast_loss 1,074 · slow_loss 565 · missed_continuation 524 · clean_win 477 · noisy_win 331 · bad_entry_good_idea 189 · scratch 140
- **Exit diagnoses:** premature_exit 1,280 · poor_entry 668 · noise_trade 561 · efficient_exit 336 · missed_continuation 326 · stop_loss_failure 129

## Cross-Strategy Findings

Source: `reports/strategy_diagnosis.md` (batch `batch-20260424T123546Z`, 15 strategies with trades).

- **0 robust strategies.** No strategy in the 15-strategy set qualifies as `strong_entry_strong_exit`
  under the report's archetype thresholds (avg MFE ≥ 5% AND MFE capture ≥ 66%).
- **10/15 strategies flagged `early-exit`** in the diagnostic flag column — the report's
  categorical signal that the strategy's exit rule is firing prematurely. Under the strict
  `premature_exit ≥ 45%` threshold, 8/15 qualify; the remaining 2 land in the 45-60% zone via
  other diagnostic evidence.
- **Exit inefficiency is the dominant failure mode.** 13/15 strategies belong to archetypes where
  exit quality is the limiting factor (1 × strong_entry_weak_exit + 12 × fully_inefficient);
  only 2/15 (StrategyV2, Strategy) are primarily entry-bound.
- **Mean MFE capture ratio across strategies with measurable winners: ~56%** — typical strategy
  is leaving ~44% of its favourable move on the table.

### Exit problem vs entry problem — how to tell them apart

The report's archetype classification uses two thresholds: `avg MFE ≥ 5%` for entry quality,
`MFE capture ≥ 66%` for exit quality. Applied to this batch:

| Signature | Interpretation | Strategies |
|---|---|---:|
| High MFE (≥ 5%) + low capture (< 66%) | **Exit problem** — signal is good, exit wastes the move | 1 (Coint) |
| Low MFE (< 5%) + high capture (≥ 66%) | **Entry problem** — exit is doing its job but there isn't much to capture | 2 (Strategy, StrategyV2) |
| Low MFE + low capture | **Fully inefficient** — entry and exit both weak | 12 |
| High MFE + high capture | **Robust** — entry finds moves and exit captures them | **0** |

The practical implication: for the 1 strong_entry_weak_exit strategy, exit redesign
(trailing stop, partial + runner) is the lever. For the 2 weak_entry_strong_exit strategies,
exit tuning has little headroom — entry filtering or signal redesign is required. For the
12 fully_inefficient strategies, both levers need work, and neither alone will produce a
profitable strategy.

## Strategy Archetypes

Source: `reports/strategy_diagnosis.md` § Strategy Archetypes. Thresholds: avg MFE ≥ 5% = high MFE;
MFE capture ≥ 66% = high capture.

### strong_entry_weak_exit (1 strategy, 8 trades, +54.37%)

Entry signal is finding tradeable moves (avg MFE ≥ 5%), but the exit rule under-captures them
(MFE capture < 66%). Fix lever: exit redesign.

- [[../strategies/YujiCointegrationResidualReversionStrategy]] — 8 trades · avg MFE 13.60% · MFE capture 62.83% · +54.37%

### weak_entry_strong_exit (2 strategies, 459 trades, -185.81%)

Exit rule captures most of the available move (MFE capture ≥ 66%) but there isn't much move to
capture (avg MFE < 5%). Fix lever: entry filter or signal redesign.

- YujiStrategy — 107 trades · avg MFE 2.02% · MFE capture 72.73% · -79.25%
- YujiStrategyV2 — 352 trades · avg MFE 2.18% · MFE capture 67.95% · -106.56%

### fully_inefficient (12 strategies, 2833 trades, -890.79%)

Both avg MFE < 5% and MFE capture < 66%. Neither entry nor exit is working. Fix lever: both —
and neither in isolation is likely to produce viability.

- YujiTrendRiderStrategy — 322 · MFE 2.20% · cap 57.28% · +9.09%
- YujiFluidStrategy — 132 · MFE 1.82% · cap 61.81% · +1.74%
- YujiStrategyV3 — 126 · MFE 1.96% · cap 59.19% · -6.66%
- YujiFVGStrategy — 37 · MFE 1.19% · cap 46.75% · -9.75%
- YujiSmartMoneyStrategy — 4 · MFE 0.71% · cap — · -17.01%
- YujiDivergenceStrategy — 44 · MFE 2.70% · cap 65.97% · -49.98%
- YujiMultiSignalStrategy — 98 · MFE 1.22% · cap 62.73% · -65.03%
- YujiScalperStrategy — 288 · MFE 0.76% · cap 49.03% · -66.54%
- YujiRegimeStrategy — 219 · MFE 1.06% · cap 43.94% · -92.31%
- YujiInverseScalperStrategy — 411 · MFE 0.83% · cap 64.79% · -114.06%
- YujiMoneyMakerStrategy — 232 · MFE 1.65% · cap 61.35% · -122.50%
- YujiVWAPMeanReversionStrategy — 920 · MFE 0.38% · cap 37.50% · -357.78%

### robust / strong_entry_strong_exit (0 strategies)

No strategy in the 15-strategy batch meets both thresholds.

## Graveyard (if/when tests falsify)

(Empty. Nothing has been tested to negative conclusion yet.)
