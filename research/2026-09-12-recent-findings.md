# Research notes — recent findings verified 2026-09-12

Purpose: capture recent (2023–2026) results and their exact numbers/caveats so chapters can cite
them accurately. Older canonical literature (Dunlosky 2013, Roediger & Karpicke 2006, Cepeda 2006,
Pashler 2008, Ericsson 1993, etc.) is well established and cited from memory in chapters.

## AI tutoring / generative AI and learning

- **Kestin et al. 2025, Scientific Reports** ("AI tutoring outperforms in-class active learning").
  Harvard intro physics RCT (crossover, ~194 students). AI tutor (GPT-4 with pedagogical prompts,
  scaffolding, "don't give the answer away") vs. well-designed in-class active learning. Median
  post-test 4.5 vs 3.5 (out of ~7-ish scale); learning gains roughly **2×**, in **less time**;
  higher engagement/motivation. Caveats: short-term (single-lesson), same-week test, tutor
  carefully engineered with guardrails and pedagogy — NOT "students using ChatGPT freely".
  https://www.nature.com/articles/s41598-025-97652-6
- **Bastani et al. 2025, PNAS** ("Generative AI without guardrails can harm learning").
  ~1,000 high-school maths students in Turkey; 3 arms: no AI, GPT Base (vanilla ChatGPT interface),
  GPT Tutor (with guardrails: hints, no direct answers). During practice: GPT Base +48%, GPT Tutor
  +127% on practice problems. On the unassisted exam afterwards: **GPT Base −17%** vs control;
  GPT Tutor ≈ no difference (harm eliminated but no gain). Mechanism: students use AI as a
  "crutch" — ask for answers; also GPT Base gave wrong answers ~half the time on some problems.
  https://www.pnas.org/doi/10.1073/pnas.2422633122
- **World Bank Nigeria RCT (De Simone et al., "From Chalkboards to Chatbots", 2025)**.
  Edo State, six-week after-school programme, GPT-4 via Copilot, teacher-guided, English
  language. Effect ≈ **0.3 SD** on English, AI knowledge, digital skills; authors convert this to
  "1.5–2 years of business-as-usual learning". Caveats: extra instruction time confound, teacher
  present, short. https://documents.worldbank.org/en/publication/documents-reports/documentdetail/099548105192529324
- **Kosmyna et al. 2025 (MIT Media Lab, "Your Brain on ChatGPT")**, arXiv 2506.08872, preprint.
  54 participants, EEG during essay writing: LLM group showed weakest connectivity, lowest
  ownership, poorest recall of own essay; "cognitive debt" framing. Caveats: small n, preprint,
  essay quoting task — suggestive not definitive.
- **Wang & Fan 2025 meta-analysis (Humanities & Social Sciences Communications), g = 0.867 for
  ChatGPT on learning performance — RETRACTED 22 April 2026** "owing to concerns regarding
  discrepancies in the meta-analysis" (see psyarxiv critique "Substantial Errors Invalidate…").
  Do NOT cite the 0.867 figure as evidence. A newer meta-analysis (Wu et al. 2026, HSSC) reports
  g ≈ 0.67 but same heterogeneity/quality concerns apply; Deng et al. 2025 (Computers & Education)
  systematic review: positive on performance, reduces mental effort, no effect on some outcomes.
  Lesson for the chapter: the field is young, noisy, and the direction of effect depends almost
  entirely on **how** the tool is used (answers vs. scaffolding).

## Spaced repetition algorithms

- **FSRS** (Free Spaced Repetition Scheduler, Jarrett Ye / open-spaced-repetition). In Anki since
  23.10 (Nov 2023), default-available in 24.04+. Benchmark on ~10k users / ~700M+ reviews shows
  FSRS beats SM-2 clearly on log-loss/RMSE; users report **20–30% fewer reviews** for same
  retention. Uses a 3-component model of memory (Difficulty, Stability, Retrievability — DSR).
  Lets the user choose desired retention (e.g. 0.9). https://expertium.github.io/Benchmark.html ;
  https://github.com/open-spaced-repetition/srs-benchmark

## Growth mindset — honest effect sizes

- **Macnamara & Burgoyne 2022/2023, Psychological Bulletin** meta-analysis: overall effect on
  academic achievement small (d ≈ 0.05–0.08), often non-significant when controlling for study
  quality; <25% of studies showed the intervention actually changed mindsets.
- **Burnette et al. 2023** (competing meta-analysis): small but positive effects (d ≈ 0.09–0.1
  overall), larger (≈0.2) for at-risk / low-achieving students.
- **Tipton et al. 2023** ("Why meta-analyses of growth mindset… vary"): heterogeneity is the
  point — effects concentrated in specific subgroups/contexts (Yeager et al. 2019 Nature national
  study: +0.1 GPA points for lower-achieving students in supportive-peer-norm schools).
- Framing for chapter: mindset is real as a *belief*, interventions are cheap, but expected effects
  are small and context-dependent; don't oversell.

## Retrieval practice

- Agarwal, Nunes & Blunt 2021 (Educ Psych Review) systematic review of 50 classroom studies:
  57% medium/large effects, 35% small, 8% null/negative — consistently positive in real classrooms.
- Yang et al. 2021 (Psychological Bulletin) meta-analysis of classroom quizzing: g ≈ 0.50 across
  222 studies; larger for feedback provided, and for match between quiz and test format.
- Corral et al. 2025 (Learning & Instruction): retrieval benefits for retention robust; transfer
  benefits smaller/less consistent — retrieval should be combined with elaboration/varied examples.

## Interleaving

- Brunmair & Richter 2019 (Psychological Bulletin) meta-analysis: 59 studies, **g = 0.42**
  overall; strongest for visual categories (paintings, birds) and maths; weaker or negative for
  highly dissimilar/expository text materials. "Similarity matters": interleave things that are
  confusable.

## Productive failure / problem-solving first

- Sinha & Kapur 2021 (Review of Educational Research) meta-analysis: 53 studies, ~12k participants,
  problem-solving-followed-by-instruction (PS-I) > instruction-then-problem-solving with moderate
  effect (g ≈ 0.36 overall, larger with fidelity to PF design principles, ~0.58); works better
  from grade 6 up; conceptual knowledge & transfer more than procedural.

## Pretesting / prequestions

- St. Hilaire & Carpenter 2024 meta-analysis of prequestion effect: reliable benefit for
  prequestioned material; benefit for non-prequestioned material depends on modality (video/
  lecture > text). Yan et al. 2025: pretesting effect robust across adulthood incl. older adults.
  Pan et al. 2025: ChatGPT-generated prequestions work too.

## Handwriting vs typing

- Mueller & Oppenheimer 2014 ("pen is mightier") found handwriting > laptop; **Morehead, Dunlosky &
  Rawson 2019** and **Urry et al. 2021** (multi-site replication, n≈600) found **no reliable
  difference** in learning. 2024 meta-analysis (24 studies) reports a small handwriting advantage;
  Van der Weel & Van der Meer 2024 (EEG) show broader connectivity when handwriting but that's
  not a learning outcome. Conclusion: medium matters less than *what you do* (generative vs
  verbatim). For young children learning letters, handwriting matters more.

## Exercise and cognition

- Singh et al. 2025, BJSM umbrella review / meta-meta-analysis (133 systematic reviews, >250k
  participants): small-to-moderate improvements in general cognition (~0.4 SMD for some outcomes),
  memory and executive function; even light-intensity; children/adolescents and ADHD populations
  show larger effects; exergames and yoga/mind-body also positive.
- Acute exercise (single bout, moderate, 20–30 min) reliably improves subsequent attention and
  memory encoding for ~1–2 hours (Chang et al. 2012 meta-analysis; Roig et al. 2013 for memory).

## Phones and attention

- Ward et al. 2017 "Brain Drain": mere presence of phone reduces working-memory capacity.
  Meta-analyses (Böttger et al. 2023; Hartanto et al. 2024) find the mere-presence effect is
  **small and inconsistent** — the real damage is from *use*/notifications/task-switching, not
  from the phone sitting there.
- Castelo et al. 2025 (PNAS Nexus): blocking mobile internet for two weeks improved sustained
  attention (effect comparable to being 10 years younger), mental health and well-being.
- OECD PISA 2022: ~30% of students distracted by digital devices in most/every maths lesson;
  distracted students score significantly lower (≈15 points); ~65% distracted in at least some lessons.

## Sleep

- Targeted memory reactivation (TMR) meta-analysis Hu et al. 2020 (Psych Bull): small-to-medium
  benefit during NREM sleep (d ≈ 0.29); Carbone & Diekelmann 2024 update confirms. Not a
  practical everyday tool yet but proves consolidation mechanism.
- Consistency (regularity) of sleep timing predicts outcomes as much as duration (Windred et al.
  2024 Sleep; Okano et al. 2019 for students' grades).

## Working memory / brain training

- Melby-Lervåg, Redick & Hulme 2016; Sala & Gobet 2017/2019: WM training gives near transfer only;
  **no far transfer** to intelligence or academic achievement. Rodas et al. 2024 find publication
  bias inflates even near-transfer estimates.

## Language apps

- Jiang et al. 2024 (CALICO) & Smith 2024: Duolingo completers reached A2-ish reading/listening
  after ~27–30 h; comparable to ~2–4 semesters of college for receptive skills; grammar/speaking
  weaker. Kim et al. (SSLA 2025): Duolingo ≈ classroom on most skills except grammar. Mostly
  company-funded — note conflict of interest.

## Successive relearning

- Rawson & Dunlosky 2022 review; Janes et al. 2020: successive relearning (retrieve to criterion
  in 3+ spaced sessions) raised high-stakes exam scores in biopsychology by about a letter grade
  on covered material; Mawson et al. 2025 review of distributed practice in classrooms confirms
  spacing effects are robust in authentic settings.
