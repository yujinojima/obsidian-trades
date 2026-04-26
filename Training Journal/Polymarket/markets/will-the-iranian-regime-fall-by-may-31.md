---
title: "Polymarket — Will the Iranian regime fall by May 31?"
type: polymarket-market
slug: will-the-iranian-regime-fall-by-may-31
updated: 2026-04-24T20:12:55+00:00
status: paper
end_date: 2026-05-31T00:00:00Z
category: (none)
low_price: 0.0330
low_outcome: Yes
spread: 0.0020
liquidity_usd: 348771
volume_24h_usd: 934937
hours_to_close: 867.8
global_safety_gate: PASS
---

# Will the Iranian regime fall by May 31?

**Scanned:** 2026-04-24T20:12:55+00:00

## Market state

| Field | Value |
|---|---|
| slug | `will-the-iranian-regime-fall-by-may-31` |
| outcomes | Yes, No |
| prices | 0.0330 / 0.9670 |
| best_bid | 0.0320 |
| best_ask | 0.0340 |
| midpoint | 0.0330 |
| spread | 0.0020 |
| liquidity (USD) | $348,771 |
| 24h volume (USD) | $934,937 |
| 24h price change | -0.0075 |
| hours to close | 867.8 |
| end_date | 2026-05-31T00:00:00Z |
| category | (uncategorised) |
| low-price side | Yes @ 0.0330 |
| low-price token | `57360053771630303266236723124451177814047338705194149193939656360140487569996` |

## Global safety gate: **PASS**

## Per-strategy evaluation

### spread_capture

- **Signal:** `SKIP`
- **Proposed side:** Yes
- **Proposed price:** 0.0420
- **Expected edge / share:** +0.0000
- **Confidence:** 0.20
- **Decision:** `skip`
- **Risk score:** 0.044
- **Reason:** post-only @ 0.042, edge ≈ 0.0000/share

### momentum_reaction

- **Signal:** `SKIP`
- **Decision:** `skip`
- **Risk score:** 0.044
- **Reason:** |24h move| -0.007 < 0.05

### mean_reversion

- **Signal:** `PAPER_LIMIT_BUY`
- **Proposed side:** Yes
- **Proposed price:** 0.0330
- **Expected edge / share:** +0.0200
- **Confidence:** 0.20
- **Decision:** `paper_trade`
- **Risk score:** 0.044
- **Reason:** near-zero extreme 0.033; small re-rate bet

### news_event_no_trade_filter

- **Signal:** `NO_AVOID_FLAG`
- **Decision:** `skip`
- **Risk score:** 0.044
- **Reason:** no news-event risk detected

### endgame_decay

- **Signal:** `SKIP`
- **Decision:** `skip`
- **Risk score:** 0.244
- **Reason:** not endgame (867.8h to close)

## Paper-trade tracker

Fill outcomes at 15m / 1h / 4h / close are recorded in daily log entries.

## Linked

- [[../daily/2026-04-24|Today's daily log]]
- [[../README|Polymarket journal index]]
- CSV row: `polymarket-bot/reports/polymarket_strategy_scores.csv`

