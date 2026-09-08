---
title: "From Pandas to SQLite: Working with Databases (1 of 2)"
slug: 06-from-pandas-to-sqlite-page-1
course: database-methods
course_title: "Database Methods"
series: core
series_title: "Notebooks"
version: 2026.09.06.1
---

# From Pandas to SQLite: Working with Databases

This notebook introduces SQLite databases and shows how pandas can serve as a bridge between Python and SQL. SQLite is a lightweight database system that stores everything in a single file, requiring no separate server installation. It's built into Python, making it ideal for learning database concepts and for projects that don't require a full database server.

By the end of this notebook, you will understand how to create and connect to SQLite databases, create tables with appropriate data types, insert data, query data with filtering conditions, delete records, and move data between pandas DataFrames and database tables.

## Why Databases?

You might wonder why we need databases when CSV and Excel files work well for storing data. Databases offer several advantages:

**Structured queries:** SQL provides a standardised way to ask questions about your data. Instead of writing Python code to filter a DataFrame, you can write a query that describes what you want.

**Data integrity:** Databases can enforce rules about what data is allowed, preventing errors before they happen.

**Multiple tables:** Databases naturally handle related tables. A school database might have separate tables for students, courses, and enrolments, all linked together.

**Persistence:** The database file exists independently of your Python session. You can close your notebook, reopen it later, and the data is still there.

For this course, we use SQLite because it requires no setup beyond importing Python's built-in sqlite3 module.

```python exec
id: 06-from-pandas-to-sqlite-page-1-1
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
```

## Creating and Connecting to a Database

SQLite stores an entire database in a single file. When you connect to a database file that doesn't exist, SQLite creates it for you.

```python exec
id: 06-from-pandas-to-sqlite-page-1-2
# Create a connection to a database file
# If the file doesn't exist, SQLite creates it
conn = sqlite3.connect('college.db')

print("Connected to college.db")
print(f"Connection object: {conn}")
```

The connection object (`conn`) is your link to the database. You'll use it for all database operations. When you're finished working with the database, you should close the connection to release the file.

```python exec
id: 06-from-pandas-to-sqlite-page-1-3
# The cursor object executes SQL commands
cursor = conn.cursor()

print("Cursor created - ready to execute SQL")
```

## SQL Data Types

When creating tables, you specify what type of data each column can hold. SQLite uses these main data types:

| Type | Description | Examples |
|------|-------------|----------|
| TEXT | Text strings | 'Dublin', 'Computing', 'Dr. Smith' |
| INTEGER | Whole numbers | 42, -7, 2024 |
| REAL | Decimal numbers | 3.14, 98.6, -0.5 |
| BLOB | Binary data | Images, files (rarely used directly) |
| NULL | Missing/unknown | Represents absence of data |

Choosing the right type helps ensure data quality. If a column should only contain numbers, declaring it as INTEGER prevents accidentally storing text there.

## Creating Tables

Tables are created using the `CREATE TABLE` statement. You specify the table name and define each column with its name and data type.

```python exec
id: 06-from-pandas-to-sqlite-page-1-4
# Create a students table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        name TEXT,
        age INTEGER,
        programme TEXT
    )
''')

print("Created students table")
```

The `IF NOT EXISTS` clause is helpful during development. Without it, trying to create a table that already exists would cause an error. With this clause, SQLite simply skips the creation if the table is already there.

```python exec
id: 06-from-pandas-to-sqlite-page-1-5
# Create a modules table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS modules (
        module_name TEXT,
        hours_per_week INTEGER,
        lecturer TEXT
    )
''')

print("Created modules table")
```

```python exec
id: 06-from-pandas-to-sqlite-page-1-6
# Check what tables exist in the database
cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
tables = cursor.fetchall()

print("Tables in database:")
for table in tables:
    print(f"  - {table[0]}")
```

## Inserting Data

The `INSERT INTO` statement adds rows to a table. You specify which columns you're filling and provide the values.

```python exec
id: 06-from-pandas-to-sqlite-page-1-7
# Insert a single row
cursor.execute('''
    INSERT INTO students (name, age, programme)
    VALUES ('Maya Chen', 19, 'Computing')
''')

print("Inserted one student")
```

```python exec
id: 06-from-pandas-to-sqlite-page-1-8
# Insert multiple rows at once
cursor.execute('''
    INSERT INTO students (name, age, programme)
    VALUES
        ('Fatima Al-Rahman', 22, 'Business'),
        ('Kofi Mensah', 20, 'Design'),
        ('Aoife Kelly', 21, 'Computing'),
        ('Liam Murphy', 19, 'Business')
''')

print("Inserted four more students")
```

```python exec
id: 06-from-pandas-to-sqlite-page-1-9
# Insert data into modules table
cursor.execute('''
    INSERT INTO modules (module_name, hours_per_week, lecturer)
    VALUES
        ('Database Methods', 4, 'Dr. Walsh'),
        ('Programming Fundamentals', 5, 'Ms. Patel'),
        ('Web Development', 6, 'Mr. O Sullivan'),
        ('Communications', 3, 'Dr. Ryan')
''')

print("Inserted modules")
```

```python exec
id: 06-from-pandas-to-sqlite-page-1-10
# Commit the changes to save them to the file
conn.commit()

print("Changes committed to database")
```

The `commit()` call is important. SQLite uses transactions, which means changes aren't permanently saved until you commit them. This allows you to make multiple changes and then either save them all together or undo them if something goes wrong.

## Querying Data with SELECT

The `SELECT` statement retrieves data from a table. The simplest form retrieves all columns and all rows.

```python exec
id: 06-from-pandas-to-sqlite-page-1-11
# Select all data from students
cursor.execute('SELECT * FROM students')
results = cursor.fetchall()

print("All students:")
for row in results:
    print(f"  {row}")
```

The asterisk (*) means "all columns". You can also select specific columns by name.

```python exec
id: 06-from-pandas-to-sqlite-page-1-12
# Select specific columns
cursor.execute('SELECT name, programme FROM students')
results = cursor.fetchall()

print("Student names and programmes:")
for row in results:
    print(f"  {row[0]} - {row[1]}")
```

### Filtering with WHERE

The `WHERE` clause filters rows based on conditions. Only rows that satisfy the condition are returned.

```python exec
id: 06-from-pandas-to-sqlite-page-1-13
# Filter: students aged 20 or older
cursor.execute('SELECT * FROM students WHERE age >= 20')
results = cursor.fetchall()

print("Students aged 20 or older:")
for row in results:
    print(f"  {row}")
```

```python exec
id: 06-from-pandas-to-sqlite-page-1-14
# Filter: students in Computing programme
cursor.execute("SELECT * FROM students WHERE programme = 'Computing'")
results = cursor.fetchall()

print("Computing students:")
for row in results:
    print(f"  {row}")
```

```python exec
id: 06-from-pandas-to-sqlite-page-1-15
# Filter: modules with 5 or more hours per week
cursor.execute('SELECT * FROM modules WHERE hours_per_week >= 5')
results = cursor.fetchall()

print("Modules with 5+ hours per week:")
for row in results:
    print(f"  {row}")
```

### Common WHERE Operators

| Operator | Meaning | Example |
|----------|---------|--------|
| = | Equal to | `age = 20` |
| != or <> | Not equal to | `programme != 'Business'` |
| > | Greater than | `hours_per_week > 4` |
| >= | Greater than or equal | `age >= 21` |
| < | Less than | `age < 20` |
| <= | Less than or equal | `hours_per_week <= 3` |
| LIKE | Pattern matching | `name LIKE 'A%'` (starts with A) |

```python exec
id: 06-from-pandas-to-sqlite-page-1-16
# LIKE with wildcards
# % matches any sequence of characters
cursor.execute("SELECT * FROM students WHERE name LIKE 'A%'")
results = cursor.fetchall()

print("Students whose name starts with A:")
for row in results:
    print(f"  {row}")
```

```python exec
id: 06-from-pandas-to-sqlite-page-1-17
# LIKE for contains
cursor.execute("SELECT * FROM modules WHERE lecturer LIKE '%Dr%'")
results = cursor.fetchall()

print("Modules taught by doctors:")
for row in results:
    print(f"  {row}")
```

## Deleting Data

The `DELETE FROM` statement removes rows from a table. Always use a `WHERE` clause to specify which rows to delete, otherwise all rows will be removed.

```python exec
id: 06-from-pandas-to-sqlite-page-1-18
# Check students before deletion
cursor.execute('SELECT * FROM students')
print("Before deletion:")
for row in cursor.fetchall():
    print(f"  {row}")
```

```python exec
id: 06-from-pandas-to-sqlite-page-1-19
# Delete a specific student
cursor.execute("DELETE FROM students WHERE name = 'Maya Chen'")
conn.commit()

print("Deleted Maya Chen")
```

```python exec
id: 06-from-pandas-to-sqlite-page-1-20
# Check students after deletion
cursor.execute('SELECT * FROM students')
print("After deletion:")
for row in cursor.fetchall():
    print(f"  {row}")
```

## Looking back

Before leaving this page, a sentence on each. What you write stays on this device.

```reflect
- Something you expected before running a cell that turned out differently
- The one idea from this page you could explain to someone else now
- Something you would change or try next, if there were time
- A question this page raised for you that it did not answer. Bring it to the next session; these questions are where the next session starts.
```
