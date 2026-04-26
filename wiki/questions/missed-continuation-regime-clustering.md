---
title: Do missed-continuation trades cluster by regime?
type: question
updated: 2026-04-25
status: open
---

# Question — Do missed-continuation trades cluster by regime?

## The question

Of the 4 [[../concepts/missed-continuation|missed-continuation]] trades in the sample, do they share
a common market-state signature at entry — most plausibly, entering while the underlying
instrument is itself trending, so reversion-of-residual does not imply exhaustion-of-move?

## Why it matters

If missed-continuation is concentrated in a specific regime, then the expectancy fix is not
necessarily a different exit rule — it could be a **regime filter at entry** plus regime-specific
exits. That's a different and possibly better intervention than replacing the exit entirely
(see [[trailing-stop-vs-coint-z-reverted]]).

## How to answer

Requires Phase 1 market-state labeller to ship. Once labels exist:

1. Label each of the 8 trades with its entry-bar market state.
2. Count missed-continuation occurrence per state.
3. Compare against the base rate of each state over the same calendar period.

## Status

Blocked on Phase 1.

## Resolution

(pending)
