---
title: "Introduction to Databases: From SQL to Pandas (1 of 3)"
slug: joins-sql-and-pandas-page-1
course: database-methods
series: notebooks
series_title: "Notebooks"
version: 2026.09.07.1
---

*Page 1 of 3.*

# Introduction to Databases: From SQL to Pandas

**Course:** Database Methods 5N0783 
**Institution:** Dublin and Dún Laoghaire ETB

---

## What This Tutorial Covers

This notebook introduces you to working with databases using two different approaches:

1. **SQL (Structured Query Language)** - The traditional language for databases
2. **Pandas** - A Python library that can do the same operations

For each concept, you'll see:
- What the operation does and why it's useful
- How to do it in SQL
- How to do the same thing in pandas
- When you might prefer one approach over the other

By the end, you'll understand that SQL and pandas are two different ways of asking questions about data - and both are valuable to know!

---

## Our Example: A Small Library Database

We'll use a library database with two tables:
- **Books**: Information about books
- **Authors**: Information about who wrote them

This is simple enough to understand but complex enough to demonstrate real database concepts.

## Setup: Import Libraries and Create Sample Database

Run this cell first to set everything up:

```python exec
id: joins-sql-and-pandas-page-1-1
# Import the libraries we'll need
import sqlite3
import pandas as pd

# Create a connection to a new database
conn = sqlite3.connect('library.db')
cursor = conn.cursor()

print("✓ Libraries imported and database connection created!")
```

---

# Part 1: Creating Tables

## Why Tables?

A **table** is like a spreadsheet - it has:
- **Rows** (also called records) - each row represents one item
- **Columns** (also called fields) - each column represents a property

For example, a Books table might have:
- One row for each book
- Columns for title, author, year, etc.

## Creating Tables with SQL

In SQL, we use `CREATE TABLE` to define the structure of our table.

```python exec
id: joins-sql-and-pandas-page-1-2
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
```

### What This SQL Does:

- `CREATE TABLE IF NOT EXISTS` - Makes a new table (if it doesn't already exist)
- `INTEGER PRIMARY KEY` - A unique number that identifies each row
- `TEXT NOT NULL` - Text that must have a value (can't be empty)
- `FOREIGN KEY` - Links the books table to the authors table

**Key concept:** The `author_id` in the books table references the `author_id` in the authors table. This creates a relationship between the tables.

---

# Part 2: Adding Data (INSERT)

Now let's add some data to our tables.

## Method 1: SQL INSERT Statements

SQL uses `INSERT INTO` to add new rows.

```python exec
id: joins-sql-and-pandas-page-1-3
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
```

### What This SQL Does:

- `INSERT INTO table_name` - Specifies which table to add to
- `VALUES (?, ?, ?)` - The `?` are placeholders for our data
- `executemany()` - Runs the same INSERT for multiple rows efficiently
- `INSERT OR IGNORE` - Skips the insert if that ID already exists (prevents duplicates)
- `conn.commit()` - Saves the changes to the database

**Important:** We added authors first because books reference them!

## Method 2: Using Pandas to Add Data

Pandas can also add data to SQL databases. It's sometimes easier when you already have data in DataFrames.

```python exec
id: joins-sql-and-pandas-page-1-4
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
```

```python exec
id: joins-sql-and-pandas-page-1-5
# Save DataFrames to the database
# (We use 'replace' here since we already added the data with SQL)
df_authors.to_sql('authors', conn, if_exists='replace', index=False)
df_books.to_sql('books', conn, if_exists='replace', index=False)

print("✓ Data added using pandas!")
```

### Pandas vs SQL for Adding Data:

**Use SQL when:**
- You're adding data directly to the database
- You need fine control over the insert process
- You're working with large amounts of data

**Use Pandas when:**
- You already have data in a DataFrame
- You've cleaned/transformed data and want to save it
- You're importing from CSV or Excel files

---

# Part 3: Reading Data (SELECT)

The most common operation is reading data from tables.

## SQL SELECT: Getting All Columns

`SELECT *` means "select all columns"

```python exec
id: joins-sql-and-pandas-page-1-6
# Get all books
cursor.execute('SELECT * FROM books')
results = cursor.fetchall()

print("All books (using SQL):")
for row in results[:3]:  # Show just first 3
    print(row)
```

### Pandas Equivalent: read_sql or Direct Access

Pandas makes this even easier - it returns a nicely formatted DataFrame.

```python exec
id: joins-sql-and-pandas-page-1-7
# Get all books using pandas
df_books = pd.read_sql('SELECT * FROM books', conn)

print("All books (using pandas):")
print(df_books.head(3))
```

## SQL SELECT: Choosing Specific Columns

Often you don't need all columns - you can specify which ones you want.

```python exec
id: joins-sql-and-pandas-page-1-8
# Get just title and year
cursor.execute('SELECT title, year_published FROM books')
results = cursor.fetchall()

print("Books with title and year (SQL):")
for row in results[:3]:
    print(f"{row[0]} ({row[1]})")
```

### Pandas Equivalent: Column Selection

In pandas, you can select columns using square brackets.

```python exec
id: joins-sql-and-pandas-page-1-9
# Two ways to select columns in pandas:

# Method 1: Use SQL
df_titles = pd.read_sql('SELECT title, year_published FROM books', conn)
print("Method 1 - Using SQL in pandas:")
print(df_titles.head(3))

# Method 2: Select from existing DataFrame
df_titles2 = df_books[['title', 'year_published']]
print("\nMethod 2 - Selecting from DataFrame:")
print(df_titles2.head(3))
```

**Pandas Note:** Notice we can either:
1. Use `pd.read_sql()` with a SQL query
2. Load the whole table, then select columns with `df[['col1', 'col2']]`

Both work! Method 2 is more "pandas-like" but Method 1 is closer to SQL.

---

# Part 4: Filtering Data (WHERE)

Often you want to find specific rows that meet certain criteria.

## SQL WHERE: Finding Fantasy Books

```python exec
id: joins-sql-and-pandas-page-1-10
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
```

### Pandas Equivalent: Boolean Indexing

Pandas uses boolean conditions inside square brackets to filter.

```python exec
id: joins-sql-and-pandas-page-1-11
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
```

**How pandas filtering works:**
- `df_books['genre'] == 'Fantasy'` creates a True/False column
- `df_books[True/False column]` keeps only True rows
- `[['title', 'genre', 'year_published']]` selects specific columns

## SQL WHERE: Books Published After 1980

```python exec
id: joins-sql-and-pandas-page-1-12
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
```

### Pandas Equivalent: Comparison Operators

```python exec
id: joins-sql-and-pandas-page-1-13
# Pandas filtering with >=
df_recent = df_books[df_books['year_published'] >= 1980][['title', 'year_published']]

print(f"Books from 1980 onwards (pandas): {len(df_recent)} books found")
print(df_recent)
```

## Looking back

Before leaving this page, a sentence on each. What you write stays on this device.

```reflect
- Something you expected before running a cell that turned out differently
- The one idea from this page you could explain to someone else now
- A question this page raised that it did not answer
```
