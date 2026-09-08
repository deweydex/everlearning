---
title: "Pandas vs SQL Cheat Sheet"
slug: 05-pandas-sql-cheat-sheet
course: database-methods
course_title: "Database Methods"
series: core
series_title: "Notebooks"
version: 2026.09.06.1
---

# Pandas vs SQL Cheat Sheet
## Using a Terry Pratchett Discworld Books Dataset

This notebook provides a side-by-side comparison of common operations in pandas and SQL (SQLite3), using a fun dataset based on Terry Pratchett's Discworld books.

## Setup and Imports

```python exec
id: 05-pandas-sql-cheat-sheet-1
import pandas as pd
import numpy as np
import sqlite3
import matplotlib.pyplot as plt

# Set pandas options for better display
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

# Create SQLite connection
conn = sqlite3.connect(':memory:')
cursor = conn.cursor()
```

## 1. Creating Data Structures

### Creating a DataFrame/Table

#### Pandas

```python exec
id: 05-pandas-sql-cheat-sheet-2
# Create books DataFrame
books_data = {
    'book_id': [1, 2, 3, 4, 5],
    'title': ['The Colour of Magic', 'Guards! Guards!', 'Mort', 'Going Postal', 'Small Gods'],
    'pub_year': [1983, 1989, 1987, 2004, 1992],
    'pages': [288, 355, 304, 394, 400],
    'main_character': ['Rincewind', 'Sam Vimes', 'Death', 'Moist von Lipwig', 'Brutha'],
    'sub_series': ['Rincewind', 'City Watch', 'Death', 'Moist von Lipwig', 'One-off']
}

books_df = pd.DataFrame(books_data)
books_df
```

```python exec
id: 05-pandas-sql-cheat-sheet-3
# Create characters DataFrame
characters_data = {
    'char_id': [1, 2, 3, 4, 5, 6],
    'name': ['Rincewind', 'Sam Vimes', 'Death', 'Moist von Lipwig', 'Brutha', 'Granny Weatherwax'],
    'occupation': ['Wizzard', 'Guard', 'Anthropomorphic Personification', 'Postmaster', 'Novice', 'Witch'],
    'location': ['Unseen University', 'Ankh-Morpork', "Death's Domain", 'Ankh-Morpork', 'Omnia', 'Lancre'],
    'first_appearance': [1, 8, 1, 33, 13, 6]
}

characters_df = pd.DataFrame(characters_data)
characters_df
```

#### SQL (SQLite3)

```python exec
id: 05-pandas-sql-cheat-sheet-4
# Create books table
cursor.execute('''
CREATE TABLE books (
    book_id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    pub_year INTEGER,
    pages INTEGER,
    main_character TEXT,
    sub_series TEXT
);
''')

# Insert book data
cursor.executemany('''
INSERT INTO books (book_id, title, pub_year, pages, main_character, sub_series)
VALUES (?, ?, ?, ?, ?, ?);
''', [
    (1, 'The Colour of Magic', 1983, 288, 'Rincewind', 'Rincewind'),
    (2, 'Guards! Guards!', 1989, 355, 'Sam Vimes', 'City Watch'),
    (3, 'Mort', 1987, 304, 'Death', 'Death'),
    (4, 'Going Postal', 2004, 394, 'Moist von Lipwig', 'Moist von Lipwig'),
    (5, 'Small Gods', 1992, 400, 'Brutha', 'One-off')
])

# Create characters table
cursor.execute('''
CREATE TABLE characters (
    char_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    occupation TEXT,
    location TEXT,
    first_appearance INTEGER
);
''')

# Insert character data
cursor.executemany('''
INSERT INTO characters (char_id, name, occupation, location, first_appearance)
VALUES (?, ?, ?, ?, ?);
''', [
    (1, 'Rincewind', 'Wizzard', 'Unseen University', 1),
    (2, 'Sam Vimes', 'Guard', 'Ankh-Morpork', 8),
    (3, 'Death', 'Anthropomorphic Personification', "Death's Domain", 1),
    (4, 'Moist von Lipwig', 'Postmaster', 'Ankh-Morpork', 33),
    (5, 'Brutha', 'Novice', 'Omnia', 13),
    (6, 'Granny Weatherwax', 'Witch', 'Lancre', 6)
])

conn.commit()

# Verify the data was inserted correctly
pd.read_sql("SELECT * FROM books", conn)
```

## 2. Basic Data Exploration

### Viewing Data

#### Pandas

```python exec
id: 05-pandas-sql-cheat-sheet-5
# View first 5 rows
books_df.head()
```

```python exec
id: 05-pandas-sql-cheat-sheet-6
# View shape and data types
print(f"Shape: {books_df.shape}")
books_df.dtypes
```

```python exec
id: 05-pandas-sql-cheat-sheet-7
# Summary statistics
books_df.describe()
```

#### SQL (SQLite3)

```python exec
id: 05-pandas-sql-cheat-sheet-8
# View first 5 rows
pd.read_sql("SELECT * FROM books LIMIT 5", conn)
```

```python exec
id: 05-pandas-sql-cheat-sheet-9
# Get column information
cursor.execute("PRAGMA table_info(books)")
cursor.fetchall()
```

```python exec
id: 05-pandas-sql-cheat-sheet-10
# Basic statistics
pd.read_sql("""
SELECT
    COUNT(*) as count,
    MIN(pub_year) as min_year,
    MAX(pub_year) as max_year,
    AVG(pages) as avg_pages
FROM books
""", conn)
```

## 3. Column Operations

### Selecting Columns

#### Pandas

```python exec
id: 05-pandas-sql-cheat-sheet-11
# Select single column
books_df['title']
```

```python exec
id: 05-pandas-sql-cheat-sheet-12
# Select multiple columns
books_df[['title', 'pub_year', 'main_character']]
```

#### SQL (SQLite3)

```python exec
id: 05-pandas-sql-cheat-sheet-13
# Select single column
pd.read_sql("SELECT title FROM books", conn)
```

```python exec
id: 05-pandas-sql-cheat-sheet-14
# Select multiple columns
pd.read_sql("SELECT title, pub_year, main_character FROM books", conn)
```

### Renaming Columns

#### Pandas

```python exec
id: 05-pandas-sql-cheat-sheet-15
# Rename specific columns
renamed_df = books_df.rename(columns={
    'pub_year': 'year_published',
    'main_character': 'protagonist'
})
renamed_df.head()
```

```python exec
id: 05-pandas-sql-cheat-sheet-16
# Rename all columns
renamed_all_df = books_df.copy()
renamed_all_df.columns = ['id', 'book_title', 'year', 'page_count', 'hero', 'series']
renamed_all_df.head()
```

#### SQL (SQLite3)

```python exec
id: 05-pandas-sql-cheat-sheet-17
# Use column aliases in query (doesn't change the original table)
pd.read_sql("""
SELECT
    book_id as id,
    title as book_title,
    pub_year as year,
    pages as page_count,
    main_character as hero,
    sub_series as series
FROM books
""", conn)
```

### Dropping Columns

#### Pandas

```python exec
id: 05-pandas-sql-cheat-sheet-18
# Drop a single column
books_df.drop('pages', axis=1).head()
```

```python exec
id: 05-pandas-sql-cheat-sheet-19
# Drop multiple columns
books_df.drop(['pub_year', 'sub_series'], axis=1).head()
```

#### SQL (SQLite3)

```python exec
id: 05-pandas-sql-cheat-sheet-20
# Select only the columns you want to keep
pd.read_sql("SELECT book_id, title, main_character FROM books", conn)
```

## 4. Adding and Modifying Data

### Adding New Columns

#### Pandas

```python exec
id: 05-pandas-sql-cheat-sheet-21
# Add a constant column
books_with_author = books_df.copy()
books_with_author['author'] = 'Terry Pratchett'
books_with_author.head()
```

```python exec
id: 05-pandas-sql-cheat-sheet-22
# Add a calculated column
books_with_age = books_df.copy()
books_with_age['age'] = 2023 - books_with_age['pub_year']
books_with_age.head()
```

#### SQL (SQLite3)

```python exec
id: 05-pandas-sql-cheat-sheet-23
# Add a constant column
cursor.execute("ALTER TABLE books ADD COLUMN author TEXT DEFAULT 'Terry Pratchett';")
conn.commit()
pd.read_sql("SELECT * FROM books", conn)
```

```python exec
id: 05-pandas-sql-cheat-sheet-24
# Add a calculated column (in a query - doesn't modify the table)
pd.read_sql("SELECT *, 2023 - pub_year as age FROM books", conn)
```

### Adding New Rows

#### Pandas

```python exec
id: 05-pandas-sql-cheat-sheet-25
# Add a single row
new_book = pd.DataFrame([{
    'book_id': 6,
    'title': 'Wyrd Sisters',
    'pub_year': 1988,
    'pages': 265,
    'main_character': 'Granny Weatherwax',
    'sub_series': 'Witches'
}])
more_books_df = pd.concat([books_df, new_book], ignore_index=True)
more_books_df
```

#### SQL (SQLite3)

```python exec
id: 05-pandas-sql-cheat-sheet-26
# Add a single row
cursor.execute("""
INSERT INTO books (book_id, title, pub_year, pages, main_character, sub_series)
VALUES (6, 'Wyrd Sisters', 1988, 265, 'Granny Weatherwax', 'Witches');
""")
conn.commit()
pd.read_sql("SELECT * FROM books", conn)
```

### Updating Existing Values

#### Pandas

```python exec
id: 05-pandas-sql-cheat-sheet-27
# Update a specific value
update_df = books_df.copy()
update_df.loc[update_df['title'] == 'Small Gods', 'pages'] = 403
update_df[update_df['title'] == 'Small Gods']
```

```python exec
id: 05-pandas-sql-cheat-sheet-28
# Update multiple rows based on condition
update_df.loc[update_df['sub_series'] == 'One-off', 'sub_series'] = 'Standalone'
update_df
```

#### SQL (SQLite3)

```python exec
id: 05-pandas-sql-cheat-sheet-29
# Update a specific value
cursor.execute("UPDATE books SET pages = 403 WHERE title = 'Small Gods';")
conn.commit()
pd.read_sql("SELECT * FROM books WHERE title = 'Small Gods'", conn)
```

```python exec
id: 05-pandas-sql-cheat-sheet-30
# Update multiple rows based on condition
cursor.execute("UPDATE books SET sub_series = 'Standalone' WHERE sub_series = 'One-off';")
conn.commit()
pd.read_sql("SELECT * FROM books", conn)
```

## 5. Query and Filtering Operations

#### Pandas

```python exec
id: 05-pandas-sql-cheat-sheet-31
# Books published after 1990
books_df[books_df['pub_year'] > 1990]
```

```python exec
id: 05-pandas-sql-cheat-sheet-32
# Multiple conditions: Books from the 80s
books_df[(books_df['pub_year'] >= 1980) & (books_df['pub_year'] < 1990)]
```

```python exec
id: 05-pandas-sql-cheat-sheet-33
# Using .isin() for multiple values
selected_chars = ['Rincewind', 'Death']
books_df[books_df['main_character'].isin(selected_chars)]
```

#### SQL (SQLite3)

```python exec
id: 05-pandas-sql-cheat-sheet-34
# Books published after 1990
pd.read_sql("SELECT * FROM books WHERE pub_year > 1990", conn)
```

```python exec
id: 05-pandas-sql-cheat-sheet-35
# Multiple conditions: Books from the 80s
pd.read_sql("""
SELECT * FROM books
WHERE pub_year >= 1980 AND pub_year < 1990
""", conn)
```

```python exec
id: 05-pandas-sql-cheat-sheet-36
# Using IN for multiple values
pd.read_sql("""
SELECT * FROM books
WHERE main_character IN ('Rincewind', 'Death')
""", conn)
```

### String Operations

#### Pandas

```python exec
id: 05-pandas-sql-cheat-sheet-37
# Books with titles containing "of"
books_df[books_df['title'].str.contains('of')]
```

#### SQL (SQLite3)

```python exec
id: 05-pandas-sql-cheat-sheet-38
# Books with titles containing "of"
pd.read_sql("SELECT * FROM books WHERE title LIKE '%of%'", conn)
```

## 6. Sorting and Ordering

#### Pandas

```python exec
id: 05-pandas-sql-cheat-sheet-39
# Sort by year (ascending)
books_df.sort_values('pub_year')
```

```python exec
id: 05-pandas-sql-cheat-sheet-40
# Sort by multiple columns with mixed direction
books_df.sort_values(['sub_series', 'pub_year'], ascending=[True, False])
```

#### SQL (SQLite3)

```python exec
id: 05-pandas-sql-cheat-sheet-41
# Sort by year (ascending)
pd.read_sql("SELECT * FROM books ORDER BY pub_year", conn)
```

```python exec
id: 05-pandas-sql-cheat-sheet-42
# Sort by multiple columns with mixed direction
pd.read_sql("SELECT * FROM books ORDER BY sub_series ASC, pub_year DESC", conn)
```

## 7. Aggregations and Grouping

#### Pandas

```python exec
id: 05-pandas-sql-cheat-sheet-43
# Count books by sub-series
books_df.groupby('sub_series').size()
```

```python exec
id: 05-pandas-sql-cheat-sheet-44
# Calculate average pages by sub-series
books_df.groupby('sub_series')['pages'].mean()
```

```python exec
id: 05-pandas-sql-cheat-sheet-45
# Multiple aggregations
books_df.groupby('sub_series').agg({
    'book_id': 'count',
    'pages': ['mean', 'sum'],
    'pub_year': ['min', 'max']
})
```

#### SQL (SQLite3)

```python exec
id: 05-pandas-sql-cheat-sheet-46
# Count books by sub-series
pd.read_sql("""
SELECT sub_series, COUNT(*) as book_count
FROM books
GROUP BY sub_series
""", conn)
```

```python exec
id: 05-pandas-sql-cheat-sheet-47
# Calculate average pages by sub-series
pd.read_sql("""
SELECT sub_series, AVG(pages) as avg_pages
FROM books
GROUP BY sub_series
""", conn)
```

```python exec
id: 05-pandas-sql-cheat-sheet-48
# Multiple aggregations
pd.read_sql("""
SELECT
    sub_series,
    COUNT(book_id) as book_count,
    AVG(pages) as avg_pages,
    SUM(pages) as total_pages,
    MIN(pub_year) as earliest_book,
    MAX(pub_year) as latest_book
FROM books
GROUP BY sub_series
""", conn)
```

## 8. Joining and Merging

#### Pandas

```python exec
id: 05-pandas-sql-cheat-sheet-49
# Inner join books with characters
pd.merge(
    books_df,
    characters_df,
    left_on='main_character',
    right_on='name',
    how='inner'
)
```

```python exec
id: 05-pandas-sql-cheat-sheet-50
# Left join - keep all books
pd.merge(
    books_df,
    characters_df,
    left_on='main_character',
    right_on='name',
    how='left'
)
```

#### SQL (SQLite3)

```python exec
id: 05-pandas-sql-cheat-sheet-51
# Inner join books with characters
pd.read_sql("""
SELECT b.*, c.*
FROM books b
INNER JOIN characters c ON b.main_character = c.name
""", conn)
```

```python exec
id: 05-pandas-sql-cheat-sheet-52
# Left join - keep all books
pd.read_sql("""
SELECT b.*, c.*
FROM books b
LEFT JOIN characters c ON b.main_character = c.name
""", conn)
```

## Summary

This notebook has demonstrated key operations in both pandas and SQL using a Terry Pratchett Discworld dataset. Here's a quick reference of the equivalents:

| Operation | Pandas | SQL |
|-----------|--------|-----|
| Create data | `pd.DataFrame(data)` | `CREATE TABLE` + `INSERT INTO` |
| Read data | `df.head()`, `df.info()` | `SELECT * FROM table LIMIT 5` |
| Select columns | `df[['col1', 'col2']]` | `SELECT col1, col2 FROM table` |
| Rename columns | `df.rename(columns={'old':'new'})` | Column aliases or create new table |
| Add columns | `df['new_col'] = value` | `ALTER TABLE ADD COLUMN` |
| Add rows | `pd.concat([df, new_rows])` | `INSERT INTO table VALUES` |
| Update values | `df.loc[condition, 'col'] = value` | `UPDATE table SET col = value WHERE condition` |
| Filter rows | `df[df['col'] > value]` | `SELECT * FROM table WHERE col > value` |
| Sort data | `df.sort_values('col')` | `SELECT * FROM table ORDER BY col` |
| Aggregate | `df.groupby('col').agg(functions)` | `SELECT col, AGG(col2) FROM table GROUP BY col` |
| Join tables | `pd.merge(df1, df2, on='key')` | `SELECT * FROM table1 JOIN table2 ON key` |

Both pandas and SQL are powerful tools for data manipulation. Pandas offers more interactive and intuitive syntax with built-in analysis capabilities, while SQL excels at working with large datasets and database operations.
