#!/usr/bin/env python3
"""
Generate wiki/synthesis/cross-strategy-trade-library.md from data/all_trades_dataset.csv.

Scope constraints (per ingest task):
  - 3300 trades, 15 strategies, 4 years of BTC + other pairs
  - Do not run backtests or compute new metrics beyond grouping/summarising CSV fields
  - Do not embed all charts; select representative top-10 per section
  - Chart paths are taken verbatim from the CSV `chart_path` column

Sections produced:
  - Overview (totals + distributions)
  - Wins (clean_win + noisy_win)
  - Losses (fast_loss + slow_loss + bad_entry_good_idea + scratch)
  - Premature Exits (exit_diagnosis = premature_exit)
  - Missed Continuations (outcome OR exit_diagnosis = missed_continuation)
  - Stop Loss Failures (exit_diagnosis = stop_loss_failure)

Selection rules are stated inside each section so the reader knows what "top 10" means.
"""
from __future__ import annotations
import csv
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CSV_PATH = ROOT.parent / "data" / "all_trades_dataset.csv"
OUT_PATH = ROOT / "wiki" / "synthesis" / "cross-strategy-trade-library.md"

# Path from wiki/synthesis/*.md to Yuji Project root is "../../..", then into data/
CHART_REL_PREFIX = "../../../data"


def load_rows() -> list[dict]:
    with CSV_PATH.open() as f:
        rdr = csv.DictReader(f)
        rows = list(rdr)
    # Coerce numerics
    for r in rows:
        for k in ("profit_ratio", "mfe_pct", "mae_pct", "profit_abs",
                 "open_rate", "close_rate", "min_rate", "max_rate", "trade_duration_min"):
            try:
                r[k] = float(r[k])
            except (ValueError, KeyError, TypeError):
                r[k] = 0.0
    return rows


def fmt_pct(v: float) -> str:
    return f"{v*100:+.2f}%" if abs(v) < 5 else f"{v*100:+.1f}%"


def fmt_mfe(v: float) -> str:
    return f"{v*100:.2f}%"


def trade_row(idx: int, r: dict) -> str:
    """Emit one 'row' = a trade entry with chart embed + fields + one mechanical sentence."""
    pr = r["profit_ratio"]
    mfe = r["mfe_pct"]
    mae = r["mae_pct"]
    chart = f"{CHART_REL_PREFIX}/{r['chart_path']}"
    # Build mechanical explanation using only CSV fields
    diag = r["exit_diagnosis"] or "unclassified"
    outcome = r["outcome"] or "unclassified"

    if diag == "premature_exit":
        expl = (f"Trade reached +{fmt_mfe(mfe)} MFE but closed at {fmt_pct(pr)}, "
                f"so capture was low and is classified as premature_exit.")
    elif diag == "missed_continuation" or outcome == "missed_continuation":
        expl = (f"Trade closed at {fmt_pct(pr)} against a peak MFE of +{fmt_mfe(mfe)}; "
                f"labelled missed_continuation because the favourable excursion extended well "
                f"beyond the realised exit.")
    elif diag == "stop_loss_failure":
        expl = (f"Trade closed at {fmt_pct(pr)} with MAE of -{fmt_mfe(abs(mae))}; "
                f"labelled stop_loss_failure because the stop exit did not contain the adverse move.")
    elif diag == "efficient_exit":
        expl = (f"Trade closed at {fmt_pct(pr)} near the MFE of +{fmt_mfe(mfe)}; "
                f"labelled efficient_exit — exit captured most of the favourable move.")
    elif diag == "poor_entry":
        expl = (f"Trade closed at {fmt_pct(pr)} with MFE +{fmt_mfe(mfe)} and MAE -{fmt_mfe(abs(mae))}; "
                f"labelled poor_entry because adverse excursion matched or exceeded favourable excursion.")
    elif diag == "noise_trade":
        expl = (f"Trade closed at {fmt_pct(pr)}; MFE +{fmt_mfe(mfe)} / MAE -{fmt_mfe(abs(mae))} "
                f"produced no decisive direction — labelled noise_trade.")
    elif outcome == "fast_loss":
        expl = (f"Trade closed at {fmt_pct(pr)} with MAE -{fmt_mfe(abs(mae))} reached quickly "
                f"(duration {int(r['trade_duration_min'])//60}h); labelled fast_loss.")
    elif outcome == "slow_loss":
        expl = (f"Trade closed at {fmt_pct(pr)} with MAE -{fmt_mfe(abs(mae))} over "
                f"{int(r['trade_duration_min'])//60}h; labelled slow_loss.")
    elif outcome == "scratch":
        expl = (f"Trade closed at {fmt_pct(pr)} with small MFE +{fmt_mfe(mfe)} / MAE -{fmt_mfe(abs(mae))}; "
                f"labelled scratch.")
    elif outcome == "clean_win":
        expl = (f"Trade closed at {fmt_pct(pr)} with MFE +{fmt_mfe(mfe)} and shallow MAE "
                f"-{fmt_mfe(abs(mae))}; labelled clean_win.")
    elif outcome == "noisy_win":
        expl = (f"Trade closed at {fmt_pct(pr)} with MFE +{fmt_mfe(mfe)} but MAE -{fmt_mfe(abs(mae))}; "
                f"labelled noisy_win because the path was volatile before closing positive.")
    else:
        expl = f"Trade closed at {fmt_pct(pr)} / MFE +{fmt_mfe(mfe)} / MAE -{fmt_mfe(abs(mae))}."

    lines = [
        f"### {idx}. {r['strategy']} — {r['pair']} · {fmt_pct(pr)}",
        "",
        f"![{r['strategy']} {r['pair']} {fmt_pct(pr)}]({chart})",
        "",
        f"| Field | Value |",
        f"|---|---|",
        f"| strategy | `{r['strategy']}` |",
        f"| pair | {r['pair']} |",
        f"| open_date | {r['open_date']} |",
        f"| close_date | {r['close_date']} |",
        f"| profit_ratio | {fmt_pct(pr)} |",
        f"| MFE | +{fmt_mfe(mfe)} |",
        f"| MAE | -{fmt_mfe(abs(mae))} |",
        f"| exit_reason | `{r['exit_reason']}` |",
        f"| outcome | `{outcome}` |",
        f"| exit_diagnosis | `{diag}` |",
        "",
        f"> {expl}",
        "",
    ]
    return "\n".join(lines)


def section_intro(title: str, rule: str, n_pool: int, n_shown: int) -> list[str]:
    return [
        f"## {title}",
        "",
        f"- **Pool size:** {n_pool} trades",
        f"- **Selection rule:** {rule}",
        f"- **Showing:** top {n_shown} representative trades",
        "",
    ]


def build_page(rows: list[dict]) -> str:
    n = len(rows)
    strategies = sorted({r["strategy"] for r in rows})
    outcomes = Counter(r["outcome"] for r in rows)
    diag = Counter(r["exit_diagnosis"] for r in rows)
    pairs = Counter(r["pair"] for r in rows)
    dates = [r["open_date"][:10] for r in rows if r["open_date"]]
    date_min, date_max = min(dates), max(dates)

    lines: list[str] = [
        "---",
        "title: Cross-Strategy Trade Library",
        "type: synthesis",
        "updated: 2026-04-25",
        "status: active",
        "cross_strategy_source: data/all_trades_dataset.csv (3300 trades, 15 strategies)",
        f"total_trades: {n}",
        "---",
        "",
        "# Cross-Strategy Trade Library",
        "",
        "A summarised, representative-sample view over the full 3,300-trade dataset exported from",
        "Ben's all-trades build. **This page does not re-run backtests or derive new metrics — it",
        "only groups, counts, and embeds trades using fields already present in",
        "`data/all_trades_dataset.csv`.**",
        "",
        "Chart images are embedded via filesystem-relative paths into `data/all_trade_charts/` —",
        "not moved into `raw/`. The full dataset stays in `data/` as Ben's build produced it.",
        "",
        "---",
        "",
        "## Overview",
        "",
        f"- **Total trades:** {n:,}",
        f"- **Strategies:** {len(strategies)}",
        f"- **Pairs:** {len(pairs)} — top 5 by volume: "
        + ", ".join(f"{p} ({c})" for p, c in pairs.most_common(5)),
        f"- **Date span (open_date):** {date_min} → {date_max}",
        "",
        "### Outcome distribution",
        "",
        "| Outcome | Count | % |",
        "|---|---:|---:|",
    ]
    for k, v in outcomes.most_common():
        lines.append(f"| `{k}` | {v:,} | {100*v/n:.1f}% |")
    lines.append("")

    lines += [
        "### Exit diagnosis distribution",
        "",
        "| Diagnosis | Count | % |",
        "|---|---:|---:|",
    ]
    for k, v in diag.most_common():
        lines.append(f"| `{k}` | {v:,} | {100*v/n:.1f}% |")
    lines.append("")

    lines += [
        "### Strategies",
        "",
        "| Strategy | Trades |",
        "|---|---:|",
    ]
    strat_counts = Counter(r["strategy"] for r in rows)
    for s, c in strat_counts.most_common():
        lines.append(f"| `{s}` | {c:,} |")
    lines.append("")

    # --- Section: Wins ---
    wins = [r for r in rows if r["outcome"] in ("clean_win", "noisy_win")]
    wins.sort(key=lambda r: r["profit_ratio"], reverse=True)
    win_sample = _diversify(wins, "strategy", n_target=10)
    lines += section_intro(
        "Wins",
        "Union of `outcome ∈ {clean_win, noisy_win}`, ranked by `profit_ratio` "
        "descending with strategy-diversity picking (no strategy may appear twice until "
        "every strategy with a win has been represented once).",
        len(wins),
        len(win_sample),
    )
    lines.append(f"**clean_win:** {outcomes.get('clean_win', 0):,} · "
                 f"**noisy_win:** {outcomes.get('noisy_win', 0):,}")
    lines.append("")
    for i, r in enumerate(win_sample, 1):
        lines.append(trade_row(i, r))

    # --- Section: Losses ---
    losses = [r for r in rows if r["outcome"] in ("fast_loss", "slow_loss",
                                                   "bad_entry_good_idea", "scratch")]
    losses.sort(key=lambda r: r["profit_ratio"])  # most-negative first
    loss_sample = _diversify(losses, "strategy", n_target=10)
    lines += section_intro(
        "Losses",
        "Union of `outcome ∈ {fast_loss, slow_loss, bad_entry_good_idea, scratch}`, "
        "ranked by `profit_ratio` ascending (largest losses first) with strategy-diversity picking.",
        len(losses),
        len(loss_sample),
    )
    lines.append(f"**fast_loss:** {outcomes.get('fast_loss', 0):,} · "
                 f"**slow_loss:** {outcomes.get('slow_loss', 0):,} · "
                 f"**bad_entry_good_idea:** {outcomes.get('bad_entry_good_idea', 0):,} · "
                 f"**scratch:** {outcomes.get('scratch', 0):,}")
    lines.append("")
    for i, r in enumerate(loss_sample, 1):
        lines.append(trade_row(i, r))

    # --- Section: Premature Exits ---
    prem = [r for r in rows if r["exit_diagnosis"] == "premature_exit"]
    # Rank by realised-vs-MFE gap (two-field subtraction, not a new metric)
    prem.sort(key=lambda r: (r["mfe_pct"] - r["profit_ratio"]), reverse=True)
    prem_sample = _diversify(prem, "strategy", n_target=10)
    lines += section_intro(
        "Premature Exits",
        "`exit_diagnosis = premature_exit`, ranked by `mfe_pct − profit_ratio` descending "
        "(largest unrealised gap first) with strategy-diversity picking. "
        "Note: the ranking key is a subtraction of two existing CSV fields, not a new metric.",
        len(prem),
        len(prem_sample),
    )
    for i, r in enumerate(prem_sample, 1):
        lines.append(trade_row(i, r))

    # --- Section: Missed Continuations ---
    missed = [r for r in rows
              if r["outcome"] == "missed_continuation"
              or r["exit_diagnosis"] == "missed_continuation"]
    missed.sort(key=lambda r: r["mfe_pct"], reverse=True)
    missed_sample = _diversify(missed, "strategy", n_target=10)
    lines += section_intro(
        "Missed Continuations",
        "`outcome = missed_continuation` OR `exit_diagnosis = missed_continuation` (union), "
        "ranked by `mfe_pct` descending with strategy-diversity picking.",
        len(missed),
        len(missed_sample),
    )
    lines.append(
        f"**outcome=missed_continuation:** {outcomes.get('missed_continuation', 0):,} · "
        f"**exit_diagnosis=missed_continuation:** {diag.get('missed_continuation', 0):,} · "
        f"**union (unique trades):** {len(missed):,}"
    )
    lines.append("")
    for i, r in enumerate(missed_sample, 1):
        lines.append(trade_row(i, r))

    # --- Section: Stop Loss Failures ---
    sl = [r for r in rows if r["exit_diagnosis"] == "stop_loss_failure"]
    sl.sort(key=lambda r: r["mae_pct"])  # most-negative MAE first
    sl_sample = _diversify(sl, "strategy", n_target=10)
    lines += section_intro(
        "Stop Loss Failures",
        "`exit_diagnosis = stop_loss_failure`, ranked by `mae_pct` ascending "
        "(deepest adverse excursion first) with strategy-diversity picking.",
        len(sl),
        len(sl_sample),
    )
    for i, r in enumerate(sl_sample, 1):
        lines.append(trade_row(i, r))

    # --- Footer: links to trade groups ---
    lines += [
        "---",
        "",
        "## Chart path index (by strategy)",
        "",
        "All charts live under `data/all_trade_charts/<Strategy>/`. "
        "Per-strategy counts:",
        "",
    ]
    for s, c in strat_counts.most_common():
        lines.append(f"- `{CHART_REL_PREFIX}/all_trade_charts/{s}/` — {c:,} charts")
    lines.append("")

    lines += [
        "## Related wiki pages",
        "",
        "- [[current-trading-thesis|Current trading thesis]] (cross-strategy findings + archetypes)",
        "- [[../concepts/missed-continuation|Missed Continuation]] (concept · evidence updated to full library)",
        "- [[../concepts/mfe-capture-ratio|MFE Capture Ratio]] (concept · evidence updated to full library)",
        "- [[../exit-analysis/premature-exit|premature_exit]] (exit diagnosis · evidence updated to full library)",
        "- [[../exit-analysis/coint-z-reverted|coint_z_reverted]] (exit reason · Coint strategy)",
        "",
    ]

    return "\n".join(lines) + "\n"


def _diversify(pool: list[dict], key: str, n_target: int) -> list[dict]:
    """
    Select up to n_target items from `pool` preserving the pool's existing ordering
    but ensuring each distinct `key` value appears before any repeats are allowed.
    """
    seen_once: set[str] = set()
    first_pass: list[dict] = []
    remainder: list[dict] = []
    for r in pool:
        k = r[key]
        if k not in seen_once:
            first_pass.append(r)
            seen_once.add(k)
        else:
            remainder.append(r)
    combined = first_pass + remainder
    return combined[:n_target]


def main() -> int:
    rows = load_rows()
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUT_PATH.write_text(build_page(rows))
    print(f"wrote {OUT_PATH} ({len(rows)} trades summarised)")
    return 0


if __name__ == "__main__":
    import sys
    sys.exit(main())
