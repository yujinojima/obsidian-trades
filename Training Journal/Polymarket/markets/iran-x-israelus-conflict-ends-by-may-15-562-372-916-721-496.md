---
title: "Polymarket — Iran x Israel/US conflict ends by May 15?"
type: polymarket-market
slug: iran-x-israelus-conflict-ends-by-may-15-562-372-916-721-496
updated: 2026-04-24T20:11:29+00:00
status: paper
end_date: 2026-05-15T00:00:00Z
category: (none)
low_price: 0.0005
low_outcome: No
spread: 0.0010
liquidity_usd: 3309377
volume_24h_usd: 2836710
hours_to_close: 483.8
global_safety_gate: FAIL
---

# Iran x Israel/US conflict ends by May 15?

**Scanned:** 2026-04-24T20:11:29+00:00

## Market state

| Field | Value |
|---|---|
| slug | `iran-x-israelus-conflict-ends-by-may-15-562-372-916-721-496` |
| outcomes | Yes, No |
| prices | 0.9995 / 0.0005 |
| best_bid | 0.9990 |
| best_ask | 1.0000 |
| midpoint | 0.9995 |
| spread | 0.0010 |
| liquidity (USD) | $3,309,377 |
| 24h volume (USD) | $2,836,710 |
| 24h price change | +0.0000 |
| hours to close | 483.8 |
| end_date | 2026-05-15T00:00:00Z |
| category | (uncategorised) |
| low-price side | No @ 0.0005 |
| low-price token | `31869663470674113137413574637244458645080626094263106105850314096988098095887` |

## Global safety gate: **FAIL**

> Reason: low_price 0.001 is dust (< $0.02)

## Per-strategy evaluation

### spread_capture

- **Signal:** `SKIP`
- **Decision:** `skip`
- **Risk score:** 0.013
- **Reason:** low_price 0.001 is dust (< $0.02)

### momentum_reaction

- **Signal:** `SKIP`
- **Decision:** `skip`
- **Risk score:** 0.013
- **Reason:** low_price 0.001 is dust (< $0.02)

### mean_reversion

- **Signal:** `SKIP`
- **Decision:** `skip`
- **Risk score:** 0.013
- **Reason:** low_price 0.001 is dust (< $0.02)

### news_event_no_trade_filter

- **Signal:** `NO_AVOID_FLAG`
- **Decision:** `skip`
- **Risk score:** 0.013
- **Reason:** no news-event risk detected

### endgame_decay

- **Signal:** `SKIP`
- **Decision:** `skip`
- **Risk score:** 0.213
- **Reason:** not endgame (483.8h to close)

## Paper-trade tracker

Fill outcomes at 15m / 1h / 4h / close are recorded in daily log entries.

## Linked

- [[../daily/2026-04-24|Today's daily log]]
- [[../README|Polymarket journal index]]
- CSV row: `polymarket-bot/reports/polymarket_strategy_scores.csv`

