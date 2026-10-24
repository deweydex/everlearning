# SUGGESTION: A real team-programming project for PDP LO8

> **Learning outcome at stake:** PDP 5N2927, LO8 — "Work as part of a team to design, develop, release and review multiple versions of a multi-modular program over an extended period of time." Assessed as Skills Demonstration 2 (40%) per the module descriptor, for teams of 3–5 learners.
> **Status:** Confirmed as the most significant PDP gap in this curriculum. `everlearning`'s own plan (`SkillsDemos/BoringPDPandMIT-SkillsDemos/NB4_Group_Portion_Ideas.md`) is an optional, **ungraded**, calculus-content activity (patching the MIT 3.2–3.7/4.1–4.10 gaps via group work) rather than a graded software project — good content, wrong learning outcome. Nothing currently in this curriculum sets up a genuine teams-of-3–5, extended-over-time, release-and-review project — the closest existing material is built around **pairs** (2 people, one 80–90 minute session), not teams of 3–5 over an extended period, and doesn't cover team-based development at all.

## Why this gap matters

LO8 isn't a "nice to have" — it's 40% of the PDP Skills Demonstration grade (Skills Demonstration 2), and the module descriptor is specific about what it requires: teams of 3–5, a top-down algorithm/pseudocode, modularisation with parameter passing, at least one function that returns a value, at least one system-defined function, real test data, and a **released** solution with evidence of each team member's individual contribution. None of the current material, however good it is on its own terms, satisfies that combination.

## Suggested approach

The good news: `everlearning`'s own tutorial sequence already teaches every *individual* skill this project needs — modularisation (`Tutorial_08_Building_Reusable_Tools.ipynb`), testing (`Tutorial_07`, `Tutorial_08`), and the full toolkit of polynomial/equation/set functions built across `Tutorial_13`–`Tutorial_17` that a team project could assemble into something bigger. What's missing is the *team* structure and the *extended-over-time* release/review cycle — that's a project-management design problem more than a content problem.

A concrete shape for the project:

1. **Pick a problem big enough to need modularisation across 3–5 people, but built from tools students already have.** Two natural options that reuse existing tutorial content instead of inventing something from scratch:
   - **A "Maths Toolkit" command-line app**: combine the polynomial, equation-solving, set, and statistics functions already built individually across Tutorials 09–17 into one integrated program with a menu, where each team member owns one module (e.g. one person owns polynomial operations, another owns equation solving, another owns sets, another owns stats/probability) and they integrate their pieces together — this doubles as excellent revision for the MIT skills-demo content, taught through PDP's team-project lens.
   - **A small game or simulation**, scaled up to a real team: e.g. a dice/card probability simulator that reuses the counting/probability functions from `Tutorial_09`/`Tutorial_10`, with different team members responsible for different game mechanics, statistics tracking, and the display/menu layer.
2. **Structure it explicitly around the module descriptor's required stages**, not just "go build something": problem discussion → candidate solutions → chosen solution → top-down pseudocode with modules assigned to team members → individual module development with agreed parameter/return-value contracts → integration → testing with real test data → a **released** version → a **second, revised version** after review (the "multiple versions... release and review" language in the LO is specific — a single final submission doesn't satisfy it).
3. **Build in individual-contribution evidence from the start** — a shared dev log or a simple per-person git commit history (if the class uses source control) rather than trying to reconstruct who-did-what after the fact, since `everlearning`'s own draft marking scheme for the group portion (in `NB4_Group_Portion_Ideas.md`) already flags "individual contribution/reflection" as something to grade.
4. **Timing:** the module descriptor allows 10 hours per skills demonstration and expects this to run "over an extended period of time" — closer to an incremental, staged development process than a single sitting, but scaled from one 80-minute session to multiple work sessions across a few weeks.

## Suggested file structure

A new top-level unit, e.g. `PDP_MIT_2026_2027_Integrated/SkillsDemos/TeamProject/`, containing: a facilitator/assessor brief (clear and concise, scaled to teams and multiple sessions), a student-facing project brief with the staged milestones above, a shared `PROJECT_PLANNING.md`-style template (adapted for a team rather than a pair), and a marking rubric that explicitly covers algorithm/pseudocode, modularisation, testing, coding standards, and team contribution — mirroring the module descriptor's Skills Demonstration 2 marking sheet almost line for line.

## Fun reinforcement idea

Give the "released, reviewed, re-released" cycle a concrete narrative: each team "ships" their v1 to another team (a code + a one-page README), that team plays with it and files 2–3 "bug reports" or feature requests as if they were real users, and the original team addresses at least one of them in a v2 release. This is a light, low-overhead way to make "release and review multiple versions" feel like real software practice rather than an abstract instruction, and it naturally produces the two required versions plus genuine evidence of iteration.
