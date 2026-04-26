---
title: Mean Reversion (signal family)
type: concept
updated: 2026-04-25
status: active
evidence_count: 8
---

# Mean Reversion

## Definition

A signal family predicated on the hypothesis that a series has a central tendency and that extreme
deviations from that tendency are more likely to revert than to continue. In the trades vault this
shows up specifically as **cointegration residual z-score reversion**: a linear combination of two
assets (e.g. ETH and a partner) whose residual series is tested for stationarity; entries fire when
the residual's z-score exceeds a threshold, exits fire when it reverts toward zero.

## Why it matters

Mean-reversion signals behave very differently from momentum/trend signals:

- They tend to have **higher win rate, lower average R**.
- They are **vulnerable to regime breaks** — a cointegration relationship that decays during a
  trend regime can give rise to losses while the z-score keeps extending.
- They **exit by design at the mean**, which is structurally prone to [[missed-continuation]] when
  the underlying leg keeps trending post-reversion.

## Evidence (this vault)

| Strategy | Signal | Trades | Win rate | Profit sum |
|---|---|---:|---:|---:|
| [[../strategies/YujiCointegrationResidualReversionStrategy]] | `coint_z` threshold cross | 8 | 75% | +54.37% |

## Linked primitives

Mean-reversion setups often coincide with [[../primitives/bollinger-squeeze-breakout|volatility compression]]
(the residual's volatility contracts before the reversion fires). Signal-level confirmation is
unavailable in v1 export; Phase 1 labeller will make this testable.

## Linked market states

Mean reversion should work best in [[../market-states/ranging]] and poorly in strong
[[../market-states/trending-up|trending]] / [[../market-states/trending-down|trending-down]] regimes.
That hypothesis is untested in this vault until market-state labels are populated.

## Open questions

- Are the [[../concepts/missed-continuation|missed-continuation]] trades concentrated in trending regimes? (Plausible — if the instrument is trending, the z-score reverting does not mean the instrument has stopped moving.)
- Does a volatility-state filter (compression → expansion) improve win rate?

## Next tests

- Stratify the 8 trades by market state once Phase 1 ships.
- Test an "exit only when z-score reverts AND underlying instrument volatility expands" rule.
