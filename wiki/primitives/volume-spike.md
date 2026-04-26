---
title: volume-spike (provisional)
type: primitive
updated: 2026-04-25
status: provisional
registry_name: null
aliases: [volume-spike, volume-burst, rel-volume-spike]
tier: research_candidate
timeframes: [1h, 4h]
---

# volume-spike

> [!caution] Provisional — no canonical registry entry
> The existing `freqtrade/user_data/prim_registry.json` contains `volume-clock-informed-trading`
> (axis 40, intermediate tier), which is a related but semantically distinct primitive (VPIN /
> informed-trading flow, not a simple z-score spike). This page tracks the simpler
> `volume-spike` primitive until it is formally registered.

## Canonical definition (provisional)

Current-bar volume's z-score relative to a trailing N-bar rolling mean/std exceeds a threshold
(commonly z > 2). Boolean firing + continuous strength (the z itself, clipped to [0, 1] via a
sigmoid of your choice) + metadata `{window: int, threshold: float}`.

## Observed firings in this vault

Inferred from v1 trade metadata (`volume_vs_20bar_avg` ratio):

- [[../trades/YujiCointegrationResidualReversionStrategy/trade_0001]] — 1.61× 20-bar avg (weak spike, below typical threshold)

The v1 export reports a ratio, not a z-score; it is not a faithful proxy but is close enough for
audit.

## Linked primitives

- [[liquidity-sweep-reversal]] — volume confirmation on a sweep bar.
- [[bollinger-squeeze-breakout]] — volume expansion on breakout resolution.

## Next tests

- Register `volume-spike` as a primitive in the freqtrade registry (separate from
  `volume-clock-informed-trading`).
- Define the canonical computation: rolling z-score, window = 20 bars, threshold = 2.0.
- Compute base rates for each market state.
