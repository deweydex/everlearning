---
title: "Introduction to Databases: From SQL to Pandas (2 of 3)"
slug: joins-sql-and-pandas-page-2
course: database-methods
series: notebooks
series_title: "Notebooks"
version: 2026.09.07.1
---

*Page 2 of 3.*

*Before starting this page, run the cell below. It repeats the setup from the earlier pages that this page uses.*

```python exec
id: joins-sql-and-pandas-page-2-setup
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
```

## SQL WHERE: Multiple Conditions (AND, OR)

You can combine conditions with AND or OR.

```python exec
id: joins-sql-and-pandas-page-2-1
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
```

### Pandas Equivalent: Combining Conditions with & and |

```python exec
id: joins-sql-and-pandas-page-2-2
# Pandas uses & for AND and | for OR
# IMPORTANT: Need parentheses around each condition!
df_recent_fantasy = df_books[
    (df_books['genre'] == 'Fantasy') & 
    (df_books['year_published'] > 1985)
][['title', 'genre', 'year_published']]

print("Recent fantasy books (pandas):")
print(df_recent_fantasy)
```

**Important pandas syntax:**
- AND is `&` (not `and`)
- OR is `|` (not `or`)
- Each condition needs parentheses: `(condition1) & (condition2)`

---

# Part 5: Sorting Data (ORDER BY)

Sorting helps us see patterns - oldest to newest, shortest to longest, alphabetically, etc.

## SQL ORDER BY: Sorting Books by Year

```python exec
id: joins-sql-and-pandas-page-2-3
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
```

```python exec
id: joins-sql-and-pandas-page-2-4
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
```

### SQL Sort Options:
- `ASC` = ascending (smallest to largest, A to Z) - this is the default
- `DESC` = descending (largest to smallest, Z to A)

### Pandas Equivalent: sort_values()

```python exec
id: joins-sql-and-pandas-page-2-5
# Sort oldest first (ascending)
df_sorted_asc = df_books.sort_values('year_published', ascending=True)[['title', 'year_published']]
print("Books sorted by year (oldest first - pandas):")
print(df_sorted_asc)

# Sort newest first (descending)
df_sorted_desc = df_books.sort_values('year_published', ascending=False)[['title', 'year_published']]
print("\nBooks sorted by year (newest first - pandas):")
print(df_sorted_desc)
```

**Pandas Note:**
- `ascending=True` is like SQL's `ASC`
- `ascending=False` is like SQL's `DESC`

## SQL ORDER BY: Sorting by Multiple Columns

```python exec
id: joins-sql-and-pandas-page-2-6
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
```

### Pandas Equivalent: Sorting by Multiple Columns

```python exec
id: joins-sql-and-pandas-page-2-7
# Sort by multiple columns in pandas
df_multi_sort = df_books.sort_values(['genre', 'year_published'], ascending=[True, True])
print("Books sorted by genre, then year (pandas):")
print(df_multi_sort[['title', 'genre', 'year_published']])
```

---

# Part 6: Aggregation (COUNT, AVG, SUM, MIN, MAX)

Sometimes we want summary statistics rather than individual rows.

## SQL Aggregation: Counting Rows

```python exec
id: joins-sql-and-pandas-page-2-8
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
```

### SQL Aggregate Functions:
- `COUNT(*)` - Count all rows
- `AVG(column)` - Calculate average
- `SUM(column)` - Add up all values
- `MIN(column)` - Find smallest value
- `MAX(column)` - Find largest value

### Pandas Equivalent: Aggregation Methods

```python exec
id: joins-sql-and-pandas-page-2-9
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
```

**Pandas aggregation methods:**
- `len(df)` or `df['column'].count()` - Count rows
- `df['column'].mean()` - Calculate average
- `df['column'].sum()` - Add up values
- `df['column'].min()` - Find smallest
- `df['column'].max()` - Find largest

---

# Part 7: GROUP BY - The Most Powerful Feature

GROUP BY lets us calculate statistics **for each category** in our data.

## SQL GROUP BY: Books per Genre

```python exec
id: joins-sql-and-pandas-page-2-10
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
```

### What GROUP BY Does:
1. **Groups** all rows with the same genre together
2. **Calculates** the aggregate function (COUNT, AVG, etc.) for each group
3. **Returns** one row per group

### Pandas Equivalent: groupby()

```python exec
id: joins-sql-and-pandas-page-2-11
# Count books per genre in pandas
books_per_genre = df_books.groupby('genre').size()
print("Books per genre (pandas):")
print(books_per_genre)

# Or with more details:
books_per_genre_df = df_books.groupby('genre')['book_id'].count().reset_index()
books_per_genre_df.columns = ['genre', 'num_books']
print("\nBooks per genre (as DataFrame):")
print(books_per_genre_df)
```

## SQL GROUP BY: Average Pages per Genre

```python exec
id: joins-sql-and-pandas-page-2-12
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
```

### Pandas Equivalent: groupby with mean()

```python exec
id: joins-sql-and-pandas-page-2-13
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

## Looking back

Before leaving this page, a sentence on each. What you write stays on this device.

```reflect
- Something you expected before running a cell that turned out differently
- The one idea from this page you could explain to someone else now
- A question this page raised that it did not answer
```
