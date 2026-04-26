---
title: trending-up
type: market-state
updated: 2026-04-25
status: stub
---

# Market State — `trending_up`

> [!caution] Status: unlabelled
> The v1 trade export contains a rough EMA-stack description per trade (e.g. "downtrend EMA20<50<200")
> but does not apply the composite `market_state` labels defined in the research pipeline plan.
> Real population of this page requires **Phase 1 — Market-State Labeller**
> (`research/src/labels/market_state.py`). Until then, the observations below are inferred from
> per-trade EMA-stack metadata and should be treated as provisional.

## Canonical definition (planned)

Composite label assigned when:
- EMA20 > EMA50 > EMA200 (stack alignment), AND
- EMA50 slope positive over last N bars, AND
- ADX > threshold (if computed).

## Inferred observations (from v1 trade metadata)

- None of the 8 exported trades entered in a `trending_up` regime by EMA-stack.

## Linked strategies

- (none yet)

## Related primitives

- [[../primitives/trend-break]] — trend-break-up fires within this regime most informatively.

## Next tests

- Implement Phase 1 labeller and backfill this page from full 4-year history.
