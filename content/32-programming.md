---
title: Learning to program and other technical skills
part: Part IV — Applying it to specific domains
summary: How to learn programming — what computing-education research says about novices, the roles of reading, writing, tracing and debugging code, tutorial hell and how to escape it, projects versus exercises, learning from documentation, and how to use AI coding assistants without stunting your growth.
---

## A domain with unusually good research

Programming is one of the most commonly self-taught skills in the world, and one of the most commonly abandoned. It also has a strong research tradition — computing education research — with findings that overturn much of the folk wisdom about how to learn to code. Greg Wilson's *Teaching Tech Together* and Felienne Hermans's *The Programmer's Brain* synthesise much of it; this chapter applies it alongside the general principles of Parts I–III.

## What programming is, cognitively

Programming draws on several distinct kinds of knowledge and skill:

- **Syntax** — the surface form of the language. Declarative at first, must become automatic (a chunk) so that working memory is free for the problem.
- **Semantics / the notional machine** — a mental model of what the computer actually does when the code runs: how variables hold values, how control flows, how function calls work, what happens in memory. Novices' most persistent errors trace to wrong or missing notional machines (du Boulay, 1986; Sorva, 2013).
- **Patterns / plans / idioms** — the recurring chunks of code that solve recurring sub-problems: iterate over a collection and accumulate; find the maximum; parse input; the shapes of a recursive function. Experts have thousands; novices reinvent each from scratch (Soloway's "programming plans").
- **Problem decomposition and design** — turning a fuzzy requirement into a sequence of solvable sub-problems.
- **Debugging** — a distinct skill: forming hypotheses about why behaviour differs from intent, and testing them.
- **Tools and ecosystem** — editors, version control, build systems, libraries, documentation. Large, fragmented, constantly changing.
- **Reading code** — a skill separate from writing, and the one professionals spend most time on.

Most beginners' curricula emphasise syntax and writing small programs. The research says the bottlenecks are elsewhere: in the notional machine, in pattern knowledge, in reading and tracing code, and in debugging.

## What the research says

### Novices need to trace before they can write

Lister et al. (2004) and the "Leeds working group" found that many students who had passed introductory courses could not *trace* simple code — predict what a short program would output — and that tracing ability predicted the ability to write code, not the other way around. Students who cannot reliably predict what code does cannot debug their own, cannot read others', and write by trial and error. **Tracing is a prerequisite skill, and it is trained by tracing, not by writing.**

*Practice:* take short snippets, predict the output on paper, then run and compare. Trace with a variable table — the value of every variable at every step. Do it for code you wrote and code you didn't. Tools that visualise execution step by step (Python Tutor and equivalents) make the notional machine visible.

### Reading code is undertrained and hugely valuable

Hermans's work emphasises that reading code is a distinct skill involving all three memory systems: recognising syntax and idioms from long-term memory (chunking), holding structure in working memory, and building a model of what the code does. Novices lack chunks, so every line is a fresh parse — the same problem as beginning readers. Deliberate practice at reading — summarising what a function does, identifying its structure, refactoring it in your head — builds the chunk library that makes both reading and writing fluent.

### Worked examples and "explain in plain English"

The cognitive-load findings apply directly ([Chapter 5](05-cognitive-load.md)): novices learn more from studying and self-explaining worked code than from writing from scratch. **Parsons problems** — reassembling scrambled lines of a correct program — are a well-studied intermediate: they teach structure and idiom without the cognitive load of syntax generation, and studies find they're more efficient than writing equivalent code for novices (Ericson et al., 2018). "**Explain in plain English**" tasks — describe what this code does at the level of purpose, not line by line — predict and build understanding (Murphy et al., 2012). The progression is: read and trace → explain in plain English → reassemble (Parsons) → complete partial code → modify working code → write from scratch.

### Misconceptions about the machine are the main enemy

Novices carry stable, predictable misconceptions: that a variable can hold more than one value; that assignment is symmetric like an equation; that a loop's condition is checked continuously; that the computer "understands" names; that code executes in the order written regardless of function calls. These come from applying prior schemas (algebra, natural language) to a system that behaves differently. They are not fixed by writing more code; they are fixed by tracing, by execution visualisers, and by refutational explanation that names the misconception.

### Debugging is a skill to learn, not an annoyance to endure

Beginners spend most of their time debugging and are taught almost nothing about it. Debugging is hypothesis-driven investigation: what did I expect? what happened? what could cause the difference? how can I test that? Explicit instruction in debugging strategy — read the error message carefully; reproduce reliably; localise by bisection; form a hypothesis before changing code; change one thing; use print/log statements and the debugger systematically; explain the problem aloud ([rubber ducking](20-problem-solving-teaching.md)) — measurably improves outcomes. Treat each bug as a puzzle with a method, and keep a log of the bugs you've hit and their causes; patterns emerge.

### Language choice matters less than you think, at first

The first language is a vehicle for learning the notional machine, decomposition and patterns, which transfer. Choose one with readable syntax, a forgiving environment, good learning materials and a community (Python is the common default); avoid languages whose incidental complexity dominates the early experience. The second language is far easier than the first; the third easier still. Don't agonise; don't switch repeatedly.

## Tutorial hell and how to escape it

The characteristic failure mode of self-taught programmers: completing tutorial after tutorial, following along, everything working — and being unable to build anything without one. Every mechanism in this guide explains it:

- Following a tutorial is **recognition**, not **retrieval**. Each step makes sense given the previous one; you never had to produce a step.
- It generates **fluency without learning** ([Chapter 7](07-desirable-difficulties.md)): the code appears on screen, it works, you feel competent.
- It is **blocked and scaffolded** to the maximum; nothing is faded.
- **Performance is high, learning is low.**

The escape follows from the diagnosis:

1. **Never just follow along.** Pause the video before each step; predict what comes next; write it yourself; then compare. Every tutorial becomes a sequence of retrieval attempts with feedback.
2. **Close the tutorial and rebuild.** After finishing, delete the code and rebuild from memory. Then rebuild with a variation (different data, an extra feature, a different structure). Then rebuild something adjacent without a tutorial at all.
3. **Fade deliberately.** Tutorial → tutorial with gaps you fill → spec with hints → spec alone.
4. **Ratio.** For every hour of tutorial, spend two building without one.
5. **Start projects before you feel ready.** You will never feel ready. The feeling of readiness comes from having done it, not before.

## Exercises versus projects

Both are needed; they do different things.

**Exercises** (small, well-defined problems — Exercism, LeetCode, Advent of Code, textbook problems) are deliberate practice for components: syntax fluency, idioms, algorithms, data structures, tracing. They allow interleaving (mix problem types), spacing (revisit), immediate feedback (tests), and calibrated difficulty. Their weakness: they're pre-decomposed; someone else did the design.

**Projects** (building something that does something you or someone wants) are the whole task: requirements, decomposition, design, tooling, integration, debugging in the large, reading documentation, dealing with the messy world. They supply motivation, meaning and the skills exercises can't. Their weakness: slow feedback, unbounded difficulty, and the temptation to spend all the time on the parts you already know.

The pattern that works: **projects for direction and integration; exercises for the components the project reveals you're weak at.** Start a project; hit a wall (you can't manipulate strings fluently; you don't understand async; your data structure choice is wrong); step out to targeted exercises on that component; return. This is the identify-the-limiting-factor loop of deliberate practice ([Chapter 18](18-deliberate-practice.md)), and it keeps both exercises and projects at the edge of your ability.

Project selection: something you actually want to exist (motivation), small enough to finish (proximal goals), slightly beyond what you can do (ZPD), and — early on — a known kind of thing (a to-do app, a game clone, a scraper, a CLI tool) so that the design is not entirely novel and reference implementations exist to compare against afterward.

## Learning from documentation and code

Professionals learn continuously from documentation, source code and others' work. It is a skill.

- **Documentation**: preview the structure (what kinds of things does this library do? what are its main abstractions?) before diving into any function; read the conceptual overview before the API reference; run the examples and *modify* them; when you look something up, retrieve first ("I think it's called… and takes…") and then check.
- **Reading others' code**: start with the entry point and the data structures; trace one path through; summarise each function's purpose in a sentence; ask why it was structured this way; identify idioms you don't know and look them up. Reading good code is how you acquire patterns you'd never invent.
- **Error messages and stack traces**: read them completely and slowly. Beginners skim them and guess; experts read them and know. The error message is documentation about your specific mistake.
- **Source over search**: when a library behaves unexpectedly, reading its source is often faster than searching, and teaches more.

## AI coding assistants

This is now the defining question for anyone learning to program, and the evidence is arriving ([Chapter 35](35-learning-with-ai.md) covers AI and learning in general). The core finding — from Bastani et al.'s 2025 maths study, from Kosmyna et al.'s essay-writing study, and from early computing-education work (Prather et al., 2023; Kazemitabaar et al., 2023) — is that **AI assistance used to produce answers impairs learning, while AI used as a scaffolded tutor can help**. For programming specifically:

- **Beginners who let the assistant write the code learn less.** They cannot trace or debug what they didn't write, they don't build the notional machine, and they develop a dependence that fails the moment the assistant is absent or wrong. Kazemitabaar et al. found novices with code-generation access completed more tasks but showed no better (in some measures, worse) performance on subsequent unaided tests.
- **Metacognitive difficulties compound.** Prather et al. found novices struggled to judge whether generated code was correct, over-trusted it, and got lost in it — "drifting" through suggestions without a plan.
- **Assistants are excellent at the things experts already know how to do**, which is why experts find them so productive and why that productivity doesn't transfer to beginners: the expert is supervising; the beginner is delegating.

Guidelines that follow from the evidence:

1. **Write it yourself first, especially early.** Code generation is off during learning of a new concept. You need the struggle to build the machine model and the chunks.
2. **Use AI as a tutor, not a vending machine.** Ask it to explain code you don't understand; to explain an error; to give a hint rather than a solution; to quiz you; to review your code and point out (not fix) problems; to generate practice problems at your level. Configure it explicitly: "Don't give me the answer; ask me questions / give one hint at a time."
3. **Predict before you accept.** If you do use suggestions, predict what the code will do before running it, and trace it. Never accept code you couldn't have written and can't explain.
4. **Use it to accelerate what you already know**: boilerplate, syntax in a language you know conceptually, looking up an API — the way experts use it.
5. **Verify aggressively.** Assistants are confidently wrong, subtly and often. Treat output as a draft from a junior colleague.
6. **Periodically work without it** to check that the skill is yours.

The goal is a programmer who can use these tools as a force multiplier because they understand what the tools produce — not one who can't function without them.

## A learning method for programming

**Foundations (first weeks–months):**
- One language. Learn the notional machine explicitly (how variables, control flow, functions, memory work) with an execution visualiser.
- Daily: trace short programs on paper, then run. Explain-in-plain-English exercises. Parsons problems if available.
- Worked examples with self-explanation → completion → writing. Small exercises, interleaved by concept, with tests as feedback.
- Type every line yourself. No copy-paste from tutorials; predict before each step.
- Start a tiny project by week three or four.

**Building (months 2–12):**
- A project always in progress; exercises targeted at the components it exposes.
- Read code daily: solutions to problems you've solved, library source, good open-source projects. Summarise; identify idioms; card them.
- Debugging as a deliberate skill: method, log, patterns.
- Spaced retrieval for the factual layer (syntax, standard library, idioms, concepts) — Anki with code snippets works.
- Learn the tools (editor, git, testing, debugger) properly once each, then use daily.
- Explain what you learn: write it up, answer questions in a community, teach a friend.

**Deepening (year 2+):**
- Second language, chosen to be different (a different paradigm teaches more than a similar syntax).
- Larger projects; contributing to others' code; code review both ways.
- Fundamentals that projects tend to skip: data structures and algorithms, systems, how the machine actually works. Studied with problems, not just reading.
- Deliberate practice on the limiting factor — design, testing, performance, whatever the log shows.
- AI as a collaborator you supervise, not a crutch you lean on.

**Throughout:** retrieve (rebuild from memory), space, interleave, sleep on hard bugs, and judge yourself by what you can build unaided, not by tutorials completed.

> [!RESEARCH]
> Lister et al. (2004), in a multi-national study of students who had just completed introductory programming courses, found that many could not correctly predict the output of short programs or fill in a missing line — tasks well below "writing a program". The students had been assessed mainly on writing and had passed; but they lacked the tracing ability that writing depends on. Later work (Lopez et al., 2008; Venables et al., 2009) confirmed a hierarchy: tracing and explaining precede and predict writing. The implication for self-learners: if you struggle to write code, the fix is probably more reading and tracing, not more writing.

> [!PRACTICE]
> Take a program you wrote following a tutorial. Delete it. Rebuild it from memory without the tutorial, using only documentation and error messages when stuck. Note every place you couldn't proceed — those are the concepts you followed but didn't learn. Then add one feature the tutorial didn't have. The gap between following and building is the gap between performance and learning, and this exercise measures it.

The next chapter turns from cognitive skills to physical ones — motor skills, music and sport — where the science of practice has its longest history.
