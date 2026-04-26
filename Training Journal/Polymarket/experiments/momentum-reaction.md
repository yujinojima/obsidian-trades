---
title: "Polymarket Experiment — momentum_reaction"
type: polymarket-experiment
updated: 2026-04-25
status: active
phase: 1
paper_trades_total: 0
live_trades_total: 0
---

# Experiment — momentum_reaction

## Hypothesis

When a Polymarket binary market's implied probability moves sharply (|24h change| ≥ 5pp)
AND volume confirms (`vol24 ≥ $100,000`), the move contains information and continuation
follow-through occurs over the next 1–4 hours. A small entry at the current price captures
a slice of the continuation.

## Entry condition

- `|one_day_pct| ≥ 0.05` (≥ 5pp move in 24h)
- `vol24 ≥ $100,000`
- All safety gates pass
- **Order:** limit buy in direction of the move at `price − 1 tick` (slight patience discount)

## Outcome criteria (per trade)

- **SUCCESS:** price continues in the entry direction by ≥ 2pp over the following 4h
- **FAIL:** price reverses by ≥ 2pp over the following 4h
- **FLAT:** |movement| < 2pp over 4h (signal was noise)

## Current status (2026-04-25)

**Zero paper trades.** Scanner filtered top-20 by `low_price asc`; none had |24h move| ≥ 5pp.
Long-shot sub-$0.05 markets don't move enough in absolute terms to trigger this signal.

## What failed

- Same selection bias as [[spread-capture]]: the low_price-ranked candidate pool doesn't
  contain markets that would fire momentum signals. Mid-probability (0.20–0.80) markets are
  where absolute probability moves of 5pp+ actually occur.

## Next adjustment

- **Re-rank candidate pool** to include the `|one_day_pct|` top decile. A separate ranking
  query on Gamma (`order=oneDayPriceChange&ascending=false`) would surface exactly the
  candidates this strategy needs.
- **Consider volume-confirmation tightening.** $100k is low — news-driven moves tend to
  produce $500k+ volume spikes. Raising the floor to $250k would improve signal quality.

## Linked

- [[../daily/2026-04-25|Today's daily log]]
- [[../README|Polymarket journal index]]
- Source: `polymarket-bot/scripts/polymarket_strategy_scan.py` → `score_momentum_reaction()`
