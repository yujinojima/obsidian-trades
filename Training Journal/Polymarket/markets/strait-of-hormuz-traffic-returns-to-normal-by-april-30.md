---
title: "Polymarket — Strait of Hormuz traffic returns to normal by end of April?"
type: polymarket-market
slug: strait-of-hormuz-traffic-returns-to-normal-by-april-30
updated: 2026-04-24T20:12:55+00:00
status: paper
end_date: 2026-04-30T00:00:00Z
category: (none)
low_price: 0.0205
low_outcome: Yes
spread: 0.0010
liquidity_usd: 640659
volume_24h_usd: 2168287
hours_to_close: 123.8
global_safety_gate: PASS
---

# Strait of Hormuz traffic returns to normal by end of April?

**Scanned:** 2026-04-24T20:12:55+00:00

## Market state

| Field | Value |
|---|---|
| slug | `strait-of-hormuz-traffic-returns-to-normal-by-april-30` |
| outcomes | Yes, No |
| prices | 0.0205 / 0.9795 |
| best_bid | 0.0200 |
| best_ask | 0.0210 |
| midpoint | 0.0205 |
| spread | 0.0010 |
| liquidity (USD) | $640,659 |
| 24h volume (USD) | $2,168,287 |
| 24h price change | -0.0060 |
| hours to close | 123.8 |
| end_date | 2026-04-30T00:00:00Z |
| category | (uncategorised) |
| low-price side | Yes @ 0.0205 |
| low-price token | `77893140510362582253172593084218413010407941075415081594586195705930819989216` |

## Global safety gate: **PASS**

## Per-strategy evaluation

### spread_capture

- **Signal:** `SKIP`
- **Proposed side:** Yes
- **Proposed price:** 0.0300
- **Expected edge / share:** +0.0000
- **Confidence:** 0.20
- **Decision:** `skip`
- **Risk score:** 0.185
- **Reason:** post-only @ 0.03, edge ≈ 0.0000/share

### momentum_reaction

- **Signal:** `SKIP`
- **Decision:** `skip`
- **Risk score:** 0.185
- **Reason:** |24h move| -0.006 < 0.05

### mean_reversion

- **Signal:** `PAPER_LIMIT_BUY`
- **Proposed side:** Yes
- **Proposed price:** 0.0205
- **Expected edge / share:** +0.0200
- **Confidence:** 0.20
- **Decision:** `paper_trade`
- **Risk score:** 0.185
- **Reason:** near-zero extreme 0.021; small re-rate bet

### news_event_no_trade_filter

- **Signal:** `AVOID`
- **Decision:** `skip`
- **Risk score:** 0.185
- **Reason:** closes in 123.8h (< 7 days)

### endgame_decay

- **Signal:** `SKIP`
- **Decision:** `skip`
- **Risk score:** 0.385
- **Reason:** not endgame (123.8h to close)

## Paper-trade tracker

Fill outcomes at 15m / 1h / 4h / close are recorded in daily log entries.

## Linked

- [[../daily/2026-04-24|Today's daily log]]
- [[../README|Polymarket journal index]]
- CSV row: `polymarket-bot/reports/polymarket_strategy_scores.csv`

