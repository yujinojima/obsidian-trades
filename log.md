# Activity Log

Append-only. Latest entries at the top. Each entry uses the schema in [[CLAUDE|CLAUDE.md]] §4.

---

## [2026-04-25 00:15] wiki-init | Karpathy-style restructure of obsidian_trade_journals

- Source: v1 export at `YujiCointegrationResidualReversionStrategy/` (8 trades, generated 2026-04-24T13:59Z)
- Files created:
  - `CLAUDE.md` (schema)
  - `index.md` (rewritten as global wiki content map)
  - `log.md` (this file)
  - `dashboard.md` (rewritten as operational dashboard)
  - `raw/journals/YujiCointegrationResidualReversionStrategy-20260424/` (immutable copy of v1 export)
  - `raw/charts/YujiCointegrationResidualReversionStrategy/trade_0001.png` … `trade_0008.png` (immutable copy)
  - `wiki/strategies/YujiCointegrationResidualReversionStrategy.md`
  - `wiki/trades/YujiCointegrationResidualReversionStrategy/trade_0001.md` … `trade_0008.md` (rewritten with concept/primitive/state backlinks)
  - `wiki/concepts/missed-continuation.md`
  - `wiki/concepts/slow-loss.md`
  - `wiki/concepts/noisy-win.md`
  - `wiki/concepts/bad-entry-good-idea.md`
  - `wiki/concepts/clean-win.md`
  - `wiki/concepts/mfe-capture-ratio.md`
  - `wiki/concepts/mean-reversion.md`
  - `wiki/exit-analysis/coint-z-reverted.md`
  - `wiki/exit-analysis/premature-exit.md`
  - `wiki/exit-analysis/efficient-exit.md`
  - `wiki/exit-analysis/poor-entry.md`
  - `wiki/primitives/bollinger-squeeze-breakout.md` (canonical) — alias: volatility-compression
  - `wiki/primitives/fair-value-gap-price-discovery.md` (canonical) — aliases: fair-value-gap, fvg
  - `wiki/primitives/liquidity-sweep-reversal.md` (canonical) — aliases: liquidity-sweep, sweep
  - `wiki/primitives/volume-spike.md` (provisional, no registry entry)
  - `wiki/primitives/trend-break.md` (provisional, no registry entry)
  - `wiki/market-states/trending-up.md`
  - `wiki/market-states/trending-down.md`
  - `wiki/market-states/ranging.md`
  - `wiki/market-states/high-volatility.md`
  - `wiki/market-states/compression.md`
  - `wiki/synthesis/current-trading-thesis.md`
  - `wiki/questions/README.md`
  - `scripts/wiki_maintain.py`
  - `reports/wiki_lint_report.md` (generated)
- Files updated:
  - `index.md` (was v1 strategy table → now Karpathy-style content map)
  - `dashboard.md` (was v1 tag-query dump → now operational dashboard)
- Files preserved without edit:
  - `YujiCointegrationResidualReversionStrategy/` (v1 folder kept in place per user decision #3; raw is a copy, not a move)
- Key findings:
  - 8-trade sample is statistically fragile; all strategy / concept pages carry LOW-confidence flags
  - Exit diagnosis `premature_exit` fires on 5 of 8 trades (62.5%) — strongest signal in the sample
  - 100% of trades use the `coint_z_reverted` exit — exit concentration is complete
  - 4 of 6 winners flagged `missed_continuation`; MFE capture ratio 62.83% → exits leave continuation on the table
  - 88% of trades on ETH/USDT → pair-dependence warning
  - Signal-level data (primitive firings, true market state labels) is unavailable in v1 export; primitives and market-state pages marked provisional
- Open questions (now tracked in `wiki/questions/`):
  - Does a trailing stop beat `coint_z_reverted` on the same signal set?
  - Does the strategy hold on pairs other than ETH/USDT at useful sample size?
  - Do the 4 `missed_continuation` trades share a market-state signature?

---

## [2026-04-25 00:24] maintain | wiki_maintain.py pass
- Pages scanned: 35
- Orphans: 0
- Broken links: 25
- Missing frontmatter: 0
- Stale: 0
- Strategies missing trade links: 0
- Trades missing related links: 0
- Files updated: `index.md`, `dashboard.md`, `reports/wiki_lint_report.md`

---

## [2026-04-25 00:25] maintain | wiki_maintain.py pass
- Pages scanned: 35
- Orphans: 0
- Broken links: 0
- Missing frontmatter: 0
- Stale: 0
- Strategies missing trade links: 0
- Trades missing related links: 0
- Files updated: `index.md`, `dashboard.md`, `reports/wiki_lint_report.md`

---

## [2026-04-25 00:38] maintain | wiki_maintain.py pass
- Pages scanned: 35
- Orphans: 0
- Broken links: 0
- Missing frontmatter: 0
- Stale: 0
- Strategies missing trade links: 0
- Trades missing related links: 0
- Files updated: `index.md`, `dashboard.md`, `reports/wiki_lint_report.md`

---

## [2026-04-25 00:40] ingest | strategy_diagnosis.md cross-strategy data

- Source: `reports/strategy_diagnosis.md` (batch `batch-20260424T123546Z`, 15 strategies)
- Files created: none (structure unchanged per task constraints)
- Files updated:
  - `wiki/synthesis/current-trading-thesis.md` (+ Cross-Strategy Findings, + Strategy Archetypes, + cross_strategy_source frontmatter)
  - `wiki/concepts/missed-continuation.md` (evidence_count 4 → 524, + cross-strategy section)
  - `wiki/concepts/mfe-capture-ratio.md` (evidence_count 8 → 15, + full 15-strategy distribution)
  - `wiki/exit-analysis/premature-exit.md` (evidence_count 5 → 1280, + cross-strategy section)
  - `dashboard.md` (+ System-Level Diagnosis section, regenerated via wiki_maintain.py)
  - `scripts/wiki_maintain.py` (dashboard template extended)
- Key findings:
  - 0 robust strategies in the 15-strategy batch (no strong_entry_strong_exit archetype member)
  - 10/15 strategies carry the report's `early-exit` flag; 8/15 strictly exceed 45% premature_exit
  - Exit inefficiency is the dominant failure mode — 13/15 strategies have an exit-related failure signature
  - Archetype counts: 1 strong_entry_weak_exit · 2 weak_entry_strong_exit · 12 fully_inefficient · 0 robust
  - Mean MFE capture across measurable strategies: ≈58% (typical strategy leaves ~42% of the move)
  - Missed-continuation trades: 524 across 14 of 15 strategies
  - premature_exit-diagnosed trades: ~1,280 across 14 of 15 strategies
  - YujiVWAPMeanReversionStrategy has low missed-continuation rate (0.76%) because win rate is 1.8%, not because exits are efficient — capture is 37.5% (lowest in batch)
- Open questions:
  - Does the partial-take-profit + runner exit variant recover expected PnL on the top-3 highest-count strategies (Scalper, V2, MoneyMaker)?
  - Are the 2 weak_entry_strong_exit strategies (Strategy, StrategyV2) candidates for entry-filter redesign rather than exit tuning?

---

## [2026-04-25 00:39] maintain | wiki_maintain.py pass
- Pages scanned: 35
- Orphans: 0
- Broken links: 0
- Missing frontmatter: 0
- Stale: 0
- Strategies missing trade links: 0
- Trades missing related links: 0
- Files updated: `index.md`, `dashboard.md`, `reports/wiki_lint_report.md`

---

## [2026-04-25 01:07] maintain | wiki_maintain.py pass
- Pages scanned: 36
- Orphans: 0
- Broken links: 0
- Missing frontmatter: 0
- Stale: 0
- Strategies missing trade links: 0
- Trades missing related links: 0
- Files updated: `index.md`, `dashboard.md`, `reports/wiki_lint_report.md`

---

## [2026-04-25 00:55] ingest | data/all_trades_dataset.csv (Ben's all-trades build)

- Source: `data/all_trades_dataset.csv` (3,300 trades, 15 strategies, 2022-05-02 → 2026-04-20)
  + `data/all_trade_charts/` (3,300 PNG charts, all paths verified to resolve)
- Files created:
  - `wiki/synthesis/cross-strategy-trade-library.md` (1,087 lines, 50 representative trade rows across 5 sections)
  - `scripts/ingest_all_trades_library.py` (generator, idempotent, re-runnable)
- Files updated:
  - `wiki/synthesis/current-trading-thesis.md` (+ Full Trade Library section above Cross-Strategy Findings)
  - `wiki/concepts/missed-continuation.md` (+ Full-library evidence section; frontmatter now cites all_trades_dataset.csv)
  - `wiki/concepts/mfe-capture-ratio.md` (+ Full-library evidence section; added efficient_exit=336)
  - `wiki/exit-analysis/premature-exit.md` (+ Full-library evidence section; confirmed 1,280)
  - `wiki/exit-analysis/efficient-exit.md` (evidence_count 1 → 336; + Full-library evidence section)
  - `scripts/wiki_maintain.py` (dashboard template extended with full-library totals)
  - `dashboard.md` (regenerated by wiki_maintain.py)
- Key findings:
  - `fast_loss` is the single largest outcome bucket at 1,074 trades (32.5%) — not `missed_continuation`
  - `premature_exit` is the single largest exit diagnosis at 1,280 trades (38.8%)
  - `slow_loss` (565) is the second-largest outcome bucket, previously unsurfaced in concept pages (no dedicated concept page created per "do not change structure")
  - `outcome = missed_continuation` (524) and `exit_diagnosis = missed_continuation` (326) are distinct labels with heavy but not total overlap; union used for library section
  - 6 distinct pairs: BTC/USDT (1,231) > ETH/USDT (1,177) > SOL/USDT (262) > XRP/USDT (220) > LINK/USDT (208) > AVAX/USDT (202)
  - Representative selection rule per section explicitly stated at the top of each section
- Constraints respected:
  - No backtests re-run
  - No new metrics beyond grouping/summarising CSV fields (only allowed computation was `mfe_pct − profit_ratio` subtraction as a ranking key for the premature-exits section, which is a difference of two existing fields)
  - No inferred market states or indicators
  - No new primitive pages, no new concept pages (structure unchanged)
  - All 3,300 charts stayed in `data/`; wiki page links in via relative paths, 50 embedded
- Broken chart paths: **0** (all 3,300 verified before generation)
- Broken wikilinks: **0** (lint clean post-ingest)

---

## [2026-04-25 01:07] maintain | wiki_maintain.py pass
- Pages scanned: 36
- Orphans: 0
- Broken links: 0
- Missing frontmatter: 0
- Stale: 0
- Strategies missing trade links: 0
- Trades missing related links: 0
- Files updated: `index.md`, `dashboard.md`, `reports/wiki_lint_report.md`

---

## [2026-04-25 05:06] maintain | wiki_maintain.py pass
- Pages scanned: 36
- Orphans: 0
- Broken links: 0
- Missing frontmatter: 0
- Stale: 0
- Strategies missing trade links: 0
- Trades missing related links: 0
- Files updated: `index.md`, `dashboard.md`, `reports/wiki_lint_report.md`

---

## [2026-04-25 01:20] ingest | Training Journal structure created

- Source: no new data — this is a learning-system scaffolding pass on top of the existing
  library. Uses labels and counts already present in `data/all_trades_dataset.csv`.
- Files created:
  - `Training Journal/master.md` (system state, key stats, hypothesis, active experiments)
  - `Training Journal/Daily/2026-04-25.md` (first daily log)
  - `Training Journal/Patterns/premature-exit.md` (practitioner-facing recognition + remedy)
  - `Training Journal/Patterns/missed-continuation.md` (practitioner-facing recognition + remedy)
  - `Training Journal/Patterns/low-mfe-capture.md` (strategy-level signature + remedies per archetype)
  - `Training Journal/Mistakes.md` (recurring-errors taxonomy with append-only per-incident log)
- Files updated:
  - `scripts/wiki_maintain.py` (dashboard template gained a Training Journal section)
  - `dashboard.md` (regenerated)
- Not touched (per "do not replace existing trade library"):
  - `wiki/` — all 36 pages untouched
  - `raw/` — unchanged
  - `data/all_trades_dataset.csv` + `data/all_trade_charts/` — not modified
- Structural notes:
  - Training Journal sits as a sibling of `wiki/`, `raw/`, `reports/`, `scripts/`; it is a
    separate subsystem with its own naming scheme.
  - Pattern pages share basenames with wiki/concepts/ pages (e.g. `missed-continuation.md`)
    by user-path instruction. Cross-links from journal to wiki use explicit relative paths
    (`[[../../wiki/...]]`) to avoid basename-resolution ambiguity.
- wiki_maintain.py coverage:
  - `wiki/` lint coverage is unchanged (36 pages, 0 broken, 0 orphans).
  - Training Journal/ internal links are **not** currently lint-scanned — a follow-up could
    extend the scanner to include that directory. Chart embeds in journal pages use
    markdown syntax `![alt](../../../data/...)` so they don't register as wikilinks.

---

## [2026-04-25 05:06] maintain | wiki_maintain.py pass
- Pages scanned: 36
- Orphans: 0
- Broken links: 0
- Missing frontmatter: 0
- Stale: 0
- Strategies missing trade links: 0
- Trades missing related links: 0
- Files updated: `index.md`, `dashboard.md`, `reports/wiki_lint_report.md`

---

## [2026-04-25 05:13] maintain | wiki_maintain.py pass
- Pages scanned: 36
- Orphans: 0
- Broken links: 0
- Missing frontmatter: 0
- Stale: 0
- Strategies missing trade links: 0
- Trades missing related links: 0
- Files updated: `index.md`, `dashboard.md`, `reports/wiki_lint_report.md`

---

## [2026-04-25 01:45] extend | Training Journal → Ralph feedback loop

- Source: no new data — extends the 01:20 Training Journal scaffolding into an active
  decision system by wiring Patterns → Triggers → Instructions → Experiments → Daily-log Feedback.
- Files created:
  - `Training Journal/Control Signals.md` — Ralph-facing instruction source with Global
    Priority, Active Instructions, Current Focus Primitives, and a machine-readable
    `ralph-control` YAML block consumers can parse
  - `Training Journal/Experiments/trailing-stop-vs-coint.md` (HIGH, queued)
  - `Training Journal/Experiments/partial-tp-runner.md` (HIGH, queued)
  - `Training Journal/Experiments/time-based-exit.md` (MEDIUM, queued)
- Files updated:
  - `Training Journal/master.md` (+ System Bottleneck, + Enforcement Rule, + Control signals / Experiments cross-link sections)
  - `Training Journal/Patterns/premature-exit.md` (+ Action Trigger, + Active Experiments, + Control link)
  - `Training Journal/Patterns/missed-continuation.md` (+ Action Trigger, + Active Experiments, + Control link)
  - `Training Journal/Patterns/low-mfe-capture.md` (+ Action Trigger, + Active Experiments, + Control link)
  - `Training Journal/Daily/2026-04-25.md` (+ Next Cycle Instruction section with machine-readable `ralph-next-cycle` YAML block)
  - `scripts/wiki_maintain.py` (dashboard template gained Control Signals link and Experiments listing)
  - `dashboard.md` (regenerated)
- Not touched (per "do not change existing library / dataset / charts / pattern explanations"):
  - `wiki/` — all 36 pages untouched
  - `data/` — unchanged
  - `raw/` — unchanged
  - Pattern explanation bodies (Recognition, Representative trades, Library evidence,
    Remedy candidates) were preserved; extensions are additive only
- Structural notes:
  - Control Signals.md is the single authoritative instruction source. The `ralph-control`
    fenced YAML block is the machine-readable form; human-text sections are canonical if
    they disagree.
  - Daily log gained a `ralph-next-cycle` YAML block — today's next cycle: REFINE mode on
    cointegration exit logic, targeting `trailing-stop-vs-coint` experiment.
  - Enforcement Rule: "All new work must prioritise exit refinement over entry creation"
    is live in master.md and reflected in Control Signals active instructions.
  - Three experiments queued with full YAML frontmatter (status, priority,
    originating_pattern, target strategies, cycle_mode) — Ralph can pick any up by path.
- Verification:
  - wiki_maintain.py lint on wiki/: 36 pages, 0 broken, 0 orphans, 0 missing frontmatter, 0 stale
  - Manual lint over the 10 Training Journal pages: 109 wikilinks checked, **0 broken**;
    all markdown image embeds resolve

---

## [2026-04-25 05:14] maintain | wiki_maintain.py pass
- Pages scanned: 36
- Orphans: 0
- Broken links: 0
- Missing frontmatter: 0
- Stale: 0
- Strategies missing trade links: 0
- Trades missing related links: 0
- Files updated: `index.md`, `dashboard.md`, `reports/wiki_lint_report.md`

---

## [2026-04-25 05:25] maintain | wiki_maintain.py pass
- Pages scanned: 36
- Orphans: 0
- Broken links: 0
- Missing frontmatter: 0
- Stale: 0
- Strategies missing trade links: 0
- Trades missing related links: 0
- Files updated: `index.md`, `dashboard.md`, `reports/wiki_lint_report.md`

---

## [2026-04-25 02:10] extend | Research Layer — cross-domain interpretation for top 5 prims

- Source: `freqtrade/user_data/prim_registry.json` (canonical prim metadata) +
  `data/primitive_scores.csv` (scoring + force_exit_refine flag) + strategy files at
  `freqtrade/user_data/strategies/Yuji*Strategy.py` (signal ground truth)
- Files created:
  - `Research/README.md` (index + scope rules)
  - `Research/Prims/cointegration.md`
  - `Research/Prims/trendrider.md`
  - `Research/Prims/scalper.md`
  - `Research/Prims/strategyv2.md`
  - `Research/Prims/vwap-mean-reversion.md`
- Files updated:
  - `scripts/wiki_maintain.py` (dashboard template gained Research Layer section)
  - `dashboard.md` (regenerated)
- Not touched (per "additive, not a rewrite"):
  - `wiki/` — all 36 pages untouched
  - `Training Journal/` — all 10 pages untouched
  - `raw/` — unchanged
  - `data/` — unchanged (read-only)
  - `freqtrade/` — unchanged (read-only)
- Scope of each Research/Prims page (fixed structure):
  1. Trading Definition (strategy-file ground truth)
  2. Behavioural Interpretation (named theories: anchoring, disposition, under-reaction, herding, gambler's fallacy, etc.)
  3. Quant / Physics Interpretation (OU process, Engle-Granger, Jegadeesh & Titman, Moskowitz/Ooi/Pedersen, Jegadeesh 1990, Lo & MacKinlay, Berkowitz/Logue/Noser, Roll model references)
  4. Failure Modes
  5. Implication for Strategy Design
- Selection note — "any prim flagged force_exit_refine":
  - Only `cointegration-residual-reversion` has `force_exit_refine=True` in primitive_scores.csv
  - That overlapped with user's first-slot named prim, so the 5th slot was interpreted as
    "highest-impact additional force-refine candidate"
  - Chosen: `vwap-deviation-mean-reversion` (worst MFE capture 37.5%, largest volume 920 trades,
    worst cumulative PnL -357.78%)
  - Interpretation stated explicitly in the 5th file's `selection_note` frontmatter
- Signal ground-truth discoveries from reading the strategy files:
  - TrendRider file explicitly forbids ATR trailing ("ATR trailing destroys edge; PF drops to 0.603, WR 28%") — captured in the trailing-stop failure mode section
  - Scalper is actually mean-reversion on 15m (BB + Stoch RSI + HA), NOT microstructure scalping — interpretation reframed accordingly
  - StrategyV2 was built from "lessons from 8 strategy backtests" as an ensemble OR of three sub-signals — captured as the ensemble-inconsistency failure mode
- Verification:
  - wiki_maintain.py lint on wiki/: 36 pages, 0 broken, 0 orphans, 0 missing frontmatter, 0 stale
  - Manual lint over the 6 Research pages: **39 wikilinks checked, 0 broken**

---

## [2026-04-25 05:26] maintain | wiki_maintain.py pass
- Pages scanned: 36
- Orphans: 0
- Broken links: 0
- Missing frontmatter: 0
- Stale: 0
- Strategies missing trade links: 0
- Trades missing related links: 0
- Files updated: `index.md`, `dashboard.md`, `reports/wiki_lint_report.md`

---

## [2026-04-25 05:48] maintain | wiki_maintain.py pass
- Pages scanned: 36
- Orphans: 0
- Broken links: 0
- Missing frontmatter: 0
- Stale: 0
- Strategies missing trade links: 0
- Trades missing related links: 0
- Files updated: `index.md`, `dashboard.md`, `reports/wiki_lint_report.md`

---

## [2026-04-25 02:30] extend | Research/Prims — Execution Translation sections added

- Source: no new data. Translates existing section-5 material in each Research/Prims page
  into concrete execution rules. No new theory.
- Files updated:
  - `Research/Prims/cointegration.md` (+ Execution Translation section, 4 subsections)
  - `Research/Prims/trendrider.md` (+ Execution Translation section, 4 subsections)
  - `Research/Prims/scalper.md` (+ Execution Translation section, 4 subsections)
  - `Research/Prims/strategyv2.md` (+ Execution Translation section, 4 subsections)
  - `Research/Prims/vwap-mean-reversion.md` (+ Execution Translation section, 4 subsections)
- Files NOT touched: everything else (wiki/, Training Journal/, data/, raw/, scripts/)
- Structure of each Execution Translation section (fixed per task):
  1. Entry Implication — concrete rules on filters, conditions, avoidance
  2. Exit Implication — explicitly references premature_exit, missed_continuation, MFE capture
     per task requirement; translates theory to exact exit-logic rules
  3. Risk / Positioning Implication — sizing, holding time, trade frequency
  4. What this means for current experiments — explicit supports/does-not-apply/conditional
     verdict for each of the 3 queued experiments with justification
- Experiment-verdict matrix (cross-reference for Ralph):
  | Prim           | trailing-stop-vs-coint | partial-tp-runner | time-based-exit |
  |----------------|------------------------|-------------------|-----------------|
  | cointegration  | SUPPORTS (primary)     | SUPPORTS (fallback) | CONDITIONAL    |
  | trendrider     | DOES NOT APPLY         | SUPPORTS (swing-low variant only) | DOES NOT APPLY (median) |
  | scalper        | DOES NOT APPLY (xfer)  | SUPPORTS (primary) | CONDITIONAL     |
  | strategyv2     | DOES NOT APPLY         | DOES NOT APPLY    | DOES NOT APPLY  |
  | vwap-mean-rev  | DOES NOT APPLY         | DOES NOT APPLY (after entry fix) | DOES NOT APPLY |
- Implicit new experiments flagged (not yet queued in Training Journal/Experiments/):
  - strategyv2: per-sub-signal regime-gated entry redesign (blocked by enforcement rule)
  - vwap-mean-reversion: intraday-trend-regime-gated entry (proposed as exception to enforcement rule)
- Verification:
  - wiki_maintain.py lint on wiki/: 36 pages, 0 broken, 0 orphans, 0 missing frontmatter, 0 stale
  - Manual lint on Research/: **56 wikilinks checked, 0 broken**
  - Section-structure audit: all 5 pages have the 4 required subsections in the specified order
  - Exit-Implication concept-citation audit: all 5 pages reference premature_exit,
    missed_continuation, and MFE capture in the Exit Implication subsection

---

## [2026-04-25 05:48] maintain | wiki_maintain.py pass
- Pages scanned: 36
- Orphans: 0
- Broken links: 0
- Missing frontmatter: 0
- Stale: 0
- Strategies missing trade links: 0
- Trades missing related links: 0
- Files updated: `index.md`, `dashboard.md`, `reports/wiki_lint_report.md`

---

## [2026-04-25 06:17] maintain | wiki_maintain.py pass
- Pages scanned: 36
- Orphans: 0
- Broken links: 0
- Missing frontmatter: 0
- Stale: 0
- Strategies missing trade links: 0
- Trades missing related links: 0
- Files updated: `index.md`, `dashboard.md`, `reports/wiki_lint_report.md`

---

## [2026-04-25 21:16] maintain | wiki_maintain.py pass
- Pages scanned: 36
- Orphans: 0
- Broken links: 0
- Missing frontmatter: 0
- Stale: 0
- Strategies missing trade links: 0
- Trades missing related links: 0
- Files updated: `index.md`, `dashboard.md`, `reports/wiki_lint_report.md`
