---
title: Research Layer
type: research-index
updated: 2026-04-25
status: active
---

# Research Layer

Cross-domain interpretation for existing trading prims. **Additive only — never a rewrite of
the wiki or Training Journal.** Each page maps a prim to known behavioural-finance and
quant/physics concepts with named references, and surfaces failure modes and strategy-design
implications that are not in the trading record.

## Contents

### Prims/

Top 5 highest-impact prims by the exit-inefficiency scoring:

- [[Prims/cointegration|cointegration]] — OU residual reversion, pairs trading (`force_exit_refine=True`)
- [[Prims/trendrider|trendrider]] — EMA-ribbon + ADX + MACD trend following
- [[Prims/scalper|scalper]] — BB + Stochastic RSI mean-reversion on 15m (not microstructure)
- [[Prims/strategyv2|strategyv2]] — RSI-MR + EMA cross + volume-capitulation ensemble
- [[Prims/vwap-mean-reversion|vwap-mean-reversion]] — VWAP-deviation reversion (worst-capture strategy in library)

## Scope rules

- **Interpretation only.** No re-derivation of metrics; no trade listings; no chart embeds.
  For trades and evidence, link out to `wiki/` or `Training Journal/`.
- **No speculative theory.** Every concept cited must map to a named paper or established
  model (OU process, Jegadeesh & Titman, Hong & Stein, Berkowitz/Logue/Noser, etc.).
- **One page per existing prim.** Do not create Research pages for prims that don't have
  an entry in `freqtrade/user_data/prim_registry.json` or a matching `Yuji*Strategy.py`.
- **Section structure is fixed:** (1) Trading Definition, (2) Behavioural, (3) Quant/Physics,
  (4) Failure Modes, (5) Implication for Strategy Design.

## Not in scope

- New primitives — adding to the registry is a separate workflow.
- Pattern pages, experiments, daily logs — those live in `Training Journal/`.
- Strategy records, trade cards, concept evidence — those live in `wiki/`.

## See also

- [[../wiki/synthesis/current-trading-thesis|Current trading thesis]]
- [[../Training Journal/master|Training Journal master]]
- [[../Training Journal/Control Signals|Control Signals]]
