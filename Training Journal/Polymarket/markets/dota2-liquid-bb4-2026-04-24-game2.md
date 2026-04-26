---
title: "Polymarket — Dota 2: Team Liquid vs BetBoom Team - Game 2 Winner"
type: polymarket-market
slug: dota2-liquid-bb4-2026-04-24-game2
updated: 2026-04-24T20:11:29+00:00
status: paper
end_date: 2026-04-24T23:20:00Z
category: (none)
low_price: 0.0005
low_outcome: Team Liquid
spread: 0.0010
liquidity_usd: 503950
volume_24h_usd: 1124128
hours_to_close: 3.1
global_safety_gate: FAIL
---

# Dota 2: Team Liquid vs BetBoom Team - Game 2 Winner

**Scanned:** 2026-04-24T20:11:29+00:00

## Market state

| Field | Value |
|---|---|
| slug | `dota2-liquid-bb4-2026-04-24-game2` |
| outcomes | Team Liquid, BetBoom Team |
| prices | 0.0005 / 0.9995 |
| best_bid | 0.0000 |
| best_ask | 0.0010 |
| midpoint | 0.0005 |
| spread | 0.0010 |
| liquidity (USD) | $503,950 |
| 24h volume (USD) | $1,124,128 |
| 24h price change | -0.4345 |
| hours to close | 3.1 |
| end_date | 2026-04-24T23:20:00Z |
| category | (uncategorised) |
| low-price side | Team Liquid @ 0.0005 |
| low-price token | `111874038205253543401783942507499848752366804303887100003389959471448947451138` |

## Global safety gate: **FAIL**

> Reason: closes in 3.1h < 24h

## Per-strategy evaluation

### spread_capture

- **Signal:** `SKIP`
- **Decision:** `skip`
- **Risk score:** 0.510
- **Reason:** closes in 3.1h < 24h

### momentum_reaction

- **Signal:** `SKIP`
- **Decision:** `skip`
- **Risk score:** 0.510
- **Reason:** closes in 3.1h < 24h

### mean_reversion

- **Signal:** `SKIP`
- **Decision:** `skip`
- **Risk score:** 0.510
- **Reason:** closes in 3.1h < 24h

### news_event_no_trade_filter

- **Signal:** `AVOID`
- **Decision:** `skip`
- **Risk score:** 0.510
- **Reason:** closes in 3.1h (< 7 days); large 24h move -0.434 suggests active news flow

### endgame_decay

- **Signal:** `PAPER_ONLY`
- **Proposed side:** BetBoom Team
- **Proposed price:** 0.9995
- **Expected edge / share:** +0.2172
- **Confidence:** 0.25
- **Decision:** `paper_trade`
- **Risk score:** 0.710
- **Reason:** endgame drift -0.434 with 3.1h remaining; PAPER ONLY per spec

## Paper-trade tracker

Fill outcomes at 15m / 1h / 4h / close are recorded in daily log entries.

## Linked

- [[../daily/2026-04-24|Today's daily log]]
- [[../README|Polymarket journal index]]
- CSV row: `polymarket-bot/reports/polymarket_strategy_scores.csv`

