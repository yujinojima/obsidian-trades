---
title: "Trade 0004 — ETH/USDT"
type: trade
strategy: YujiCointegrationResidualReversionStrategy
pair: ETH/USDT
open_date: 2024-02-14T16:00:00+00:00
close_date: 2024-02-19T13:00:00+00:00
profit_ratio: 0.0548860065818536
outcome: noisy_win
exit_reason: coint_z_reverted
exit_diagnosis: efficient_exit
updated: 2026-04-25
status: active
tags:
  - trade
  - trade-journal
  - freqtrade
  - crypto
  - YujiCointegrationResidualReversionStrategy
  - strategy/YujiCointegrationResidualReversionStrategy
  - outcome/noisy_win
  - exit/efficient_exit
  - pair/ETHUSDT
---

## Wiki links

- **Strategy**: [[../../strategies/YujiCointegrationResidualReversionStrategy]]
- **Outcome concept**: [[../../concepts/noisy-win|noisy_win]]
- **Exit diagnosis**: [[../../exit-analysis/efficient-exit|efficient_exit]]
- **Exit reason**: [[../../exit-analysis/coint-z-reverted|coint_z_reverted]]
- **Signal family**: [[../../concepts/mean-reversion]]
- **Inferred market states at entry** (pre-Phase-1, provisional): [[../../market-states/trending-up]]
- **Primitives (signal-level unavailable in v1)**: [[../../primitives/bollinger-squeeze-breakout]]

# Trade 0004 — ETH/USDT

![[../../../raw/charts/YujiCointegrationResidualReversionStrategy/trade_0004.png]]

## Trade Summary

- Pair: **ETH/USDT**
- Direction: **long**
- Entry time: 2024-02-14T16:00:00+00:00
- Exit time: 2024-02-19T13:00:00+00:00
- Entry price: 2749.4
- Exit price: 2906.11
- Stop loss (initial): 2337.0
- Profit ratio: +5.489%
- Profit absolute: 5.48327799
- Exit reason: coint_z_reverted
- Duration: 117.00h
- Enter tag: coint_long
- Min rate seen: 2719.01
- Max rate seen: 2931.0
- Max favourable excursion: +6.61%
- Max adverse excursion: -1.11%
- MFE capture ratio: 83.10%
- Exit diagnosis: **efficient_exit**
- Market state at entry: `{"trend": "uptrend (EMA20>50>200)", "distance_from_ema20_pct": 1.905, "distance_from_ema50_pct": 3.793, "distance_from_ema200_pct": 7.463, "volume_vs_20bar_avg": "1.52x", "volatility_regime": "normal (20b/50b range = 0.57)"}`

## Setup Explanation

- Entry signal tag: `coint_long` (from strategy's `populate_entry_trend`).
- Trend at prior bar: uptrend (EMA20>50>200).
- Volatility regime (20b vs 50b range): normal (20b/50b range = 0.57).
- Price distance from EMA20 at prior close: +1.91%.
- Entry-bar volume vs trailing 20-bar avg: 1.52x.
- This section uses **only pre-entry data** (bars strictly before `open_date`) — no lookahead.

## Signal Breakdown

- Liquidity sweep: Unavailable in v2 without exported signal data
- Volume spike: yes (1.52x 20-bar avg)
- Trend state: uptrend (EMA20>50>200)
- EMA alignment: uptrend (EMA20>50>200)
- Volatility state: normal (20b/50b range = 0.57)
- Entry distance from EMA20: +1.91%
- Entry distance from EMA50: +3.79%
- Entry distance from EMA200: +7.46%

## What Went Well

- Trade finished at +5.49% realised PnL.
- Max favourable excursion reached +6.61% in favour of the position.
- Entry was long with EMA20>50>200 alignment at the prior bar — trend filter cooperated.

## What Went Wrong

- Adverse excursion hit -1.11% — position was underwater at some point.

## Outcome Classification

**noisy_win**

## Learning Note

Net positive (+5.49%) but the trade saw -1.11% adverse excursion — review stop placement to reduce pain.
Market state at entry: uptrend (EMA20>50>200).
Volatility regime: normal (20b/50b range = 0.57).

## Raw Trade Data

| Field | Value |
|---|---|
| pair | ETH/USDT |
| stake_amount | 99.80322 |
| max_stake_amount | 99.80322 |
| amount | 0.0363 |
| open_date | 2024-02-14 16:00:00+00:00 |
| close_date | 2024-02-19 13:00:00+00:00 |
| open_rate | 2749.4 |
| close_rate | 2906.11 |
| fee_open | 0.001 |
| fee_close | 0.001 |
| trade_duration | 7020 |
| profit_ratio | 0.0548860065818536 |
| profit_abs | 5.48327799 |
| exit_reason | coint_z_reverted |
| initial_stop_loss_abs | 2337.0 |
| initial_stop_loss_ratio | -0.15 |
| stop_loss_abs | 2337.0 |
| stop_loss_ratio | -0.15 |
| min_rate | 2719.01 |
| max_rate | 2931.0 |
| is_open | False |
| enter_tag | coint_long |
| leverage | 1.0 |
| is_short | False |
| open_timestamp | 1707926400000 |
| close_timestamp | 1708347600000 |
| funding_fees | 0.0 |
| weekday | 0 |
| _idx | 4 |
| _outcome | noisy_win |
| _exit_diag | efficient_exit |

## Related Trades

- [[trade_0001|Trade 0001 · ETH/USDT · +9.39% · missed_continuation]]  _(same pair)_
- [[trade_0002|Trade 0002 · ETH/USDT · +5.42% · missed_continuation]]  _(same pair)_
- [[trade_0003|Trade 0003 · ETH/USDT · -2.65% · slow_loss]]  _(same pair)_
- [[trade_0008|Trade 0008 · LINK/USDT · +6.43% · missed_continuation]]  _(similar profit)_
