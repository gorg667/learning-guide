#!/usr/bin/env python3
"""
validate.py — stdlib-only sanity checks for the guide.

Checks:
  * every content/NN-slug.md has front matter with title, part, summary
  * chapter numbers are unique and sequential
  * no chapter is suspiciously short (< 400 words) unless it declares `short: true`
  * headings start at H2 inside chapters (H1 is generated from the title)
  * internal links ([text](NN-slug.md) or (slug.html)) resolve to real chapters
  * the generated site/LEARNING_GUIDE.md are fresh (build hash matches)
  * generated HTML files exist for every chapter

Exit code 0 = OK, 1 = problems found.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build  # noqa: E402

ROOT = Path(__file__).resolve().parent
problems: list[str] = []
warnings: list[str] = []


def main() -> int:
    chapters = build.load_chapters()
    if not chapters:
        problems.append("no chapters in content/")
        return report()

    nums = [c.number for c in chapters]
    if len(set(nums)) != len(nums):
        problems.append(f"duplicate chapter numbers: {nums}")
    if nums != list(range(nums[0], nums[0] + len(nums))):
        warnings.append(f"chapter numbers not contiguous: {nums}")

    slugs = {c.slug for c in chapters}
    filenames = {c.path.name for c in chapters}

    for c in chapters:
        if not c.title:
            problems.append(f"{c.path.name}: missing title")
        if not c.part:
            problems.append(f"{c.path.name}: missing part")
        if not c.summary:
            problems.append(f"{c.path.name}: missing summary")
        meta, _ = build.parse_front_matter(c.path.read_text(encoding="utf-8"))
        if c.words < 400 and meta.get("short", "false").lower() != "true":
            problems.append(f"{c.path.name}: only {c.words} words (looks unfinished)")
        for i, line in enumerate(c.body_md.splitlines(), 1):
            if re.match(r"^#\s", line):
                problems.append(f"{c.path.name}:{i}: H1 inside chapter body (use ## and below)")
            if "TODO" in line or "TKTK" in line:
                problems.append(f"{c.path.name}:{i}: leftover TODO marker")
        # links
        for m in re.finditer(r"\]\(([^)\s#]+)(#[^)]*)?\)", c.body_md):
            href = m.group(1)
            if href.startswith(("http://", "https://", "mailto:")):
                continue
            if href.endswith(".md"):
                if Path(href).name not in filenames:
                    problems.append(f"{c.path.name}: broken link to {href}")
            elif href.endswith(".html"):
                if Path(href).stem not in slugs | {"index", "full"}:
                    problems.append(f"{c.path.name}: broken link to {href}")
        # unbalanced fences
        if c.body_md.count("```") % 2:
            problems.append(f"{c.path.name}: unbalanced code fence")

    # generated outputs
    site = ROOT / "site"
    for c in chapters:
        if not (site / f"{c.slug}.html").exists():
            problems.append(f"site/{c.slug}.html missing — run build.py")
    for f in ("index.html", "full.html", "search.json"):
        if not (site / f).exists():
            problems.append(f"site/{f} missing — run build.py")
    if not (ROOT / "LEARNING_GUIDE.md").exists():
        problems.append("LEARNING_GUIDE.md missing — run build.py")
    h = site / ".build-hash"
    if h.exists():
        if h.read_text().strip() != build.content_hash(chapters):
            problems.append("generated files are stale — run build.py")
    else:
        problems.append("site/.build-hash missing — run build.py")

    total = sum(c.words for c in chapters)
    print(f"{len(chapters)} chapters, {total:,} words")
    return report()


def report() -> int:
    for w in warnings:
        print("WARN ", w)
    for p in problems:
        print("ERROR", p)
    if problems:
        print(f"\n{len(problems)} problem(s).")
        return 1
    print("OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
