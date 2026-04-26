---
title: "Polymarket — Will Netherlands win the 2026 FIFA World Cup?"
type: polymarket-market
slug: will-netherlands-win-the-2026-fifa-world-cup-739
updated: 2026-04-24T20:12:55+00:00
status: paper
end_date: 2026-07-20T00:00:00Z
category: (none)
low_price: 0.0335
low_outcome: Yes
spread: 0.0010
liquidity_usd: 1375408
volume_24h_usd: 248345
hours_to_close: 2067.8
global_safety_gate: PASS
---

# Will Netherlands win the 2026 FIFA World Cup?

**Scanned:** 2026-04-24T20:12:55+00:00

## Market state

| Field | Value |
|---|---|
| slug | `will-netherlands-win-the-2026-fifa-world-cup-739` |
| outcomes | Yes, No |
| prices | 0.0335 / 0.9665 |
| best_bid | 0.0330 |
| best_ask | 0.0340 |
| midpoint | 0.0335 |
| spread | 0.0010 |
| liquidity (USD) | $1,375,408 |
| 24h volume (USD) | $248,345 |
| 24h price change | +0.0000 |
| hours to close | 2067.8 |
| end_date | 2026-07-20T00:00:00Z |
| category | (uncategorised) |
| low-price side | Yes @ 0.0335 |
| low-price token | `55935183786009449883683540312350046975246300613283087403691731856990327029236` |

## Global safety gate: **PASS**

## Per-strategy evaluation

### spread_capture

- **Signal:** `SKIP`
- **Proposed side:** Yes
- **Proposed price:** 0.0430
- **Expected edge / share:** +0.0000
- **Confidence:** 0.20
- **Decision:** `skip`
- **Risk score:** 0.013
- **Reason:** post-only @ 0.043, edge ≈ 0.0000/share

### momentum_reaction

- **Signal:** `SKIP`
- **Decision:** `skip`
- **Risk score:** 0.013
- **Reason:** |24h move| +0.000 < 0.05

### mean_reversion

- **Signal:** `PAPER_LIMIT_BUY`
- **Proposed side:** Yes
- **Proposed price:** 0.0335
- **Expected edge / share:** +0.0200
- **Confidence:** 0.20
- **Decision:** `paper_trade`
- **Risk score:** 0.013
- **Reason:** near-zero extreme 0.034; small re-rate bet

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

