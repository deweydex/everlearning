# Repository Inventory

_Last updated: 2026-08-01_

This is a snapshot of what currently exists across the four repositories we have access to, so we know what's available before deciding what to migrate into `everlearning` and how to organise it. Content was reviewed by actually opening files (worksheets, notebooks, docs), not just reading filenames.

This is step 1 of the curriculum work. Step 2 — mapping this content against the MIT/PDP module descriptor learning outcomes and identifying gaps — is in [`mit-pdp-coverage-gap-analysis.md`](./mit-pdp-coverage-gap-analysis.md) in this same folder.

---

## 1. `everlearning` (this repo) — the current curriculum home

Everything currently lives under `PDP_MIT_2026_2027_Integrated/`, which is the working folder for the two Irish QQI Level 5 modules we teach together:

- **Maths for Information Technology** — 5N18396 ("MIT")
- **Programming & Design Principles** — 5N2927 ("PDP")

Both official QQI module descriptor PDFs are here: `MathsforInformationTechnology5N18396.pdf` and `ProgrammingDesignPrinciples5N2927.pdf`.

### Tutorials (`Tutorials/BoringTutorials/`) — 17 notebooks + 1 interlude

A sequential, self-directed Python-notebook course that teaches PDP and MIT concepts together (maths concepts are implemented as small Python functions and verified/tested).

| # | File | Covers (short) |
|---|---|---|
| 01 | `Tutorial_01_First_Steps.ipynb` | Jupyter basics, `print()`, arithmetic operators/BODMAS, intro to algorithms & pseudocode |
| 02 | `Tutorial_02_Storing_and_Computing.ipynb` | Variables, data types, type conversion, `input()`, binary & hex number systems |
| 03 | `Tutorial_03_Making_Decisions.ipynb` | Comparison/Boolean operators, `if`/`elif`/`else`, number-domain classifier |
| 04 | `Tutorial_04_Repeating_Yourself.ipynb` | `while`/`for` loops, accumulator pattern, sigma (Σ) & pi (Π) notation, nested loops |
| 05 | `Tutorial_05_Lists_and_Sequences.ipynb` | Lists, `enumerate()`, functions/parameters/return, Fibonacci, sequences as functions |
| 06 | `Tutorial_06_Finding_Things.ipynb` | Functions as mappings, scope, linear & binary search, divide and conquer, Big-O intuition |
| 07 | `Tutorial_07_Putting_Things_in_Order.ipynb` | Bubble/insertion/selection sort (shell sort & recursion as *optional* extensions) |
| 08 | `Tutorial_08_Building_Reusable_Tools.ipynb` | Docstrings, single-responsibility functions, systematic PASS/FAIL testing |
| 09 | `Tutorial_09_Counting_Carefully.ipynb` | Factorial, permutations, combinations, applied counting word problems |
| 10 | `Tutorial_10_What_Are_the_Chances.ipynb` | Probability rules, independent/mutually exclusive events, simulation |
| 11 | `Tutorial_11_Making_Sense_of_Data.ipynb` | Mean/median/mode/range/std dev, data types, frequency tables, first histogram |
| 12 | `Tutorial_12_Pictures_Worth_Numbers.ipynb` | Choosing chart types, matplotlib bar/line/scatter, visualization best practice |
| 13 | `Tutorial_13_Numbers_and_Their_Families.ipynb` | N/Z/Q/R, indices, logarithms, area/perimeter/volume/surface-area formulas |
| 14 | `Tutorial_14_Expressions_Come_Alive.ipynb` | Expressions vs equations, polynomials as lists, `add_poly`/`multiply_poly` (FOIL) |
| 15 | `Tutorial_15_Cracking_Equations.ipynb` | Linear/quadratic solving, factoring, linear inequalities, simultaneous equations |
| 16 | `Tutorial_16_Sets_as_Sorted_Lists.ipynb` | Sets as sorted lists, union/intersection/difference/symmetric difference |
| 17 | `Tutorial_17_Bringing_It_All_Together.ipynb` | Integrative review combining polynomials, equation-solving and sets |
| — | `Tutorial_Interlude_Critique_and_Reflection.ipynb` | Peer code review / reflection. **Note:** its own text says it follows Skills Demo 1, so content-wise it belongs between Tutorial 7 and 8, not at the end of the numbered sequence. |

### Skills Demos (assessment notebooks)

Two parallel "tracks" covering the same assessed learning outcomes with different framing — **they are not a clean 1:1 reskin**; content coverage differs between them in places (noted below and detailed in the gap-analysis doc).

**`SkillsDemos/BoringPDPandMIT-SkillsDemos/`**
| File | Covers |
|---|---|
| `NB1_PDP_SD1_MIT_A2_How_Computers_Think.ipynb` | Binary/hex, sigma/pi, linear/binary search, bubble/insertion/selection sort |
| `NB2_PDP_SD2a_MIT_A1a_Chance_and_Patterns.ipynb` | Counting, probability, mean/median/mode/std dev, data types, histograms |
| `NB3_PDP_SD2b_MIT_A1b_The_Algebra_Engine.ipynb` | Number domains, indices/logs, geometry formulas, polynomials, quadratics, sets, inequalities, simultaneous equations |
| `NB4_Group_Portion_Ideas.md` | Instructor planning doc for the 10% PDP team-work component. Explicitly names MIT graphing/trig/calculus (LO 3.2–3.7, 4.1–4.10) as **exam-only content not covered by any graded assignment** — see gap analysis. |

**`SkillsDemos/FunPDPandMIT-SkillsDemos/`**
| File | Covers | Differs from Boring counterpart |
|---|---|---|
| `NB1_The_Number_Detective.ipynb` | Binary/hex "secret messages," binary-search guessing game, higher-order sigma/pi | **Adds** recursion-vs-iteration (Fibonacci, timing comparison) as a *required* exercise — Boring only makes this optional |
| `NB2_Casino_Night.ipynb` | Card-probability word problems, simulation, stats on simulated hands | **Omits** the data-type classification exercise present in Boring NB2 |
| `NB3_The_Algebra_Sketchpad.ipynb` | Number domains, polynomials, quadratics, basic graphing, sets | **Adds** `plot_polynomial` graphing and a Bezier-curve drawing exercise (the only place in the whole corpus functions are graphed); **omits** indices/logs, geometry formulas, factoring, inequalities, and simultaneous equations that Boring NB3 covers, and only implements a subset of set operations |

### Other files
- `MathsforInformationTechnology5N18396.pdf`, `ProgrammingDesignPrinciples5N2927.pdf` — the official QQI module descriptors.
- `OldPDPMIT.zip` — **a redundant archive**: confirmed byte-identical to the current Tutorials/SkillsDemos content (a nested nested zip of an earlier "Better_PDP_and_MIT_SDs" naming plus copies of the same tutorials). No unique content here; candidate for deletion once we're confident nothing else references it.

---

## 2. `mathematics` — QQI MIT worksheet bank

A pen-and-paper worksheet bank (Markdown source → rendered PDF, with separate annotated/teacher and solutions PDFs) covering most of the MIT syllabus in far more depth than `everlearning`'s own tutorials, especially calculus and trigonometry — **but with zero content on Set Theory/Boolean Logic or Algorithms/Computations** (confirmed by keyword sweep, not just absence of matching filenames).

103 files total: 28 canonical worksheets (Markdown, mostly under `markdown/`, a few duplicated at repo root), each typically with matching `pdfs/worksheets/`, `pdfs/annotated/`, and `pdfs/solutions/` PDFs, plus one interactive worksheet available as both a Jupyter notebook and a Marimo app.

| Worksheet | Topic | Format(s) |
|---|---|---|
| `worksheet_01_exponents_and_logarithms(.md / _applications.md)` | Exponent laws, logs, applied contexts (decay, decibels, Big-O aside) | md only (root) |
| `worksheet_01_fractions.md` / `01a_fractions_fundamentals.md` | Numeric & algebraic fractions, complex fractions, limit-behaviour reasoning | md + pdf + annotated + solutions |
| `worksheet_01b_fractions_wild.md` | Fractions applied to physics/ML/Bayes formulas (root & markdown versions differ — markdown has ~2x the content) | md + pdf + annotated + solutions |
| `worksheet_02a_lines_coordinates_vectors.md` | Coordinate geometry: slope, midpoint, distance, parallel/perpendicular, 2-unknown simultaneous equations | md + pdf + annotated + solutions |
| `worksheet_02b_*` (jupyter.ipynb, marimo.py, `_linear_thinking_data_curves.md`) | Line of best fit, residuals, correlation, tangent-line intuition | md + pdf + annotated + solutions + 2 interactive notebook formats |
| `worksheet_03a_foil_expanding.md` | FOIL, binomial expansion, Pascal's Triangle | md + pdf + annotated + solutions |
| `worksheet_03b_factoring_solving.md` | Factoring, completing the square, quadratic formula (stops at "no real solutions" — no complex roots) | md + pdf + annotated + solutions |
| `worksheet_03c_applications.md` | Projectile motion, optimisation word problems, binomial probability | md + pdf + annotated + solutions |
| `worksheet_03d_graphing.md` | Parabola shape/vertex form, completing the square, discriminant↔graph | md + pdf + annotated + solutions |
| `worksheet_04a_derivatives_integrals_inverse.md` | Power rule, antiderivatives, definite integrals | md + pdf + solutions |
| `worksheet_04b_what_they_tell_us.md` | Derivative as slope/rate, concavity, optimisation, FTC | md + pdf + solutions |
| `worksheet_04c_advanced_rules.md` | **Product, quotient, chain rule**, integration by parts, u-substitution | md + pdf + solutions |
| `worksheet_04d_transcendental_series.md` | Taylor series for eˣ/sin/cos/ln, Euler's formula | md + pdf + solutions |
| `worksheet_04e_optimisation.md` | Critical points, 1st/2nd derivative tests, optimisation, gradient descent | md + pdf + solutions |
| `worksheet_05a_angles_radians_unit_circle.md` | Degrees/radians, arc length, unit circle exact values | md + pdf + solutions |
| `worksheet_05b_right_triangle_trig.md` | SOH-CAH-TOA, special triangles, elevation/depression | md + pdf + solutions |
| `worksheet_05c_graphs_sine_cosine.md` | Amplitude, period, phase shift | md + pdf + solutions |
| `worksheet_05d_identities_equations.md` | Trig identities, sum/difference/double-angle formulas | md + pdf + solutions |
| `worksheet_05e_laws_sines_cosines.md` | Sine Rule, Cosine Rule, triangle area formula | md + pdf + solutions |
| `worksheet_06a_statistics_probability.md` | Mean/median/mode/SD, normal distribution, permutations/combinations, Bayes preview | md + pdf + solutions |
| `worksheet_07a_matrix_operations.md` | Matrix ops, determinants, inverses (beyond MIT syllabus) | md + pdf + solutions |
| `worksheet_07b_linear_systems.md` | Gaussian elimination, 3-unknown systems, RREF | md + pdf + solutions |
| `worksheet_07c_eigenvalues_eigenvectors.md` | Eigenvalues/vectors, PCA (beyond MIT syllabus) | md + pdf + solutions |
| `worksheet_07d_markov_chains.md` | Transition matrices, steady state (beyond MIT syllabus) | md + pdf + solutions |
| `worksheet_08a_conditional_probability_bayes.md` | Conditional probability, Bayes' theorem, Monty Hall | md + pdf + solutions |
| `worksheet_08b_probability_distributions.md` | Binomial/Poisson/Normal/CLT (beyond MIT syllabus) | md + pdf + solutions |

**Confirmed absent:** Venn diagrams, truth tables, De Morgan's Laws, set notation, binary/hex number systems, sorting/searching algorithms, recursion. This repo would need to stay paired with `everlearning`'s own Algorithms/Sets tutorials — it doesn't substitute for them.

---

## 3. `2plus1coding` — AI-assisted pair-programming workshop

A single-session (80–90 min), five-project, beginner/advanced pair-programming activity where students build a small Python project (tic-tac-toe, word-guessing game, RPG battle, image processing, or basic ML classifier) while learning to prompt Claude incrementally. Two delivery paths: web (Claude.ai + Colab) or desktop (Claude Code CLI, mirrored as plain `.py` starter files).

| Area | Files | Notes |
|---|---|---|
| Docs | `README.md`, `PROJECT_PLANNING.md`, `Educational_Reference_Document.md` | Planning template covers goal/MVP/functions/test cases; the "Educational_Reference_Document" is actually LLM-authoring style guidance, not curriculum content itself |
| Current notebooks | `colab-notebooks/*.ipynb` (11 files: tictactoe ×3, wordguess ×2, rpg ×2, imageproc ×2, ml ×2) | Beginner notebooks give board/display scaffolding, advanced notebooks give much more pre-built and ask for the "hard part"; `tictactoe_beginner_enhanced.ipynb` is the most heavily scaffolded, phase-by-phase version |
| Desktop mirrors | `starter-code/*.py` (10 files) | Same content as the notebooks, for the Claude Code CLI path |
| Superseded set | `archive/` (facilitator guide, student handouts, solutions for tictactoe/rpg/wordguess only — no image/ML) | Earlier 3-project version of the same workshop |
| Site | `index.html`, `getting-started.html`, `prompting-guide.html`, `for-teachers.html`, `projects.html`, `projects/*.html` | `prompting-guide.html` is the most substantive doc — LLM/prompting technique, iterative development as a feedback loop; `projects/machine-learning.html` explains train/test split, overfitting, bias-variance in prose |

**Confirmed:** no classes/OOP, no recursion, no unit-testing framework (testing is informal "play-test it"), no sorting/searching algorithms, no history-of-programming content, no coding-standards lesson. Built entirely around **pairs**, not teams of 3–5 — `for-teachers.html` explicitly frames pair programming as the collaboration unit; there's no multi-week release/review team project anywhere in this repo.

---

## 4. `python-with-ml` — Python & ML tutorial series

12 notebooks. The first eight (`Tutorial_0`–`Tutorial_3`, `Tutorial_5`–`Tutorial_8`) are explicitly QQI-branded ("Module: Programming & Design Principles 5N2927 / QQI Level 5" headers with numbered learning outcomes) and form a PDP-aligned core. The last four (`Tutorial_9`, `Tutorial_A`, `Tutorial_B`, `Tutorial_C`) are a separate, non-QQI-branded advanced/enrichment track (academic citations instead of LO headers).

| File | Covers |
|---|---|
| `Tutorial_0_Getting_Started_in_Python.ipynb` | Jupyter, `print()`, variables, arithmetic, naming/comments |
| `Tutorial_1_History_ML_Basics.ipynb` | **History of programming**: machine code → assembly → FORTRAN/COBOL/LISP → C/Python; paradigms; compiled vs interpreted |
| `Tutorial_2_Algorithms_Complete.ipynb` | Algorithm design process: pseudocode, flowcharts, data dictionaries (not the sort/search canon) |
| `Tutorial_3_Variables_DataTypes.ipynb` | Data types, casting, operators, feature-engineering (normalization/standardization) |
| **`Tutorial_4` — missing** | **Confirmed gap.** Tutorial_3's closing cell previews "Selection Structures & Decision Making" (Boolean logic, if/elif/else, nested conditionals) as the next tutorial; Tutorial_5 opens referencing it. It was never delivered — only a single commit exists adding all 13 files at once, no deleted-file history. |
| `Tutorial_5_Iteration_Loops.ipynb` | while/for loops, break/continue, linear-search-as-loop-pattern, debugging loops |
| `Tutorial_6_Lists_Comprehensions.ipynb` | Lists, slicing, comprehensions, `sorted()`/`.sort()` (no manual sort algorithm) |
| `Tutorial_7_Functions_Modularization.ipynb` | Functions, scope, parameters/return, `math`/`statistics` system functions |
| `Tutorial_8_Testing_Debugging.ipynb` | Error types, tracebacks, assert-based test suites, rubber-duck debugging, trace tables |
| `Tutorial_9_Math_Random_Libraries.ipynb` | (enrichment) `math`/`random`, distributions, Monte Carlo, bootstrap sampling |
| `Tutorial_A_NumPy_Numerical_Computing.ipynb` | (enrichment) NumPy arrays, vectorization, linear algebra, linear regression from scratch |
| `Tutorial_B_Matplotlib.ipynb` | (enrichment) Visualization: line/scatter/histogram/box/contour plots |
| `Tutorial_C_Object_Oriented_Programming.ipynb` | (enrichment) Classes, encapsulation, inheritance, polymorphism, a KNN classifier exercise |

**Confirmed absent:** classical sort/search algorithms (bubble/insertion/selection/shell sort, binary search) are never implemented — "binary search" appears only as a debugging metaphor in Tutorial_8. No team-programming content.

---

## Cross-repo observations (feeding into the gap analysis)

- **MIT Geometry & Trigonometry (Section 4)** has essentially zero coverage in `everlearning` itself but is thoroughly covered, pen-and-paper style, in `mathematics` (`worksheet_05a`–`05e`). Same story for **derivatives/differentiation rules (MIT 3.6–3.7)**: covered in `mathematics` (`worksheet_04a`–`04c`), not in `everlearning`.
- **Set theory's "hard" parts** — Venn diagrams, truth tables, De Morgan's Laws, the complex-number set C, Cartesian product, power set — aren't covered *anywhere* across all four repos.
- **Complex roots of the quadratic formula** (MIT 1.10) are never computed anywhere; every implementation across `everlearning` and `mathematics` stops at "no real roots."
- **History of programming** (PDP LO1) is well covered in `python-with-ml` (`Tutorial_1`) but not present in `everlearning`'s own tutorials.
- **Team programming with 3–5 learners, releasing and reviewing multiple versions** (PDP LO8) is not genuinely satisfied anywhere: `2plus1coding` is pair-only by design, and `everlearning`'s own team-work plan (`NB4_Group_Portion_Ideas.md`) is an optional, ungraded, calculus-focused activity rather than a multi-week software project.
- `python-with-ml`'s missing Tutorial_4 (branching/decision structures) is a gap in that repo specifically, but `everlearning`'s own `Tutorial_03_Making_Decisions.ipynb` already covers this territory, so it's not a curriculum-wide gap.

See [`mit-pdp-coverage-gap-analysis.md`](./mit-pdp-coverage-gap-analysis.md) for the full learning-outcome-by-learning-outcome mapping.
