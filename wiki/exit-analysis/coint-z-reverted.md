---
title: coint_z_reverted (exit reason)
type: exit-diagnosis
updated: 2026-04-25
status: active
evidence_count: 8
---

# Exit Reason — `coint_z_reverted`

## Definition

The exit signal fires when the cointegration residual's z-score retraces toward zero — i.e., the
spread that the entry was betting on to revert has reverted. Defined in strategy code, not in a
generic exit handler.

## Why it matters

This is the **only** exit the strategy uses in the current export — 8 of 8 trades closed under
this rule. That level of exit concentration means the exit is *the* variable to test; any
improvement to the strategy's expectancy likely comes from changing this rule, not the entry.

## Evidence (8 trades, 100% of sample)

| # | Pair | Realised | MFE | Outcome | Exit diagnosis |
|---:|---|---:|---:|---|---|
| [[../trades/YujiCointegrationResidualReversionStrategy/trade_0001\|0001]] | ETH/USDT | +9.39% | +16.08% | [[../concepts/missed-continuation\|missed_continuation]] | [[premature-exit]] |
| [[../trades/YujiCointegrationResidualReversionStrategy/trade_0002\|0002]] | ETH/USDT | +5.42% | — | [[../concepts/missed-continuation\|missed_continuation]] | [[premature-exit]] |
| [[../trades/YujiCointegrationResidualReversionStrategy/trade_0003\|0003]] | ETH/USDT | -2.65% | — | [[../concepts/slow-loss\|slow_loss]] | poor_entry |
| [[../trades/YujiCointegrationResidualReversionStrategy/trade_0004\|0004]] | ETH/USDT | +5.49% | — | [[../concepts/noisy-win\|noisy_win]] | [[efficient-exit]] |
| [[../trades/YujiCointegrationResidualReversionStrategy/trade_0005\|0005]] | ETH/USDT | +26.57% | — | [[../concepts/missed-continuation\|missed_continuation]] | [[premature-exit]] |
| [[../trades/YujiCointegrationResidualReversionStrategy/trade_0006\|0006]] | ETH/USDT | -4.37% | — | [[../concepts/bad-entry-good-idea\|bad_entry_good_idea]] | [[poor-entry]] |
| [[../trades/YujiCointegrationResidualReversionStrategy/trade_0007\|0007]] | ETH/USDT | +8.10% | — | [[../concepts/clean-win\|clean_win]] | [[premature-exit]] |
| [[../trades/YujiCointegrationResidualReversionStrategy/trade_0008\|0008]] | LINK/USDT | +6.43% | — | [[../concepts/missed-continuation\|missed_continuation]] | [[premature-exit]] |

## Aggregate findings

- Average MFE: +13.60% / Average realised: +6.80% → **MFE capture 62.83%** in winners.
- **premature_exit** diagnosis on 5/8 (62.5%) trades — this exit is firing too early.
- No stop exits in the sample — the stoploss never fired.

## Linked concepts

- [[../concepts/mean-reversion]] — `coint_z_reverted` is the canonical reversion-to-mean exit.
- [[../concepts/missed-continuation]] — the pathology this exit produces most.
- [[../concepts/mfe-capture-ratio]] — the metric that characterises this exit's cost.

## Linked strategies

- [[../strategies/YujiCointegrationResidualReversionStrategy]] — the only strategy using this exit in v1.

## Open questions

- See [[../questions/trailing-stop-vs-coint-z-reverted]].
- Does a **hybrid** (take partial at z=0, let remainder trail) outperform both the pure revert-to-mean and the pure trailing stop?

## Next tests

See [[../strategies/YujiCointegrationResidualReversionStrategy#What should be tested next]].
