---
title: fair-value-gap-price-discovery
type: primitive
updated: 2026-04-25
status: active
registry_name: fair-value-gap-price-discovery
aliases: [fair-value-gap, fvg, fvg-bullish, fvg-bearish]
tier: sophisticated
timeframes: [4h]
---

# fair-value-gap-price-discovery

## Canonical definition

A three-candle imbalance where price discovery "skips" a zone: on a bullish FVG, candle-1's
high is below candle-3's low (leaving an untraded range in between); on a bearish FVG, candle-1's
low is above candle-3's high. The primitive framing is that price has travelled without liquidity
in the gap zone and has a probabilistic tendency to return to fill it.

## Aliases

- `fair-value-gap`
- `fvg`
- `fvg-bullish`
- `fvg-bearish`

## Registry reference

- `freqtrade/user_data/prim_registry.json` → tier `sophisticated`, timeframes `[4h]`

## Why it matters

FVG is an **order-flow / market-microstructure primitive** — it is one of the few purely
price-derived signals whose rationale is grounded in liquidity rather than statistics. It
composes well with mean-reversion entries (reversion to an unfilled gap) and with
[[liquidity-sweep-reversal]] (sweep into an opposing FVG).

## Observed firings in this vault

> [!warning] Signal-level data unavailable in v1 export
> Not observed in the current trade sample (or, if observed, not exported). Status: provisional
> with respect to this vault's evidence base.

## Linked primitives

- [[liquidity-sweep-reversal]] — common composite setup.
- [[bollinger-squeeze-breakout]] — different family; non-overlapping.

## Next tests

- Detect FVG firings on the current 4h BTC/ETH dataset (4-year history) and compute base-rate
  reversion-to-fill probability by market state.
- Test FVG-filter on the cointegration strategy's entries.
