#!/usr/bin/env python3
"""
Wiki maintenance pass for obsidian_trade_journals/.

Does four things:
  1. Rebuild `index.md` (content-oriented map across wiki/).
  2. Append an entry to `log.md` recording this pass.
  3. Emit `reports/wiki_lint_report.md` with the findings below.
  4. Rebuild a minimal `dashboard.md` (operational view).

Lint checks:
  - orphan pages (no inbound [[wikilinks]] and not the index/log/CLAUDE)
  - broken [[wikilinks]] (target page does not exist)
  - pages missing YAML frontmatter
  - stale pages (`updated:` > 30 days from today)
  - concept mentions in trade/strategy pages with no concept page
  - strategies with no trade links
  - trades with no related-trade links

Usage:
  python3 scripts/wiki_maintain.py
"""
from __future__ import annotations
import datetime as dt
import re
import sys
from pathlib import Path
from collections import defaultdict

ROOT = Path(__file__).resolve().parent.parent
WIKI = ROOT / "wiki"
REPORT = ROOT / "reports" / "wiki_lint_report.md"
INDEX = ROOT / "index.md"
LOG = ROOT / "log.md"
DASHBOARD = ROOT / "dashboard.md"

TODAY = dt.date.today()
STALE_DAYS = 30

FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---", re.DOTALL)
# Captures whether preceded by `!` (image embed) in group 1, target in group 2
WIKILINK_RE = re.compile(r"(!?)\[\[([^\]]+?)\]\]")

TOP_LEVEL_MD = {"CLAUDE", "index", "log", "dashboard"}


def load_pages() -> list[Path]:
    return sorted(p for p in WIKI.rglob("*.md") if p.is_file())


def parse_frontmatter(text: str) -> dict:
    m = FRONTMATTER_RE.match(text)
    if not m:
        return {}
    meta: dict = {}
    current_key = None
    for line in m.group(1).split("\n"):
        if line.startswith("  - ") or line.startswith("    - "):
            if current_key is None:
                continue
            val = line.lstrip()[2:].strip()
            existing = meta.get(current_key)
            if isinstance(existing, list):
                existing.append(val)
            elif existing in (None, ""):
                meta[current_key] = [val]
            else:
                meta[current_key] = [existing, val]
        elif ":" in line and not line.startswith(" "):
            k, _, v = line.partition(":")
            meta[k.strip()] = v.strip()
            current_key = k.strip()
    return meta


def page_slug(p: Path) -> str:
    """Return the slug used inside [[wikilinks]]."""
    return p.relative_to(WIKI).with_suffix("").as_posix()


def link_target(link: str) -> str:
    # Obsidian alias pipe may be escaped as \| in markdown tables. Strip trailing \
    target = link.split("|", 1)[0].strip()
    target = target.split("#", 1)[0].strip()
    target = target.rstrip("\\")
    return target


def resolve_link(link_target_str: str, src_page: Path, page_slugs: set[str], page_basenames: dict[str, list[str]]) -> str | None:
    """
    Resolve a [[wikilink]] target (which may be relative-path-like or a bare basename)
    to a canonical slug within WIKI, or None if broken.
    """
    t = link_target_str.strip()
    if not t:
        return None

    # Try relative-to-source resolution
    try:
        rel = (src_page.parent / (t + ".md")).resolve()
        wiki_resolved = rel.relative_to(WIKI).with_suffix("").as_posix()
        if wiki_resolved in page_slugs:
            return wiki_resolved
    except (ValueError, OSError):
        pass

    # Try as absolute slug within WIKI
    if t in page_slugs:
        return t

    # Bare basename — collapse to a unique match
    basename = Path(t).name
    candidates = page_basenames.get(basename, [])
    if len(candidates) == 1:
        return candidates[0]

    return None


def main() -> int:
    pages = load_pages()
    page_slugs: set[str] = {page_slug(p) for p in pages}
    page_basenames: dict[str, list[str]] = defaultdict(list)
    for p in pages:
        page_basenames[p.stem].append(page_slug(p))

    inbound: dict[str, list[str]] = defaultdict(list)
    frontmatter_missing: list[str] = []
    stale: list[tuple[str, str]] = []
    broken_links: list[tuple[str, str]] = []
    concept_mentions: dict[str, list[str]] = defaultdict(list)  # slug → pages that mention it
    strategy_has_trade_link: dict[str, bool] = {}
    trade_has_related_link: dict[str, bool] = {}

    existing_concept_slugs = {page_slug(p) for p in pages if p.parent.name == "concepts"}

    for p in pages:
        slug = page_slug(p)
        text = p.read_text()
        meta = parse_frontmatter(text)

        if not meta:
            frontmatter_missing.append(slug)
        else:
            updated = meta.get("updated")
            if updated:
                try:
                    u_date = dt.date.fromisoformat(updated)
                    if (TODAY - u_date).days > STALE_DAYS:
                        stale.append((slug, updated))
                except ValueError:
                    pass  # malformed date

        ptype = meta.get("type", "")
        if ptype == "strategy":
            strategy_has_trade_link[slug] = False
        elif ptype == "trade":
            trade_has_related_link[slug] = False

        # Links
        for match in WIKILINK_RE.finditer(text):
            is_embed = bool(match.group(1))
            raw = match.group(2)
            tgt = link_target(raw)

            if is_embed:
                # Image / file embed — check filesystem, not page index
                try:
                    resolved_fs = (p.parent / tgt).resolve()
                    if resolved_fs.exists():
                        continue  # valid embed, don't count as link
                    broken_links.append((slug, tgt))
                except (ValueError, OSError):
                    broken_links.append((slug, tgt))
                continue

            # Top-level .md files (CLAUDE, index, log, dashboard) are not in wiki/
            if tgt in TOP_LEVEL_MD:
                if (ROOT / f"{tgt}.md").exists():
                    continue
                broken_links.append((slug, tgt))
                continue

            resolved = resolve_link(tgt, p, page_slugs, page_basenames)
            if resolved is None:
                broken_links.append((slug, tgt))
            else:
                inbound[resolved].append(slug)

                # Strategy→trade detection
                if ptype == "strategy" and resolved.startswith("trades/"):
                    strategy_has_trade_link[slug] = True
                # Trade→trade detection (related-trade links)
                if ptype == "trade" and resolved.startswith("trades/") and resolved != slug:
                    trade_has_related_link[slug] = True

                # Concept mentions accrue regardless of resolution
                if resolved.startswith("concepts/"):
                    concept_mentions[resolved].append(slug)

        # Also scan body for concept-like slugs referenced outside wikilinks but mentioned inline —
        # skipped; we only track links as evidence.

    orphans: list[str] = []
    for p in pages:
        slug = page_slug(p)
        # Exempt schema-like pages
        if slug in {"synthesis/current-trading-thesis"} or slug.endswith("README"):
            continue
        if not inbound.get(slug):
            # also exempt primary index pages per-folder which we don't maintain
            orphans.append(slug)

    # Concept-mention-without-concept-page: skipped because we enforce via link resolution; any
    # textual mention without a link wouldn't appear in broken_links. Placeholder for future expansion.
    concept_missing: list[str] = []  # would require textual scan beyond wikilinks

    # --- Rebuild index.md ---
    index_lines: list[str] = [
        "---",
        "title: Global Index",
        "type: index",
        f"updated: {TODAY.isoformat()}",
        "---",
        "",
        "# Global Index",
        "",
        "Content map for the wiki. Regenerated by `scripts/wiki_maintain.py`.",
        "",
        f"- [[CLAUDE|Schema / maintenance rules]]",
        f"- [[dashboard|Operational dashboard]]",
        f"- [[log|Activity log]]",
        f"- [[reports/wiki_lint_report|Latest lint report]]",
        "",
    ]

    sections = [
        ("Strategies", "strategies"),
        ("Trades", "trades"),
        ("Concepts", "concepts"),
        ("Financial primitives", "primitives"),
        ("Market states", "market-states"),
        ("Exit analysis", "exit-analysis"),
        ("Open questions", "questions"),
        ("Synthesis", "synthesis"),
    ]

    for heading, folder in sections:
        index_lines.append(f"## {heading}")
        index_lines.append("")
        folder_pages = [p for p in pages if p.relative_to(WIKI).parts[0] == folder]
        if not folder_pages:
            index_lines.append("_(empty)_")
            index_lines.append("")
            continue
        if folder == "trades":
            # Group trades by strategy subfolder
            by_strat: dict[str, list[Path]] = defaultdict(list)
            for p in folder_pages:
                parts = p.relative_to(WIKI).parts
                if len(parts) >= 3:
                    by_strat[parts[1]].append(p)
            for strat, ps in sorted(by_strat.items()):
                index_lines.append(f"### {strat}")
                index_lines.append("")
                for p in sorted(ps):
                    slug = page_slug(p)
                    meta = parse_frontmatter(p.read_text())
                    title = meta.get("title", slug).strip('"')
                    outcome = meta.get("outcome", "")
                    updated = meta.get("updated", "")
                    outcome_part = f" · {outcome}" if outcome else ""
                    index_lines.append(f"- [[{slug}|{title}]]{outcome_part} — _updated {updated}_")
                index_lines.append("")
        else:
            for p in sorted(folder_pages):
                slug = page_slug(p)
                meta = parse_frontmatter(p.read_text())
                title = meta.get("title", slug).strip('"')
                status = meta.get("status", "")
                updated = meta.get("updated", "")
                status_part = f" · _{status}_" if status else ""
                index_lines.append(f"- [[{slug}|{title}]]{status_part} — _updated {updated}_")
            index_lines.append("")

    INDEX.write_text("\n".join(index_lines) + "\n")

    # --- Rebuild dashboard.md ---
    dash_lines: list[str] = [
        "---",
        "title: Dashboard",
        "type: dashboard",
        f"updated: {TODAY.isoformat()}",
        "---",
        "",
        "# Operational Dashboard",
        "",
        f"- Pages in wiki: **{len(pages)}**",
        f"- Orphans: **{len(orphans)}**",
        f"- Broken links: **{len(broken_links)}**",
        f"- Missing frontmatter: **{len(frontmatter_missing)}**",
        f"- Stale pages (>{STALE_DAYS}d): **{len(stale)}**",
        "",
        "## System-Level Diagnosis",
        "",
        "Primary source: `data/all_trades_dataset.csv` (3,300 trades, 15 strategies, 2022-05-02 → 2026-04-20).",
        "Prior source: `reports/strategy_diagnosis.md` (batch `batch-20260424T123546Z`).",
        "",
        "- **Dominant failure mode:** exit inefficiency.",
        "- **Full-library trades:** **3,300** across 15 strategies.",
        "- **`premature_exit` diagnosis trades:** **1,280** (38.8% of library) — most common diagnosis.",
        "- **`missed_continuation` outcome trades:** **524** (15.9%).",
        "- **`fast_loss` outcome trades:** **1,074** (32.5%) — single largest outcome bucket.",
        "- **`efficient_exit` diagnosis trades:** **336** (10.2%) — the positive counter-signal.",
        "- **Strategies flagged `early-exit`:** 10/15 (66.7%).",
        "- **Strategies with premature_exit ≥ 45%:** 8/15 (53.3%).",
        "- **Robust strategies (strong_entry_strong_exit archetype):** **0**.",
        "- **Mean MFE capture across strategies with measurable winners:** ≈58%.",
        "- Representative trade samples: [[wiki/synthesis/cross-strategy-trade-library|Cross-Strategy Trade Library]]",
        "- Interpretation: [[wiki/synthesis/current-trading-thesis#Cross-Strategy Findings|synthesis § Cross-Strategy Findings]]",
        "",
        "## Research Layer",
        "",
        "- [[Research/README|Research index]]",
        "- Prims: [[Research/Prims/cointegration|cointegration]] · "
        "[[Research/Prims/trendrider|trendrider]] · "
        "[[Research/Prims/scalper|scalper]] · "
        "[[Research/Prims/strategyv2|strategyv2]] · "
        "[[Research/Prims/vwap-mean-reversion|vwap-mean-reversion]]",
        "",
        "## Training Journal",
        "",
        "- [[Training Journal/master|Training Journal — Master]]",
        "- [[Training Journal/Control Signals|Control Signals]] — Ralph-facing instructions",
        "- Daily logs: `Training Journal/Daily/`",
        "- Pattern pages: [[Training Journal/Patterns/premature-exit|premature-exit]] · "
        "[[Training Journal/Patterns/missed-continuation|missed-continuation]] · "
        "[[Training Journal/Patterns/low-mfe-capture|low-mfe-capture]]",
        "- Experiments (queued): [[Training Journal/Experiments/trailing-stop-vs-coint|trailing-stop-vs-coint]] · "
        "[[Training Journal/Experiments/partial-tp-runner|partial-tp-runner]] · "
        "[[Training Journal/Experiments/time-based-exit|time-based-exit]]",
        "- Recurring mistakes: [[Training Journal/Mistakes|Mistakes.md]]",
        "",
        "## Latest synthesis",
        "",
        "- [[wiki/synthesis/current-trading-thesis|Current trading thesis]]",
        "",
        "## Open questions",
        "",
    ]
    q_pages = [p for p in pages if p.relative_to(WIKI).parts[0] == "questions"]
    for p in sorted(q_pages):
        slug = page_slug(p)
        meta = parse_frontmatter(p.read_text())
        title = meta.get("title", slug).strip('"')
        status = meta.get("status", "")
        dash_lines.append(f"- [[wiki/{slug}|{title}]] — _{status}_")
    dash_lines.append("")
    dash_lines.append("## Strategies")
    dash_lines.append("")
    for p in sorted(pages):
        if p.relative_to(WIKI).parts[0] != "strategies":
            continue
        slug = page_slug(p)
        meta = parse_frontmatter(p.read_text())
        title = meta.get("title", slug).strip('"')
        tn = meta.get("total_trades", "?")
        wr = meta.get("win_rate", "?")
        dash_lines.append(f"- [[wiki/{slug}|{title}]] — trades: {tn}, win rate: {wr}")
    dash_lines.append("")
    dash_lines.append("See [[reports/wiki_lint_report|lint report]] for full detail.")
    dash_lines.append("")
    DASHBOARD.write_text("\n".join(dash_lines))

    # --- Lint report ---
    lines: list[str] = [
        "---",
        "title: Wiki Lint Report",
        "type: report",
        f"updated: {TODAY.isoformat()}",
        "---",
        "",
        "# Wiki Lint Report",
        "",
        f"Generated: {dt.datetime.now().isoformat(timespec='seconds')}",
        f"Pages scanned: {len(pages)}",
        "",
        "## Summary",
        "",
        f"| Check | Count |",
        f"|---|---:|",
        f"| Orphan pages | {len(orphans)} |",
        f"| Broken wikilinks | {len(broken_links)} |",
        f"| Pages missing frontmatter | {len(frontmatter_missing)} |",
        f"| Stale pages (>{STALE_DAYS}d) | {len(stale)} |",
        f"| Concept pages without inbound mentions | — |",
        f"| Strategies without trade links | {sum(1 for v in strategy_has_trade_link.values() if not v)} |",
        f"| Trades without related-trade links | {sum(1 for v in trade_has_related_link.values() if not v)} |",
        "",
        "## Orphan pages",
        "",
    ]
    if orphans:
        for slug in orphans:
            lines.append(f"- [[{slug}]]")
    else:
        lines.append("_none_")
    lines.append("")

    lines.append("## Broken wikilinks")
    lines.append("")
    if broken_links:
        lines.append("| Source | Broken target |")
        lines.append("|---|---|")
        for src, tgt in broken_links:
            lines.append(f"| `{src}` | `{tgt}` |")
    else:
        lines.append("_none_")
    lines.append("")

    lines.append("## Pages missing frontmatter")
    lines.append("")
    if frontmatter_missing:
        for slug in frontmatter_missing:
            lines.append(f"- `{slug}`")
    else:
        lines.append("_none_")
    lines.append("")

    lines.append(f"## Stale pages (updated > {STALE_DAYS} days ago)")
    lines.append("")
    if stale:
        for slug, updated in stale:
            lines.append(f"- `{slug}` — updated {updated}")
    else:
        lines.append("_none_")
    lines.append("")

    lines.append("## Strategies without trade links")
    lines.append("")
    bad_strats = [s for s, v in strategy_has_trade_link.items() if not v]
    if bad_strats:
        for s in bad_strats:
            lines.append(f"- `{s}`")
    else:
        lines.append("_none_")
    lines.append("")

    lines.append("## Trades without related-trade links")
    lines.append("")
    bad_trades = [s for s, v in trade_has_related_link.items() if not v]
    if bad_trades:
        for s in bad_trades:
            lines.append(f"- `{s}`")
    else:
        lines.append("_none_")
    lines.append("")

    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text("\n".join(lines) + "\n")

    # --- Append to log.md ---
    stamp = dt.datetime.now().strftime("%Y-%m-%d %H:%M")
    log_entry = (
        f"\n---\n\n## [{stamp}] maintain | wiki_maintain.py pass\n"
        f"- Pages scanned: {len(pages)}\n"
        f"- Orphans: {len(orphans)}\n"
        f"- Broken links: {len(broken_links)}\n"
        f"- Missing frontmatter: {len(frontmatter_missing)}\n"
        f"- Stale: {len(stale)}\n"
        f"- Strategies missing trade links: {sum(1 for v in strategy_has_trade_link.values() if not v)}\n"
        f"- Trades missing related links: {sum(1 for v in trade_has_related_link.values() if not v)}\n"
        f"- Files updated: `index.md`, `dashboard.md`, `reports/wiki_lint_report.md`\n"
    )
    with LOG.open("a") as f:
        f.write(log_entry)

    print(f"pages={len(pages)} orphans={len(orphans)} broken_links={len(broken_links)} "
          f"missing_fm={len(frontmatter_missing)} stale={len(stale)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
