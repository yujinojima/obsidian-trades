---
title: Noisy Win
type: concept
updated: 2026-04-25
status: active
evidence_count: 1
---

# Noisy Win

> [!caution] Provisional — evidence_count = 1

## Definition

A winning trade whose path to the exit was volatile — meaningful adverse excursion occurred
before the position ultimately closed green. The outcome was correct; the journey was not clean.

Operational shape (v1 export): realised PnL > 0, MAE > small threshold, MFE/MAE ratio < 2.

## Why it matters

Noisy wins are psychologically and operationally expensive: they look like slow losses for much
of their duration, which tempts discretionary intervention and creates real risk of cutting a
winner early. For a rule-based system the risk is different — the trade may be dangerous to
compound because position-sizing that assumes a clean path will underperform.

## Evidence (1 trade)

- [[../trades/YujiCointegrationResidualReversionStrategy/trade_0004]] · ETH/USDT · +5.49% · exit=`coint_z_reverted`

## Linked concepts

- [[mfe-capture-ratio]] — noisy wins often still capture most of a modest MFE.

## Next tests

- Too-few-observations (n=1).
