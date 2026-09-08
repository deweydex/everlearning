---
title: "Introduction to Pandas and Matplotlib"
slug: 03-pandas-and-matplotlib
course: database-methods
course_title: "Database Methods"
series: core
series_title: "Notebooks"
version: 2026.09.06.1
---

# Introduction to Pandas and Matplotlib

This notebook introduces basic data manipulation with pandas and visualization with matplotlib using real-world data from "Our World in Data".

## 1. Setup and Data Loading

```python exec
id: 03-pandas-and-matplotlib-1
# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Set matplotlib style for better-looking plots
plt.style.use('seaborn-v0_8-whitegrid')

# Ensure plots display within the notebook

# Make plots larger by default
plt.rcParams['figure.figsize'] = [10, 6]
plt.rcParams['figure.dpi'] = 100  # Higher resolution
```

```python exec
id: 03-pandas-and-matplotlib-2
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
# Your code here
```

Let's load data on CO2 emissions from Our World in Data:

```python exec
id: 03-pandas-and-matplotlib-3
# Load CO2 emissions data from Our World in Data
url = "https://raw.githubusercontent.com/owid/co2-data/master/owid-co2-data.csv"
df = pd.read_csv(url)

# Display basic information about the dataset
print(f"Dataset shape: {df.shape} (rows, columns)\n")
print("Column names:")
print(df.columns.tolist()[:10])
print("...and more columns")

# Look at the first few rows
df.head()
```

## 2. Basic Pandas Operations

### 2.1 Data Exploration

```python exec
id: 03-pandas-and-matplotlib-4
# Get summary statistics
df.describe()
```

```python exec
id: 03-pandas-and-matplotlib-5
# Check for missing values in key columns
key_columns = ['country', 'year', 'co2', 'co2_per_capita', 'population']
df[key_columns].isna().sum()
```

### 2.2 Data Filtering

Let's filter the data to focus on recent years and a few major countries:

```python exec
id: 03-pandas-and-matplotlib-6
# Select relevant countries and years
countries = ['World', 'United States', 'China', 'India', 'European Union', 'United Kingdom']
recent_years = df[df['year'] >= 1950]
filtered_df = recent_years[recent_years['country'].isin(countries)]

# Check the result
print(f"Filtered data shape: {filtered_df.shape}")
filtered_df.head()
```

## 3. Basic Matplotlib Visualizations

### 3.1 Line Plot: CO2 Emissions Over Time

```python exec
id: 03-pandas-and-matplotlib-7
# Create a line plot for CO2 emissions over time by country
plt.figure(figsize=(12, 7))

# Loop through countries and plot each one
for country in countries:
    country_data = filtered_df[filtered_df['country'] == country]
    plt.plot(country_data['year'], country_data['co2'], label=country, linewidth=2)

# Add plot elements
plt.title('CO2 Emissions Over Time (1950-Present)', fontsize=16)
plt.xlabel('TwH', fontsize=12)

plt.ylabel('CO2 Emissions (million tonnes)', fontsize=12)
plt.legend(fontsize=12)
plt.grid(True, alpha=0.3)

# Show the plot
plt.tight_layout()
plt.show()
```

### 3.2 Bar Chart: CO2 Emissions per Capita (2019)

```python exec
id: 03-pandas-and-matplotlib-8
# Filter for the latest year with good data coverage (typically 2019)
latest_year = 2019
latest_data = filtered_df[filtered_df['year'] == latest_year]

# Create a bar chart of CO2 emissions per capita
plt.figure(figsize=(10, 6))

# Create bars
bars = plt.bar(
    latest_data['country'],
    latest_data['co2_per_capita'],
    color='skyblue',
    edgecolor='navy'
)

# Add data labels on top of bars
for bar in bars:
    height = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width()/2.,
        height + 0.1,
        f'{height:.1f}',
        ha='center',
        va='bottom'
    )

# Add plot elements
plt.title(f'CO2 Emissions per Capita ({latest_year})', fontsize=16)
plt.xlabel('Country', fontsize=12)
plt.ylabel('Tonnes of CO2 per Person', fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y', alpha=0.3)

# Show the plot
plt.tight_layout()
plt.show()
```

### 3.3 Pie Chart: Share of Global CO2 Emissions (2019)

```python exec
id: 03-pandas-and-matplotlib-9
# Add 'Rest of World' category to make a complete pie
world_data = latest_data[latest_data['country'] == 'World']['co2'].values[0]
selected_countries = latest_data[latest_data['country'] != 'World']
selected_sum = selected_countries['co2'].sum()
rest_of_world = world_data - selected_sum

# Create data for the pie chart
pie_data = selected_countries.copy()
rest_row = pd.DataFrame({'country': ['Rest of World'], 'co2': [rest_of_world]})
pie_data = pd.concat([pie_data, rest_row], ignore_index=True)

# Create a pie chart
plt.figure(figsize=(10, 8))

# Define colors and explode settings (to emphasize certain slices)
colors = plt.cm.tab10(range(len(pie_data)))
explode = [0.1 if country == 'China' or country == 'United States' else 0 for country in pie_data['country']]

# Create pie chart
plt.pie(
    pie_data['co2'],
    labels=pie_data['country'],
    autopct='%1.1f%%',
    explode=explode,
    colors=colors,
    shadow=True,
    startangle=140
)

# Add title
plt.title(f'Share of Global CO2 Emissions ({latest_year})', fontsize=16)

# Ensure pie is drawn as a circle
plt.axis('equal')

# Show the plot
plt.tight_layout()
plt.show()
```

### 3.4 Subplot: Multiple Visualizations in One Figure

```python exec
id: 03-pandas-and-matplotlib-10
# Create a figure with multiple subplots
fig, axes = plt.subplots(2, 1, figsize=(12, 12))

# Plot 1: Annual change in CO2 emissions for selected countries
for country in ['United States', 'China', 'European Union']:
    country_data = filtered_df[filtered_df['country'] == country].sort_values('year')

    # Calculate annual percentage change
    country_data['pct_change'] = country_data['co2'].pct_change() * 100

    # Plot the data (excluding first row which has NaN percent change)
    axes[0].plot(country_data['year'][1:], country_data['pct_change'][1:], label=country, linewidth=2)

# Add elements to first subplot
axes[0].set_title('Annual Change in CO2 Emissions (1950-Present)', fontsize=14)
axes[0].set_xlabel('Year', fontsize=12)
axes[0].set_ylabel('Annual Change (%)', fontsize=12)
axes[0].axhline(y=0, color='black', linestyle='-', alpha=0.3)
axes[0].legend()
axes[0].grid(True, alpha=0.3)

# Plot 2: Cumulative CO2 emissions since 1750
# Filter and sort data
cumulative_data = df[(df['year'] == latest_year) & (df['country'].isin(countries))]
cumulative_data = cumulative_data.sort_values('cumulative_co2', ascending=False)

# Create horizontal bar chart
bars = axes[1].barh(
    cumulative_data['country'],
    cumulative_data['cumulative_co2'],
    color='lightgreen',
    edgecolor='darkgreen'
)

# Add data labels
for bar in bars:
    width = bar.get_width()
    axes[1].text(
        width + 1000,
        bar.get_y() + bar.get_height()/2,
        f'{width:,.0f} million tonnes',
        va='center'
    )

# Add elements to second subplot
axes[1].set_title('Cumulative CO2 Emissions Since 1750', fontsize=14)
axes[1].set_xlabel('CO2 Emissions (million tonnes)', fontsize=12)
axes[1].grid(axis='x', alpha=0.3)

# Adjust layout and show the figure
plt.tight_layout()
plt.show()
```

## 4. Combining Pandas Operations with Matplotlib

Pandas has built-in plotting capabilities that are based on matplotlib.

```python exec
id: 03-pandas-and-matplotlib-11
# Create a pivot table for easier plotting
emissions_pivot = filtered_df.pivot(index='year', columns='country', values='co2_per_capita')

# Plot directly from the pandas DataFrame
emissions_pivot.plot(
    figsize=(12, 7),
    linewidth=2.5,
    title='CO2 Emissions per Capita Over Time (1950-Present)'
)

plt.ylabel('CO2 per Capita (tonnes)')
plt.grid(True, alpha=0.3)
plt.legend(title='Country')
plt.show()
```

### 4.1 Using Pandas' Built-in Statistical Visualization

```python exec
id: 03-pandas-and-matplotlib-12
# Get most recent year's data for all countries with sufficient data
recent_data = df[(df['year'] == latest_year) &
                (~df['co2_per_capita'].isna()) &
                (df['population'] > 1e6)]

# Create a histogram of CO2 per capita distribution
recent_data['co2_per_capita'].plot(
    kind='hist',
    bins=30,
    figsize=(10, 6),
    color='skyblue',
    edgecolor='black',
    alpha=0.7,
    title=f'Distribution of CO2 Emissions per Capita Across Countries ({latest_year})'
)

plt.xlabel('CO2 per Capita (tonnes)')
plt.ylabel('Number of Countries')
plt.grid(axis='y', alpha=0.3)
plt.show()
```

## 5. Summary and Key Takeaways

### Pandas Key Functions:
- `pd.read_csv()` - Load data from CSV files
- `.head()`, `.describe()` - Quick data exploration
- Filtering with boolean conditions (`df[df['column'] == value]`)
- `.isna()`, `.sum()` - Check for missing values
- `.sort_values()` - Order data
- `.pivot()` - Reshape data for analysis
- `.pct_change()` - Calculate percentage changes

### Matplotlib Key Functions:
- `plt.figure()` - Create a new figure
- `plt.plot()` - Line charts
- `plt.bar()`, `plt.barh()` - Bar charts
- `plt.scatter()` - Scatter plots
- `plt.pie()` - Pie charts
- `plt.subplots()` - Create multiple plots in one figure
- Plot customization: titles, labels, colors, grids, legends

### Pandas + Matplotlib:
- DataFrame's `.plot()` method provides direct visualization
- Built-in methods for common visualizations (histogram, boxplot, etc.)
- Seamless integration for data analysis workflow

These tools together provide a powerful environment for exploring, analyzing, and visualizing data!

## Looking back

Before leaving this page, a sentence on each. What you write stays on this device.

```reflect
- Something you expected before running a cell that turned out differently
- The one idea from this page you could explain to someone else now
- Something you would change or try next, if there were time
- A question this page raised for you that it did not answer. Bring it to the next session; these questions are where the next session starts.
```
