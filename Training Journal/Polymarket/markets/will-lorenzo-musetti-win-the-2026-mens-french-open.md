---
title: "Polymarket — Will Lorenzo Musetti win the 2026 Men's French Open?"
type: polymarket-market
slug: will-lorenzo-musetti-win-the-2026-mens-french-open
updated: 2026-04-24T20:12:55+00:00
status: paper
end_date: 2026-06-07T00:00:00Z
category: (none)
low_price: 0.0230
low_outcome: Yes
spread: 0.0040
liquidity_usd: 53467
volume_24h_usd: 450474
hours_to_close: 1035.8
global_safety_gate: PASS
---

# Will Lorenzo Musetti win the 2026 Men's French Open?

**Scanned:** 2026-04-24T20:12:55+00:00

## Market state

| Field | Value |
|---|---|
| slug | `will-lorenzo-musetti-win-the-2026-mens-french-open` |
| outcomes | Yes, No |
| prices | 0.0230 / 0.9770 |
| best_bid | 0.0210 |
| best_ask | 0.0250 |
| midpoint | 0.0230 |
| spread | 0.0040 |
| liquidity (USD) | $53,467 |
| 24h volume (USD) | $450,474 |
| 24h price change | +0.0060 |
| hours to close | 1035.8 |
| end_date | 2026-06-07T00:00:00Z |
| category | (uncategorised) |
| low-price side | Yes @ 0.0230 |
| low-price token | `17221527894426601950996432589013277000140067344765011503715902729911475041759` |

## Global safety gate: **PASS**

## Per-strategy evaluation

### spread_capture

- **Signal:** `SKIP`
- **Proposed side:** Yes
- **Proposed price:** 0.0310
- **Expected edge / share:** +0.0000
- **Confidence:** 0.20
- **Decision:** `skip`
- **Risk score:** 0.065
- **Reason:** post-only @ 0.031, edge ≈ 0.0000/share

### momentum_reaction

- **Signal:** `SKIP`
- **Decision:** `skip`
- **Risk score:** 0.065
- **Reason:** |24h move| +0.006 < 0.05

### mean_reversion

- **Signal:** `PAPER_LIMIT_BUY`
- **Proposed side:** Yes
- **Proposed price:** 0.0230
- **Expected edge / share:** +0.0200
- **Confidence:** 0.20
- **Decision:** `paper_trade`
- **Risk score:** 0.065
- **Reason:** near-zero extreme 0.023; small re-rate bet

### news_event_no_trade_filter

- **Signal:** `NO_AVOID_FLAG`
- **Decision:** `skip`
- **Risk score:** 0.065
- **Reason:** no news-event risk detected

### endgame_decay

- **Signal:** `SKIP`
- **Decision:** `skip`
- **Risk score:** 0.265
- **Reason:** not endgame (1035.8h to close)

## Paper-trade tracker

Fill outcomes at 15m / 1h / 4h / close are recorded in daily log entries.

## Linked

- [[../daily/2026-04-24|Today's daily log]]
- [[../README|Polymarket journal index]]
- CSV row: `polymarket-bot/reports/polymarket_strategy_scores.csv`

