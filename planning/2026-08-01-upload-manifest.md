# 2026-08-01 Upload Manifest

On 2026-08-01, three items were uploaded alongside a request to check whether `2plus1coding` had anything useful, get a read on other repos under the `deweydex` account, and organise the uploaded material (particularly combining the split-up practice problems and describing everything in the zip):

- `Old_PDP_Skills_Demo_1_PRACTICE.ipynb`
- `Old_PDP_Skills_Demo_2_PRACTICE.ipynb`
- `python.zip` (a `python/` folder containing 21 files, plus macOS `__MACOSX/` resource-fork junk which was ignored)

This document is the file-by-file record of what was in that upload and where each thing ended up. Everything QQI-relevant went into `PDP_MIT_2026_2027_Integrated/`; everything from a clearly different course went into `OtherCourses/` (see that folder's own README for why); one item is a genuinely excluded duplicate.

## Skills demo notebooks (uploaded directly, not in the zip)

| Original | Destination | Notes |
|---|---|---|
| `Old_PDP_Skills_Demo_1_PRACTICE.ipynb` | `SkillsDemos/PracticePDPandMIT-SkillsDemos/NB1_PDP_SD1_List-Operations-Practice.ipynb` | Renamed for consistency with the existing `NB1`/`NB2`/`NB3` skills-demo naming convention |
| `Old_PDP_Skills_Demo_2_PRACTICE.ipynb` | `SkillsDemos/PracticePDPandMIT-SkillsDemos/NB2_PDP_SD2_Card-Game-Practice.ipynb` | Same |

## `python.zip` contents

| Original file | Destination | Notes |
|---|---|---|
| `skills_demo_2_complete.py` | `SkillsDemos/PracticePDPandMIT-SkillsDemos/SOLUTION_PDP_SD2_Word-Length-Language-Classifier.py` | A **complete worked solution** for a different Skills Demo 2 design (word-length language classifier) than the card-game one above — not an answer key for `NB2` |
| `practice-problems-1-2.py` | Combined into `PracticeProblems/PDP-Practice-Problem-Bank.py` as Problems 1-7 | Clean version of these 7 problems |
| `practice-problems-1_3.py` | **Excluded** | Byte-for-byte comparison against `practice-problems-1-2.py` showed identical function signatures but messy in-progress annotations scribbled into the docstrings/bodies (e.g. `divide_numbers(4:, 10)`, stray `return num1 + num2` fragments) — a draft/scratch copy of the same 7 problems, not a distinct problem set. The clean version was kept instead. |
| `practice-problems-2.py` | Combined into `PDP-Practice-Problem-Bank.py` as Problems 8-12 | |
| `practice-problems-3.py` | Combined into `PDP-Practice-Problem-Bank.py` as Problems 13-17 | |
| `practice-problems-4.py` | Combined into `PDP-Practice-Problem-Bank.py` as Problems 18-22 | |
| `practice-problems-5.py` | Combined into `PDP-Practice-Problem-Bank.py` as Problems 23-27 (`StringAndNumberExercises`) | Already carried "Problem N" numbering in its source docstrings |
| `practice-problems-6.py` | Combined into `PDP-Practice-Problem-Bank.py` as Problems 28-32 (`StringAndArrayExercises`) | Already numbered |
| `practice-problems-7.py` | Combined into `PDP-Practice-Problem-Bank.py` as Problems 33-36 (`NumberAndStringChecks`) | Already numbered |
| `practice-problems-other.py` | Combined into `PDP-Practice-Problem-Bank.py` as Problems 37-38 | Its `find_most_frequent_number` and `is_valid_palindrome` were kept; a commented-out **C# practice-problem scrap** (`MergeSortedArrays`, `LongestSubstringLength`) in the same file was dropped — no home in a Python-only PDP course, and it was already inert (inside a triple-quoted string, not live code) |
| `1_Slow_Fibonacci.ipynb` | `LearningOutcomes/MIT/MIT-6.8_Recursion-Fibonacci-and-Big-O.ipynb` | Resolves the recursion-consistency gap already flagged in `SUGGESTION_MIT-Verify-Minor-Gaps.md` — see that file and the gap-analysis row for MIT 6.8 |
| `1_Exponential_Function_CODE_import_math.ipynb` | `Enrichment/Taylor-Series-Exponential-Sine-Cosine.ipynb` | Beyond-syllabus (Taylor series aren't a numbered MIT LO); coded companion to `mathematics/worksheet_04d_transcendental_series.md`, which itself was never pulled into `everlearning` for the same beyond-syllabus reason |
| `Binary_Search_and_Squaring_a_List.ipynb` | **Excluded** | A short binary-search drill; the algorithm is already solidly covered by `Tutorial_06_Finding_Things.ipynb` (MIT 6.8, "well covered" per the gap analysis) and this notebook adds no new technique or angle — reviewed and deliberately left out rather than adding redundant content |
| `week0_notebook.py` … `week9_10_notebook.py` (6 files) | `OtherCourses/Markov-Chains-and-Text-Generation/` | Renamed `.py` → `.ipynb` (they were valid notebook JSON saved with the wrong extension) and given descriptive names per week range. A 10-week advanced/extracurricular course (random walks → Markov chains → text generation), unrelated to QQI MIT/PDP — see that folder's README |
| `Part_1B_Bresenhams_Line_Algorithm.ipynb` | `OtherCourses/Computer-Graphics-Algorithms/` | Computer-graphics rasterization, unrelated to QQI MIT/PDP |
| `Part_2B_The_Midpoint_Circle_Algorithm.ipynb` | `OtherCourses/Computer-Graphics-Algorithms/` | Same |
| `structured_pruning_notebook_cells.py` | `OtherCourses/Neural-Network-Pruning/` | Graduate-level ML (Keras/TF structured pruning), unrelated to QQI MIT/PDP and a code fragment rather than a standalone notebook |

## Other repos checked

`2plus1coding` was re-reviewed at the same time (see `repo-inventory.md` §3 for the full read, and `LearningOutcomes/PDP/SUGGESTION_PDP-LO8_Team-Programming-Project.md` for how it's actually used — its `PROJECT_PLANNING.md` and `prompting-guide.html` are flagged there as directly reusable scaffolding for the team-project gap, not something to copy wholesale). No new files were pulled from it this pass.

Other repos under the `deweydex` account were surfaced by name only (`FromMLtoAI`, `AIML_WA`, `aiml-web-authoring`, `WADB_Tutorials`, `py5experiments`, `HTML-CSS-SQL-JS`, `webauthoringdemo`, `databaseL5`, and others) — none were opened, since their names suggest different modules entirely (web authoring/database, general AI/ML, creative coding) rather than QQI MIT/PDP. Flagging here in case any of them turn out to be worth a closer look later.
