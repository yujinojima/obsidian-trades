---
title: "Polymarket — Will Norway win the 2026 FIFA World Cup?"
type: polymarket-market
slug: will-norway-win-the-2026-fifa-world-cup-893
updated: 2026-04-24T20:12:55+00:00
status: paper
end_date: 2026-07-20T00:00:00Z
category: (none)
low_price: 0.0235
low_outcome: Yes
spread: 0.0010
liquidity_usd: 1620539
volume_24h_usd: 139854
hours_to_close: 2067.8
global_safety_gate: PASS
---

# Will Norway win the 2026 FIFA World Cup?

**Scanned:** 2026-04-24T20:12:55+00:00

## Market state

| Field | Value |
|---|---|
| slug | `will-norway-win-the-2026-fifa-world-cup-893` |
| outcomes | Yes, No |
| prices | 0.0235 / 0.9765 |
| best_bid | 0.0230 |
| best_ask | 0.0240 |
| midpoint | 0.0235 |
| spread | 0.0010 |
| liquidity (USD) | $1,620,539 |
| 24h volume (USD) | $139,854 |
| 24h price change | +0.0000 |
| hours to close | 2067.8 |
| end_date | 2026-07-20T00:00:00Z |
| category | (uncategorised) |
| low-price side | Yes @ 0.0235 |
| low-price token | `60447443643099453130956385288904175887233107411078568881602330835010340506057` |

## Global safety gate: **PASS**

## Per-strategy evaluation

### spread_capture

- **Signal:** `SKIP`
- **Proposed side:** Yes
- **Proposed price:** 0.0330
- **Expected edge / share:** +0.0000
- **Confidence:** 0.20
- **Decision:** `skip`
- **Risk score:** 0.013
- **Reason:** post-only @ 0.033, edge ≈ 0.0000/share

### momentum_reaction

- **Signal:** `SKIP`
- **Decision:** `skip`
- **Risk score:** 0.013
- **Reason:** |24h move| +0.000 < 0.05

### mean_reversion

- **Signal:** `PAPER_LIMIT_BUY`
- **Proposed side:** Yes
- **Proposed price:** 0.0235
- **Expected edge / share:** +0.0200
- **Confidence:** 0.20
- **Decision:** `paper_trade`
- **Risk score:** 0.013
- **Reason:** near-zero extreme 0.024; small re-rate bet

### news_event_no_trade_filter

- **Signal:** `NO_AVOID_FLAG`
- **Decision:** `skip`
- **Risk score:** 0.013
- **Reason:** no news-event risk detected

### endgame_decay

- **Signal:** `SKIP`
- **Decision:** `skip`
- **Risk score:** 0.213
- **Reason:** not endgame (2067.8h to close)

## Paper-trade tracker

Fill outcomes at 15m / 1h / 4h / close are recorded in daily log entries.

## Linked

- [[../daily/2026-04-24|Today's daily log]]
- [[../README|Polymarket journal index]]
- CSV row: `polymarket-bot/reports/polymarket_strategy_scores.csv`

