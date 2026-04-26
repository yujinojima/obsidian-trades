---
title: ranging
type: market-state
updated: 2026-04-25
status: stub
---

# Market State — `ranging`

> [!caution] Status: unlabelled — Phase 1 labeller needed

## Canonical definition (planned)

- EMA20, EMA50, EMA200 braided (no persistent stack), AND
- EMA50 slope near zero, AND
- Price oscillating within a bounded BBW range.

## Inferred observations

None confidently identified in the v1 sample.

## Linked concepts

- [[../concepts/mean-reversion]] — ranging is the regime where mean-reversion signals are hypothesised to perform best.

## Related primitives

- [[../primitives/liquidity-sweep-reversal]] — sweep-reversal has strongest base rate in ranging regimes.

## Open questions

- Is the cointegration strategy's expected "home regime" ranging? (Hypothesis; untested.)
