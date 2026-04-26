---
title: Does the cointegration strategy port off ETH/USDT?
type: question
updated: 2026-04-25
status: open
---

# Question — Does the cointegration strategy port off ETH/USDT?

## The question

7 of 8 exported trades are on ETH/USDT (88%). LINK/USDT contributed 1 winner. Is the strategy's
positive expectancy an ETH-specific artefact, or does it hold across the Binance universe
(BTC, SOL, XRP, AVAX, LINK, DOGE, ADA)?

## Why it matters

Single-pair strategies are legitimate but fragile. If expectancy doesn't transfer, we learn
something about either the cointegration methodology (maybe the partner-asset pairing is
ETH-specific) or about ETH itself (e.g. its relationship with a particular macro asset during
2022-2025).

## How to answer

Re-run [[../strategies/YujiCointegrationResidualReversionStrategy]] across the full
`user_data/config-backtest-binance.json` pair list. Already supported by the existing
`freqtrade/batch-backtest.sh` — just needs a full-universe invocation.

## Status

Open. Not blocked on any pipeline phase. Can be done now.

## Resolution

(pending)
