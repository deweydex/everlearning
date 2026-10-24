# Changes from V2 to V3: Database-Methods-5N0783

V3 is built from V2 by `_reorg/build_v3.py`. It is the language-and-environment pass described in the critique: outcome lists moved to the end, tables of contents removed, praise and reassurance removed, mastery and drill headings renamed, a looking-back cell with the learner's own question at the end of every core notebook, a question posed after examples that judge a person, a way of knowing after the learner cells of the notebooks written for this collection, the SQL introduction freed of its installation, an entry notebook per course, and Option D on the assessment brief. Nothing else was edited.

- `Database-Methods-5N0783/01_Introduction_to_SQLite.ipynb`: praise lines removed
- `Database-Methods-5N0783/01_Introduction_to_SQLite.ipynb`: looking-back cell added
- `Database-Methods-5N0783/02_Pandas_Star_Trek_Tutorial.ipynb`: "Exercise" headings renamed "Your turn" (7)
- `Database-Methods-5N0783/02_Pandas_Star_Trek_Tutorial.ipynb`: looking-back cell added
- `Database-Methods-5N0783/03_Pandas_and_Matplotlib.ipynb`: looking-back cell added
- `Database-Methods-5N0783/04_Pandas_versus_SQL.ipynb`: looking-back cell added
- `Database-Methods-5N0783/06_From_Pandas_to_SQLite__page1of2.ipynb`: looking-back cell added
- `Database-Methods-5N0783/06_From_Pandas_to_SQLite__page2of2.ipynb`: looking-back cell added
- `Database-Methods-5N0783/07_Interactive_Widgets.ipynb`: looking-back cell added
- `Database-Methods-5N0783/08_Inserting_Rows_and_Building_Forms.ipynb`: looking-back cell added
- `Database-Methods-5N0783/01_Introduction_to_SQLite.ipynb`: rebuilt on the sqlite3 library that every later notebook uses: the package install, the notebook extension and the %%sql magics are gone, replaced by one small run_sql function defined at the top, so the first lesson works wherever the last one does
- `Database-Methods-5N0783/New_00_Your_Questions.ipynb`: new: an entry notebook that asks for the situations from the learner's own life the course might reach, and tells the teacher what to do with them
