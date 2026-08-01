# MIT / PDP Module Descriptor Coverage & Gap Analysis

_Last updated: 2026-08-01_

This maps every learning outcome in the two QQI Level 5 module descriptors —
**Maths for Information Technology 5N18396** (MIT) and **Programming & Design
Principles 5N2927** (PDP) — against what actually exists across
`everlearning`, `mathematics`, `2plus1coding`, and `python-with-ml`. Every row
below was checked by opening the actual worksheet/notebook content, not by
matching filenames, so "covered" means the sub-topic is genuinely taught or
practised there.

Companion doc: [`repo-inventory.md`](./repo-inventory.md) has the plain
per-repo file listing this table draws on.

**Columns:**
- **Subject / sub-subject** — the exact wording (or a close paraphrase) of the module descriptor's learning outcome.
- **Coverage** — `Tutorial` (a self-directed notebook/worksheet exists), `Assessment` (only shows up in a graded skills-demo/exercise, not a teaching tutorial), `Not covered`, or `Other` (e.g. planned-but-ungraded).
- **Teaching method** — `Programming exercises`, `Pen-and-paper exercises`, `Board-work` (nothing currently uses this — flagged where it'd be a natural fit for a gap), `External resources`, or `Other`.
- **Source repo(s)** — where the content currently lives.
- **Tutorial file path(s)** — the teaching/walkthrough material.
- **Exercise / assessment file path(s)** — where it's practised or assessed (often the same notebook as the tutorial, since these are exercise-embedded notebooks).
- **Notes** — the specific gap or caveat that a filename alone wouldn't tell you.

---

## Key gaps at a glance

> **Update (2026-08-01, second pass):** MIT Section 4 in full, the 3.3/3.4/3.6/3.7 calculus content, PDP LO1/LO3 (via a newly-built combined tutorial), and PDP LO9 have all now been pulled/built directly into `everlearning` under [`PDP_MIT_2026_2027_Integrated/LearningOutcomes/`](../PDP_MIT_2026_2027_Integrated/LearningOutcomes/README.md) — see that folder's README for what moved where. `everlearning` no longer needs to reach into `mathematics` or `python-with-ml` for those outcomes. The table below still names the original source repos for provenance, but the "Tutorial file path(s)" columns now point at the local copies. Items 1, 2, and 6 below are **resolved**; items 3, 4, 5 and the `python-with-ml`-specific note in item 7 remain genuine gaps, now tracked as `SUGGESTION_*` files in that same folder rather than open-ended notes here.

1. ~~**MIT Section 4 (Geometry & Trigonometry) — zero coverage in `everlearning`.**~~ **Resolved.** All of coordinate geometry, right-triangle trig, radians/unit circle, and the Sine/Cosine rules are now local to `everlearning` (`LearningOutcomes/MIT/MIT-4.*`).
2. ~~**MIT Section 3 (Functions & Calculus) — mostly missing from `everlearning`.**~~ **Mostly resolved.** 3.3 (trig graphing), 3.4 (completing the square), 3.6 (derivatives), and 3.7 (product/quotient/chain rule) are now local (`LearningOutcomes/MIT/MIT-3.*`). Still open: 3.1 (inverse functions) and the linear/cubic-graphing half of 3.2, and 3.5 (limits) — see `SUGGESTION_MIT-3.1-3.2_Functions-and-Graphing.md` and `SUGGESTION_MIT-3.5_Limits.md`.
3. **MIT Section 2's "hard half" is still missing everywhere.** Set operations (union/intersection/difference) are well covered, but **Venn diagrams, truth tables, De Morgan's Laws, the complex number set ℂ, Cartesian product, and power set** appear in none of the four repos. Tracked in `SUGGESTION_MIT-2_Sets-Venn-Truth-Tables-DeMorgan.md`.
4. **MIT 1.10 — complex roots of the quadratic formula are still never computed.** Every implementation (`everlearning` Tutorial 15, both Boring/Fun Algebra skills demos, `mathematics` worksheet_03b) stops at "no real solutions" for a negative discriminant. Tracked in `SUGGESTION_MIT-1.10_Complex-Roots.md`.
5. **PDP LO8 (team of 3–5, releasing/reviewing multiple versions over time) is still not genuinely satisfied anywhere.** `2plus1coding` is explicitly pair-only by design; `everlearning`'s own team-work plan is optional, ungraded, and calculus-focused rather than a multi-week software project with a release/review cycle. Tracked in `SUGGESTION_PDP-LO8_Team-Programming-Project.md`.
6. ~~**PDP LO1 (history of programming) isn't in `everlearning`'s own tutorials.**~~ **Resolved** — `LearningOutcomes/PDP/PDP-LO1_LO3_MIT-1.4_The-Computing-Time-Machine.ipynb` is a newly-built tutorial covering PDP LO1 and LO3 together, framed around reinforcing the MIT 1.4 binary/hex skills students already have.
7. **Sort/search algorithms (MIT 6.8) are uniquely `everlearning`'s territory** — neither `mathematics`, `2plus1coding`, nor `python-with-ml` implement bubble/insertion/selection/shell sort or binary search as a taught topic. Within `everlearning`, shell sort and recursion are inconsistently required: optional in the "Boring" track, required in the "Fun" track (Fibonacci recursion). Tracked (as a consistency question, not a coverage gap) in `SUGGESTION_MIT-Verify-Minor-Gaps.md`.
8. **`python-with-ml`'s Tutorial_4 (Selection Structures & Decision Making) was planned and never delivered** — but `everlearning`'s own `Tutorial_03_Making_Decisions.ipynb` already covers that ground, so it's a gap in that source repo specifically, not in the curriculum overall. No action taken.

---

## MIT 5N18396 — Maths for Information Technology

### Section 1: Basic Arithmetic and Algebra

| Subject / sub-subject | Coverage | Teaching method | Source repo(s) | Tutorial file path(s) | Exercise / assessment path(s) | Notes |
|---|---|---|---|---|---|---|
| 1.1 Ops in N/Z/Q/R; indices & logarithms | Tutorial | Programming + Pen-and-paper | everlearning, mathematics | `everlearning/PDP_MIT_2026_2027_Integrated/Tutorials/BoringTutorials/Tutorial_13_Numbers_and_Their_Families.ipynb` | same file; also `mathematics/worksheet_01_exponents_and_logarithms.md` | Well covered, two teaching modes available |
| 1.2 Area/perimeter (square, rectangle, triangle, circle) | Tutorial | Programming exercises | everlearning | `.../Tutorial_13_Numbers_and_Their_Families.ipynb` | same file | Covered |
| 1.3 Volume/surface area (cube, cylinder, cone, sphere) | Tutorial (partial) | Programming exercises | everlearning | `.../Tutorial_13_Numbers_and_Their_Families.ipynb` | same file | Cylinder & sphere confirmed; **cube and cone not confirmed present** — verify and add if missing |
| 1.4 Binary/hex arithmetic & conversion | Tutorial | Programming exercises | everlearning | `.../Tutorial_02_Storing_and_Computing.ipynb`, `.../SkillsDemos/BoringPDPandMIT-SkillsDemos/NB1_...ipynb`, `.../FunPDPandMIT-SkillsDemos/NB1_The_Number_Detective.ipynb` | same files | Strong, repeated coverage |
| 1.5 Distinguish expression vs equation | Tutorial | Programming exercises | everlearning | `.../Tutorial_14_Expressions_Come_Alive.ipynb` | same file | Covered |
| 1.6 Evaluate/expand/simplify expressions | Tutorial | Programming + Pen-and-paper | everlearning, mathematics | `.../Tutorial_14_Expressions_Come_Alive.ipynb` | same file; also `mathematics/worksheet_03a_foil_expanding.md` | Covered |
| 1.7 Transpose formulae; operate on rational algebraic expressions | Not covered (weak) | — | mathematics (partial) | — | `mathematics/worksheet_01_fractions.md` / `worksheet_01a_fractions_fundamentals.md` (algebraic fraction operations only) | **Gap**: "transpose formulae" (rearranging for a variable) isn't explicitly taught anywhere; rational-expression arithmetic is only partially covered via fractions worksheets |
| 1.8 Multiply linear expressions → quadratics/cubics | Tutorial | Programming + Pen-and-paper | everlearning, mathematics | `.../Tutorial_14_Expressions_Come_Alive.ipynb` | same file; `mathematics/worksheet_03a_foil_expanding.md` | Covered |
| 1.9 Factor quadratics by inspection; solve | Tutorial | Programming + Pen-and-paper | everlearning, mathematics | `.../Tutorial_15_Cracking_Equations.ipynb` | same file; `mathematics/worksheet_03b_factoring_solving.md` | Covered |
| 1.10 Solve quadratics incl. complex roots | **Not covered (real roots only)** | Programming + Pen-and-paper | everlearning, mathematics | `.../Tutorial_15_Cracking_Equations.ipynb`, `.../NB3_...The_Algebra_Engine.ipynb`, `.../NB3_The_Algebra_Sketchpad.ipynb` | same files; `mathematics/worksheet_03b_factoring_solving.md` | **Gap**: every implementation explicitly treats discriminant < 0 as "no real roots" and stops there; complex-number roots (a+bi form) never produced |
| 1.11 Solve linear inequalities | Tutorial | Programming exercises | everlearning | `.../Tutorial_15_Cracking_Equations.ipynb` | same file | Covered |
| 1.12 Simultaneous equations, 2 & 3 unknowns | Tutorial | Programming + Pen-and-paper | everlearning, mathematics | `.../Tutorial_15_Cracking_Equations.ipynb` (2 unknowns, elimination/determinant) | same; `mathematics/worksheet_02a_lines_coordinates_vectors.md` (2 unknowns); `mathematics/worksheet_07b_linear_systems.md` (3 unknowns via matrices) | Covered well across repos; 3-unknown case currently only via the matrix-method worksheet |

### Section 2: Set Theory and Boolean Logic

| Subject / sub-subject | Coverage | Teaching method | Source repo(s) | Tutorial file path(s) | Exercise / assessment path(s) | Notes |
|---|---|---|---|---|---|---|
| 2.1 Set language: N/Z/Q/R/ℂ/∅, finite/infinite, cardinality | Tutorial (partial) | Programming exercises | everlearning | `.../Tutorial_13_Numbers_and_Their_Families.ipynb`, `.../Tutorial_16_Sets_as_Sorted_Lists.ipynb` | same files | N/Z/Q/R covered well; **complex number set ℂ and cardinality of infinite sets not covered anywhere** |
| 2.2 Set operations: union, intersection, complement, symmetric difference, Cartesian product, power set | Tutorial (partial) | Programming exercises | everlearning | `.../Tutorial_16_Sets_as_Sorted_Lists.ipynb`, `.../NB3_The_Algebra_Sketchpad.ipynb` | same files | Union/intersection/difference/symmetric difference covered (Boring track only has symmetric difference; Fun track omits it); **Cartesian product and power set not covered anywhere** |
| 2.3 Venn diagrams (2 and 3 sets) | **Not covered** | — | — | — | — | **Gap** — natural fit for board-work/in-class delivery |
| 2.4 Truth tables: AND, NOT, OR, XOR | **Not covered** | — | — | — | — | **Gap.** Boolean `and`/`or`/`not` are *used* operationally in `Tutorial_03_Making_Decisions.ipynb`'s `if` statements, but never formalised as a truth table |
| 2.5 De Morgan's Laws | **Not covered** | — | — | — | — | **Gap** |

### Section 3: Functions and Calculus

| Subject / sub-subject | Coverage | Teaching method | Source repo(s) | Tutorial file path(s) | Exercise / assessment path(s) | Notes |
|---|---|---|---|---|---|---|
| 3.1 Function/inverse function concept | **Not covered (weak)** | Programming exercises | everlearning (partial) | `.../Tutorial_06_Finding_Things.ipynb` (functions-as-mappings concept only) | — | **Gap** — see `LearningOutcomes/MIT/SUGGESTION_MIT-3.1-3.2_Functions-and-Graphing.md` |
| 3.2 Graph linear/quadratic/cubic; solve via graph | Tutorial (partial) | Programming + Pen-and-paper | everlearning | `.../FunPDPandMIT-SkillsDemos/NB3_The_Algebra_Sketchpad.ipynb` (`plot_polynomial`, linear & quadratic); `LearningOutcomes/MIT/MIT-3.2_3.4_Quadratic-Graphing-and-Completing-the-Square.md` (quadratic graphing, pulled in from `mathematics`) | same files | Quadratic graphing now well covered. **Still open:** dedicated linear/cubic graphing practice and "solve f(x)=g(x) via graph" — see `SUGGESTION_MIT-3.1-3.2_Functions-and-Graphing.md` |
| 3.3 Define/graph trig functions | Tutorial | Pen-and-paper | everlearning (pulled in from mathematics) | `LearningOutcomes/MIT/MIT-3.3_Graphing-Sine-and-Cosine.md` | same file | **Resolved this pass** — was previously mismarked as uncovered; the source worksheet (amplitude/period/phase/vertical shift) is an explicit match and is now local |
| 3.4 Complete the square (quadratic function → roots/vertex) | Tutorial | Pen-and-paper | everlearning (pulled in from mathematics) | `LearningOutcomes/MIT/MIT-3.2_3.4_Quadratic-Graphing-and-Completing-the-Square.md` | same file | **Resolved this pass** — now local, no longer depends on the `mathematics` repo |
| 3.5 Limit of a function | **Not covered** | — | — | — | — | **Gap** — see `LearningOutcomes/MIT/SUGGESTION_MIT-3.5_Limits.md`. (`mathematics/worksheet_01b_fractions_wild.md` touches informal limiting behaviour of formulas but not the formal LO3.5 treatment) |
| 3.6 Derivative as limit / tangent line / rate of change | Tutorial | Pen-and-paper | everlearning (pulled in from mathematics) | `LearningOutcomes/MIT/MIT-3.6_Derivatives-Integrals-and-Inverse-Operations.md`, `LearningOutcomes/MIT/MIT-3.6_What-Derivatives-and-Integrals-Tell-Us.md` | same files | **Resolved this pass** — now local, no longer depends on the `mathematics` repo |
| 3.7 Sum/product/quotient/chain rule differentiation | Tutorial | Pen-and-paper | everlearning (pulled in from mathematics) | `LearningOutcomes/MIT/MIT-3.7_Product-Quotient-Chain-Rule.md` | same file | **Resolved this pass** — now local, no longer depends on the `mathematics` repo |

### Section 4: Geometry and Trigonometry

| Subject / sub-subject | Coverage | Teaching method | Source repo(s) | Tutorial file path(s) | Exercise / assessment path(s) | Notes |
|---|---|---|---|---|---|---|
| 4.1 Linear equations ax+by+c=0 | Tutorial | Pen-and-paper | everlearning (pulled in from mathematics) | `LearningOutcomes/MIT/MIT-4.1-4.3_Coordinate-Geometry.md` | same file | **Resolved this pass** |
| 4.2 Slope; parallel/perpendicular lines | Tutorial | Pen-and-paper | everlearning (pulled in from mathematics) | `LearningOutcomes/MIT/MIT-4.1-4.3_Coordinate-Geometry.md` | same file | **Resolved this pass** |
| 4.3 Midpoint & length of a line segment | Tutorial | Pen-and-paper | everlearning (pulled in from mathematics) | `LearningOutcomes/MIT/MIT-4.1-4.3_Coordinate-Geometry.md` | same file | **Resolved this pass** |
| 4.4 Pythagorean theorem | Tutorial | Pen-and-paper | everlearning (pulled in from mathematics) | `LearningOutcomes/MIT/MIT-4.4_4.9_Right-Triangle-Trigonometry.md` | same file | **Resolved this pass** |
| 4.5 Degree & radian measure | Tutorial | Pen-and-paper | everlearning (pulled in from mathematics) | `LearningOutcomes/MIT/MIT-4.5-4.7_Radians-and-the-Unit-Circle.md` | same file | **Resolved this pass** |
| 4.6 sin/cos/tan definitions; unit circle (amplitude, phase, period) | Tutorial | Pen-and-paper | everlearning (pulled in from mathematics) | `LearningOutcomes/MIT/MIT-4.5-4.7_Radians-and-the-Unit-Circle.md` | same file | **Resolved this pass** |
| 4.7 Trig ratios in root/surd form | Tutorial | Pen-and-paper | everlearning (pulled in from mathematics) | `LearningOutcomes/MIT/MIT-4.5-4.7_Radians-and-the-Unit-Circle.md` | same file | **Resolved this pass** — confirmed present (the special-angle table gives exact surd values) |
| 4.8 Triangle area = ½ab·sin θ | Tutorial | Pen-and-paper | everlearning (pulled in from mathematics) | `LearningOutcomes/MIT/MIT-4.8_4.10_Triangle-Area-Sine-and-Cosine-Rules.md` | same file | **Resolved this pass** |
| 4.9 Practical right-triangle trig (SOH-CAH-TOA) | Tutorial | Pen-and-paper | everlearning (pulled in from mathematics) | `LearningOutcomes/MIT/MIT-4.4_4.9_Right-Triangle-Trigonometry.md` | same file | **Resolved this pass** |
| 4.10 Sine Rule & Cosine Rule | Tutorial | Pen-and-paper | everlearning (pulled in from mathematics) | `LearningOutcomes/MIT/MIT-4.8_4.10_Triangle-Area-Sine-and-Cosine-Rules.md` | same file | **Resolved this pass** |

> **Whole-section note (resolved 2026-08-01):** MIT Section 4 previously had no `everlearning` content at all. All 10 sub-outcomes have now been pulled in from `mathematics` into `LearningOutcomes/MIT/` (5 files: coordinate geometry, right-triangle trig, radians/unit circle, and triangle-area/Sine-Cosine rules), each carrying a provenance header. `everlearning` no longer depends on the `mathematics` repo for this section.

### Section 5: Probability and Statistics

| Subject / sub-subject | Coverage | Teaching method | Source repo(s) | Tutorial file path(s) | Exercise / assessment path(s) | Notes |
|---|---|---|---|---|---|---|
| 5.1 List outcomes of an experiment | Tutorial | Programming exercises | everlearning | `.../Tutorial_10_What_Are_the_Chances.ipynb` | same file | Covered |
| 5.2 Fundamental principle of counting | Tutorial | Programming exercises | everlearning | `.../Tutorial_09_Counting_Carefully.ipynb`, `.../NB2_Chance_and_Patterns.ipynb`, `.../NB2_Casino_Night.ipynb` | same files | Covered |
| 5.3 n! arrangements | Tutorial | Programming exercises | everlearning | `.../Tutorial_09_Counting_Carefully.ipynb` | same file | Covered |
| 5.4 Permutations P(n,r) | Tutorial | Programming exercises | everlearning | `.../Tutorial_09_Counting_Carefully.ipynb` | same file | Covered |
| 5.5 Combinations C(n,r) | Tutorial | Programming + Pen-and-paper | everlearning, mathematics | `.../Tutorial_09_Counting_Carefully.ipynb` | same; `mathematics/worksheet_06a_statistics_probability.md` | Covered |
| 5.6 Probability as a 0–1 scale | Tutorial | Programming exercises | everlearning | `.../Tutorial_10_What_Are_the_Chances.ipynb` | same file | Covered |
| 5.7 Probability via equally-likely outcomes | Tutorial | Programming exercises | everlearning | `.../Tutorial_10_What_Are_the_Chances.ipynb` | same file | Covered |
| 5.8 Compound probability: independent & mutually exclusive events | Tutorial | Programming + Pen-and-paper | everlearning, mathematics | `.../Tutorial_10_What_Are_the_Chances.ipynb` | same; `mathematics/worksheet_08a_conditional_probability_bayes.md` (deeper — conditional probability, Bayes, Monty Hall) | Strong, layered coverage |
| 5.9 Data types: categorical (nominal/ordinal), numerical (discrete/continuous) | Tutorial (uneven) | Programming exercises | everlearning | `.../Tutorial_11_Making_Sense_of_Data.ipynb`, `.../NB2_Chance_and_Patterns.ipynb` (Boring track) | same files | **Fun track's `NB2_Casino_Night.ipynb` omits this exercise** — Boring track has it, Fun track doesn't |
| 5.10 Effectiveness of displays (pie, histogram, stem-and-leaf) | Tutorial (partial) | Programming exercises | everlearning | `.../Tutorial_12_Pictures_Worth_Numbers.ipynb` | same file | Histogram/bar/line/scatter/pie covered; **stem-and-leaf plot not confirmed present** |
| 5.11 Frequency tables & histograms | Tutorial | Programming exercises | everlearning | `.../Tutorial_11_Making_Sense_of_Data.ipynb` | same file | Covered |
| 5.12 Mean, median, mode, range, standard deviation | Tutorial | Programming + Pen-and-paper | everlearning, mathematics, python-with-ml | `.../Tutorial_11_Making_Sense_of_Data.ipynb` | same; `mathematics/worksheet_06a_statistics_probability.md`; `python-with-ml/Tutorial_7_Functions_Modularization.ipynb` (`statistics` module) | Comprehensive, multi-repo coverage |
| 5.13 Limitations/merits of mean/median/mode with skewed data | Tutorial (likely) | Programming + Pen-and-paper | everlearning, mathematics | `.../Tutorial_11_Making_Sense_of_Data.ipynb` (outlier effect on mean vs median) | `mathematics/worksheet_06a_statistics_probability.md` | Reasonably covered; worth double-checking depth of discussion when consolidating |

### Section 6: Algorithms and Computations

| Subject / sub-subject | Coverage | Teaching method | Source repo(s) | Tutorial file path(s) | Exercise / assessment path(s) | Notes |
|---|---|---|---|---|---|---|
| 6.1 Concept of an algorithm | Tutorial | Programming exercises | everlearning, python-with-ml | `.../Tutorial_01_First_Steps.ipynb` | `python-with-ml/Tutorial_2_Algorithms_Complete.ipynb` (pseudocode/flowcharts/data dictionaries) | Well covered |
| 6.2 Algorithm as a function on a domain of inputs | Tutorial | Programming exercises | everlearning | `.../Tutorial_06_Finding_Things.ipynb` | same file | Covered |
| 6.3 Manipulate lists/arrays incl. addition & multiplication | Tutorial | Programming exercises | everlearning, python-with-ml | `.../Tutorial_05_Lists_and_Sequences.ipynb` | `python-with-ml/Tutorial_6_Lists_Comprehensions.ipynb`, `Tutorial_A_NumPy_Numerical_Computing.ipynb` | Covered |
| 6.4 Index, sigma (Σ), pi (Π) notation | Tutorial | Programming exercises | everlearning | `.../Tutorial_04_Repeating_Yourself.ipynb`, `.../NB1_How_Computers_Think.ipynb`, `.../NB1_The_Number_Detective.ipynb` | same files | Strong, explicit coverage tying notation directly to loops |
| 6.5 Lists/arrays applied to simple problems (e.g. shopping lists) | Tutorial (informal) | Programming exercises | everlearning | general list exercises across Tutorials 04–08 | — | No dedicated "shopping list" scenario confirmed, but the general applied-list skill is well practised |
| 6.6 Divide and conquer | Tutorial | Programming exercises | everlearning | `.../Tutorial_06_Finding_Things.ipynb` | same file | Explicit discussion alongside binary search |
| 6.7 Iterate over 1-D arrays by index | Tutorial | Programming exercises | everlearning, python-with-ml | `.../Tutorial_04_Repeating_Yourself.ipynb`, `.../Tutorial_05_Lists_and_Sequences.ipynb` | `python-with-ml/Tutorial_5_Iteration_Loops.ipynb` | Covered |
| 6.8 Recursion; linear & binary search; bubble/insertion/selection/shell sort | Tutorial (uneven) | Programming exercises | everlearning | `.../Tutorial_06_Finding_Things.ipynb` (search), `.../Tutorial_07_Putting_Things_in_Order.ipynb` (sort), `.../NB1_How_Computers_Think.ipynb`, `.../NB1_The_Number_Detective.ipynb` | same files | Linear/binary search and bubble/insertion/selection sort are solidly required. **Shell sort and recursion are only *optional* in the Boring track**; the Fun track makes recursion (Fibonacci) *required* but doesn't touch shell sort either — inconsistent between tracks |

> **Whole-section note:** No other repo touches MIT Section 6 at all — `mathematics` has zero algorithms content, and `python-with-ml`/`2plus1coding` never implement a named sort algorithm or binary search from scratch (only `sorted()`/library calls, or "binary search" as a debugging metaphor). This entire outcome currently depends on `everlearning`'s own tutorials.

---

## PDP 5N2927 — Programming & Design Principles

| Subject / sub-subject (LO) | Coverage | Teaching method | Source repo(s) | Tutorial file path(s) | Exercise / assessment path(s) | Notes |
|---|---|---|---|---|---|---|
| LO1 History of computer programming | Tutorial | Programming exercises (conceptual) | everlearning (new, inspired by python-with-ml) | `LearningOutcomes/PDP/PDP-LO1_LO3_MIT-1.4_The-Computing-Time-Machine.ipynb` | same file | **Resolved this pass** — rather than copying `python-with-ml/Tutorial_1_History_ML_Basics.ipynb` directly, built a new fun-themed notebook that teaches the same history content while reinforcing MIT 1.4 binary/hex skills |
| LO2 Algorithms & their real-world application | Tutorial | Programming exercises | everlearning, python-with-ml | `everlearning/.../Tutorial_01_First_Steps.ipynb`, `.../Tutorial_06/07_...ipynb` (pseudocode per algorithm) | `python-with-ml/Tutorial_2_Algorithms_Complete.ipynb` (dedicated: pseudocode, flowcharts, data dictionaries); `everlearning/.../NB1_...` (pseudocode required) | Well covered, `python-with-ml` is the most dedicated single source |
| LO3 Differentiate programming languages by characteristics | Tutorial | Programming exercises (conceptual) | everlearning (new, inspired by python-with-ml) | `LearningOutcomes/PDP/PDP-LO1_LO3_MIT-1.4_The-Computing-Time-Machine.ipynb` | same file | **Resolved this pass** — same notebook as LO1 above; Stop 4 (language/paradigm table) and Stop 5 (paradigm comparison snippets) address this LO specifically |
| LO4 Procedural syntax: storage, expressions, statements, I/O, keywords, operators | Tutorial | Programming exercises | everlearning, python-with-ml, 2plus1coding | `everlearning/.../Tutorial_02_Storing_and_Computing.ipynb` | `python-with-ml/Tutorial_0_Getting_Started_in_Python.ipynb`, `Tutorial_3_Variables_DataTypes.ipynb`; `2plus1coding` starter notebooks (variables/I-O throughout) | Comprehensively covered across three repos |
| LO5 Sequential nature of problem solving | Tutorial | Programming exercises | everlearning, python-with-ml | `everlearning/.../Tutorial_01_First_Steps.ipynb` | `python-with-ml/Tutorial_2_Algorithms_Complete.ipynb` | Covered |
| LO6 Structured programming/design: pseudo-code, storage, control structures (selection & iteration) | Tutorial (uneven — see notes) | Programming exercises | everlearning, python-with-ml, 2plus1coding | `everlearning/.../Tutorial_03_Making_Decisions.ipynb` (selection), `.../Tutorial_04_Repeating_Yourself.ipynb` (iteration) | `python-with-ml/Tutorial_5_Iteration_Loops.ipynb` (iteration only); `2plus1coding` notebooks (branching/loops used operationally) | **`python-with-ml` has a confirmed hole here**: its planned "Tutorial 4 — Selection Structures & Decision Making" (Boolean logic, if/elif/else, nested conditionals) was never delivered — Tutorials 1–3 use `if` incidentally without ever teaching it. `everlearning`'s own Tutorial 3 already covers this well, so the curriculum as a whole is fine, but `python-with-ml` specifically needs that tutorial written (or explicitly deferred to `everlearning`'s version) |
| LO7 Develop documented programs for familiar/unfamiliar problems | Tutorial | Programming exercises | everlearning, python-with-ml, 2plus1coding | across most everlearning Tutorials (docstrings from Tutorial 08 on) | all three repos' notebooks use this pattern throughout | Well covered as an ongoing practice, not one isolated lesson |
| LO8 Modularisation: functions, procedures, scope, parameter passing | Tutorial | Programming exercises | everlearning, python-with-ml, 2plus1coding | `everlearning/.../Tutorial_05_Lists_and_Sequences.ipynb`, `.../Tutorial_08_Building_Reusable_Tools.ipynb` | `python-with-ml/Tutorial_7_Functions_Modularization.ipynb` (dedicated, incl. system/library functions); `2plus1coding` (functions throughout, no OOP) | Strongly covered across all three programming repos |
| LO9 Interpret compiler/linker messages and react appropriately | Tutorial | Programming exercises | everlearning (pulled in from python-with-ml) | `LearningOutcomes/PDP/PDP-LO9_LO10_Reading-Compiler-Errors-and-Debugging.ipynb` | same file; also `everlearning/.../Tutorial_01_First_Steps.ipynb` (predict/verify quizzes) | **Resolved this pass** — copied in from `python-with-ml`, now local |
| LO10 Testing process: structured walkthroughs & debugging tools | Tutorial | Programming exercises | everlearning, python-with-ml, 2plus1coding | `everlearning/.../Tutorial_07/08/14/15/16/17_...ipynb` (verification-based testing throughout) | `python-with-ml/Tutorial_8_Testing_Debugging.ipynb` (dedicated: assert-based test suites, rubber-duck, trace tables — most formal treatment); `2plus1coding` (informal "test it" play-testing only, no formal test-data design — **weaker here**) | Best covered via `everlearning` + `python-with-ml` combined; `2plus1coding` doesn't meet this LO on its own |
| LO11 Coding standards: comments, indentation, variable naming | Tutorial (uneven) | Programming exercises | everlearning, python-with-ml | `everlearning/.../Tutorial_02_Storing_and_Computing.ipynb` (naming/snake_case), `.../Tutorial_08.../Tutorial_14_...ipynb` (docstrings), `.../Tutorial_Interlude_Critique_and_Reflection.ipynb` (peer readability review) | `python-with-ml/Tutorial_0_Getting_Started_in_Python.ipynb` (naming/comments) | Reasonably covered in `everlearning` + `python-with-ml`; **`2plus1coding` has no explicit lesson** — its code is well-commented by the authors as a model but doesn't teach the standard |
| LO12 Team programming: design/develop/release/review multiple versions over time (3–5 learners) | **Other (planned, ungraded, not this LO in substance)** | Other | everlearning, 2plus1coding | `everlearning/.../NB4_Group_Portion_Ideas.md`; `2plus1coding/for-teachers.html` | — | **Significant gap.** `everlearning`'s plan is an optional, ungraded, calculus-content activity, not a multi-week release/review software project. `2plus1coding` is explicitly pair-based (2 people, one 80–90 min session), not teams of 3–5 over an extended period. Neither satisfies LO12 as written — this needs a purpose-built team project |

---

## Suggested next steps

The first pass of this document was descriptive only. As of 2026-08-01, a
second pass acted on the highest-value items: MIT Section 4 in full, the
3.3/3.4/3.6/3.7 calculus content, and PDP LO1/LO3/LO9 have all been pulled or
newly built into `everlearning/PDP_MIT_2026_2027_Integrated/LearningOutcomes/`
(see that folder's [`README.md`](../PDP_MIT_2026_2027_Integrated/LearningOutcomes/README.md)
for the full breakdown of what moved, what was newly authored, and what's
still open).

What's left is genuinely new content, not migration — each remaining gap now
has a `SUGGESTION_*.md` file in that same `LearningOutcomes/` folder with a
concrete plan (teaching method, suggested structure, a fun-reinforcement
angle) rather than just a note in this table:

- `MIT/SUGGESTION_MIT-2_Sets-Venn-Truth-Tables-DeMorgan.md` — Venn diagrams, truth tables, De Morgan's Laws, Cartesian product, power set, ℂ
- `MIT/SUGGESTION_MIT-1.10_Complex-Roots.md` — complex roots of the quadratic formula
- `MIT/SUGGESTION_MIT-1.7_Transposing-Formulae.md` — rearranging formulas, rational expressions
- `MIT/SUGGESTION_MIT-3.1-3.2_Functions-and-Graphing.md` — inverse functions, linear/cubic graphing, solving via graph
- `MIT/SUGGESTION_MIT-3.5_Limits.md` — the formal limit concept
- `MIT/SUGGESTION_MIT-Verify-Minor-Gaps.md` — small completeness checks (cube/cone formulas, stem-and-leaf plots, recursion/shell-sort consistency)
- `PDP/SUGGESTION_PDP-LO8_Team-Programming-Project.md` — a real teams-of-3–5 release/review software project, the most significant remaining gap
