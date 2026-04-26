---
title: "Polymarket — Will Germany win the 2026 FIFA World Cup?"
type: polymarket-market
slug: will-germany-win-the-2026-fifa-world-cup-467
updated: 2026-04-24T20:12:55+00:00
status: paper
end_date: 2026-07-20T00:00:00Z
category: (none)
low_price: 0.0525
low_outcome: Yes
spread: 0.0010
liquidity_usd: 1104152
volume_24h_usd: 455753
hours_to_close: 2067.8
global_safety_gate: PASS
---

# Will Germany win the 2026 FIFA World Cup?

**Scanned:** 2026-04-24T20:12:55+00:00

## Market state

| Field | Value |
|---|---|
| slug | `will-germany-win-the-2026-fifa-world-cup-467` |
| outcomes | Yes, No |
| prices | 0.0525 / 0.9475 |
| best_bid | 0.0520 |
| best_ask | 0.0530 |
| midpoint | 0.0525 |
| spread | 0.0010 |
| liquidity (USD) | $1,104,152 |
| 24h volume (USD) | $455,753 |
| 24h price change | -0.0010 |
| hours to close | 2067.8 |
| end_date | 2026-07-20T00:00:00Z |
| category | (uncategorised) |
| low-price side | Yes @ 0.0525 |
| low-price token | `81739002353269632749850710185641576213562066971072676369728657545679630163887` |

## Global safety gate: **PASS**

## Per-strategy evaluation

### spread_capture

- **Signal:** `SKIP`
- **Proposed side:** Yes
- **Proposed price:** 0.0620
- **Expected edge / share:** +0.0000
- **Confidence:** 0.20
- **Decision:** `skip`
- **Risk score:** 0.015
- **Reason:** post-only @ 0.062, edge ≈ 0.0000/share

### momentum_reaction

- **Signal:** `SKIP`
- **Decision:** `skip`
- **Risk score:** 0.015
- **Reason:** |24h move| -0.001 < 0.05

### mean_reversion

- **Signal:** `SKIP`
- **Decision:** `skip`
- **Risk score:** 0.015
- **Reason:** low_price 0.052 not at extreme (< 0.05)

### news_event_no_trade_filter

- **Signal:** `NO_AVOID_FLAG`
- **Decision:** `skip`
- **Risk score:** 0.015
- **Reason:** no news-event risk detected

### endgame_decay

- **Signal:** `SKIP`
- **Decision:** `skip`
- **Risk score:** 0.215
- **Reason:** not endgame (2067.8h to close)

## Paper-trade tracker

Fill outcomes at 15m / 1h / 4h / close are recorded in daily log entries.

## Linked

- [[../daily/2026-04-24|Today's daily log]]
- [[../README|Polymarket journal index]]
- CSV row: `polymarket-bot/reports/polymarket_strategy_scores.csv`

