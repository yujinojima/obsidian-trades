---
title: "Polymarket — Will Bitcoin reach $85,000 in April?"
type: polymarket-market
slug: will-bitcoin-reach-85k-in-april-2026
updated: 2026-04-24T20:12:55+00:00
status: paper
end_date: 2026-05-01T04:00:00Z
category: (none)
low_price: 0.0525
low_outcome: Yes
spread: 0.0010
liquidity_usd: 194803
volume_24h_usd: 162206
hours_to_close: 151.8
global_safety_gate: PASS
---

# Will Bitcoin reach $85,000 in April?

**Scanned:** 2026-04-24T20:12:55+00:00

## Market state

| Field | Value |
|---|---|
| slug | `will-bitcoin-reach-85k-in-april-2026` |
| outcomes | Yes, No |
| prices | 0.0525 / 0.9475 |
| best_bid | 0.0520 |
| best_ask | 0.0530 |
| midpoint | 0.0525 |
| spread | 0.0010 |
| liquidity (USD) | $194,803 |
| 24h volume (USD) | $162,206 |
| 24h price change | -0.0205 |
| hours to close | 151.8 |
| end_date | 2026-05-01T04:00:00Z |
| category | (uncategorised) |
| low-price side | Yes @ 0.0525 |
| low-price token | `67399009651248931128484970624141355422398090617680818427428637927246754082167` |

## Global safety gate: **PASS**

## Per-strategy evaluation

### spread_capture

- **Signal:** `SKIP`
- **Proposed side:** Yes
- **Proposed price:** 0.0620
- **Expected edge / share:** +0.0000
- **Confidence:** 0.20
- **Decision:** `skip`
- **Risk score:** 0.201
- **Reason:** post-only @ 0.062, edge ≈ 0.0000/share

### momentum_reaction

- **Signal:** `SKIP`
- **Decision:** `skip`
- **Risk score:** 0.201
- **Reason:** |24h move| -0.021 < 0.05

### mean_reversion

- **Signal:** `SKIP`
- **Decision:** `skip`
- **Risk score:** 0.201
- **Reason:** low_price 0.052 not at extreme (< 0.05)

### news_event_no_trade_filter

- **Signal:** `AVOID`
- **Decision:** `skip`
- **Risk score:** 0.201
- **Reason:** closes in 151.8h (< 7 days)

### endgame_decay

- **Signal:** `SKIP`
- **Decision:** `skip`
- **Risk score:** 0.401
- **Reason:** not endgame (151.8h to close)

## Paper-trade tracker

Fill outcomes at 15m / 1h / 4h / close are recorded in daily log entries.

## Linked

- [[../daily/2026-04-24|Today's daily log]]
- [[../README|Polymarket journal index]]
- CSV row: `polymarket-bot/reports/polymarket_strategy_scores.csv`

