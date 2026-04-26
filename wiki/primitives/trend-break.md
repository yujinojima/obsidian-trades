---
title: trend-break (provisional)
type: primitive
updated: 2026-04-25
status: provisional
registry_name: null
aliases: [trend-break, structure-break, bos, break-of-structure]
tier: research_candidate
timeframes: [1h, 4h]
---

# trend-break

> [!caution] Provisional — no canonical registry entry
> The registry has no dedicated `trend-break` / structure-break primitive as of this export. This
> page tracks the primitive until it is formally registered.

## Canonical definition (provisional)

Close breaks above the most recent N-bar swing high (`trend_break_up`) or below the most recent
N-bar swing low (`trend_break_down`). Output: boolean + continuous strength (distance through
the broken level, normalised by ATR) + metadata `{lookback: int, direction: up|down}`.

## Why it matters

Trend-break is the symmetric counterpart to `liquidity-sweep-reversal` — same structural feature
(a pivot), opposite interpretation (continuation rather than reversal). Taken together, they
form a pivot-event family whose regime dependence is the primary distinguishing signal:
liquidity sweep resolves favourably in ranging / reversal regimes; trend-break resolves
favourably in trending / breakout regimes.

## Observed firings in this vault

Not observed. No primitive firings exported in v1.

## Linked primitives

- [[liquidity-sweep-reversal]] — same structural event, opposite resolution.
- [[bollinger-squeeze-breakout]] — trend-break is often the resolution form of a squeeze.

## Next tests

- Register `trend-break-up` and `trend-break-down` (two directions, canonical naming) in the
  registry with tier `research_candidate`.
- Compute break → continuation rate by regime.
