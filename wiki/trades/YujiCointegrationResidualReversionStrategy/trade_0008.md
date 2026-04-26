---
title: "Trade 0008 — LINK/USDT"
type: trade
strategy: YujiCointegrationResidualReversionStrategy
pair: LINK/USDT
open_date: 2025-10-10T22:00:00+00:00
close_date: 2025-10-29T19:00:00+00:00
profit_ratio: 0.0642618251313903
outcome: missed_continuation
exit_reason: coint_z_reverted
exit_diagnosis: missed_continuation
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
  - exit/missed_continuation
  - pair/LINKUSDT
---

## Wiki links

- **Strategy**: [[../../strategies/YujiCointegrationResidualReversionStrategy]]
- **Outcome concept**: [[../../concepts/missed-continuation|missed_continuation]]
- **Exit reason**: [[../../exit-analysis/coint-z-reverted|coint_z_reverted]]
- **Signal family**: [[../../concepts/mean-reversion]]
- **Inferred market states at entry** (pre-Phase-1, provisional): [[../../market-states/trending-down]], [[../../market-states/high-volatility]]
- **Primitives (signal-level unavailable in v1)**: [[../../primitives/bollinger-squeeze-breakout]]

# Trade 0008 — LINK/USDT

![[../../../raw/charts/YujiCointegrationResidualReversionStrategy/trade_0008.png]]

## Trade Summary

- Pair: **LINK/USDT**
- Direction: **long**
- Entry time: 2025-10-10T22:00:00+00:00
- Exit time: 2025-10-29T19:00:00+00:00
- Entry price: 17.02
- Exit price: 18.15
- Stop loss (initial): 14.47
- Profit ratio: +6.426%
- Profit absolute: 6.4266521
- Exit reason: coint_z_reverted
- Duration: 453.00h
- Enter tag: coint_long
- Min rate seen: 15.12
- Max rate seen: 20.19
- Max favourable excursion: +18.63%
- Max adverse excursion: -11.16%
- MFE capture ratio: 34.50%
- Exit diagnosis: **missed_continuation**
- Market state at entry: `{"trend": "downtrend (EMA20<50<200)", "distance_from_ema20_pct": -19.483, "distance_from_ema50_pct": -21.643, "distance_from_ema200_pct": -24.518, "volume_vs_20bar_avg": "19.77x", "volatility_regime": "expansion (20b/50b range = 1.00)"}`

## Setup Explanation

- Entry signal tag: `coint_long` (from strategy's `populate_entry_trend`).
- Trend at prior bar: downtrend (EMA20<50<200).
- Volatility regime (20b vs 50b range): expansion (20b/50b range = 1.00).
- Price distance from EMA20 at prior close: -19.48%.
- Entry-bar volume vs trailing 20-bar avg: 19.77x.
- This section uses **only pre-entry data** (bars strictly before `open_date`) — no lookahead.

## Signal Breakdown

- Liquidity sweep: Unavailable in v2 without exported signal data
- Volume spike: yes (19.77x 20-bar avg)
- Trend state: downtrend (EMA20<50<200)
- EMA alignment: downtrend (EMA20<50<200)
- Volatility state: expansion (20b/50b range = 1.00)
- Entry distance from EMA20: -19.48%
- Entry distance from EMA50: -21.64%
- Entry distance from EMA200: -24.52%

## What Went Well

- Trade finished at +6.43% realised PnL.
- Max favourable excursion reached +18.63% in favour of the position.

## What Went Wrong

- Adverse excursion hit -11.16% — position was underwater at some point.

## Outcome Classification

**missed_continuation**

## Learning Note

Closed at +6.43% but peaked at +18.63% — exit logic left a follow-through on the table.
Market state at entry: downtrend (EMA20<50<200).
Volatility regime: expansion (20b/50b range = 1.00).

## Raw Trade Data

| Field | Value |
|---|---|
| pair | LINK/USDT |
| stake_amount | 99.9074 |
| max_stake_amount | 99.9074 |
| amount | 5.87 |
| open_date | 2025-10-10 22:00:00+00:00 |
| close_date | 2025-10-29 19:00:00+00:00 |
| open_rate | 17.02 |
| close_rate | 18.15 |
| fee_open | 0.001 |
| fee_close | 0.001 |
| trade_duration | 27180 |
| profit_ratio | 0.0642618251313903 |
| profit_abs | 6.4266521 |
| exit_reason | coint_z_reverted |
| initial_stop_loss_abs | 14.47 |
| initial_stop_loss_ratio | -0.15 |
| stop_loss_abs | 14.47 |
| stop_loss_ratio | -0.15 |
| min_rate | 15.12 |
| max_rate | 20.19 |
| is_open | False |
| enter_tag | coint_long |
| leverage | 1.0 |
| is_short | False |
| open_timestamp | 1760133600000 |
| close_timestamp | 1761764400000 |
| funding_fees | 0.0 |
| weekday | 2 |
| _idx | 8 |
| _outcome | missed_continuation |
| _exit_diag | missed_continuation |

## Related Trades

- [[trade_0001|Trade 0001 · ETH/USDT · +9.39% · missed_continuation]]  _(same outcome)_
- [[trade_0002|Trade 0002 · ETH/USDT · +5.42% · missed_continuation]]  _(same outcome)_
- [[trade_0005|Trade 0005 · ETH/USDT · +26.57% · missed_continuation]]  _(same outcome)_
- [[trade_0004|Trade 0004 · ETH/USDT · +5.49% · noisy_win]]  _(similar profit)_
