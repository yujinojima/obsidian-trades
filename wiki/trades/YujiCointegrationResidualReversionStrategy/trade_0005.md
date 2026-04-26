---
title: "Trade 0005 — ETH/USDT"
type: trade
strategy: YujiCointegrationResidualReversionStrategy
pair: ETH/USDT
open_date: 2024-02-19T16:00:00+00:00
close_date: 2024-03-15T12:00:00+00:00
profit_ratio: 0.2657433184127705
outcome: missed_continuation
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
  - outcome/missed_continuation
  - exit/premature_exit
  - pair/ETHUSDT
---

## Wiki links

- **Strategy**: [[../../strategies/YujiCointegrationResidualReversionStrategy]]
- **Outcome concept**: [[../../concepts/missed-continuation|missed_continuation]]
- **Exit diagnosis**: [[../../exit-analysis/premature-exit|premature_exit]]
- **Exit reason**: [[../../exit-analysis/coint-z-reverted|coint_z_reverted]]
- **Signal family**: [[../../concepts/mean-reversion]]
- **Inferred market states at entry** (pre-Phase-1, provisional): [[../../market-states/trending-up]]
- **Primitives (signal-level unavailable in v1)**: [[../../primitives/bollinger-squeeze-breakout]]

# Trade 0005 — ETH/USDT

![[../../../raw/charts/YujiCointegrationResidualReversionStrategy/trade_0005.png]]

## Trade Summary

- Pair: **ETH/USDT**
- Direction: **long**
- Entry time: 2024-02-19T16:00:00+00:00
- Exit time: 2024-03-15T12:00:00+00:00
- Entry price: 2908.93
- Exit price: 3689.33
- Stop loss (initial): 2472.6
- Profit ratio: +26.574%
- Profit absolute: 26.54139968
- Exit reason: coint_z_reverted
- Duration: 596.00h
- Enter tag: coint_long
- Min rate seen: 2868.0
- Max rate seen: 4093.92
- Max favourable excursion: +40.74%
- Max adverse excursion: -1.41%
- MFE capture ratio: 65.24%
- Exit diagnosis: **premature_exit**
- Market state at entry: `{"trend": "uptrend (EMA20>50>200)", "distance_from_ema20_pct": 0.745, "distance_from_ema50_pct": 2.015, "distance_from_ema200_pct": 3.328, "volume_vs_20bar_avg": "0.87x", "volatility_regime": "normal (20b/50b range = 0.54)"}`

## Setup Explanation

- Entry signal tag: `coint_long` (from strategy's `populate_entry_trend`).
- Trend at prior bar: uptrend (EMA20>50>200).
- Volatility regime (20b vs 50b range): normal (20b/50b range = 0.54).
- Price distance from EMA20 at prior close: +0.74%.
- Entry-bar volume vs trailing 20-bar avg: 0.87x.
- This section uses **only pre-entry data** (bars strictly before `open_date`) — no lookahead.

## Signal Breakdown

- Liquidity sweep: Unavailable in v2 without exported signal data
- Volume spike: no (0.87x 20-bar avg)
- Trend state: uptrend (EMA20>50>200)
- EMA alignment: uptrend (EMA20>50>200)
- Volatility state: normal (20b/50b range = 0.54)
- Entry distance from EMA20: +0.74%
- Entry distance from EMA50: +2.02%
- Entry distance from EMA200: +3.33%

## What Went Well

- Trade finished at +26.57% realised PnL.
- Max favourable excursion reached +40.74% in favour of the position.
- Entry was long with EMA20>50>200 alignment at the prior bar — trend filter cooperated.

## What Went Wrong

- Adverse excursion hit -1.41% — position was underwater at some point.

## Outcome Classification

**missed_continuation**

## Learning Note

Closed at +26.57% but peaked at +40.74% — exit logic left a follow-through on the table.
Market state at entry: uptrend (EMA20>50>200).
Volatility regime: normal (20b/50b range = 0.54).

## Raw Trade Data

| Field | Value |
|---|---|
| pair | ETH/USDT |
| stake_amount | 99.776299 |
| max_stake_amount | 99.776299 |
| amount | 0.0343 |
| open_date | 2024-02-19 16:00:00+00:00 |
| close_date | 2024-03-15 12:00:00+00:00 |
| open_rate | 2908.93 |
| close_rate | 3689.33 |
| fee_open | 0.001 |
| fee_close | 0.001 |
| trade_duration | 35760 |
| profit_ratio | 0.2657433184127705 |
| profit_abs | 26.54139968 |
| exit_reason | coint_z_reverted |
| initial_stop_loss_abs | 2472.6 |
| initial_stop_loss_ratio | -0.15 |
| stop_loss_abs | 2472.6 |
| stop_loss_ratio | -0.15 |
| min_rate | 2868.0 |
| max_rate | 4093.92 |
| is_open | False |
| enter_tag | coint_long |
| leverage | 1.0 |
| is_short | False |
| open_timestamp | 1708358400000 |
| close_timestamp | 1710504000000 |
| funding_fees | 0.0 |
| weekday | 4 |
| _idx | 5 |
| _outcome | missed_continuation |
| _exit_diag | premature_exit |

## Related Trades

- [[trade_0001|Trade 0001 · ETH/USDT · +9.39% · missed_continuation]]  _(same pair)_
- [[trade_0002|Trade 0002 · ETH/USDT · +5.42% · missed_continuation]]  _(same pair)_
- [[trade_0003|Trade 0003 · ETH/USDT · -2.65% · slow_loss]]  _(same pair)_
- [[trade_0008|Trade 0008 · LINK/USDT · +6.43% · missed_continuation]]  _(same outcome)_
- [[trade_0006|Trade 0006 · ETH/USDT · -4.37% · bad_entry_good_idea]]  _(same exit diagnosis)_
