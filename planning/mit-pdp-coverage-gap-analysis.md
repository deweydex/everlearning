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

1. **MIT Section 4 (Geometry & Trigonometry) — zero coverage in `everlearning`.** All 10 sub-outcomes (coordinate geometry, Pythagoras, radians, sin/cos/tan, unit circle, Sine/Cosine rules) exist only as pen-and-paper worksheets in `mathematics` (`worksheet_05a`–`05e`), not yet pulled into `everlearning`.
2. **MIT Section 3 (Functions & Calculus) — mostly missing from `everlearning`**, and this is *known and named by the curriculum's own planning doc*: `NB4_Group_Portion_Ideas.md` explicitly lists graphing (3.2), trig functions (3.3), completing the square (3.4), limits (3.5), derivatives (3.6) and differentiation rules (3.7) as "exam-relevant content the assignments do not cover," and proposes patching it only via an optional, ungraded team activity. The actual teaching material for derivatives/differentiation rules already exists, pen-and-paper, in `mathematics` (`worksheet_04a`–`04c`).
3. **MIT Section 2's "hard half" is missing everywhere.** Set operations (union/intersection/difference) are well covered, but **Venn diagrams, truth tables, De Morgan's Laws, the complex number set ℂ, Cartesian product, and power set** appear in none of the four repos.
4. **MIT 1.10 — complex roots of the quadratic formula are never computed.** Every implementation (`everlearning` Tutorial 15, both Boring/Fun Algebra skills demos, `mathematics` worksheet_03b) stops at "no real solutions" for a negative discriminant.
5. **PDP LO8 (team of 3–5, releasing/reviewing multiple versions over time) is not genuinely satisfied anywhere.** `2plus1coding` is explicitly pair-only by design; `everlearning`'s own team-work plan is optional, ungraded, and calculus-focused rather than a multi-week software project with a release/review cycle.
6. **PDP LO1 (history of programming)** isn't in `everlearning`'s own tutorials — it's well covered in `python-with-ml` (`Tutorial_1_History_ML_Basics.ipynb`), not yet pulled in.
7. **Sort/search algorithms (MIT 6.8) are uniquely `everlearning`'s territory** — neither `mathematics`, `2plus1coding`, nor `python-with-ml` implement bubble/insertion/selection/shell sort or binary search as a taught topic. Within `everlearning`, shell sort and recursion are inconsistently required: optional in the "Boring" track, required in the "Fun" track (Fibonacci recursion).
8. **`python-with-ml`'s Tutorial_4 (Selection Structures & Decision Making) was planned and never delivered** — but `everlearning`'s own `Tutorial_03_Making_Decisions.ipynb` already covers that ground, so it's a gap in that source repo specifically, not in the curriculum overall.

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
| 3.1 Function/inverse function concept | **Not covered (weak)** | Programming exercises | everlearning (partial) | `.../Tutorial_06_Finding_Things.ipynb` (functions-as-mappings concept only) | — | **Gap**: inverse-function computation not present |
| 3.2 Graph linear/quadratic/cubic; solve via graph | **Not covered** (named gap) | Programming exercises (minimal) | everlearning (minimal) | `.../FunPDPandMIT-SkillsDemos/NB3_The_Algebra_Sketchpad.ipynb` (`plot_polynomial`, linear & quadratic only) | — | Explicitly named as exam-only/uncovered in `NB4_Group_Portion_Ideas.md`; no cubic graphing, no "solve f(x)=g(x) via graph" exercise |
| 3.3 Define/graph trig functions | **Not covered** | — | — | — | — | **Gap**, explicitly named in `NB4_Group_Portion_Ideas.md` |
| 3.4 Complete the square (quadratic function → roots/vertex) | Tutorial | Pen-and-paper | mathematics | `mathematics/worksheet_03d_graphing.md` | same file | Covered pen-and-paper in `mathematics`; **not covered in `everlearning`** — candidate to pull in |
| 3.5 Limit of a function | **Not covered** | — | — | — | — | **Gap**, explicitly named in `NB4_Group_Portion_Ideas.md`. (`mathematics/worksheet_01b_fractions_wild.md` touches informal limiting behaviour of formulas but not the formal LO3.5 treatment) |
| 3.6 Derivative as limit / tangent line / rate of change | Tutorial | Pen-and-paper | mathematics | `mathematics/worksheet_04a_derivatives_integrals_inverse.md`, `mathematics/worksheet_04b_what_they_tell_us.md` | same files | Covered pen-and-paper in `mathematics`; **not covered in `everlearning`**, explicitly named as a gap in `NB4_Group_Portion_Ideas.md` |
| 3.7 Sum/product/quotient/chain rule differentiation | Tutorial | Pen-and-paper | mathematics | `mathematics/worksheet_04c_advanced_rules.md` | same file | Covered pen-and-paper in `mathematics` (explicit chain-rule content); **not covered in `everlearning`** |

### Section 4: Geometry and Trigonometry

| Subject / sub-subject | Coverage | Teaching method | Source repo(s) | Tutorial file path(s) | Exercise / assessment path(s) | Notes |
|---|---|---|---|---|---|---|
| 4.1 Linear equations ax+by+c=0 | Tutorial | Pen-and-paper | mathematics | `mathematics/worksheet_02a_lines_coordinates_vectors.md` | same file | **Not covered in `everlearning`** |
| 4.2 Slope; parallel/perpendicular lines | Tutorial | Pen-and-paper | mathematics | `mathematics/worksheet_02a_lines_coordinates_vectors.md` | same file | **Not covered in `everlearning`** |
| 4.3 Midpoint & length of a line segment | Tutorial | Pen-and-paper | mathematics | `mathematics/worksheet_02a_lines_coordinates_vectors.md` | same file | **Not covered in `everlearning`** |
| 4.4 Pythagorean theorem | Tutorial | Pen-and-paper | mathematics | `mathematics/worksheet_05b_right_triangle_trig.md` | same file | **Not covered in `everlearning`** |
| 4.5 Degree & radian measure | Tutorial | Pen-and-paper | mathematics | `mathematics/worksheet_05a_angles_radians_unit_circle.md` | same file | **Not covered in `everlearning`** |
| 4.6 sin/cos/tan definitions; unit circle (amplitude, phase, period) | Tutorial | Pen-and-paper | mathematics | `mathematics/worksheet_05a_angles_radians_unit_circle.md` | same file | **Not covered in `everlearning`** |
| 4.7 Trig ratios in root/surd form | Tutorial (likely) | Pen-and-paper | mathematics | `mathematics/worksheet_05a_angles_radians_unit_circle.md` | same file | Unit-circle exact values plausibly include root form — verify when pulling in |
| 4.8 Triangle area = ½ab·sin θ | Tutorial | Pen-and-paper | mathematics | `mathematics/worksheet_05e_laws_sines_cosines.md` | same file | **Not covered in `everlearning`** |
| 4.9 Practical right-triangle trig (SOH-CAH-TOA) | Tutorial | Pen-and-paper | mathematics | `mathematics/worksheet_05b_right_triangle_trig.md` | same file | **Not covered in `everlearning`** |
| 4.10 Sine Rule & Cosine Rule | Tutorial | Pen-and-paper | mathematics | `mathematics/worksheet_05e_laws_sines_cosines.md` | same file | **Not covered in `everlearning`** |

> **Whole-section note:** MIT Section 4 has **no `everlearning` content at all** — it exists entirely as pen-and-paper worksheets in `mathematics`. This is the single largest, cleanest gap in the analysis: importing `worksheet_02a` and `worksheet_05a`–`05e` (and their annotated/solutions PDFs) would close it in one move.

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
| LO1 History of computer programming | **Not covered in `everlearning`** | Programming exercises (conceptual) | python-with-ml | `python-with-ml/Tutorial_1_History_ML_Basics.ipynb` | same file | Strong dedicated coverage exists in `python-with-ml`, not yet pulled into `everlearning` |
| LO2 Algorithms & their real-world application | Tutorial | Programming exercises | everlearning, python-with-ml | `everlearning/.../Tutorial_01_First_Steps.ipynb`, `.../Tutorial_06/07_...ipynb` (pseudocode per algorithm) | `python-with-ml/Tutorial_2_Algorithms_Complete.ipynb` (dedicated: pseudocode, flowcharts, data dictionaries); `everlearning/.../NB1_...` (pseudocode required) | Well covered, `python-with-ml` is the most dedicated single source |
| LO3 Differentiate programming languages by characteristics | **Not covered in `everlearning`** | Programming exercises (conceptual) | python-with-ml | `python-with-ml/Tutorial_1_History_ML_Basics.ipynb` (paradigms: procedural/OOP/functional/logic/scripting) | same file | Same gap as LO1 — bundled in the same notebook |
| LO4 Procedural syntax: storage, expressions, statements, I/O, keywords, operators | Tutorial | Programming exercises | everlearning, python-with-ml, 2plus1coding | `everlearning/.../Tutorial_02_Storing_and_Computing.ipynb` | `python-with-ml/Tutorial_0_Getting_Started_in_Python.ipynb`, `Tutorial_3_Variables_DataTypes.ipynb`; `2plus1coding` starter notebooks (variables/I-O throughout) | Comprehensively covered across three repos |
| LO5 Sequential nature of problem solving | Tutorial | Programming exercises | everlearning, python-with-ml | `everlearning/.../Tutorial_01_First_Steps.ipynb` | `python-with-ml/Tutorial_2_Algorithms_Complete.ipynb` | Covered |
| LO6 Structured programming/design: pseudo-code, storage, control structures (selection & iteration) | Tutorial (uneven — see notes) | Programming exercises | everlearning, python-with-ml, 2plus1coding | `everlearning/.../Tutorial_03_Making_Decisions.ipynb` (selection), `.../Tutorial_04_Repeating_Yourself.ipynb` (iteration) | `python-with-ml/Tutorial_5_Iteration_Loops.ipynb` (iteration only); `2plus1coding` notebooks (branching/loops used operationally) | **`python-with-ml` has a confirmed hole here**: its planned "Tutorial 4 — Selection Structures & Decision Making" (Boolean logic, if/elif/else, nested conditionals) was never delivered — Tutorials 1–3 use `if` incidentally without ever teaching it. `everlearning`'s own Tutorial 3 already covers this well, so the curriculum as a whole is fine, but `python-with-ml` specifically needs that tutorial written (or explicitly deferred to `everlearning`'s version) |
| LO7 Develop documented programs for familiar/unfamiliar problems | Tutorial | Programming exercises | everlearning, python-with-ml, 2plus1coding | across most everlearning Tutorials (docstrings from Tutorial 08 on) | all three repos' notebooks use this pattern throughout | Well covered as an ongoing practice, not one isolated lesson |
| LO8 Modularisation: functions, procedures, scope, parameter passing | Tutorial | Programming exercises | everlearning, python-with-ml, 2plus1coding | `everlearning/.../Tutorial_05_Lists_and_Sequences.ipynb`, `.../Tutorial_08_Building_Reusable_Tools.ipynb` | `python-with-ml/Tutorial_7_Functions_Modularization.ipynb` (dedicated, incl. system/library functions); `2plus1coding` (functions throughout, no OOP) | Strongly covered across all three programming repos |
| LO9 Interpret compiler/linker messages and react appropriately | Tutorial (partial) | Programming exercises | everlearning, python-with-ml | error-handling touched in `everlearning/.../Tutorial_01_First_Steps.ipynb` (predict/verify quizzes) | `python-with-ml/Tutorial_8_Testing_Debugging.ipynb` (syntax vs runtime vs logical errors, reading tracebacks — dedicated, strongest match) | `python-with-ml` has the best-targeted material here; not yet in `everlearning` |
| LO10 Testing process: structured walkthroughs & debugging tools | Tutorial | Programming exercises | everlearning, python-with-ml, 2plus1coding | `everlearning/.../Tutorial_07/08/14/15/16/17_...ipynb` (verification-based testing throughout) | `python-with-ml/Tutorial_8_Testing_Debugging.ipynb` (dedicated: assert-based test suites, rubber-duck, trace tables — most formal treatment); `2plus1coding` (informal "test it" play-testing only, no formal test-data design — **weaker here**) | Best covered via `everlearning` + `python-with-ml` combined; `2plus1coding` doesn't meet this LO on its own |
| LO11 Coding standards: comments, indentation, variable naming | Tutorial (uneven) | Programming exercises | everlearning, python-with-ml | `everlearning/.../Tutorial_02_Storing_and_Computing.ipynb` (naming/snake_case), `.../Tutorial_08.../Tutorial_14_...ipynb` (docstrings), `.../Tutorial_Interlude_Critique_and_Reflection.ipynb` (peer readability review) | `python-with-ml/Tutorial_0_Getting_Started_in_Python.ipynb` (naming/comments) | Reasonably covered in `everlearning` + `python-with-ml`; **`2plus1coding` has no explicit lesson** — its code is well-commented by the authors as a model but doesn't teach the standard |
| LO12 Team programming: design/develop/release/review multiple versions over time (3–5 learners) | **Other (planned, ungraded, not this LO in substance)** | Other | everlearning, 2plus1coding | `everlearning/.../NB4_Group_Portion_Ideas.md`; `2plus1coding/for-teachers.html` | — | **Significant gap.** `everlearning`'s plan is an optional, ungraded, calculus-content activity, not a multi-week release/review software project. `2plus1coding` is explicitly pair-based (2 people, one 80–90 min session), not teams of 3–5 over an extended period. Neither satisfies LO12 as written — this needs a purpose-built team project |

---

## Suggested next steps

This document is descriptive (what exists, where, and what's missing) rather
than prescriptive. A reasonable next planning pass, once this is agreed, would
be to turn the gaps above into a punch list: which `mathematics` worksheets to
import wholesale (Section 4 and 3.4–3.7 are the highest-value, lowest-effort
wins), which topics need genuinely new material (Venn diagrams/truth
tables/De Morgan's, complex roots, a real LO12 team project), and which
existing content just needs a home inside `everlearning`'s own folder
structure (history of programming and debugging/testing material from
`python-with-ml`).
