---
title: "Polymarket — Will Jesus Christ return before 2027?"
type: polymarket-market
slug: will-jesus-christ-return-before-2027
updated: 2026-04-24T20:12:55+00:00
status: paper
end_date: 2026-12-31T00:00:00Z
category: (none)
low_price: 0.0385
low_outcome: Yes
spread: 0.0010
liquidity_usd: 1754351
volume_24h_usd: 189197
hours_to_close: 6003.8
global_safety_gate: PASS
---

# Will Jesus Christ return before 2027?

**Scanned:** 2026-04-24T20:12:55+00:00

## Market state

| Field | Value |
|---|---|
| slug | `will-jesus-christ-return-before-2027` |
| outcomes | Yes, No |
| prices | 0.0385 / 0.9615 |
| best_bid | 0.0380 |
| best_ask | 0.0390 |
| midpoint | 0.0385 |
| spread | 0.0010 |
| liquidity (USD) | $1,754,351 |
| 24h volume (USD) | $189,197 |
| 24h price change | +0.0000 |
| hours to close | 6003.8 |
| end_date | 2026-12-31T00:00:00Z |
| category | (uncategorised) |
| low-price side | Yes @ 0.0385 |
| low-price token | `69324317355037271422943965141382095011871956039434394956830818206664869608517` |

## Global safety gate: **PASS**

## Per-strategy evaluation

### spread_capture

- **Signal:** `SKIP`
- **Proposed side:** Yes
- **Proposed price:** 0.0480
- **Expected edge / share:** +0.0000
- **Confidence:** 0.20
- **Decision:** `skip`
- **Risk score:** 0.013
- **Reason:** post-only @ 0.048, edge ≈ 0.0000/share

### momentum_reaction

- **Signal:** `SKIP`
- **Decision:** `skip`
- **Risk score:** 0.013
- **Reason:** |24h move| +0.000 < 0.05

### mean_reversion

- **Signal:** `PAPER_LIMIT_BUY`
- **Proposed side:** Yes
- **Proposed price:** 0.0385
- **Expected edge / share:** +0.0200
- **Confidence:** 0.20
- **Decision:** `paper_trade`
- **Risk score:** 0.013
- **Reason:** near-zero extreme 0.038; small re-rate bet

### news_event_no_trade_filter

- **Signal:** `NO_AVOID_FLAG`
- **Decision:** `skip`
- **Risk score:** 0.013
- **Reason:** no news-event risk detected

### endgame_decay

- **Signal:** `SKIP`
- **Decision:** `skip`
- **Risk score:** 0.213
- **Reason:** not endgame (6003.8h to close)

## Paper-trade tracker

Fill outcomes at 15m / 1h / 4h / close are recorded in daily log entries.

## Linked

- [[../daily/2026-04-24|Today's daily log]]
- [[../README|Polymarket journal index]]
- CSV row: `polymarket-bot/reports/polymarket_strategy_scores.csv`

