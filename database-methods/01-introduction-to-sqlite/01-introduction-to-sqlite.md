---
title: "Introduction to SQLite with Jupyter Notebook"
slug: 01-introduction-to-sqlite
course: database-methods
course_title: "Database Methods"
series: core
series_title: "Notebooks"
version: 2026.09.06.1
---

# Introduction to SQLite with Jupyter Notebook

Welcome! In this tutorial, we'll explore the basics of working with databases using SQLite. SQLite is a lightweight database that's perfect for learning, and we'll be using some prehistoric creatures as our example data.

By the end of this tutorial, we'll be able to:
- Create database tables
- Insert and query data
- Filter and sort our results
- Add our own data using an interactive form

Let's get started!

## Setting up

SQLite comes with Python, so there is nothing to install. The cell below opens (or creates) a database file and defines one small function, `run_sql`, that sends a piece of SQL to it. A query that asks for data comes back as a table; anything else is carried out and saved.

```python exec
id: 01-introduction-to-sqlite-1
import sqlite3
import pandas as pd

connection = sqlite3.connect('prehistoric_creatures.db')

def run_sql(query):
    """Run one piece of SQL against our database.
    A SELECT comes back as a table you can read; anything else (CREATE, INSERT, ...) is carried out and saved."""
    if query.strip().lower().startswith('select'):
        return pd.read_sql_query(query, connection)
    connection.executescript(query)
    connection.commit()

print('Connected to prehistoric_creatures.db')
```

## Creating Our First Table: Dinosaurs

Now let's create our first table to store information about dinosaurs. We write the SQL inside `run_sql(""" ... """)`, so that the whole statement can run over several lines.

Our dinosaur table will have:
- An ID number (primary key)
- Name
- Diet (herbivore, carnivore, or omnivore)
- Length in meters
- Period when they lived

```python exec
id: 01-introduction-to-sqlite-2
run_sql("""
CREATE TABLE IF NOT EXISTS dinosaurs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    diet TEXT NOT NULL,
    length_meters REAL,
    period TEXT
);
""")
```

## Adding Dinosaur Data

Let's populate our dinosaurs table with some interesting specimens. We'll add several different types to give us good data to work with.

```python exec
id: 01-introduction-to-sqlite-3
run_sql("""
INSERT INTO dinosaurs (name, diet, length_meters, period) VALUES
    ('Tyrannosaurus Rex', 'Carnivore', 12.3, 'Late Cretaceous'),
    ('Triceratops', 'Herbivore', 9.0, 'Late Cretaceous'),
    ('Velociraptor', 'Carnivore', 2.0, 'Late Cretaceous'),
    ('Brachiosaurus', 'Herbivore', 25.0, 'Late Jurassic'),
    ('Stegosaurus', 'Herbivore', 9.0, 'Late Jurassic'),
    ('Allosaurus', 'Carnivore', 9.7, 'Late Jurassic'),
    ('Diplodocus', 'Herbivore', 27.0, 'Late Jurassic'),
    ('Ankylosaurus', 'Herbivore', 6.25, 'Late Cretaceous'),
    ('Spinosaurus', 'Carnivore', 15.0, 'Cretaceous'),
    ('Parasaurolophus', 'Herbivore', 10.0, 'Late Cretaceous');
""")
```

## Creating Our Second Table: Sea Creatures

Now let's create a second table for prehistoric marine life. These creatures lived in the oceans alongside the dinosaurs.

```python exec
id: 01-introduction-to-sqlite-4
run_sql("""
CREATE TABLE IF NOT EXISTS sea_creatures (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    diet TEXT NOT NULL,
    length_meters REAL,
    period TEXT
);
""")
```

## Adding Sea Creature Data

Let's add some fascinating marine reptiles and other sea-dwelling creatures from prehistoric times.

```python exec
id: 01-introduction-to-sqlite-5
run_sql("""
INSERT INTO sea_creatures (name, diet, length_meters, period) VALUES
    ('Mosasaurus', 'Carnivore', 17.0, 'Late Cretaceous'),
    ('Plesiosaurus', 'Carnivore', 3.5, 'Early Jurassic'),
    ('Ichthyosaurus', 'Carnivore', 2.0, 'Early Jurassic'),
    ('Elasmosaurus', 'Carnivore', 14.0, 'Late Cretaceous'),
    ('Liopleurodon', 'Carnivore', 7.0, 'Middle Jurassic'),
    ('Kronosaurus', 'Carnivore', 10.0, 'Early Cretaceous'),
    ('Tylosaurus', 'Carnivore', 14.0, 'Late Cretaceous'),
    ('Shonisaurus', 'Carnivore', 15.0, 'Late Triassic');
""")
```

## Querying Our Data

Now that we have data in our tables, let's learn how to retrieve it! We'll start with simple queries and gradually make them more complex.

### Viewing All Dinosaurs

The SELECT statement is how we retrieve data. Let's look at all our dinosaurs:

```python exec
id: 01-introduction-to-sqlite-6
run_sql("""
SELECT * FROM dinosaurs;
""")
```

### Viewing All Sea Creatures

Let's do the same for our marine friends:

```python exec
id: 01-introduction-to-sqlite-7
run_sql("""
SELECT * FROM sea_creatures;
""")
```

## Filtering Data with WHERE

Often we don't want ALL the data - we want to find specific records. Let's use the WHERE clause to filter our results.

### Finding Carnivorous Dinosaurs

Let's find all the meat-eating dinosaurs:

```python exec
id: 01-introduction-to-sqlite-8
run_sql("""
SELECT name, length_meters, period
FROM dinosaurs
WHERE diet = 'Carnivore';
""")
```

### Finding Large Creatures

Let's find all dinosaurs that were longer than 10 meters:

```python exec
id: 01-introduction-to-sqlite-9
run_sql("""
SELECT name, length_meters, diet
FROM dinosaurs
WHERE length_meters > 10
ORDER BY length_meters DESC;
""")
```

### Finding Creatures from Specific Time Periods

Let's see which creatures lived during the Late Cretaceous period:

```python exec
id: 01-introduction-to-sqlite-10
run_sql("""
SELECT name, 'Dinosaur' as type, diet, length_meters
FROM dinosaurs
WHERE period = 'Late Cretaceous'
UNION
SELECT name, 'Sea Creature' as type, diet, length_meters
FROM sea_creatures
WHERE period = 'Late Cretaceous'
ORDER BY length_meters DESC;
""")
```

## Aggregate Functions

SQL has powerful functions that let us calculate statistics about our data. Let's explore some of these.

### Counting Records

How many dinosaurs do we have in our database?

```python exec
id: 01-introduction-to-sqlite-11
run_sql("""
SELECT COUNT(*) as total_dinosaurs FROM dinosaurs;
""")
```

### Average, Minimum, and Maximum

Let's calculate some statistics about dinosaur sizes:

```python exec
id: 01-introduction-to-sqlite-12
run_sql("""
SELECT
    AVG(length_meters) as average_length,
    MIN(length_meters) as smallest,
    MAX(length_meters) as largest
FROM dinosaurs;
""")
```

### Grouping Data

We can group our results by categories. Let's count how many dinosaurs of each diet type we have:

```python exec
id: 01-introduction-to-sqlite-13
run_sql("""
SELECT diet, COUNT(*) as count, AVG(length_meters) as average_length
FROM dinosaurs
GROUP BY diet;
""")
```

## Comparing Land and Sea

Let's compare the average sizes of our dinosaurs versus sea creatures:

```python exec
id: 01-introduction-to-sqlite-14
run_sql("""
SELECT 'Dinosaurs' as creature_type,
       COUNT(*) as count,
       AVG(length_meters) as avg_length,
       MAX(length_meters) as max_length
FROM dinosaurs
UNION
SELECT 'Sea Creatures' as creature_type,
       COUNT(*) as count,
       AVG(length_meters) as avg_length,
       MAX(length_meters) as max_length
FROM sea_creatures;
""")
```

## Interactive Form: Add Your Own Creature!

Now let's create an interactive form that allows us to add our own creatures to either table. This is a great way to practice inserting data into a database.

```python exec
id: 01-introduction-to-sqlite-15
# First, let's import the widgets we'll need
import ipywidgets as widgets
from IPython.display import display, clear_output
import sqlite3

# Create a connection to our database
conn = sqlite3.connect('prehistoric_creatures.db')
cursor = conn.cursor()

# Create the form widgets
creature_type = widgets.Dropdown(
    options=['Dinosaur', 'Sea Creature'],
    value='Dinosaur',
    description='Type:'
)

name_input = widgets.Text(
    value='',
    placeholder='Enter creature name',
    description='Name:'
)

diet_input = widgets.Dropdown(
    options=['Carnivore', 'Herbivore', 'Omnivore'],
    value='Carnivore',
    description='Diet:'
)

length_input = widgets.FloatText(
    value=5.0,
    description='Length (m):'
)

period_input = widgets.Text(
    value='',
    placeholder='e.g., Late Cretaceous',
    description='Period:'
)

submit_button = widgets.Button(
    description='Add Creature',
    button_style='success'
)

output_area = widgets.Output()

def add_creature(b):
    with output_area:
        clear_output()

        # Get the values from the form
        name = name_input.value
        diet = diet_input.value
        length = length_input.value
        period = period_input.value
        table = 'dinosaurs' if creature_type.value == 'Dinosaur' else 'sea_creatures'

        # Validate input
        if not name or not period:
            print("Please fill in all fields!")
            return

        try:
            # Insert the new creature
            cursor.execute(f"""
                INSERT INTO {table} (name, diet, length_meters, period)
                VALUES (?, ?, ?, ?)
            """, (name, diet, length, period))
            conn.commit()

            print(f"Successfully added {name} to the {table} table!")

            # Show the updated table
            cursor.execute(f"SELECT * FROM {table} ORDER BY id DESC LIMIT 5")
            results = cursor.fetchall()
            print(f"\nLast 5 entries in {table}:")
            for row in results:
                print(f"  {row[1]} - {row[2]}, {row[3]}m, {row[4]}")

            # Clear the form
            name_input.value = ''
            period_input.value = ''

        except Exception as e:
            print(f"Error adding creature: {e}")

submit_button.on_click(add_creature)

# Display the form
print("Add a New Creature to Our Database")
print("===================================\n")
display(creature_type, name_input, diet_input, length_input, period_input, submit_button, output_area)
```

## Viewing Your Additions

After adding some creatures with the form above, we can run these queries to see our complete updated tables:

```python exec
id: 01-introduction-to-sqlite-16
run_sql("""
SELECT * FROM dinosaurs ORDER BY id DESC LIMIT 10;
""")
```

```python exec
id: 01-introduction-to-sqlite-17
run_sql("""
SELECT * FROM sea_creatures ORDER BY id DESC LIMIT 10;
""")
```

## Practice Exercises

Now that we've learned the basics, let's try some practice queries. Try writing SQL to answer these questions:

1. Find all herbivore dinosaurs from the Late Jurassic period
2. Find the three largest sea creatures
3. Count how many creatures (both dinosaurs and sea creatures) lived in each period
4. Find all creatures (land or sea) that are between 5 and 10 meters long

Use the empty cells below to write your queries:

```python exec
id: 01-introduction-to-sqlite-18
run_sql("""
-- Your query here:  1: Your query here
""")
```

```python exec
id: 01-introduction-to-sqlite-19
run_sql("""
-- Your query here:  2: Your query here
""")
```

```python exec
id: 01-introduction-to-sqlite-20
run_sql("""
-- Your query here:  3: Your query here
""")
```

```python exec
id: 01-introduction-to-sqlite-21
run_sql("""
-- Your query here:  4: Your query here
""")
```

## Summary


- Open a SQLite database from Python with nothing to install
- Create tables with appropriate data types
- Insert data into our tables
- Query data using SELECT statements
- Filter results with WHERE clauses
- Sort results with ORDER BY
- Use aggregate functions like COUNT, AVG, MIN, and MAX
- Group data with GROUP BY
- Combine results from multiple tables with UNION
- Create an interactive form to add data

These are the fundamental building blocks of working with databases. As we continue learning, we'll discover more advanced topics like joins, subqueries, and database optimization.

Feel free to experiment more with the database - try adding more creatures, writing different queries, or even creating new tables!

## Clean Up (Optional)

If we want to start fresh, we can drop our tables with these commands:

```python exec
id: 01-introduction-to-sqlite-22
# Uncomment these lines if you want to delete the tables and start over
# run_sql('DROP TABLE IF EXISTS dinosaurs;')
# run_sql('DROP TABLE IF EXISTS sea_creatures;')
```

## Looking back

Before leaving this page, a sentence on each. What you write stays on this device.

```reflect
- Something you expected before running a cell that turned out differently
- The one idea from this page you could explain to someone else now
- Something you would change or try next, if there were time
- A question this page raised for you that it did not answer. Bring it to the next session; these questions are where the next session starts.
```
