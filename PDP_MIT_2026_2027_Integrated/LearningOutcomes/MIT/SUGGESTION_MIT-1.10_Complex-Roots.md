# SUGGESTION: Extending the quadratic formula to complex roots

> **Learning outcome at stake:** MIT 5N18396, 1.10 — "Solve quadratic equations with real **and complex** roots by factorisation or formula."
> **Status:** Confirmed gap. Every existing implementation — `Tutorials/BoringTutorials/Tutorial_15_Cracking_Equations.ipynb`, `SkillsDemos/BoringPDPandMIT-SkillsDemos/NB3_...The_Algebra_Engine.ipynb`, `SkillsDemos/FunPDPandMIT-SkillsDemos/NB3_The_Algebra_Sketchpad.ipynb` — treats a negative discriminant as "no real roots" and stops there. `FunPDPandMIT-SkillsDemos/NB3` even says so explicitly in a code comment: *"complex roots exist but we will keep things real."*

## Why this gap matters

This is the smallest gap in the whole analysis to close — the machinery (discriminant, quadratic formula) is already fully built and taught; what's missing is one more case in an existing function.

## Suggested approach

This is squarely a **programming exercise**, and a light one — it's a direct extension of `solve_quadratic()` in `Tutorial_15_Cracking_Equations.ipynb`, not a new topic. Python's `complex` type and `cmath` module make this genuinely simple:

```python
import cmath

def solve_quadratic_complex(a, b, c):
    discriminant = b**2 - 4*a*c
    root = cmath.sqrt(discriminant)  # cmath.sqrt handles negative numbers natively
    x1 = (-b + root) / (2*a)
    x2 = (-b - root) / (2*a)
    return x1, x2
```

`cmath.sqrt(-4)` returns `2j` directly — no manual "pull out the `i`" logic needed, which keeps the exercise about *interpreting* complex roots (What does a+bi mean here? Why do complex roots always come in conjugate pairs for real-coefficient quadratics?) rather than fighting Python syntax.

A good exercise sequence:
1. Extend `solve_quadratic` (or add a sibling function) to always return complex roots via `cmath`, and verify: when the discriminant ≥ 0, the "complex" answer's imaginary part is exactly 0 — so the new function is a strict superset of the old one.
2. Plot a few example quadratics (reusing the graphing skills from the completing-the-square worksheet) side by side with their roots, showing visually *why* a parabola that doesn't cross the x-axis still has roots — just not real, not-plottable-on-this-axis ones.
3. A short "why do complex roots always come in conjugate pairs?" discussion/proof sketch — ties back into MIT 2.1's complex number set ℂ.

## Suggested file structure

Doesn't need a whole new file — a natural home is either as an added section at the end of `Tutorial_15_Cracking_Equations.ipynb` (or `Tutorial_17_Bringing_It_All_Together.ipynb`, which already reviews equation-solving), or a short standalone `Tutorial_15b_Complex_Roots.ipynb` if the instructor prefers to keep it separately assessable.

## Fun reinforcement idea

Frame it as "the roots that got away" — set up a few real-world quadratics (projectile motion, revenue models) where the parabola doesn't touch the x-axis, ask "does this equation have a solution?", let students discover the answer is "yes, just not one you can plot on this graph," and have them write a one-function "detector" that classifies any quadratic as real-distinct / real-repeated / complex roots before solving it — reusing the discriminant logic they already know from `Tutorial_15`, just adding the missing branch.
