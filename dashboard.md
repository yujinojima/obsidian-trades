---
title: Dashboard
type: dashboard
updated: 2026-04-25
---

# Operational Dashboard

- Pages in wiki: **36**
- Orphans: **0**
- Broken links: **0**
- Missing frontmatter: **0**
- Stale pages (>30d): **0**

## System-Level Diagnosis

Primary source: `data/all_trades_dataset.csv` (3,300 trades, 15 strategies, 2022-05-02 → 2026-04-20).
Prior source: `reports/strategy_diagnosis.md` (batch `batch-20260424T123546Z`).

- **Dominant failure mode:** exit inefficiency.
- **Full-library trades:** **3,300** across 15 strategies.
- **`premature_exit` diagnosis trades:** **1,280** (38.8% of library) — most common diagnosis.
- **`missed_continuation` outcome trades:** **524** (15.9%).
- **`fast_loss` outcome trades:** **1,074** (32.5%) — single largest outcome bucket.
- **`efficient_exit` diagnosis trades:** **336** (10.2%) — the positive counter-signal.
- **Strategies flagged `early-exit`:** 10/15 (66.7%).
- **Strategies with premature_exit ≥ 45%:** 8/15 (53.3%).
- **Robust strategies (strong_entry_strong_exit archetype):** **0**.
- **Mean MFE capture across strategies with measurable winners:** ≈58%.
- Representative trade samples: [[wiki/synthesis/cross-strategy-trade-library|Cross-Strategy Trade Library]]
- Interpretation: [[wiki/synthesis/current-trading-thesis#Cross-Strategy Findings|synthesis § Cross-Strategy Findings]]

## Research Layer

- [[Research/README|Research index]]
- Prims: [[Research/Prims/cointegration|cointegration]] · [[Research/Prims/trendrider|trendrider]] · [[Research/Prims/scalper|scalper]] · [[Research/Prims/strategyv2|strategyv2]] · [[Research/Prims/vwap-mean-reversion|vwap-mean-reversion]]

## Training Journal

- [[Training Journal/master|Training Journal — Master]]
- [[Training Journal/Control Signals|Control Signals]] — Ralph-facing instructions
- Daily logs: `Training Journal/Daily/`
- Pattern pages: [[Training Journal/Patterns/premature-exit|premature-exit]] · [[Training Journal/Patterns/missed-continuation|missed-continuation]] · [[Training Journal/Patterns/low-mfe-capture|low-mfe-capture]]
- Experiments (queued): [[Training Journal/Experiments/trailing-stop-vs-coint|trailing-stop-vs-coint]] · [[Training Journal/Experiments/partial-tp-runner|partial-tp-runner]] · [[Training Journal/Experiments/time-based-exit|time-based-exit]]
- Recurring mistakes: [[Training Journal/Mistakes|Mistakes.md]]

## Latest synthesis

- [[wiki/synthesis/current-trading-thesis|Current trading thesis]]

## Open questions

- [[wiki/questions/README|Open Research Questions]] — _active_
- [[wiki/questions/coint-strategy-portability|Does the cointegration strategy port off ETH/USDT?]] — _open_
- [[wiki/questions/missed-continuation-regime-clustering|Do missed-continuation trades cluster by regime?]] — _open_
- [[wiki/questions/trailing-stop-vs-coint-z-reverted|Trailing Stop vs coint_z_reverted]] — _open_

## Strategies

- [[wiki/strategies/YujiCointegrationResidualReversionStrategy|YujiCointegrationResidualReversionStrategy]] — trades: 8, win rate: 0.75

See [[reports/wiki_lint_report|lint report]] for full detail.
