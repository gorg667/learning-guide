---
title: Learning with AI — what the evidence actually shows
part: Part IV — Applying it to specific domains
summary: A careful look at generative AI as a learning tool — the randomised trials that show large gains and the ones that show harm, why the difference is entirely about how it's used, the cognitive risks of offloading, a set of prompts and practices that make AI a tutor rather than a crutch, and what remains unknown.
---

## The most important open question in learning

Large language models arrived in 2022 and have already changed how millions of people study, write and code. They can explain any concept at any level, generate unlimited practice problems, give instant feedback, answer questions at 2 am, and — this is the problem — do the work for you. Whether they turn out to be the greatest educational technology ever invented or a machine for producing the illusion of learning depends on how they are used, and the research to date says both outcomes are real.

This chapter is written in late 2026 with the evidence available to that point; the field moves fast, and specific findings should be checked. The principles are more stable than the findings, because they follow from how learning works.

## What the trials show

### The good news: well-designed AI tutoring works

**Kestin et al. (2025, *Scientific Reports*)** ran a randomised crossover trial in Harvard's introductory physics course. Students learned one topic with an AI tutor — GPT-4 wrapped in carefully engineered pedagogy: scaffolding, one step at a time, never giving the answer away, checking understanding — and another topic in a well-designed active-learning class. On post-tests, students learned about **twice as much** with the AI tutor, in less time, and reported higher engagement and motivation. The comparison condition was not a bad lecture; it was research-based active learning, which is itself far better than lectures.

**World Bank (De Simone et al., 2025)**, Nigeria: a six-week after-school programme in which secondary students used GPT-4 (via Copilot) as an English tutor with a teacher present found effects of about **0.3 standard deviations** on English, AI knowledge and digital skills — which the authors convert to roughly 1.5–2 years of typical learning, and which compares favourably with almost all education interventions studied in low-income settings. Caveats: additional instruction time, teacher facilitation, short duration.

Together with older results on intelligent tutoring systems (VanLehn's 2011 review found ITS effects around d = 0.76, near those of human tutors; Kulik & Fletcher's 2016 meta-analysis found d ≈ 0.66), these findings support the view that **one-to-one adaptive tutoring is extremely effective, and AI can now provide it at scale** — when it is designed to tutor.

### The bad news: unguided AI can harm learning

**Bastani et al. (2025, *PNAS*)** ran a field experiment with about 1,000 high-school maths students in Turkey. Three conditions during practice sessions: no AI; **GPT Base** (a standard ChatGPT interface); and **GPT Tutor** (the same model with guardrails — hints, no direct answers, teacher-designed prompts). During practice, both AI groups did far better than control (GPT Base +48%, GPT Tutor +127% on practice problems). On the *unassisted exam afterward*, **students who had used GPT Base scored 17% worse than students with no AI at all.** GPT Tutor students scored about the same as control — the guardrails eliminated the harm but did not produce a gain on the exam. Analysis of chat logs showed GPT Base users predominantly asked for answers, and the model's answers were wrong a substantial fraction of the time. Students used the AI as a crutch, did not build the skill, and were worse off when it was removed.

**Kosmyna et al. (2025, MIT Media Lab preprint)** had participants write essays with an LLM, with a search engine, or unaided, while recording EEG. The LLM group showed the weakest brain connectivity, the lowest sense of ownership of their essays, and — strikingly — most could not quote a sentence from an essay they had "written" minutes earlier. The authors called this "cognitive debt". The study is small (54 participants), a preprint, and the EEG interpretation is contested, but the behavioural finding — you don't remember what you didn't produce — is exactly what the generation effect ([Chapter 11](11-elaboration-generation.md)) predicts.

**Computing education** studies (Prather et al., 2023; Kazemitabaar et al., 2023) find novices with code-generation access complete more tasks during practice but show no advantage — sometimes a disadvantage — on subsequent unaided tests, and struggle to judge whether generated code is correct ([Chapter 32](32-programming.md)).

### The noise: meta-analyses to be cautious about

A widely cited 2025 meta-analysis (Wang & Fan, *Humanities and Social Sciences Communications*) reporting a large positive effect of ChatGPT on learning performance (g = 0.867) was **retracted in April 2026** after errors in the analysis were identified. Other syntheses (Deng et al., 2025; Wu et al., 2026) report moderate positive average effects but combine studies of wildly different designs, durations and uses, most measuring performance *with* the AI rather than learning *after* it. The field is young, heterogeneous, and prone to measuring the wrong thing. Treat any single headline number with suspicion.

## Why the results diverge: the same principle as everything else

The pattern across these studies is not mysterious. It is the learning-versus-performance distinction ([Chapter 2](02-what-learning-is.md)) and the generation effect ([Chapter 11](11-elaboration-generation.md)), at scale:

- **AI that does the cognitive work for you raises performance and lowers learning.** Getting the answer feels productive and produces nothing durable — like rereading, like watching a solution, like copying notes, only faster and more convincing.
- **AI that makes you do the cognitive work, with support, raises learning.** Scaffolding, hints, questions, explanations of *your* errors, practice generation, feedback — this is what a good human tutor does, and it works for the same reasons.

The tool is the same in both cases. The difference is entirely in the interaction design — and, when you're using a general-purpose model yourself, that design is up to you.

## The specific risks

**Cognitive offloading.** Every time you ask the model to do something you could have done, you lose the practice. Offloading is rational for things you already know and will never need to do unaided; it is corrosive for things you are trying to learn. The failure is invisible: the output is good, the task is done, and the skill was not built.

**The fluency illusion, amplified.** A clear, confident, well-organised explanation produces a powerful sense of understanding ([Chapter 7](07-desirable-difficulties.md)). LLM explanations are extremely fluent. The gap between "that made sense" and "I can do this" is wider with AI than with any previous medium.

**Confident errors.** Models are wrong — sometimes subtly, often confidently — at a rate that depends on the domain and the question. A learner who cannot yet evaluate the domain cannot detect the errors and will learn them. Bastani et al. found GPT Base's answers were incorrect on about half of one problem type.

**Metacognitive erosion.** If the model always knows, you never practise judging what you know ([Chapter 13](13-metacognition.md)). Prather et al. describe novices "drifting" — accepting suggestion after suggestion without a plan or a model of what they were building.

**Loss of desirable difficulty.** The struggle that produces learning — the retrieval attempt, the productive failure, the debugging — is exactly what the tool offers to remove. Removing it removes the learning.

**Skill atrophy.** Skills you stop practising decay. Writing, mental arithmetic, navigating a codebase, reading a primary source — if the tool always does it, the capacity fades, and with it the ability to supervise the tool.

## Using AI as a tutor: practices with evidence behind them

Each of these maps an AI use onto a technique from Part II.

### Retrieval and self-testing
- **"Quiz me."** Ask for questions on a topic — short-answer, not multiple-choice — at your level. Answer *before* it shows anything. Then ask it to grade and explain.
- **"Ask me to explain X, then critique my explanation."** The Feynman technique with a knowledgeable listener ([Chapter 20](20-problem-solving-teaching.md)).
- **Generate practice problems** of a specified type, difficulty and variation — and mixed types, for interleaving ([Chapter 10](10-interleaving.md)). Pan et al. (2025) found LLM-generated prequestions produce the pretesting benefit.

### Elaboration and understanding
- **"Explain why, not just what."** Ask for the mechanism, the reason, the counterexample.
- **"Give me three examples from different domains."** Then ask what they share ([Chapter 19](19-transfer-mental-models.md)).
- **"Where does this analogy break down?"**
- **"What misconceptions do people have about this, and why are they appealing?"** Refutational learning on demand.
- **Explain first, then check.** Write your understanding; ask the model to identify what's wrong or missing. This is elaboration with feedback — and it ensures you generated before receiving.

### Scaffolding and worked examples
- **"Don't give me the answer. Give me one hint and wait."** The single most important prompt. Repeat as needed.
- **"Show me a worked example of a *similar* problem, then let me try this one."**
- **"I'm stuck at this step; what question should I be asking myself?"** Pólya's heuristics delivered just in time.
- **Fade the scaffolding** yourself: start with hints available, then forbid them.

### Feedback
- **"Here's my solution / essay / code. Point out the problems; don't fix them."** Process-level feedback ([Chapter 21](21-feedback.md)) that leaves the correction to you.
- **"What would an expert notice about this that I haven't?"**
- **"Grade this against this rubric and explain each score."**

### Metacognition
- **"Before I look anything up, let me tell you what I think the answer is."** Then check. Calibration practice.
- **"What are the prerequisites for understanding this, and how can I check whether I have them?"**
- **Keep a log** of what you asked and what you got wrong; it's your error log ([Chapter 13](13-metacognition.md)).

### Planning and materials
- Building a syllabus, finding the structure of a domain, identifying the standard textbooks, generating a spaced review schedule, converting notes to flashcards, summarising a paper *after* you've read it to check your summary — these are legitimate uses where the model is a research assistant rather than a substitute for thinking.

### A system prompt for learning

Many models let you set persistent instructions. Something like:

> *I am learning, not looking for answers. Never give me a direct solution unless I explicitly say "show me the answer". Give one hint at a time and wait for my response. When I explain something, tell me what's wrong or missing before telling me what's right. Ask me questions to check my understanding. When I ask for an explanation, ask first what I already think, then correct and extend. Prefer questions to statements.*

This turns a vending machine into a tutor. Kestin's group did this with a great deal more engineering; the basic version captures much of the benefit.

## When to let it do the work

Offloading is not always wrong. The question is: **is this a skill I am trying to build, or a task I am trying to complete?**

- Formatting references, boilerplate code in a language you already know, translating a document you don't need to be able to translate, summarising a report you'll never need to summarise yourself — offload freely.
- Understanding a concept you'll build on, writing you want to be able to write, code in a language you're learning, problems in a domain where you want competence — do it yourself, with the model as tutor.
- The test: **could you supervise the output?** If you couldn't tell whether it's right, you are not ready to delegate it — and using it teaches you to trust what you can't check.

## For teachers and parents

- **Guardrails work.** Bastani's GPT Tutor eliminated the harm. Configure tools not to give answers; teach students to configure them.
- **Assess the unaided skill.** If assessment can be completed by the tool, students will complete it with the tool, and learning will collapse. Assess retrieval, explanation, in-person problem-solving, oral defence.
- **Teach the meta-skill explicitly.** Students need to know *why* asking for answers hurts them; the mechanism is not obvious, and the tool's fluency argues against it every time.
- **Use it for what it's uniquely good at**: unlimited practice, instant feedback on drafts, adaptive explanation, patient repetition, availability.

## What we don't know yet

- **Long-term effects.** Almost all studies are short. Whether AI-tutored learning is as durable and transferable as conventional learning is not established.
- **Effects on motivation and identity.** Does easy access to answers change whether people want to learn things?
- **Effects across ability levels.** Early evidence suggests weaker students may be both the most helped by good tutoring and the most harmed by unguided use.
- **Whether "supervisory" skill can be built without the underlying skill.** Experts supervise AI well because they can do the task; whether a generation that never did the task can supervise is an open and important question.
- **The models themselves change** faster than the research can evaluate them.

> [!KEY]
> AI is the most powerful learning tool ever made available to individuals, and the most powerful tool for avoiding learning while feeling productive. Which one it is depends on a single variable: **whether you are doing the cognitive work with its help, or it is doing the cognitive work instead of you.** Configure it to tutor, not to answer. Generate before you receive. Verify what you can't yet judge. And periodically work without it, to check that the skill is yours.

> [!PRACTICE]
> Next time you'd normally ask an AI for an answer or explanation, do this instead: write your own best attempt first; then ask the model to critique it without giving the answer; revise; then, and only then, ask for the full explanation and compare. Notice that this takes three times as long — and that a week later you remember it, which is not true of the answers you simply read.

The next chapter looks at how learning changes across the lifespan — from children through adolescents to older adults — and what each stage needs.
