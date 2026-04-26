---
title: "Research — Scalper (Bollinger + Stochastic RSI Mean Reversion, 15m)"
type: research-prim
updated: 2026-04-25
status: active
parent_strategy: YujiScalperStrategy
force_exit_refine: false
---

# Scalper — Cross-Domain Interpretation

Interpretation layer only. The strategy name is somewhat misleading: despite "scalper" it is
a **mean-reversion** strategy on 15m bars using Heikin Ashi smoothing, Bollinger Band %B,
and Stochastic RSI — not a microstructure scalper in the market-making or HFT sense. The
interpretation below treats it as a short-horizon mean-reversion prim.

## 1. Trading Definition

- 15m timeframe (explicitly no 4h informative data in the strategy file)
- Heikin Ashi candles for noise reduction
- Bollinger Band %B → entries on stretch below band (oversold mean-reversion)
- Stochastic RSI for timing precision
- Volume-weighted entry filter (only "real moves")
- Tight stoploss (-2.5%) + trailing stop
- Exit via `exit_signal` on mean-reversion target hit

## 2. Behavioural Interpretation

- **Short-horizon mean-reversion bias** (Jegadeesh 1990): at ≤ 1-week horizons, cross-sectional
  returns mean-revert. Intraday, this manifests as over-reaction corrections.
- **Liquidity-provision compensation.** The strategy is implicitly selling liquidity to
  participants who need immediacy at band extremes. The edge (if any) is the premium those
  participants pay to exit.
- **Gambler's fallacy** in the counter-party: many participants overweight the probability of
  continuation after a short run and exit into the band-stretch, providing the liquidity
  this strategy consumes.

## 3. Quant / Physics Interpretation

- **Bollinger %B ≈ z-score** relative to a rolling mean. %B = (price − lower band) / (upper − lower).
  Entries at %B < 0 are entries at more than N × σ below the rolling mean.
- **Short-horizon return distribution:** mean-reversion at ≤ 1-week lags is a documented
  anomaly (Jegadeesh 1990; Lo & MacKinlay 1988 on variance-ratio tests). Negative
  autocorrelation at daily-and-below scales.
- **Heikin Ashi** is a recursive smoothing of OHLC that dampens single-bar noise at the cost
  of signal latency — equivalent to a 2-bar low-pass filter on the raw candle sequence.
- **Stochastic RSI:** a normalisation of RSI to its own rolling range — a second-order
  oscillator indicator, reducing to a unit-variance signal on RSI's distribution.
- **Critical cost structure:** on 15m, a strategy trades ~4-8× as often as on 1h.
  Fees + spread per round-trip must be < realised edge per trade or expectancy is negative
  regardless of signal quality.

## 4. Failure Modes

- **Strong trend regimes.** Bollinger %B goes persistently extreme in a trending market;
  each "oversold" entry is met with further drawdown. The strategy's own comments acknowledge
  this: "Worst in: strong trends (use YujiTrendRider instead)."
- **Cost drag exceeds edge.** With a small avg MFE (0.76% in the library across 288 trades),
  the edge per trade is narrow. Fees (taker 0.1% × 2 = 0.2% round-trip) + spread are a
  material fraction of gross expectancy.
- **Late entries** relative to the turning point. Stochastic RSI and %B are both lagging
  indicators — when they signal, the reversion may be partly realised.
- **Stop-cluster raids.** Tight stops (-2.5%) cluster in predictable locations near the band.
  Informed flow can sweep the stops before the reversion, producing `fast_loss` outcomes
  (40 fast_loss trades in this strategy's library share).

## 5. Implication for Strategy Design

- **Entry:** regime filter is non-negotiable. Do not trade in trending regimes (the strategy's
  own notes agree). An ADX-low filter or Hurst < 0.5 estimator is the canonical gate.
- **Exit:** the strategy library shows 49.03% MFE capture and 34.4% premature_exit rate —
  the tight trailing stop is biting before the full reversion target. Candidates: (i) fixed
  target at mid-band with no trail, (ii) partial at 1R with remainder to mid-band.
  See [[../../Training Journal/Experiments/partial-tp-runner]].
- **Stop:** current -2.5% is structurally tight. Consider widening **and** reducing size to
  hold MAE-per-capital constant — reduces stop-cluster raid frequency without raising risk.
- **Sizing:** edge per trade must exceed 3× round-trip cost. At 0.2% fee round-trip, minimum
  viable edge ≈ 0.6% — the library's avg realised of -0.23% is net negative.
- **Framing:** do not treat as microstructure scalping; treat as short-horizon mean-reversion.
  The remedies are from the mean-reversion playbook, not the market-making one.

## Execution Translation

### Entry Implication

- **Trending-regime lockout is mandatory.** No entries when ADX > 25 or when Hurst estimator on the recent window is > 0.55. The strategy's own docstring agrees ("Worst in: strong trends") but the library shows this gate is not strictly enforced.
- **Raise the %B entry threshold** to farther-from-band. Later entries accept fewer firings but higher per-signal expectancy — trades less often but with edge per trade above the cost floor.
- **Require volume-weighted confirmation** (already present as filter) — do not relax it. Low-volume band stretches are the noise channel.

### Exit Implication

- **Current `premature_exit` rate = 34.4% (99 trades) with MFE capture = 49.03%** — the trailing stop is firing before the mean-reversion target is reached. The trailing stop is the proximate cause; the underlying issue is a mismatch between the strategy's signal horizon (mid-band cross) and its trailing-stop horizon (minor pullback).
- **Replace the trailing stop with a fixed mid-band target** on primary exit — if entry is at %B < 0 (below lower band), target is the mid-band (%B = 0.5). No trail. This converts trailing-driven `premature_exit` into signal-completion exits.
- **Alternative:** partial at 1R, remainder to mid-band. Locks in risk-reduction at 1R while letting the signal complete to its structural target. Directly addresses the 17.7% `missed_continuation` rate and raises MFE capture.
- **Do not layer a tighter trail** on top of either design — that's what produced the current premature_exit pattern.

### Risk / Positioning Implication

- **Raise minimum edge requirement.** Fees + spread round-trip ≈ 0.2% taker; min viable edge per trade ≈ 0.6%. Library avg realised = -0.23% means current design is below the cost floor — sizing cannot fix a negative-edge signal.
- **Widen stop (currently -2.5%) and reduce size proportionally** so MAE-per-capital is constant — reduces stop-cluster sweep frequency (40 `fast_loss` trades) without raising risk.
- **Lower trade frequency** by tightening the regime gate and entry threshold — targets 1/3 to 1/2 current firing rate. Expected improvement: edge per trade rises enough to cross the cost floor.

### What this means for current experiments

- [[../../Training Journal/Experiments/partial-tp-runner]] — **SUPPORTS DIRECTLY.** The partial-at-1R + remainder-to-mid-band variant is exactly the design this theory recommends. Highest-priority experiment for this prim.
- [[../../Training Journal/Experiments/trailing-stop-vs-coint]] — **DOES NOT APPLY DIRECTLY** (different strategy), but the underlying principle (replace fixed-target/trailing with a smarter exit condition) transfers. The Coint result informs design choices for this prim but is not a substitute experiment.
- [[../../Training Journal/Experiments/time-based-exit]] — **CONDITIONAL.** A median-winner time-stop on 15m is a short time-budget; could help by enforcing completion before noise dominates, but risks cutting off slower mean-reversions. Run only after partial-TP-runner to disentangle effects.

## See also

- Strategy file: `freqtrade/user_data/strategies/YujiScalperStrategy.py`
- Library section: [[../../wiki/synthesis/cross-strategy-trade-library|Cross-Strategy Trade Library]] (Losses + Premature Exits)
- Patterns: [[../../Training Journal/Patterns/missed-continuation]] · [[../../Training Journal/Patterns/low-mfe-capture]]
- Experiment: [[../../Training Journal/Experiments/partial-tp-runner]]
