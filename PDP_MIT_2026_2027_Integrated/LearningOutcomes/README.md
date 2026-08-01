# Learning Outcomes

This folder fills in curriculum gaps for the MIT/PDP learning outcomes — content that wasn't otherwise covered anywhere in the day-to-day teaching sequence. It's organised alongside — not instead of — the existing `Tutorials/` and `SkillsDemos/` folders, which remain the primary day-to-day teaching sequence.

## What's here

- **`MIT/`** — content mapped to Maths for Information Technology (5N18396) learning outcomes.
- **`PDP/`** — content mapped to Programming & Design Principles (5N2927) learning outcomes.

## Naming convention

Files are named `<Module>-<LO number(s)>_<Short-Title>.<ext>`, e.g. `MIT-4.5-4.7_Radians-and-the-Unit-Circle.md` or `PDP-LO9_LO10_Reading-Compiler-Errors-and-Debugging.ipynb`. Where one source file naturally covers several sub-outcomes at once (the usual case — a worksheet rarely maps 1:1 to a single numbered outcome), the filename lists all of them rather than being artificially split apart.

Files prefixed `SUGGESTION_` are **not filled-in content** — they're a gap description plus a concrete plan for closing it, for outcomes where nothing existing covers the topic. Each one includes a suggested teaching method (programming exercise, pen-and-paper, board-work, or a hybrid), a suggested file/tutorial structure, and a short "fun reinforcement idea" for making the eventual content stick, in the same spirit as the existing "Fun" skills-demo track (`NB1_The_Number_Detective.ipynb`, `NB2_Casino_Night.ipynb`, `NB3_The_Algebra_Sketchpad.ipynb`).

## What's filled in vs. newly built vs. still a gap

**Worksheets adapted for this curriculum** (9 files, `MIT/` folder, no `SUGGESTION_` prefix) — this closes MIT Section 4 (Geometry & Trigonometry) entirely, plus the calculus/graphing content (3.2 partial, 3.3, 3.4, 3.6, 3.7) that previously wasn't covered here at all.

**A dedicated debugging treatment** (1 file, `PDP/PDP-LO9_LO10_Reading-Compiler-Errors-and-Debugging.ipynb`) — covers interpreting compiler/runtime errors and structured debugging (PDP LO9/LO10).

**Newly built, not adapted from anything** (`PDP/PDP-LO1_LO3_MIT-1.4_The-Computing-Time-Machine.ipynb`) — a from-scratch notebook combining PDP LO1 (history of programming) and LO3 (differentiating languages/paradigms) with a fun "time-travelling codebreaker" framing that reuses and reinforces the MIT 1.4 binary/hex skills students already have from `Tutorial_02` and the NB1 skills demos, rather than teaching binary a second time in isolation.

**Recursion, closing a consistency gap** (`MIT/MIT-6.8_Recursion-Fibonacci-and-Big-O.ipynb`) — closes the "recursion required in the Fun track but only optional in the Boring track" inconsistency flagged in `SUGGESTION_MIT-Verify-Minor-Gaps.md`, by giving recursion its own dedicated required treatment (naive vs. memoized vs. iterative Fibonacci, with the O(2ⁿ)-vs-O(n) difference made concrete) that either track can assign.

**Still genuine gaps, `SUGGESTION_` files only** — no existing content anywhere to build from, so these describe the plan rather than the finished material:

| File | Gap |
|---|---|
| `MIT/SUGGESTION_MIT-2_Sets-Venn-Truth-Tables-DeMorgan.md` | Venn diagrams, truth tables, De Morgan's Laws, Cartesian product, power set, complex number set ℂ |
| `MIT/SUGGESTION_MIT-1.10_Complex-Roots.md` | Quadratic formula never produces complex roots anywhere in the curriculum |
| `MIT/SUGGESTION_MIT-1.7_Transposing-Formulae.md` | Rearranging formulas for a different variable; rational algebraic expression arithmetic |
| `MIT/SUGGESTION_MIT-3.1-3.2_Functions-and-Graphing.md` | Inverse functions; linear/cubic graphing; solving `f(x)=g(x)` via graph intersection |
| `MIT/SUGGESTION_MIT-3.5_Limits.md` | The formal concept of a limit (a prerequisite the existing derivative content quietly skips) |
| `MIT/SUGGESTION_MIT-Verify-Minor-Gaps.md` | Small completeness checks: cube/cone formulas, stem-and-leaf plots, recursion/shell-sort consistency between the Boring/Fun tracks |
| `PDP/SUGGESTION_PDP-LO8_Team-Programming-Project.md` | A real teams-of-3–5, release-and-review software project — the most significant PDP gap found; nothing existing currently satisfies this |
