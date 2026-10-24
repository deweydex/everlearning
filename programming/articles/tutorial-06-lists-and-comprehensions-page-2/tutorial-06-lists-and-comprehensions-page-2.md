---
title: "tutorial-06-lists-and-comprehensions-page-2 (2 of 2)"
slug: tutorial-06-lists-and-comprehensions-page-2
course: programming-and-design-principles
course_title: "Programming and Design Principles"
series: tutorials
series_title: "Tutorials"
version: 2026.09.06.1
---

Before starting this page, run the cell below. It repeats the imports and definitions from the earlier pages that this page uses.

```python exec
id: tutorial-06-lists-and-comprehensions-page-2-setup
# Study hours for five students
study_hours = [12, 15, 8, 20, 10]

# Student names
student_names = ["Alice", "Bob", "Charlie", "Diana", "Eve"]

# Exam scores
exam_scores = [85, 92, 78, 95, 88]

print("Study hours:", study_hours)
print("Names:", student_names)
print("Scores:", exam_scores)

study_hours = [12, 15, 8, 20, 10]

# Accessing individual elements
first_student = study_hours[0]   # First item (index 0)
second_student = study_hours[1]  # Second item (index 1)
last_student = study_hours[4]    # Last item (index 4)

print("First student's hours:", first_student)
print("Second student's hours:", second_student)
print("Last student's hours:", last_student)

# Python also allows negative indexing
also_last = study_hours[-1]   # -1 means last item
second_last = study_hours[-2] # -2 means second-to-last

print("\nUsing negative indices:")
print("Last item:", also_last)
print("Second-to-last:", second_last)

# Start with initial data
scores = [85, 90, 78]
print("Initial scores:", scores)

# Adding elements
scores.append(92)          # Add to end
print("After append:", scores)

scores.insert(1, 88)       # Insert at specific position
print("After insert:", scores)

# Removing elements
scores.remove(78)          # Remove specific value
print("After remove:", scores)

last_score = scores.pop()  # Remove and return last item
print("After pop:", scores)
print("Popped value:", last_score)

# Modifying elements
scores[0] = 95             # Change first element
print("After modification:", scores)
```

---

## Part 4: List Comprehensions - Elegant Data Processing

List comprehensions provide a concise way to create and transform lists. They're a hallmark of Pythonic code and essential for data processing.

### Exploration 4.1: From Loops to Comprehensions

First, see the traditional approach with loops:

```python exec
id: tutorial-06-lists-and-comprehensions-page-2-1
# Traditional loop approach
study_hours = [12, 15, 8, 20, 10]

# Calculate predicted scores using loop
predicted_scores_loop = []
for hours in study_hours:
    prediction = hours * 3.5 + 30
    predicted_scores_loop.append(prediction)

print("Using loop:", predicted_scores_loop)
```

Now see the list comprehension approach:

```python exec
id: tutorial-06-lists-and-comprehensions-page-2-2
# List comprehension approach - same result, one line!
predicted_scores = [hours * 3.5 + 30 for hours in study_hours]
print("Using comprehension:", predicted_scores)
```

### Structure of List Comprehensions:

```python
[expression for item in iterable]
```

- **expression**: What to do with each item
- **item**: Variable representing current item
- **iterable**: Collection to process (like a list)

### Exploration 4.2: Simple Transformations

```python exec
id: tutorial-06-lists-and-comprehensions-page-2-3
# Double each number
numbers = [1, 2, 3, 4, 5]
doubled = [num * 2 for num in numbers]
print("Doubled:", doubled)

# Square each number
squared = [num ** 2 for num in numbers]
print("Squared:", squared)

# Convert temperatures from Celsius to Fahrenheit
celsius = [0, 10, 20, 30, 40]
fahrenheit = [(temp * 9/5) + 32 for temp in celsius]
print("Fahrenheit:", fahrenheit)
```

### Your Turn: Transform Data

Practice writing list comprehensions for these transformations:

```python exec
id: tutorial-06-lists-and-comprehensions-page-2-4
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
prices = [10.99, 15.50, 8.75, 22.00, 5.25]

# Your code here:
# Use list comprehensions to create:
# 1. prices_with_tax: each price plus 20% tax
# 2. rounded_prices: each price rounded to nearest integer
# 3. discounted_prices: each price reduced by 10%
```

### Exploration 4.3: Comprehensions with Conditions

You can filter lists using conditions in comprehensions:

```python exec
id: tutorial-06-lists-and-comprehensions-page-2-5
scores = [85, 92, 48, 95, 67, 88, 55, 90]

# Get only passing scores (>= 50)
passing = [score for score in scores if score >= 50]
print("Passing scores:", passing)

# Get only high scores (>= 85)
high_scores = [score for score in scores if score >= 85]
print("High scores:", high_scores)

# Get even scores
even_scores = [score for score in scores if score % 2 == 0]
print("Even scores:", even_scores)
```

### Syntax with Conditions:

```python
[expression for item in iterable if condition]
```

Only items where the condition is True are included.

### Your Turn: Filtering Data

```python exec
id: tutorial-06-lists-and-comprehensions-page-2-6
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
study_hours = [5, 12, 8, 15, 3, 20, 10, 7, 18, 6]

# Your code here:
# Use list comprehensions to create:
# 1. sufficient_study: hours >= 10
# 2. low_study: hours < 8
# 3. doubled_sufficient: double each hour that is >= 10
```

### Exploration 4.4: Combining Transformation and Filtering

```python exec
id: tutorial-06-lists-and-comprehensions-page-2-7
# Apply transformation only to items meeting a condition
scores = [85, 92, 48, 95, 67, 88, 55, 90]

# Boost passing scores by 5 points
boosted_passing = [score + 5 for score in scores if score >= 50]
print("Boosted passing:", boosted_passing)

# Square only the high scores
squared_high = [score ** 2 for score in scores if score >= 85]
print("Squared high scores:", squared_high)
```

### Try this: Multiple Operations

Create a system that processes student data with multiple criteria:

```python exec
id: tutorial-06-lists-and-comprehensions-page-2-8
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
# Student study hours
hours = [12, 5, 15, 8, 20, 3, 18, 10]

# Your code here:
# Create three lists using comprehensions:
# 1. predictions: hours * 3.5 + 30 for all students
# 2. high_performers: predictions >= 80
# 3. need_support: original hours < 8
# Display results with clear labels
```

---

## Part 5: Working with Multiple Lists

Often, you need to process multiple related lists together. Python provides tools for this.

### Exploration 5.1: Parallel Lists

```python exec
id: tutorial-06-lists-and-comprehensions-page-2-9
# Related data in separate lists
names = ["Alice", "Bob", "Charlie", "Diana"]
hours = [12, 15, 8, 20]
scores = [85, 92, 78, 95]

# Process using indices
print("Student Analysis:")
for i in range(len(names)):
    print(f"{names[i]}: {hours[i]} hours -> score {scores[i]}")
```

### Exploration 5.2: The zip() Function

The `zip()` function pairs up elements from multiple lists:

```python exec
id: tutorial-06-lists-and-comprehensions-page-2-10
# Better approach using zip
names = ["Alice", "Bob", "Charlie", "Diana"]
hours = [12, 15, 8, 20]
scores = [85, 92, 78, 95]

print("Using zip():")
for name, hour, score in zip(names, hours, scores):
    print(f"{name}: {hour} hours -> score {score}")
```

### Your Turn: Calculate Individual Predictions

```python exec
id: tutorial-06-lists-and-comprehensions-page-2-11
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
student_names = ["Alice", "Bob", "Charlie", "Diana", "Eve"]
study_hours = [12, 15, 8, 20, 10]
attendance = [0.85, 0.90, 0.75, 0.95, 0.88]

# Your code here:
# For each student, calculate predicted score:
# prediction = (hours * 3.5) + (attendance * 20) + 30
# Display: "Name: prediction"
# Use zip() to process all three lists together
```

### Exploration 5.3: List Comprehensions with zip()

```python exec
id: tutorial-06-lists-and-comprehensions-page-2-12
# Combine list comprehensions with zip
hours = [12, 15, 8, 20, 10]
attendance = [0.85, 0.90, 0.75, 0.95, 0.88]

# Calculate predictions for all students in one line
predictions = [(h * 3.5) + (a * 20) + 30
               for h, a in zip(hours, attendance)]

print("All predictions:", predictions)
```

---

## Part 6: Nested Lists and Matrices

Lists can contain other lists, creating multi-dimensional structures. This is essential for understanding NumPy arrays.

### Exploration 6.1: Creating 2D Lists

```python exec
id: tutorial-06-lists-and-comprehensions-page-2-13
# Student data: [study_hours, attendance_rate, exam_score]
student_data = [
    [12, 0.85, 85],
    [15, 0.90, 92],
    [8, 0.75, 78],
    [20, 0.95, 95],
    [10, 0.88, 88]
]

print("All student data:")
print(student_data)

# Access individual student
first_student = student_data[0]
print("\nFirst student:", first_student)

# Access specific element
first_student_hours = student_data[0][0]
first_student_attendance = student_data[0][1]
print(f"First student: {first_student_hours} hours, {first_student_attendance} attendance")
```

### Exploration 6.2: Processing 2D Data

```python exec
id: tutorial-06-lists-and-comprehensions-page-2-14
# Process each student's data
print("Student Analysis:")
for i, student in enumerate(student_data):
    hours = student[0]
    attendance = student[1]
    score = student[2]

    prediction = (hours * 3.5) + (attendance * 20) + 30
    difference = score - prediction

    print(f"Student {i+1}:")
    print(f"  Predicted: {prediction:.1f}, Actual: {score}, Difference: {difference:.1f}")
```

### Your Turn: Extract Columns from 2D List

In machine learning, we often need to extract specific features (columns) from our dataset.

```python exec
id: tutorial-06-lists-and-comprehensions-page-2-15
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
# Student data: [hours, attendance, score]
data = [
    [12, 0.85, 85],
    [15, 0.90, 92],
    [8, 0.75, 78],
    [20, 0.95, 95],
    [10, 0.88, 88]
]

# Your code here:
# Use list comprehensions to extract:
# 1. all_hours: list of just the hours (first column)
# 2. all_attendance: list of just attendance (second column)
# 3. all_scores: list of just scores (third column)
# Hint: [row[0] for row in data] gets first column
```

### Exploration 6.3: Connection to NumPy

The nested lists you've been working with are similar to NumPy arrays. Soon you'll learn to use NumPy, which provides optimized operations for this kind of data:

```python exec
id: tutorial-06-lists-and-comprehensions-page-2-16
# This is what you'll do with NumPy soon:
# import numpy as np
# data_array = np.array(student_data)
# hours = data_array[:, 0]  # Get all rows, first column

# For now, understand that NumPy arrays are like lists,
# but with powerful mathematical operations built in

print("You've been preparing for NumPy arrays!")
print("The skills you learned here transfer directly.")
```

---

## Part 7: Practical Applications

### Project 7.1: Complete ML Prediction System

Build a complete system that collects data, processes it, and makes predictions.

```python exec
id: tutorial-06-lists-and-comprehensions-page-2-17
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
# Sample dataset
students = [
    {"name": "Alice", "hours": 12, "attendance": 0.85},
    {"name": "Bob", "hours": 15, "attendance": 0.90},
    {"name": "Charlie", "hours": 8, "attendance": 0.75},
    {"name": "Diana", "hours": 20, "attendance": 0.95},
    {"name": "Eve", "hours": 10, "attendance": 0.88}
]

# Your code here:
# 1. Extract hours and attendance into separate lists
# 2. Calculate predictions for all students (hours * 3.5 + attendance * 20 + 30)
# 3. Identify students who need support (prediction < 70)
# 4. Display comprehensive report showing:
#    - Each student's name and prediction
#    - Average predicted score
#    - Students needing support
#    - Students predicted to excel (>= 85)
```

### Project 7.2: Data Cleaning and Validation

Real datasets often contain errors. Practice filtering and cleaning data:

```python exec
id: tutorial-06-lists-and-comprehensions-page-2-18
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
# Raw data with some invalid entries
raw_scores = [85, -5, 92, 150, 78, 95, None, 88, 67, 200, 82]

# Your code here:
# 1. Remove invalid scores (None, negative, or > 100)
# 2. Calculate statistics on clean data (average, min, max)
# 3. Report how many scores were removed
# Use list comprehensions for filtering
```

### Project 7.3: Feature Engineering

Create new features from existing data - a crucial ML technique:

```python exec
id: tutorial-06-lists-and-comprehensions-page-2-19
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
# Original features
study_hours = [12, 15, 8, 20, 10, 18, 14]
attendance_rates = [0.85, 0.90, 0.75, 0.95, 0.88, 0.92, 0.82]

# Your code here:
# Create these new features using list comprehensions:
# 1. engagement_score: hours * attendance
# 2. consistency_flag: 1 if both hours >= 10 AND attendance >= 0.80, else 0
# 3. risk_level: "low" if engagement >= 10, "medium" if >= 7, else "high"
# Display all features in a clear format
```

---

## Reflection Questions

Consider your learning journey through this tutorial:

1. **How do lists make data processing more efficient than using individual variables?**
   
   (Your answer here)

2. **When would you choose a list comprehension over a traditional loop?**
   
   (Your answer here)

3. **How do the concepts in this tutorial prepare you for working with NumPy and pandas?**
   
   (Your answer here)

4. **What was the most challenging aspect of working with lists?**
   
   (Your answer here)

---

## Summary and Key Takeaways


### Lists Fundamentals
- Creating and accessing list elements
- Zero-based indexing and negative indices
- List methods: append, insert, remove, pop
- Useful functions: len, max, min, sum, sorted

### Slicing
- Basic slicing syntax: [start:end:step]
- Extracting subsets of data
- Reversing lists with [::-1]
- Creating training/test splits

### List Comprehensions
- Concise syntax for creating lists
- Transforming data with expressions
- Filtering with conditions
- Combining transformation and filtering

### Advanced Operations
- Working with parallel lists
- Using zip() for multiple iterables
- Nested lists and 2D data
- Feature extraction and engineering

### Connection to Machine Learning
- Storing datasets as lists
- Processing features systematically
- Data cleaning and validation
- Preparation for NumPy arrays

---

## Looking back

Before leaving this page, a sentence on each. What you write stays on this device.

```reflect
- Something you expected before running a cell that turned out differently
- The one idea from this page you could explain to someone else now
- Something you would change or try next, if there were time
- A question this page raised for you that it did not answer. Bring it to the next session; these questions are where the next session starts.
```

## Next Steps

Before continuing to Tutorial 7:
- [ ] Complete all practice exercises
- [ ] Write list comprehensions for at least 5 different problems
- [ ] Practice slicing with various ranges and steps
- [ ] Experiment with nested lists
- [ ] Review the connection between lists and NumPy

### In Tutorial 7, we'll explore:
- **Functions** - creating reusable code blocks
- **Parameter passing** and return values
- **Variable scope** and encapsulation
- **Building an ML prediction library**
- **Code organization** and modularity

---

## Additional Resources

- **Python List Documentation**: docs.python.org/3/tutorial/datastructures.html
- **List Comprehensions Guide**: realpython.com/list-comprehension-python
- **NumPy Quickstart**: numpy.org/doc/stable/user/quickstart.html
- **Practice Platform**: leetcode.com (lists and arrays problems)

---
