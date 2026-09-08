---
title: "Stuff that was missing from the sample project:"
slug: 08-inserting-rows-and-building-forms
course: database-methods
course_title: "Database Methods"
series: core
series_title: "Notebooks"
version: 2026.09.06.1
---

# Stuff that was missing from the sample project:

1. Inserting a row in a database/dataframe (Section 4)
2. Adding a form (Section 4 or 7)

```python exec
id: 08-inserting-rows-and-building-forms-1
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sqlite3
# import ipywidgets! This was missing before!
import ipywidgets as widgets
from IPython.display import display
```

```python exec
id: 08-inserting-rows-and-building-forms-2
# This data was ported using OWID's data api these are from the previous notebook!
oneP_income_share = pd.read_csv("https://ourworldindata.org/grapher/income-share-top-1-before-tax-wid-extrapolations.csv?v=1&csvType=full&useColumnShortNames=true", storage_options = {'User-Agent': 'Our World In Data data fetch/1.0'})

oneP_income_share.rename(columns = {"Entity": "country", "Code": "country_code", "Year": "year", "p99p100_share_pretax":"OneP_Share", "p99p100_share_pretax_extrapolated": "Extrap_OneP_Share"}, inplace = True)
# lets figure out some more specifics in our next section
my_countries = ["Ireland", "Germany", "Kazakhstan"]
my_countries_df = oneP_income_share[(oneP_income_share["country"].isin(my_countries)) & (oneP_income_share["year"] > 1925)]
```

## Missed Element of Sample Project 1 of 2

### This is just a quick "add a row to your dataframe" to be included in section 4 as per the brief.

```python exec
id: 08-inserting-rows-and-building-forms-3
# lets add a country to my_country that is fictional, perhaps wakanda, with some sample data that is appropriately optimistic
new_row = pd.DataFrame({'country': ['Wakanda'], 'country_code': ['WAK'], 'year': [2023], 'OneP_Share': [0.5], 'Extrap_OneP_Share': [0.16]})
my_countries_df = pd.concat([my_countries_df, new_row], ignore_index=True)
# another way of doing the same thing (commented out so no duplicates)
#my_countries_df.loc[len(my_countries_df)] = pd.DataFrame([new_row])
```

## Alternate if you are using sqlite.

not necessary for project, but useful for the practical exam: (more can be found on the sql pandas cheat sheet)

```python exec
id: 08-inserting-rows-and-building-forms-4
# To do the same thing in sqlite:
# Create or connect to the database
conn = sqlite3.connect('my_database.db')
cursor = conn.cursor()

# Create table (if not exists) and insert data from DataFrame
my_countries_df.to_sql('my_countries_table', conn, if_exists='replace', index=False)

# Define and execute the INSERT statement
insert_query = """
    INSERT INTO my_countries_table (country, country_code, year, OneP_Share, Extrap_OneP_Share)
    VALUES (?, ?, ?, ?, ?);
"""
new_row_data = ('Wakanda', 'WAK', 2023, 0.5, 0.16)
cursor.execute(insert_query, new_row_data)

# Commit changes and fetch the updated DataFrame
conn.commit()
my_countries_df = pd.read_sql_query("SELECT * FROM my_countries_table", conn)

# Close the connection
conn.close()

# Now my_countries_df includes Wakanda.
```

## Missed Element of Sample Project 2 of 2

### This form can be placed in either section 7 or 4. I recommend you use it on one of your queries (section 4) with a dataframe that has only a few columns selected so the form is nice and easy to manage. 3 fields is totally sufficient! And you are welcome to modify the code below as this was such a last minute catch. Note you may indeed use this with the previous "insert into db/df" part.

```python exec
id: 08-inserting-rows-and-building-forms-5
# Assuming our DataFrame is our original dataframe, it would be fine to use the smaller ones!
import ipywidgets as widgets
from IPython.display import display
# note that we imported import ipywidgets as widgets and from IPython.display import display to make the code easier to read

# Input widgets for each column, these would change type (widgets.STUDENTS DATA TYPE) based on what they want to have as thier data
country_input = widgets.Text(description="Country:")
country_code_input = widgets.Text(description="CNTRYCode:")
year_input = widgets.IntText(description="Year:")
oneP_share_input = widgets.FloatText(description="One% Share:")
# if you want your widget to be a bit wider, its a bit annoying, but doable: these are the same as CSS Tags for these widgets pushed through our jupyter notebook server! :)
extrap_oneP_share_input = widgets.FloatText(description="Extrapolated 1% Share of Income:",style={'description_width': '200px'}, layout={'width': '500px'}  )

# It is possible to input the row directly without a function but this code is more reusable and allows one to better see the fact that we are dealing with something asynchronous in the next step
def add_row_to_dataframe(button_input_variable_Necessary_But_Not_Used):
    new_row = {
        'country': country_input.value,
        'country_code': country_code_input.value,
        'year': year_input.value,
        'OneP_Share': oneP_share_input.value,
        'Extrap_OneP_Share': extrap_oneP_share_input.value
    }
    global oneP_income_share  # Access the global DataFrame
    # concat is the newer preferred method of adding, but students can use
    #df.loc[len(df)] = new_row if they prefer
    oneP_income_share = pd.concat([oneP_income_share, pd.DataFrame([new_row])], ignore_index=True)
    print("Row added successfully!")

# Button to add the row
add_row_button = widgets.Button(description="Add Row")
add_row_button.on_click(add_row_to_dataframe)

# Display the form by adding all the various widgets--don't forget the button!
# when the button is clicked the function should print a confirmation
display(country_input, country_code_input, year_input, oneP_share_input, extrap_oneP_share_input, add_row_button)
```

## Shorter Easier to Transfer Version of Code

```python exec
id: 08-inserting-rows-and-building-forms-6
import ipywidgets as widgets
from IPython.display import display
# Input widgets for each column based on column's datatype
country_input = widgets.Text(description="Country:")
country_code_input = widgets.Text(description="CNTRYCode:")
year_input = widgets.IntText(description="Year:")
oneP_share_input = widgets.FloatText(description="1% Share of Income:")
extrap_oneP_share_input = widgets.FloatText(description="Extrapolated 1% Share of Income:")

def add_row_to_dataframe(b):
    new_row = {
        'country': country_input.value,
        'country_code': country_code_input.value,
        'year': year_input.value,
        'OneP_Share': oneP_share_input.value,
        'Extrap_OneP_Share': extrap_oneP_share_input.value
    }
    global oneP_income_share  # Access the global DataFrame
    # concat is prefered (used above) here is another option
    oneP_income_share.loc[len(oneP_income_share)] = pd.DataFrame([new_row])
    print("Row added successfully!")

# Button to add the row
add_row_button = widgets.Button(description="Add Row")
add_row_button.on_click(add_row_to_dataframe)

# Display the form by adding all the various widgets
display(country_input, country_code_input, year_input, oneP_share_input, extrap_oneP_share_input, add_row_button)
```

## Looking back

Before leaving this page, a sentence on each. What you write stays on this device.

```reflect
- Something you expected before running a cell that turned out differently
- The one idea from this page you could explain to someone else now
- Something you would change or try next, if there were time
- A question this page raised for you that it did not answer. Bring it to the next session; these questions are where the next session starts.
```
