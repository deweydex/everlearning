# SUGGESTION: The concept of a limit

> **Learning outcome at stake:** MIT 5N18396, 3.5 — "Investigate the concept of the limit of a function and compute the limits of linear, quadratic and quotient functions and understand the idea of a continuous function."
> **Status:** Confirmed gap, and explicitly named as one in `SkillsDemos/BoringPDPandMIT-SkillsDemos/NB4_Group_Portion_Ideas.md` ("limits (3.5)... not covered by the assignments"). An existing fractions worksheet touches informal limiting behaviour of formulas (e.g. "what happens as n→∞") but doesn't build the formal limit concept the LO calls for, and it isn't specific to MIT's linear/quadratic/quotient-function scope.

## Why this gap matters

Limits are the one purely conceptual, non-computational piece of MIT Section 3 — everything else in the section (graphing, completing the square, derivatives, differentiation rules) is now covered somewhere in the repo, but the *idea* that a derivative "arises as a limit" (3.6, which is covered) is hard to teach honestly without first building the limit concept itself (3.5). Right now that dependency is skipped.

## Suggested approach

Limits are unusually well suited to a **hybrid pen-and-paper + programming** approach, because the core intuition — "what value does the function approach, even if it's not defined exactly there?" — is easiest to *see* numerically before it's proven algebraically:

1. **Numerical exploration (programming):** for a quotient function with a removable discontinuity, e.g. `f(x) = (x**2 - 4) / (x - 2)`, evaluate it at `x = 1.9, 1.99, 1.999, 2.001, 2.01, 2.1` and watch the outputs converge to 4, even though `f(2)` itself is undefined (division by zero). This is a short, satisfying exercise students can run themselves and see the pattern.
2. **Algebraic confirmation (pen-and-paper):** factor and cancel, `(x-2)(x+2)/(x-2) = x+2`, confirming the limit is `4` algebraically — connecting the numerical pattern to the factoring skills already built in `Tutorial_15`/`worksheet_03b`.
3. **Continuity, informally:** contrast a function that *is* continuous at a point (limit exists and equals the function value) against the quotient example above (limit exists, but the function itself is undefined there) — this is exactly the setup MIT 3.6 needs before "a derivative arises as a limit" makes sense.
4. Limits of linear and quadratic functions are the easy case (just plug in the value — they're continuous everywhere), so most of the exercise time should go to the quotient-function case where the interesting behaviour is.

## Suggested file structure

A short new worksheet/notebook — either pen-and-paper (`LearningOutcomes/MIT/MIT-3.5_Limits.md`, in the style of the other worksheets in this folder) or a light notebook if the numerical-exploration approach above is preferred, since evaluating a function at a sequence of x-values is a natural fit for a few lines of Python and a `matplotlib` plot showing the "hole" in the graph being approached from both sides.

## Fun reinforcement idea

"The Approaching Train" — frame the numerical exploration as watching a value approach a station without ever quite arriving (or arriving from a different platform than expected, for the discontinuous case), with a short animated/step-by-step print of the sequence of x and f(x) values getting closer and closer. It's a small framing change, but it gives students a concrete mental image for "limit" before the formal definition, similar in spirit to how `Tutorial_06_Finding_Things.ipynb` uses divide-and-conquer intuition before naming binary search.
