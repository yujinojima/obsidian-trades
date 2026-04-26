---
title: "Polymarket — LoL: Natus Vincere vs Karmine Corp - Game 1 Winner"
type: polymarket-market
slug: lol-navi-kc-2026-04-24-game1
updated: 2026-04-24T20:11:29+00:00
status: paper
end_date: 2026-04-24T23:40:00Z
category: (none)
low_price: 0.0005
low_outcome: Natus Vincere
spread: 0.0010
liquidity_usd: 189580
volume_24h_usd: 480848
hours_to_close: 3.5
global_safety_gate: FAIL
---

# LoL: Natus Vincere vs Karmine Corp - Game 1 Winner

**Scanned:** 2026-04-24T20:11:29+00:00

## Market state

| Field | Value |
|---|---|
| slug | `lol-navi-kc-2026-04-24-game1` |
| outcomes | Natus Vincere, Karmine Corp |
| prices | 0.0005 / 0.9995 |
| best_bid | 0.0000 |
| best_ask | 0.0010 |
| midpoint | 0.0005 |
| spread | 0.0010 |
| liquidity (USD) | $189,580 |
| 24h volume (USD) | $480,848 |
| 24h price change | -0.3995 |
| hours to close | 3.5 |
| end_date | 2026-04-24T23:40:00Z |
| category | (uncategorised) |
| low-price side | Natus Vincere @ 0.0005 |
| low-price token | `107613665747622137288670869001270085888531504551333499490115700148824896361833` |

## Global safety gate: **FAIL**

> Reason: closes in 3.5h < 24h

## Per-strategy evaluation

### spread_capture

- **Signal:** `SKIP`
- **Decision:** `skip`
- **Risk score:** 0.510
- **Reason:** closes in 3.5h < 24h

### momentum_reaction

- **Signal:** `SKIP`
- **Decision:** `skip`
- **Risk score:** 0.510
- **Reason:** closes in 3.5h < 24h

### mean_reversion

- **Signal:** `SKIP`
- **Decision:** `skip`
- **Risk score:** 0.510
- **Reason:** closes in 3.5h < 24h

### news_event_no_trade_filter

- **Signal:** `AVOID`
- **Decision:** `skip`
- **Risk score:** 0.510
- **Reason:** closes in 3.5h (< 7 days); large 24h move -0.400 suggests active news flow

### endgame_decay

- **Signal:** `PAPER_ONLY`
- **Proposed side:** Karmine Corp
- **Proposed price:** 0.9995
- **Expected edge / share:** +0.1998
- **Confidence:** 0.25
- **Decision:** `paper_trade`
- **Risk score:** 0.710
- **Reason:** endgame drift -0.400 with 3.5h remaining; PAPER ONLY per spec

## Paper-trade tracker

Fill outcomes at 15m / 1h / 4h / close are recorded in daily log entries.

## Linked

- [[../daily/2026-04-24|Today's daily log]]
- [[../README|Polymarket journal index]]
- CSV row: `polymarket-bot/reports/polymarket_strategy_scores.csv`

