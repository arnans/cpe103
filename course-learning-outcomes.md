# Basic Computer Engineering — Course Learning Outcomes (CLOs) & Rubrics

## How these outcomes were designed

Each outcome follows established good practice for learning-outcome design:

- **One coherent skill per outcome.** Each CLO names a demonstrable behavior — or a coherent cluster of closely related actions (e.g. *write and debug*) — so it can be taught and assessed cleanly. What it avoids is bundling *unrelated* ideas (e.g. "show skills *and* show understanding").
- **Measurable action verbs (Bloom's taxonomy).** Vague verbs like *show*, *understand*, or *know* are replaced with verbs that name observable performance — *write, apply, analyze, collaborate, communicate, design, integrate*.
- **Condition + criterion where useful.** Outcomes name the context ("using fundamental constructs," "for a defined problem") so the standard of performance is clear.
- **Constructive alignment.** Each CLO maps to how it will be taught and assessed, and the rubric levels make "good" concrete and gradeable.
- **Appropriate cognitive level.** As an introductory ("Basic") course, outcomes target *Apply / Analyze* with a capstone reaching *Create* — a sensible progression.
- **A consistent 5-level performance scale (0–4)** is used across every rubric:

| Level | Label | Meaning |
|-------|-------|---------|
| 0 | **No Evidence** | Nothing submitted or demonstrated to assess |
| 1 | **Below Mastery** | Below expectations; needs substantial support |
| 2 | **Near Mastery** | Approaching expectations; works with guidance |
| 3 | **Mastery** | Performs exactly as the CLO states — the target standard for the course |
| 4 | **Exemplary** | Meets Mastery and goes beyond the CLO in at least one way |

> **Level 3 (Mastery) is the pass/target standard** — the student does exactly what the CLO describes. **Level 4 (Exemplary)** is reserved for work that meets Mastery *and* demonstrates at least one thing beyond what the CLO states.

---

## The Course Learning Outcomes

> *On successful completion of Basic Computer Engineering, students will be able to:*

| # | Course Learning Outcome |
|---|-------------------------|
| **CLO1** | **Write and debug basic programs** using fundamental constructs including variables, control flow, functions, and algorithms. |
| **CLO2** | **Apply** User Journey Analysis and Process Mapping to a system, and **recommend** design improvements justified by that analysis. |
| **CLO3** | **Collaborate** in a team to plan, manage, and deliver assignments and projects, fulfilling individual responsibilities and contributing to shared goals. |
| **CLO4** | **Communicate** engineering concepts clearly in **written** form and in **oral** presentation. |
| **CLO5** | **Design and build** a complete software application that **integrates** programming, system analysis, teamwork, and communication, taking it from initial concept to a working product. |

Each CLO has a single **master rubric**, used everywhere that CLO is assessed.

---

## How the rubrics work

- **One master rubric per CLO.** The same rubric is reused across every activity that assesses that CLO, so expectations stay consistent and students improve against a fixed standard.
- **Each criterion is scored 0–4** on the shared scale above. A CLO's score is the **average of its criteria** (equal weight). Per-criterion scores double as feedback — they show students *where* they are strong or weak, not just an overall number.
- **Scoring a compound criterion.** Some criteria bundle two closely related behaviors joined by *and* (e.g. *completes own share on time* **and** *communicates respectfully*). When the two halves perform at different levels, **score to the weaker half** unless the level cell says otherwise — the target is met only when both are met.
- **Anchored to the CLO.** For every criterion, **Level 3 means the student does exactly what the CLO states** (the target). **Level 4** means they meet Level 3 *and* go beyond in at least one way (the cell gives an example). Levels 2 and 1 are *approaching* and *below*; Level 0 is no evidence.
- **How levels become grades.** Each level carries a value (4 / 3 / 2.5 / 2 / 0) that converts to a percentage by `% = 25 × value`; a CLO's percentage is the average of its criteria, and the final grade is the equal-weight average of the five CLO percentages. The full method, grade bands, and the CLO ← assessment weighting are in **[grading-methodology.md](grading-methodology.md)**. In short: **Mastery on every CLO earns a B; an Exemplary Final Project is what lifts the grade to B+ and A** (Exemplary is available on the Final Project only — every other assessment caps at Mastery, and the grade ceiling is 90%).
- **Earning Exemplary — students claim it.** **Exemplary (Level 4) is available on the Final Project only** — every other assessment is capped at Mastery (see [grading-methodology.md](grading-methodology.md)). On the project, Level 4 is not something the instructor hunts for across 90 students. To be scored Exemplary on a criterion, **the student points to the specific evidence** — the test file, the slide, the commit, the journey-map detail — that shows they went beyond Mastery. *No claim, no Level 4.* This keeps grading defensible (you verify a claim rather than detect excellence cold), reduces detection workload, and channels students' strong motivation into producing visible evidence instead of disputing scores. Claims are due **with** the deliverable (a short "where I exceeded" note or Canvas comment).
- **Team CLOs (CLO3, CLO5) carry team and individual signal.** CLO3 is scored at both the **individual** level (each student's own responsibility and collaboration) and the **team** level (shared planning and delivery). CLO5 is scored at the **team** level (the shared product and its design); each student's individual capstone contribution is captured through CLO3, not re-scored here. Criteria below are tagged *(team)* or *(individual)*.
- **CLO4 is the reusable presentation rubric** applied across all five verbal activities. For purely **written** deliverables, apply *Clarity & organization* and omit *Oral delivery*.

---

## CLO1 — Programming Fundamentals

**Outcome:** Write and debug basic programs using fundamental constructs including variables, control flow, functions, and algorithms.

| Criterion | 0 — No Evidence | 1 — Below Mastery | 2 — Near Mastery | 3 — Mastery | 4 — Exemplary (Final Project) |
|-----------|-----------------|-------------------|------------------|-------------|----------------|
| **Correctness** | Nothing to assess | Program does not run, or fails most required cases | Runs but fails one required case | Produces the required behavior in all specified cases | Also handles edge cases and unexpected input gracefully |
| **Use of constructs** | Nothing to assess | Misuses or avoids core constructs | Uses constructs but with errors or needless redundancy | Selects and uses appropriate constructs (variables, control flow, custom blocks/functions, algorithms) correctly, in readable code | Also applies a new algorithm beyond those taught, correctly, and can explain how it works |

---

## CLO2 — System Analysis (User Journey & Process Mapping)

**Outcome:** Apply User Journey Analysis and Process Mapping to a system, and recommend design improvements justified by that analysis.

| Criterion | 0 — No Evidence | 1 — Below Mastery | 2 — Near Mastery | 3 — Mastery | 4 — Exemplary (Final Project) |
|-----------|-----------------|-------------------|------------------|-------------|----------------|
| **User journey analysis & improvement** | Nothing to assess | Journey missing or inaccurate, and no usable recommendation | Captures some of the journey but with gaps, and improvements are generic or weakly grounded in it | Maps a complete, accurate journey of the user's experience (key stages, touchpoints, pain points) **and** recommends improvements justified by it, revising the design through one iteration | Also closes the loop — re-tests the revised design and shows, with before/after evidence, that the targeted pain point measurably eased — **or** reconciles multiple user segments / journeys in one design |
| **Process Mapping** | Nothing to assess | Absent or incorrect notation | Partial map; flow unclear | Documents a clear, correct map of the system's internal process flow — its steps and their sequence, distinct from the user's experience | Also adds decision points, exceptions, or responsibility lanes (interactions between actors/components) |

---

## CLO3 — Teamwork & Collaboration

**Outcome:** Collaborate in a team to plan, manage, and deliver assignments and projects, fulfilling individual responsibilities and contributing to shared goals.

| Criterion | 0 — No Evidence | 1 — Below Mastery | 2 — Near Mastery | 3 — Mastery | 4 — Exemplary (Final Project) |
|-----------|-----------------|-------------------|------------------|-------------|----------------|
| **Individual responsibility & collaboration** *(individual)* | No evidence | Little or no contribution; disengaged or misses commitments | Inconsistent; needs reminders, and communicates sporadically | Reliably completes own assigned share on time, **and** communicates and cooperates respectfully toward shared goals | Also takes on extra work, or actively improves how the team works — unblocks a teammate, proposes or improves a process, or synthesizes others' ideas into a shared decision |
| **Planning & delivery** *(team)* | No evidence | No planning; work uncoordinated; fails to deliver | Plans loosely; tasks tracked unevenly; delivers late or incomplete | Plans and tracks the work to stay on schedule, **and** delivers the complete assignment or project as required | Also strengthens the plan up front (checkpoints, contingencies, workload rebalancing), or delivers early or beyond the required scope or quality |

---

## CLO4 — Communication (Reusable Presentation Rubric)

**Outcome:** Communicate engineering concepts clearly in written form and in oral presentation.

| Criterion | 0 — No Evidence | 1 — Below Mastery | 2 — Near Mastery | 3 — Mastery | 4 — Exemplary (Final Project) |
|-----------|-----------------|-------------------|------------------|-------------|----------------|
| **Clarity & organization** | No evidence | Disorganized; hard to follow | Some structure; clarity uneven | Clear and well-organized; the audience can follow easily | Also notably concise and compelling, or adapts to the audience |
| **Oral delivery** | No evidence | Unclear; reads slides; no engagement | Hesitant; limited engagement | Clear, confident, well-paced delivery; answers questions adequately | Also engaging, and handles questions skillfully |

---

## CLO5 — Capstone Integration

**Outcome:** Design and build a complete software application that integrates programming, system analysis, teamwork, and communication, taking it from initial concept to a working product.

| Criterion | 0 — No Evidence | 1 — Below Mastery | 2 — Near Mastery | 3 — Mastery | 4 — Exemplary (Final Project) |
|-----------|-----------------|-------------------|------------------|-------------|----------------|
| **Working product** *(team)* | Nothing to assess | Largely non-functional | Partially works; misses core requirements | Application works and meets its core requirements | Also robust or polished, or exceeds the required scope |
| **Design & integration** *(team)* | Nothing to assess | Components disconnected; no evident design | Loosely integrated; design weakly informed by analysis | A coherent product, designed from the analysis and built with sound programming, taken from concept to a working build | Also shows thoughtful or innovative design, or clear reflection on trade-offs |

---

## Claiming Exemplary on the Final Project

Exemplary (Level 4) is earned on the **Final Project only**, and it is **claimed, not hunted** — the student points to specific evidence with the deliverable (see the claim-rule bullets under [How the rubrics work](#how-the-rubrics-work)). This table records, per criterion, what *beyond Mastery* means and the evidence a student must provide to claim it. **One path is enough.**

| CLO · criterion | Beyond Mastery (one path is enough) | Evidence to point to |
|---|---|---|
| **CLO1 (a)** — Correctness | Handles edge cases / invalid input, not just the required cases | A test or demo run exercising edge cases (empty, boundary, invalid input). |
| **CLO1 (b)** — Use of constructs | Applies a new algorithm beyond those taught, correctly | The code, the algorithm named, + description on how it works. |
| **CLO2 (a)** — User journey analysis & improvement | Demonstrates measurable impact — before/after evidence that the targeted pain point eased — **or** reconciles multiple user segments / journeys in one design | **Impact:** user-test notes or before/after feedback showing the targeted pain point eased after the redesign. **Multi-segment:** a journey map covering ≥2 player types or paths — e.g. difficulty modes or accessibility options serving casual vs. skilled players — plus the design decision that reconciles their conflicting needs. |
| **CLO2 (b)** — Process Mapping | Adds decision points, exceptions, or responsibility lanes (interactions between actors/components) beyond a linear flow | The map, pointing to the branch/exception path or the actor/component lanes. |
| **CLO3 (a)** — Individual responsibility & collaboration | Takes on extra work, **or** improves how the team works (unblocks, improves a process, synthesizes ideas) | A commit/PR, chat or meeting log, or peer-eval comment naming what you did and its effect. |
| **CLO3 (b)** — Planning & delivery | Stronger plan up front (checkpoints, contingencies, rebalancing), **or** early / expanded delivery | The plan artifact showing it, **or** a delivery record. |
| **CLO4 (a)** — Clarity & organization | Notably concise and compelling, **or** adapts to the audience | The slide or section where you tailored or distilled, + one line on the choice. |
| **CLO4 (b)** — Oral delivery | Engaging, **and** handles questions skillfully | A recording/timestamp of a Q&A moment handled well. |
| **CLO5 (a)** — Working product | Robust / polished, **or** beyond the required scope | The extra feature, **or** robustness handling (error states, edge cases) in the demo/repo. |
| **CLO5 (b)** — Design & integration | Thoughtful / innovative design, **or** clear reflection on trade-offs | A design note, sketch, or decision log showing the choice or the trade-offs weighed. |

---

### Rollout tips
- Share each rubric with students **before** the activity — the rubric is also the instruction sheet.
- Keep the 0–4 scale and the Level-3-anchored wording identical across CLOs so grades are comparable.
- The reusable CLO4 rubric lets students see their presentation skill improve across all five verbal activities.
- **Tell students how Exemplary works up front:** Exemplary is earned on the **Final Project only**, and it's claimed, not hunted — point to the evidence with the deliverable. Meeting all targets earns a B; an Exemplary Final Project is what lifts the grade to B+ and A, up to a 90% ceiling (see [grading-methodology.md](grading-methodology.md)). This sets expectations before the grade-bearing work begins.

