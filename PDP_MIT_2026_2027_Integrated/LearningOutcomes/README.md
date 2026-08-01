# Learning Outcomes

This folder makes `everlearning` self-sufficient for the MIT/PDP curriculum gaps identified in [`../../planning/mit-pdp-coverage-gap-analysis.md`](../../planning/mit-pdp-coverage-gap-analysis.md), so we no longer need to reach into the `mathematics`, `python-with-ml`, or `2plus1coding` repos to teach this material. It's organised alongside — not instead of — the existing `Tutorials/` and `SkillsDemos/` folders, which remain the primary day-to-day teaching sequence.

## What's here

- **`MIT/`** — content mapped to Maths for Information Technology (5N18396) learning outcomes.
- **`PDP/`** — content mapped to Programming & Design Principles (5N2927) learning outcomes.

## Naming convention

Files are named `<Module>-<LO number(s)>_<Short-Title>.<ext>`, e.g. `MIT-4.5-4.7_Radians-and-the-Unit-Circle.md` or `PDP-LO9_LO10_Reading-Compiler-Errors-and-Debugging.ipynb`. Where one source file naturally covers several sub-outcomes at once (the usual case — a worksheet rarely maps 1:1 to a single numbered outcome), the filename lists all of them rather than being artificially split apart.

Files prefixed `SUGGESTION_` are **not filled-in content** — they're a gap description plus a concrete plan for closing it, for outcomes where no existing material (in any of the four repos) covers the topic. Each one includes a suggested teaching method (programming exercise, pen-and-paper, board-work, or a hybrid), a suggested file/tutorial structure, and — per the brief for this pass — a short "fun reinforcement idea" for making the eventual content stick, in the same spirit as the existing "Fun" skills-demo track (`NB1_The_Number_Detective.ipynb`, `NB2_Casino_Night.ipynb`, `NB3_The_Algebra_Sketchpad.ipynb`).

## What was pulled in vs. newly built vs. still a gap

**Pulled in from `mathematics`** (9 files, `MIT/` folder, no `SUGGESTION_` prefix) — this closes MIT Section 4 (Geometry & Trigonometry) entirely, plus the calculus/graphing content (3.2 partial, 3.3, 3.4, 3.6, 3.7) that previously only existed as pen-and-paper worksheets in a different repo. Each file carries a provenance header noting the original `mathematics` path.

**Pulled in from `python-with-ml`** (1 file, `PDP/PDP-LO9_LO10_Reading-Compiler-Errors-and-Debugging.ipynb`) — the most dedicated existing treatment of interpreting compiler/runtime errors and structured debugging (PDP LO9/LO10), copied over as-is.

**Newly built, not a copy of anything** (`PDP/PDP-LO1_LO3_MIT-1.4_The-Computing-Time-Machine.ipynb`) — a from-scratch notebook combining PDP LO1 (history of programming) and LO3 (differentiating languages/paradigms) with a fun "time-travelling codebreaker" framing that reuses and reinforces the MIT 1.4 binary/hex skills students already have from `Tutorial_02` and the NB1 skills demos, rather than teaching binary a second time in isolation. This is the "combine history-of-computing and binary into one new tutorial" piece specifically requested for this pass.

**Still genuine gaps, `SUGGESTION_` files only** — no existing content anywhere to pull from, so these describe the plan rather than the finished material:

| File | Gap |
|---|---|
| `MIT/SUGGESTION_MIT-2_Sets-Venn-Truth-Tables-DeMorgan.md` | Venn diagrams, truth tables, De Morgan's Laws, Cartesian product, power set, complex number set ℂ |
| `MIT/SUGGESTION_MIT-1.10_Complex-Roots.md` | Quadratic formula never produces complex roots anywhere in the curriculum |
| `MIT/SUGGESTION_MIT-1.7_Transposing-Formulae.md` | Rearranging formulas for a different variable; rational algebraic expression arithmetic |
| `MIT/SUGGESTION_MIT-3.1-3.2_Functions-and-Graphing.md` | Inverse functions; linear/cubic graphing; solving `f(x)=g(x)` via graph intersection |
| `MIT/SUGGESTION_MIT-3.5_Limits.md` | The formal concept of a limit (a prerequisite the existing derivative content quietly skips) |
| `MIT/SUGGESTION_MIT-Verify-Minor-Gaps.md` | Small completeness checks: cube/cone formulas, stem-and-leaf plots, recursion/shell-sort consistency between the Boring/Fun tracks |
| `PDP/SUGGESTION_PDP-LO8_Team-Programming-Project.md` | A real teams-of-3–5, release-and-review software project — the most significant PDP gap found; nothing in any of the four repos currently satisfies this |

## Relationship to `planning/`

The [`planning/`](../../planning/) folder one level up has the full picture this folder is built from: `repo-inventory.md` (what existed where before this pass) and `mit-pdp-coverage-gap-analysis.md` (the full learning-outcome-by-learning-outcome table). Treat this `LearningOutcomes/` folder as the working answer to those gaps — as more of the `SUGGESTION_` files get built out into real content, update the corresponding row in `mit-pdp-coverage-gap-analysis.md` rather than letting the two drift apart.
