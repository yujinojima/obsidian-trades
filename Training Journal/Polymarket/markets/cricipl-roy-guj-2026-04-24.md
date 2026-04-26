---
title: "Polymarket — Indian Premier League: Royal Challengers Bangalore vs Gujarat Titans"
type: polymarket-market
slug: cricipl-roy-guj-2026-04-24
updated: 2026-04-24T20:11:29+00:00
status: paper
end_date: 2026-05-01T10:00:00Z
category: (none)
low_price: 0.0005
low_outcome: Gujarat Titans
spread: 0.0010
liquidity_usd: 477289
volume_24h_usd: 1756592
hours_to_close: 157.8
global_safety_gate: FAIL
---

# Indian Premier League: Royal Challengers Bangalore vs Gujarat Titans

**Scanned:** 2026-04-24T20:11:29+00:00

## Market state

| Field | Value |
|---|---|
| slug | `cricipl-roy-guj-2026-04-24` |
| outcomes | Royal Challengers Bangalore, Gujarat Titans |
| prices | 0.9995 / 0.0005 |
| best_bid | 0.9990 |
| best_ask | 1.0000 |
| midpoint | 0.9995 |
| spread | 0.0010 |
| liquidity (USD) | $477,289 |
| 24h volume (USD) | $1,756,592 |
| 24h price change | +0.4145 |
| hours to close | 157.8 |
| end_date | 2026-05-01T10:00:00Z |
| category | (uncategorised) |
| low-price side | Gujarat Titans @ 0.0005 |
| low-price token | `78585037198163493262321931587256382144188960322198286701047080482524517882899` |

## Global safety gate: **FAIL**

> Reason: low_price 0.001 is dust (< $0.02)

## Per-strategy evaluation

### spread_capture

- **Signal:** `SKIP`
- **Decision:** `skip`
- **Risk score:** 0.395
- **Reason:** low_price 0.001 is dust (< $0.02)

### momentum_reaction

- **Signal:** `SKIP`
- **Decision:** `skip`
- **Risk score:** 0.395
- **Reason:** low_price 0.001 is dust (< $0.02)

### mean_reversion

- **Signal:** `SKIP`
- **Decision:** `skip`
- **Risk score:** 0.395
- **Reason:** low_price 0.001 is dust (< $0.02)

### news_event_no_trade_filter

- **Signal:** `AVOID`
- **Decision:** `skip`
- **Risk score:** 0.395
- **Reason:** closes in 157.8h (< 7 days); large 24h move +0.414 suggests active news flow

### endgame_decay

- **Signal:** `SKIP`
- **Decision:** `skip`
- **Risk score:** 0.595
- **Reason:** not endgame (157.8h to close)

## Paper-trade tracker

Fill outcomes at 15m / 1h / 4h / close are recorded in daily log entries.

## Linked

- [[../daily/2026-04-24|Today's daily log]]
- [[../README|Polymarket journal index]]
- CSV row: `polymarket-bot/reports/polymarket_strategy_scores.csv`

