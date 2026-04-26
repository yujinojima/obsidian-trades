---
title: efficient_exit (exit diagnosis)
type: exit-diagnosis
updated: 2026-04-25
status: active
evidence_count: 336
evidence_count_total_trades: 3300
cross_strategy_source: data/all_trades_dataset.csv (3300 trades, 15 strategies)
---

# Exit Diagnosis — `efficient_exit`

## Full-library evidence (added 2026-04-25)

Source: `data/all_trades_dataset.csv`. **336 trades** across the 3,300-trade library carry the
`efficient_exit` diagnosis (10.2% of all trades). This is the second-smallest exit-diagnosis
bucket in the dataset; `stop_loss_failure` (129) is smaller. The diagnosis is the positive
mirror of [[premature-exit]] — when it appears, the exit rule did its job for that trade.

## Prior single-trade note

## Definition

A code-level diagnostic label for trades whose exit fired near the MFE extremum. The exit rule
captured most of the available move. This is the target behaviour; the exit is not the limiting
factor on this trade's expectancy.

## Evidence

- [[../trades/YujiCointegrationResidualReversionStrategy/trade_0004]] · ETH/USDT · +5.49% · [[../concepts/noisy-win|noisy_win]]

## Linked strategies

- [[../strategies/YujiCointegrationResidualReversionStrategy]] — 1/8 trades diagnosed efficient_exit.

## Next tests

Too-few-observations (n=1). Re-evaluate when n ≥ 5.
