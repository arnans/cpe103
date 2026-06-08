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
- The full method (level values, `% = 25 × value`, equal-weight averaging, grade bands, and the CLO ← assessment weighting) is now written up in **[grading-methodology.md](grading-methodology.md)**. The %-mapping has been shared and reconciled — see "Resolved" below.

Implication: because Exemplary is literally the B/B+/A line, every Exemplary descriptor must be **demonstrable on demand** and **defensible when contested** — not just good feedback language.

---

## Design decisions made

1. **~~A CLO counts as "Exemplary" only when ≥ half its criteria are at Level 4.~~** *(Superseded — the half-rule was a discrete gate.)* Grading is now **continuous**: each criterion's value converts to a percentage by `% = 25 × value`, a CLO is the average of its criteria, and the final grade is the equal-weight average of the five CLOs. Under this scheme the B/B+/A ladder falls out naturally (5 Mastery = 75% = B; 4M+1 Exemplary = 80% = B+; 3M+2E = 85% = A) without needing a half-rule. See [grading-methodology.md](grading-methodology.md).
2. **"Claim your Exemplary":** Level 4 is **student-claimed, not instructor-hunted**. To be scored Exemplary on a criterion, the student points to specific evidence (test file, slide, commit, journey-map detail), submitted *with* the deliverable. No claim, no Level 4. This keeps grading defensible and cuts the instructor's detection workload at ~90 students.
3. **Exemplary cells must not depend on luck/circumstance.** Cells that required an external event (a conflict to resolve, a problem to adapt to, a tough question to be asked) were reworded to things a student can choose to do regardless of circumstance.
4. **CLO1 testing must be visible** — students submit their own test cases so "testing & debugging" is actually gradeable.

### Edits applied this session (committed)
- Added the Mastery-vs-Exemplary band rule and the "claim your Exemplary" mechanic to *How the rubrics work*.
- Reworded 3 contingency-dependent Exemplary cells: **CLO3 Collaboration** ("resolves conflict" → proposes/improves a process, unblocks a teammate, synthesizes ideas), **CLO3 Planning** ("adapts when problems arise" → builds in checkpoints/contingencies up front), **CLO4 Technical accuracy** ("fields tough questions" → proactively addresses a likely question/limitation/trade-off).
- CLO1: require submitted test cases (*Assessed via* + the *Testing & debugging* Mastery/Exemplary cells).
- Added a rollout tip explaining the Exemplary mechanic to students up front.

---

## Resolved (this session)

1. **CLO-level → % mapping — DONE.** Level values 4/3/2.5/2/0, `% = 25 × value` (Exemplary 100 / Mastery 75 / Near Mastery 62.5 / Below Mastery 50 / No Evidence 0). Final grade = equal-weight average of the five CLO %s, mapped through the official Thai grade band table. Confirmed against the instructor's worked example (4 Mastery + 1 Exemplary = 16/20 = 80% = B+). Full tables in [grading-methodology.md](grading-methodology.md).
2. **Below-Mastery letters — DONE.** Same continuous logic, no separate threshold rule. The instructor's first-listed lower percentages (80/70/60) were inconsistent with the weights and were corrected to 75/62.5/50.
3. **Half-rule removed** from [course-learning-outcomes.md](course-learning-outcomes.md) (the "Mastery vs Exemplary" band bullet and the matching rollout tip) — superseded by the continuous scheme above.
4. **CLO ← assessment mapping — DONE.** Captured in [grading-methodology.md](grading-methodology.md); every CLO's assessment weights total 100%.

## Open items (need instructor input)

1. **Claim-count cap:** decide whether to cap how many Exemplary criteria a student may claim per deliverable (e.g. at most N), to avoid adjudicating every criterion × 90 students. Hold vs add — pending observed volume.
2. **Final Project concentration risk:** the project is 50% of four CLOs and 100% of CLO5. Confirm this weighting is intended, or spread some weight to other assessments.

---

## Earlier workload discussion (context, not yet acted on)

Original concern was grading workload at ~90 students. Key reframe: grading cost = (artifacts *you* read) × (judgments per artifact); the number of rubric criteria is the *small* multiplier. Bigger levers: number of summative scoring **events** per CLO, **grain** (90 individuals vs ~18 teams), and **who** scores (instructor vs peer review vs autograder). Suggested but not yet implemented: decouple formative from summative (score to rubric only at a few checkpoints), autograde CLO1 correctness, lean on week-2 peer review with criteria intact, keep team CLOs at team grain. A possible CLO3 simplification (4 criteria → 2) was discussed but **not** applied.
