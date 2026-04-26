---
title: "Polymarket — Will Bitcoin dip to $65,000 in April?"
type: polymarket-market
slug: will-bitcoin-dip-to-65k-in-april-2026-355-765
updated: 2026-04-24T20:12:55+00:00
status: paper
end_date: 2026-05-01T04:00:00Z
category: (none)
low_price: 0.0285
low_outcome: Yes
spread: 0.0010
liquidity_usd: 41378
volume_24h_usd: 313445
hours_to_close: 151.8
global_safety_gate: PASS
---

# Will Bitcoin dip to $65,000 in April?

**Scanned:** 2026-04-24T20:12:55+00:00

## Market state

| Field | Value |
|---|---|
| slug | `will-bitcoin-dip-to-65k-in-april-2026-355-765` |
| outcomes | Yes, No |
| prices | 0.0285 / 0.9715 |
| best_bid | 0.0280 |
| best_ask | 0.0290 |
| midpoint | 0.0285 |
| spread | 0.0010 |
| liquidity (USD) | $41,378 |
| 24h volume (USD) | $313,445 |
| 24h price change | -0.0065 |
| hours to close | 151.8 |
| end_date | 2026-05-01T04:00:00Z |
| category | (uncategorised) |
| low-price side | Yes @ 0.0285 |
| low-price token | `91891168804884935930999247357727984305771756132991676079520973027739343180431` |

## Global safety gate: **PASS**

## Per-strategy evaluation

### spread_capture

- **Signal:** `SKIP`
- **Proposed side:** Yes
- **Proposed price:** 0.0380
- **Expected edge / share:** +0.0000
- **Confidence:** 0.20
- **Decision:** `skip`
- **Risk score:** 0.209
- **Reason:** post-only @ 0.038, edge ≈ 0.0000/share

### momentum_reaction

- **Signal:** `SKIP`
- **Decision:** `skip`
- **Risk score:** 0.209
- **Reason:** |24h move| -0.006 < 0.05

### mean_reversion

- **Signal:** `PAPER_LIMIT_BUY`
- **Proposed side:** Yes
- **Proposed price:** 0.0285
- **Expected edge / share:** +0.0200
- **Confidence:** 0.20
- **Decision:** `paper_trade`
- **Risk score:** 0.209
- **Reason:** near-zero extreme 0.029; small re-rate bet

### news_event_no_trade_filter

- **Signal:** `AVOID`
- **Decision:** `skip`
- **Risk score:** 0.209
- **Reason:** closes in 151.8h (< 7 days)

### endgame_decay

- **Signal:** `SKIP`
- **Decision:** `skip`
- **Risk score:** 0.409
- **Reason:** not endgame (151.8h to close)

## Paper-trade tracker

Fill outcomes at 15m / 1h / 4h / close are recorded in daily log entries.

## Linked

- [[../daily/2026-04-24|Today's daily log]]
- [[../README|Polymarket journal index]]
- CSV row: `polymarket-bot/reports/polymarket_strategy_scores.csv`

