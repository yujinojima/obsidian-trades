---
title: "Research — VWAP Deviation Mean Reversion"
type: research-prim
updated: 2026-04-25
status: active
registry_name: vwap-deviation-mean-reversion
parent_strategy: YujiVWAPMeanReversionStrategy
force_exit_refine: false
selection_note: "5th slot — force_exit_refine=True is set on only one registry entry (cointegration). This is the highest-impact additional force-refine candidate by MFE capture (37.5%, lowest in library) and volume (920 trades, largest in library)."
---

# VWAP Mean Reversion — Cross-Domain Interpretation

Interpretation layer only. Registry entry `vwap-deviation-mean-reversion` (sophisticated tier),
matched strategy `YujiVWAPMeanReversionStrategy`. Library stats: 920 trades · 1.85% WR ·
37.5% MFE capture · avg MFE 0.38% · cumulative -357.78%. The **worst** capture and **worst**
cumulative PnL in the 15-strategy library.

## 1. Trading Definition

Volume-Weighted Average Price deviation as a mean-reversion signal. Entries fire when price
deviates above or below VWAP by more than a threshold — short stretched-above, long
stretched-below — with the hypothesis that price will revert toward the day's VWAP. Exits
at VWAP cross or on reversion-complete signal.

## 2. Behavioural Interpretation

- **VWAP as the institutional reference price.** Large execution desks benchmark their fills
  against VWAP (Berkowitz, Logue, Noser 1988). Algorithms deliberately execute *toward* VWAP
  to minimise reported slippage, which creates mechanical reversion flow during the day.
- **Price-anchoring** to the session's running mean. Discretionary participants treat VWAP
  as the "fair price" of the session and trade against stretches — self-fulfilling while the
  mean-reversion interpretation holds.
- **End-of-day closing flows** amplify reversion if institutional algos need to hit VWAP by
  close, producing a characteristic convergence in the final hour.

## 3. Quant / Physics Interpretation

- **VWAP as expectation estimator.** VWAP_t = Σ(p_i × v_i) / Σ v_i over session = the
  volume-weighted sample mean of executed prices. Deviations are interpretable as
  innovations relative to this running estimator.
- **Price-to-VWAP ratio behaves approximately as an OU process on intraday scale** under
  stationary intraday conditions — the same mathematical framing as [[cointegration|cointegration]]
  but with a single-asset, single-session scope.
- **Regime-dependent stationarity.** Intraday returns are approximately mean-reverting within
  a ranging session but become directional (random-walk or trending) within a news-driven or
  news-absorbing session. The signal's validity is entirely conditional on regime.
- **Cross-asset parallel:** closely related to the capital asset "excess-return-to-benchmark"
  framing — a long/short position against a day-specific benchmark.

## 4. Failure Modes

- **Trending-day regime.** On a directional day, VWAP drifts in the direction of the trend
  faster than the strategy's exit threshold triggers. Entries stretched against the trend
  see the stretch widen indefinitely. This is the textbook VWAP-reversion failure and is
  consistent with the library's 1.85% WR — almost all trades are wrong because the mean
  itself is moving.
- **End-of-session effect inversion.** If institutional flow is already long-VWAP vs
  short-VWAP imbalanced, end-of-session rebalancing can be *with* the deviation, not
  against it — the assumed reversion flow flips.
- **Stop-cluster dynamics.** Tight stops near VWAP invite sweeps similar to
  [[scalper|Scalper]]'s failure mode — band extremities are predictable liquidity pools.
- **Scale mismatch.** 4 years of trade history at ~920 trades implies this strategy fires
  ~0.6 times per day — consistent with a session-scope signal that should be higher-frequency
  if VWAP truly mean-reverts in the expected way. The low firing frequency suggests the
  entry threshold is very selective, yet WR is still 1.85% — a selective signal with
  near-zero hit rate is a bad signal, full stop.

## 5. Implication for Strategy Design

- **Entry:** regime filter is the single largest lever. A trending-day filter (intraday ADX,
  opening-range break detection, or an intraday Hurst estimator) should gate every entry.
  The current implementation clearly does not have this gate working.
- **Exit:** 37.5% MFE capture is the **worst in the library** — the exit rule is fighting
  the (rare) winners. But before redesigning the exit, the entry filter must be fixed;
  otherwise the exit redesign is polishing a negative-edge signal.
- **Risk:** 1.85% WR on 920 trades is a decisive statistical rejection of the signal *as
  currently implemented*. The strategy is a **candidate for deprecation**, not refinement,
  unless an entry-filter change moves WR materially above 30%.
- **Sequencing for Ralph:** exit-refinement experiments on this strategy (e.g., the
  partial-TP-runner design from [[../../Training Journal/Experiments/partial-tp-runner]])
  will produce noise rather than learning. Queue an **entry-filter experiment** first —
  specifically, add an intraday-trend gate and re-run the backtest to see if WR crosses
  into the tradeable range. If it doesn't, deprecate.

## Execution Translation

### Entry Implication

- **Add intraday-trend-regime gate** as a hard entry precondition. Candidates: (a) intraday ADX > threshold → block, (b) opening-range break detection → block, (c) first-hour-of-session range expansion → block. Without this gate, every entry against a directional session is a structural loss.
- **Raise the deviation threshold** for what counts as "stretched" so entries fire less often but require a larger dislocation to trigger. A selective signal whose WR is still 1.85% is not being selective in the right way — the selection must move from magnitude to regime.
- **Suspend on end-of-session periods** where closing-auction flow can invert the normal reversion-to-VWAP dynamic.

### Exit Implication

- **`premature_exit` rate on this prim (23.3%, 214 trades) is deceptively low** — lower than the library average of 38.8% — **only because the win rate is 1.85%**. A prim cannot register premature exits on trades that never become favourable; the denominator effect masks the exit quality.
- **`missed_continuation` contribution (0.98%)** looks low only because the win rate is 1.85% — there are almost no winners to miss continuation on. **Do not read this as evidence the exit is working.**
- **MFE capture = 37.5% (worst in the library)** — the exit rule does cut winners short on the rare occasions they exist, but improving exit capture on a 1.85%-WR signal cannot rescue expectancy. Raising capture from 37.5% to 100% on 17 winners per 920 trades is mathematically incapable of offsetting the 903 losers.
- **Fix-ordering is non-negotiable:** entry filter FIRST, exit redesign LAST. Running exit experiments before the entry gate is fixed produces noise and wastes experiment cycles.
- **If WR does not cross 30% after entry-filter fix**, the prim is a **deprecation candidate** — no exit redesign will save a 1.85%-WR signal.

### Risk / Positioning Implication

- **Paper-mode only until entry fix.** Kelly fraction at 1.85% WR × unfavourable payoff is negative by any measure. Live sizing is not defensible on the current evidence.
- **Cap maximum drawdown contribution** from this prim to zero in any portfolio construction until WR crosses the tradeable threshold.
- **Frequency reduction** is the main lever. Current firing rate (~0.6/day over 4 years) is already moderate, but if the entry gate tightens further, expect ≤ 0.1-0.2/day — acceptable.

### What this means for current experiments

- [[../../Training Journal/Experiments/trailing-stop-vs-coint]] — **DOES NOT APPLY.** Different strategy; and the failure mode here is entry, not exit.
- [[../../Training Journal/Experiments/partial-tp-runner]] — **DOES NOT APPLY** on this prim in the current state. Partial take + runner on a 1.85%-WR signal still loses — the three-way split of entries into (win-taken-partial, win-continued-by-runner, loss-at-stop) is still dominated by the 98% losing bucket. Queue only after entry-filter fix moves WR > 30%.
- [[../../Training Journal/Experiments/time-based-exit]] — **DOES NOT APPLY.** A time-stop on a strategy with 98% losers compresses the loss distribution slightly but does not fix the sign of expectancy.
- **Implied new experiment (not yet queued):** intraday-trend-regime-gated entry. This is the correct and only valid next experiment on this prim. It should be proposed to [[../../Training Journal/Control Signals]] as a priority-HIGH item once the first round of exit-refinement completes elsewhere, OR immediately as the entry-gate exception to the enforcement rule (the enforcement rule blocks *new entry primitives*, not entry-filter fixes on existing prims).

## See also

- Registry: `data/primitive_scores.csv` → `vwap-deviation-mean-reversion` (tier: sophisticated,
  force_exit_refine: False, final_score: 0.0967, score_bucket: WEAK)
- Strategy file: `freqtrade/user_data/strategies/YujiVWAPMeanReversionStrategy.py`
- Library section: [[../../wiki/synthesis/cross-strategy-trade-library|Cross-Strategy Trade Library]]
- Sister mean-reversion prims: [[cointegration]] · [[scalper]] · [[strategyv2]]
