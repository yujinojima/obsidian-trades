---
title: "Trade 0007 — ETH/USDT"
type: trade
strategy: YujiCointegrationResidualReversionStrategy
pair: ETH/USDT
open_date: 2024-11-04T22:00:00+00:00
close_date: 2024-11-06T03:00:00+00:00
profit_ratio: 0.0809580389488784
outcome: clean_win
exit_reason: coint_z_reverted
exit_diagnosis: premature_exit
updated: 2026-04-25
status: active
tags:
  - trade
  - trade-journal
  - freqtrade
  - crypto
  - YujiCointegrationResidualReversionStrategy
  - strategy/YujiCointegrationResidualReversionStrategy
  - outcome/clean_win
  - exit/premature_exit
  - pair/ETHUSDT
---

## Wiki links

- **Strategy**: [[../../strategies/YujiCointegrationResidualReversionStrategy]]
- **Outcome concept**: [[../../concepts/clean-win|clean_win]]
- **Exit diagnosis**: [[../../exit-analysis/premature-exit|premature_exit]]
- **Exit reason**: [[../../exit-analysis/coint-z-reverted|coint_z_reverted]]
- **Signal family**: [[../../concepts/mean-reversion]]
- **Inferred market states at entry** (pre-Phase-1, provisional): [[../../market-states/trending-down]], [[../../market-states/high-volatility]]
- **Primitives (signal-level unavailable in v1)**: [[../../primitives/bollinger-squeeze-breakout]]

# Trade 0007 — ETH/USDT

![[../../../raw/charts/YujiCointegrationResidualReversionStrategy/trade_0007.png]]

## Trade Summary

- Pair: **ETH/USDT**
- Direction: **long**
- Entry time: 2024-11-04T22:00:00+00:00
- Exit time: 2024-11-06T03:00:00+00:00
- Entry price: 2371.21
- Exit price: 2568.31
- Stop loss (initial): 2015.53
- Profit ratio: +8.096%
- Profit absolute: 8.08995621
- Exit reason: coint_z_reverted
- Duration: 29.00h
- Enter tag: coint_long
- Min rate seen: 2365.81
- Max rate seen: 2638.0
- Max favourable excursion: +11.25%
- Max adverse excursion: -0.23%
- MFE capture ratio: 71.95%
- Exit diagnosis: **premature_exit**
- Market state at entry: `{"trend": "downtrend (EMA20<50<200)", "distance_from_ema20_pct": -2.785, "distance_from_ema50_pct": -3.474, "distance_from_ema200_pct": -4.885, "volume_vs_20bar_avg": "5.58x", "volatility_regime": "expansion (20b/50b range = 0.95)"}`

## Setup Explanation

- Entry signal tag: `coint_long` (from strategy's `populate_entry_trend`).
- Trend at prior bar: downtrend (EMA20<50<200).
- Volatility regime (20b vs 50b range): expansion (20b/50b range = 0.95).
- Price distance from EMA20 at prior close: -2.79%.
- Entry-bar volume vs trailing 20-bar avg: 5.58x.
- This section uses **only pre-entry data** (bars strictly before `open_date`) — no lookahead.

## Signal Breakdown

- Liquidity sweep: Unavailable in v2 without exported signal data
- Volume spike: yes (5.58x 20-bar avg)
- Trend state: downtrend (EMA20<50<200)
- EMA alignment: downtrend (EMA20<50<200)
- Volatility state: expansion (20b/50b range = 0.95)
- Entry distance from EMA20: -2.79%
- Entry distance from EMA50: -3.47%
- Entry distance from EMA200: -4.88%

## What Went Well

- Trade finished at +8.10% realised PnL.
- Max favourable excursion reached +11.25% in favour of the position.
- Drawdown stayed under 0.5% while the trade was open.

## What Went Wrong

- No rule flagged adversity — trade executed cleanly.

## Outcome Classification

**clean_win**

## Learning Note

This setup produced a +8.10% result in 29.0h with max adverse only -0.23%. Pattern worth replicating.
Market state at entry: downtrend (EMA20<50<200).
Volatility regime: expansion (20b/50b range = 0.95).

## Raw Trade Data

| Field | Value |
|---|---|
| pair | ETH/USDT |
| stake_amount | 99.827941 |
| max_stake_amount | 99.827941 |
| amount | 0.0421 |
| open_date | 2024-11-04 22:00:00+00:00 |
| close_date | 2024-11-06 03:00:00+00:00 |
| open_rate | 2371.21 |
| close_rate | 2568.31 |
| fee_open | 0.001 |
| fee_close | 0.001 |
| trade_duration | 1740 |
| profit_ratio | 0.0809580389488784 |
| profit_abs | 8.08995621 |
| exit_reason | coint_z_reverted |
| initial_stop_loss_abs | 2015.53 |
| initial_stop_loss_ratio | -0.15 |
| stop_loss_abs | 2015.53 |
| stop_loss_ratio | -0.15 |
| min_rate | 2365.81 |
| max_rate | 2638.0 |
| is_open | False |
| enter_tag | coint_long |
| leverage | 1.0 |
| is_short | False |
| open_timestamp | 1730757600000 |
| close_timestamp | 1730862000000 |
| funding_fees | 0.0 |
| weekday | 2 |
| _idx | 7 |
| _outcome | clean_win |
| _exit_diag | premature_exit |

## Related Trades

- [[trade_0001|Trade 0001 · ETH/USDT · +9.39% · missed_continuation]]  _(same pair)_
- [[trade_0002|Trade 0002 · ETH/USDT · +5.42% · missed_continuation]]  _(same pair)_
- [[trade_0003|Trade 0003 · ETH/USDT · -2.65% · slow_loss]]  _(same pair)_
- [[trade_0005|Trade 0005 · ETH/USDT · +26.57% · missed_continuation]]  _(same exit diagnosis)_
