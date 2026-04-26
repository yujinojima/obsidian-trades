---
title: compression
type: market-state
updated: 2026-04-25
status: stub
---

# Market State — `compression`

> [!caution] Status: unlabelled — Phase 1 labeller needed

## Canonical definition (planned)

- 20-bar range / 50-bar range < threshold (classic "squeeze" framing), OR
- BBW at low percentile, OR
- ATR at low percentile.

## Inferred observations (from v1 trade metadata)

Several trades entered with the v1 compression tag:

- [[../trades/YujiCointegrationResidualReversionStrategy/trade_0001]] — compression (20b/50b range = 0.44)
- Others — see each trade's Setup Explanation section.

## Related primitives

- [[../primitives/bollinger-squeeze-breakout]] — the specific primitive used to detect compression.

## Open questions

- Does the cointegration strategy enter disproportionately from compression? (Likely yes,
  because reversion signals tend to fire after a contracted-range period. Needs Phase 1
  labeller to confirm with proper base rates.)
- Do compression-entries outperform non-compression entries on this strategy?
