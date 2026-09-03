# Fifteen repositories: what is there, what overlaps, and where it should go

_Written 2026-09-03. Successor to `repo-inventory.md` (2026-08-01), which looked at four repositories and named everlearning the curriculum home. A month later that is no longer true, and this document says why and what follows from it._

Scope: the fifteen repositories under `deweydex` that this session could read. One more is referenced from the class pages and was not readable here: `HTML-CSS-SQL-JS`, linked from the Web Authoring page for the week of 13 October. It belongs in this picture and should be looked at before anything is deleted.

---

## 1. Summary

**The centre already exists.** dewlab is where the tutorials live now. It has 47 tutorial pages (43 tutorials and four mixed problem sets), 40 practice pages, glossaries, a curriculum map keyed to the QQI descriptors, a plain-language pass, and, as of last week, a Python workspace that can also run HTML, CSS, SQL and JavaScript cells. Everything that is a tutorial should end up there, and most of what was a tutorial elsewhere already has. everlearning, Mathematics and python-with-ml are now source archives for it, whether or not their READMEs say so.

**The website is settled too.** flowershowtest is the public site and was committed to today. deweydex.github.io was the previous attempt at the same thing, from November 2025, and is superseded. The two carry three copies of the same sixty class handouts between them.

**Web authoring and databases are the loose end, and they are two different problems.** There is a lot of web authoring material (WADB_Tutorials, AIML_WA, webauthoringdemo, aiml-web-authoring, and the briefs on the site) and it overlaps in the way you expected. There is almost no database material: one SQLite notebook about dinosaurs, one SQL quiz, and links to Colab and Drive files that are in no repository at all. The web authoring problem is choosing between two tutorials and making one repository the student's starting point. The database problem is writing the module, and dewlab is the place to write it.

**The recommendation, in one paragraph.** Keep five repositories active: dewlab (all tutorials), flowershowtest (the site, the class pages, the briefs), one web authoring starter repository for students to fork (seeded from AIML_WA into the empty aiml-web-authoring, with WADB's templates and GitHub guides brought along), 2plus1Coding (a standalone workshop with its own audience), and FAQ (a writing tool, unrelated to teaching). Mark everlearning and Mathematics as archives of source material. Write the Database Methods module inside dewlab, where the SQL engine and the real-data apparatus already sit, and delete databaseL5 rather than start a third home for tutorials. Archive or delete the rest: deweydex.github.io once the root domain is redirected, WADB_Tutorials once its content has moved and its front page points to the new homes, python-with-ml once its three unique notebooks have been mined, and webauthoringdemo, FromMLtoAI and ML1-X now.

**Timing matters.** The class pages show web authoring running from September to December and databases from January. The starter repository is this month's work. The database module has until January. Web authoring tutorials inside dewlab, which need a small platform change, can wait until the summer.

---

## 2. The map

| Repository | What it is | Last commit | Verdict |
|---|---|---|---|
| dewlab | The tutorial platform and its content | 2026-09-02 | Centre. Everything tutorial-shaped goes here. |
| flowershowtest | The public site (Flowershow, markdown) | 2026-09-03 | Keep. Fix internal duplication. |
| everlearning | Notebook tutorials and planning that dewlab was converted from | 2026-08-01 | Archive of sources. Say so in the README. |
| Mathematics | 26 maths worksheets, markdown and PDF, with solutions | 2026-03-16 | Archive of sources. Tidy the duplicates first. |
| WADB_Tutorials | Hand-built HTML tutorial site: 13 lessons, GitHub guides, templates, a SQL quiz | 2025-12-17 | Mine, then retire behind a pointer. |
| AIML_WA | Fork-and-edit portfolio starter with 25 exercises in the README | 2026-01-27 | The better web authoring tutorial. Becomes the seed of the starter repo. |
| 2plus1Coding | "Coding with AI" workshop site, five projects, teacher guide | 2025-11-06 | Keep as is. Remove one duplicated file. |
| deweydex.github.io | Earlier hand-built site plus a homemade CMS | 2025-11-23 | Superseded. Redirect the root domain, then archive. |
| FAQ | A personal writing app (Preact) that publishes to a public FAQ page | 2026-07-24 | Unrelated to teaching. Leave alone. |
| python-with-ml | 12 Python notebooks, October 2025, no README | 2025-10-14 | Mine three notebooks, then archive. |
| FromMLtoAI | A README holding a workshop schedule | 2026-05-12 | Delete. The schedule is on the site already. |
| ML1-X | 2020 TU Berlin coursework and 44 MB of textbook chapter PDFs | 2020-11-09 | Archive. Check it is private. |
| aiml-web-authoring | README only | 2026-01-05 | Empty. The target for the web authoring starter. |
| databaseL5 | README only | 2025-11-12 | Empty. Delete; databases go to dewlab. |
| webauthoringdemo | One demo HTML file | 2026-01-20 | Delete. |

---

## 3. The target shape

Three kinds of thing are being kept, and each has one home.

**Tutorials live in dewlab.** A tutorial is prose a student reads with cells they run. dewlab's frontmatter, glossary files, practice pages, versioning and curriculum map exist so that a tutorial written once is findable, referenced, checkable against the descriptor, and safe to revise without losing a student's work. Any tutorial kept elsewhere loses all of that. The three empty module folders in `tutorials/` (`database-methods`, `mathematics-for-it`, `programming-design-principles`) are the platform's own statement of intent. The second and third are covered by the integrated module and can go. The first is the one to fill.

**Class-facing pages, briefs and handouts live in flowershowtest.** The week-by-week pages, the assessment briefs, the module descriptors, the guides and the prior-teaching record are a website, not a tutorial, and Flowershow is a good fit for them. The site should link out to dewlab for tutorials and to the starter repository for the student's own site, and hold nothing that duplicates either.

**The student's own website starts from one starter repository.** Web authoring is the one module where the pedagogy needs the student to own files, save them, refresh a browser, commit and see the result on GitHub Pages. A cell in a page cannot replace that, and the GitHub workflow is itself a learning outcome. So one repository exists to be forked, and it should be the only one.

Everything else is either an archive of sources (kept, read-only, labelled) or gone.

---

## 4. Web authoring and databases, in depth

### 4.1 What exists

Web authoring material is in five places.

WADB_Tutorials is a hand-written static site of 80 files: thirteen lessons (HTML basics through CSS animations), seven GitHub guides (six of them in both markdown and HTML), four examples, eleven templates, a design-resources page, troubleshooting, a quick reference, a project-ideas page, a code playground, a progress tracker and three themes. It is live at `deweydex.github.io/WADB_Tutorials` and the Web Authoring class page calls it "the tutorials we use". It also holds repository cruft that should not be there: `GIT_PUSH_INSTRUCTIONS.md` with a personal desktop path in it, `recent_chat_ideas.md` and `session_plan_advanced_content.md` (session logs from the assistant that built it), a `.DS_Store`, a root `styles.css` beside a `css/` directory, and `Educational_Reference_Document.md`, a byte-identical copy of the file in 2plus1Coding.

AIML_WA is six files: `index.html`, `about.html`, `styles.css`, a README of about twenty-five numbered exercises, a `CONCEPTS.md` of optional depth, and a licence. The HTML and CSS are commented so that the code files are the reference and the README is the path through them. It is live at `deweydex.github.io/AIML_WA` and the AIML class page links it as "our very own tutorial pages".

webauthoringdemo is a single demo page from a class in January. aiml-web-authoring is a README. flowershowtest holds the two assessment briefs (the 30% portfolio landing page and the 70% multi-page project), their planning and README templates, the "Under Construction: Resources" guidance page, the "Programs to Install" page and the module descriptor PDF for 5N1910.

Database material is in three places, and thin. `sqlite_tutorial.ipynb` (44 cells, dinosaurs and sea creatures, CREATE through JOIN) sits in flowershowtest's assets and twice in deweydex.github.io. `tentacular-plushies-quiz-final.html`, a SQL quiz, sits in WADB_Tutorials. The class pages for January through April link a database practice exam, a reference sheet, a "Database Dinosaur Exam", a pandas Colab notebook and "Our Tutorial Series so far", none of which are in any repository this session could see. The Database Methods descriptor (5N0783) is in flowershowtest's assets. dewlab has `run_query()` in its tools bridge and, since decision 7.118, a SQL cell type in dewmini running on Python's own `sqlite3`, so a table created in SQL is a table a Python cell can read with pandas.

### 4.2 Which web authoring tutorial is better

AIML_WA, and not narrowly. It is the one written the way the dewlab style guide asks for: try something, look at what happened, then get the name. Every exercise ends with an "Explore:" prompt that asks the student to break something and watch. The site is live from exercise two, so every later change is visible at a real URL. The reference is in the code as comments, where a student looks when confused, and `CONCEPTS.md` is offered as optional depth rather than prerequisite reading.

WADB_Tutorials is thorough and assumes nothing, which is a real virtue, but it reads as a reference manual. Each lesson opens with learning outcomes, then a section on why the topic matters, then the definitions, then a worked example, then practice. That is the reverse of explore-then-name. The prose is long. A quick measure of sentence length over the sources, counting sentences of three words or more:

| Source | Sentences | Mean words | Over 25 words |
|---|---|---|---|
| WADB lesson 01, HTML basics | 155 | 23.6 | 26% |
| WADB lesson 03, CSS basics | 147 | 20.4 | 18% |
| WADB GitHub guide 01 | 70 | 17.3 | 10% |
| AIML_WA README | 231 | 11.3 | 5% |
| AIML_WA CONCEPTS.md | 145 | 11.5 | 4% |
| dewlab, First Steps | 82 | 14.4 | 11% |
| dewlab, Grid of Numbers | 59 | 17.5 | 22% |

The style guide's target is twenty words and its ceiling is twenty-five. WADB's lessons run a quarter of their sentences over the ceiling. Its GitHub guides are the readable part, because they are procedural: do this, then this. They are also the part with the least pedagogical judgement in them, which is why they port well.

WADB's real value is not its lessons. It is the shelf around them: eleven templates with commented code, four small examples, the troubleshooting page, the quick reference, and lessons 11 to 13 on advanced flexbox and grid, component design and animation, which serve the 70% project brief's requirement for Flexbox, Grid and responsive layout. Those should survive. The lessons should not be ported as they are.

AIML_WA has its own faults. The README is one long file. A few of the Explore prompts use idioms the style guide flags ("sit with it for a moment"). It has no troubleshooting, no templates beyond its own pages, and nothing past a first portfolio. Those are exactly the gaps WADB fills.

### 4.3 The combined shape

One starter repository, whose contents are:

- AIML_WA's three files as the starting site, with the exercise numbers in the code comments kept.
- The README split into a short front page and a `docs/` folder: the path through the exercises, then the GitHub guides from WADB (the markdown versions, lightly edited; the seventh guide, on browser devtools, exists only as HTML and needs converting), then troubleshooting and the quick reference.
- WADB's `templates/` and `examples/` as a `templates/` folder, each file keeping its comments.
- `CONCEPTS.md` extended with the parts of WADB lessons 04, 05 and 11 that the 70% brief needs (box model, flexbox, grid, media queries), rewritten to the style guide rather than pasted.
- No SQL. The quiz goes with the database module.

The target repository is aiml-web-authoring, which you asked for: an empty repository, already named for the course. Nothing is lost by seeding it from AIML_WA, which has two commits. The name could become `web-authoring` later, since GitHub redirects renamed repositories, and the module is taught to both the AIML and Computer Science groups.

WADB_Tutorials then gets a one-paragraph notice on its front page pointing to the new starter repository and to dewlab, stays live until the class pages have been updated, and is archived. Its lessons 01 to 03 and 06 to 10 are not carried anywhere; their content is covered by the starter's exercises and CONCEPTS.md, and the rest belongs in dewlab when the web module is written there.

### 4.4 Where web authoring tutorials go later

The concept teaching (what a selector is, how the box model works, what flexbox does when the window narrows) is tutorial-shaped and belongs in dewlab in the end. dewlab's tutorial pages run only `python exec` cells today (`build.py` line 116). dewmini has had Web cells since decisions 7.116 through 7.121, including a split editor with a live preview, so the engine exists; what is missing is the fence tag, the build step and the runtime branch on a tutorial page. That is a bounded piece of platform work, and it is the kind the roadmap says to take: it multiplies content, because it unlocks a whole module. It is not this term's work. A `web-authoring` module folder in `tutorials/`, with the 5N1910 descriptor in `planning/curriculum/descriptors/` and its outcomes in `outcomes.yaml` so the curriculum map shows the gap, is a reasonable first commit.

### 4.5 Databases: write the module in dewlab

There is not enough database material to consolidate; there is a module to write. dewlab is the right place for five reasons. The SQL engine is already there. `run_query()` renders a query as a table on a tutorial page. The dataset apparatus (`data/`, `load_csv()`, the `datasets:` frontmatter, sidebar attribution) is built and, by the roadmap's own account, used by nothing yet; a database module built on an Our World in Data extract would be the first real-data tutorial the roadmap asks for, and it matches what the class project already does. The curriculum map will show 5N0783's outcomes in red until they are taught, which is how the other modules were driven to completion. And a tutorial in dewlab is one with practice pages, a glossary and versioning from the first commit.

A first outline, in the order the dinosaur notebook already teaches and the descriptor asks for:

1. **A table is a list of rows.** Port the dinosaur notebook: CREATE, INSERT, SELECT, with a SQL cell for each and a Python cell showing the same table through pandas. Drop the `ipython-sql` magics and the `pip install`; on Pyodide there is nothing to install.
2. **Asking questions of a table.** WHERE, ORDER BY, LIMIT, then COUNT, AVG, GROUP BY. The quiz's questions become the practice page.
3. **Two tables.** The sea creatures table, then JOIN, then why one table for both would have been wrong.
4. **Designing before typing.** Keys, one-to-many, the smallest normalisation a Level 5 student needs, and an ER diagram (the class page already links a SQL-to-ER tool).
5. **A real dataset.** An Our World in Data CSV loaded with `load_csv()`, written into SQLite, queried, and charted with matplotlib. This is the class project in miniature.

The practice exam and reference sheet the class pages link are assessments and belong in a private place, not in a public tutorial repository. databaseL5 is not needed for any of this and should be deleted rather than left as a third place tutorials might go.

---

## 5. Repository by repository

### dewlab

The centre, and in good order. 223 commits, the last yesterday. 37 tutorial pages under the integrated maths-and-programming module (33 tutorials and four mixed problem sets), 10 under computational methods, 40 practice pages, a glossary per tutorial, the curriculum map, a plain-language pass with its own ledger, and the workbench.

Things to do here as part of consolidation: delete the two empty module folders that the integrated module covers; add the 5N0783 and 5N1910 descriptor PDFs to `planning/curriculum/descriptors/` and their outcomes to the yaml so the map shows the gaps; write the database module; later, Web cells on tutorial pages and a web authoring module. `planning/BUILD_PLAN.md` still links `outlines/from-everlearning.md`, which was never written; either write it (this document is most of it) or drop the link.

### flowershowtest

The site, active today, and the right tool for what it holds. Two problems.

`Current Teaching/` and `Teaching Materials/Prior Teaching/2025-2026 Teaching/` hold the same tree twice: AI Workshops for Teachers, AI for Business, AIML Web Authoring, Mathematics, Research and Study Skills, Web Authoring and Databases. Most files are identical; eight already differ, so the drift has started. A prior-teaching snapshot should be taken once, at the end of a year, and then left alone, and the current tree should be the only one edited. Decide which copy is canonical for 2025-26 and delete the other, or make the current tree the 2026-27 one and let the snapshot stand.

`assets/` holds sixty class handouts, PDFs, notebooks and practice files. deweydex.github.io holds the same sixty in `materials/` and again in `Coda Export Joshua Aaron's Webpage/`, with `(1)`, `(2)` and `(3)` duplicates. Once deweydex.github.io is retired this resolves itself; until then, flowershowtest's copy is the one to edit.

Small things: `_import/QUESTIONS_FOR_JOSH.md` and `_import/LINK_AUDIT.md` are import-time notes and should either be answered and deleted or moved out of the content tree. The Web Authoring class page links WADB_Tutorials and AIML_WA; both links need updating when the starter repository exists.

### everlearning

The source dewlab was converted from. Its seventeen notebooks became dewlab's maths-and-programming series (the titles match one for one). Its practice bank gave dewlab's practice pages their questions. Its planning folder holds the inventory and gap analysis from August, which named everlearning "the current curriculum home"; that was true for about three weeks.

What is unique here and not yet in dewlab: the three sets of skills demos with solutions (assessments; see the question in section 7 about whether they should be public at all), the Taylor series enrichment notebook, the `LearningOutcomes/` drafts not yet turned into tutorials (a few have been: complex roots, limits, transposing formulae, sets and Venn diagrams all exist in dewlab now), the graphics-algorithms and neural-network-pruning courses under `OtherCourses/`, the Markov chains course (which dewlab's *Where Chains Lead* drew on), and `OldPDPMIT.zip`.

Recommendation: keep, mark the README as an archive of sources with a pointer to dewlab, correct the claim in `planning/repo-inventory.md`, and move the two descriptor PDFs to dewlab's descriptors folder. Nothing else needs to move until a dewlab tutorial wants it.

### Mathematics

Twenty-six worksheets for AIML Foundations Mathematics, in `markdown/` with PDFs of the worksheets, their solutions and nine annotated versions. dewlab's `EXERCISES.md` has already mined the twenty with answer keys. flowershowtest's Mathematics page links the "Somewhat-Traditional Worksheets", so the repository is still the class's handout shelf.

Tidy before archiving: ten root-level markdown files duplicate their `markdown/` versions (nine byte-identical, one that differs and needs a look) and should go; two exponents-and-logarithms worksheets exist only at the root and should move into `markdown/`; worksheet 02b exists as markdown, a Jupyter notebook and a marimo script, and the two computational versions are the seed of a dewlab tutorial if the topic is wanted. Then label the README as an archive.

### WADB_Tutorials

Covered in section 4. Mine the templates, examples, GitHub guides, troubleshooting and reference into the starter repository; give the quiz to the database module; leave a pointer on the front page; archive when the class pages stop linking it. The three assistant session logs and the personal-path instructions file should be deleted regardless.

### AIML_WA

Covered in section 4. The seed of the starter repository. Two commits, so nothing is lost by moving it; the live URL should carry a pointer until the class page changes.

### 2plus1Coding

A self-contained workshop site with its own audience (teachers running an AI-assisted pair-programming session), five projects each with beginner and advanced starters and Colab versions, a teacher guide, a prompting guide, and an archive of the earlier handouts. Its teacher guide is well written and plainly useful. Keep it as it is. The one change is `Educational_Reference_Document.md`, the LLM guide it shares byte for byte with WADB_Tutorials; dewlab's `PEDAGOGICAL_STYLE_GUIDE.md` superseded it (dewlab's roadmap records removing its own copy), so delete it here and in WADB and let the style guide be the one document.

### deweydex.github.io

The November 2025 site: hand-built HTML pages, a markdown CMS in `cms.html` and `edit/`, `pages/*.md` content, an audit report that puts it at sixty percent complete, and the Coda export it was built from. flowershowtest replaced it. Its unique content is small: `pages/podcast.md`, `pages/projects.md`, `norms-expectations.html`, two docx files in the Coda export (the Banana assignment brief and `Drafting_Guide_final.docx`). Check those against the site, copy over what is missing, then retire.

One caution before archiving: this repository serves the root of `deweydex.github.io`. The project sites (`/WADB_Tutorials/`, `/2plus1Coding/`, `/AIML_WA/`) are served from their own repositories and are unaffected, but the root URL is whatever this repository's Pages build is. If the Flowershow site is hosted elsewhere, replace this repository's content with a single redirect page before archiving. If the Flowershow site is meant to be the root site, this is the repository it has to be built into.

### FAQ

A writing app, with e2e tests, a deploy workflow and its own decisions log. It publishes a public FAQ page from a separate private content repository. It is not teaching material and shares only a name with flowershowtest's student FAQ. Leave it alone.

### python-with-ml

Twelve notebooks uploaded in one go in October 2025 with no README: Getting Started, History and ML Basics, Algorithms, Variables, Iteration, Lists, Functions, Testing and Debugging, Maths and Random, then NumPy, Matplotlib and Object-Oriented Programming. It is an independent lineage from everlearning's notebooks (no shared sentences between the two first-steps notebooks), a textbook-style series with anchors and "Think about it" reflections. dewlab already covers most of it. The three worth mining are Testing and Debugging (dewlab's *When It Goes Wrong* could take the testing half), NumPy (dewlab's matrices series touches it but does not teach the library), and Object-Oriented Programming, which dewlab does not teach at all. If the PDP descriptor asks for objects, this is the source. Then archive.

### FromMLtoAI

A README holding the schedule for the technical AI workshop for teachers. The same schedule is on the site under Technical AI Workshops for Teachers, Day 1. Delete.

### ML1-X

Coursework from a 2020 TU Berlin course, plus sixteen chapter PDFs of Duda, Hart and Stork's *Pattern Classification*, which is a copyrighted textbook. It has nothing to do with the teaching repositories. Archive it, and check that it is private; if it is public, the PDFs should come out of the history before it stays public.

### aiml-web-authoring, databaseL5, webauthoringdemo

Two READMEs and one demo page. aiml-web-authoring becomes the starter repository. databaseL5 is deleted, because the database module goes to dewlab. webauthoringdemo is deleted.

---

## 6. A sequence

**Now, an afternoon.** Delete webauthoringdemo and FromMLtoAI. Archive ML1-X after checking its visibility. Delete the shared LLM guide from 2plus1Coding and WADB. Tidy Mathematics (root duplicates, the two stray worksheets) and mark it an archive. Mark everlearning an archive and correct its inventory. Fix the flowershowtest duplication. Put all eight descriptor PDFs in dewlab's descriptors folder.

**September, before the web authoring assignment is set.** Build the starter repository in aiml-web-authoring from AIML_WA plus WADB's shelf, per section 4.3. Update the two class pages to link it. Put a pointer on WADB_Tutorials' and AIML_WA's front pages.

**Autumn.** Sort out the root domain, then retire deweydex.github.io. Mine python-with-ml's three notebooks into dewlab issues or outlines, then archive it.

**By January, when databases start.** The five database tutorials in dewlab, with the 5N0783 outcomes in the curriculum map. Delete databaseL5.

**Summer 2027.** Web cells on dewlab tutorial pages, then the web authoring module. Archive WADB_Tutorials.

---

## 7. Questions only you can answer

1. What is served at the root of `deweydex.github.io` today, and where is the Flowershow site hosted? This decides whether deweydex.github.io becomes a redirect or the build target.
2. Should the skills demos with solutions in everlearning be public at all? They are assessments.
3. What is in `HTML-CSS-SQL-JS`? It is linked from a class page and was not readable here.
4. Is the starter repository enough for web authoring for 2026-27, or is it worth doing the Web-cell platform work in dewlab this year?
5. Is ML1-X private?
6. Does the PDP descriptor ask for objects and classes? If it does, python-with-ml's OOP notebook is the source and the gap is real; if not, it can be archived without mining.
