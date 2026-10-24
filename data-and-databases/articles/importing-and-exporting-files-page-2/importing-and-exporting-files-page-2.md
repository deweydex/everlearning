---
title: "Working with Files: Import, Explore, and Export (2 of 2)"
slug: importing-and-exporting-files-page-2
course: database-methods
series: notebooks
series_title: "Notebooks"
version: 2026.09.07.1
---

*Page 2 of 2.*

*Before starting this page, run the cell below. It repeats the setup from the earlier pages that this page uses.*

```python exec
id: importing-and-exporting-files-page-2-setup
# From an earlier page of this tutorial: needed again here.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Detect environment
try:
    import google.colab
    IN_COLAB = True
    print("Running in Google Colab")
except ImportError:
    IN_COLAB = False
    print("Running in standard Jupyter environment")


# From an earlier page of this tutorial: needed again here.
# Create a dataset about European cities
cities_data = {
    'city': ['Dublin', 'London', 'Paris', 'Berlin', 'Madrid', 'Rome', 'Amsterdam', 'Vienna'],
    'country': ['Ireland', 'UK', 'France', 'Germany', 'Spain', 'Italy', 'Netherlands', 'Austria'],
    'population_millions': [1.4, 9.0, 2.1, 3.6, 3.3, 2.9, 0.9, 1.9],
    'avg_temp_july_c': [16, 19, 20, 19, 25, 26, 17, 21],
    'avg_rainfall_mm': [762, 602, 637, 570, 436, 798, 838, 620],
    'year_founded': [841, 47, -250, 1237, 852, -753, 1275, -500]
}

cities = pd.DataFrame(cities_data)
cities

# From an earlier page of this tutorial: needed again here.
# Save to CSV file
# index=False prevents pandas from writing row numbers as a column
cities.to_csv('european_cities.csv', index=False)

print("Saved to european_cities.csv")

# From an earlier page of this tutorial: needed again here.
# Let's look at what the CSV file actually contains
with open('european_cities.csv', 'r') as f:
    print(f.read())

# From an earlier page of this tutorial: needed again here.
# Read the CSV back into a DataFrame
df = pd.read_csv('european_cities.csv')
df

# From an earlier page of this tutorial: needed again here.
# Uncomment and run in Colab to upload a file
# if IN_COLAB:
#     from google.colab import files
#     uploaded = files.upload()  # Opens a file picker
#     # Then read with: df = pd.read_csv('your_filename.csv')

# From an earlier page of this tutorial: needed again here.
# Read only specific columns
df_subset = pd.read_csv('european_cities.csv', usecols=['city', 'country', 'population_millions'])
df_subset

# From an earlier page of this tutorial: needed again here.
# Use a column as the index
df_indexed = pd.read_csv('european_cities.csv', index_col='city')
df_indexed

# From an earlier page of this tutorial: needed again here.
# Read only first N rows (useful for previewing large files)
df_preview = pd.read_csv('european_cities.csv', nrows=3)
df_preview

# From an earlier page of this tutorial: needed again here.
# Other common parameters:
# sep='\t'          - Tab-separated files
# encoding='utf-8'  - Specify character encoding
# skiprows=2        - Skip header rows
# na_values=['N/A'] - Treat specific strings as missing

# From an earlier page of this tutorial: needed again here.
# Reload fresh
df = pd.read_csv('european_cities.csv')

# Basic info
print(f"Shape: {df.shape}")
print(f"\nColumns: {list(df.columns)}")
print(f"\nData types:")
print(df.dtypes)

# From an earlier page of this tutorial: needed again here.
# Statistical summary
df.describe()

# From an earlier page of this tutorial: needed again here.
# Bar chart: Population by city
plt.figure(figsize=(10, 5))

# Sort for better visualisation
df_sorted = df.sort_values('population_millions', ascending=True)

plt.barh(df_sorted['city'], df_sorted['population_millions'], color='steelblue', edgecolor='white')
plt.xlabel('Population (millions)')
plt.title('European Cities by Population')
plt.tight_layout()
plt.show()

# From an earlier page of this tutorial: needed again here.
# Scatter plot: Temperature vs Rainfall
plt.figure(figsize=(10, 6))

plt.scatter(df['avg_temp_july_c'], df['avg_rainfall_mm'], 
            s=df['population_millions'] * 50,  # Size by population
            alpha=0.6, color='teal', edgecolor='white', linewidth=2)

# Label each point
for i, row in df.iterrows():
    plt.annotate(row['city'], (row['avg_temp_july_c'] + 0.3, row['avg_rainfall_mm']))

plt.xlabel('Average July Temperature (°C)')
plt.ylabel('Average Annual Rainfall (mm)')
plt.title('European Cities: Climate Comparison\n(circle size = population)')
plt.tight_layout()
plt.show()

# From an earlier page of this tutorial: needed again here.
# Add a calculated column
df['age_years'] = 2024 - df['year_founded']

# Filter: Cities founded before year 0
ancient_cities = df[df['year_founded'] < 0]
print("Ancient cities (founded BCE):")
ancient_cities[['city', 'year_founded', 'age_years']]

# From an earlier page of this tutorial: needed again here.
# Filter: Warm and dry cities
warm_dry = df[(df['avg_temp_july_c'] > 20) & (df['avg_rainfall_mm'] < 700)]
print("Warm (>20°C) and relatively dry (<700mm):")
warm_dry[['city', 'avg_temp_july_c', 'avg_rainfall_mm']]

# From an earlier page of this tutorial: needed again here.
# Save the enhanced DataFrame
df.to_csv('cities_with_age.csv', index=False)
print("Saved enhanced data to cities_with_age.csv")

# In Colab, download the file
if IN_COLAB:
    from google.colab import files
    files.download('cities_with_age.csv')

# From an earlier page of this tutorial: needed again here.
# Install openpyxl if needed (usually pre-installed)
# !pip install openpyxl

# From an earlier page of this tutorial: needed again here.
# Create a second dataset: Monthly temperatures
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

temp_data = {
    'month': months,
    'dublin': [5, 5, 7, 9, 12, 14, 16, 16, 14, 11, 7, 6],
    'madrid': [6, 8, 11, 13, 17, 22, 25, 25, 21, 15, 9, 7],
    'stockholm': [-3, -3, 1, 6, 11, 16, 18, 17, 12, 7, 2, -1]
}

temps = pd.DataFrame(temp_data)
temps

# From an earlier page of this tutorial: needed again here.
# Save single DataFrame to Excel
temps.to_excel('temperatures.xlsx', index=False, sheet_name='Monthly')
print("Saved to temperatures.xlsx")

# From an earlier page of this tutorial: needed again here.
# Save multiple DataFrames to different sheets in one Excel file
with pd.ExcelWriter('city_data.xlsx') as writer:
    df.to_excel(writer, sheet_name='City Info', index=False)
    temps.to_excel(writer, sheet_name='Temperatures', index=False)

print("Saved city_data.xlsx with two sheets")

# From an earlier page of this tutorial: needed again here.
# Read from Excel
df_loaded = pd.read_excel('temperatures.xlsx')
df_loaded

# From an earlier page of this tutorial: needed again here.
# Read a specific sheet by name
temps_loaded = pd.read_excel('city_data.xlsx', sheet_name='Temperatures')
temps_loaded

# From an earlier page of this tutorial: needed again here.
# Read all sheets into a dictionary
all_sheets = pd.read_excel('city_data.xlsx', sheet_name=None)
print(f"Sheets found: {list(all_sheets.keys())}")

# Access each sheet by name
print(f"\nCity Info shape: {all_sheets['City Info'].shape}")
print(f"Temperatures shape: {all_sheets['Temperatures'].shape}")
```

## Data Exploration 2: Temperature Analysis

Let's explore the temperature data.

```python exec
id: importing-and-exporting-files-page-2-1
# Line chart: Monthly temperatures for all cities
plt.figure(figsize=(12, 6))

plt.plot(temps['month'], temps['dublin'], marker='o', linewidth=2, label='Dublin')
plt.plot(temps['month'], temps['madrid'], marker='s', linewidth=2, label='Madrid')
plt.plot(temps['month'], temps['stockholm'], marker='^', linewidth=2, label='Stockholm')

plt.xlabel('Month')
plt.ylabel('Average Temperature (°C)')
plt.title('Monthly Average Temperatures')
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
```

```python exec
id: importing-and-exporting-files-page-2-2
# Calculate annual statistics
print("Annual Temperature Statistics (°C):")
print()
for city in ['dublin', 'madrid', 'stockholm']:
    print(f"{city.title()}:")
    print(f"  Mean: {temps[city].mean():.1f}")
    print(f"  Min:  {temps[city].min()}")
    print(f"  Max:  {temps[city].max()}")
    print(f"  Range: {temps[city].max() - temps[city].min()}")
    print()
```

```python exec
id: importing-and-exporting-files-page-2-3
# Add summary statistics as new columns
temps['average'] = temps[['dublin', 'madrid', 'stockholm']].mean(axis=1)
temps['range'] = temps[['dublin', 'madrid', 'stockholm']].max(axis=1) - temps[['dublin', 'madrid', 'stockholm']].min(axis=1)

temps
```

```python exec
id: importing-and-exporting-files-page-2-4
# Multiple subplots
fig, axes = plt.subplots(1, 3, figsize=(15, 4), sharey=True)

cities_temps = ['dublin', 'madrid', 'stockholm']
colors = ['#2ecc71', '#e74c3c', '#3498db']

for i, (city, color) in enumerate(zip(cities_temps, colors)):
    axes[i].bar(temps['month'], temps[city], color=color, edgecolor='white')
    axes[i].set_title(city.title())
    axes[i].set_xlabel('Month')
    axes[i].axhline(y=0, color='gray', linestyle='--', alpha=0.5)
    if i == 0:
        axes[i].set_ylabel('Temperature (°C)')

fig.suptitle('Monthly Temperatures by City', fontsize=14, y=1.02)
plt.tight_layout()
plt.show()
```

```python exec
id: importing-and-exporting-files-page-2-5
# Save enhanced temperature data
temps.to_csv('temperatures_with_stats.csv', index=False)
print("Saved temperatures_with_stats.csv")
```

### Saving a Figure

```python exec
id: importing-and-exporting-files-page-2-6
# Create and save a figure
fig, ax = plt.subplots(figsize=(10, 6))

ax.plot(temps['month'], temps['dublin'], marker='o', linewidth=2, label='Dublin')
ax.plot(temps['month'], temps['madrid'], marker='s', linewidth=2, label='Madrid')
ax.plot(temps['month'], temps['stockholm'], marker='^', linewidth=2, label='Stockholm')

ax.set_xlabel('Month')
ax.set_ylabel('Average Temperature (°C)')
ax.set_title('Monthly Average Temperatures')
ax.legend()
ax.grid(True, alpha=0.3)

# Save to file
fig.savefig('temperature_comparison.png', dpi=150, bbox_inches='tight')
print("Saved temperature_comparison.png")

plt.show()

# Download in Colab
if IN_COLAB:
    from google.colab import files
    files.download('temperature_comparison.png')
```

## Practice Exercises

**Exercise 1:** Create a DataFrame with information about 5 movies (title, year, rating, genre). Save it to a CSV file, then read it back and display the movies sorted by rating.

```python exec
id: importing-and-exporting-files-page-2-7
# Your code here
```

**Exercise 2:** Using the cities DataFrame, create a bar chart showing average July temperature for each city, with cities sorted from coolest to warmest. Save the figure as a PNG file.

```python exec
id: importing-and-exporting-files-page-2-8
# Your code here
```

**Exercise 3:** Create an Excel file with two sheets: one containing the original cities data and one containing only cities with population over 2 million. Name the sheets appropriately.

```python exec
id: importing-and-exporting-files-page-2-9
# Your code here
```

**Exercise 4:** Using the temperatures data, filter to find months where all three cities have temperatures above 10°C. Display these months.

```python exec
id: importing-and-exporting-files-page-2-10
# Your code here
```

## Summary

This notebook covered the essential file operations:

**CSV files:** `pd.read_csv()` and `df.to_csv()` with useful parameters like `usecols`, `index_col`, and `nrows`.

**Excel files:** `pd.read_excel()` and `df.to_excel()`, including working with multiple sheets using `ExcelWriter` and `sheet_name=None`.

**Data exploration:** Using `describe()`, filtering, calculated columns, and various matplotlib visualisations.

**Saving figures:** `fig.savefig()` with `dpi` and `bbox_inches` parameters.

**Colab compatibility:** Using `files.upload()` and `files.download()` for file transfer.

## Bibliography

pandas documentation: IO Tools. https://pandas.pydata.org/docs/user_guide/io.html

McKinney, W. (2022). *Python for Data Analysis* (3rd ed.). O'Reilly Media. Chapter 6 covers data loading. https://wesmckinney.com/book/

Matplotlib documentation: Saving figures. https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.savefig.html

Google Colab: External data. https://colab.research.google.com/notebooks/io.ipynb

## Cleanup

```python exec
id: importing-and-exporting-files-page-2-11
# Optional: Remove files created during this tutorial
import os

files_to_remove = [
    'european_cities.csv', 'cities_with_age.csv', 'temperatures.xlsx',
    'city_data.xlsx', 'temperatures_with_stats.csv', 'temperature_comparison.png'
]

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
- A question this page raised that it did not answer
```
