---
title: "Polymarket — Madrid Open: Sebastian Ofner vs Tomas Etcheverry"
type: polymarket-market
slug: atp-ofner-etcheve-2026-04-23
updated: 2026-04-24T20:11:29+00:00
status: paper
end_date: 2026-04-30T08:00:00Z
category: (none)
low_price: 0.0005
low_outcome: Sebastian Ofner
spread: 0.0010
liquidity_usd: 327943
volume_24h_usd: 453626
hours_to_close: 131.8
global_safety_gate: FAIL
---

# Madrid Open: Sebastian Ofner vs Tomas Etcheverry

**Scanned:** 2026-04-24T20:11:29+00:00

## Market state

| Field | Value |
|---|---|
| slug | `atp-ofner-etcheve-2026-04-23` |
| outcomes | Sebastian Ofner, Tomas Etcheverry |
| prices | 0.0005 / 0.9995 |
| best_bid | 0.0000 |
| best_ask | 0.0010 |
| midpoint | 0.0005 |
| spread | 0.0010 |
| liquidity (USD) | $327,943 |
| 24h volume (USD) | $453,626 |
| 24h price change | -0.4145 |
| hours to close | 131.8 |
| end_date | 2026-04-30T08:00:00Z |
| category | (uncategorised) |
| low-price side | Sebastian Ofner @ 0.0005 |
| low-price token | `107646481641552545285084857765947327260193624965553267242852744157161863759869` |

## Global safety gate: **FAIL**

> Reason: low_price 0.001 is dust (< $0.02)

## Per-strategy evaluation

### spread_capture

- **Signal:** `SKIP`
- **Decision:** `skip`
- **Risk score:** 0.414
- **Reason:** low_price 0.001 is dust (< $0.02)

### momentum_reaction

- **Signal:** `SKIP`
- **Decision:** `skip`
- **Risk score:** 0.414
- **Reason:** low_price 0.001 is dust (< $0.02)

### mean_reversion

- **Signal:** `SKIP`
- **Decision:** `skip`
- **Risk score:** 0.414
- **Reason:** low_price 0.001 is dust (< $0.02)

### news_event_no_trade_filter

- **Signal:** `AVOID`
- **Decision:** `skip`
- **Risk score:** 0.414
- **Reason:** closes in 131.8h (< 7 days); large 24h move -0.414 suggests active news flow

### endgame_decay

- **Signal:** `SKIP`
- **Decision:** `skip`
- **Risk score:** 0.614
- **Reason:** not endgame (131.8h to close)

## Paper-trade tracker

Fill outcomes at 15m / 1h / 4h / close are recorded in daily log entries.

## Linked

- [[../daily/2026-04-24|Today's daily log]]
- [[../README|Polymarket journal index]]
- CSV row: `polymarket-bot/reports/polymarket_strategy_scores.csv`

