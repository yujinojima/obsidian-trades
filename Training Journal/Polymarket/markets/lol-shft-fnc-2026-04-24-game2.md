---
title: "Polymarket — LoL: Shifters vs Fnatic - Game 2 Winner"
type: polymarket-market
slug: lol-shft-fnc-2026-04-24-game2
updated: 2026-04-24T20:11:29+00:00
status: paper
end_date: 2026-04-24T21:10:00Z
category: (none)
low_price: 0.0005
low_outcome: Shifters
spread: 0.0010
liquidity_usd: 410517
volume_24h_usd: 333616
hours_to_close: 1.0
global_safety_gate: FAIL
---

# LoL: Shifters vs Fnatic - Game 2 Winner

**Scanned:** 2026-04-24T20:11:29+00:00

## Market state

| Field | Value |
|---|---|
| slug | `lol-shft-fnc-2026-04-24-game2` |
| outcomes | Shifters, Fnatic |
| prices | 0.0005 / 0.9995 |
| best_bid | 0.0000 |
| best_ask | 0.0010 |
| midpoint | 0.0005 |
| spread | 0.0010 |
| liquidity (USD) | $410,517 |
| 24h volume (USD) | $333,616 |
| 24h price change | -0.4395 |
| hours to close | 1.0 |
| end_date | 2026-04-24T21:10:00Z |
| category | (uncategorised) |
| low-price side | Shifters @ 0.0005 |
| low-price token | `111896117616680261081556210174798056885005161762885942888886427284082443298475` |

## Global safety gate: **FAIL**

> Reason: closes in 1.0h < 24h

## Per-strategy evaluation

### spread_capture

- **Signal:** `SKIP`
- **Decision:** `skip`
- **Risk score:** 0.512
- **Reason:** closes in 1.0h < 24h

### momentum_reaction

- **Signal:** `SKIP`
- **Decision:** `skip`
- **Risk score:** 0.512
- **Reason:** closes in 1.0h < 24h

### mean_reversion

- **Signal:** `SKIP`
- **Decision:** `skip`
- **Risk score:** 0.512
- **Reason:** closes in 1.0h < 24h

### news_event_no_trade_filter

- **Signal:** `AVOID`
- **Decision:** `skip`
- **Risk score:** 0.512
- **Reason:** closes in 1.0h (< 7 days); large 24h move -0.440 suggests active news flow

### endgame_decay

- **Signal:** `SKIP`
- **Decision:** `skip`
- **Risk score:** 0.712
- **Reason:** too close to resolution, settlement risk

## Paper-trade tracker

Fill outcomes at 15m / 1h / 4h / close are recorded in daily log entries.

## Linked

- [[../daily/2026-04-24|Today's daily log]]
- [[../README|Polymarket journal index]]
- CSV row: `polymarket-bot/reports/polymarket_strategy_scores.csv`

