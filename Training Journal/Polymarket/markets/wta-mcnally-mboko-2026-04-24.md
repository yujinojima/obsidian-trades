---
title: "Polymarket — Madrid Open: Caty McNally vs Victoria Mboko"
type: polymarket-market
slug: wta-mcnally-mboko-2026-04-24
updated: 2026-04-24T20:11:29+00:00
status: paper
end_date: 2026-05-01T09:00:00Z
category: (none)
low_price: 0.0005
low_outcome: Victoria Mboko
spread: 0.0010
liquidity_usd: 206346
volume_24h_usd: 454612
hours_to_close: 156.8
global_safety_gate: FAIL
---

# Madrid Open: Caty McNally vs Victoria Mboko

**Scanned:** 2026-04-24T20:11:29+00:00

## Market state

| Field | Value |
|---|---|
| slug | `wta-mcnally-mboko-2026-04-24` |
| outcomes | Caty McNally, Victoria Mboko |
| prices | 0.9995 / 0.0005 |
| best_bid | 0.9990 |
| best_ask | 1.0000 |
| midpoint | 0.9995 |
| spread | 0.0010 |
| liquidity (USD) | $206,346 |
| 24h volume (USD) | $454,612 |
| 24h price change | +0.7745 |
| hours to close | 156.8 |
| end_date | 2026-05-01T09:00:00Z |
| category | (uncategorised) |
| low-price side | Victoria Mboko @ 0.0005 |
| low-price token | `90534236130456123874083731234109316165479829241034452500099554133824198226702` |

## Global safety gate: **FAIL**

> Reason: low_price 0.001 is dust (< $0.02)

## Per-strategy evaluation

### spread_capture

- **Signal:** `SKIP`
- **Decision:** `skip`
- **Risk score:** 0.396
- **Reason:** low_price 0.001 is dust (< $0.02)

### momentum_reaction

- **Signal:** `SKIP`
- **Decision:** `skip`
- **Risk score:** 0.396
- **Reason:** low_price 0.001 is dust (< $0.02)

### mean_reversion

- **Signal:** `SKIP`
- **Decision:** `skip`
- **Risk score:** 0.396
- **Reason:** low_price 0.001 is dust (< $0.02)

### news_event_no_trade_filter

- **Signal:** `AVOID`
- **Decision:** `skip`
- **Risk score:** 0.396
- **Reason:** closes in 156.8h (< 7 days); large 24h move +0.774 suggests active news flow

### endgame_decay

- **Signal:** `SKIP`
- **Decision:** `skip`
- **Risk score:** 0.596
- **Reason:** not endgame (156.8h to close)

## Paper-trade tracker

Fill outcomes at 15m / 1h / 4h / close are recorded in daily log entries.

## Linked

- [[../daily/2026-04-24|Today's daily log]]
- [[../README|Polymarket journal index]]
- CSV row: `polymarket-bot/reports/polymarket_strategy_scores.csv`

