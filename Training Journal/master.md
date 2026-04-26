---
title: Training Journal — Master
type: journal-master
updated: 2026-04-25
status: active
---

# Training Journal — Master

The learning layer sitting on top of the trade library. The **library** (`wiki/`) is the
reference record — what happened and how it's labelled. The **journal** is the practitioner's
log — what I noticed, what I got wrong, what I'm going to try next.

- **Primary data source:** `data/all_trades_dataset.csv` (3,300 trades, 15 strategies,
  2022-05-02 → 2026-04-20)
- **Reference layer:** [[../wiki/synthesis/current-trading-thesis|Current trading thesis]],
  [[../wiki/synthesis/cross-strategy-trade-library|Cross-Strategy Trade Library]]
- **Dashboard:** [[../dashboard|Vault dashboard]]

---

## System state (as of 2026-04-25)

- **Total trades observed:** 3,300 across 15 strategies
- **Profitable strategies in full library:** 3 of 15 (Coint +54.4%, TrendRider +9.1%, Fluid +1.7%)
- **Robust strategies (strong_entry_strong_exit archetype):** **0**
- **Net library PnL sum across all strategies:** **-1,022%** (losing by a wide margin)
- **Top failure mode:** exit inefficiency — 1,280 premature_exit trades (38.8% of the library)
- **Second failure mode:** entry quality — 668 poor_entry trades (20.2%) plus 561 noise_trade (17.0%)
  together account for more than a third of all trades
- **Positive counter-signal:** efficient_exit diagnoses = 336 trades (10.2%). The exit logic is
  working on ~1 in 10 trades; the rest have a diagnosable exit problem.
- **Pair concentration:** BTC/USDT (1,231) + ETH/USDT (1,177) = 73% of trades. 4 other pairs
  contribute the remaining 27%.

## Key stats (frozen snapshot — regenerate by re-reading the CSV)

| Metric | Value | Source |
|---|---:|---|
| Total trades | 3,300 | CSV |
| premature_exit trades | 1,280 | CSV exit_diagnosis |
| missed_continuation outcome | 524 | CSV outcome |
| missed_continuation diagnosis | 326 | CSV exit_diagnosis |
| fast_loss | 1,074 | CSV outcome |
| slow_loss | 565 | CSV outcome |
| efficient_exit | 336 | CSV exit_diagnosis |
| poor_entry | 668 | CSV exit_diagnosis |
| noise_trade | 561 | CSV exit_diagnosis |
| stop_loss_failure | 129 | CSV exit_diagnosis |
| Mean MFE capture (strategies w/ winners) | ≈58% | reports/strategy_diagnosis.md |

## System Bottleneck

- **Primary issue:** exit inefficiency.
- **Evidence:**
  - `premature_exit` diagnosis ≈ **38.8%** of library (1,280 / 3,300 trades)
  - Mean MFE capture across strategies with measurable winners ≈ **58%** (typical strategy
    leaves ~42% of the favourable move on the table)
  - 13 of 15 strategies classified as `strong_entry_weak_exit` or `fully_inefficient` —
    both archetypes have exit quality as the first lever
  - 0 strategies classified as `strong_entry_strong_exit` (no robust strategies in the batch)
- **Second issue (subset):** missed_continuation — 524 outcome + 326 diagnosis — a narrower
  manifestation of the same bottleneck where post-exit price continues in the winning direction.

## Enforcement Rule

- **All new work must prioritise exit refinement over entry creation.**
- Creating a new entry-side primitive requires explicit justification and Director approval.
- See [[Control Signals#Active Instructions]] for the operational form of this rule that
  Ralph consumes.

## Current hypothesis

> **Exits are the primary limiting factor across the entire Yuji strategy family, not entries.**
> 13/15 strategies sit in archetypes (strong_entry_weak_exit, fully_inefficient) where the
> exit rule is part of the failure mode. Replacing fixed exits (ROI, signal-based, z-reversion)
> with variants (trailing stop, partial + runner, time-stop) should move the most expectancy
> per unit of engineering effort.

Secondary hypothesis (from [[../wiki/synthesis/current-trading-thesis#Low-confidence speculations|current-trading-thesis]]):

> The cointegration strategy's reversion-to-zero exit under-captures because the *residual*
> reverts while the *underlying pair* keeps trending. The right exit may not be "exit at z=0"
> but "exit at z=0 then trail the pair" or "hold until z-cross to opposite extreme."

## Active experiments

| # | Experiment | Status | Blocking |
|---:|---|---|---|
| 1 | Trailing stop vs `coint_z_reverted` on the same Coint entry set | open | nothing — can run |
| 2 | Partial take-profit + runner (50% at 1R, trail remainder) applied to top-3 highest-count strategies (Scalper, V2, MoneyMaker) | open | nothing — can run |
| 3 | Missed-continuation regime clustering — do they share a state? | blocked | Phase 1 market-state labeller |
| 4 | Cointegration strategy portability off ETH/USDT | open | nothing — can run |
| 5 | Entry-filter redesign for weak_entry_strong_exit pair (Strategy, StrategyV2) | open | nothing — can run |

Full list: [[../wiki/questions/README|wiki/questions/]].

## Pattern pages

- [[Patterns/premature-exit|Premature Exit]] — recognition, remedy, examples
- [[Patterns/missed-continuation|Missed Continuation]] — recognition, remedy, examples
- [[Patterns/low-mfe-capture|Low MFE Capture]] — strategy-level signature, not per-trade

## Daily logs

- [[Daily/2026-04-25|2026-04-25]] — journal inception, ingested Ben's 3,300-trade library

## Recurring mistakes

- [[Mistakes|Mistakes.md]]

## Polymarket (prediction markets)

- [[Polymarket/README|Polymarket journal index]] — phase-1 paper scan active
- [[Polymarket/daily/2026-04-25|Today's Polymarket session]] — 20 markets scanned, 18 mean-reversion paper trades, 4 news-event AVOID flags
- Strategy experiments: [[Polymarket/experiments/spread-capture|spread_capture]] · [[Polymarket/experiments/momentum-reaction|momentum_reaction]] · [[Polymarket/experiments/mean-reversion|mean_reversion]] · [[Polymarket/experiments/news-event-no-trade-filter|news_event_no_trade_filter]] · [[Polymarket/experiments/endgame-decay|endgame_decay]]

## Control signals

- [[Control Signals]] — Ralph-facing instruction source (global priority, active instructions, focus primitives, machine-readable payload)

## Experiments

- [[Experiments/trailing-stop-vs-coint]] — queued · HIGH
- [[Experiments/partial-tp-runner]] — queued · HIGH
- [[Experiments/time-based-exit]] — queued · MEDIUM

---

## Maintenance

- This file is the human-facing anchor. Update the "System state" and "Current hypothesis"
  sections whenever the underlying data changes.
- Daily logs are the append-only record; one file per day, no overwrites.
- Pattern pages are updated when new evidence arrives — never reset, always extended.
- Mistakes.md is append-only on the per-incident log; aggregate counts at the top are
  regenerated.
