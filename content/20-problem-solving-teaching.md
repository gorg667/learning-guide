---
title: Problem solving, the Feynman technique and learning by teaching
part: Part II — The evidence-based toolkit
summary: How to get better at solving problems — Pólya's method, heuristics, focused and diffuse thinking, the Einstellung trap — and why explaining things to others (or to a rubber duck) is one of the most powerful learning acts available, with the evidence for the "protégé effect".
---

## Problem solving as the test of understanding

Everything in this guide aims at knowledge you can use, and the purest use of knowledge is solving a problem you have not seen before. Problem-solving ability is what distinguishes a learner who has understood from one who has memorised; it is what employers, examiners and life actually test; and it is itself a skill that improves with the right kind of practice.

This chapter has two halves. The first is about solving problems: the general strategies, the cognitive traps, and how to practise. The second is about the most underused learning technique of all — explaining and teaching — and why it works so well.

## How experts solve problems

Research comparing experts and novices in physics, mathematics, medicine, chess and programming finds consistent differences, and they are not about raw intelligence:

- **Experts categorise problems by deep structure** ("this is a conservation problem") while novices categorise by surface ("this is a problem about a ramp"). The expert's first move is to identify the *type*, which brings the relevant schema and approach with it.
- **Experts work forward from the givens** using known principles; novices work backward from the goal via means–ends search ("I need X; what gives X? I need Y for that…"), which is slow and heavy on working memory (Larkin et al., 1980).
- **Experts spend more time on representation** — understanding the problem, drawing a diagram, restating it — before computing. Novices dive into calculation.
- **Experts monitor themselves**, noticing when an approach isn't working and switching; novices persist.
- **Experts have vastly more chunks** — familiar patterns that make the problem's structure visible at a glance ([Chapter 4](04-memory-systems.md)).

Notice that most of these are teachable habits, and the last is the product of practice.

## Pólya's four phases

George Pólya's *How to Solve It* (1945) remains the best general framework, and its four phases map onto what experts do:

### 1. Understand the problem

Before anything else: what is being asked? What are the givens? What are the unknowns? What are the conditions connecting them? Restate the problem in your own words. Draw a figure. Introduce notation. Ask: is there enough information? Is it consistent? What kind of problem is this?

Most failed solutions fail here — the solver started working on a problem slightly different from the one posed. Spending a third of your time on understanding is not slow; it is how experts work.

### 2. Devise a plan

Find the connection between givens and unknowns. Pólya's heuristics — questions to ask yourself when you don't know what to do — remain the core toolkit:

- **Have you seen a problem with the same unknown?** Related problems and their methods are the first place to look.
- **Can you think of a related, simpler problem?** Solve a special case, a smaller version, a version with a constraint removed. Then generalise.
- **Can you restate the problem?** In different terms, in a different representation (algebraic → geometric; verbal → diagram).
- **Work backward.** Start from the goal and ask what would immediately produce it.
- **Decompose.** Split into sub-problems; solve each.
- **Vary the problem.** Drop a condition and see what happens; add one; consider the extreme cases.
- **Look for a pattern.** Try small cases; tabulate; guess the rule; then prove or check it.
- **Use all the data.** Have you used every given? If not, why is it there?
- **Introduce auxiliary elements.** A construction line, a helper variable, an intermediate quantity.
- **Consider the inverse / contrapositive / complementary problem.**

### 3. Carry out the plan

Execute carefully. Check each step. When it stalls, return to phase 2 rather than pushing harder on a plan that isn't working.

### 4. Look back

The phase everyone skips and the one that produces most of the *learning*. Check the result: does it make sense? Are the units right? Does it satisfy the conditions? Could you have got it another way? Can you use the method or the result for another problem? What was the key insight — and what kind of problem does it generalise to?

Looking back is where a solved problem becomes a transferable schema ([Chapter 19](19-transfer-mental-models.md)). Skipping it is why students can solve fifty problems and learn from none.

## Focused and diffuse thinking

Barbara Oakley popularised, in *A Mind for Numbers* and the *Learning How to Learn* course, a distinction that captures something real about problem solving: two modes of thought.

**Focused mode** is deliberate, attentive, sequential — working through a problem with concentration, following known paths. It is what most of this guide is about and it is essential.

**Diffuse mode** is relaxed, wide-ranging, associative — the mind wandering, making distant connections, not trying. It is what happens in the shower, on a walk, or when you've stopped working on the problem.

The neuroscience behind this is real, if less tidy than the metaphor: focused attention engages task-positive control networks and *suppresses* the default-mode network, which is associated with associative and self-generated thought; when focus relaxes, the default network re-engages and can produce novel combinations. The relevant behavioural findings:

- **Incubation effects are real but modest.** Sio and Ormerod's 2009 meta-analysis found that taking a break from a problem improves later solution rates, especially for creative and divergent problems and when the break involves an undemanding task rather than a demanding one.
- **Fixation is the enemy.** Much of incubation's benefit comes from *forgetting the wrong approach*: when you return, you are less locked into the path that wasn't working.
- **Sleep produces insight.** Wagner et al. (2004) found that sleeping after working on a problem more than doubled the chance of discovering a hidden shortcut ([Chapter 22](22-sleep.md)).

The practical pattern: work hard in focused mode until genuinely stuck, then *stop* — walk, do something undemanding, sleep — and return. Don't skip the focused work (diffuse mode has nothing to work with otherwise), and don't skip the break (focused mode gets stuck in ruts).

### Einstellung: the mental set trap

Luchins' (1942) water-jar experiments showed that people who solved a series of problems with one method continued to use it even when a much simpler method was available — and even when it no longer worked. The **Einstellung effect** (mental set) is the tendency to see a new problem through the lens of recent solutions. It is a cost of expertise and of blocked practice: the more automatic an approach, the harder it is to notice it doesn't fit. Countermeasures: interleaved practice (which trains method selection), the habit of spending time on representation before choosing a method, and the deliberate question "what other approach could work?" before committing.

## Practising problem solving

Problem-solving skill in a domain comes overwhelmingly from solving problems in that domain — with the following adjustments to make the practice deliberate ([Chapter 18](18-deliberate-practice.md)):

- **Attempt before looking.** Time-boxed genuine effort before consulting the solution. The struggle is where learning happens; the solution then lands on prepared ground.
- **When stuck, use heuristics, not the answer key.** Run through Pólya's questions. Simplify. Draw. Try a special case. Only when heuristics are exhausted, look at a hint — the smallest hint that unsticks you, not the whole solution.
- **After solving, look back** — always. What type? What key idea? Where else?
- **Self-explain solutions you had to look up**, step by step, and then re-solve from scratch a few days later.
- **Mix problem types** so that recognising the type is part of the practice.
- **Do problems without the chapter's methods labelled** — cumulative sets, old exams, problems from other sources.
- **Keep an error log**: not just wrong answers but *why* — misread the problem, wrong type identified, computational slip, missing knowledge. Patterns in the log tell you what to practise.
- **Work at the right level.** Problems you can do instantly are review; problems you can't touch after ten minutes need prerequisites. The middle — solvable with real effort — is where skill grows.
- **Do fewer problems more thoroughly** rather than many superficially. Twenty problems solved, looked back on and re-solved beat a hundred done once.

## The other half: learning by teaching

### The protégé effect

Everyone who has taught knows that you understand something differently after explaining it. The research confirms this and shows the effect is large.

The **protégé effect** — the finding that people learn more when they learn in order to teach others — has been demonstrated repeatedly. Bargh and Schul (1980) found students who studied a passage *expecting to teach it* learned more than those expecting a test, even though none actually taught. Nestojko et al. (2014) replicated this: the expectation of teaching alone improved recall and organisation of the material. Fiorella and Mayer (2013, 2014) found that students who *actually* explained the material to others (on video) outperformed those who merely expected to, and that the benefit persisted a week later. Chase et al.'s (2009) "teachable agents" — students teaching a computer character — learned more and worked harder than students learning for themselves.

Kobayashi's 2019 meta-analysis of learning-by-teaching studies found a moderate positive effect (g ≈ 0.3–0.5), larger when the teaching was interactive (the learner had to answer questions) and when it involved actual explanation rather than just preparation.

### Why it works

Teaching combines almost every effective technique in this guide:

- **Retrieval.** To explain, you must recall — and recall in an organised, connected way.
- **Elaboration and organisation.** You must decide what's important, sequence it, connect it, find examples.
- **Generation.** You produce the explanation rather than receiving it.
- **Metacognition.** Gaps become glaringly obvious: you reach a point where you can't explain and you know precisely what you don't understand. This is the fluency illusion being punctured in real time.
- **Motivation and attention.** Expecting to teach changes how you study — more carefully, more structurally — and an audience, even an imagined one, focuses attention.
- **Questions.** A learner's questions expose assumptions and force you to articulate what was tacit.

### The Feynman technique

Named after Richard Feynman, who was famous for explaining physics in plain language and who reportedly said that if you can't explain something simply you don't understand it. The technique, as popularised:

1. **Choose a concept** and write its name at the top of a blank page.
2. **Explain it in plain language**, as if to a bright twelve-year-old (or a friend outside the field). No jargon. Use examples. Write it out.
3. **Identify the gaps.** Wherever you hesitated, reached for jargon, hand-waved, or couldn't produce an example — that's a gap. Go back to the source and fill it.
4. **Simplify and use analogies.** Rewrite until the explanation is clear and simple, with an analogy where one helps.

There is no direct research on "the Feynman technique" by name, but every component is well supported: it is retrieval (from memory), self-explanation, generation, elaboration with concrete examples, and metacognitive monitoring, in one procedure. The "plain language" constraint is important: jargon lets you feel you've explained when you've only labelled. The "to a twelve-year-old" constraint forces you to find the actual idea.

Its limit is the same as self-explanation's: explaining wrongly with confidence entrenches error. Check the explanation against a good source, or against someone who knows.

### Rubber-duck debugging and talking aloud

Programmers know that explaining a bug aloud — to a colleague, or famously to a rubber duck on the desk — often reveals the problem before the listener says a word. The mechanism is the same: articulation forces sequential, explicit reconstruction of your reasoning, and the assumption you hadn't noticed becomes visible when you have to say it. This works for any problem. Talking through your reasoning aloud (or writing it out) is a form of self-teaching available at any moment.

### How to use teaching to learn

- **Study as if you'll have to teach it.** Even without an audience, adopting the frame improves organisation and retention.
- **Actually explain — aloud or in writing — from memory.** Not with the notes open. The gaps only show when you have to produce.
- **Teach a real person when you can.** A study partner, a classmate who's behind, a friend, a family member, an online forum. Their questions are worth more than your monologue.
- **Answer questions in communities.** Stack Overflow, subject forums, language-exchange groups. Formulating an answer for a stranger is deliberate practice at explanation with feedback.
- **Write explanations.** Blog posts, study guides, answers to imagined FAQs. Writing forces linearity and completeness.
- **Make and then teach a "one-page explanation"** of each major topic — the Feynman technique with a spaced revisit.
- **Tutor.** The tutor typically learns more than the tutee. If you can find someone to tutor in what you're learning, do.
- **Reverse the roles in a study group.** Each person teaches a topic to the rest; the rest question.

## Bringing the halves together

Problem solving and teaching are the two most demanding uses of knowledge, and for that reason the two most powerful for building it. A study routine that ends every topic with (a) a set of problems solved with Pólya's look-back and (b) a plain-language explanation produced from memory will produce knowledge that is deep, connected, transferable and durable — the opposite of inert.

> [!RESEARCH]
> Fiorella and Mayer (2013) had students study a lesson on the Doppler effect under three conditions: study for a test; study expecting to teach; study and then actually teach (record a video explanation). On an immediate test, both teaching groups beat the test-prep group. A week later, only the group that had *actually taught* retained the advantage — the expectation alone faded, but the act of explaining produced durable learning.

> [!PRACTICE]
> Choose the most important concept from what you studied this week. Take a blank page. Explain it, in writing, in plain language, to an imagined intelligent fourteen-year-old, with one example — from memory, no notes. Mark every place you hesitated or used a technical term you couldn't unpack. Those marks are the precise coordinates of what you don't yet understand. Fill them, then rewrite. Save the page: it is both your best study note and a record of the moment you actually learned the thing.

Solving and teaching both depend on getting good information about how you're doing. The final chapter of Part II is about feedback: how to get it, how to use it, and how to give it.
