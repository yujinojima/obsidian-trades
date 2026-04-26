---
title: "Polymarket Experiment — news_event_no_trade_filter"
type: polymarket-experiment
updated: 2026-04-25
status: active
phase: 1
avoid_flags_total: 4
---

# Experiment — news_event_no_trade_filter

Inverse strategy. This is **not a signal generator** — it produces AVOID flags that remove
markets from the tradeable set for every other strategy.

## Hypothesis

Markets that are **news-sensitive close to resolution** have outcome realisations dominated
by single headlines, not orderbook dynamics. Attempting spread_capture / momentum_reaction /
mean_reversion on them is analogous to trading through a known earnings announcement —
execution edge is swamped by idiosyncratic jump risk.

## Trigger conditions (fire AVOID)

A market is flagged AVOID if ANY of:

- `hours_to_close < 7 × 24` AND market category contains a news-driven keyword
  (`politic`, `geopol`, `election`, `war`, `conflict`)
- `hours_to_close < 7 × 24` (generic endgame cutoff, regardless of category)
- `|one_day_pct| > 0.10` (probability already moving > 10pp in 24h → active news flow)

## Current status (2026-04-25)

**4 AVOID flags** on today's scan:

| Market | hours_to_close | Reason |
|---|---:|---|
| strait-of-hormuz-traffic-returns-to-normal-by-april-30 | 123.8 | < 7 days |
| will-bitcoin-dip-to-65k-in-april-2026 | 151.8 | < 7 days |
| kharg-island-no-longer-under-iranian-control-by-april-30 | 147.7 | < 7 days |
| will-bitcoin-reach-85k-in-april-2026 | 151.8 | < 7 days |

All four are within 7 days of resolution. Geopolitics (Hormuz, Kharg) and BTC price
brackets — both highly news-sensitive. Filter worked as designed.

## Outcome criteria

This strategy's "outcome" is **retroactive**: after a flagged market resolves, did the
final-N-days price path resemble jump-dominated (news-driven) or drift-dominated behaviour?
If mostly drift, the filter was too conservative (flagged a tradeable market). If mostly
jumps, the filter was correct.

Simple post-hoc check: plot realised MFE/MAE on the final-7-day window for flagged vs
unflagged markets of similar liquidity. If flagged markets have 2×+ MAE than unflagged, the
filter is earning its keep.

## Current assessment

The four AVOID flags match independent common sense — these are all binary geopolitical /
BTC-spot markets that could resolve abruptly on a single event. No false positives on this
batch.

**Unknown:** whether the filter has FALSE NEGATIVES (markets it should have flagged but
didn't). Detecting those requires tracking unflagged markets and looking for ex-post
jump-dominated paths.

## Next adjustment

- **Category tagging is weak.** `category: "(none)"` on most Polymarket markets — Gamma
  either doesn't populate it or uses a taxonomy this filter doesn't recognise. Need to
  switch to **slug-keyword matching** (e.g. `iran`, `election`, `war`, `btc`, `nuclear`)
  to catch news-sensitive markets that lack a category tag.
- **Add an orderbook-imbalance trigger.** A sudden widening of the spread to > 3× its
  7-day median is a real-time indicator of news flow hitting the market.

## Linked

- [[../daily/2026-04-25|Today's daily log (4 AVOID flags)]]
- [[../README|Polymarket journal index]]
- Source: `polymarket-bot/scripts/polymarket_strategy_scan.py` → `score_news_event_no_trade_filter()`
