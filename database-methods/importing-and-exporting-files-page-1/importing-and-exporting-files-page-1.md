---
title: "Working with Files: Import, Explore, and Export (1 of 2)"
slug: importing-and-exporting-files-page-1
course: database-methods
series: notebooks
series_title: "Notebooks"
version: 2026.09.07.1
---

*Page 1 of 2.*

# Working with Files: Import, Explore, and Export

This notebook focuses on the practical skills of loading data from files, exploring it with pandas and matplotlib, and saving your results. These operations form the foundation of most data analysis work: you receive data in a file, examine and transform it, then save the results.

We will work through two complete data exploration examples, from loading a CSV or Excel file through to exporting processed results. The techniques here apply to virtually any tabular dataset you might encounter.

## Environment Setup

```python exec
id: importing-and-exporting-files-page-1-1
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

```

## Part 1: CSV Files

CSV (Comma-Separated Values) is the most common format for sharing tabular data. It's plain text, readable by virtually any software, and easy to inspect manually.

### Creating Sample Data

Let's first create a dataset to work with, then save it so we can practice loading it.

```python exec
id: importing-and-exporting-files-page-1-2
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
```

### Saving to CSV

```python exec
id: importing-and-exporting-files-page-1-3
# Save to CSV file
# index=False prevents pandas from writing row numbers as a column
cities.to_csv('european_cities.csv', index=False)

print("Saved to european_cities.csv")
```

```python exec
id: importing-and-exporting-files-page-1-4
# Let's look at what the CSV file actually contains
with open('european_cities.csv', 'r') as f:
    print(f.read())
```

The first line contains column names, and each subsequent line is one row of data. Values are separated by commas, which is where the format gets its name.

### Loading from CSV

```python exec
id: importing-and-exporting-files-page-1-5
# Read the CSV back into a DataFrame
df = pd.read_csv('european_cities.csv')
df
```

### Colab File Upload

In Google Colab, you might need to upload files from your computer. Here's how:

```python exec
id: importing-and-exporting-files-page-1-6
# Uncomment and run in Colab to upload a file
# if IN_COLAB:
#     from google.colab import files
#     uploaded = files.upload()  # Opens a file picker
#     # Then read with: df = pd.read_csv('your_filename.csv')
```

### Useful read_csv Parameters

Real-world CSV files often need additional parameters.

```python exec
id: importing-and-exporting-files-page-1-7
# Read only specific columns
df_subset = pd.read_csv('european_cities.csv', usecols=['city', 'country', 'population_millions'])
df_subset
```

```python exec
id: importing-and-exporting-files-page-1-8
# Use a column as the index
df_indexed = pd.read_csv('european_cities.csv', index_col='city')
df_indexed
```

```python exec
id: importing-and-exporting-files-page-1-9
# Read only first N rows (useful for previewing large files)
df_preview = pd.read_csv('european_cities.csv', nrows=3)
df_preview
```

```python exec
id: importing-and-exporting-files-page-1-10
# Other common parameters:
# sep='\t'          - Tab-separated files
# encoding='utf-8'  - Specify character encoding
# skiprows=2        - Skip header rows
# na_values=['N/A'] - Treat specific strings as missing
```

## Data Exploration 1: European Cities

Now let's explore our cities dataset using the techniques from previous notebooks.

```python exec
id: importing-and-exporting-files-page-1-11
# Reload fresh
df = pd.read_csv('european_cities.csv')

# Basic info
print(f"Shape: {df.shape}")
print(f"\nColumns: {list(df.columns)}")
print(f"\nData types:")
print(df.dtypes)
```

```python exec
id: importing-and-exporting-files-page-1-12
# Statistical summary
df.describe()
```

```python exec
id: importing-and-exporting-files-page-1-13
# Bar chart: Population by city
plt.figure(figsize=(10, 5))

# Sort for better visualisation
df_sorted = df.sort_values('population_millions', ascending=True)

plt.barh(df_sorted['city'], df_sorted['population_millions'], color='steelblue', edgecolor='white')
plt.xlabel('Population (millions)')
plt.title('European Cities by Population')
plt.tight_layout()
plt.show()
```

```python exec
id: importing-and-exporting-files-page-1-14
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
```

```python exec
id: importing-and-exporting-files-page-1-15
# Add a calculated column
df['age_years'] = 2024 - df['year_founded']

# Filter: Cities founded before year 0
ancient_cities = df[df['year_founded'] < 0]
print("Ancient cities (founded BCE):")
ancient_cities[['city', 'year_founded', 'age_years']]
```

```python exec
id: importing-and-exporting-files-page-1-16
# Filter: Warm and dry cities
warm_dry = df[(df['avg_temp_july_c'] > 20) & (df['avg_rainfall_mm'] < 700)]
print("Warm (>20°C) and relatively dry (<700mm):")
warm_dry[['city', 'avg_temp_july_c', 'avg_rainfall_mm']]
```

### Exporting Results

```python exec
id: importing-and-exporting-files-page-1-17
# Save the enhanced DataFrame
df.to_csv('cities_with_age.csv', index=False)
print("Saved enhanced data to cities_with_age.csv")

# In Colab, download the file
if IN_COLAB:
    from google.colab import files
    files.download('cities_with_age.csv')
```

## Part 2: Excel Files

Excel files can contain multiple sheets, formatting, and formulas. Pandas reads and writes Excel using the openpyxl library.

```python exec
id: importing-and-exporting-files-page-1-18
# Install openpyxl if needed (usually pre-installed)
# !pip install openpyxl
```

```python exec
id: importing-and-exporting-files-page-1-19
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
```

### Saving to Excel

```python exec
id: importing-and-exporting-files-page-1-20
# Save single DataFrame to Excel
temps.to_excel('temperatures.xlsx', index=False, sheet_name='Monthly')
print("Saved to temperatures.xlsx")
```

```python exec
id: importing-and-exporting-files-page-1-21
# Save multiple DataFrames to different sheets in one Excel file
with pd.ExcelWriter('city_data.xlsx') as writer:
    df.to_excel(writer, sheet_name='City Info', index=False)
    temps.to_excel(writer, sheet_name='Temperatures', index=False)

print("Saved city_data.xlsx with two sheets")
```

### Loading from Excel

```python exec
id: importing-and-exporting-files-page-1-22
# Read from Excel
df_loaded = pd.read_excel('temperatures.xlsx')
df_loaded
```

```python exec
id: importing-and-exporting-files-page-1-23
# Read a specific sheet by name
temps_loaded = pd.read_excel('city_data.xlsx', sheet_name='Temperatures')
temps_loaded
```

```python exec
id: importing-and-exporting-files-page-1-24
# Read all sheets into a dictionary
all_sheets = pd.read_excel('city_data.xlsx', sheet_name=None)
print(f"Sheets found: {list(all_sheets.keys())}")

# Access each sheet by name
print(f"\nCity Info shape: {all_sheets['City Info'].shape}")
print(f"Temperatures shape: {all_sheets['Temperatures'].shape}")
```

## Looking back

Before leaving this page, a sentence on each. What you write stays on this device.

```reflect
- Something you expected before running a cell that turned out differently
- The one idea from this page you could explain to someone else now
- A question this page raised that it did not answer
```
