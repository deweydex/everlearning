---
title: "Introduction to Interactive Jupyter with ipywidgets"
slug: 07-interactive-widgets
course: database-methods
course_title: "Database Methods"
series: core
series_title: "Notebooks"
version: 2026.09.06.1
---

# Introduction to Interactive Jupyter with ipywidgets

This notebook demonstrates how to use ipywidgets to create interactive elements in Jupyter Notebooks. We'll also show how to connect these widgets to SQLite databases and pandas DataFrames.

## 1. Getting Started with ipywidgets

First, let's import the necessary libraries:

```python exec
id: 07-interactive-widgets-1
# Import basic libraries
import pandas as pd
import numpy as np
import sqlite3
import matplotlib.pyplot as plt
from IPython.display import display, clear_output

# Import ipywidgets
import ipywidgets as widgets
from ipywidgets import interact, Button, HBox, VBox

# Set up matplotlib for notebook display

```

## 2. Basic Widgets Examples

Let's explore some basic widgets. These are the building blocks for interactive applications.

```python exec
id: 07-interactive-widgets-2
# Text widget - for entering text
text = widgets.Text(
    description='Name:',
    placeholder='Enter your name'
)
display(text)

# Slider - for selecting a number in a range
slider = widgets.IntSlider(
    description='Age:',
    min=0,
    max=100,
    value=25
)
display(slider)

# Dropdown - for selecting from a list of options
dropdown = widgets.Dropdown(
    description='Favorite color:',
    options=['Red', 'Green', 'Blue', 'Yellow', 'Purple']
)
display(dropdown)

# Button - for triggering actions
button = widgets.Button(
    description='Click Me!',
    button_style='success'  # Options: 'success', 'info', 'warning', 'danger', ''
)
display(button)
```

## 3. Widget Interaction

Now, let's make these widgets interactive by connecting them to functions:

```python exec
id: 07-interactive-widgets-3
# Create an output area to display results
output = widgets.Output()

# Define what happens when the button is clicked
def on_button_click(b):
    # Clear previous output
    with output:
        clear_output()
        print(f"Hello, {text.value}!")
        print(f"You are {slider.value} years old.")
        print(f"Your favorite color is {dropdown.value}.")

# Connect the function to the button
button.on_click(on_button_click)

# Display all the widgets together
display(text, slider, dropdown, button, output)
```

## 4. Creating a Simple SQLite Database

Let's create a simple database to store student information:

```python exec
id: 07-interactive-widgets-4
# Create a connection to a SQLite database (will be created if it doesn't exist)
conn = sqlite3.connect('students.db')
cursor = conn.cursor()

# Create a table for student records
cursor.execute('''
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER,
    grade TEXT
)
''')

# Add some sample data
sample_students = [
    ('Alice Smith', 20, 'A'),
    ('Bob Johnson', 22, 'B+'),
    ('Charlie Brown', 21, 'A-'),
    ('Diana Ross', 19, 'B')
]

# Check if the table is empty
cursor.execute("SELECT COUNT(*) FROM students")
if cursor.fetchone()[0] == 0:
    # Insert sample data
    cursor.executemany("INSERT INTO students (name, age, grade) VALUES (?, ?, ?)", sample_students)
    print("Added sample data to the database.")
else:
    print("Database already contains records.")

# Save (commit) the changes
conn.commit()

# Query the database and display the data
students_df = pd.read_sql_query("SELECT * FROM students", conn)
display(students_df)

# Close the connection
conn.close()
```

## 5. Simple Student Record Form

Now let's create a form to add student records to our database:

```python exec
id: 07-interactive-widgets-5
# Create form widgets
student_name = widgets.Text(description='Name:', placeholder='Enter student name')
student_age = widgets.IntSlider(description='Age:', min=16, max=30, value=20)
student_grade = widgets.Dropdown(
    options=['A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D', 'F'],
    value='B',
    description='Grade:'
)

submit_button = widgets.Button(
    description='Add Student',
    button_style='success'
)

refresh_button = widgets.Button(
    description='Refresh',
    button_style='info'
)

form_output = widgets.Output()
data_output = widgets.Output()

# Function to add a new student record
def add_student(b):
    with form_output:
        clear_output()

        # Validate input
        if not student_name.value:
            print("Error: Student name is required.")
            return

        try:
            # Connect to the database
            conn = sqlite3.connect('students.db')
            cursor = conn.cursor()

            # Insert the new student
            cursor.execute(
                "INSERT INTO students (name, age, grade) VALUES (?, ?, ?)",
                (student_name.value, student_age.value, student_grade.value)
            )

            # Save the changes
            conn.commit()
            conn.close()

            print(f"Added new student: {student_name.value}")

            # Clear the form
            student_name.value = ''
            student_age.value = 20
            student_grade.value = 'B'

            # Refresh the data display
            refresh_data(None)

        except Exception as e:
            print(f"Error: {e}")

# Function to display the current data
def refresh_data(b):
    with data_output:
        clear_output()

        # Connect to the database and fetch data
        conn = sqlite3.connect('students.db')
        students_df = pd.read_sql_query("SELECT * FROM students", conn)
        conn.close()

        # Display the data
        display(students_df)

        # Create a simple visualization of grade distribution
        grade_counts = students_df['grade'].value_counts().sort_index()

        plt.figure(figsize=(10, 5))
        grade_counts.plot(kind='bar')
        plt.title('Grade Distribution')
        plt.xlabel('Grade')
        plt.ylabel('Number of Students')
        plt.show()

# Connect the buttons to their functions
submit_button.on_click(add_student)
refresh_button.on_click(refresh_data)

# Arrange the form with all elements
form = VBox([
    student_name,
    student_age,
    student_grade,
    HBox([submit_button, refresh_button]),
    form_output
])

# Display the form and data
display(widgets.HTML("<h3>Student Records</h3>"))
display(form)
display(widgets.HTML("<h4>Current Students</h4>"))
display(data_output)

# Show the initial data
refresh_data(None)
```

## 6. Interactive Data Filtering

Let's add the ability to filter our student data:

```python exec
id: 07-interactive-widgets-6
# Create filter widgets
min_age_filter = widgets.IntSlider(
    description='Min Age:',
    min=16,
    max=30,
    value=16
)

max_age_filter = widgets.IntSlider(
    description='Max Age:',
    min=16,
    max=30,
    value=30
)

grade_filter = widgets.Dropdown(
    options=['All', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D', 'F'],
    value='All',
    description='Grade:'
)

filter_button = widgets.Button(
    description='Apply Filters',
    button_style='primary'
)

filter_output = widgets.Output()

# Function to filter the data
def filter_data(b):
    with filter_output:
        clear_output()

        # Connect to the database and fetch data
        conn = sqlite3.connect('students.db')
        students_df = pd.read_sql_query("SELECT * FROM students", conn)
        conn.close()

        # Apply filters
        filtered_df = students_df[
            (students_df['age'] >= min_age_filter.value) &
            (students_df['age'] <= max_age_filter.value)
        ]

        if grade_filter.value != 'All':
            filtered_df = filtered_df[filtered_df['grade'] == grade_filter.value]

        # Display the filtered data
        print(f"Found {len(filtered_df)} students matching your criteria.")
        display(filtered_df)

        # Create a simple chart (if there's data)
        if len(filtered_df) > 0:
            plt.figure(figsize=(10, 5))
            plt.scatter(filtered_df['age'], range(len(filtered_df)), c='blue')
            plt.yticks(range(len(filtered_df)), filtered_df['name'])
            plt.xlabel('Age')
            plt.title('Students by Age')
            plt.grid(True, alpha=0.3)
            plt.tight_layout()
            plt.show()

# Connect the filter button
filter_button.on_click(filter_data)

# Arrange the filter controls
filters = VBox([
    widgets.HTML("<h3>Filter Students</h3>"),
    min_age_filter,
    max_age_filter,
    grade_filter,
    filter_button,
    filter_output
])

# Display the filter controls
display(filters)

# Initial filter run
filter_data(None)
```

## 7. Visualizing Student Data

Let's create a simple visualization tool that updates when you change parameters:

```python exec
id: 07-interactive-widgets-7
# Create visualization controls
chart_type = widgets.RadioButtons(
    options=['Bar Chart', 'Pie Chart', 'Scatter Plot'],
    value='Bar Chart',
    description='Chart Type:'
)

color_option = widgets.ColorPicker(
    concise=False,
    description='Chart Color:',
    value='#3498db'
)

viz_output = widgets.Output()

# Function to update the visualization
def update_viz(change):
    with viz_output:
        clear_output()

        # Get the data
        conn = sqlite3.connect('students.db')
        students_df = pd.read_sql_query("SELECT * FROM students", conn)
        conn.close()

        if len(students_df) == 0:
            print("No data to visualize.")
            return

        # Create the requested chart
        plt.figure(figsize=(10, 6))

        if chart_type.value == 'Bar Chart':
            # Create a grade count bar chart
            grade_counts = students_df['grade'].value_counts().sort_index()
            grade_counts.plot(kind='bar', color=color_option.value)
            plt.title('Grades Distribution')
            plt.xlabel('Grade')
            plt.ylabel('Number of Students')

        elif chart_type.value == 'Pie Chart':
            # Create a grade distribution pie chart
            grade_counts = students_df['grade'].value_counts()
            plt.pie(grade_counts, labels=grade_counts.index, autopct='%1.1f%%', startangle=90,
                   colors=[color_option.value] + [f'#{np.random.randint(0, 16777215):06x}' for _ in range(len(grade_counts)-1)])
            plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle
            plt.title('Grades Distribution')

        elif chart_type.value == 'Scatter Plot':
            # Create a scatter plot of ID vs age
            plt.scatter(students_df['id'], students_df['age'], color=color_option.value, s=100)
            plt.title('Student Age by ID')
            plt.xlabel('Student ID')
            plt.ylabel('Age')
            plt.grid(True, alpha=0.3)

        plt.tight_layout()
        plt.show()

# Connect the controls to the update function
chart_type.observe(update_viz, names='value')
color_option.observe(update_viz, names='value')

# Arrange the visualization controls
viz_controls = VBox([
    widgets.HTML("<h3>Data Visualization</h3>"),
    chart_type,
    color_option,
    viz_output
])

# Display the visualization controls
display(viz_controls)

# Initial visualization
update_viz(None)
```

## 8. Data Summarization

Finally, let's create a simple tool to see summary statistics about our students:

```python exec
id: 07-interactive-widgets-8
# Create a button to show summary statistics
summary_button = widgets.Button(
    description='Show Summary',
    button_style='info'
)

summary_output = widgets.Output()

# Function to show the summary
def show_summary(b):
    with summary_output:
        clear_output()

        # Get the data
        conn = sqlite3.connect('students.db')
        students_df = pd.read_sql_query("SELECT * FROM students", conn)
        conn.close()

        # Show basic statistics
        print("=== Student Database Summary ===")
        print(f"Total number of students: {len(students_df)}")
        print(f"Average age: {students_df['age'].mean():.1f} years")
        print(f"Youngest student: {students_df['age'].min()} years")
        print(f"Oldest student: {students_df['age'].max()} years")
        print("\n=== Grade Distribution ===")

        # Grade distribution
        grade_counts = students_df['grade'].value_counts().sort_index()
        for grade, count in grade_counts.items():
            percentage = count / len(students_df) * 100
            print(f"{grade}: {count} students ({percentage:.1f}%)")

        # Create a simple summary visualization
        plt.figure(figsize=(10, 5))
        students_df['age'].plot(kind='hist', bins=range(16, 31), edgecolor='black')
        plt.title('Age Distribution')
        plt.xlabel('Age')
        plt.ylabel('Number of Students')
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.show()

# Connect the button
summary_button.on_click(show_summary)

# Display the summary controls
display(widgets.HTML("<h3>Database Summary</h3>"))
display(summary_button)
display(summary_output)

# Initial summary
show_summary(None)
```

## Conclusion

In this notebook, we've learned how to:

1. Create basic ipywidgets (text inputs, sliders, dropdowns, buttons)
2. Connect widgets to functions
3. Create and interact with a SQLite database
4. Build a simple form to add data to the database
5. Filter and visualize data using interactive controls
6. Generate summary statistics

These techniques can be extended to create more complex interactive applications for data analysis and visualization.

## Looking back

Before leaving this page, a sentence on each. What you write stays on this device.

```reflect
- Something you expected before running a cell that turned out differently
- The one idea from this page you could explain to someone else now
- Something you would change or try next, if there were time
- A question this page raised for you that it did not answer. Bring it to the next session; these questions are where the next session starts.
```
