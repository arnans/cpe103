# Basic Computer Engineering — Grading Methodology & CLO Assessment Mapping

*Companion to [course-learning-outcomes.md](course-learning-outcomes.md). Defines how rubric results become CLO scores, how CLO scores become a final letter grade, and which assessments feed each CLO.*

---

## 1. From rubric levels to a CLO score

Every criterion is scored on the shared 0–4 scale. Each level carries a **value** and a corresponding **percentage** (`% = 25 × value`):

| Rubric level | Value | Percentage |
|---|---|---|
| 4 — Exemplary | 4 | 100% |
| 3 — Mastery | 3 | 75% |
| 2 — Near Mastery | 2.5 | 62.5% |
| 1 — Below Mastery | 2 | 50% |
| 0 — No Evidence | 0 | 0% |

A **CLO's value** is the equal-weight average of its criterion values. Because the value→percentage relationship is linear through the origin (`% = 25 × value`), averaging values and averaging percentages give the same result.

> Note: a student who submits work but performs at *Below Mastery* on a criterion still earns value 2 (50%), not 0 — Level 0 is reserved for nothing submitted/demonstrated.

---

## 2. From CLO scores to a final grade

The course grade is the **equal-weight average of the five CLO percentages**:

```
Course %  =  (sum of the 5 CLO values) ÷ 20 × 100
          =  25 × (mean CLO value)
```

That percentage is mapped to a letter grade:

| Course % | Grade | Grade point | Points (of 20) | Mean CLO value |
|---|:--:|:--:|---|---|
| 81–100 | **A**  | 4.00 | 16.2 – 20.0 | 3.24 – 4.00 |
| 76–80  | **B+** | 3.50 | 15.2 – 16.0 | 3.04 – 3.20 |
| 71–75  | **B**  | 3.00 | 14.2 – 15.0 | 2.84 – 3.00 |
| 66–70  | **C+** | 2.50 | 13.2 – 14.0 | 2.64 – 2.80 |
| 61–65  | **C**  | 2.00 | 12.2 – 13.0 | 2.44 – 2.60 |
| 56–60  | **D+** | 1.50 | 11.2 – 12.0 | 2.24 – 2.40 |
| 51–55  | **D**  | 1.00 | 10.2 – 11.0 | 2.04 – 2.20 |
| 0–50   | **F**  | 0.00 | 0 – 10.0 | 0 – 2.00 |

*Round the course % to the nearest whole percent before looking up the band.*

### The intuitive ladder

Starting from "Mastery on every CLO" and adding Exemplary CLOs:

| Profile | Points | % | Grade |
|---|:--:|:--:|:--:|
| 5 Exemplary | 20.0 | 100% | A |
| 3 Mastery + 2 Exemplary | 17.0 | 85% | A |
| **4 Mastery + 1 Exemplary** | 16.0 | 80% | **B+** |
| **5 Mastery** | 15.0 | 75% | **B** |

**Meet every target → B; one Exemplary → B+; two or more Exemplary → A.**

### Falling short of Mastery (examples)

| Profile | Points | % | Grade |
|---|:--:|:--:|:--:|
| 4 Mastery + 1 Near Mastery | 14.5 | 72.5% | B |
| 3 Mastery + 2 Near Mastery | 14.0 | 70% | C+ |
| 5 Near Mastery | 12.5 | 62.5% | C |
| 3 Mastery + 2 Below Mastery | 13.0 | 65% | C |
| 5 Below Mastery | 10.0 | 50% | F |

---

## 3. CLO ← Assessment mapping

Each CLO score is a weighted combination of assessment results. Cells show **each assessment's weight toward that CLO**; every CLO totals 100%. The **Venue** column ties each assessment to its slot in [course-agenda.md](course-agenda.md).

| Assessment | Venue (agenda) | CLO1 | CLO2 | CLO3 | CLO4 | CLO5 |
|---|---|:--:|:--:|:--:|:--:|:--:|
| Scratch homework | Lab 1 (Jun 24) | 10% | — | — | — | — |
| Scratch class test | Lab 2 (Jul 1) | 10% | — | — | — | — |
| Scratch Tests (exam) | Coding Exam (Jul 15) | 30% | — | — | — | — |
| User Journey 1 | Lab 4 (Jul 22) | — | 10% | — | — | — |
| User Journey 2 | Lab 5 (Aug 5) | — | 20% | — | — | — |
| Process Mapping | Aug 14 lecture (presentation) | — | 20% | — | — | — |
| Presentation — self-selected topic | Lab 7 (Sep 9) | — | — | — | 30% | — |
| Teamwork & Task Management (with Planning, presented) | Lab 9 (Sep 23) | — | — | 50% | 20% | — |
| Final Project | Openhouse (Oct 7) + Report (Oct 14) | 50% | 50% | 50% | 50% | 100% |
| **Total** | | **100%** | **100%** | **100%** | **100%** | **100%** |

### Grouped by CLO

| CLO | Contributing assessments (weight · venue) | Σ |
|---|---|:--:|
| **CLO1** — Programming | Scratch homework 10% (Lab 1) · Scratch class test 10% (Lab 2) · Scratch Tests 30% (Coding Exam) · Final Project 50% | 100% |
| **CLO2** — System Analysis | User Journey 1 10% (Lab 4) · User Journey 2 20% (Lab 5) · Process Mapping 20% (Aug 14) · Final Project 50% | 100% |
| **CLO3** — Teamwork | Teamwork & Task Mgmt 50% (Lab 9) · Final Project 50% | 100% |
| **CLO4** — Communication | Presentation 30% (Lab 7) · Teamwork/Planning presented 20% (Lab 9) · Final Project 50% | 100% |
| **CLO5** — Capstone Integration | Final Project 100% | 100% |

**Notes**
- **Practice / formative (not scored):** Lab 6 — Presentation Practice (Sep 2), Lab 8 — Final Project Planning Practice (Sep 16), and Final Project Preparations (Sep 30). These use peer review but do not feed CLO scores.
- **The Final Project carries heavy weight** — 50% of four CLOs and 100% of CLO5 — so one weak project affects five outcomes at once. Deliberate, but it concentrates risk. The **Report (Oct 14)** is due one week after the Openhouse and is the students' opportunity to close any CLO-evidence gaps left from the Openhouse demo.
- Consistent with the CLO5 rubric ([course-learning-outcomes.md](course-learning-outcomes.md)): teamwork and communication *within* the project are scored with the CLO3/CLO4 rubrics (the project's 50% CLO3 and 50% CLO4 weights), while CLO5 scores only the product — no double-counting.
