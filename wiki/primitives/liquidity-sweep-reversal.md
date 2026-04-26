---
title: liquidity-sweep-reversal
type: primitive
updated: 2026-04-25
status: active
registry_name: liquidity-sweep-reversal
aliases: [liquidity-sweep, sweep, stop-hunt, liquidity-grab]
tier: sophisticated
timeframes: [1h, 4h]
---

# liquidity-sweep-reversal

## Canonical definition

Price takes out a recent swing extreme (high or low) and then closes back through it — sweeping
stop-loss liquidity that was resting above/below the pivot, then reversing. Two directions:

- **sweep-high (bearish)**: price makes a new high, then closes back below the prior swing high.
- **sweep-low (bullish)**: price makes a new low, then closes back above the prior swing low.

## Aliases

- `liquidity-sweep`
- `sweep`
- `stop-hunt`
- `liquidity-grab`

## Registry reference

- `freqtrade/user_data/prim_registry.json` → tier `sophisticated`, timeframes `[1h, 4h]`

## Why it matters

Liquidity sweep is one of the cleanest microstructure signals: it identifies moments where the
market has just consumed a pool of resting orders and has a structural reason to mean-revert
(the liquidity pool that was fuelling the move is now exhausted). It composes well with
[[../concepts/mean-reversion]] setups and is a classical input to the "sweep reversal" strategies
in the prompt spec (Sweep Reversal Long / Short).

## Observed firings in this vault

> [!warning] Signal-level data unavailable in v1 export
> Not observed in the current trade sample — signal export not yet wired.

## Linked primitives

- [[fair-value-gap-price-discovery]] — frequent composite: sweep into the far side of an FVG, reverse to fill.
- [[volume-spike]] (provisional) — volume spike on the sweep bar adds confirmation.

## Next tests

- Detect sweeps on 4-year 1h BTC/ETH and compute base-rate next-N-bar reversion probability by regime.
- Feature: add a `recent_liquidity_sweep` flag to the ML dataset produced by Phase 2.
