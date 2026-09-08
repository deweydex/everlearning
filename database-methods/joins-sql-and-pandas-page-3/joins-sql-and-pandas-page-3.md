---
title: "Introduction to Databases: From SQL to Pandas (3 of 3)"
slug: joins-sql-and-pandas-page-3
course: database-methods
series: notebooks
series_title: "Notebooks"
version: 2026.09.07.1
---

*Page 3 of 3.*

*Before starting this page, run the cell below. It repeats the setup from the earlier pages that this page uses.*

```python exec
id: joins-sql-and-pandas-page-3-setup
# From an earlier page of this tutorial: needed again here.
# Import the libraries we'll need
import sqlite3
import pandas as pd

# Create a connection to a new database
conn = sqlite3.connect('library.db')
cursor = conn.cursor()

print("✓ Libraries imported and database connection created!")

# From an earlier page of this tutorial: needed again here.
# Create the Authors table
cursor.execute('''
CREATE TABLE IF NOT EXISTS authors (
    author_id INTEGER PRIMARY KEY,
    author_name TEXT NOT NULL,
    birth_year INTEGER,
    nationality TEXT
)
''')

# Create the Books table
cursor.execute('''
CREATE TABLE IF NOT EXISTS books (
    book_id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    author_id INTEGER,
    genre TEXT,
    year_published INTEGER,
    pages INTEGER,
    FOREIGN KEY (author_id) REFERENCES authors(author_id)
)
''')

conn.commit()
print("✓ Tables created with SQL!")

# From an earlier page of this tutorial: needed again here.
# First, add authors (we need these before adding books that reference them)
authors_data = [
    (1, 'Terry Pratchett', 1948, 'British'),
    (2, 'Ursula K. Le Guin', 1929, 'American'),
    (3, 'Neil Gaiman', 1960, 'British'),
    (4, 'Octavia Butler', 1947, 'American'),
    (5, 'Douglas Adams', 1952, 'British')
]

cursor.executemany('''
INSERT OR IGNORE INTO authors (author_id, author_name, birth_year, nationality)
VALUES (?, ?, ?, ?)
''', authors_data)

# Now add books
books_data = [
    (1, 'Good Omens', 3, 'Fantasy', 1990, 288),
    (2, 'The Colour of Magic', 1, 'Fantasy', 1983, 206),
    (3, 'Mort', 1, 'Fantasy', 1987, 272),
    (4, 'A Wizard of Earthsea', 2, 'Fantasy', 1968, 183),
    (5, 'The Left Hand of Darkness', 2, 'Science Fiction', 1969, 304),
    (6, 'American Gods', 3, 'Fantasy', 2001, 465),
    (7, 'Kindred', 4, 'Science Fiction', 1979, 287),
    (8, 'Parable of the Sower', 4, 'Science Fiction', 1993, 345),
    (9, "The Hitchhiker's Guide to the Galaxy", 5, 'Science Fiction', 1979, 216),
    (10, 'Dirk Gently\'s Holistic Detective Agency', 5, 'Science Fiction', 1987, 247)
]

cursor.executemany('''
INSERT OR IGNORE INTO books (book_id, title, author_id, genre, year_published, pages)
VALUES (?, ?, ?, ?, ?, ?)
''', books_data)

conn.commit()
print(f"✓ Added {len(authors_data)} authors and {len(books_data)} books using SQL!")

# From an earlier page of this tutorial: needed again here.
# Create DataFrames with the same data
df_authors = pd.DataFrame(authors_data, 
                          columns=['author_id', 'author_name', 'birth_year', 'nationality'])

df_books = pd.DataFrame(books_data,
                        columns=['book_id', 'title', 'author_id', 'genre', 
                                'year_published', 'pages'])

# Show what the DataFrames look like
print("Authors DataFrame:")
print(df_authors.head())
print("\nBooks DataFrame:")
print(df_books.head())

# From an earlier page of this tutorial: needed again here.
# Save DataFrames to the database
# (We use 'replace' here since we already added the data with SQL)
df_authors.to_sql('authors', conn, if_exists='replace', index=False)
df_books.to_sql('books', conn, if_exists='replace', index=False)

print("✓ Data added using pandas!")

# From an earlier page of this tutorial: needed again here.
# Get all books
cursor.execute('SELECT * FROM books')
results = cursor.fetchall()

print("All books (using SQL):")
for row in results[:3]:  # Show just first 3
    print(row)

# From an earlier page of this tutorial: needed again here.
# Get all books using pandas
df_books = pd.read_sql('SELECT * FROM books', conn)

print("All books (using pandas):")
print(df_books.head(3))

# From an earlier page of this tutorial: needed again here.
# Get just title and year
cursor.execute('SELECT title, year_published FROM books')
results = cursor.fetchall()

print("Books with title and year (SQL):")
for row in results[:3]:
    print(f"{row[0]} ({row[1]})")

# From an earlier page of this tutorial: needed again here.
# Two ways to select columns in pandas:

# Method 1: Use SQL
df_titles = pd.read_sql('SELECT title, year_published FROM books', conn)
print("Method 1 - Using SQL in pandas:")
print(df_titles.head(3))

# Method 2: Select from existing DataFrame
df_titles2 = df_books[['title', 'year_published']]
print("\nMethod 2 - Selecting from DataFrame:")
print(df_titles2.head(3))

# From an earlier page of this tutorial: needed again here.
# Find all fantasy books
cursor.execute('''
SELECT title, genre, year_published
FROM books
WHERE genre = 'Fantasy'
''')

results = cursor.fetchall()
print("Fantasy books (SQL):")
for row in results:
    print(f"- {row[0]} ({row[2]})")

# From an earlier page of this tutorial: needed again here.
# Method 1: Using SQL
df_fantasy = pd.read_sql("""
    SELECT title, genre, year_published
    FROM books
    WHERE genre = 'Fantasy'
""", conn)

print("Fantasy books - Method 1 (SQL in pandas):")
print(df_fantasy)

# Method 2: Using pandas filtering
df_fantasy2 = df_books[df_books['genre'] == 'Fantasy'][['title', 'genre', 'year_published']]

print("\nFantasy books - Method 2 (pandas filtering):")
print(df_fantasy2)

# From an earlier page of this tutorial: needed again here.
# Find recent books
cursor.execute('''
SELECT title, year_published
FROM books
WHERE year_published >= 1980
''')

results = cursor.fetchall()
print(f"Books from 1980 onwards (SQL): {len(results)} books found")
for row in results:
    print(f"- {row[0]} ({row[1]})")

# From an earlier page of this tutorial: needed again here.
# Pandas filtering with >=
df_recent = df_books[df_books['year_published'] >= 1980][['title', 'year_published']]

print(f"Books from 1980 onwards (pandas): {len(df_recent)} books found")
print(df_recent)

# From an earlier page of this tutorial: needed again here.
# Find fantasy books published after 1985
cursor.execute('''
SELECT title, genre, year_published
FROM books
WHERE genre = 'Fantasy' AND year_published > 1985
''')

results = cursor.fetchall()
print("Recent fantasy books (SQL):")
for row in results:
    print(f"- {row[0]} ({row[2]})")

# From an earlier page of this tutorial: needed again here.
# Pandas uses & for AND and | for OR
# IMPORTANT: Need parentheses around each condition!
df_recent_fantasy = df_books[
    (df_books['genre'] == 'Fantasy') & 
    (df_books['year_published'] > 1985)
][['title', 'genre', 'year_published']]

print("Recent fantasy books (pandas):")
print(df_recent_fantasy)

# From an earlier page of this tutorial: needed again here.
# Sort by year, oldest first (ascending)
cursor.execute('''
SELECT title, year_published
FROM books
ORDER BY year_published ASC
''')

results = cursor.fetchall()
print("Books sorted by year (oldest first - SQL):")
for row in results:
    print(f"{row[1]}: {row[0]}")

# From an earlier page of this tutorial: needed again here.
# Sort by year, newest first (descending)
cursor.execute('''
SELECT title, year_published
FROM books
ORDER BY year_published DESC
''')

results = cursor.fetchall()
print("Books sorted by year (newest first - SQL):")
for row in results:
    print(f"{row[1]}: {row[0]}")

# From an earlier page of this tutorial: needed again here.
# Sort oldest first (ascending)
df_sorted_asc = df_books.sort_values('year_published', ascending=True)[['title', 'year_published']]
print("Books sorted by year (oldest first - pandas):")
print(df_sorted_asc)

# Sort newest first (descending)
df_sorted_desc = df_books.sort_values('year_published', ascending=False)[['title', 'year_published']]
print("\nBooks sorted by year (newest first - pandas):")
print(df_sorted_desc)

# From an earlier page of this tutorial: needed again here.
# Sort by genre first, then by year within each genre
cursor.execute('''
SELECT title, genre, year_published
FROM books
ORDER BY genre ASC, year_published ASC
''')

results = cursor.fetchall()
print("Books sorted by genre, then year (SQL):")
for row in results:
    print(f"{row[1]:<20} {row[2]}: {row[0]}")

# From an earlier page of this tutorial: needed again here.
# Sort by multiple columns in pandas
df_multi_sort = df_books.sort_values(['genre', 'year_published'], ascending=[True, True])
print("Books sorted by genre, then year (pandas):")
print(df_multi_sort[['title', 'genre', 'year_published']])

# From an earlier page of this tutorial: needed again here.
# How many books do we have?
cursor.execute('SELECT COUNT(*) FROM books')
count = cursor.fetchone()[0]
print(f"Total number of books (SQL): {count}")

# How many pages on average?
cursor.execute('SELECT AVG(pages) FROM books')
avg_pages = cursor.fetchone()[0]
print(f"Average pages (SQL): {avg_pages:.1f}")

# Shortest and longest book?
cursor.execute('SELECT MIN(pages), MAX(pages) FROM books')
min_pages, max_pages = cursor.fetchone()
print(f"Shortest book (SQL): {min_pages} pages")
print(f"Longest book (SQL): {max_pages} pages")

# From an earlier page of this tutorial: needed again here.
# Count rows
count = len(df_books)
# Or: count = df_books['book_id'].count()
print(f"Total number of books (pandas): {count}")

# Average pages
avg_pages = df_books['pages'].mean()
print(f"Average pages (pandas): {avg_pages:.1f}")

# Min and Max
min_pages = df_books['pages'].min()
max_pages = df_books['pages'].max()
print(f"Shortest book (pandas): {min_pages} pages")
print(f"Longest book (pandas): {max_pages} pages")

# From an earlier page of this tutorial: needed again here.
# Count how many books in each genre
cursor.execute('''
SELECT genre, COUNT(*) as num_books
FROM books
GROUP BY genre
''')

results = cursor.fetchall()
print("Books per genre (SQL):")
for row in results:
    print(f"- {row[0]}: {row[1]} books")

# From an earlier page of this tutorial: needed again here.
# Count books per genre in pandas
books_per_genre = df_books.groupby('genre').size()
print("Books per genre (pandas):")
print(books_per_genre)

# Or with more details:
books_per_genre_df = df_books.groupby('genre')['book_id'].count().reset_index()
books_per_genre_df.columns = ['genre', 'num_books']
print("\nBooks per genre (as DataFrame):")
print(books_per_genre_df)

# From an earlier page of this tutorial: needed again here.
# Calculate average pages for each genre
cursor.execute('''
SELECT genre, AVG(pages) as avg_pages
FROM books
GROUP BY genre
ORDER BY avg_pages DESC
''')

results = cursor.fetchall()
print("Average pages per genre (SQL):")
for row in results:
    print(f"- {row[0]}: {row[1]:.1f} pages on average")

# From an earlier page of this tutorial: needed again here.
# Calculate average pages per genre
avg_pages_per_genre = df_books.groupby('genre')['pages'].mean().sort_values(ascending=False)
print("Average pages per genre (pandas):")
print(avg_pages_per_genre)

# Or with more control:
avg_pages_df = df_books.groupby('genre')['pages'].mean().reset_index()
avg_pages_df.columns = ['genre', 'avg_pages']
avg_pages_df = avg_pages_df.sort_values('avg_pages', ascending=False)
print("\nAverage pages per genre (as DataFrame):")
print(avg_pages_df)
```

## SQL GROUP BY: Multiple Statistics at Once

```python exec
id: joins-sql-and-pandas-page-3-1
# Get count, average, min, and max for each genre
cursor.execute('''
SELECT 
    genre,
    COUNT(*) as num_books,
    AVG(pages) as avg_pages,
    MIN(pages) as shortest,
    MAX(pages) as longest
FROM books
GROUP BY genre
''')

results = cursor.fetchall()
print("Genre statistics (SQL):")
for row in results:
    print(f"\n{row[0]}:")
    print(f"  Books: {row[1]}")
    print(f"  Average: {row[2]:.1f} pages")
    print(f"  Range: {row[3]} to {row[4]} pages")
```

### Pandas Equivalent: agg() with Multiple Functions

```python exec
id: joins-sql-and-pandas-page-3-2
# Calculate multiple statistics at once
genre_stats = df_books.groupby('genre')['pages'].agg([
    ('num_books', 'count'),
    ('avg_pages', 'mean'),
    ('shortest', 'min'),
    ('longest', 'max')
]).round(1)

print("Genre statistics (pandas):")
print(genre_stats)
```

---

# Part 8: Joining Tables

The real power of databases is connecting information across tables.

## SQL JOIN: Combining Books with Authors

Right now, the books table only has an author_id. To see author names, we need to JOIN.

```python exec
id: joins-sql-and-pandas-page-3-3
# Join books with authors to see author names
cursor.execute('''
SELECT books.title, authors.author_name, books.year_published
FROM books
JOIN authors ON books.author_id = authors.author_id
ORDER BY books.year_published
''')

results = cursor.fetchall()
print("Books with author names (SQL):")
for row in results:
    print(f"{row[2]}: {row[0]} by {row[1]}")
```

### How SQL JOIN Works:
- `JOIN authors ON books.author_id = authors.author_id`
- For each book, SQL finds the matching author row
- It combines columns from both tables into one result
- Use `table.column` to specify which table a column comes from

### Pandas Equivalent: merge()

```python exec
id: joins-sql-and-pandas-page-3-4
# Method 1: Using SQL in pandas
df_joined = pd.read_sql('''
    SELECT books.title, authors.author_name, books.year_published
    FROM books
    JOIN authors ON books.author_id = authors.author_id
    ORDER BY books.year_published
''', conn)

print("Books with author names (SQL in pandas):")
print(df_joined)

# Method 2: Using pandas merge
df_joined2 = df_books.merge(df_authors, on='author_id')
df_joined2 = df_joined2[['title', 'author_name', 'year_published']].sort_values('year_published')

print("\nBooks with author names (pandas merge):")
print(df_joined2)
```

**Pandas merge() parameters:**
- `df1.merge(df2, on='common_column')` - Join on a shared column
- `how='inner'` - Only keep rows that match in both tables (default)
- `how='left'` - Keep all rows from left table
- `how='right'` - Keep all rows from right table
- `how='outer'` - Keep all rows from both tables

## SQL JOIN with GROUP BY: Books per Author

```python exec
id: joins-sql-and-pandas-page-3-5
# Count how many books each author has
cursor.execute('''
SELECT authors.author_name, COUNT(*) as num_books
FROM books
JOIN authors ON books.author_id = authors.author_id
GROUP BY authors.author_name
ORDER BY num_books DESC
''')

results = cursor.fetchall()
print("Books per author (SQL):")
for row in results:
    print(f"- {row[0]}: {row[1]} books")
```

### Pandas Equivalent: Merge then GroupBy

```python exec
id: joins-sql-and-pandas-page-3-6
# Join tables first, then group
df_joined = df_books.merge(df_authors, on='author_id')
books_per_author = df_joined.groupby('author_name').size().sort_values(ascending=False)

print("Books per author (pandas):")
print(books_per_author)
```

---

# Summary: SQL vs Pandas Quick Reference

| Operation | SQL | Pandas |
|-----------|-----|--------|
| **Select all** | `SELECT * FROM table` | `pd.read_sql('SELECT * FROM table', conn)` |
| **Select columns** | `SELECT col1, col2 FROM table` | `df[['col1', 'col2']]` |
| **Filter** | `WHERE condition` | `df[df['col'] == value]` |
| **Sort** | `ORDER BY col DESC` | `df.sort_values('col', ascending=False)` |
| **Count** | `COUNT(*)` | `len(df)` or `df['col'].count()` |
| **Average** | `AVG(col)` | `df['col'].mean()` |
| **Sum** | `SUM(col)` | `df['col'].sum()` |
| **Min/Max** | `MIN(col)`, `MAX(col)` | `df['col'].min()`, `df['col'].max()` |
| **Group by** | `GROUP BY col` | `df.groupby('col')` |
| **Join** | `JOIN table2 ON condition` | `df1.merge(df2, on='col')` |

## When to Use SQL vs Pandas?

**Use SQL when:**
- Working with very large databases (millions of rows)
- You need to extract specific data before analyzing
- Working with production databases shared by multiple systems
- You want to learn the industry-standard database language

**Use Pandas when:**
- Data is already loaded in memory
- You need to clean or transform data before/after queries
- You want to create visualizations or reports
- You're doing exploratory data analysis
- You prefer Python syntax to SQL

**Best practice:** Many data analysts use BOTH!
- Use SQL to extract data from large databases
- Use pandas for analysis, cleaning, and visualization

---

# Practice Exercises

Try these exercises using BOTH SQL and pandas!

## Your turn 1: Books by British Authors
Find all books written by British authors. Show the title, author name, and year.

**Hint:** You'll need to JOIN the tables and use WHERE

```python exec
id: joins-sql-and-pandas-page-3-7
# Your SQL solution here
```

```python exec
id: joins-sql-and-pandas-page-3-8
# Your pandas solution here
```

## Your turn 2: Longest Book per Genre
For each genre, find the longest book. Show genre, title, and number of pages.

**Hint:** This is challenging! You might need a subquery or multiple steps.

```python exec
id: joins-sql-and-pandas-page-3-9
# Your SQL solution here
```

```python exec
id: joins-sql-and-pandas-page-3-10
# Your pandas solution here
```

## Your turn 3: Author with Most Pages Written
Which author has written the most total pages across all their books?

**Hint:** JOIN, GROUP BY, SUM, ORDER BY

```python exec
id: joins-sql-and-pandas-page-3-11
# Your SQL solution here
```

```python exec
id: joins-sql-and-pandas-page-3-12
# Your pandas solution here
```

---

# What's Next?

Now that you understand the basics, you're ready to:

1. **Start your database project** - Use these techniques with your own data
2. **Learn more advanced SQL** - Subqueries, HAVING, DISTINCT, LIMIT
3. **Explore more pandas** - Merging multiple tables, pivot tables, advanced grouping
4. **Add visualizations** - Use matplotlib to visualize your query results
5. **Create interactive tools** - Build forms with ipywidgets

Remember: SQL and pandas aren't competitors - they're partners! Learn both, and use whichever makes sense for each task.

```python exec
id: joins-sql-and-pandas-page-3-13
# Don't forget to close the database connection when you're done!
conn.close()
print("✓ Database connection closed. Thanks for learning!")
```

## Looking back

Before leaving this page, a sentence on each. What you write stays on this device.

```reflect
- Something you expected before running a cell that turned out differently
- The one idea from this page you could explain to someone else now
- A question this page raised that it did not answer
```
