---
title: bollinger-squeeze-breakout
type: primitive
updated: 2026-04-25
status: active
registry_name: bollinger-squeeze-breakout
aliases: [volatility-compression, bb-squeeze, squeeze, compression]
tier: sophisticated
timeframes: [4h]
axis: 17
---

# bollinger-squeeze-breakout

## Canonical definition

A volatility-compression primitive detecting periods where Bollinger Band width (or an equivalent
range measure) sits below a rolling percentile threshold — "the squeeze" — followed by a directional
breakout. The setup is the compression; the firing event is the breakout out of it.

## Aliases

- `volatility-compression`
- `bb-squeeze`
- `squeeze`
- `compression`

## Registry reference

- `freqtrade/user_data/prim_registry.json` → axis 17, tier `sophisticated`, timeframes `[4h]`
- Memory: elevated to `sophisticated` in recent cycle work (see git log: `feat: apply vpin-toxicity-gate sophisticated advances` and adjacent commits).

## Why it matters

Volatility compression is a leading indicator for regime change. A squeeze that resolves into a
directional break creates trades with asymmetric MFE/MAE profiles (the breakout direction runs;
the rejected direction fails fast). It is a natural **entry filter** for mean-reversion exits
when the breakout aligns with the reversion direction, and a natural **exit trigger** for
counter-breakout positions when a squeeze is detected against the position.

## Observed firings in this vault

> [!warning] Signal-level data unavailable in v1 export
> Trade pages in this vault carry a rough volatility-regime snapshot at entry (20b/50b range ratio)
> derived from price history, but **do not** carry registry primitive firings. The connection
> between this page and individual trades is inferred from per-trade volatility snapshots, not
> from exported primitive data.

Inferred matches (compression snapshots at entry, from v1 trade metadata):

- [[../trades/YujiCointegrationResidualReversionStrategy/trade_0001]] — 20b/50b range = 0.44 (compression)
- Other trades' compression states are embedded in each page's `Setup Explanation` section.

## Linked concepts

- [[../concepts/mean-reversion]] — mean-reversion setups often coincide with compression before resolution.

## Linked market states

- [[../market-states/compression]]
- [[../market-states/high-volatility]] — the state a successful breakout resolves into.

## Next tests

- Once Phase 3 discovery layer ships, compute expectancy of strategies gated by
  `bollinger-squeeze-breakout = true` at entry.
- Cross-reference [[../concepts/missed-continuation]] trades against compression-at-entry:
  do missed-continuation trades originate from compression regimes more often than random?
