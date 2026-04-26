---
title: "Polymarket Single-Test — Will the Iranian regime fall by May 31?"
type: polymarket-single-test
session_date: 2026-04-25
opened_at: 2026-04-24T20:21:36+00:00
status: paper
market_slug: will-the-iranian-regime-fall-by-may-31
side: Yes
proposed_price: 0.0315
paper_size_usd: 0.25
paper_shares: 7.9365
strategy: mean_reversion
candidate_score: 3.036
checkpoints_due: [15m, 1h, 4h, close]
---

# Single-Test — Will the Iranian regime fall by May 31?

**Opened:** 2026-04-24T20:21:36+00:00  ·  **Mode:** PAPER_MODE (no live order placed)

## Trade intent

| Field | Value |
|---|---|
| side | **Yes** |
| proposed_price | **0.0315** |
| paper size (USD) | **$0.25** |
| paper shares | 7.9365 |
| spread | 0.0030 |
| midpoint | 0.0315 |
| liquidity (USD) | $364,481 |
| hours to close | 867.6 |
| token_id | `57360053771630303266236723124451177814047338705194149193939656360140487569996` |
| strategy | `mean_reversion` |

## candidate_score breakdown

| Component | Value |
|---|---:|
| liquidity_score | +0.927 |
| spread_score | +0.850 |
| time_to_resolution_score | +0.959 |
| low_price_score | +0.300 |
| ambiguity_penalty | −0.000 |
| news_risk_penalty | −0.000 |
| **total** | **+3.036** |

## Why this trade was selected

- Highest `candidate_score` (3.036) among markets that also produced a firing strategy signal (mean_reversion).
- near-zero extreme 0.032; small re-rate bet
- Composite beats pure-cheap heuristic: liquidity ($364,481) and spread (0.0030) both top-decile among safety-gate survivors.

## Why this trade could fail

- **Cheap price does not equal edge.** Low-priced markets are often cheap because the event is unlikely. A $0.05 market reverting upward assumes a catalyst that may never arrive.
- The selected strategy has confidence = 0.20, which is a self-declared heuristic, not a validated win-rate.
- Orderbook depth at the proposed price is unmeasured — scanner pulled mid/bid/ask but not depth. Fill quality on live is not guaranteed.
- Time-to-resolution is 86+ days; the paper trade won't produce a definitive outcome until close, only interim price moves.

## Outcome checkpoints

Record observed Yes-side price at each interval. Populated by `scripts/polymarket_check_single_trade.py`.

| Checkpoint | Due at | Observed price | Δ from entry | Notes |
|---|---|---:|---:|---|
| entry | 2026-04-24T20:21:36+00:00 | 0.0315 | — | opened |
| 15m | | | | |
| 1h | | | | |
| 4h | | | | |
| close | 2026-05-31T00:00:00Z | | | |

## Linked

- [[../daily/2026-04-25|Today's Polymarket daily log]]
- [[../experiments/mean-reversion|Strategy: mean_reversion]]
- [[../README|Polymarket journal index]]
- CSV row: `polymarket-bot/reports/polymarket_single_trade_test.csv`

