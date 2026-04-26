---
title: Bad Entry, Good Idea
type: concept
updated: 2026-04-25
status: active
evidence_count: 1
---

# Bad Entry, Good Idea

> [!caution] Provisional — evidence_count = 1

## Definition

A losing trade where the underlying thesis was reasonable but the entry was mistimed — the signal
fired too early (before confirmation) or at a location that left insufficient room between entry
and stop. The adverse excursion exceeds what the thesis should tolerate; the idea itself was not
invalidated by what happened next.

Distinguished from [[slow-loss]] by **path**: slow loss drifts, bad-entry drops. Distinguished from
[[../exit-analysis/poor-entry|poor_entry diagnosis]] in that the latter is a code-level exit-analysis label
whereas this is the outcome classification.

## Why it matters

Bad-entry trades are the highest-leverage diagnostic for **entry filtering**. If a strategy has a
cluster of these, tightening the entry rule (additional confirmation, wider threshold, filter on
regime) typically raises expectancy without sacrificing sample size much.

## Evidence (1 trade)

- [[../trades/YujiCointegrationResidualReversionStrategy/trade_0006]] · ETH/USDT · -4.37% · exit=`coint_z_reverted`
- Also diagnosed as [[../exit-analysis/poor-entry|poor_entry]] at the exit-analysis layer.

## Next tests

- Too-few-observations (n=1).
- When sample grows: cross-reference with market state at entry (does bad-entry cluster in a regime?).
