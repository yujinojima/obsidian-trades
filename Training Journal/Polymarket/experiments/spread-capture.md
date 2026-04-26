---
title: "Polymarket Experiment — spread_capture"
type: polymarket-experiment
updated: 2026-04-25
status: active
phase: 1
paper_trades_total: 0
live_trades_total: 0
---

# Experiment — spread_capture

## Hypothesis

On Polymarket binary markets with **tight but non-trivial spreads** ($0.02–$0.05) and
**≥ $10,000 liquidity**, posting a passive post-only limit at `best_bid + 1 tick` captures
bid-ask edge when opposing flow crosses. Polymarket has no maker fees on most markets, so
captured spread is gross profit (minus settlement risk).

## Entry condition

- `spread ≥ 2 × tick_size` (room to add)
- `liquidity ≥ $10,000`
- `hours_to_close ≥ 24`
- `low_price ≥ $0.02`
- **Order:** post-only limit at `best_bid + tick_size`; cancel and re-post if best_bid moves away

## Outcome criteria (per trade)

- **SUCCESS:** filled at proposed price AND price ≥ proposed at 4h mark (realised the edge)
- **FAIL:** filled and price < proposed at close (adverse)
- **NO FILL:** neither filled nor cancelled-by-book-movement within 4h (noise, no data)

## Current status (2026-04-25)

**Zero paper trades.** Scanner's $0.01 tick assumption is too coarse for the sub-$0.10
long-shot markets the phase-1 candidate pool concentrates on (real tick on those is $0.001,
which means every "tight spread" market has spread < scanner tick → no viable proposal).

## What failed

- Candidate pool was wrong. Top-20 ranked by `low_price asc` is a long-shot bucket where
  spread_capture cannot fire. The strategy needs $0.20–$0.80 bracket markets.
- Scanner tick assumption needs to read real tick from the market config.

## Next adjustment

- **Diversify candidate pool.** Add a second ranking pass that picks 10 markets from the
  0.20–0.80 mid-probability band with the widest spreads, not the lowest prices.
- **Pull real tick from CLOB** (`/markets/{condition_id}` returns `minimum_tick_size`).
- **Then re-run** spread_capture on the mid-band subset.

## Linked

- [[../daily/2026-04-25|Today's daily log]]
- [[../README|Polymarket journal index]]
- Source: `polymarket-bot/scripts/polymarket_strategy_scan.py` → `score_spread_capture()`
