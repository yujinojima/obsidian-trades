---
title: "Research — StrategyV2 (RSI Mean-Reversion + EMA Cross + Volume Capitulation)"
type: research-prim
updated: 2026-04-25
status: active
parent_strategy: YujiStrategyV2
force_exit_refine: false
---

# StrategyV2 — Cross-Domain Interpretation

Interpretation layer only. The strategy file explicitly documents its lineage: built on
YujiStrategy (V1) with three added entry signals (EMA crossover from MultiSignal,
volume-spike capitulation from ExtinctionBurst) and widened exits. Archetype:
`weak_entry_strong_exit` (avg MFE 2.18%, MFE capture 67.95%, 77% WR, -106.56% cumulative).

## 1. Trading Definition

- 1h timeframe
- Three entry conditions (OR'd):
  1. **RSI mean-reversion** (V1 base signal) — oversold RSI in non-choppy regime
  2. **EMA crossover** (inherited from MultiSignal) — trend-start signal
  3. **Volume spike + extreme RSI** (inherited from ExtinctionBurst) — capitulation entry
- Wider stop (-7%) and trailing stop (1% activation at 2.5% offset)
- ADX filter to avoid choppy markets
- Exits via ROI / trailing / exit_signal

## 2. Behavioural Interpretation

- **RSI mean-reversion** leans on **short-horizon over-reaction** (De Bondt & Thaler 1985):
  extreme recent price moves over-correct then revert.
- **EMA crossover** leans on **under-reaction to information** (Hong & Stein 1999) — the
  same rationale as [[trendrider|TrendRider]] but with a less selective regime filter.
- **Volume capitulation** leans on **panic selling** (Shleifer & Summers 1990): forced
  liquidations produce price dislocation that reverses once capitulation flow exhausts.
- **Mixed-signal design** is itself a behavioural artefact: the strategy's own notes say it
  was rebuilt from "lessons from 8 strategy backtests." It's an ensemble where each
  component addresses a different regime — which means the strategy's expectancy inherits
  the **average** over regimes, not the best.

## 3. Quant / Physics Interpretation

- **RSI(14)** is a bounded oscillator in [0, 100] whose distribution is approximately
  symmetric around 50 in a ranging regime and skews to one end in a trending regime. As a
  stationary indicator it produces a reliable signal only when the underlying return series
  is itself stationary.
- **EMA crossover** is the discrete equivalent of a zero-crossing of the first derivative
  of a low-pass-filtered price series. Its signal-to-noise improves with smoothing but
  latency grows proportionally.
- **Volume-z-score + RSI-extreme** is a compound condition whose joint probability in random
  data is low — the signal has a strong **selection effect**: few firings, and when it
  fires it's usually a real dislocation. But "few firings" means expectancy is dominated by
  outlier trades with poor statistical power.
- **Asymmetric payoff signature.** 77% WR × avg -0.30% realised = implies individual losses
  are materially larger than individual wins (average loser ≈ 3–4× average winner). This is
  the hallmark of a strategy that clips winners (wide trailing, ROI target) while letting
  losers drift to stop.

## 4. Failure Modes

- **Three-signal inconsistency.** RSI mean-reversion and EMA crossover have opposite regime
  preferences: one wants range, the other wants trend. Firing either without a regime
  arbiter produces trades that are correct for the wrong regime.
- **ADX filter is too permissive.** The strategy's archetype classification places it in
  `weak_entry_strong_exit` — the exits are doing their job but the entries find too-small
  MFE. This is consistent with entries firing in marginal regimes the ADX gate allows.
- **Fat-tailed loss distribution.** Slow_loss count (25) and cumulative -106% despite 77% WR
  suggests infrequent large losers dominate realised PnL. Classical over-fit-to-WR pathology.
- **Signal overlap with other Yuji strategies.** On the same bar, StrategyV2 and V3 have
  been observed entering the same trade idea on the same pair — see Missed Continuation
  section examples of Fluid trade_0058 and V3 trade_0055 both hitting XRP at the same MFE.
  StrategyV2 likely has correlated trades; portfolio sizing must account for this.

## 5. Implication for Strategy Design

- **Entry:** the three sub-signals should not be OR'd. Either (a) gate each with a
  regime-specific filter (RSI-mean-rev only in range, EMA cross only in trend,
  volume-capitulation only on high-vol days) or (b) remove one. The ensemble as structured
  averages over incompatible regimes.
- **Exit:** capture ratio 67.95% is above the archetype threshold — exit is not the lever
  here. Do NOT run exit-redesign experiments on this strategy first; it is blocked by the
  enforcement rule in [[../../Training Journal/Control Signals#Active Instructions]].
- **Risk:** 77% WR is a trap statistic when avg loser > avg winner. Compute and report
  expectancy (WR × avg_win − (1−WR) × avg_loss) rather than WR alone.
- **Sizing:** reduce size proportional to the loss-size tail. Kelly fraction for this strategy
  would be ≈ 0 or negative given -0.30% avg and asymmetric payoff.
- **Deprecation candidate:** the strategy's own lineage says it incorporated learnings from
  8 backtests. If the ensemble approach has not converged after V1→V2 iterations, the
  hypothesis that "adding signals improves robustness" should itself be tested before V3.

## Execution Translation

### Entry Implication

- **Do NOT OR the three sub-signals.** Each one has an opposite-regime twin inside the same strategy. Either (a) replace the OR with per-signal regime gates (RSI-MR firing only in low-ADX/ranging regime, EMA-cross firing only in high-ADX/trending regime, volume-capitulation firing only on high-vol days) or (b) split into three strategies with independent entry gates and let a portfolio layer combine them.
- **Add expectancy-based pruning.** Compute per-sub-signal win rate × avg_win − (1−WR) × avg_loss. Disable any sub-signal whose expectancy is negative, even if its WR is high.
- **The current ADX filter is too permissive** — tighten the regime gate per sub-signal as above.

### Exit Implication

- **Do NOT run exit-redesign experiments on this prim.** Current MFE capture = 67.95%, above the archetype threshold. The exit is not the failure mode. Running trailing-stop, partial-TP, or time-stop variants here wastes cycles and produces misleading A/B comparisons because the baseline exit is already efficient.
- **`missed_continuation` contribution (87 trades) is the second-largest in the library**, but on this prim it is a **symptom of low avg MFE (2.18%)**, not of exit inefficiency. Fixing the exit cannot raise MFE; only entry redesign can.
- **Enforcement Rule in [[../../Training Journal/Control Signals#Active Instructions]]** currently blocks entry-side work until exit fixes are exhausted elsewhere. Holding that line means this prim is **deferred**, not deprioritised permanently.
- **`premature_exit` rate (45.2%)** on this prim is driven by the strategy's wide trailing + ADX-exit combination firing on marginal regime reversals. Exits fire "correctly" given entries, but entries were marginal.

### Risk / Positioning Implication

- **Stop using WR as the headline metric.** Report expectancy per trade and expectancy × frequency per period. WR = 77% with expectancy = negative is a well-known trap.
- **Kelly-implied size ≤ 0** given current expectancy. Any size > 0 has negative long-run growth rate. Run paper-mode only until entry redesign moves expectancy positive.
- **Do not compound losses** across consecutive sub-signal firings — if RSI-MR fires and loses, block the next EMA-cross fire on the same pair for K bars to prevent sub-signal correlation from amplifying drawdown.

### What this means for current experiments

- [[../../Training Journal/Experiments/trailing-stop-vs-coint]] — **DOES NOT APPLY.** Exit rule is not this prim's failure mode; a trailing stop experiment here would produce a misleading comparison. Direct conflict with the enforcement rule.
- [[../../Training Journal/Experiments/partial-tp-runner]] — **DOES NOT APPLY.** Same reason as above. The 67.95% MFE capture means partial-TP-runner would at best be a wash and at worst regress by adding friction. Deferred indefinitely.
- [[../../Training Journal/Experiments/time-based-exit]] — **DOES NOT APPLY** for the same reason. Time-stop cannot raise avg MFE, which is the actual lever.
- **Implied new experiment (not yet queued):** per-sub-signal regime-gated entry redesign. This is the correct experiment for this prim but is blocked by the enforcement rule until the exit-side experiments on Coint / Scalper / MoneyMaker complete.

## See also

- Strategy file: `freqtrade/user_data/strategies/YujiStrategyV2.py`
- Library section: [[../../wiki/synthesis/cross-strategy-trade-library|Cross-Strategy Trade Library]]
- Patterns: [[../../Training Journal/Patterns/low-mfe-capture]] (weak_entry_strong_exit archetype)
- Control: [[../../Training Journal/Control Signals#Active Instructions]] (entry-side work is blocked)
