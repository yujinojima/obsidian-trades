---
title: "Trade 0003 — ETH/USDT"
type: trade
strategy: YujiCointegrationResidualReversionStrategy
pair: ETH/USDT
open_date: 2023-08-17T15:00:00+00:00
close_date: 2023-08-29T19:00:00+00:00
profit_ratio: -0.0264867151258156
outcome: slow_loss
exit_reason: coint_z_reverted
exit_diagnosis: poor_entry
updated: 2026-04-25
status: active
tags:
  - trade
  - trade-journal
  - freqtrade
  - crypto
  - YujiCointegrationResidualReversionStrategy
  - strategy/YujiCointegrationResidualReversionStrategy
  - outcome/slow_loss
  - exit/poor_entry
  - pair/ETHUSDT
---

## Wiki links

- **Strategy**: [[../../strategies/YujiCointegrationResidualReversionStrategy]]
- **Outcome concept**: [[../../concepts/slow-loss|slow_loss]]
- **Exit diagnosis**: [[../../exit-analysis/poor-entry|poor_entry]]
- **Exit reason**: [[../../exit-analysis/coint-z-reverted|coint_z_reverted]]
- **Signal family**: [[../../concepts/mean-reversion]]
- **Inferred market states at entry** (pre-Phase-1, provisional): [[../../market-states/trending-down]]
- **Primitives (signal-level unavailable in v1)**: [[../../primitives/bollinger-squeeze-breakout]]

# Trade 0003 — ETH/USDT

![[../../../raw/charts/YujiCointegrationResidualReversionStrategy/trade_0003.png]]

## Trade Summary

- Pair: **ETH/USDT**
- Direction: **long**
- Entry time: 2023-08-17T15:00:00+00:00
- Exit time: 2023-08-29T19:00:00+00:00
- Entry price: 1779.3
- Exit price: 1735.64
- Stop loss (initial): 1512.41
- Profit ratio: -2.649%
- Profit absolute: -2.65123163
- Exit reason: coint_z_reverted
- Duration: 292.00h
- Enter tag: coint_long
- Min rate seen: 1550.0
- Max rate seen: 1780.09
- Max favourable excursion: +0.04%
- Max adverse excursion: -12.89%
- MFE capture ratio: n/a (non-positive MFE or loss)
- Exit diagnosis: **poor_entry**
- Market state at entry: `{"trend": "downtrend (EMA20<50<200)", "distance_from_ema20_pct": -1.049, "distance_from_ema50_pct": -1.86, "distance_from_ema200_pct": -3.038, "volume_vs_20bar_avg": "1.45x", "volatility_regime": "normal (20b/50b range = 0.68)"}`

## Setup Explanation

- Entry signal tag: `coint_long` (from strategy's `populate_entry_trend`).
- Trend at prior bar: downtrend (EMA20<50<200).
- Volatility regime (20b vs 50b range): normal (20b/50b range = 0.68).
- Price distance from EMA20 at prior close: -1.05%.
- Entry-bar volume vs trailing 20-bar avg: 1.45x.
- This section uses **only pre-entry data** (bars strictly before `open_date`) — no lookahead.

## Signal Breakdown

- Liquidity sweep: Unavailable in v2 without exported signal data
- Volume spike: no (1.45x 20-bar avg)
- Trend state: downtrend (EMA20<50<200)
- EMA alignment: downtrend (EMA20<50<200)
- Volatility state: normal (20b/50b range = 0.68)
- Entry distance from EMA20: -1.05%
- Entry distance from EMA50: -1.86%
- Entry distance from EMA200: -3.04%

## What Went Well

- No positive rule matched — treat the win (if any) as unexplained noise.

## What Went Wrong

- Adverse excursion hit -12.89% — position was underwater at some point.

## Outcome Classification

**slow_loss**

## Learning Note

Trade bled out over 292.0h before exit — review exit criteria or time-based filter.
Market state at entry: downtrend (EMA20<50<200).
Volatility regime: normal (20b/50b range = 0.68).

## Raw Trade Data

| Field | Value |
|---|---|
| pair | ETH/USDT |
| stake_amount | 99.99666 |
| max_stake_amount | 99.99666 |
| amount | 0.0562 |
| open_date | 2023-08-17 15:00:00+00:00 |
| close_date | 2023-08-29 19:00:00+00:00 |
| open_rate | 1779.3 |
| close_rate | 1735.64 |
| fee_open | 0.001 |
| fee_close | 0.001 |
| trade_duration | 17520 |
| profit_ratio | -0.0264867151258156 |
| profit_abs | -2.65123163 |
| exit_reason | coint_z_reverted |
| initial_stop_loss_abs | 1512.41 |
| initial_stop_loss_ratio | -0.15 |
| stop_loss_abs | 1512.41 |
| stop_loss_ratio | -0.15 |
| min_rate | 1550.0 |
| max_rate | 1780.09 |
| is_open | False |
| enter_tag | coint_long |
| leverage | 1.0 |
| is_short | False |
| open_timestamp | 1692284400000 |
| close_timestamp | 1693335600000 |
| funding_fees | 0.0 |
| weekday | 1 |
| _idx | 3 |
| _outcome | slow_loss |
| _exit_diag | poor_entry |

## Related Trades

- [[trade_0001|Trade 0001 · ETH/USDT · +9.39% · missed_continuation]]  _(same pair)_
- [[trade_0002|Trade 0002 · ETH/USDT · +5.42% · missed_continuation]]  _(same pair)_
- [[trade_0004|Trade 0004 · ETH/USDT · +5.49% · noisy_win]]  _(same pair)_
