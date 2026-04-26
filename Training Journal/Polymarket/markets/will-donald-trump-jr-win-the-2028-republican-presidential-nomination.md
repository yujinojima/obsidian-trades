---
title: "Polymarket — Will Donald Trump Jr. win the 2028 Republican presidential nomination?"
type: polymarket-market
slug: will-donald-trump-jr-win-the-2028-republican-presidential-nomination
updated: 2026-04-24T20:12:55+00:00
status: paper
end_date: 2028-11-07T00:00:00Z
category: (none)
low_price: 0.0225
low_outcome: Yes
spread: 0.0010
liquidity_usd: 556443
volume_24h_usd: 162967
hours_to_close: 22251.8
global_safety_gate: PASS
---

# Will Donald Trump Jr. win the 2028 Republican presidential nomination?

**Scanned:** 2026-04-24T20:12:55+00:00

## Market state

| Field | Value |
|---|---|
| slug | `will-donald-trump-jr-win-the-2028-republican-presidential-nomination` |
| outcomes | Yes, No |
| prices | 0.0225 / 0.9775 |
| best_bid | 0.0220 |
| best_ask | 0.0230 |
| midpoint | 0.0225 |
| spread | 0.0010 |
| liquidity (USD) | $556,443 |
| 24h volume (USD) | $162,967 |
| 24h price change | +0.0005 |
| hours to close | 22251.8 |
| end_date | 2028-11-07T00:00:00Z |
| category | (uncategorised) |
| low-price side | Yes @ 0.0225 |
| low-price token | `96972794085445478502118386209219626048407104930213167197946285611747327241358` |

## Global safety gate: **PASS**

## Per-strategy evaluation

### spread_capture

- **Signal:** `SKIP`
- **Proposed side:** Yes
- **Proposed price:** 0.0320
- **Expected edge / share:** +0.0000
- **Confidence:** 0.20
- **Decision:** `skip`
- **Risk score:** 0.014
- **Reason:** post-only @ 0.032, edge ≈ 0.0000/share

### momentum_reaction

- **Signal:** `SKIP`
- **Decision:** `skip`
- **Risk score:** 0.014
- **Reason:** |24h move| +0.001 < 0.05

### mean_reversion

- **Signal:** `PAPER_LIMIT_BUY`
- **Proposed side:** Yes
- **Proposed price:** 0.0225
- **Expected edge / share:** +0.0200
- **Confidence:** 0.20
- **Decision:** `paper_trade`
- **Risk score:** 0.014
- **Reason:** near-zero extreme 0.022; small re-rate bet

### news_event_no_trade_filter

- **Signal:** `NO_AVOID_FLAG`
- **Decision:** `skip`
- **Risk score:** 0.014
- **Reason:** no news-event risk detected

### endgame_decay

- **Signal:** `SKIP`
- **Decision:** `skip`
- **Risk score:** 0.214
- **Reason:** not endgame (22251.8h to close)

## Paper-trade tracker

Fill outcomes at 15m / 1h / 4h / close are recorded in daily log entries.

## Linked

- [[../daily/2026-04-24|Today's daily log]]
- [[../README|Polymarket journal index]]
- CSV row: `polymarket-bot/reports/polymarket_strategy_scores.csv`

