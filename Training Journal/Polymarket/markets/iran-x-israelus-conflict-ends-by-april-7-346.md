---
title: "Polymarket — Iran x Israel/US conflict ends by April 7?"
type: polymarket-market
slug: iran-x-israelus-conflict-ends-by-april-7-346
updated: 2026-04-24T20:11:29+00:00
status: paper
end_date: 2026-04-07T00:00:00Z
category: (none)
low_price: 0.0005
low_outcome: No
spread: 0.0010
liquidity_usd: 10037547
volume_24h_usd: 18272521
hours_to_close: 0.0
global_safety_gate: FAIL
---

# Iran x Israel/US conflict ends by April 7?

**Scanned:** 2026-04-24T20:11:29+00:00

## Market state

| Field | Value |
|---|---|
| slug | `iran-x-israelus-conflict-ends-by-april-7-346` |
| outcomes | Yes, No |
| prices | 0.9995 / 0.0005 |
| best_bid | 0.9990 |
| best_ask | 1.0000 |
| midpoint | 0.9995 |
| spread | 0.0010 |
| liquidity (USD) | $10,037,547 |
| 24h volume (USD) | $18,272,521 |
| 24h price change | +0.0000 |
| hours to close | 0.0 |
| end_date | 2026-04-07T00:00:00Z |
| category | (uncategorised) |
| low-price side | No @ 0.0005 |
| low-price token | `111480277258850178537736943682653186709510728707904846394206772928007084779467` |

## Global safety gate: **FAIL**

> Reason: closes in 0.0h < 24h

## Per-strategy evaluation

### spread_capture

- **Signal:** `SKIP`
- **Decision:** `skip`
- **Risk score:** 0.263
- **Reason:** closes in 0.0h < 24h

### momentum_reaction

- **Signal:** `SKIP`
- **Decision:** `skip`
- **Risk score:** 0.263
- **Reason:** closes in 0.0h < 24h

### mean_reversion

- **Signal:** `SKIP`
- **Decision:** `skip`
- **Risk score:** 0.263
- **Reason:** closes in 0.0h < 24h

### news_event_no_trade_filter

- **Signal:** `AVOID`
- **Decision:** `skip`
- **Risk score:** 0.263
- **Reason:** closes in 0.0h (< 7 days)

### endgame_decay

- **Signal:** `SKIP`
- **Decision:** `skip`
- **Risk score:** 0.463
- **Reason:** too close to resolution, settlement risk

## Paper-trade tracker

Fill outcomes at 15m / 1h / 4h / close are recorded in daily log entries.

## Linked

- [[../daily/2026-04-24|Today's daily log]]
- [[../README|Polymarket journal index]]
- CSV row: `polymarket-bot/reports/polymarket_strategy_scores.csv`

