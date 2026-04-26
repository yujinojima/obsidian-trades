---
title: "Polymarket Single-Test — Will the Detroit Pistons win the 2026 NBA Finals?"
type: polymarket-single-test
session_date: 2026-04-25
opened_at: 2026-04-24T20:23:06+00:00
status: paper
market_slug: will-the-detroit-pistons-win-the-2026-nba-finals
side: Yes
proposed_price: 0.0325
paper_size_usd: 0.25
paper_shares: 7.6923
strategy: mean_reversion
candidate_score: 2.925
checkpoints_due: [15m, 1h, 4h, close]
---

# Single-Test — Will the Detroit Pistons win the 2026 NBA Finals?

**Opened:** 2026-04-24T20:23:06+00:00  ·  **Mode:** PAPER_MODE (no live order placed)

## Trade intent

| Field | Value |
|---|---|
| side | **Yes** |
| proposed_price | **0.0325** |
| paper size (USD) | **$0.25** |
| paper shares | 7.6923 |
| spread | 0.0010 |
| midpoint | 0.0325 |
| liquidity (USD) | $342,680 |
| hours to close | 1611.6 |
| token_id | `59742411602053785892348440048778056320272639465974092140970920277782290781360` |
| strategy | `mean_reversion` |

## candidate_score breakdown

| Component | Value |
|---|---:|
| liquidity_score | +0.922 |
| spread_score | +0.950 |
| time_to_resolution_score | +0.752 |
| low_price_score | +0.300 |
| ambiguity_penalty | −0.000 |
| news_risk_penalty | −0.000 |
| **total** | **+2.925** |

## Why this trade was selected

- Highest `candidate_score` (2.925) among markets that also produced a firing strategy signal (mean_reversion).
- near-zero extreme 0.033; small re-rate bet
- Composite beats pure-cheap heuristic: liquidity ($342,680) and spread (0.0010) both top-decile among safety-gate survivors.

## Why this trade could fail

- **Cheap price does not equal edge.** Low-priced markets are often cheap because the event is unlikely. A $0.05 market reverting upward assumes a catalyst that may never arrive.
- The selected strategy has confidence = 0.20, which is a self-declared heuristic, not a validated win-rate.
- Orderbook depth at the proposed price is unmeasured — scanner pulled mid/bid/ask but not depth. Fill quality on live is not guaranteed.
- Time-to-resolution is 86+ days; the paper trade won't produce a definitive outcome until close, only interim price moves.

## Outcome checkpoints

Record observed Yes-side price at each interval. Populated by `scripts/polymarket_check_single_trade.py`.

| Checkpoint | Due at | Observed price | Δ from entry | Notes |
|---|---|---:|---:|---|
| entry | 2026-04-24T20:23:06+00:00 | 0.0325 | — | opened |
| 15m | 2026-04-24T20:41:21+00:00 | 0.0325 | +0.00pp | recorded |
| 1h | | | | |
| 4h | | | | |
| close | 2026-07-01T00:00:00Z | | | |

## Linked

- [[../daily/2026-04-25|Today's Polymarket daily log]]
- [[../experiments/mean-reversion|Strategy: mean_reversion]]
- [[../README|Polymarket journal index]]
- CSV row: `polymarket-bot/reports/polymarket_single_trade_test.csv`

