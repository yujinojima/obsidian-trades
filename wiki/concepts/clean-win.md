---
title: Clean Win
type: concept
updated: 2026-04-25
status: active
evidence_count: 1
---

# Clean Win

> [!caution] Provisional — evidence_count = 1

## Definition

A winning trade that went favourably shortly after entry, spent little time underwater, captured
most of its MFE, and exited near the peak. The reference shape for "the strategy working as
designed."

Operational shape (v1 export): realised PnL > 0, small MAE (< ~1/3 of MFE), high MFE capture
(> ~0.75), duration short relative to the strategy's median.

## Why it matters

Clean wins are the template. They show what the system looks like when signal, entry, and exit
are all aligned. Their distinguishing features (market state, volatility regime, time-of-day,
pair) are the best targets for replication — if you can characterise them, you can try to
trade only when those conditions hold.

## Evidence (1 trade)

- [[../trades/YujiCointegrationResidualReversionStrategy/trade_0007]] · ETH/USDT · +8.10% · duration ≈ 1.2 days · exit=`coint_z_reverted`

## Linked concepts

- [[mfe-capture-ratio]] — clean wins sit at the top of the capture distribution.

## Next tests

- Too-few-observations (n=1).
- Once sample grows: fit a classifier predicting `outcome == clean_win` from entry-time features.
  That classifier becomes a candidate entry filter.
