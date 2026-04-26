---
title: "Polymarket — US x Iran permanent peace deal by April 24, 2026?"
type: polymarket-market
slug: us-x-iran-permanent-peace-deal-by-april-24-2026
updated: 2026-04-24T20:11:29+00:00
status: paper
end_date: 2026-04-24T00:00:00Z
category: (none)
low_price: 0.0005
low_outcome: Yes
spread: 0.0010
liquidity_usd: 336627
volume_24h_usd: 1083521
hours_to_close: 0.0
global_safety_gate: FAIL
---

# US x Iran permanent peace deal by April 24, 2026?

**Scanned:** 2026-04-24T20:11:29+00:00

## Market state

| Field | Value |
|---|---|
| slug | `us-x-iran-permanent-peace-deal-by-april-24-2026` |
| outcomes | Yes, No |
| prices | 0.0005 / 0.9995 |
| best_bid | 0.0000 |
| best_ask | 0.0010 |
| midpoint | 0.0005 |
| spread | 0.0010 |
| liquidity (USD) | $336,627 |
| 24h volume (USD) | $1,083,521 |
| 24h price change | -0.0040 |
| hours to close | 0.0 |
| end_date | 2026-04-24T00:00:00Z |
| category | (uncategorised) |
| low-price side | Yes @ 0.0005 |
| low-price token | `73451767581833755534290283287150634572320766963843705278849195665912417601921` |

## Global safety gate: **FAIL**

> Reason: closes in 0.0h < 24h

## Per-strategy evaluation

### spread_capture

- **Signal:** `SKIP`
- **Decision:** `skip`
- **Risk score:** 0.273
- **Reason:** closes in 0.0h < 24h

### momentum_reaction

- **Signal:** `SKIP`
- **Decision:** `skip`
- **Risk score:** 0.273
- **Reason:** closes in 0.0h < 24h

### mean_reversion

- **Signal:** `SKIP`
- **Decision:** `skip`
- **Risk score:** 0.273
- **Reason:** closes in 0.0h < 24h

### news_event_no_trade_filter

- **Signal:** `AVOID`
- **Decision:** `skip`
- **Risk score:** 0.273
- **Reason:** closes in 0.0h (< 7 days)

### endgame_decay

- **Signal:** `SKIP`
- **Decision:** `skip`
- **Risk score:** 0.473
- **Reason:** too close to resolution, settlement risk

## Paper-trade tracker

Fill outcomes at 15m / 1h / 4h / close are recorded in daily log entries.

## Linked

- [[../daily/2026-04-24|Today's daily log]]
- [[../README|Polymarket journal index]]
- CSV row: `polymarket-bot/reports/polymarket_strategy_scores.csv`

