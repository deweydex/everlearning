# Content review order — cross-repo reference audit

Purpose: check every student/teacher-facing file for references to sibling
repos (`mathematics`, `python-with-ml`, `2plus1coding`), links into this
repo's own `planning/` folder, or pointers to material that isn't actually
included here — none of which a reader without maintainer access should
ever hit. `planning/` itself is exempt: it's maintainer-only process
documentation and is expected to talk about other repos.

Order follows how a student/teacher would actually traverse the curriculum:
README of a section before its contents, sections in teaching sequence.

## PDP_MIT_2026_2027_Integrated/

1. `Tutorials/BoringTutorials/` — the primary day-to-day sequence, in order:
   `Tutorial_01` … `Tutorial_17`, then `Tutorial_Interlude_Critique_and_Reflection`
2. `SkillsDemos/` — README first in each subfolder, then its notebooks:
   - `BoringPDPandMIT-SkillsDemos/` (NB1–NB4)
   - `FunPDPandMIT-SkillsDemos/` (NB1–NB3)
   - `PracticePDPandMIT-SkillsDemos/README.md`, then NB1, NB2, `SOLUTION_...`
3. `LearningOutcomes/README.md`, then:
   - `MIT/` — the 9 pulled-in worksheets, then the `SUGGESTION_*.md` files
   - `PDP/` — the 2 notebooks, then `SUGGESTION_PDP-LO8...`
4. `PracticeProblems/README.md`, then `PDP-Practice-Problem-Bank.py`
5. `Enrichment/README.md`, then `Taylor-Series-Exponential-Sine-Cosine.ipynb`
6. `MathsforInformationTechnology5N18396.pdf`, `ProgrammingDesignPrinciples5N2927.pdf`
   — official QQI module descriptors, not reviewed here (not authored content)
7. `OldPDPMIT.zip` — archival, not extracted/reviewed (not active teaching material)

## OtherCourses/

1. `README.md`
2. `Markov-Chains-and-Text-Generation/README.md`, then `Week00` … `Week09-10`
3. `Computer-Graphics-Algorithms/README.md`, then `Part_1B`, `Part_2B`
4. `Neural-Network-Pruning/README.md`, then `structured_pruning_notebook_cells.py`

## Out of scope for this pass

`planning/*.md` — internal-only, expected to reference other repos.
