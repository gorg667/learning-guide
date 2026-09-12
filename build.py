#!/usr/bin/env python3
"""
build.py — zero-dependency site + Markdown-book builder.

Reads content/NN-slug.md (with a small front-matter block), and produces:

  site/index.html          landing page with table of contents
  site/<slug>.html         one page per chapter (prev/next nav, sidebar TOC)
  site/full.html           the whole guide on one page
  site/search.json         tiny search index (title, summary, headings)
  LEARNING_GUIDE.md        single Markdown adaptation of the whole guide

Stdlib only. Run:  python3 build.py
"""
from __future__ import annotations

import hashlib
import html
import json
import os
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

ROOT = Path(__file__).resolve().parent
CONTENT = ROOT / "content"
SITE = ROOT / "site"
ASSETS = SITE / "assets"
BOOK = ROOT / "LEARNING_GUIDE.md"

SITE_TITLE = "Learning How to Learn"
SITE_TAGLINE = "The comprehensive, evidence-based guide to maximizing your ability to learn anything"

# ----------------------------------------------------------------------------
# Front matter
# ----------------------------------------------------------------------------

@dataclass
class Chapter:
    path: Path
    number: int
    slug: str
    title: str
    part: str
    summary: str
    body_md: str
    body_html: str = ""
    headings: list = field(default_factory=list)  # (level, text, id)
    words: int = 0


def parse_front_matter(text: str) -> tuple[dict, str]:
    if not text.startswith("---"):
        return {}, text
    end = text.find("\n---", 3)
    if end == -1:
        return {}, text
    block = text[3:end].strip("\n")
    meta = {}
    for line in block.splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            meta[k.strip()] = v.strip().strip('"').strip("'")
    body = text[end + 4 :].lstrip("\n")
    return meta, body


# ----------------------------------------------------------------------------
# Inline Markdown
# ----------------------------------------------------------------------------

_CODE_SPAN = re.compile(r"`([^`]+)`")
_STRONG = re.compile(r"\*\*(.+?)\*\*")
_EM = re.compile(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])")
_EM_US = re.compile(r"(?<![\w_])_(?!\s)(.+?)(?<!\s)_(?![\w_])")
_LINK = re.compile(r"\[([^\]]+)\]\(([^)\s]+)(?:\s+\"([^\"]*)\")?\)")
_AUTOLINK = re.compile(r"(?<![\(\"'>])(https?://[^\s<)\]]+)")
_FOOTREF = re.compile(r"\[\^([^\]]+)\]")


def slugify(text: str) -> str:
    text = re.sub(r"<[^>]+>", "", text)
    text = html.unescape(text)
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s-]", "", text)
    text = re.sub(r"[\s-]+", "-", text).strip("-")
    return text or "section"


def render_inline(text: str) -> str:
    """Convert inline markdown to HTML. Protects code spans first."""
    placeholders: list[str] = []

    def stash(m: re.Match) -> str:
        placeholders.append(f"<code>{html.escape(m.group(1))}</code>")
        return f"\x00{len(placeholders) - 1}\x00"

    text = _CODE_SPAN.sub(stash, text)
    text = html.escape(text, quote=False)

    def link(m: re.Match) -> str:
        label, href, title = m.group(1), m.group(2), m.group(3)
        href = href.replace("&amp;", "&")
        # Convert internal chapter links: NN-slug.md -> slug.html
        if href.endswith(".md") and not href.startswith("http"):
            stem = Path(href).stem
            stem = re.sub(r"^\d+-", "", stem)
            href = stem + ".html"
        t = f' title="{html.escape(title)}"' if title else ""
        ext = ' target="_blank" rel="noopener"' if href.startswith("http") else ""
        return f'<a href="{href}"{t}{ext}>{label}</a>'

    text = _LINK.sub(link, text)
    text = _AUTOLINK.sub(lambda m: f'<a href="{m.group(1)}" target="_blank" rel="noopener">{m.group(1)}</a>', text)
    text = _STRONG.sub(r"<strong>\1</strong>", text)
    text = _EM.sub(r"<em>\1</em>", text)
    text = _EM_US.sub(r"<em>\1</em>", text)
    text = _FOOTREF.sub(r'<sup class="fn"><a href="#fn-\1" id="fnref-\1">\1</a></sup>', text)
    # smart-ish typography
    text = text.replace(" -- ", " — ").replace("(c)", "©")

    def unstash(m: re.Match) -> str:
        return placeholders[int(m.group(1))]

    return re.sub(r"\x00(\d+)\x00", unstash, text)


# ----------------------------------------------------------------------------
# Block Markdown
# ----------------------------------------------------------------------------

_H = re.compile(r"^(#{1,6})\s+(.*?)\s*#*\s*$")
_HR = re.compile(r"^(?:-{3,}|\*{3,}|_{3,})\s*$")
_UL = re.compile(r"^(\s*)[-*+]\s+(.*)$")
_OL = re.compile(r"^(\s*)(\d+)[.)]\s+(.*)$")
_TABLE_SEP = re.compile(r"^\s*\|?\s*:?-+:?\s*(\|\s*:?-+:?\s*)*\|?\s*$")
_FOOTDEF = re.compile(r"^\[\^([^\]]+)\]:\s+(.*)$")
_CALLOUT = re.compile(r"^\[!(NOTE|TIP|WARNING|IMPORTANT|KEY|EXAMPLE|RESEARCH|PRACTICE)\]\s*(.*)$", re.I)


class MDRenderer:
    def __init__(self, heading_offset: int = 0, id_prefix: str = ""):
        self.heading_offset = heading_offset
        self.id_prefix = id_prefix
        self.headings: list[tuple[int, str, str]] = []
        self.footnotes: list[tuple[str, str]] = []
        self._ids: set[str] = set()

    def unique_id(self, base: str) -> str:
        i = base
        n = 2
        while i in self._ids:
            i = f"{base}-{n}"
            n += 1
        self._ids.add(i)
        return i

    def render(self, md: str) -> str:
        lines = md.replace("\r\n", "\n").split("\n")
        out: list[str] = []
        i = 0
        n = len(lines)
        while i < n:
            line = lines[i]

            if not line.strip():
                i += 1
                continue

            # fenced code
            if line.startswith("```"):
                lang = line[3:].strip()
                j = i + 1
                buf = []
                while j < n and not lines[j].startswith("```"):
                    buf.append(lines[j])
                    j += 1
                cls = f' class="language-{html.escape(lang)}"' if lang else ""
                out.append(f"<pre><code{cls}>{html.escape(chr(10).join(buf))}</code></pre>")
                i = j + 1
                continue

            # heading
            m = _H.match(line)
            if m:
                level = min(6, len(m.group(1)) + self.heading_offset)
                text = m.group(2)
                hid = self.unique_id(self.id_prefix + slugify(text))
                self.headings.append((level, text, hid))
                out.append(f'<h{level} id="{hid}">{render_inline(text)}<a class="anchor" href="#{hid}" aria-label="link to section">#</a></h{level}>')
                i += 1
                continue

            # hr
            if _HR.match(line):
                out.append("<hr>")
                i += 1
                continue

            # footnote definition
            m = _FOOTDEF.match(line)
            if m:
                key, text = m.group(1), m.group(2)
                j = i + 1
                while j < n and lines[j].startswith("    "):
                    text += " " + lines[j].strip()
                    j += 1
                self.footnotes.append((key, text))
                i = j
                continue

            # blockquote / callout
            if line.startswith(">"):
                j = i
                buf = []
                while j < n and (lines[j].startswith(">") or (lines[j].strip() and buf and not lines[j].startswith(("#", "```")) and lines[j - 1].startswith(">") and False)):
                    buf.append(re.sub(r"^>\s?", "", lines[j]))
                    j += 1
                inner_md = "\n".join(buf)
                cm = _CALLOUT.match(inner_md.strip().split("\n")[0])
                if cm:
                    kind = cm.group(1).lower()
                    first_rest = cm.group(2)
                    rest_lines = inner_md.split("\n")[1:]
                    body = ("\n".join(([first_rest] if first_rest else []) + rest_lines)).strip()
                    sub = MDRenderer(self.heading_offset, self.id_prefix)
                    sub._ids = self._ids
                    inner = sub.render(body)
                    self.footnotes.extend(sub.footnotes)
                    label = {"note": "Note", "tip": "Tip", "warning": "Warning", "important": "Important",
                             "key": "Key idea", "example": "Example", "research": "What the research says",
                             "practice": "Try this"}[kind]
                    out.append(f'<div class="callout callout-{kind}"><div class="callout-title">{label}</div>{inner}</div>')
                else:
                    sub = MDRenderer(self.heading_offset, self.id_prefix)
                    sub._ids = self._ids
                    inner = sub.render(inner_md)
                    self.footnotes.extend(sub.footnotes)
                    out.append(f"<blockquote>{inner}</blockquote>")
                i = j
                continue

            # table
            if "|" in line and i + 1 < n and _TABLE_SEP.match(lines[i + 1]):
                header = self._split_row(line)
                aligns = []
                for cell in self._split_row(lines[i + 1]):
                    c = cell.strip()
                    if c.startswith(":") and c.endswith(":"):
                        aligns.append("center")
                    elif c.endswith(":"):
                        aligns.append("right")
                    else:
                        aligns.append("left")
                j = i + 2
                rows = []
                while j < n and "|" in lines[j] and lines[j].strip():
                    rows.append(self._split_row(lines[j]))
                    j += 1
                t = ['<div class="table-wrap"><table>', "<thead><tr>"]
                for k, h in enumerate(header):
                    a = aligns[k] if k < len(aligns) else "left"
                    t.append(f'<th style="text-align:{a}">{render_inline(h.strip())}</th>')
                t.append("</tr></thead><tbody>")
                for r in rows:
                    t.append("<tr>")
                    for k in range(len(header)):
                        cell = r[k] if k < len(r) else ""
                        a = aligns[k] if k < len(aligns) else "left"
                        t.append(f'<td style="text-align:{a}">{render_inline(cell.strip())}</td>')
                    t.append("</tr>")
                t.append("</tbody></table></div>")
                out.append("".join(t))
                i = j
                continue

            # lists
            if _UL.match(line) or _OL.match(line):
                block, i = self._collect_list(lines, i)
                out.append(self._render_list(block))
                continue

            # paragraph
            j = i
            buf = []
            while j < n and lines[j].strip() and not _H.match(lines[j]) and not lines[j].startswith(("```", ">")) \
                    and not _HR.match(lines[j]) and not _UL.match(lines[j]) and not _OL.match(lines[j]) \
                    and not _FOOTDEF.match(lines[j]) \
                    and not ("|" in lines[j] and j + 1 < n and _TABLE_SEP.match(lines[j + 1])):
                buf.append(lines[j].strip())
                j += 1
            if buf:
                out.append(f"<p>{render_inline(' '.join(buf))}</p>")
                i = j
            else:
                i += 1  # safety

        return "\n".join(out)

    @staticmethod
    def _split_row(line: str) -> list[str]:
        s = line.strip()
        if s.startswith("|"):
            s = s[1:]
        if s.endswith("|"):
            s = s[:-1]
        # split on unescaped pipes not inside code spans
        cells, cur, in_code = [], "", False
        for ch in s:
            if ch == "`":
                in_code = not in_code
            if ch == "|" and not in_code:
                cells.append(cur)
                cur = ""
            else:
                cur += ch
        cells.append(cur)
        return cells

    def _collect_list(self, lines: list[str], i: int) -> tuple[list[str], int]:
        n = len(lines)
        buf = [lines[i]]
        first_ordered = bool(_OL.match(lines[i]))
        base_indent = len((_OL.match(lines[i]) or _UL.match(lines[i])).group(1).expandtabs(4))
        j = i + 1
        while j < n:
            l = lines[j]
            if not l.strip():
                # blank line: continue list only if next non-blank is indented or a same-type list item
                k = j + 1
                while k < n and not lines[k].strip():
                    k += 1
                if k < n:
                    nxt = lines[k]
                    mo, mu = _OL.match(nxt), _UL.match(nxt)
                    same_type_base = (mo and first_ordered and len(mo.group(1).expandtabs(4)) == base_indent) or \
                                     (mu and not first_ordered and len(mu.group(1).expandtabs(4)) == base_indent)
                    nested = (mo or mu) and len((mo or mu).group(1).expandtabs(4)) > base_indent
                    if same_type_base or nested or (nxt.startswith(("  ", "\t")) and not (mo or mu)):
                        buf.append("")
                        j += 1
                        continue
                break
            mo, mu = _OL.match(l), _UL.match(l)
            if (mo or mu) and len((mo or mu).group(1).expandtabs(4)) == base_indent and bool(mo) != first_ordered:
                break  # a different list type starts at the same level
            if mo or mu or l.startswith(("  ", "\t")):
                buf.append(l)
                j += 1
            else:
                # lazy continuation
                if buf and buf[-1].strip():
                    buf.append("  " + l.strip())
                    j += 1
                else:
                    break
        return buf, j

    def _render_list(self, block: list[str]) -> str:
        # Determine base indent and type
        first = block[0]
        m = _OL.match(first)
        ordered = bool(m)
        base_indent = len((_OL.match(first) or _UL.match(first)).group(1).expandtabs(4))
        items: list[list[str]] = []
        for l in block:
            le = l.expandtabs(4)
            mm = _OL.match(le) if ordered else _UL.match(le)
            if mm and len(mm.group(1)) == base_indent:
                items.append([mm.group(3) if ordered else mm.group(2)])
            else:
                # if a differently-typed marker at base indent appears, treat as new item text (rare)
                other = _UL.match(le) if ordered else _OL.match(le)
                if other and len(other.group(1)) == base_indent:
                    items.append([other.group(2) if ordered else other.group(3)])
                elif items:
                    # strip base_indent + 2 spaces of nesting
                    stripped = le[base_indent:]
                    if stripped.startswith("    "):
                        stripped = stripped[4:]
                    elif stripped.startswith("  "):
                        stripped = stripped[2:]
                    elif stripped.startswith("   "):
                        stripped = stripped[3:]
                    items[-1].append(stripped)
        tag = "ol" if ordered else "ul"
        start = ""
        if ordered:
            s = int(m.group(2))
            if s != 1:
                start = f' start="{s}"'
        out = [f"<{tag}{start}>"]
        for it in items:
            head = it[0]
            rest = it[1:]
            # task list
            cls = ""
            tm = re.match(r"^\[( |x|X)\]\s+(.*)$", head)
            if tm:
                checked = tm.group(1).lower() == "x"
                head = tm.group(2)
                cls = ' class="task"'
                box = '<input type="checkbox" disabled' + (" checked" if checked else "") + "> "
            else:
                box = ""
            if rest and any(r.strip() for r in rest):
                sub = MDRenderer(self.heading_offset, self.id_prefix)
                sub._ids = self._ids
                inner = sub.render("\n".join(rest))
                self.footnotes.extend(sub.footnotes)
                out.append(f"<li{cls}>{box}{render_inline(head)}{inner}</li>")
            else:
                out.append(f"<li{cls}>{box}{render_inline(head)}</li>")
        out.append(f"</{tag}>")
        return "".join(out)

    def render_footnotes(self) -> str:
        if not self.footnotes:
            return ""
        out = ['<section class="footnotes"><h2>Notes</h2><ol>']
        for key, text in self.footnotes:
            out.append(f'<li id="fn-{key}">{render_inline(text)} <a href="#fnref-{key}" class="fn-back">↩</a></li>')
        out.append("</ol></section>")
        return "".join(out)


def md_to_html(md: str, heading_offset: int = 0, id_prefix: str = "") -> tuple[str, list]:
    r = MDRenderer(heading_offset, id_prefix)
    body = r.render(md)
    return body + r.render_footnotes(), r.headings


# ----------------------------------------------------------------------------
# Site generation
# ----------------------------------------------------------------------------

def load_chapters() -> list[Chapter]:
    chapters = []
    for p in sorted(CONTENT.glob("*.md")):
        m = re.match(r"^(\d+)-(.+)\.md$", p.name)
        if not m:
            continue
        text = p.read_text(encoding="utf-8")
        meta, body = parse_front_matter(text)
        ch = Chapter(
            path=p,
            number=int(m.group(1)),
            slug=m.group(2),
            title=meta.get("title", m.group(2).replace("-", " ").title()),
            part=meta.get("part", ""),
            summary=meta.get("summary", ""),
            body_md=body,
        )
        ch.words = len(re.findall(r"\b\w+\b", body))
        chapters.append(ch)
    return chapters


def read_asset(name: str) -> str:
    return (ASSETS / name).read_text(encoding="utf-8")


def layout(title: str, body: str, *, chapters: list[Chapter], current: Chapter | None,
           description: str = "", extra_head: str = "", page_class: str = "") -> str:
    nav_items = []
    last_part = None
    for ch in chapters:
        if ch.part != last_part:
            if last_part is not None:
                nav_items.append("</ul></details>")
            open_attr = " open" if (current and current.part == ch.part) else ""
            nav_items.append(f'<details{open_attr}><summary>{html.escape(ch.part)}</summary><ul>')
            last_part = ch.part
        cls = ' class="active"' if current and current.slug == ch.slug else ""
        nav_items.append(f'<li{cls}><a href="{ch.slug}.html"><span class="num">{ch.number:02d}</span> {html.escape(ch.title)}</a></li>')
    if last_part is not None:
        nav_items.append("</ul></details>")
    nav = "\n".join(nav_items)
    desc = html.escape(description or SITE_TAGLINE)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)} · {SITE_TITLE}</title>
<meta name="description" content="{desc}">
<meta property="og:title" content="{html.escape(title)}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="article">
<link rel="stylesheet" href="assets/style.css">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'%3E%3Ctext y='.9em' font-size='90'%3E%F0%9F%A7%A0%3C/text%3E%3C/svg%3E">
<script>try{{var t=localStorage.getItem('theme');if(t)document.documentElement.setAttribute('data-theme',t);}}catch(e){{}}</script>
{extra_head}
</head>
<body class="{page_class}">
<a class="skip" href="#main">Skip to content</a>
<header class="topbar">
  <button class="menu-btn" id="menu-btn" aria-label="Toggle navigation" aria-expanded="false">☰</button>
  <a class="brand" href="index.html">🧠 {SITE_TITLE}</a>
  <div class="topbar-right">
    <input type="search" id="search" placeholder="Search the guide…" aria-label="Search" autocomplete="off">
    <a class="top-link" href="full.html" title="Whole guide on one page">Single page</a>
    <a class="top-link" href="https://github.com/gorg667/learning-guide/blob/main/LEARNING_GUIDE.md" title="Markdown version" target="_blank" rel="noopener">Markdown</a>
    <button class="theme-btn" id="theme-btn" aria-label="Toggle dark mode">◐</button>
  </div>
  <div id="search-results" class="search-results" hidden></div>
</header>
<div class="shell">
  <nav class="sidebar" id="sidebar" aria-label="Chapters">
    <a class="side-home" href="index.html">Contents</a>
    {nav}
  </nav>
  <main id="main" class="content">
{body}
  </main>
</div>
<footer class="site-footer">
  <p>{SITE_TITLE} — {SITE_TAGLINE}. Written for learners of every age. Text released under CC BY 4.0.</p>
  <p><a href="index.html">Home</a> · <a href="full.html">Single page</a> · <a href="https://github.com/gorg667/learning-guide" target="_blank" rel="noopener">Source on GitHub</a></p>
</footer>
<script src="assets/app.js"></script>
</body>
</html>
"""


def toc_html(headings: list, max_level: int = 3) -> str:
    items = [h for h in headings if 2 <= h[0] <= max_level]
    if not items:
        return ""
    out = ['<aside class="toc"><div class="toc-title">On this page</div><ul>']
    for level, text, hid in items:
        out.append(f'<li class="lvl{level}"><a href="#{hid}">{render_inline(text)}</a></li>')
    out.append("</ul></aside>")
    return "".join(out)


def reading_time(words: int) -> str:
    mins = max(1, round(words / 230))
    return f"{mins} min read"


def build_chapter_page(ch: Chapter, chapters: list[Chapter], idx: int) -> str:
    prev_ch = chapters[idx - 1] if idx > 0 else None
    next_ch = chapters[idx + 1] if idx + 1 < len(chapters) else None
    nav = ['<nav class="pager">']
    if prev_ch:
        nav.append(f'<a class="prev" href="{prev_ch.slug}.html"><span>← Previous</span><strong>{html.escape(prev_ch.title)}</strong></a>')
    else:
        nav.append("<span></span>")
    if next_ch:
        nav.append(f'<a class="next" href="{next_ch.slug}.html"><span>Next →</span><strong>{html.escape(next_ch.title)}</strong></a>')
    nav.append("</nav>")
    pager = "".join(nav)
    body = f"""
<article class="chapter">
  <header class="chapter-head">
    <div class="crumbs"><a href="index.html">Contents</a> › <span>{html.escape(ch.part)}</span></div>
    <h1><span class="chapter-num">Chapter {ch.number}</span>{html.escape(ch.title)}</h1>
    <p class="lede">{render_inline(ch.summary)}</p>
    <p class="meta">{ch.words:,} words · {reading_time(ch.words)}</p>
  </header>
  <div class="chapter-grid">
    <div class="prose">
{ch.body_html}
    </div>
    {toc_html(ch.headings)}
  </div>
  {pager}
</article>
"""
    return layout(ch.title, body, chapters=chapters, current=ch, description=ch.summary)


def build_index(chapters: list[Chapter]) -> str:
    total_words = sum(c.words for c in chapters)
    parts: dict[str, list[Chapter]] = {}
    for ch in chapters:
        parts.setdefault(ch.part, []).append(ch)
    cards = []
    for part, chs in parts.items():
        cards.append(f'<section class="part"><h2>{html.escape(part)}</h2><div class="cards">')
        for ch in chs:
            cards.append(
                f'<a class="card" href="{ch.slug}.html"><div class="card-num">{ch.number:02d}</div>'
                f'<h3>{html.escape(ch.title)}</h3><p>{render_inline(ch.summary)}</p>'
                f'<div class="card-meta">{reading_time(ch.words)}</div></a>'
            )
        cards.append("</div></section>")
    intro_path = CONTENT / "_index_intro.md"
    intro_html = ""
    if intro_path.exists():
        intro_html, _ = md_to_html(intro_path.read_text(encoding="utf-8"))
    body = f"""
<section class="hero">
  <h1>{SITE_TITLE}</h1>
  <p class="hero-tagline">{SITE_TAGLINE}</p>
  <p class="hero-stats">{len(chapters)} chapters · {total_words:,} words · roughly {total_words // 230 // 60}h {total_words // 230 % 60}m of reading · hundreds of cited studies</p>
  <div class="hero-actions">
    <a class="btn primary" href="{chapters[0].slug}.html">Start reading →</a>
    <a class="btn" href="cheat-sheet.html">One-page cheat sheet</a>
    <a class="btn" href="full.html">Single-page version</a>
  </div>
</section>
<div class="prose intro">{intro_html}</div>
{''.join(cards)}
"""
    return layout("Home", body, chapters=chapters, current=None, page_class="home")


def build_full(chapters: list[Chapter]) -> str:
    total_words = sum(c.words for c in chapters)
    toc = ['<nav class="full-toc"><h2>Contents</h2><ol>']
    for ch in chapters:
        toc.append(f'<li><a href="#ch-{ch.number:02d}">{html.escape(ch.title)}</a></li>')
    toc.append("</ol></nav>")
    parts = []
    last_part = None
    for ch in chapters:
        if ch.part != last_part:
            parts.append(f'<h1 class="part-title">{html.escape(ch.part)}</h1>')
            last_part = ch.part
        body_html, _ = md_to_html(ch.body_md, heading_offset=1, id_prefix=f"ch{ch.number:02d}-")
        parts.append(
            f'<article class="chapter" id="ch-{ch.number:02d}"><header class="chapter-head">'
            f'<h1><span class="chapter-num">Chapter {ch.number}</span>{html.escape(ch.title)}</h1>'
            f'<p class="lede">{render_inline(ch.summary)}</p></header><div class="prose">{body_html}</div></article>'
        )
    body = f"""
<section class="hero compact">
  <h1>{SITE_TITLE}</h1>
  <p class="hero-tagline">{SITE_TAGLINE}</p>
  <p class="hero-stats">Complete single-page edition · {total_words:,} words</p>
</section>
{''.join(toc)}
{''.join(parts)}
"""
    return layout("Complete guide (single page)", body, chapters=chapters, current=None, page_class="full")


def build_book(chapters: list[Chapter]) -> str:
    total_words = sum(c.words for c in chapters)
    out = [
        f"# {SITE_TITLE}",
        "",
        f"*{SITE_TAGLINE}.*",
        "",
        f"> This is the single-file Markdown edition of the guide ({len(chapters)} chapters, {total_words:,} words). "
        "The website edition, with navigation and search, lives in `site/`. Both are generated from the "
        "chapter sources in `content/` by `build.py`.",
        "",
        "## Contents",
        "",
    ]
    last_part = None
    for ch in chapters:
        if ch.part != last_part:
            out.append(f"**{ch.part}**")
            out.append("")
            last_part = ch.part
        anchor = slugify(f"{ch.number} {ch.title}")
        out.append(f"{ch.number}. [{ch.title}](#{anchor}) — {ch.summary}")
    out.append("")
    out.append("---")
    out.append("")
    last_part = None
    for ch in chapters:
        if ch.part != last_part:
            out.append(f"# {ch.part}")
            out.append("")
            last_part = ch.part
        out.append(f"# {ch.number}. {ch.title}")
        out.append("")
        if ch.summary:
            out.append(f"*{ch.summary}*")
            out.append("")
        # demote headings by one level, fix internal links
        body = ch.body_md
        body = re.sub(r"^(#{1,5})\s", lambda m: "#" + m.group(1) + " ", body, flags=re.M)

        def fix_link(m: re.Match) -> str:
            label, href = m.group(1), m.group(2)
            if href.endswith(".md") and not href.startswith("http"):
                target = next((c for c in chapters if c.path.name == Path(href).name), None)
                if target:
                    return f"[{label}](#{slugify(f'{target.number} {target.title}')})"
            return m.group(0)

        body = re.sub(r"\[([^\]]+)\]\(([^)\s]+)\)", fix_link, body)
        out.append(body.rstrip())
        out.append("")
        out.append("---")
        out.append("")
    return "\n".join(out)


def build_search_index(chapters: list[Chapter]) -> str:
    idx = []
    for ch in chapters:
        idx.append({
            "t": ch.title,
            "u": f"{ch.slug}.html",
            "s": ch.summary,
            "h": [{"t": t, "id": hid} for level, t, hid in ch.headings if level <= 3],
            "p": ch.part,
            "n": ch.number,
        })
    return json.dumps(idx, ensure_ascii=False, separators=(",", ":"))


def content_hash(chapters: list[Chapter]) -> str:
    h = hashlib.sha256()
    for ch in chapters:
        h.update(ch.path.read_bytes())
    h.update((ROOT / "build.py").read_bytes())
    for a in sorted(ASSETS.glob("*")):
        if a.is_file():
            h.update(a.read_bytes())
    return h.hexdigest()[:16]


def main() -> int:
    chapters = load_chapters()
    if not chapters:
        print("No chapters found in content/", file=sys.stderr)
        return 1
    SITE.mkdir(exist_ok=True)
    ASSETS.mkdir(exist_ok=True)

    # render bodies
    for ch in chapters:
        ch.body_html, ch.headings = md_to_html(ch.body_md)

    # remove stale chapter pages
    keep = {f"{c.slug}.html" for c in chapters} | {"index.html", "full.html"}
    for p in SITE.glob("*.html"):
        if p.name not in keep:
            p.unlink()

    for i, ch in enumerate(chapters):
        (SITE / f"{ch.slug}.html").write_text(build_chapter_page(ch, chapters, i), encoding="utf-8")
    (SITE / "index.html").write_text(build_index(chapters), encoding="utf-8")
    (SITE / "full.html").write_text(build_full(chapters), encoding="utf-8")
    (SITE / "search.json").write_text(build_search_index(chapters), encoding="utf-8")
    BOOK.write_text(build_book(chapters), encoding="utf-8")
    (SITE / ".build-hash").write_text(content_hash(chapters), encoding="utf-8")

    total = sum(c.words for c in chapters)
    print(f"Built {len(chapters)} chapters, {total:,} words → site/ and LEARNING_GUIDE.md")
    return 0


if __name__ == "__main__":
    sys.exit(main())
