---
title: poor_entry (exit diagnosis)
type: exit-diagnosis
updated: 2026-04-25
status: active
evidence_count: 1
---

# Exit Diagnosis — `poor_entry`

> [!caution] Provisional — evidence_count = 1

## Definition

A code-level diagnostic label for trades that lost money but in a way that implicates the **entry**
rather than the exit. Characteristic: adverse excursion dominates favourable excursion, the trade
never meaningfully moves in favour, realised PnL is negative. The exit was not what went wrong;
the entry arrived in conditions the signal should have filtered.

## Evidence

- [[../trades/YujiCointegrationResidualReversionStrategy/trade_0006]] · ETH/USDT · -4.37% · [[../concepts/bad-entry-good-idea|bad_entry_good_idea]]

## Linked concepts

- [[../concepts/bad-entry-good-idea]]

## Linked strategies

- [[../strategies/YujiCointegrationResidualReversionStrategy]] — 1/8 trades diagnosed poor_entry.

## Next tests

Too-few-observations. Once sample grows, cluster poor_entry trades by entry-time market state — look
for a regime filter that would have blocked them.
