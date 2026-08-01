# SUGGESTION: Small verification/completeness checks (not full gaps)

> These are minor items flagged during the coverage analysis that are likely already fine, or need only a small addition — not full new tutorials. Bundled into one file rather than fragmenting into several near-empty ones.

## MIT 1.3 — Volume/surface area of cube and cone

`Tutorials/BoringTutorials/Tutorial_13_Numbers_and_Their_Families.ipynb` was confirmed to cover circle, rectangle, triangle, cylinder and sphere area/perimeter/volume/surface-area formulas — but **cube and cone were not confirmed present** in the research pass behind the gap analysis.

**Suggested action:** open `Tutorial_13` and check directly. If cube and cone are genuinely missing, they're a very small addition — both formulas are simple (`cube: V = s³, SA = 6s²`; `cone: V = ⅓πr²h, SA = πr² + πrl`) and slot into the same function-per-shape pattern the tutorial already uses for cylinder and sphere. No new exercise design needed, just two more functions in the existing style.

## MIT 4.7 — Trigonometric ratios in root/surd form

Resolved during this pass — [`MIT-4.5-4.7_Radians-and-the-Unit-Circle.md`](./MIT-4.5-4.7_Radians-and-the-Unit-Circle.md)'s special-angle table (Part C) gives sin/cos values in exact surd form (e.g. `√3/2`, `√2/2`) for all the standard angles, which directly satisfies this outcome. No further action needed — noted here so it isn't mistakenly re-flagged as a gap later.

## MIT 5.10 — Stem-and-leaf plots

`Tutorial_12_Pictures_Worth_Numbers.ipynb` was confirmed to cover histogram, bar, line, scatter and pie charts — but a **stem-and-leaf plot specifically was not confirmed present**, and it's one of the three display types the module descriptor names explicitly (`pie charts, histograms, stem and leaf plots`).

**Suggested action:** if genuinely absent, this is a small, self-contained addition to `Tutorial_12` or `Tutorial_11_Making_Sense_of_Data.ipynb` — a `stem_and_leaf(data)` function that groups values by their "stem" (all digits but the last) and lists the "leaves" (last digit) next to each stem, printed as simple text rows. It's a good complement to the histogram work already there, since it's often taught as "a histogram you can still read the exact values off."

## MIT 6.8 — Recursion and shell sort: inconsistent between tracks

Confirmed in the gap analysis: shell sort and recursion are **optional extensions** in `Tutorial_07_Putting_Things_in_Order.ipynb` and `BoringPDPandMIT-SkillsDemos/NB1_...ipynb` (the "Boring" track), but `FunPDPandMIT-SkillsDemos/NB1_The_Number_Detective.ipynb` makes **recursion required** (the Fibonacci recursion-vs-iteration timing exercise) while still leaving shell sort untouched in either track.

**Suggested action:** this isn't a coverage gap so much as a consistency question for whoever is setting the assessment bar — decide once whether recursion is core-required or genuinely optional-extension across *both* tracks, and apply that decision consistently. If recursion is made core-required everywhere, the Fun track's existing Fibonacci exercise is a ready-made template that could be adapted into the Boring track too (or vice versa — the Boring track's binary-search-recursively extension could become required in the Fun track). Shell sort can reasonably stay an optional "if you want the extra challenge" extension in both tracks, since it's the one MIT 6.8 sort algorithm least likely to come up again outside this course.
