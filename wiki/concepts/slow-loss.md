---
title: Slow Loss
type: concept
updated: 2026-04-25
status: active
evidence_count: 1
---

# Slow Loss

> [!caution] Provisional — evidence_count = 1

## Definition

A losing trade whose drawdown accumulates gradually rather than via a sharp adverse move. The
adverse excursion is not dramatic relative to volatility, the stop never trips, but realised PnL
slowly drifts negative until the exit signal closes the trade.

Operational shape (v1 export): realised PnL < 0, MAE closer to stop than to entry, duration
longer than the median winner.

## Why it matters

Slow losses are indistinguishable from viable holds on an intraday basis — they only reveal
themselves over time. They consume capital and attention without an identifiable turning point,
and are the natural weakness of signals that **exit by reversion target** rather than by
stop-out.

## Evidence (1 trade)

- [[../trades/YujiCointegrationResidualReversionStrategy/trade_0003]] · ETH/USDT · -2.65% · exit=`coint_z_reverted`

## Linked concepts

- [[mean-reversion]] — slow loss is a characteristic failure mode of reversion-to-the-mean exits.
- [[../exit-analysis/coint-z-reverted]] — the exit that fired here.

## Open questions

- Does adding a time-stop or adverse-excursion-stop cut slow losses without cutting winners? (Needs a larger sample.)

## Next tests

- Too-few-observations (n=1). Re-evaluate when n ≥ 5.
