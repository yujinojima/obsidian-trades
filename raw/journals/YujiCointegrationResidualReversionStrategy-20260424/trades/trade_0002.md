---
strategy: YujiCointegrationResidualReversionStrategy
pair: ETH/USDT
date: 2023-06-10T06:00:00+00:00
open_date: 2023-06-10T06:00:00+00:00
close_date: 2023-06-21T16:00:00+00:00
profit_ratio: 0.0542054693802933
profit_abs: 5.4255849
exit_reason: coint_z_reverted
outcome: missed_continuation
exit_diagnosis: premature_exit
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

# Trade 0002 — ETH/USDT

![[trade_0002.png]]

## Trade Summary

- Pair: **ETH/USDT**
- Direction: **long**
- Entry time: 2023-06-10T06:00:00+00:00
- Exit time: 2023-06-21T16:00:00+00:00
- Entry price: 1751.19
- Exit price: 1849.81
- Stop loss (initial): 1488.52
- Profit ratio: +5.421%
- Profit absolute: 5.4255849
- Exit reason: coint_z_reverted
- Duration: 274.00h
- Enter tag: coint_long
- Min rate seen: 1626.01
- Max rate seen: 1900.0
- Max favourable excursion: +8.50%
- Max adverse excursion: -7.15%
- MFE capture ratio: 63.79%
- Exit diagnosis: **premature_exit**
- Market state at entry: `{"trend": "mixed EMAs", "distance_from_ema20_pct": -4.057, "distance_from_ema50_pct": -4.591, "distance_from_ema200_pct": -4.401, "volume_vs_20bar_avg": "7.02x", "volatility_regime": "expansion (20b/50b range = 0.95)"}`

## Setup Explanation

- Entry signal tag: `coint_long` (from strategy's `populate_entry_trend`).
- Trend at prior bar: mixed EMAs.
- Volatility regime (20b vs 50b range): expansion (20b/50b range = 0.95).
- Price distance from EMA20 at prior close: -4.06%.
- Entry-bar volume vs trailing 20-bar avg: 7.02x.
- This section uses **only pre-entry data** (bars strictly before `open_date`) — no lookahead.

## Signal Breakdown

- Liquidity sweep: Unavailable in v2 without exported signal data
- Volume spike: yes (7.02x 20-bar avg)
- Trend state: mixed EMAs
- EMA alignment: mixed EMAs
- Volatility state: expansion (20b/50b range = 0.95)
- Entry distance from EMA20: -4.06%
- Entry distance from EMA50: -4.59%
- Entry distance from EMA200: -4.40%

## What Went Well

- Trade finished at +5.42% realised PnL.
- Max favourable excursion reached +8.50% in favour of the position.

## What Went Wrong

- Adverse excursion hit -7.15% — position was underwater at some point.

## Outcome Classification

**missed_continuation**

## Learning Note

Closed at +5.42% but peaked at +8.50% — exit logic left a follow-through on the table.
Market state at entry: mixed EMAs.
Volatility regime: expansion (20b/50b range = 0.95).

## Raw Trade Data

| Field | Value |
|---|---|
| pair | ETH/USDT |
| stake_amount | 99.992949 |
| max_stake_amount | 99.992949 |
| amount | 0.0571 |
| open_date | 2023-06-10 06:00:00+00:00 |
| close_date | 2023-06-21 16:00:00+00:00 |
| open_rate | 1751.19 |
| close_rate | 1849.81 |
| fee_open | 0.001 |
| fee_close | 0.001 |
| trade_duration | 16440 |
| profit_ratio | 0.0542054693802933 |
| profit_abs | 5.4255849 |
| exit_reason | coint_z_reverted |
| initial_stop_loss_abs | 1488.52 |
| initial_stop_loss_ratio | -0.15 |
| stop_loss_abs | 1488.52 |
| stop_loss_ratio | -0.15 |
| min_rate | 1626.01 |
| max_rate | 1900.0 |
| is_open | False |
| enter_tag | coint_long |
| leverage | 1.0 |
| is_short | False |
| open_timestamp | 1686376800000 |
| close_timestamp | 1687363200000 |
| funding_fees | 0.0 |
| weekday | 2 |
| _idx | 2 |
| _outcome | missed_continuation |
| _exit_diag | premature_exit |

## Related Trades

- [[trade_0001|Trade 0001 · ETH/USDT · +9.39% · missed_continuation]]  _(same pair)_
- [[trade_0003|Trade 0003 · ETH/USDT · -2.65% · slow_loss]]  _(same pair)_
- [[trade_0004|Trade 0004 · ETH/USDT · +5.49% · noisy_win]]  _(same pair)_
- [[trade_0005|Trade 0005 · ETH/USDT · +26.57% · missed_continuation]]  _(same outcome)_
- [[trade_0008|Trade 0008 · LINK/USDT · +6.43% · missed_continuation]]  _(same outcome)_
