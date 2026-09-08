---
title: "Pandas vs SQL: A Beginner's Guide"
slug: 04-pandas-versus-sql
course: database-methods
course_title: "Database Methods"
series: core
series_title: "Notebooks"
version: 2026.09.06.1
---

# Pandas vs SQL: A Beginner's Guide

This notebook introduces basic data manipulation in pandas and compares it with equivalent SQL commands. We'll use a dataset from "Our World in Data" on COVID-19 vaccinations to demonstrate these concepts.

## Setup and Data Loading

```python exec
id: 04-pandas-versus-sql-1
# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load data directly from Our World in Data
df = pd.read_csv("https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/vaccinations/vaccinations.csv", storage_options = {'User-Agent': 'Our World In Data data fetch/1.0'})
# Display the first few rows

print(f"Dataset shape: {df.shape}")
df.head()
```

```python exec
id: 04-pandas-versus-sql-2
df.info()
```

## Example 1: Selecting Columns

Let's start with the basic operation of selecting specific columns from our dataset.

```python exec
id: 04-pandas-versus-sql-3
# Pandas: Select specific columns
selected_columns = df[['location', 'date', 'total_vaccinations']]
display(selected_columns.head())
selected_columns.tail()
```

**Equivalent SQL:**
```sql
SELECT location, date, total_vaccinations
FROM vaccinations
LIMIT 5;
```

**Key differences:**
- In pandas, we use square brackets `[]` with a list of column names
- In pandas, limiting rows is a separate operation (using `.head()` or slicing)
- Pandas operations can be chained together, making complex queries more readable

## Example 2: Filtering Rows

Now let's filter our data to look at vaccinations in a specific country.

```python exec
id: 04-pandas-versus-sql-4
# Pandas: Filter rows
us_data = df[df['location'] == 'United States']
print(f"Number of rows: {len(us_data)}")
us_data.head()
```

**Equivalent SQL:**
```sql
SELECT *
FROM vaccinations
WHERE location = 'United States'
LIMIT 5;
```

**Key differences:**
- In pandas, we use boolean expressions inside square brackets
- The condition syntax is closer to Python: `df['column'] == value` instead of SQL's `column = value`
- We can chain multiple conditions using `&` (AND), `|` (OR), and `~` (NOT) operators

## Example 3: Aggregation and Grouping

Let's group the data by country and calculate the maximum vaccination rate.

```python exec
id: 04-pandas-versus-sql-5
# Pandas: Group by and aggregation
country_stats = df.groupby('location').agg({
    'total_vaccinations': 'max',
    'people_fully_vaccinated': 'max'
}).reset_index()

# Sort by total vaccinations in descending order
country_stats = country_stats.sort_values('total_vaccinations', ascending=False)

# Display top 10 countries
country_stats.head(10)
```

**Equivalent SQL:**
```sql
SELECT
    location,
    MAX(total_vaccinations) as total_vaccinations,
    MAX(people_fully_vaccinated) as people_fully_vaccinated
FROM vaccinations
GROUP BY location
ORDER BY total_vaccinations DESC
LIMIT 10;
```

**Key differences:**
- Pandas uses the `.groupby()` and `.agg()` methods with a dictionary of column-to-aggregation mappings
- `reset_index()` is needed to convert the grouped results back to a regular DataFrame
- Sorting is done with `.sort_values()` rather than `ORDER BY`

## Example 4: Creating New Columns

Let's create a new column calculating the percentage of population fully vaccinated.

```python exec
id: 04-pandas-versus-sql-6
# Create a copy to avoid warnings
df_copy = df.copy()
# Suppose we add population column in our dataframe:
#total people vaccinated / vaccinations per hundred gives us the population
df_copy['population'] = df_copy['people_fully_vaccinated'] / df_copy['people_vaccinated_per_hundred']
# Pandas: Create a new calculated column
df_copy['vaccination_percentage'] = (df_copy['people_fully_vaccinated'] / df_copy['population']) * 100

# Select relevant columns and filter out rows with missing values
result = df_copy[['location', 'date', 'people_fully_vaccinated', 'population', 'vaccination_percentage']]
result = result.dropna(subset=['vaccination_percentage'])

# Display a sample of the data
result.sample(5)
```

**Equivalent SQL:**
```sql
SELECT
    location,
    date,
    people_fully_vaccinated,
    population,
    (people_fully_vaccinated / population) * 100 as vaccination_percentage
FROM vaccinations
WHERE people_fully_vaccinated IS NOT NULL AND population IS NOT NULL
ORDER BY RANDOM()
LIMIT 5;
```

**Key differences:**
- In pandas, creating new columns is as simple as assigning values to a new column name
- Math operations on columns are more intuitive in pandas (similar to numpy)
- `.dropna()` is a convenient method to handle missing values
- `.sample()` easily selects random rows (equivalent to `ORDER BY RANDOM()` in SQL)

## Example 5: Time Series Analysis

Let's analyze vaccination progress over time for a few selected countries.

```python exec
id: 04-pandas-versus-sql-7
# Pandas: Time series filtering and visualization
# Filter data for selected countries and convert dates
countries = ['United States', 'United Kingdom', 'Israel', 'Canada']
filtered_data = df[df['location'].isin(countries)]
filtered_data['date'] = pd.to_datetime(filtered_data['date'])

# Create a pivot table for easy plotting
vaccination_rates = filtered_data.pivot(index='date', columns='location', values='people_vaccinated_per_hundred')

# Plot the data
plt.figure(figsize=(12, 6))
vaccination_rates.plot(figsize=(12, 6))
plt.title('Vaccination Rates Over Time')
plt.xlabel('Date')
plt.ylabel('People Vaccinated per 100 Population')
plt.grid(True, alpha=0.3)
plt.legend(title='Country')
plt.show()

# Display most recent values
latest_data = filtered_data.sort_values('date').groupby('location').last()
latest_data[['date', 'people_vaccinated_per_hundred']]
```

**Equivalent SQL (simplified, without visualization):**
```sql
WITH latest_values AS (
    SELECT
        location,
        date,
        people_vaccinated_per_hundred,
        ROW_NUMBER() OVER (PARTITION BY location ORDER BY date DESC) as row_num
    FROM vaccinations
    WHERE location IN ('United States', 'United Kingdom', 'Israel', 'Canada')
)
SELECT location, date, people_vaccinated_per_hundred
FROM latest_values
WHERE row_num = 1
ORDER BY location;
```

**Key differences:**
- Pandas really shines for time series analysis with built-in datetime handling
- The `.isin()` method is a clean way to filter for multiple values
- `.pivot()` makes reshaping data for analysis and visualization much easier
- Built-in plotting capabilities make visualization simple
- Getting the latest values per group is more intuitive than SQL's window functions

## Summary: Pandas vs SQL

### When to use pandas:
- Interactive data exploration and analysis
- Complex data transformations
- Statistical analysis and machine learning
- Visualization and reporting
- When working with moderate-sized datasets that fit in memory

### When to use SQL:
- Working with very large datasets
- When data is already in a database
- For production data pipelines
- When multiple users need to access the same data
- For transactions and data integrity requirements

### Key pandas advantages over SQL:
1. More intuitive syntax for data scientists familiar with Python
2. Richer set of built-in functions and methods
3. Seamless integration with visualization libraries
4. Better support for complex data transformations
5. Full programming language capabilities (loops, conditions, functions)

In practice, data professionals often use both: SQL for initial data extraction and pandas for analysis and visualization.

## Looking back

Before leaving this page, a sentence on each. What you write stays on this device.

```reflect
- Something you expected before running a cell that turned out differently
- The one idea from this page you could explain to someone else now
- Something you would change or try next, if there were time
- A question this page raised for you that it did not answer. Bring it to the next session; these questions are where the next session starts.
```
