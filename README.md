# everlearning

everlearning is a staging ground for teaching material. It holds the originals as they were made, the Markdown versions converted from them, and a record of where each piece is headed. Nothing here is a finished course. Finished material lives in its own home: interactive tutorials in [dewlab](https://github.com/deweydex/dewlab) and [dewsharp](https://github.com/deweydex/dewsharp), quizzes in [WADB_Tutorials](https://github.com/deweydex/WADB_Tutorials), and write-ups on [jsaaron.com](https://jsaaron.com). This repository is where material waits, gets sorted, and gets decided on.

## How it is organised

The repository is organised by subject rather than by module, so the material can serve any programme that teaches the same ideas. Module codes appear in [INVENTORY.md](INVENTORY.md), not in folder names.

Each subject folder follows the same pattern. A `sources` folder holds originals: notebooks, PDFs, worksheets and small web projects. An `articles` folder holds Markdown conversions, arranged into series by the `.order.yaml` files beside them. A `briefs` folder holds assignment and project briefs where a subject has them.

| Folder | What it holds |
| --- | --- |
| `programming/` | Python tutorials, practice, object-oriented projects, the integrated programming and maths notebooks, and the enrichment notebooks |
| `ml-and-ai/` | Neural networks from scratch, learning a line, linear algebra, probability, the Markov chain and hidden-messages projects |
| `data-and-databases/` | SQLite, pandas and matplotlib notebooks, early SQL quizzes, the database project brief |
| `maths/` | The worksheet series from fractions to trigonometry, and earlier secondary-school material |
| `web/` | Break and Make a Website, the tax simulator, Web Authoring briefs and templates |
| `reference/` | Module descriptors |
| `tools/` | The read-aloud reader |
| `archive/` | Duplicates and superseded copies, kept until someone confirms they can go |

## Sources and articles

Many notebooks in `sources` have a Markdown twin in `articles`. Both copies stay for now, and the inventory pairs them. Each pair gets reviewed on its own, and the review decides which copy is current. When a twin is retired, it moves to `archive`.

## What does not live here

This repository is public, so solutions, exams and assessment data do not belong in it. They are gathered in `_to-private/` while a private repository is set up, and that folder disappears once they have moved.

## Adding material

New material goes into the subject it teaches, under `sources` if it is an original and `articles` if it is a conversion. Folder names use lowercase words joined by hyphens. Each new item gets a line in the inventory with its status and intended destination.
