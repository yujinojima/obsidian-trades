---
title: "Polymarket — Kharg Island no longer under Iranian control by April 30?"
type: polymarket-market
slug: kharg-island-no-longer-under-iranian-control-by-april-30-912
updated: 2026-04-24T20:12:55+00:00
status: paper
end_date: 2026-04-30T23:55:00Z
category: (none)
low_price: 0.0350
low_outcome: Yes
spread: 0.0020
liquidity_usd: 243181
volume_24h_usd: 382691
hours_to_close: 147.7
global_safety_gate: PASS
---

# Kharg Island no longer under Iranian control by April 30?

**Scanned:** 2026-04-24T20:12:55+00:00

## Market state

| Field | Value |
|---|---|
| slug | `kharg-island-no-longer-under-iranian-control-by-april-30-912` |
| outcomes | Yes, No |
| prices | 0.0350 / 0.9650 |
| best_bid | 0.0340 |
| best_ask | 0.0360 |
| midpoint | 0.0350 |
| spread | 0.0020 |
| liquidity (USD) | $243,181 |
| 24h volume (USD) | $382,691 |
| 24h price change | -0.0230 |
| hours to close | 147.7 |
| end_date | 2026-04-30T23:55:00Z |
| category | (uncategorised) |
| low-price side | Yes @ 0.0350 |
| low-price token | `66760013958706218500063341242954853503885044406421636173986330736153883161818` |

## Global safety gate: **PASS**

## Per-strategy evaluation

### spread_capture

- **Signal:** `SKIP`
- **Proposed side:** Yes
- **Proposed price:** 0.0440
- **Expected edge / share:** +0.0000
- **Confidence:** 0.20
- **Decision:** `skip`
- **Risk score:** 0.223
- **Reason:** post-only @ 0.044, edge ≈ 0.0000/share

### momentum_reaction

- **Signal:** `SKIP`
- **Decision:** `skip`
- **Risk score:** 0.223
- **Reason:** |24h move| -0.023 < 0.05

### mean_reversion

- **Signal:** `PAPER_LIMIT_BUY`
- **Proposed side:** Yes
- **Proposed price:** 0.0350
- **Expected edge / share:** +0.0200
- **Confidence:** 0.20
- **Decision:** `paper_trade`
- **Risk score:** 0.223
- **Reason:** near-zero extreme 0.035; small re-rate bet

### news_event_no_trade_filter

- **Signal:** `AVOID`
- **Decision:** `skip`
- **Risk score:** 0.223
- **Reason:** closes in 147.7h (< 7 days)

### endgame_decay

- **Signal:** `SKIP`
- **Decision:** `skip`
- **Risk score:** 0.423
- **Reason:** not endgame (147.7h to close)

## Paper-trade tracker

Fill outcomes at 15m / 1h / 4h / close are recorded in daily log entries.

## Linked

- [[../daily/2026-04-24|Today's daily log]]
- [[../README|Polymarket journal index]]
- CSV row: `polymarket-bot/reports/polymarket_strategy_scores.csv`

