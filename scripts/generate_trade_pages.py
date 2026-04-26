#!/usr/bin/env python3
"""
One-off generator that rewrites v1 trade pages into the Karpathy-style wiki layout.

Reads: raw/journals/<Strat>-YYYYMMDD/trades/trade_NNNN.md (v1 format, already no-lookahead-safe)
Writes: wiki/trades/<Strat>/trade_NNNN.md (v2 format with concept/primitive/exit backlinks)

Runs for YujiCointegrationResidualReversionStrategy only. Safe to re-run — overwrites.
"""
from __future__ import annotations
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
STRAT = "YujiCointegrationResidualReversionStrategy"
SRC_DIR = ROOT / "raw" / "journals" / f"{STRAT}-20260424" / "trades"
DST_DIR = ROOT / "wiki" / "trades" / STRAT
CHART_DIR_REL = f"../../../raw/charts/{STRAT}"

OUTCOME_TO_CONCEPT = {
    "missed_continuation": "missed-continuation",
    "slow_loss": "slow-loss",
    "noisy_win": "noisy-win",
    "bad_entry_good_idea": "bad-entry-good-idea",
    "clean_win": "clean-win",
}

EXIT_DIAG_TO_PAGE = {
    "premature_exit": "premature-exit",
    "efficient_exit": "efficient-exit",
    "poor_entry": "poor-entry",
    "missed_continuation": None,  # maps to concept, already covered
}

# Inferred market-state from v1 per-trade snapshot text
def infer_market_state_pages(trend: str, vol: str) -> list[str]:
    pages: list[str] = []
    t = (trend or "").lower()
    v = (vol or "").lower()
    if "downtrend" in t or "ema20<50<200" in t:
        pages.append("trending-down")
    elif "uptrend" in t or "ema20>50>200" in t:
        pages.append("trending-up")
    else:
        pages.append("ranging")
    if "compression" in v:
        pages.append("compression")
    elif "expansion" in v or "high" in v:
        pages.append("high-volatility")
    return pages


FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)


def parse_frontmatter(text: str) -> tuple[dict, str]:
    m = FRONTMATTER_RE.match(text)
    if not m:
        return {}, text
    meta_raw = m.group(1)
    body = text[m.end():]
    meta: dict = {}
    current_key = None
    for line in meta_raw.split("\n"):
        if line.startswith("  - "):
            meta.setdefault(current_key, []).append(line[4:].strip())
        elif ":" in line and not line.startswith(" "):
            k, _, v = line.partition(":")
            k = k.strip()
            v = v.strip()
            if v == "":
                current_key = k
                meta[k] = []
            else:
                meta[k] = v
                current_key = k
    return meta, body


def extract_value(body: str, pattern: str) -> str | None:
    m = re.search(pattern, body)
    return m.group(1).strip() if m else None


def build_trade_page(src_md: Path, idx: int) -> str:
    raw = src_md.read_text()
    meta, body = parse_frontmatter(raw)

    pair = meta.get("pair", "?/?")
    open_date = meta.get("open_date", meta.get("date", "?"))
    close_date = meta.get("close_date", "?")
    profit_ratio = meta.get("profit_ratio", "0")
    outcome = meta.get("outcome", "unknown")
    exit_reason = meta.get("exit_reason", "unknown")
    exit_diag = meta.get("exit_diagnosis", "unknown")
    tags = meta.get("tags", []) if isinstance(meta.get("tags"), list) else []

    try:
        pnl_pct = float(profit_ratio) * 100
    except (TypeError, ValueError):
        pnl_pct = 0.0

    trend = extract_value(body, r"Trend at prior bar: ([^\n]+?)\.")
    vol = extract_value(body, r"Volatility regime \(20b vs 50b range\): ([^\n]+?)\.")
    vol_ratio = extract_value(body, r"Entry-bar volume vs trailing 20-bar avg: ([^\n]+?)\.")

    # Concept backlinks
    concept_slug = OUTCOME_TO_CONCEPT.get(outcome)
    exit_page = EXIT_DIAG_TO_PAGE.get(exit_diag)
    state_pages = infer_market_state_pages(trend or "", vol or "")

    # Build frontmatter
    fm_lines = [
        "---",
        f'title: "Trade {idx:04d} — {pair}"',
        "type: trade",
        f"strategy: {STRAT}",
        f"pair: {pair}",
        f"open_date: {open_date}",
        f"close_date: {close_date}",
        f"profit_ratio: {profit_ratio}",
        f"outcome: {outcome}",
        f"exit_reason: {exit_reason}",
        f"exit_diagnosis: {exit_diag}",
        "updated: 2026-04-25",
        "status: active",
        "tags:",
    ]
    for t in tags:
        fm_lines.append(f"  - {t}")
    fm_lines.append("---")
    fm = "\n".join(fm_lines) + "\n"

    # Build backlinks section
    backlinks = ["## Wiki links", ""]
    backlinks.append(f"- **Strategy**: [[../../strategies/{STRAT}]]")
    if concept_slug:
        backlinks.append(f"- **Outcome concept**: [[../../concepts/{concept_slug}|{outcome}]]")
    if exit_page:
        backlinks.append(f"- **Exit diagnosis**: [[../../exit-analysis/{exit_page}|{exit_diag}]]")
    backlinks.append(f"- **Exit reason**: [[../../exit-analysis/coint-z-reverted|{exit_reason}]]")
    backlinks.append("- **Signal family**: [[../../concepts/mean-reversion]]")
    if state_pages:
        state_links = ", ".join(f"[[../../market-states/{p}]]" for p in state_pages)
        backlinks.append(f"- **Inferred market states at entry** (pre-Phase-1, provisional): {state_links}")
    backlinks.append("- **Primitives (signal-level unavailable in v1)**: [[../../primitives/bollinger-squeeze-breakout]]")
    backlinks.append("")

    # Chart embed with correct relative path into raw/
    chart_line = f"![[{CHART_DIR_REL}/trade_{idx:04d}.png]]"

    # Rewrite body: replace the v1 chart embed with the new path and inject backlinks above body
    body = re.sub(r"!\[\[trade_\d{4}\.png\]\]", chart_line, body)

    # Related trades section from v1 references v1 filenames (trade_NNNN). Those still work
    # because we place new pages in the same folder. Nothing to change.

    return fm + "\n" + "\n".join(backlinks) + body


def main() -> int:
    DST_DIR.mkdir(parents=True, exist_ok=True)
    files = sorted(SRC_DIR.glob("trade_*.md"))
    if not files:
        print(f"No source trade files at {SRC_DIR}", file=sys.stderr)
        return 1

    created = 0
    for f in files:
        m = re.match(r"trade_(\d+)\.md$", f.name)
        if not m:
            continue
        idx = int(m.group(1))
        out_path = DST_DIR / f"trade_{idx:04d}.md"
        out_path.write_text(build_trade_page(f, idx))
        created += 1

    print(f"Wrote {created} trade pages to {DST_DIR}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
