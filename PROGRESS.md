# PROGRESS.md — agent memory for this repo

Repo goal: the most comprehensive, well-researched guide to **learning how to learn** —
delivered as (a) a static website in `site/` and (b) a single Markdown adaptation
`LEARNING_GUIDE.md` at the repo root.

## Architecture (decided 2026-09-12)

- `content/NN-slug.md` — one chapter per file, YAML-ish front matter (`title:`, `part:`, `summary:`).
  Chapters are numbered so ordering is file order.
- `build.py` — **zero-dependency** (stdlib only) Markdown → HTML converter + site generator.
  Produces `site/index.html`, `site/<slug>.html` per chapter, `site/full.html` (single page),
  and regenerates `LEARNING_GUIDE.md` (all chapters concatenated with a TOC).
- `validate.py` — stdlib checks: front matter present, headings well-formed, internal links
  resolve, generated files fresh (build hash), no empty chapters.
- `qa.py` — optional headless-browser QA (Playwright) if available; otherwise skipped.
- `research/` — dated notes from web research (sources, numbers, decisions).
- Branch policy (user, 2026-09-12): **push straight to `main`** after every commit. No branches/PRs.

## Log

- 2026-09-12 00:40 — Sandbox reset; lost unpushed ch04. Merged branch into main, deleted branch. Rewriting ch04.

- 2026-09-12 00:20 — Repo had only CLAUDE.md. Created branch `genspark_ai_developer`.
  Plan: scaffold (this file, README, build.py, validate.py, CSS) → research notes → chapters
  Part I..V → build → QA → PR.

## Next step

Write remaining chapters in order (see plan below); after each chapter: build.py, commit, push main. Ch01–03 done.

## Chapter plan (target ~40 chapters, each 2,000–6,000 words)

Part I — Foundations: how learning actually works
 01 Introduction & how to use this guide
 02 What learning is (encoding, consolidation, retrieval; declarative vs procedural)
 03 The brain that learns (neuroplasticity, hippocampus/neocortex, myelin, sleep replay)
 04 Memory systems (working memory limits, LTM, schemas, chunking, forgetting curve)
 05 Cognitive load theory
 06 Attention, focus and the myth of multitasking
 07 Desirable difficulties & the illusion of fluency

Part II — The evidence-based toolkit
 08 Retrieval practice (testing effect)
 09 Spaced repetition (spacing, lag effects, algorithms: SM-2, FSRS)
 10 Interleaving & variability
 11 Elaboration, self-explanation, generation
 12 Dual coding, concrete examples, worked examples
 13 Metacognition, calibration, judgments of learning
 14 What doesn't work (learning styles, rereading, highlighting, brain games, cramming)
 15 Note-taking (handwriting vs typing, Cornell, Zettelkasten, outlining)
 16 Reading to learn (SQ3R, active reading, speed-reading myths, deep reading)
 17 Mnemonics & memory techniques (method of loci, PAO, keyword, major system)
 18 Deliberate practice & expertise
 19 Transfer, analogies, and building mental models
 20 Problem-solving and the Feynman technique / teaching to learn
 21 Feedback: getting it, giving it, using it

Part III — The learner's body and mind
 22 Sleep and memory consolidation
 23 Exercise, nutrition, and the brain
 24 Stress, anxiety, emotion and learning
 25 Motivation: intrinsic/extrinsic, SDT, expectancy-value, curiosity
 26 Mindset, self-efficacy and beliefs about ability (with honest effect sizes)
 27 Habits, environment design, procrastination
 28 Time management for learners (Pomodoro, time-blocking, ultradian rhythms, deep work)
 29 Flow, boredom and the difficulty sweet spot

Part IV — Applying it to specific domains
 30 Learning languages
 31 Learning mathematics and quantitative subjects
 32 Learning to program / technical skills
 33 Learning motor skills, music, and sport
 34 Learning from lectures, video, MOOCs and books
 35 Learning with AI tools (LLM tutors: what the 2024–2026 RCTs actually show)
 36 Learning across the lifespan (children, adolescents, adults, older adults)
 37 Learning with others (peer instruction, study groups, teaching, communities)
 38 Learning with ADHD, dyslexia and other differences

Part V — Putting it together
 39 Designing your personal learning system (templates, weekly plan, review cadence)
 40 Study plans: exam in 2 weeks / semester course / self-taught skill in 6 months
 41 Troubleshooting: "I forget everything", "I can't focus", "I'm bored", plateaus
 42 One-page cheat sheet
 43 Annotated bibliography & further reading
 44 Glossary
 45 FAQ
