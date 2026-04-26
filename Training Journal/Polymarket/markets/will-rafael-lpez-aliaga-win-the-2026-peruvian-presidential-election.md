---
title: "Polymarket — Will Rafael López Aliaga win the 2026 Peruvian presidential election?"
type: polymarket-market
slug: will-rafael-lpez-aliaga-win-the-2026-peruvian-presidential-election
updated: 2026-04-24T20:12:55+00:00
status: paper
end_date: 2026-06-07T00:00:00Z
category: (none)
low_price: 0.0205
low_outcome: Yes
spread: 0.0010
liquidity_usd: 237314
volume_24h_usd: 636553
hours_to_close: 1035.8
global_safety_gate: PASS
---

# Will Rafael López Aliaga win the 2026 Peruvian presidential election?

**Scanned:** 2026-04-24T20:12:55+00:00

## Market state

| Field | Value |
|---|---|
| slug | `will-rafael-lpez-aliaga-win-the-2026-peruvian-presidential-election` |
| outcomes | Yes, No |
| prices | 0.0205 / 0.9795 |
| best_bid | 0.0200 |
| best_ask | 0.0210 |
| midpoint | 0.0205 |
| spread | 0.0010 |
| liquidity (USD) | $237,314 |
| 24h volume (USD) | $636,553 |
| 24h price change | -0.0175 |
| hours to close | 1035.8 |
| end_date | 2026-06-07T00:00:00Z |
| category | (uncategorised) |
| low-price side | Yes @ 0.0205 |
| low-price token | `91464516107556165907566387619157396733019262339196802152206657889196699256450` |

## Global safety gate: **PASS**

## Per-strategy evaluation

### spread_capture

- **Signal:** `SKIP`
- **Proposed side:** Yes
- **Proposed price:** 0.0300
- **Expected edge / share:** +0.0000
- **Confidence:** 0.20
- **Decision:** `skip`
- **Risk score:** 0.056
- **Reason:** post-only @ 0.03, edge ≈ 0.0000/share

### momentum_reaction

- **Signal:** `SKIP`
- **Decision:** `skip`
- **Risk score:** 0.056
- **Reason:** |24h move| -0.018 < 0.05

### mean_reversion

- **Signal:** `PAPER_LIMIT_BUY`
- **Proposed side:** Yes
- **Proposed price:** 0.0205
- **Expected edge / share:** +0.0200
- **Confidence:** 0.20
- **Decision:** `paper_trade`
- **Risk score:** 0.056
- **Reason:** near-zero extreme 0.021; small re-rate bet

### news_event_no_trade_filter

- **Signal:** `NO_AVOID_FLAG`
- **Decision:** `skip`
- **Risk score:** 0.056
- **Reason:** no news-event risk detected

### endgame_decay

- **Signal:** `SKIP`
- **Decision:** `skip`
- **Risk score:** 0.256
- **Reason:** not endgame (1035.8h to close)

## Paper-trade tracker

Fill outcomes at 15m / 1h / 4h / close are recorded in daily log entries.

## Linked

- [[../daily/2026-04-24|Today's daily log]]
- [[../README|Polymarket journal index]]
- CSV row: `polymarket-bot/reports/polymarket_strategy_scores.csv`

