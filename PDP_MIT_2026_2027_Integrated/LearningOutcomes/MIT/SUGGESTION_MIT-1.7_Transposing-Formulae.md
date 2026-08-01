# SUGGESTION: Transposing formulae & rational algebraic expressions

> **Learning outcome at stake:** MIT 5N18396, 1.7 — "Transpose formulae and perform arithmetic operations on polynomials and rational algebraic expressions."
> **Status:** Weak/partial gap. `mathematics/markdown/worksheet_01_fractions.md` and `worksheet_01a_fractions_fundamentals.md` cover algebraic fraction simplification and arithmetic well, but "transposing formulae" — rearranging an equation to isolate a different variable (e.g. rearranging `A = πr²` to solve for `r`) — isn't explicitly taught anywhere in `everlearning`, `mathematics`, or the programming repos.

## Why this gap matters

Transposing formulae is one of the most directly *vocational* skills in the whole MIT syllabus — it's exactly what students will do constantly once they're programming (rearranging a formula to solve for the variable they actually need) and it connects cleanly to the geometry formulas already taught in `Tutorial_13_Numbers_and_Their_Families.ipynb` (area, volume, surface area) — those are natural rearrangement targets.

## Suggested approach

This is a good candidate for a short **pen-and-paper** worksheet, since transposition is fundamentally an algebraic manipulation skill best practised by hand before automating it — but it should explicitly reuse formulas students already know from `Tutorial_13`, rather than introducing new ones, so the cognitive load is just "rearrange," not "also learn a new formula."

A worksheet built around the existing geometry/physics formulas already in the curriculum:
- Rearrange `A = πr²` to solve for `r`.
- Rearrange the volume of a cylinder, `V = πr²h`, to solve for `h`.
- Rearrange the quadratic-formula-adjacent `s = ut + ½at²`-style physics formulas (if used elsewhere) for a different variable.
- A short section specifically on rational algebraic expressions: simplify `(a/b) / (c/d)`-style compound fractions where `a`, `b`, `c`, `d` are themselves polynomials — this is the piece not fully covered by the existing fractions worksheets, which focus more on numeric/simple algebraic fractions.

## Suggested file structure

A short worksheet, `LearningOutcomes/MIT/MIT-1.7_Transposing-Formulae.md`, once written — following the same pen-and-paper-with-answer-key format as the pulled-in `mathematics` worksheets in this folder.

## Fun reinforcement idea

Turn it into a "formula toolkit" exercise tied to the programming side: for each geometry formula in `Tutorial_13`, write a *family* of functions — `circle_area(r)`, `circle_radius_from_area(A)`, `cylinder_volume(r, h)`, `cylinder_height_from_volume(V, r)` — where each "inverse" function is only correct if it was derived by transposing the original formula by hand first, then implemented. This turns a purely algebraic skill into a testable programming exercise (verify `circle_radius_from_area(circle_area(5))` returns `5`), reusing the verification-by-round-trip pattern already established in `Tutorial_14`/`Tutorial_15`.
