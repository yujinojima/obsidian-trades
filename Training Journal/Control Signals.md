---
title: Control Signals
type: journal-control
updated: 2026-04-25
status: active
consumers: [Ralph, Tron, human operator]
machine_readable_block: ralph-control
---

# Control Signals

The single authoritative source of **what Ralph should work on next** and **what rules
constrain that work**. Patterns → Triggers → Instructions → Experiments → Feedback. This
page is the Instruction stage.

**Read order:**

1. Patterns flag an issue
2. This page translates pattern signals into Ralph instructions
3. Ralph runs cycles on the focus primitives under the active instructions
4. Experiment pages record outcomes
5. Daily log captures the human-level "what did we learn"
6. This page updates based on new evidence

---

## Global Priority

Ranked instructions. Ralph's next cycle should target the highest-priority unfulfilled item.

1. **Exit inefficiency (HIGH)** — 1,280 premature_exit + 524 missed_continuation + 565 slow_loss
   trades; ≈58% mean MFE capture across the library. Dominant failure mode. All `REFINE`
   cycles should target exit logic until this moves.
2. **Missed continuation (HIGH, subset of #1)** — 524 outcome + 326 diagnosis; concentrated
   on high-volume strategies (Scalper 89, V2 87, MoneyMaker 70). Partial-TP-and-runner is the
   targeted remedy ([[Experiments/partial-tp-runner]]).
3. **Entry refinement (LOW)** — 668 poor_entry + 561 noise_trade flagged; but only 2/15
   strategies are classified `weak_entry_strong_exit`. Entry work is deprioritised until exit
   fixes are exhausted, per the Enforcement Rule in [[master#Enforcement Rule]].

## Active Instructions

Rules Ralph applies to every cycle until explicitly revoked on this page.

- **Force REFINE cycles on high-MFE / low-capture prims.** Any primitive associated with a
  strategy whose MFE capture < 66% and whose avg MFE ≥ 5% is a mandatory REFINE target
  (currently: the prims behind `YujiCointegrationResidualReversionStrategy`).
- **Block new entry-prim creation unless justified.** Creating a new entry-side primitive
  requires explicit justification on [[../wiki/questions/README|wiki/questions/]] — linked
  from this page — and Director approval per the workspace's revenue-alignment rule. The
  12 fully_inefficient strategies already have entry problems; the bottleneck is that we
  haven't fixed their *exits* yet, not that we need more entry signals.
- **Exit-rule variant experiments must log to `Experiments/` with the frontmatter schema**
  (see any existing experiment page). Required fields: `status`, `priority`, `originating_pattern`,
  `target_strategy(ies)`, `cycle_mode`.
- **No primitive may be promoted to `sophisticated` tier** until its parent strategy's
  MFE capture exceeds 66% on ≥ 100 trades across ≥ 2 pairs.

## Current Focus Primitives

Primitives Ralph should refine (not create) in the current cycle. List is intentionally short
— refinement focus beats breadth.

| Primitive | Tier | Archetype of parent strat | Why on the list |
|---|---|---|---|
| cointegration (signal family) | `research_candidate` | strong_entry_weak_exit | only profitable archetype; exit is the bottleneck |
| trendrider (exit family) | `intermediate` | fully_inefficient | highest-volume exit-weak, 322 trades, 52% premature_exit |
| scalper (exit family) | `intermediate` | fully_inefficient | 288 trades, 89 missed_continuation (largest volume) |
| strategyv2 (exit family) | `intermediate` | weak_entry_strong_exit | 87 missed_continuation despite "strong exit" archetype — inconsistency worth resolving |

## Deprioritised — do NOT work on these this cycle

- New entry-side signal primitives
- Primitive-taxonomy expansion / reorganisation
- New market-state definitions beyond the Phase-1 plan
- Any cosmetic changes to the wiki (documentation-only work)

## Ralph payload (machine-readable)

Ralph and downstream tooling should parse the fenced block below. This is the authoritative
structured form of the instructions above. If this block and the human-readable sections
disagree, fix the human-readable sections and re-emit the block — the human text is
canonical.

```yaml
# ralph-control
cycle_mode_default: REFINE
priority_queue:
  - id: exit-inefficiency
    level: HIGH
    evidence: "premature_exit=1280; missed_continuation=524; slow_loss=565; mean_capture~0.58"
    active: true
  - id: missed-continuation
    level: HIGH
    evidence: "outcome=524; diagnosis=326; top3_strategies=[Scalper,V2,MoneyMaker]"
    active: true
    subset_of: exit-inefficiency
  - id: entry-refinement
    level: LOW
    evidence: "poor_entry=668; noise_trade=561; weak_entry_strong_exit=2/15"
    active: false
    reason_blocked: "exit fixes not yet exhausted"

active_experiments:
  - path: "Training Journal/Experiments/trailing-stop-vs-coint.md"
    priority: HIGH
    status: queued
    target_strategy: YujiCointegrationResidualReversionStrategy
  - path: "Training Journal/Experiments/partial-tp-runner.md"
    priority: HIGH
    status: queued
    target_strategies: [YujiScalperStrategy, YujiStrategyV2, YujiMoneyMakerStrategy, YujiCointegrationResidualReversionStrategy]
  - path: "Training Journal/Experiments/time-based-exit.md"
    priority: MEDIUM
    status: queued
    target_strategies: [YujiCointegrationResidualReversionStrategy, YujiScalperStrategy, YujiStrategyV2, YujiMoneyMakerStrategy]

focus_primitives:
  - cointegration
  - trendrider
  - scalper
  - strategyv2

enforcement_rules:
  - id: prioritise-exit-over-entry
    rule: "All new work must prioritise exit refinement over entry creation"
    source: "Training Journal/master.md#Enforcement Rule"
  - id: sophistication-gate
    rule: "No primitive promoted to sophisticated tier until parent strategy MFE capture >66% on >=100 trades across >=2 pairs"
  - id: exit-variant-logging
    rule: "Exit-rule variant experiments must log to Experiments/ with required frontmatter"

deprioritised:
  - new-entry-primitives
  - primitive-taxonomy-expansion
  - new-market-state-definitions
  - documentation-only-work

last_updated: 2026-04-25
next_review_trigger: "On completion of any HIGH-priority experiment OR on ingest of new trade dataset"
```

## Revision log

- **2026-04-25** — Initial creation. Priorities derived from `data/all_trades_dataset.csv`
  (3,300 trades) and `reports/strategy_diagnosis.md`. Three experiments queued; Ralph's
  default cycle mode set to REFINE.

## Linked pages

- [[master|Training Journal master]] (System Bottleneck, Enforcement Rule)
- [[Patterns/premature-exit]] · [[Patterns/missed-continuation]] · [[Patterns/low-mfe-capture]]
- [[Experiments/trailing-stop-vs-coint]] · [[Experiments/partial-tp-runner]] · [[Experiments/time-based-exit]]
- [[Mistakes]]
- [[../wiki/synthesis/current-trading-thesis|Current trading thesis]]
