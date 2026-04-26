---
title: Mistakes — Recurring Errors
type: journal-mistakes
updated: 2026-04-25
status: active
library_source: data/all_trades_dataset.csv (3300 trades)
---

# Mistakes — Recurring Errors Across Trades

The dataset labels recurring error categories via `outcome` and `exit_diagnosis`. This page
is the rollup: what kind of mistake, how often it appears, what the mechanical signature
looks like, and what remedy is queued.

**Append-only per-incident log at the bottom.** Top counts are regenerated from the CSV.

---

## Recurring error taxonomy (from labelled CSV columns)

### 1. Exit fires before the move completes — `premature_exit`

- **Count:** 1,280 (38.8% of library)
- **Strategies affected:** 14 of 15
- **Mechanical signature:** `mfe_pct − profit_ratio` is large and positive on a winner, or
  the stop triggers after a brief favourable excursion that was never captured.
- **Queued remedy:** trailing stop; partial take + runner; wider exit threshold.
- **Pattern page:** [[Patterns/premature-exit|Premature Exit]]

### 2. Realised PnL well below MFE on a winner that kept running — `missed_continuation`

- **Count:** 524 as outcome, 326 as exit-diagnosis, ≈688 as union of unique trades
- **Strategies affected:** 14 of 15
- **Mechanical signature:** winner exits early AND post-exit price continues in the
  favourable direction. A subtype of premature_exit with continuation confirmed.
- **Queued remedy:** partial + runner (the most directly targeted remedy); regime-aware exit.
- **Pattern page:** [[Patterns/missed-continuation|Missed Continuation]]

### 3. Stop triggers quickly after entry — `fast_loss`

- **Count:** 1,074 (32.5% of library — **the single largest outcome bucket**)
- **Mechanical signature:** MAE reaches stop within a short duration; MFE minimal.
- **Interpretation:** often the stop-loss rule working as designed — the mistake is the
  **entry** being taken in conditions that produced rapid adverse excursion, not the exit
  closing the trade.
- **Queued remedy:** entry filter (regime, volatility, volume conditions); wider stop
  with smaller position size.

### 4. Gradual drawdown without a sharp adverse move — `slow_loss`

- **Count:** 565 (17.1% of library)
- **Mechanical signature:** MAE drifts down over long duration without ever hitting the stop;
  trade closes negative via exit-signal rather than stop-loss.
- **Interpretation:** the adverse excursion never quite tripped the stop but also never
  reversed into a winner — the position bled.
- **Queued remedy:** time-based exit; adverse-excursion-based exit ("if MAE > X% and duration
  > Y bars, exit").

### 5. Entry placement caused the loss — `poor_entry`

- **Count:** 668 (20.2% of library, as exit-diagnosis); 189 as the outcome label
  `bad_entry_good_idea`
- **Mechanical signature:** MAE dominates MFE from the start; the thesis was viable but the
  entry timing left no room.
- **Queued remedy:** entry filter tightening; delayed entry with confirmation.

### 6. Trade had no signal and should not have been taken — `noise_trade`

- **Count:** 561 (17.0% of library)
- **Mechanical signature:** small MFE, small MAE, small realised PnL; the trade went nowhere.
- **Interpretation:** signal fired in a non-tradeable state. The 140 `scratch` outcome
  trades overlap with this category.
- **Queued remedy:** signal threshold raising; exclude low-MFE regimes.

### 7. Stop rule didn't contain the adverse excursion — `stop_loss_failure`

- **Count:** 129 (3.9% of library)
- **Mechanical signature:** MAE exceeds the configured stop-loss threshold; could be slippage,
  gap, or a stop that was re-set unfavourably by the strategy.
- **Queued remedy:** stop-placement audit; verify stop-on-exchange vs internal stop behaviour.

---

## Process mistakes (mine, reasoning-level — not CSV-labelled)

These are recurring errors in how I think about the data, not errors the data itself labels.

- **Overweighting small samples.** The Coint strategy (n=8, +54%) has been quoted as a
  canonical example across multiple pages. The sample size does not support the claim that
  it is a validated strategy. It's an interesting hypothesis; it is not evidence.
- **Confusing outcome labels with exit-diagnosis labels.** `missed_continuation` appears in
  both column types with overlapping-but-distinct populations. Treating them as identical
  inflates the perceived evidence for that concept.
- **Counting without denominators.** YujiVWAPMeanReversionStrategy has a low
  missed_continuation rate not because its exits are efficient but because its win rate is
  1.8% — almost no winners to miss continuation on. Always check the denominator.
- **Threshold conflation.** The "% premature ≥ 45%" threshold (8/15) is not the same as the
  `early-exit` diagnostic flag (10/15). Different thresholds, different populations.

---

## Per-incident log (append-only)

### [2026-04-25] Inception

- First log entry. Taxonomy above populated from the CSV. Per-incident log begins below
  empty — future entries should record specific trades or reasoning moments where a new
  instance of one of the above categories was recognised.

<!-- Add new entries under here in reverse chronological order.
     Each entry should include: date, category, trade reference (strategy + trade_NNNN),
     mechanical explanation using CSV fields only, lesson. -->

---

## Linked pages

- [[master|Training Journal master]]
- [[Daily/2026-04-25|Today's daily log]]
- [[Patterns/premature-exit|Pattern: Premature Exit]]
- [[Patterns/missed-continuation|Pattern: Missed Continuation]]
- [[Patterns/low-mfe-capture|Pattern: Low MFE Capture]]
- [[../wiki/synthesis/cross-strategy-trade-library|Cross-Strategy Trade Library]]
