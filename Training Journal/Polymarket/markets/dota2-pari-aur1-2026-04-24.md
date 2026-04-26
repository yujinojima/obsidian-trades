---
title: "Polymarket — Dota 2: PARIVISION vs Aurora (BO3) - PGL Wallachia Playoffs"
type: polymarket-market
slug: dota2-pari-aur1-2026-04-24
updated: 2026-04-24T20:11:29+00:00
status: paper
end_date: 2026-04-24T19:35:00Z
category: (none)
low_price: 0.0005
low_outcome: PARIVISION
spread: 0.0010
liquidity_usd: 479460
volume_24h_usd: 1395809
hours_to_close: 0.0
global_safety_gate: FAIL
---

# Dota 2: PARIVISION vs Aurora (BO3) - PGL Wallachia Playoffs

**Scanned:** 2026-04-24T20:11:29+00:00

## Market state

| Field | Value |
|---|---|
| slug | `dota2-pari-aur1-2026-04-24` |
| outcomes | PARIVISION, Aurora |
| prices | 0.0005 / 0.9995 |
| best_bid | 0.0000 |
| best_ask | 0.0010 |
| midpoint | 0.0005 |
| spread | 0.0010 |
| liquidity (USD) | $479,460 |
| 24h volume (USD) | $1,395,809 |
| 24h price change | -0.5145 |
| hours to close | 0.0 |
| end_date | 2026-04-24T19:35:00Z |
| category | (uncategorised) |
| low-price side | PARIVISION @ 0.0005 |
| low-price token | `64706559344288227464015054735419133594446401006387580003849016053483089830116` |

## Global safety gate: **FAIL**

> Reason: closes in 0.0h < 24h

## Per-strategy evaluation

### spread_capture

- **Signal:** `SKIP`
- **Decision:** `skip`
- **Risk score:** 0.512
- **Reason:** closes in 0.0h < 24h

### momentum_reaction

- **Signal:** `SKIP`
- **Decision:** `skip`
- **Risk score:** 0.512
- **Reason:** closes in 0.0h < 24h

### mean_reversion

- **Signal:** `SKIP`
- **Decision:** `skip`
- **Risk score:** 0.512
- **Reason:** closes in 0.0h < 24h

### news_event_no_trade_filter

- **Signal:** `AVOID`
- **Decision:** `skip`
- **Risk score:** 0.512
- **Reason:** closes in 0.0h (< 7 days); large 24h move -0.514 suggests active news flow

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

