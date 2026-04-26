---
title: Polymarket — Strategy Selection Journal
type: polymarket-journal-index
updated: 2026-04-25
status: active
phase: 1 (paper-only)
---

# Polymarket Strategy Selection & Micro-Test Journal

Goal: let the bot decide which Polymarket strategy deserves capital via **tiny controlled
tests**, not full allocation. Paper-first; live-micro only after paper shows positive EV.

## Data flow

```
Gamma API  →  scripts/polymarket_strategy_scan.py  →  CSV + market pages + daily log
                  (read-only)                            └─ this journal
                                                         └─ reports/polymarket_strategy_scores.csv
```

- **Scanner:** `polymarket-bot/scripts/polymarket_strategy_scan.py`
- **CSV output:** `polymarket-bot/reports/polymarket_strategy_scores.csv` (one row per (market, strategy))
- **Paper trade pages:** `markets/<slug>.md` (one per scanned market, auto-generated)
- **Daily logs:** `daily/YYYY-MM-DD.md` (human-authored session record)
- **Experiment pages:** `experiments/<strategy>.md` (one per strategy hypothesis)

## Current phase

**Phase 1 — paper only, 20-market scan.**
No live orders. Results after each scan go to daily log; outcomes at 15m / 1h / 4h / close will
be added by a future monitor (not built this session).

**Phase 2 — live micro** (not yet unlocked):
- Live size $0.05–$0.25 per trade
- Daily max loss $2
- Max open exposure $5
- One live micro-position at a time
- No market orders, limit / post-only only

## Safety rules (hardcoded in the scanner)

- Skip if spread > $0.015
- Skip if liquidity < $10,000
- Skip if < 24h to resolution
- Skip if low-side price < $0.02 (dust)
- `PAPER_MODE=true` default; `LIVE_MODE=true` requires `LIVE_MODE_CONFIRM=yes` env
- `DO_NOT_TRADE` list: markets flagged by `news_event_no_trade_filter`

## Strategies under evaluation

- [[experiments/spread-capture|spread_capture]] — tight-spread passive maker
- [[experiments/momentum-reaction|momentum_reaction]] — 24h move continuation
- [[experiments/mean-reversion|mean_reversion]] — near-extreme rerate bet
- [[experiments/news-event-no-trade-filter|news_event_no_trade_filter]] — inverse; only produces AVOID flags
- [[experiments/endgame-decay|endgame_decay]] — < 48h-to-close drift (paper-only per spec)

## Recent sessions

- [[daily/2026-04-25|2026-04-25 — first phase-1 scan]]

## Linked

- [[../master|Training Journal master]]
- [[../Control Signals]]
- [[../../Research/README|Research Layer]] (if cross-applicable analyses appear)
