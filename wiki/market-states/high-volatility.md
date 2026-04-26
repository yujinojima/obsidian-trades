---
title: high-volatility
type: market-state
updated: 2026-04-25
status: stub
---

# Market State — `high_volatility`

> [!caution] Status: unlabelled — Phase 1 labeller needed

## Canonical definition (planned)

- ATR percentile above threshold over N-bar window, OR
- Bollinger Band width percentile above threshold, OR
- Realised volatility (close-to-close) above threshold.

## Related primitives

- [[../primitives/bollinger-squeeze-breakout]] — the *resolution* of a squeeze typically lands here.

## Inferred observations

None in the 8-trade sample enter in clearly-high-volatility regimes by EMA/BBW snapshots.
