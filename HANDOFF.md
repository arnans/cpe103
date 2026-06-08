# Handoff — Basic Computer Engineering CLOs & Rubrics

*Working note for continuing this design work on another machine. Tell Claude "read HANDOFF.md" to pick up the thread.*

Primary artifact: [course-learning-outcomes.md](course-learning-outcomes.md)

---

## Course context (the constraints this design must fit)

- **Students:** freshman computer engineering students.
- **Enrollment:** ~90 students per year.
- **Structure:** a 2-hour **lecture** course + a 5-hour **lab** course. Concepts are introduced in lecture; labs run in **two-week pairs** — week 1 is hands-on practice, week 2 is "show and share" (peer review is used often in week 2).
- **Tools:** Canvas LMS is the main tool. **Canvas rubrics and peer review are the strategic levers** for managing workload at this class size.
- **Grading:** CLO results are used to calculate the **final grade**.

### Grade scheme (this is what makes the Exemplary level high-stakes)
- **Mastery on all CLOs → B.**
- One additional **Exemplary** on any CLO → **B+**.
- **Two or more Exemplary** → **A**.
- The instructor has a **clear CLO-level → %-score mapping** that maps all grades. *(Not yet shared with Claude — see open items.)*

Implication: because Exemplary is literally the B/B+/A line, every Exemplary descriptor must be **demonstrable on demand** and **defensible when contested** — not just good feedback language.

---

## Design decisions made

1. **A CLO counts as "Exemplary" only when ≥ half its criteria are at Level 4** (and none below Level 3). A single Level-4 cell does **not** make the whole CLO Exemplary. The criterion average still sets the within-band %; this rule sets which band/letter. The "half" fraction is tunable but must be applied uniformly.
2. **"Claim your Exemplary":** Level 4 is **student-claimed, not instructor-hunted**. To be scored Exemplary on a criterion, the student points to specific evidence (test file, slide, commit, journey-map detail), submitted *with* the deliverable. No claim, no Level 4. This keeps grading defensible and cuts the instructor's detection workload at ~90 students.
3. **Exemplary cells must not depend on luck/circumstance.** Cells that required an external event (a conflict to resolve, a problem to adapt to, a tough question to be asked) were reworded to things a student can choose to do regardless of circumstance.
4. **CLO1 testing must be visible** — students submit their own test cases so "testing & debugging" is actually gradeable.

### Edits applied this session (committed)
- Added the Mastery-vs-Exemplary band rule and the "claim your Exemplary" mechanic to *How the rubrics work*.
- Reworded 3 contingency-dependent Exemplary cells: **CLO3 Collaboration** ("resolves conflict" → proposes/improves a process, unblocks a teammate, synthesizes ideas), **CLO3 Planning** ("adapts when problems arise" → builds in checkpoints/contingencies up front), **CLO4 Technical accuracy** ("fields tough questions" → proactively addresses a likely question/limitation/trade-off).
- CLO1: require submitted test cases (*Assessed via* + the *Testing & debugging* Mastery/Exemplary cells).
- Added a rollout tip explaining the Exemplary mechanic to students up front.

---

## Open items (need instructor input)

1. **CLO-level → % mapping:** instructor to share it. Sanity-check that it agrees with the "≥ half criteria at Level 4 = Exemplary" rule — they must agree on where the Exemplary band starts.
2. **Below-Mastery letters:** confirm the sub-B grades are defined with the same threshold logic (not naive averaging).
3. **Claim-count cap:** decide whether to cap how many Exemplary criteria a student may claim per deliverable (e.g. at most N), to avoid adjudicating every criterion × 90 students. Hold vs add — pending observed volume.

---

## Earlier workload discussion (context, not yet acted on)

Original concern was grading workload at ~90 students. Key reframe: grading cost = (artifacts *you* read) × (judgments per artifact); the number of rubric criteria is the *small* multiplier. Bigger levers: number of summative scoring **events** per CLO, **grain** (90 individuals vs ~18 teams), and **who** scores (instructor vs peer review vs autograder). Suggested but not yet implemented: decouple formative from summative (score to rubric only at a few checkpoints), autograde CLO1 correctness, lean on week-2 peer review with criteria intact, keep team CLOs at team grain. A possible CLO3 simplification (4 criteria → 2) was discussed but **not** applied.
