---
title: "Trade 0006 — ETH/USDT"
type: trade
strategy: YujiCointegrationResidualReversionStrategy
pair: ETH/USDT
open_date: 2024-05-21T11:00:00+00:00
close_date: 2024-06-11T06:00:00+00:00
profit_ratio: -0.0437250642719737
outcome: bad_entry_good_idea
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
  - outcome/bad_entry_good_idea
  - exit/premature_exit
  - pair/ETHUSDT
---

## Wiki links

- **Strategy**: [[../../strategies/YujiCointegrationResidualReversionStrategy]]
- **Outcome concept**: [[../../concepts/bad-entry-good-idea|bad_entry_good_idea]]
- **Exit diagnosis**: [[../../exit-analysis/premature-exit|premature_exit]]
- **Exit reason**: [[../../exit-analysis/coint-z-reverted|coint_z_reverted]]
- **Signal family**: [[../../concepts/mean-reversion]]
- **Inferred market states at entry** (pre-Phase-1, provisional): [[../../market-states/trending-up]], [[../../market-states/high-volatility]]
- **Primitives (signal-level unavailable in v1)**: [[../../primitives/bollinger-squeeze-breakout]]

# Trade 0006 — ETH/USDT

![[../../../raw/charts/YujiCointegrationResidualReversionStrategy/trade_0006.png]]

## Trade Summary

- Pair: **ETH/USDT**
- Direction: **long**
- Entry time: 2024-05-21T11:00:00+00:00
- Exit time: 2024-06-11T06:00:00+00:00
- Entry price: 3717.0
- Exit price: 3561.59
- Stop loss (initial): 3159.45
- Profit ratio: -4.373%
- Profit absolute: -4.37632307
- Exit reason: coint_z_reverted
- Duration: 499.00h
- Enter tag: coint_long
- Min rate seen: 3498.0
- Max rate seen: 3977.0
- Max favourable excursion: +6.99%
- Max adverse excursion: -5.89%
- MFE capture ratio: n/a (non-positive MFE or loss)
- Exit diagnosis: **premature_exit**
- Market state at entry: `{"trend": "uptrend (EMA20>50>200)", "distance_from_ema20_pct": 4.709, "distance_from_ema50_pct": 10.626, "distance_from_ema200_pct": 17.917, "volume_vs_20bar_avg": "0.95x", "volatility_regime": "expansion (20b/50b range = 0.94)"}`

## Setup Explanation

- Entry signal tag: `coint_long` (from strategy's `populate_entry_trend`).
- Trend at prior bar: uptrend (EMA20>50>200).
- Volatility regime (20b vs 50b range): expansion (20b/50b range = 0.94).
- Price distance from EMA20 at prior close: +4.71%.
- Entry-bar volume vs trailing 20-bar avg: 0.95x.
- This section uses **only pre-entry data** (bars strictly before `open_date`) — no lookahead.

## Signal Breakdown

- Liquidity sweep: Unavailable in v2 without exported signal data
- Volume spike: no (0.95x 20-bar avg)
- Trend state: uptrend (EMA20>50>200)
- EMA alignment: uptrend (EMA20>50>200)
- Volatility state: expansion (20b/50b range = 0.94)
- Entry distance from EMA20: +4.71%
- Entry distance from EMA50: +10.63%
- Entry distance from EMA200: +17.92%

## What Went Well

- Max favourable excursion reached +6.99% in favour of the position.

## What Went Wrong

- Adverse excursion hit -5.89% — position was underwater at some point.
- Was in profit (+6.99%) before reversing into a loss — missed exit.
- Volatility was already expanding — chased the move into reversal.

## Outcome Classification

**bad_entry_good_idea**

## Learning Note

Had +6.99% in favour before reversing; directional thesis was right but entry timing was poor.
Market state at entry: uptrend (EMA20>50>200).
Volatility regime: expansion (20b/50b range = 0.94).

## Raw Trade Data

| Field | Value |
|---|---|
| pair | ETH/USDT |
| stake_amount | 99.9873 |
| max_stake_amount | 99.9873 |
| amount | 0.0269 |
| open_date | 2024-05-21 11:00:00+00:00 |
| close_date | 2024-06-11 06:00:00+00:00 |
| open_rate | 3717.0 |
| close_rate | 3561.59 |
| fee_open | 0.001 |
| fee_close | 0.001 |
| trade_duration | 29940 |
| profit_ratio | -0.0437250642719737 |
| profit_abs | -4.37632307 |
| exit_reason | coint_z_reverted |
| initial_stop_loss_abs | 3159.45 |
| initial_stop_loss_ratio | -0.15 |
| stop_loss_abs | 3159.45 |
| stop_loss_ratio | -0.15 |
| min_rate | 3498.0 |
| max_rate | 3977.0 |
| is_open | False |
| enter_tag | coint_long |
| leverage | 1.0 |
| is_short | False |
| open_timestamp | 1716289200000 |
| close_timestamp | 1718085600000 |
| funding_fees | 0.0 |
| weekday | 1 |
| _idx | 6 |
| _outcome | bad_entry_good_idea |
| _exit_diag | premature_exit |

## Related Trades

- [[trade_0001|Trade 0001 · ETH/USDT · +9.39% · missed_continuation]]  _(same pair)_
- [[trade_0002|Trade 0002 · ETH/USDT · +5.42% · missed_continuation]]  _(same pair)_
- [[trade_0003|Trade 0003 · ETH/USDT · -2.65% · slow_loss]]  _(same pair)_
- [[trade_0005|Trade 0005 · ETH/USDT · +26.57% · missed_continuation]]  _(same exit diagnosis)_
