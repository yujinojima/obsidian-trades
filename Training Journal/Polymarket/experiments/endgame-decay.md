---
title: "Polymarket Experiment — endgame_decay"
type: polymarket-experiment
updated: 2026-04-25
status: active
phase: 1
paper_trades_total: 0
live_trades_total: 0
---

# Experiment — endgame_decay

## Hypothesis

In the final 2–48 hours before resolution, if a market shows **stable one-direction drift**
with no fresh news flow, the drift continues into the settlement. A tiny paper entry in the
drift direction at current price captures the remaining decay.

**Paper-only by design per user spec.** Never unlocks to live — too much settlement risk.

## Entry condition

- `2 ≤ hours_to_close ≤ 48`
- `|one_day_pct| ≥ 0.03` (clear one-direction drift)
- Not flagged by [[news-event-no-trade-filter]]
- All other safety gates pass

## Outcome criteria

- **SUCCESS:** price at resolution is within 5pp of predicted direction from entry
- **FAIL:** price reverses before resolution
- **RESOLVED_NEUTRAL:** market resolves without meaningful further movement

## Current status (2026-04-25)

**Zero paper trades.** No markets in today's scope matched (< 48h remaining AND drift
≥ 0.03). The markets close to resolution in today's fetch were the Iran/BTC markets
already blocked by [[news-event-no-trade-filter]].

## Design tension

- The entry condition `2 ≤ hours_to_close ≤ 48` is deliberately narrow — the same window
  the news-event filter partially blocks via its "< 7 days to close" rule.
- These two strategies **overlap by design**: most sub-48h markets are news-sensitive, so
  most will fail the AVOID filter. The endgame_decay strategy only fires when the market
  is near-resolution AND stable — a rare combination.
- Expected fire rate: ~1–3 per 100 scanned markets.

## Next adjustment

- **Wait for markets that qualify.** Not every scan will produce an endgame_decay signal,
  and that's correct — over-eager endgame trading is the classic settlement-risk mistake.
- **Post-mortem discipline.** When a market resolves that would have qualified (had it been
  scanned in-window), check whether the paper entry would have won. Use `markets/*.md`
  pages with expired `end_date` as a backtest corpus.

## Linked

- [[../daily/2026-04-25|Today's daily log]]
- [[../README|Polymarket journal index]]
- Source: `polymarket-bot/scripts/polymarket_strategy_scan.py` → `score_endgame_decay()`
