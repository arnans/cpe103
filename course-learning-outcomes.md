# Basic Computer Engineering — Course Learning Outcomes (CLOs) & Rubrics

## How these outcomes were designed

Each outcome follows established good practice for learning-outcome design:

- **One coherent skill per outcome.** Each CLO names a demonstrable behavior — or a coherent cluster of closely related actions (e.g. *write, test, and debug*) — so it can be taught and assessed cleanly. What it avoids is bundling *unrelated* ideas (e.g. "show skills *and* show understanding").
- **Measurable action verbs (Bloom's taxonomy).** Vague verbs like *show*, *understand*, or *know* are replaced with verbs that name observable performance — *write, test, apply, analyze, collaborate, communicate, design, integrate*.
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
| **CLO1** | **Write, test, and debug basic programs** using fundamental constructs including variables, control flow, functions, and algorithms. |
| **CLO2** | **Apply** User Journey Analysis and Process Mapping to a system, and **recommend** design improvements justified by that analysis. |
| **CLO3** | **Collaborate** in a team to plan, manage, and deliver assignments and projects, fulfilling individual responsibilities and contributing to shared goals. |
| **CLO4** | **Communicate** engineering concepts clearly and accurately in **written** form and in **oral** presentation. |
| **CLO5** | **Design and build** a complete software application that **integrates** programming, system analysis, teamwork, and communication, taking it from initial concept to a working product. |

Each CLO has a single **master rubric**, used everywhere that CLO is assessed.

---

## How the rubrics work

- **One master rubric per CLO.** The same rubric is reused across every activity that assesses that CLO, so expectations stay consistent and students improve against a fixed standard.
- **Each criterion is scored 0–4** on the shared scale above. A CLO's score is the **average of its criteria** (equal weight). Per-criterion scores double as feedback — they show students *where* they are strong or weak, not just an overall number.
- **Anchored to the CLO.** For every criterion, **Level 3 means the student does exactly what the CLO states** (the target). **Level 4** means they meet Level 3 *and* go beyond in at least one way (the cell gives an example). Levels 2 and 1 are *approaching* and *below*; Level 0 is no evidence.
- **When a CLO counts as "Mastery" vs "Exemplary" (the grade-bearing distinction).** Because letter grades turn on this, fix **one** rule and apply it to everyone: a CLO is **Mastery** when *every* criterion is at Level 3 or above, and **Exemplary** only when it *also* has **at least half of its criteria at Level 4**. A single Level-4 cell out of three does **not** make the whole CLO Exemplary. (The criterion average still drives the within-band % score; this rule decides which *band* — and therefore which letter — the CLO lands in. Tune the "half" fraction to the distribution you want, but state it once and apply it uniformly.)
- **Earning Exemplary — students claim it.** Level 4 is not something the instructor hunts for across 90 students. To be scored Exemplary on a criterion, **the student points to the specific evidence** — the test file, the slide, the commit, the journey-map detail — that shows they went beyond Mastery. *No claim, no Level 4.* This keeps grading defensible (you verify a claim rather than detect excellence cold), reduces detection workload, and channels students' strong motivation into producing visible evidence instead of disputing scores. Claims are due **with** the deliverable (a short "where I exceeded" note or Canvas comment).
- **Team CLOs (CLO3, CLO5) are scored twice:** at the **team** level (the shared product/process) and at the **individual** level (each student's own contribution). Each criterion below is tagged *(team)* or *(individual)*; a student's CLO score combines both.
- **CLO4 is the reusable presentation rubric** applied across all five verbal activities. For purely **written** deliverables, apply the *Technical accuracy* and *Clarity & organization* criteria and omit *Oral delivery*.

---

## CLO1 — Programming Fundamentals

**Outcome:** Write, test, and debug basic programs using fundamental constructs including variables, control flow, functions, and algorithms.

**Assessed via:** programming labs and coding quizzes. Students **submit their own test cases alongside the program**, so testing and debugging are visible and gradeable (and the *Testing & debugging* Level 4 has evidence to claim).

| Criterion | 0 — No Evidence | 1 — Below Mastery | 2 — Near Mastery | 3 — Mastery | 4 — Exemplary |
|-----------|-----------------|-------------------|------------------|-------------|----------------|
| **Correctness** | Nothing to assess | Program does not run, or fails most required cases | Runs but fails several required cases | Produces correct results for all required cases | Also handles edge cases or unexpected input gracefully |
| **Use of constructs** | Nothing to assess | Misuses or avoids core constructs | Uses constructs but with errors or needless redundancy | Selects and uses appropriate constructs (variables, control flow, functions, algorithms) correctly | Also uses them efficiently, or applies a more advanced construct (e.g. recursion) where it fits |
| **Testing & debugging** | Nothing to assess | Submits no tests; cannot locate errors even with help | Submits a few tests informally; fixes errors with guidance | Submits tests covering the required cases and independently locates and fixes errors | Also submits tests for edge or failure cases beyond those required, anticipating problems before they occur |

---

## CLO2 — System Analysis (User Journey & Process Mapping)

**Outcome:** Apply User Journey Analysis and Process Mapping to a system, and recommend design improvements justified by that analysis.

**Assessed via:** a user-journey design activity on an existing project, presented orally (CLO4 also applies). User Journey is the core skill; Process Mapping is a supporting documentation tool.

| Criterion | 0 — No Evidence | 1 — Below Mastery | 2 — Near Mastery | 3 — Mastery | 4 — Exemplary |
|-----------|-----------------|-------------------|------------------|-------------|----------------|
| **User Journey Analysis** | Nothing to assess | Missing or inaccurate | Captures some steps; gaps in stages, touchpoints, or pain points | Maps a complete, accurate journey with key stages, touchpoints, and pain points | Also captures nuance — emotions, alternative paths, or edge-case users |
| **Process Mapping** *(supporting documentation)* | Nothing to assess | Absent or incorrect notation | Partial map; flow unclear | Documents a clear, correct map of the process flow | Also adds decision points, exceptions, or responsibilities |
| **Justified improvement & iteration** | Nothing to assess | No recommendation, or unrelated to the analysis | Generic suggestions not clearly grounded in the analysis | Recommends improvements justified by the analysis and revises the design through one iteration | Also weighs trade-offs or anticipates the impact of the change |

---

## CLO3 — Teamwork & Collaboration

**Outcome:** Collaborate in a team to plan, manage, and deliver assignments and projects, fulfilling individual responsibilities and contributing to shared goals.

**Assessed via:** the teamwork & task-management activity, plus team-based work throughout the course — using peer evaluation, instructor observation, and team logs/contribution records. Scored at both the individual and team level.

| Criterion | 0 — No Evidence | 1 — Below Mastery | 2 — Near Mastery | 3 — Mastery | 4 — Exemplary |
|-----------|-----------------|-------------------|------------------|-------------|----------------|
| **Individual responsibility** *(individual)* | No evidence | Little or no contribution; misses commitments | Inconsistent; needs reminders to deliver | Reliably completes own assigned share on time | Also takes on extra work or supports teammates beyond own tasks |
| **Collaboration & communication** *(individual)* | No evidence | Disengaged or disruptive | Communicates sporadically; limited cooperation | Communicates and cooperates respectfully, contributing to shared goals | Also actively improves how the team works — proposes or improves a team process, unblocks a teammate, or synthesizes others' ideas into a shared decision |
| **Planning & task management** *(team)* | No evidence | No planning; work is uncoordinated | Plans loosely; tasks tracked unevenly | Plans the work and tracks tasks to stay on schedule | Also strengthens the plan up front — builds in checkpoints or contingencies, or rebalances workload before problems force it |
| **Delivery** *(team)* | No evidence | Fails to deliver | Delivers late or incomplete | Delivers the complete assignment or project as required | Also delivers early, or exceeds the required scope or quality |

---

## CLO4 — Communication (Reusable Presentation Rubric)

**Outcome:** Communicate engineering concepts clearly and accurately in written form and in oral presentation.

**Assessed via (the same rubric each time):** user-journey design, teamwork & task management, the topic-of-choice presentation, the capstone proposal, and the capstone final (openhouse). For written-only deliverables, apply the first two criteria and omit *Oral delivery*.

| Criterion | 0 — No Evidence | 1 — Below Mastery | 2 — Near Mastery | 3 — Mastery | 4 — Exemplary |
|-----------|-----------------|-------------------|------------------|-------------|----------------|
| **Technical accuracy** | No evidence | Frequent errors or misconceptions | Some inaccuracies | Concepts are presented accurately and correctly | Also adds depth or insight beyond the brief, or proactively addresses a likely question, limitation, or trade-off |
| **Clarity & organization** | No evidence | Disorganized; hard to follow | Some structure; clarity uneven | Clear and well-organized; the audience can follow easily | Also notably concise and compelling, or adapts to the audience |
| **Oral delivery** | No evidence | Unclear; reads slides; no engagement | Hesitant; limited engagement | Clear, confident, well-paced delivery; answers questions adequately | Also engaging, and handles questions skillfully |

---

## CLO5 — Capstone Integration

**Outcome:** Design and build a complete software application that integrates programming, system analysis, teamwork, and communication, taking it from initial concept to a working product.

**Assessed via:** the capstone deliverable (working application + proposal + openhouse demo), scored at both the team and individual level. Teamwork and communication during the capstone are scored with the **CLO3** and **CLO4** rubrics, so this rubric focuses on the product, its design, and each student's build contribution (no double-counting).

| Criterion | 0 — No Evidence | 1 — Below Mastery | 2 — Near Mastery | 3 — Mastery | 4 — Exemplary |
|-----------|-----------------|-------------------|------------------|-------------|----------------|
| **Working product** *(team)* | Nothing to assess | Largely non-functional | Partially works; misses core requirements | Application works and meets its core requirements | Also robust or polished, or exceeds the required scope |
| **Design & integration** *(team)* | Nothing to assess | Components disconnected; no evident design | Loosely integrated; design weakly informed by analysis | A coherent product, designed from the analysis and built with sound programming, taken from concept to a working build | Also shows thoughtful or innovative design, or clear reflection on trade-offs |
| **Individual contribution** *(individual)* | No evidence | Little or no identifiable contribution | Limited contribution; relied heavily on others | Made a clear, identifiable contribution, fulfilling own role in the build | Also contributed beyond own role, or drove a key part of the build |

---

## Activity → CLO / rubric map

| Activity | Primary CLO(s) | Rubric(s) applied |
|----------|----------------|-------------------|
| Programming labs / coding quizzes | CLO1 | CLO1 |
| User-journey design (on an existing project) | CLO2 | CLO2 + CLO4 |
| Teamwork & task management | CLO3 | CLO3 + CLO4 |
| Topic-of-choice presentation | CLO4 | CLO4 |
| Capstone proposal | CLO5 (planning) | CLO4 |
| Capstone final (openhouse) | CLO5 | CLO5 + CLO4 + CLO3 |

---

### Rollout tips
- Share each rubric with students **before** the activity — the rubric is also the instruction sheet.
- Keep the 0–4 scale and the Level-3-anchored wording identical across CLOs so grades are comparable.
- The reusable CLO4 rubric lets students see their presentation skill improve across all five verbal activities.
- **Tell students how Exemplary works up front:** it's claimed, not hunted — point to the evidence with the deliverable — and a CLO only counts as Exemplary when at least half its criteria reach Level 4. This sets expectations before the grade-bearing work begins.

