# Learning How to Learn — the comprehensive guide

An evidence-based, in-depth guide to learning how to learn: how memory and attention work,
which study techniques are actually supported by research (and which are myths), how sleep,
exercise, stress and motivation shape learning, how to apply all this to languages, maths,
programming, music and more, and how to design a personal learning system.

**Two editions, one source:**

- 🌐 **Website:** `site/` (static HTML — open `site/index.html`, or serve the folder)
- 📄 **Markdown:** [`LEARNING_GUIDE.md`](LEARNING_GUIDE.md) — the whole guide in one file

Both are generated from the chapter sources in `content/` by `build.py` (Python 3 standard library only).

```bash
python3 build.py      # regenerate site/ and LEARNING_GUIDE.md
python3 validate.py   # sanity-check content and freshness of generated files
python3 -m http.server -d site 8000   # preview locally
```

## Layout

```
content/       chapter sources, NN-slug.md with front matter (title, part, summary)
site/          generated website (+ assets/style.css, assets/app.js which are hand-written)
research/      dated research notes and source lists gathered while writing
build.py       zero-dependency Markdown → HTML/site/book builder
validate.py    checks
PROGRESS.md    working log / agent memory (see CLAUDE.md)
```

Text is released under CC BY 4.0.
