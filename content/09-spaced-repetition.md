---
title: Spaced repetition — the spacing effect and how to schedule it
part: Part II — The evidence-based toolkit
summary: Why spreading study over time beats massing it, what the research says about optimal intervals, how spaced-repetition algorithms (Leitner, SM-2, FSRS) work, how to use Anki and similar tools without drowning in reviews, and how to space learning that doesn't fit on flashcards.
---

## The spacing effect

Take a fixed amount of study time — say, four hours on a set of material. You can spend it in one block, or spread it over four one-hour sessions across two weeks. The total effort is identical. The outcome is not: on a test given some time later, the spaced schedule will produce substantially better retention, typically by a wide margin.

This is the **spacing effect** (or *distributed practice effect*), first documented by Ebbinghaus in 1885 and confirmed since in hundreds of studies with every kind of learner and material — word lists, facts, concepts, mathematics, motor skills, surgical procedures, music, language. Cepeda and colleagues' 2006 meta-analysis of 254 studies found spaced practice outperformed massed practice in the overwhelming majority, and Dunlosky et al. (2013), in their landmark review of ten learning techniques, gave distributed practice their highest rating for utility, alongside practice testing.

The size of the effect depends on the retention interval, but it is large. In Cepeda et al.'s 2008 study, the best spacing schedule roughly *doubled* retention relative to the worst at long delays. Meanwhile the massed schedule almost always *feels* more effective and produces higher performance on an immediate test — the learning-versus-performance trap in its purest form.

### Why spacing works

Several mechanisms contribute:

- **Retrieval effort.** After a gap, some forgetting has occurred, so re-encountering the material requires effortful reconstruction rather than fluent recognition. As [Chapter 4](04-memory-systems.md) explained, storage strength grows most when retrieval strength has decayed. Massed repetition finds the memory at full retrieval strength, so each repetition adds almost nothing. (This is the *study-phase retrieval* account; it predicts, correctly, that spacing helps most when the second session involves actively recalling the first.)
- **Encoding variability.** Each session occurs in a slightly different context — mood, location, time, surrounding thoughts — so the memory acquires more retrieval cues.
- **Consolidation.** The gap allows sleep-dependent consolidation to occur between sessions, so the second session builds on a partially consolidated trace rather than an unstable one. At the cellular level, spaced stimulation triggers the protein synthesis needed for lasting change while massed stimulation does not ([Chapter 3](03-the-learning-brain.md)).
- **Deficient processing.** During massed repetition, attention to the repeated item drops — it seems known, so the mind skims it. After a gap, it gets full processing again.

## What the research says about intervals

### The lag effect and the retention-interval trade-off

Not all gaps are equal. Longer gaps between sessions generally produce better long-term retention — up to a point — a finding called the **lag effect**. But the best gap depends on how long you need to remember.

Cepeda, Vul, Rohrer, Wixted and Pashler (2008) ran the definitive study: over 1,300 participants learned facts, reviewed them after gaps from minutes to 105 days, and were tested after retention intervals from a week to nearly a year. The results:

- For every retention interval there was an optimal gap, and gaps shorter or longer than the optimum did worse.
- The optimal gap increased with the retention interval, but *not proportionally*. Roughly: **optimal gap ≈ 10–20% of the retention interval** for shorter intervals, falling to around 5–10% for very long ones.
- Gaps that were *too long* hurt less than gaps that were *too short*. When in doubt, space more.

| You need to remember for | Best gap before first review |
|---|---|
| 1 week | about 1 day |
| 1 month | about 1 week |
| 2–3 months | about 2 weeks |
| 1 year | about 3–4 weeks |
| Indefinitely | expanding intervals: days → weeks → months |

These figures are for a *single* review. With multiple reviews, the gaps should typically **expand**: each successful retrieval makes the memory more durable, so the next review can be later.

### Expanding versus equal intervals

The intuitive "expanding schedule" (1 day, 3 days, 7 days, 14 days…) has been compared against equal-interval schedules (5, 5, 5, 5 days) many times. The result is that **both work well and the difference is small**; expanding schedules have a slight advantage when the first interval is short enough that the first retrieval succeeds, and equal schedules do as well or better in some conditions (Karpicke & Roediger, 2007; Karpicke & Bauernschmidt, 2011). The important variables are that (a) there are gaps at all, (b) retrieval happens in each session, and (c) the total span covers a good fraction of the retention interval. Do not agonise over the exact schedule; do not let a schedule that's slightly wrong stop you from spacing.

### How many sessions?

Rawson and Dunlosky's successive-relearning work suggests a good target for durable factual/conceptual knowledge is **three successful retrievals in three or more spaced sessions**, followed by occasional maintenance retrievals at growing intervals. More sessions bring diminishing returns; fewer leave the memory fragile. For skills the number is far higher — hundreds or thousands of spaced repetitions — but the principle is the same.

## Spaced-repetition software

For anything that can be cast as a question with a checkable answer, software can manage the schedule for you. The idea is simple: each item gets its own review date; when you review it, you rate how well you recalled it; the software uses that rating to set the next date — sooner if you struggled, later if it was easy. Over thousands of items this is impossible to manage by hand and trivial for a program.

### The Leitner system (1972)

The pre-digital version. Cards live in numbered boxes. Box 1 is reviewed daily, box 2 every few days, box 3 weekly, and so on. A card you get right moves up a box; a card you get wrong goes back to box 1. It works and needs no technology; it is the mental model behind all the algorithms.

### SM-2 (SuperMemo, 1987) and Anki's classic scheduler

Piotr Woźniak's SM-2 algorithm assigns each item an *easiness factor*; after each review, the interval is multiplied by a factor derived from your rating (roughly ×2.5 for "good"), and lapses reset the interval. Anki, the most widely used free spaced-repetition program, used a variant of SM-2 as its default for its first fifteen years. It works well and is still what most people mean by "spaced repetition".

Its weaknesses: the parameters are fixed, not learned from you; it treats all items similarly regardless of their real difficulty; and it has no explicit model of memory, so it cannot tell you your predicted retention or let you choose it.

### FSRS (Free Spaced Repetition Scheduler, 2022–)

FSRS, developed by Jarrett Ye and the open-spaced-repetition community, is a machine-learning scheduler built on an explicit three-component model of memory:

- **Difficulty** — how hard this particular item is for you;
- **Stability** — how long the memory will last before retrievability drops to 90%;
- **Retrievability** — the probability you can recall it right now.

Each review updates these; the parameters of the model are fitted to your own review history. The user chooses a **desired retention** (say 90%) and FSRS schedules each card for the moment its predicted retrievability falls to that level. Benchmarks on hundreds of millions of real Anki reviews from thousands of users show FSRS predicts recall considerably more accurately than SM-2, and users report **20–30% fewer reviews for the same retention**. It has been built into Anki since version 23.10 (November 2023) and is available in several other tools.

For a learner, FSRS's practical advantages are: fewer reviews, an explicit retention target you can tune (lower it to 85% for low-stakes material to save time; raise it to 95% for exam-critical items), and the ability to skip "ease hell", the SM-2 failure mode where difficult cards get stuck on very short intervals forever.

### Tools

- **Anki** — free (except the iOS app), open source, cross-platform, hugely extensible, supports FSRS. The default choice for serious use. Steeper learning curve.
- **RemNote, Mochi, Obsidian spaced-repetition plugins** — combine notes with spaced repetition; good if you want cards linked to your notes.
- **SuperMemo** — the original, Windows-only, with unique "incremental reading" features; niche.
- **Quizlet, Brainscape, Memrise, Duolingo and other consumer apps** — implement some form of spacing, usually less transparent and less tunable; fine for casual use.
- **Paper (Leitner boxes)** — still works for a few hundred cards.

The tool matters much less than the habit. A daily review of whatever comes due, done properly (recall before flipping), is what produces the result.

## Using spaced repetition without drowning

The most common failure with Anki is not the algorithm; it is the pile of 800 overdue cards after a fortnight away, followed by abandonment. Some rules from experienced users and from the research:

**Limit new cards per day.** Every new card creates future reviews — roughly 8–15 reviews over the following months. Twenty new cards a day is a sustainable load for most people (~100–200 reviews/day at steady state); fifty is punishing. When you feel the review load rising, reduce new cards before you burn out.

**Review daily, even briefly.** Spacing works because reviews happen approximately when scheduled. A daily five-to-thirty-minute habit beats sporadic marathons. Anki's review count is a good thing to check while waiting for the kettle.

**Make cards that are small, precise and answerable in seconds.** Long, vague or list-based cards are failed repeatedly, clog the queue and demoralise. If you keep failing a card, rewrite it or split it — don't just keep failing it.

**Say the answer before flipping.** Every time. Flipping without committing is not retrieval.

**Prefer cards you made, understand and can explain.** Downloading a 5,000-card deck for a subject you haven't studied is a fast route to memorising things you don't understand. Spaced repetition is for *retaining* what you have learned, not for learning it in the first place. Understand first, then card.

**Use desired retention deliberately (FSRS).** 90% is a good default. For exam-critical material, briefly raising to 95% in the final weeks costs more reviews but tightens recall. For "nice to know" material, 80–85% roughly halves the review load.

**Don't card everything.** Not all knowledge belongs on flashcards. Facts, vocabulary, definitions, formulas, key dates, anatomy, drug names, syntax — yes. Deep conceptual understanding, procedures, skills — spaced repetition still applies, but via spaced *problem-solving*, *explanation* and *practice*, not via cards. Over-carding is a way of feeling productive while avoiding the harder work.

**Use it for maintenance, not just acquisition.** Once you've passed the exam or finished the course, keep the deck. Twenty minutes a week can maintain years of learning that would otherwise evaporate. This is spaced repetition's most underused superpower: it makes knowledge *permanent* at very low cost.

## Spacing without flashcards

Spacing is a scheduling principle, not a card format. Everything you learn should be spaced, and most of it can't be put on a card.

### Spacing a course

If a course has weekly topics, a simple spacing plan is: study the new topic this week; briefly retrieve last week's; briefly retrieve the topic from a month ago. Many students do only the first. A weekly review session that covers, from memory, the last four weeks' topics in a few minutes each is a large gain for a small cost.

### Spacing problem-solving

Textbooks and courses usually present a topic and then a set of problems all about that topic. To space (and interleave) them: do a third of the problems now, a third next week mixed with next week's problems, and a third in a month. Doug Rohrer's work on maths learning shows this kind of schedule roughly doubles retention on delayed tests relative to conventional blocked practice (Rohrer & Taylor, 2006, 2007).

### Spacing skills

Musicians, athletes and language learners already know that daily practice beats a weekly marathon. Within a domain, spacing also applies to *components*: revisit last month's piece, last month's grammar point, the drill you thought you had mastered. Spaced retrieval of skills you think you have already learned is what prevents the slow decay that most practitioners experience without noticing.

### Spacing reading

Reading a book once produces very little durable memory. Reading it once, then a week later spending fifteen minutes recalling and reviewing your notes, then a month later doing it again, produces a great deal. If a book matters, schedule the return visits when you finish it.

### Spacing writing and projects

Working on a piece of writing or a project in several sessions separated by days consistently produces better results than one long session — partly for the same consolidation reasons, and partly because sleeping on a problem is genuinely productive ([Chapter 22](22-sleep.md)).

### Interleaving as automatic spacing

If you rotate among several topics rather than finishing one before starting the next, spacing happens automatically: each topic gets a gap while you work on the others. This is one of several reasons [interleaving](10-interleaving.md) works.

## Building a spaced schedule for an exam

Suppose you have six weeks. A schedule that respects the evidence looks like this:

1. **Weeks 1–4: learn and card.** Study each topic once, properly (understand, do problems, self-explain). Same day: brain dump. Create cards or questions for the factual layer. Start daily reviews (limit new cards).
2. **Every week from week 2: cumulative retrieval.** One session per week retrieving *all* topics covered so far — brain dump per topic, or a mixed problem set spanning them.
3. **Weeks 5–6: consolidate.** Stop adding new material. Daily reviews continue. Mixed practice tests under exam conditions, checking afterwards, re-testing errors two days later. Raise desired retention if using FSRS.
4. **The last 24 hours: light retrieval, then sleep.** A quick pass over the review queue and the error list; no new material; a full night's sleep, which is worth more than any last-minute cramming.

Compare with the typical schedule — cover material week by week, never revisit, cram in the last three days — and the difference is not in hours but in *when* the hours fall.

> [!RESEARCH]
> Kornell (2009) had students learn vocabulary either by studying a stack of flashcards in a single large deck (which produces spacing between repetitions of any given card) or by splitting the same cards into four small decks studied one after another (massing). Over 90% of students learned more with the large, spaced deck. But when asked, most believed the small massed decks had worked better. The spacing effect is invisible from the inside.

## Common questions

**"Doesn't spacing mean I forget things between sessions?"** Yes. That's the point. The forgetting creates the effortful retrieval that builds durable memory. Aim for gaps where you *mostly* remember with effort — not so long that you're starting from zero.

**"What if I don't have time to space it — the exam is in three days?"** Then space within the three days: three sessions a day apart beat one long one. And test yourself rather than rereading in each. (Then read [Chapter 40](40-study-plans.md) about how to avoid this next time.)

**"Is cramming useless?"** Cramming produces real short-term performance; if the only goal is tomorrow's test and you'll never need the material again, it works. Almost nothing you learn is like that. Cramming is a way of paying full price for knowledge and then throwing it away.

**"I've heard of the '1-7-30 rule' / 'review after 1 day, 1 week, 1 month'."** These fixed schedules are reasonable approximations of expanding intervals and far better than nothing. Software does it better because it adapts to each item and to you.

> [!PRACTICE]
> Install Anki (or your preferred tool), enable FSRS, and set new cards to 10–20 per day. Make ten cards from something you learned this week — small, precise, in your own words. Review daily for two weeks, saying the answer aloud before flipping. Separately, put a weekly 30-minute "cumulative retrieval" slot in your calendar and, in it, brain-dump every topic from the last month. Two habits, less than half an hour a day, covering the two most powerful techniques in the science of learning.

Retrieval tells you *what* to do and spacing tells you *when*. The next technique — interleaving — is about the *order*, and it is the one learners resist most.
