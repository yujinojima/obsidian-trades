---
title: "Research — Cointegration (Residual Reversion)"
type: research-prim
updated: 2026-04-25
status: active
registry_name: cointegration-residual-reversion
parent_strategy: YujiCointegrationResidualReversionStrategy
force_exit_refine: true
---

# Cointegration — Cross-Domain Interpretation

Interpretation layer only. Trading record lives at
[[../../wiki/strategies/YujiCointegrationResidualReversionStrategy|wiki/strategies/…]].
Exit pattern lives at [[../../Training Journal/Patterns/premature-exit|Patterns/premature-exit]].

## 1. Trading Definition

Two non-stationary price series whose linear combination is stationary. Trade fires when the
residual's z-score crosses an entry threshold; exits when z reverts toward zero. In this
library: ETH or LINK against a partner asset, entry at z-extreme, exit via `coint_z_reverted`.

## 2. Behavioural Interpretation

- **Relative-price anchoring.** Market participants co-price related assets. Temporary
  divergences violate the reference frame and attract convergence trades — this is the
  classic "pairs trading" rationale (Gatev, Goetzmann, Rouwenhorst 2006).
- **Convergence-trade crowding.** Once enough participants recognise the divergence, their
  positioning itself creates the reversion. The signal is partly self-fulfilling while the
  crowd persists.
- **Under-reaction on the leg that drifts** (Barberis, Shleifer, Vishny 1998): one asset's
  price lags new information while the other has already incorporated it, producing the
  residual.

## 3. Quant / Physics Interpretation

- **Residual ≈ Ornstein-Uhlenbeck process** under stationarity:
  `dXt = θ(μ − Xt)dt + σ dWt`. Half-life of reversion: `τ_½ = ln(2)/θ`.
- **Stationarity tests:** Engle-Granger (two-step), Johansen (vector framework for >2 assets),
  ADF/KPSS on the residual. Cointegration is a rank condition on Π in a VECM.
- **Statistical structure:** the residual has bounded variance in expectation and negative
  autocorrelation at the half-life scale. Its distribution is approximately Gaussian in
  equilibrium but fat-tailed at break points.
- **Z-score entry ≈ "distance from equilibrium in standard deviations."** Standard practical
  thresholds: entry at |z| ≈ 2, exit at z ≈ 0 — explicitly the mean of the OU process.

## 4. Failure Modes

- **Cointegration breaks.** The long-run relationship is a statistical fit, not a structural
  law. A regime shift (new listing, tokenomics change, de-peg, exchange migration) removes
  the equilibrium and the residual becomes a random walk.
- **Spurious cointegration** on small samples — Granger & Newbold 1974. The statistical test
  passes but the relationship is not real.
- **Leg-timing risk.** Entries are inherently multi-leg; execution slippage on one leg
  converts a spread bet into a directional position.
- **Overlap with a trending underlying.** Residual can revert while the pair keeps trending —
  a "textbook" reversion that still underperforms a momentum-style hold. Observed on Coint
  trade_0005 (+26.57% realised vs +40.74% MFE; see [[../../Training Journal/Patterns/premature-exit|premature-exit]]).
- **Non-stationary variance.** σ may itself be regime-dependent; a z-score calibrated in a
  quiet regime fires too often in a noisy one.

## 5. Implication for Strategy Design

- **Entry:** z-threshold alone is underspecified. Pair with (a) a stationarity confirmation
  (rolling ADF p-value, half-life < N bars), (b) a volatility-regime filter so the z is
  scaled to the current regime.
- **Exit:** z-reversion-to-zero is the canonical OU exit but it cuts runners when the
  underlying leg keeps trending. Candidates to test: (i) exit at z = 0 AND the pair's own
  momentum has flipped; (ii) partial exit at z = 0 with the remainder on a trail.
  See [[../../Training Journal/Experiments/trailing-stop-vs-coint]].
- **Risk:** size by the half-life — slow-reverting spreads require smaller size for the same
  expected holding-period vol.
- **Sample floor:** 8 trades is not enough. Broaden the universe (more pairs, longer window)
  before declaring an edge.

## Execution Translation

### Entry Implication

- **Add stationarity precondition** before entry: require the residual's rolling ADF p-value < 0.05 on an N-bar window AND half-life τ_½ < max_holding_bars. No OU-process claim without the test.
- **Add volatility-regime scaling** to the z-threshold: entry |z| must exceed a threshold expressed in regime-adjusted σ, not raw σ — prevents the "z-2 in quiet regime" trap.
- **No entry during observed cointegration breaks** — if ADF fails on a rolling window, suspend the pair until it re-passes.

### Exit Implication

- **The current `coint_z_reverted` exit is the direct cause of the 62.5% `premature_exit` rate** and 62.83% MFE capture — observed directly on Coint trade_0005 (+26.57% realised vs +40.74% MFE). This is the primary system bottleneck.
- **Replace pure z=0 exit with a compound condition**: exit only when the residual reverts to zero AND the underlying pair's momentum has flipped. Prevents exits into continued leg-trends (the `missed_continuation` signature).
- **Alternative:** partial exit at z=0, trail the remainder. Captures both the mean-reversion signal and continuation when the leg keeps running — directly addresses the MFE-capture gap.
- **Do not tighten exits.** The prim's failure mode is under-capture, not over-extension; any rule that shrinks the realised/MFE ratio further is moving in the wrong direction.

### Risk / Positioning Implication

- **Size inversely to half-life.** Longer τ_½ → smaller position, because expected holding-period vol scales with √τ_½.
- **Do not compound on n=8.** Cap allocation at seed size until sample exceeds 30 across at least 2 pairs.
- **Multi-leg slippage budget.** Log per-trade leg-timing slippage; if it exceeds half the z=0 target, the spread bet has degraded into a directional position.

### What this means for current experiments

- [[../../Training Journal/Experiments/trailing-stop-vs-coint]] — **SUPPORTS DIRECTLY.** The theory (OU residual + leg trending beyond residual reversion) predicts that a trailing stop will outperform the pure z-reversion exit precisely because it captures the continuation the residual exit ignores. This is the canonical test case for this prim.
- [[../../Training Journal/Experiments/partial-tp-runner]] — **SUPPORTS, SECONDARY.** Partial take at z=0 + runner is the hybrid implementation of "residual reverted but leg still running." Use as the fallback design if pure trailing underperforms.
- [[../../Training Journal/Experiments/time-based-exit]] — **CONDITIONAL.** Useful only if the half-life is stable — a time-stop at median winner duration is effectively a τ_½ approximation. Priority MEDIUM because it's less specific than the two above.

## See also

- Registry: `freqtrade/user_data/prim_registry.json` → `cointegration-residual-reversion` (tier: sophisticated)
- Strategy record: [[../../wiki/strategies/YujiCointegrationResidualReversionStrategy|wiki/strategies/…]]
- Exit analysis: [[../../wiki/exit-analysis/coint-z-reverted]]
- Journal pattern: [[../../Training Journal/Patterns/premature-exit]]
- Experiment: [[../../Training Journal/Experiments/trailing-stop-vs-coint]]
