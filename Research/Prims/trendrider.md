---
title: "Research — TrendRider (EMA Ribbon + ADX + MACD)"
type: research-prim
updated: 2026-04-25
status: active
parent_strategy: YujiTrendRiderStrategy
force_exit_refine: false
---

# TrendRider — Cross-Domain Interpretation

Interpretation layer only. Trading record lives at
[[../../wiki/synthesis/cross-strategy-trade-library|Cross-Strategy Trade Library]].
The strategy file lists its own signals verbatim — this page maps them to external concepts.

## 1. Trading Definition

Trend-following on 1h. Entries require EMA(8, 21, 50, 100) ribbon alignment + ADX > 25 (regime
filter) + MACD histogram momentum confirmation. Fixed stop below swing low — **explicit design
note in the strategy file**: "ATR trailing destroys edge (PF drops to 0.603, WR 28%). Fixed
stop below swing low is the only viable approach." Exit via `exit_signal` on loss of
ribbon alignment.

## 2. Behavioural Interpretation

- **Under-reaction to information** (Hong & Stein 1999): gradual diffusion of news produces
  persistent positive drift in price — the empirical basis for medium-horizon momentum.
- **Disposition effect** (Shefrin & Statman 1985): retail holders realise gains early and
  defer losses, which flattens resistance in uptrends (sellers disappear after they've
  exited) and steepens breakdowns.
- **Herding / trend-following flow** from systematic CTAs and trend-followers creates
  feedback — the positions themselves reinforce the signal until they saturate.
- **Recency bias** (Tversky & Kahneman 1974): recent price direction is overweighted by
  discretionary participants, amplifying the trend until a visible reversal.

## 3. Quant / Physics Interpretation

- **Positive serial correlation at intermediate lags.** Classical evidence: Jegadeesh & Titman
  (1993) on equity momentum; Moskowitz, Ooi, Pedersen (2012) on time-series momentum across
  asset classes.
- **Return distribution:** fat right tail during trend regimes, with occasional jump-down
  events (exhaustion gaps). Trend strategies earn the crash risk premium associated with
  left-tail exposure during reversal.
- **ADX as a regime gate:** ADX > 25 empirically correlates with higher Hurst exponent (H > 0.5,
  persistent behaviour); ADX < 20 corresponds to H ≈ 0.5 (random walk) or H < 0.5 (mean
  reversion). The filter is a crude Hurst proxy.
- **EMA ribbon alignment:** the 4-EMA stack is a smoothed derivative indicator. Mathematically
  equivalent to a low-pass filter that triggers when the short-period slope aligns with the
  long-period slope — a discretised test for persistent drift.

## 4. Failure Modes

- **Whipsaw in range-bound regimes.** ADX is the intended guard but is slow — by the time
  ADX falls below 20 the strategy has already lost to two or three whipsaw trades.
- **Reversal at exhaustion.** Parabolic moves end with sharp reversals that round-trip the
  entire trade. Stop placement must absorb the reversal without invalidating the setup.
- **Gap through stop.** Crypto trades 24/7 so pure gaps are rare, but low-liquidity weekends
  and exchange outages can produce slippage that exceeds the expected stop.
- **Trailing-stop pathology (documented).** ATR trailing destroys PF and WR per the
  strategy's own notes — the trail is tighter than normal retrace behaviour in the regimes
  this strategy targets. This is the explicit reason the strategy uses fixed structural
  stops.

## 5. Implication for Strategy Design

- **Entry:** regime filter is load-bearing. ADX or an alternative (Hurst estimator over
  rolling window, realised-volatility clustering test) is not optional.
- **Exit:** "let winners run" is the design principle — that rules out tight trailing stops
  (empirically verified). Candidates to test instead: (i) partial at 1R with the remainder
  on a **wide** structural trail (swing-low), (ii) time-based exit at the median trend
  duration, (iii) exit only on ribbon-alignment break (current default).
- **Stop:** structural, not statistical. Below the most recent swing low for longs.
- **Sizing:** position size should scale with ATR so that stop distance ≈ fixed % of capital
  regardless of current volatility.
- **Sequencing with mean-reversion strategies:** TrendRider is the complement of the
  cointegration / RSI / BB family. The two families should be portfolio-level hedges, not
  run in isolation, because their regimes are disjoint.

## Execution Translation

### Entry Implication

- **Regime gate is load-bearing.** Hold the existing ADX > 25 rule; audit whether ADX < 20 lockout is actually enforced on the entry-firing path.
- **Add slope sign test** on the longest EMA in the ribbon: reject entries where the long EMA slope is flat even if shorter EMAs are stacked — catches late-regime entries.
- **No entry in the first N bars after an ADX ≤ 20 → ADX > 25 transition.** The transition boundary is where whipsaw trades cluster.

### Exit Implication

- **Do NOT introduce ATR trailing.** The strategy file documents empirically that "ATR trailing destroys edge (PF drops to 0.603, WR 28%)." Imposing a tight trailing stop recreates a premature_exit pattern where none currently exists on this prim.
- **Current `premature_exit` rate = 52.2% (168 trades)** — the dominant failure mode on this prim is exit-signal firing on transient ribbon-alignment breaks inside an otherwise continuing trend. These are `missed_continuation` candidates in disguise.
- **Widen the exit trigger to require ribbon-alignment break + ADX drop below threshold** — two-condition AND prevents single-bar whipsaws from firing the exit.
- **Alternative:** partial at 1R, remainder on a **wide** structural (swing-low) trail — preserves the "let winners run" principle while locking in risk-reduction. Addresses MFE capture (57.28% currently) by raising it without reintroducing the ATR-trail pathology.

### Risk / Positioning Implication

- **Size inversely to ATR** so stop-distance-as-%-of-capital is constant across regimes.
- **Longer holding time than mean-reversion prims** — the signal is multi-day by design. Do not apply short time-stops.
- **Lower trade frequency** implies higher per-trade risk budget is acceptable (up to a cap), since fee drag is smaller.

### What this means for current experiments

- [[../../Training Journal/Experiments/trailing-stop-vs-coint]] — **DOES NOT APPLY.** The trailing-stop hypothesis is specifically contraindicated on this prim by the strategy file's documented empirical result. Running it on TrendRider would burn cycles confirming a known failure mode.
- [[../../Training Journal/Experiments/partial-tp-runner]] — **SUPPORTS, with the structural-trail variant.** The "wide trail" case (swing-low, not ATR) is the viable form on this prim. Partial at 1R + swing-low trail addresses missed_continuation without reintroducing the ATR-trail pathology.
- [[../../Training Journal/Experiments/time-based-exit]] — **DOES NOT APPLY** at the median-winner scale. Trend-following's winners are multi-day by design; a median-winner time-stop cuts the very continuation the prim exists to capture. A *maximum-duration* time-stop (weeks) is a different experiment and not currently queued.

## See also

- Registry: matched_strategies = `YujiTrendRiderStrategy` in `data/primitive_scores.csv`
- Library section: [[../../wiki/synthesis/cross-strategy-trade-library|Cross-Strategy Trade Library]]
- Patterns: [[../../Training Journal/Patterns/premature-exit]] · [[../../Training Journal/Patterns/low-mfe-capture]]
- Experiments: [[../../Training Journal/Experiments/partial-tp-runner]] · [[../../Training Journal/Experiments/time-based-exit]]
