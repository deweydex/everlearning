# SUGGESTION: Functions, inverse functions & full graphing coverage (linear/cubic + solving via graph)

> **Learning outcomes at stake:** MIT 5N18396 — 3.1 (a function assigns a single output to every input; inverse functions, computed in simple algebraic cases), 3.2 (graph linear, quadratic **and cubic** functions, and use the graphs to solve `f(x)=0`, `f(x)=k`, `f(x)=g(x)`).
> **Status:** Partial gap. [`MIT-3.2_3.4_Quadratic-Graphing-and-Completing-the-Square.md`](./MIT-3.2_3.4_Quadratic-Graphing-and-Completing-the-Square.md) (pulled in from `mathematics`) covers quadratic graphing thoroughly, and `FunPDPandMIT-SkillsDemos/NB3_The_Algebra_Sketchpad.ipynb` has a `plot_polynomial` function that can plot linear and quadratic functions — but linear graphing is never a dedicated exercise, cubic graphing doesn't appear anywhere, inverse functions are never computed, and "solve `f(x)=g(x)` by finding where two graphs intersect" is only lightly touched (the Algebra Sketchpad plots polynomial intersections for root-finding, not general `f(x)=g(x)` problems).

## Why this gap matters

Function/inverse-function concepts and reading solutions off a graph are core "translate between algebra and geometry" skills the module descriptor treats as foundational to Section 3 — and `everlearning` already has almost all the graphing infrastructure needed (`Tutorial_12_Pictures_Worth_Numbers.ipynb` teaches matplotlib plotting generally, and `NB3_The_Algebra_Sketchpad.ipynb` already has a working `plot_polynomial`). This is much more "extend what exists" than "build from nothing."

## Suggested approach

A **programming exercise** building directly on `Tutorial_14_Expressions_Come_Alive.ipynb`'s polynomial toolkit (`evaluate_poly`, `add_poly`, `multiply_poly`) and `NB3`'s `plot_polynomial`:

1. **Linear & cubic graphing:** extend `plot_polynomial` (or write a sibling function) to explicitly handle degree-1 and degree-3 polynomials, not just quadratics — since the underlying representation (a list of coefficients) already generalises, this is mostly about giving students dedicated practice/exercises with those degrees rather than new code.
2. **Solving via graph:** a short exercise sequence — plot `f(x) = k` as a horizontal line over a polynomial and visually find intersections; plot two polynomials `f(x)` and `g(x)` on the same axes and find where they cross; connect this back to the algebraic solving already done in `Tutorial_15` (do the graphical and algebraic answers agree?).
3. **Inverse functions:** a small, separate exercise — given a simple invertible function (e.g. `f(x) = 2x + 3` or `f(x) = x**3`), have students derive the inverse algebraically (pen-and-paper, transposition — see the [MIT 1.7 suggestion](./SUGGESTION_MIT-1.7_Transposing-Formulae.md)) and then verify it programmatically: `f(f_inverse(x)) == x` for a range of test values, and plot `f` and its inverse together to observe the reflection across `y = x`.

## Suggested file structure

A new tutorial or skills-demo-style notebook, e.g. `LearningOutcomes/MIT/MIT-3.1-3.2_Functions-Inverses-and-Graphing.ipynb`, once built — it would sit naturally as a companion to the existing `Tutorial_14`/`Tutorial_15` pair and the pulled-in `MIT-3.2_3.4` worksheet.

## Fun reinforcement idea

"Graph vs. Algebra Showdown": pose a solving problem two ways at once — one student/pair solves it algebraically (factoring, quadratic formula, or elimination, depending on the function), another solves it graphically (plot and read off the intersection) — then compare answers. This reinforces that algebra and graphing are two routes to the same truth, using content students already know, just recombined into a race/comparison format.
