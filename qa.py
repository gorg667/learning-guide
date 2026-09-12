#!/usr/bin/env python3
"""
qa.py — optional headless-browser QA for the built site.

Requires: pip install playwright && python3 -m playwright install --with-deps chromium
Serves site/ on a local port, loads every page at desktop and mobile widths, and reports:
  * console errors / failed requests / HTTP >= 400
  * horizontal overflow (layout bugs)
  * broken internal links
  * search returning results
Writes screenshots to /tmp/qa/. Exit 1 on any problem; exit 0 (skipped) if playwright is absent.
"""
from __future__ import annotations

import http.server
import os
import socketserver
import sys
import threading
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SITE = ROOT / "site"
PORT = 8791

try:
    from playwright.sync_api import sync_playwright
except ImportError:
    print("playwright not installed; skipping browser QA")
    sys.exit(0)


class Quiet(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *a):
        pass


def serve():
    os.chdir(SITE)
    socketserver.TCPServer.allow_reuse_address = True
    httpd = socketserver.TCPServer(("127.0.0.1", PORT), Quiet)
    threading.Thread(target=httpd.serve_forever, daemon=True).start()
    return httpd


def main() -> int:
    pages = sorted(p.name for p in SITE.glob("*.html"))
    existing = set(pages) | {f"assets/{a.name}" for a in (SITE / "assets").glob("*")} | {"search.json"}
    httpd = serve()
    problems: list[str] = []
    out = Path("/tmp/qa")
    out.mkdir(exist_ok=True)
    with sync_playwright() as pw:
        browser = pw.chromium.launch()
        for width, label in ((1280, "desktop"), (390, "mobile")):
            ctx = browser.new_context(viewport={"width": width, "height": 900})
            page = ctx.new_page()
            errors: list[str] = []
            page.on("console", lambda m: errors.append(f"console.{m.type}: {m.text}") if m.type == "error" else None)
            page.on("requestfailed", lambda r: errors.append(f"requestfailed: {r.url}"))
            page.on("response", lambda r: errors.append(f"HTTP {r.status}: {r.url}") if r.status >= 400 else None)
            for name in pages:
                errors.clear()
                page.goto(f"http://127.0.0.1:{PORT}/{name}", wait_until="load")
                page.wait_for_timeout(120)
                if page.evaluate("document.documentElement.scrollWidth > document.documentElement.clientWidth + 1"):
                    problems.append(f"[{label}] {name}: horizontal overflow")
                problems.extend(f"[{label}] {name}: {e}" for e in errors)
                if label == "desktop":
                    hrefs = page.evaluate("Array.from(document.querySelectorAll('a[href]')).map(a=>a.getAttribute('href'))")
                    for h in hrefs:
                        if h.startswith(("http", "mailto:", "#", "data:")):
                            continue
                        target = h.split("#")[0]
                        if target and target not in existing:
                            problems.append(f"{name}: broken link {h}")
                if name in ("index.html", "retrieval-practice.html", "cheat-sheet.html"):
                    page.screenshot(path=str(out / f"{label}-{name}.png"), full_page=(name != "index.html"))
            if label == "desktop":
                page.goto(f"http://127.0.0.1:{PORT}/index.html")
                page.fill("#search", "spacing")
                page.wait_for_timeout(600)
                if page.evaluate("document.querySelectorAll('#search-results a').length") == 0:
                    problems.append("search returned no results for 'spacing'")
                page.screenshot(path=str(out / "desktop-search.png"))
            ctx.close()
        browser.close()
    httpd.shutdown()
    print(f"Checked {len(pages)} pages at 2 widths; screenshots in {out}")
    for p in problems:
        print("PROBLEM", p)
    if problems:
        print(f"{len(problems)} problem(s)")
        return 1
    print("QA OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
