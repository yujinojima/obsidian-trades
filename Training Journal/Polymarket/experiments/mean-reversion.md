---
title: "Polymarket Experiment — mean_reversion"
type: polymarket-experiment
updated: 2026-04-25
status: active
phase: 1
paper_trades_total: 18
live_trades_total: 0
---

# Experiment — mean_reversion

## Hypothesis

Polymarket markets with **low-side implied probability ≤ 5%** over-penalise the low-
probability outcome. Over the market's lifetime, any non-zero news event (team starts
winning, rumour, draw reveal, etc.) should re-rate the low side upward by 2–5pp. Buying
the stretched side cheaply captures this re-rate.

**Confidence is low by design.** This is a lottery-ticket strategy whose statistical power
comes from many small bets, not high per-trade edge.

## Entry condition

- `low_price ≤ 0.05`
- All safety gates pass (spread, liquidity, time-to-close, non-dust)
- **Order:** limit buy at `low_price`, size = 1 share paper-mode, GTC
- **Sizing rationale:** each bet is independently small; expected loss per trade ≤ $0.05

## Outcome criteria (per trade)

- **SUCCESS:** price ≥ entry + 2pp at close (re-rate captured)
- **FAIL:** price ≤ entry at close (low side decayed further — expected for most)
- **PARTIAL:** price moved in between but settled flat

**Win rate expectation: 20–30%.** Strategy is positive-EV only if the average winner (say
+3-5pp) exceeds `losses × (1 − WR) / WR`. Needs a sample of ≥ 30 trades to confirm.

## Current status (2026-04-25)

**18 paper trades opened today** across the following markets (all Yes @ ≤ $0.05):

| Market | Entry price |
|---|---:|
| Belgium WC 2026 | $0.0205 |
| Hormuz normal-traffic by Apr 30 | flagged AVOID by news-filter — not traded |
| Lorenzo Musetti Men's French Open | ~$0.023 |
| Rafael López Aliaga Peru pres 2026 | $0.027 |
| Minnesota Timberwolves NBA Finals | $0.031 |
| Detroit Pistons NBA Finals | $0.033 |
| (etc — see [[../../../../polymarket-bot/reports/polymarket_strategy_scores.csv|CSV]]) | |

Full list: filter `decision=paper_trade` AND `strategy=mean_reversion` in the CSV.

## What's uncertain (pre-monitor)

- Whether the re-rate hypothesis actually plays out on these 18. Without an outcome
  tracker, we have entries only, no realised outcomes yet.
- Whether the strategy fires too eagerly. Current rule `low_price ≤ 0.05` means every
  low-price market fires — may need tightening (add a "price has been flat for N days"
  condition to rule out already-decaying markets).

## What failed (self-critique of the scan)

- **Selection effect not controlled.** Top-20 by `low_price asc` IS the mean_reversion
  candidate pool by definition. So 18/20 firing tells us nothing about discrimination —
  the strategy didn't select these, the scan did.
- **All 18 paper entries are concentrated in the lowest-probability corner of the market
  universe.** That's consistent with the strategy's definition but means the 18-trade
  sample is highly correlated.

## Next adjustment

- **Build outcome monitor** — cron job that re-fetches each market's Yes price at 15m / 1h
  / 4h / close and appends to the market page. Without this, Phase 2 cannot unlock.
- **Add a stratification.** Split the scan into "extreme" ( ≤ 0.05 ) and "near-extreme"
  ( 0.05–0.10 ) buckets and track outcomes separately. Hypothesis: extreme might decay
  more often than near-extreme — they are different sub-distributions.
- **Tighten the entry rule.** After n ≥ 30 outcomes, recompute the win rate and adjust
  the `low_price ≤` threshold to wherever win rate peaks.

## Linked

- [[../daily/2026-04-25|Today's daily log (18 paper trades opened)]]
- [[../markets/will-belgium-win-the-2026-fifa-world-cup-358|Best-candidate market page]]
- [[../README|Polymarket journal index]]
- Source: `polymarket-bot/scripts/polymarket_strategy_scan.py` → `score_mean_reversion()`
