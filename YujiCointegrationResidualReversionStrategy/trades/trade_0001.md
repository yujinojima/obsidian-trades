---
strategy: YujiCointegrationResidualReversionStrategy
pair: ETH/USDT
date: 2022-11-09T16:00:00+00:00
open_date: 2022-11-09T16:00:00+00:00
close_date: 2022-11-30T01:00:00+00:00
profit_ratio: 0.0938874886040537
profit_abs: 9.3890607
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

# Trade 0001 — ETH/USDT

![[trade_0001.png]]

## Trade Summary

- Pair: **ETH/USDT**
- Direction: **long**
- Entry time: 2022-11-09T16:00:00+00:00
- Exit time: 2022-11-30T01:00:00+00:00
- Entry price: 1163.02
- Exit price: 1274.76
- Stop loss (initial): 988.57
- Profit ratio: +9.389%
- Profit absolute: 9.3890607
- Exit reason: coint_z_reverted
- Duration: 489.00h
- Enter tag: coint_long
- Min rate seen: 1073.53
- Max rate seen: 1350.0
- Max favourable excursion: +16.08%
- Max adverse excursion: -7.69%
- MFE capture ratio: 58.40%
- Exit diagnosis: **premature_exit**
- Market state at entry: `{"trend": "downtrend (EMA20<50<200)", "distance_from_ema20_pct": -8.852, "distance_from_ema50_pct": -15.706, "distance_from_ema200_pct": -24.332, "volume_vs_20bar_avg": "1.61x", "volatility_regime": "compression (20b/50b range = 0.44)"}`

## Setup Explanation

- Entry signal tag: `coint_long` (from strategy's `populate_entry_trend`).
- Trend at prior bar: downtrend (EMA20<50<200).
- Volatility regime (20b vs 50b range): compression (20b/50b range = 0.44).
- Price distance from EMA20 at prior close: -8.85%.
- Entry-bar volume vs trailing 20-bar avg: 1.61x.
- This section uses **only pre-entry data** (bars strictly before `open_date`) — no lookahead.

## Signal Breakdown

- Liquidity sweep: Unavailable in v2 without exported signal data
- Volume spike: yes (1.61x 20-bar avg)
- Trend state: downtrend (EMA20<50<200)
- EMA alignment: downtrend (EMA20<50<200)
- Volatility state: compression (20b/50b range = 0.44)
- Entry distance from EMA20: -8.85%
- Entry distance from EMA50: -15.71%
- Entry distance from EMA200: -24.33%

## What Went Well

- Trade finished at +9.39% realised PnL.
- Max favourable excursion reached +16.08% in favour of the position.

## What Went Wrong

- Adverse excursion hit -7.69% — position was underwater at some point.

## Outcome Classification

**missed_continuation**

## Learning Note

Closed at +9.39% but peaked at +16.08% — exit logic left a follow-through on the table.
Market state at entry: downtrend (EMA20<50<200).
Volatility regime: compression (20b/50b range = 0.44).

## Raw Trade Data

| Field | Value |
|---|---|
| pair | ETH/USDT |
| stake_amount | 99.903418 |
| max_stake_amount | 99.903418 |
| amount | 0.0859 |
| open_date | 2022-11-09 16:00:00+00:00 |
| close_date | 2022-11-30 01:00:00+00:00 |
| open_rate | 1163.02 |
| close_rate | 1274.76 |
| fee_open | 0.001 |
| fee_close | 0.001 |
| trade_duration | 29340 |
| profit_ratio | 0.0938874886040537 |
| profit_abs | 9.3890607 |
| exit_reason | coint_z_reverted |
| initial_stop_loss_abs | 988.57 |
| initial_stop_loss_ratio | -0.15 |
| stop_loss_abs | 988.57 |
| stop_loss_ratio | -0.15 |
| min_rate | 1073.53 |
| max_rate | 1350.0 |
| is_open | False |
| enter_tag | coint_long |
| leverage | 1.0 |
| is_short | False |
| open_timestamp | 1668009600000 |
| close_timestamp | 1669770000000 |
| funding_fees | 0.0 |
| weekday | 2 |
| _idx | 1 |
| _outcome | missed_continuation |
| _exit_diag | premature_exit |

## Related Trades

- [[trade_0002|Trade 0002 · ETH/USDT · +5.42% · missed_continuation]]  _(same pair)_
- [[trade_0003|Trade 0003 · ETH/USDT · -2.65% · slow_loss]]  _(same pair)_
- [[trade_0004|Trade 0004 · ETH/USDT · +5.49% · noisy_win]]  _(same pair)_
- [[trade_0005|Trade 0005 · ETH/USDT · +26.57% · missed_continuation]]  _(same outcome)_
- [[trade_0008|Trade 0008 · LINK/USDT · +6.43% · missed_continuation]]  _(same outcome)_
