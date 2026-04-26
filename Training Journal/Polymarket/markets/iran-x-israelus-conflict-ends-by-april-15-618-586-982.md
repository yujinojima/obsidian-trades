---
title: "Polymarket — Iran x Israel/US conflict ends by April 15?"
type: polymarket-market
slug: iran-x-israelus-conflict-ends-by-april-15-618-586-982
updated: 2026-04-24T20:11:29+00:00
status: paper
end_date: 2026-04-15T00:00:00Z
category: (none)
low_price: 0.0005
low_outcome: No
spread: 0.0010
liquidity_usd: 3219509
volume_24h_usd: 800734
hours_to_close: 0.0
global_safety_gate: FAIL
---

# Iran x Israel/US conflict ends by April 15?

**Scanned:** 2026-04-24T20:11:29+00:00

## Market state

| Field | Value |
|---|---|
| slug | `iran-x-israelus-conflict-ends-by-april-15-618-586-982` |
| outcomes | Yes, No |
| prices | 0.9995 / 0.0005 |
| best_bid | 0.9990 |
| best_ask | 1.0000 |
| midpoint | 0.9995 |
| spread | 0.0010 |
| liquidity (USD) | $3,219,509 |
| 24h volume (USD) | $800,734 |
| 24h price change | +0.0000 |
| hours to close | 0.0 |
| end_date | 2026-04-15T00:00:00Z |
| category | (uncategorised) |
| low-price side | No @ 0.0005 |
| low-price token | `42541597022580268380579424081239402820400625604765321493406160729090848893639` |

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

