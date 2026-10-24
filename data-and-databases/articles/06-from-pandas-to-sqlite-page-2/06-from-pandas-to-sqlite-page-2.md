---
title: "06-from-pandas-to-sqlite-page-2 (2 of 2)"
slug: 06-from-pandas-to-sqlite-page-2
course: database-methods
course_title: "Database Methods"
series: core
series_title: "Notebooks"
version: 2026.09.06.1
---

Before starting this page, run the cell below. It repeats the imports and definitions from the earlier pages that this page uses.

```python exec
id: 06-from-pandas-to-sqlite-page-2-setup
import sqlite3
import pandas as pd
import numpy as np

import sqlite3
import pandas as pd
import numpy as np

# Environment detection for Colab compatibility
try:
    import google.colab
    IN_COLAB = True
    print("Running in Google Colab")
except ImportError:
    IN_COLAB = False
    print("Running in standard Jupyter environment")

# Create a connection to a database file
# If the file doesn't exist, SQLite creates it
conn = sqlite3.connect('college.db')

print("Connected to college.db")
print(f"Connection object: {conn}")

# The cursor object executes SQL commands
cursor = conn.cursor()

print("Cursor created - ready to execute SQL")

# Check what tables exist in the database
cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
tables = cursor.fetchall()

print("Tables in database:")
for table in tables:
    print(f"  - {table[0]}")
```

## The Pandas Bridge: read_sql() and to_sql()

Pandas provides convenient functions to move data between DataFrames and databases. This lets you use whichever tool is more appropriate for each task.

### Reading from Database to DataFrame

```python exec
id: 06-from-pandas-to-sqlite-page-2-1
# Read entire table into a DataFrame
students_df = pd.read_sql('SELECT * FROM students', conn)
students_df
```

```python exec
id: 06-from-pandas-to-sqlite-page-2-2
# Read with a filter - the filtering happens in SQL
computing_df = pd.read_sql("SELECT * FROM students WHERE programme = 'Computing'", conn)
computing_df
```

```python exec
id: 06-from-pandas-to-sqlite-page-2-3
# Read modules
modules_df = pd.read_sql('SELECT * FROM modules', conn)
modules_df
```

Once data is in a DataFrame, you can use all the pandas techniques you've learned: filtering, calculating new columns, visualisation, and so on.

```python exec
id: 06-from-pandas-to-sqlite-page-2-4
# Work with the DataFrame using pandas
print(f"Average age: {students_df['age'].mean():.1f}")
print(f"\nProgrammes: {students_df['programme'].unique()}")
print(f"\nStudents per programme:")
print(students_df['programme'].value_counts())
```

### Writing from DataFrame to Database

```python exec
id: 06-from-pandas-to-sqlite-page-2-5
# Create a new DataFrame
new_students = pd.DataFrame({
    'name': ['James Wong', 'Sofia Garcia', 'Erik Larsson'],
    'age': [23, 20, 22],
    'programme': ['Design', 'Computing', 'Business']
})

new_students
```

```python exec
id: 06-from-pandas-to-sqlite-page-2-6
# Write DataFrame to database
# if_exists options: 'fail', 'replace', 'append'
new_students.to_sql('students', conn, if_exists='append', index=False)

print("Added new students to database")
```

The `if_exists` parameter controls what happens if the table already exists:
- `'fail'`: Raise an error (default)
- `'replace'`: Drop the existing table and create a new one
- `'append'`: Add the new rows to the existing table

The `index=False` parameter prevents pandas from writing the DataFrame's index as a column in the database.

```python exec
id: 06-from-pandas-to-sqlite-page-2-7
# Verify the addition
all_students = pd.read_sql('SELECT * FROM students', conn)
print(f"Total students now: {len(all_students)}")
all_students
```

### Creating a New Table from a DataFrame

```python exec
id: 06-from-pandas-to-sqlite-page-2-8
# Create a DataFrame with lecturers
lecturers = pd.DataFrame({
    'name': ['Dr. Walsh', 'Ms. Patel', 'Mr. O Sullivan', 'Dr. Ryan'],
    'department': ['Computing', 'Computing', 'Computing', 'Business'],
    'years_experience': [15, 8, 12, 20]
})

# Write to a new table
lecturers.to_sql('lecturers', conn, if_exists='replace', index=False)

print("Created lecturers table")
```

```python exec
id: 06-from-pandas-to-sqlite-page-2-9
# Check tables in database
tables = pd.read_sql("SELECT name FROM sqlite_master WHERE type='table'", conn)
print("Tables in database:")
for t in tables['name']:
    print(f"  - {t}")
```

## Putting It Together: A Complete Workflow

Let's walk through a complete example that demonstrates the typical workflow of working with databases and pandas together.

```python exec
id: 06-from-pandas-to-sqlite-page-2-10
# Create a fresh database for this example
demo_conn = sqlite3.connect('bookshop.db')

# Create a books DataFrame
books = pd.DataFrame({
    'title': ['The Great Gatsby', '1984', 'Pride and Prejudice', 'To Kill a Mockingbird', 'The Catcher in the Rye'],
    'author': ['F. Scott Fitzgerald', 'George Orwell', 'Jane Austen', 'Harper Lee', 'J.D. Salinger'],
    'year': [1925, 1949, 1813, 1960, 1951],
    'price': [12.99, 9.99, 8.99, 14.99, 11.99],
    'in_stock': [True, True, False, True, True]
})

# Save to database
books.to_sql('books', demo_conn, if_exists='replace', index=False)

print("Created bookshop database with books table")
books
```

```python exec
id: 06-from-pandas-to-sqlite-page-2-11
# Query: Books priced under 12 pounds
affordable = pd.read_sql('SELECT * FROM books WHERE price < 12', demo_conn)
print("Affordable books (under 12):")
affordable
```

```python exec
id: 06-from-pandas-to-sqlite-page-2-12
# Query: Books published before 1950
classics = pd.read_sql('SELECT title, author, year FROM books WHERE year < 1950', demo_conn)
print("Pre-1950 classics:")
classics
```

```python exec
id: 06-from-pandas-to-sqlite-page-2-13
# Add new books using SQL directly
cursor = demo_conn.cursor()
cursor.execute('''
    INSERT INTO books (title, author, year, price, in_stock)
    VALUES
        ('Brave New World', 'Aldous Huxley', 1932, 10.99, 1),
        ('The Hobbit', 'J.R.R. Tolkien', 1937, 13.99, 1)
''')
demo_conn.commit()

print("Added two more books")
```

```python exec
id: 06-from-pandas-to-sqlite-page-2-14
# Read updated table
all_books = pd.read_sql('SELECT * FROM books', demo_conn)
print(f"Total books: {len(all_books)}")
all_books
```

```python exec
id: 06-from-pandas-to-sqlite-page-2-15
# Delete a book
cursor.execute("DELETE FROM books WHERE title = 'The Catcher in the Rye'")
demo_conn.commit()

# Verify
remaining = pd.read_sql('SELECT title FROM books', demo_conn)
print("Remaining books:")
for title in remaining['title']:
    print(f"  - {title}")
```

```python exec
id: 06-from-pandas-to-sqlite-page-2-16
# Close the demo connection
demo_conn.close()
print("Closed bookshop database connection")
```

## Closing Connections

When you're finished with a database, close the connection to release the file. This is especially important if other programs might need to access the database.

```python exec
id: 06-from-pandas-to-sqlite-page-2-17
# Close our main connection
conn.close()
print("Closed college.db connection")
```

You can also use Python's `with` statement to automatically close connections:

```python exec
id: 06-from-pandas-to-sqlite-page-2-18
# Using 'with' for automatic cleanup
with sqlite3.connect('college.db') as conn:
    df = pd.read_sql('SELECT * FROM students', conn)
    print(f"Read {len(df)} students")

# Connection is automatically closed when the 'with' block ends
print("Connection closed automatically")
```

## Practice Exercises

**Exercise 1:** Create a new database called `music.db`. Create a table called `songs` with columns for title (TEXT), artist (TEXT), year (INTEGER), and duration_seconds (INTEGER). Insert at least 4 songs.

```python exec
id: 06-from-pandas-to-sqlite-page-2-19
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
# Your code here
```

**Exercise 2:** Write a query to select all songs from your database that are longer than 3 minutes (180 seconds). Display the results.

```python exec
id: 06-from-pandas-to-sqlite-page-2-20
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
# Your code here
```

**Exercise 3:** Create a DataFrame with information about 3 albums (title, artist, year, num_tracks). Use `to_sql()` to save it to a new table called `albums` in your music database.

```python exec
id: 06-from-pandas-to-sqlite-page-2-21
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
# Your code here
```

**Exercise 4:** Delete one song from your songs table, then use `read_sql()` to load the remaining songs into a DataFrame and display them.

```python exec
id: 06-from-pandas-to-sqlite-page-2-22
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
# Your code here
```

## Summary

This notebook covered the fundamentals of working with SQLite databases:

**Connecting:** Use `sqlite3.connect('filename.db')` to create or open a database.

**Creating tables:** Use `CREATE TABLE` with column names and data types (TEXT, INTEGER, REAL).

**Inserting data:** Use `INSERT INTO` with column names and values.

**Querying:** Use `SELECT` to retrieve data, with `WHERE` to filter rows.

**Deleting:** Use `DELETE FROM` with a `WHERE` clause to remove specific rows.

**Pandas bridge:** Use `pd.read_sql()` to load database data into DataFrames, and `df.to_sql()` to write DataFrames to database tables.

**Cleanup:** Always close connections with `conn.close()` or use the `with` statement.

## Bibliography

SQLite documentation. https://www.sqlite.org/docs.html

Python sqlite3 module documentation. https://docs.python.org/3/library/sqlite3.html

pandas documentation: SQL queries. https://pandas.pydata.org/docs/reference/api/pandas.read_sql.html

McKinney, W. (2022). *Python for Data Analysis* (3rd ed.). O'Reilly Media. Chapter 6 covers database interaction. https://wesmckinney.com/book/

Real Python: Data Management With Python, SQLite, and SQLAlchemy. https://realpython.com/python-sqlite-sqlalchemy/

## Cleanup

```python exec
id: 06-from-pandas-to-sqlite-page-2-23
# Optional: Remove database files created during this tutorial
import os

files_to_remove = ['college.db', 'bookshop.db', 'music.db']

# Uncomment to clean up:
# for f in files_to_remove:
#     if os.path.exists(f):
#         os.remove(f)
#         print(f"Removed {f}")
```

## Looking back

Before leaving this page, a sentence on each. What you write stays on this device.

```reflect
- Something you expected before running a cell that turned out differently
- The one idea from this page you could explain to someone else now
- Something you would change or try next, if there were time
- A question this page raised for you that it did not answer. Bring it to the next session; these questions are where the next session starts.
```
