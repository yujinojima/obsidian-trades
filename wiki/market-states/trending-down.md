---
title: trending-down
type: market-state
updated: 2026-04-25
status: stub
---

# Market State — `trending_down`

> [!caution] Status: unlabelled
> See [[trending-up#Status]] — same caveat. Phase 1 labeller needed.

## Canonical definition (planned)

- EMA20 < EMA50 < EMA200, AND
- EMA50 slope negative over last N bars, AND
- ADX > threshold (if computed).

## Inferred observations (from v1 trade metadata)

At least one trade — [[../trades/YujiCointegrationResidualReversionStrategy/trade_0001]] — entered
with EMA20<50<200 stack ("downtrend EMA20<50<200"). Whether this qualifies as `trending_down`
under the composite definition depends on the slope test.

## Linked strategies

- [[../strategies/YujiCointegrationResidualReversionStrategy]] — entries in this regime produced
  [[../concepts/missed-continuation]] outcomes, consistent with the hypothesis that
  mean-reversion signals produce missed-continuation *because* the underlying trend persists.

## Related primitives

- [[../primitives/trend-break]] — trend-break-down fires within this regime.

## Open questions

- Do all 4 missed-continuation trades share this regime? (Needs Phase 1 labeller to answer.)
