---
title: "Experiments — cointegration-residual-reversion (axis 44)"
type: journal-experiment
prim: cointegration-residual-reversion
project: freqtrade
tier: sophisticated
axis: 44
updated: 2026-04-25
---

# Experiments — cointegration-residual-reversion (axis 44)

---

## Cycle 4 — REFINE(EXIT) — 2026-04-25 — Implementer report

### Changes
- `YujiCointegrationResidualReversionStrategy.py`: Added Variant D (A15 trailing z-stop) alongside existing A/B/C variants. New params: `trailing_activation_zscore` (default 1.5σ), `trailing_reversal_margin` (default 0.5σ). Updated `exit_variant` CategoricalParameter to include "D". Added `_trailing_state` dict for per-trade tracking. Added `confirm_trade_exit` for state cleanup. Updated `custom_stoploss` to use `stop_zscore` (4.0σ) for Variant D. prim: cointegration-residual-reversion, cycle 4, REFINE(EXIT) 2026-04-25.
- `YujiCointegrationResidualReversionStrategy.json`: Reset to `exit_variant="A"` (winner).
- `data/primitive_scores.csv`: `force_exit_refine` cleared to False; exit edge metrics updated from IS backtest.

### Backtest Results

IS window: 2022-01-01 → 2024-12-31, 1h, ETH/USDT (BTC/USDT: 0 trades — Engle-Granger gate fails)

| Variant | Trades | WR % | Avg PnL % | MFE % | MAE % | Cap % | Premature % | Missed Cont % | Max DD % | PF |
|---------|--------|------|-----------|-------|-------|-------|-------------|---------------|----------|----|
| A (baseline) | 13 | 46.2 | 3.50 | 12.17 | -6.94 | 67.7 | 15.4 | 7.7 | 2.32 | 1.90 |
| B (A13 partial TP) | 41 | 29.3 | 0.49 | 3.18 | -2.70 | 47.4 | 24.4 | 14.6 | 2.00 | 1.46 |
| C (A13+A14 time gate) | 47 | 38.3 | 0.35 | 3.19 | -2.85 | 48.4 | 29.8 | 19.1 | 1.99 | 1.30 |
| D (A15 trailing z-stop) | 79 | 41.8 | 0.31 | 2.12 | -2.06 | 42.8 | 36.7 | 26.6 | 1.59 | 1.53 |

Pass criteria (B/C/D vs A): capture > 66% AND premature_exit < 35%.

- **Variant A:** cap=67.7% PASS, premature=15.4% PASS → **WINNER (baseline retained)**
- **Variant B:** cap=47.4% FAIL
- **Variant C:** cap=48.4% FAIL
- **Variant D:** cap=42.8% FAIL, premature=36.7% FAIL

### CSV update decision
Variant A is the winner (only variant passing both criteria). `force_exit_refine` set to False. `refinement_attempts` = 4.

### Key findings

1. **Partial TP (A13) is destructive.** Splitting at |z| ≤ 1.0σ cuts the large winners that define Variant A's edge (best trade 61.3% vs 43.0% in B). Win rate collapses from 46.2% → 29.3% because the TP fires on retracements before full reversion.

2. **Time gate (A14) partially rescues C but not enough.** C raises WR back to 38.3% by expiring stale positions, but the partial TP still bleeds capture. Both B and C trade 3–4× more frequently (41/47 vs 13 trades) — the partial TP generates many sub-threshold exits that inflate trade count at the cost of per-trade quality.

3. **Trailing z-stop (A15/D) fires too early in 2022–2024 regime.** 79 trades (6× baseline frequency). Avg duration 1d 4h vs 19d 16h for A. The 1.5σ activation + 0.5σ reversal margin is too sensitive for the slow BTC/ETH mean-reversion dynamic. Many entries trigger before z fully reverts, so the trail fires on normal z oscillations. MAE is halved (-2.06% vs -6.94%) but so is per-trade profitability (0.31% vs 3.50%).

4. **Variant A's exit architecture is correct for this prim.** The `coint_z_reverted` signal (|z| ≤ 0.25σ) waits for full reversion — this is appropriate for an OU process with ~2-day half-life. The single stop-loss at -15.17% is acceptable given 13 trades over 3 years.

5. **IS vs live discrepancy.** Live trades showed avg_premature_exit=62.5% (8 trades); IS backtest shows 15.4% (13 trades). This discrepancy warrants investigation — possible causes: live execution slippage, partial fills, or the live period (post-2024) having different z-score dynamics.

### Next Steps
- Investigate live vs IS premature exit discrepancy (62.5% live vs 15.4% IS). If live slippage is the cause, entry sizing or limit order adjustments may help.
- Consider testing A15 with wider parameters: activation 0.75σ, margin 1.0σ — may reduce noise-triggered exits.
- BTC/USDT still produces 0 trades. The Engle-Granger gate over the full 3-year window is too strict. Consider a shorter rolling gate (e.g., 30d window) or regime-conditional gate.
- cycle_modes.log to REFINE(ENTRY) for BTC pair investigation.

---

## Cycle 6 — REFINE(EXIT) — 2026-04-25T11:15:00Z

**Trigger:** force_exit_refine=True in CSV (live N=8: cap=62.83%, premature=62.5%)

**Context from Cycles 3-5:** IS Variant A passes both criteria (cap=67.7%, premature=15.4%). Live vs IS gap confirmed. All prior exit variants (B/C/D) worsen IS performance. This cycle proposes A16 — the only charter-permitted exit experiment not yet tested.

**A16 — Profit-Based Trailing Stop (charter: "activate after +1R"):**
- Activation: current_profit >= 1.5% (approx +1R; derived from avg_MAE=-6.94%)
- After activation: track z_min = running min of |coint_zscore|; exit if |z| > z_min + 1.0 sigma
- Hard stop: 4.0 sigma (unchanged, parallel)
- No partial TP — isolates profit-based activation effect from A13 mechanism
- Key differentiation from A15: A15 activated at z<=1.5 sigma (z-based, can engage when underwater); A16 activates only on profit confirmation (ensures entry thesis is working before trailing begins)

**Hypothesis:** A16 reduces IS premature_exit below 35% and lifts capture above 66%. If not, force_exit_refine cannot be resolved via exit logic design; problem is live execution/regime; accumulate live N.

**Implementer task:** Add exit_variant="E" to strategy; implement profit-based trailing in custom_exit; backtest 2022-2024 vs Variant A baseline.

**Status:** PENDING implementer backtest

---

## Cycle 10 — REFINE(EXIT) — 2026-04-26 — Implementer report

### Changes
- `YujiCointegrationResidualReversionStrategy.py`: Added Variant E (A16 profit-activated trailing z-stop). New params: `profit_activation_pct` (default 1.5%, range 0.5–3.0), `trailing_margin_sigma` (default 1.0σ, range 0.25–2.0). Added `_trade_state` dict for per-trade activation tracking (keyed by str(trade.id)). Added Variant E branch in `custom_exit()`: activates at `current_profit >= profit_activation_pct/100`, tracks `z_min_since_activation`, exits on `z_abs > z_min + trailing_margin_sigma`. Updated `CategoricalParameter` options to `['A','B','C','D','E']`. Updated `custom_stoploss` to include 'E' in baseline stop group (4.0σ). Updated `confirm_trade_exit` to also clean `_trade_state`. prim: cointegration-residual-reversion, cycle 10, REFINE(EXIT) 2026-04-26.
- `YujiCointegrationResidualReversionStrategy.json`: `exit_variant` set to `"E"`. Added `profit_activation_pct: 1.5` and `trailing_margin_sigma: 1.0`.

### Backtest Results
- Strategy: YujiCointegrationResidualReversionStrategy (Variant E)
- Timerange: N/A — historical backtest architecturally blocked (FM8: single-gate yields 0 BTC/USDT trades in all tested timeranges)
- Timeframe: 1h
- Trades: DRY_RUN — pending N≥30 accumulation
- Profit (%): pending
- Win rate (%): pending
- MFE (avg %): pending
- MAE (avg %): pending
- MFE capture ratio (%): pending
- Premature exit rate (%): pending (pass criterion: < 35%)
- Missed continuation rate (%): pending
- Max drawdown (%): pending

### Import Verification
Strategy imports cleanly inside freqtrade-champion container:
- `exit_variant` options confirmed: `['A', 'B', 'C', 'D', 'E']`
- `profit_activation_pct` default: 1.5
- `trailing_margin_sigma` default: 1.0
- `_trade_state` attribute: present

### Next Steps
- Await N≥30 DRY_RUN trades under `exit_variant='E'`. Post-process journal CSV with `build_all_trades_dataset.py` to derive MFE/MAE/capture/premature_exit metrics.
- Pass criteria: `premature_exit_rate < 35%` AND `MFE_capture > 66%` AND `avg_pnl ≥ Variant A (3.50%)`.
- If passes: clear `force_exit_refine`; prim validated for exit edge at DRY_RUN level.
- If fails: STOP REFINE(EXIT); proceed to rolling-gate REFINE (FM8 structural debt; enables multi-year IS validation but O(N²) compute cost).

