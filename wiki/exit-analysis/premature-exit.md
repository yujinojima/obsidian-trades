---
title: premature_exit (exit diagnosis)
type: exit-diagnosis
updated: 2026-04-25
status: active
evidence_count: 1280
evidence_count_total_trades: 3300
evidence_strategies: 14
cross_strategy_source: data/all_trades_dataset.csv (3300 trades, 15 strategies)
prior_source: reports/strategy_diagnosis.md (batch-20260424T123546Z)
---

# Exit Diagnosis — `premature_exit`

## Definition

A code-level diagnostic label applied to trades whose exit fired well before the extremum of
their favourable excursion — characterised by `(MFE - realised) / MFE` being large and positive.
Distinct from the outcome label [[../concepts/missed-continuation|missed_continuation]], which is the *consequence* in
the trade's outcome classification.

## Why it matters

The ratio of trades flagged premature_exit is the single most actionable exit-quality metric in
this vault. When premature_exit dominates (62.5% in this sample), the strategy's expectancy is
being capped by exit logic, not entry logic.

## Evidence (5 trades, all from YujiCointegrationResidualReversionStrategy)

- [[../trades/YujiCointegrationResidualReversionStrategy/trade_0001]] · +9.39% (MFE +16.08%, capture 58.4%)
- [[../trades/YujiCointegrationResidualReversionStrategy/trade_0002]] · +5.42%
- [[../trades/YujiCointegrationResidualReversionStrategy/trade_0005]] · +26.57%
- [[../trades/YujiCointegrationResidualReversionStrategy/trade_0007]] · +8.10%
- [[../trades/YujiCointegrationResidualReversionStrategy/trade_0008]] · +6.43%

## Linked concepts

- [[../concepts/missed-continuation]] — 4 of the 5 premature_exit trades are also labelled missed_continuation.
- [[../concepts/mfe-capture-ratio]].

## Linked strategies

- [[../strategies/YujiCointegrationResidualReversionStrategy]] — 5/8 trades diagnosed premature_exit.

## Full-library evidence (added 2026-04-25)

Source: `data/all_trades_dataset.csv` — 3,300 trades across 15 strategies, 2022-05-02 →
2026-04-20.

- **`exit_diagnosis = premature_exit`:** **1,280 trades** (38.8% of the full library)
- **Most common exit diagnosis in the library** — larger than `poor_entry` (668),
  `noise_trade` (561), and `efficient_exit` (336) combined only slightly.
- Representative sample of 10 trades (ranked by `mfe_pct − profit_ratio` gap) is embedded in
  [[../synthesis/cross-strategy-trade-library#Premature Exits|Cross-Strategy Trade Library § Premature Exits]]

The 1,280 count from the full library now replaces the earlier estimated 1,280 from
`reports/strategy_diagnosis.md` — they happen to match because the diagnosis labels were
generated from the same underlying trade data. The full-library CSV is the authoritative source.

## Earlier batch evidence (reports/strategy_diagnosis.md, 15 strategies)

**10 of 15 strategies carry the report's `early-exit` flag** — the headline cross-strategy
finding. Under the stricter `% premature ≥ 45%` threshold, 8 of 15 qualify.

Top 5 by premature-exit rate (strategies where elevated premature-exit is strongest):

| # | Strategy | Trades | % premature | Flag |
|---:|---|---:|---:|---|
| 1 | YujiCointegrationResidualReversionStrategy | 8 | 62.5% | early-exit |
| 2 | YujiMoneyMakerStrategy | 232 | 59.5% | early-exit |
| 3 | YujiFVGStrategy | 37 | 56.8% | early-exit |
| 4 | YujiMultiSignalStrategy | 98 | 53.1% | early-exit |
| 5 | YujiFluidStrategy | 132 | 53.0% | early-exit |

Top 5 by absolute premature-exit count (volume affected):

| # | Strategy | Trades | % premature | Est. premature trades |
|---:|---|---:|---:|---:|
| 1 | YujiVWAPMeanReversionStrategy | 920 | 23.3% | ~214 |
| 2 | YujiTrendRiderStrategy | 322 | 52.2% | ~168 |
| 3 | YujiStrategyV2 | 352 | 45.2% | ~159 |
| 4 | YujiInverseScalperStrategy | 411 | 37.2% | ~153 |
| 5 | YujiMoneyMakerStrategy | 232 | 59.5% | ~138 |

Premature-exit is the **dominant failure mode** of the Yuji strategy family in this batch.
See [[../synthesis/current-trading-thesis#Cross-Strategy Findings]].

## Open questions

See [[../questions/trailing-stop-vs-coint-z-reverted]].
