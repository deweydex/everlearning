---
title: "Tutorial 6: Lists and List Comprehensions (1 of 2)"
slug: tutorial-06-lists-and-comprehensions-page-1
course: programming-and-design-principles
course_title: "Programming and Design Principles"
series: tutorials
series_title: "Tutorials"
version: 2026.09.06.1
---

# Tutorial 6: Lists and List Comprehensions

**Module**: Programming & Design Principles 5N2927  
**Level**: QQI Level 5  
**Theme**: Machine Learning Datasets and Vectorization

---

## Introduction: Collections of Data

In previous tutorials, you worked with individual pieces of data - a single student's hours, one exam score, a single prediction. But machine learning systems need to process datasets containing hundreds or thousands of data points.

Consider a machine learning system that predicts student performance:
- It needs data from many students, not just one
- It must calculate statistics across all students
- It processes features for each student systematically
- It generates predictions for entire cohorts

Without lists, you would need hundreds of individual variables. Lists allow you to organize related data efficiently.

---

## Part 1: Understanding Lists

### What is a List?

A list is an ordered collection of items. Think of it as a container that can hold multiple values, each identified by its position.

### Exploration 1.1: Creating Your First Lists

Run this code and observe what happens:

```python exec
id: tutorial-06-lists-and-comprehensions-page-1-1
# Study hours for five students
study_hours = [12, 15, 8, 20, 10]

# Student names
student_names = ["Alice", "Bob", "Charlie", "Diana", "Eve"]

# Exam scores
exam_scores = [85, 92, 78, 95, 88]

print("Study hours:", study_hours)
print("Names:", student_names)
print("Scores:", exam_scores)
```

### Reflection Questions:

1. How does storing data in lists compare to using separate variables?
2. What patterns do you notice in how lists are created?
3. How might lists make data processing easier?

Write your thoughts below:

```python exec
id: tutorial-06-lists-and-comprehensions-page-1-2
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
# Your reflection:
#
#
#
```

### Exploration 1.2: Accessing List Elements

Each item in a list has a position called an **index**. Python uses zero-based indexing - the first item is at index 0.

```python exec
id: tutorial-06-lists-and-comprehensions-page-1-3
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
```

### Investigation: Why Zero-Based Indexing?

Many programming languages use zero-based indexing. What might be the advantages of this approach? Consider how computers store data in memory.

```python exec
id: tutorial-06-lists-and-comprehensions-page-1-4
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
# Your thoughts on zero-based indexing:
#
#
#
```

### Your Turn: Create and Access Lists

Create a list representing attendance rates for six students (as decimals like 0.85 for 85%). Then access and print specific elements.

```python exec
id: tutorial-06-lists-and-comprehensions-page-1-5
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
# Your code here:
# 1. Create a list called attendance_rates with six values
# 2. Print the first, middle, and last attendance rates
# 3. Print the second-to-last rate using negative indexing
```

---

## Part 2: List Operations and Methods

Lists are dynamic - you can modify them after creation. Python provides many built-in operations for working with lists.

### Exploration 2.1: Modifying Lists

```python exec
id: tutorial-06-lists-and-comprehensions-page-1-6
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

### Critical Thinking:

Notice how list methods like `append()`, `remove()`, and `pop()` modify the list directly. How is this different from mathematical operations that create new values?

```python exec
id: tutorial-06-lists-and-comprehensions-page-1-7
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
# Your analysis:
#
#
#
```

### Exploration 2.2: Useful List Functions

```python exec
id: tutorial-06-lists-and-comprehensions-page-1-8
exam_scores = [85, 92, 78, 95, 88, 90, 82]

# Get list information
num_students = len(exam_scores)    # Number of items
highest_score = max(exam_scores)   # Maximum value
lowest_score = min(exam_scores)    # Minimum value
total_score = sum(exam_scores)     # Sum of all values

print("Number of students:", num_students)
print("Highest score:", highest_score)
print("Lowest score:", lowest_score)
print("Total of all scores:", total_score)
print("Average score:", total_score / num_students)
```

### Your Turn: Statistics Calculator

You're creating a system to analyze study hours. Given a list of study hours, calculate and display meaningful statistics.

```python exec
id: tutorial-06-lists-and-comprehensions-page-1-9
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
weekly_study_hours = [12, 15, 8, 20, 10, 18, 14, 16, 11, 13]

# Your code here:
# Calculate:
# 1. Total number of students
# 2. Total study hours
# 3. Average study hours
# 4. Minimum and maximum hours
# 5. Range (max - min)
# Display all results with clear labels
```

### Exploration 2.3: Sorting and Reversing

```python exec
id: tutorial-06-lists-and-comprehensions-page-1-10
scores = [85, 92, 78, 95, 88]
print("Original:", scores)

# Create sorted copy (original unchanged)
sorted_scores = sorted(scores)
print("Sorted (ascending):", sorted_scores)
print("Original still:", scores)

# Sort in descending order
sorted_desc = sorted(scores, reverse=True)
print("Sorted (descending):", sorted_desc)

# Sort the list in place
scores.sort()
print("After .sort():", scores)
```

### Question for Investigation:

What's the difference between `sorted(list)` and `list.sort()`? When would you choose one over the other?

```python exec
id: tutorial-06-lists-and-comprehensions-page-1-11
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
# Your explanation:
#
#
#
```

---

## Part 3: Slicing Lists

Slicing allows you to extract portions of a list. This is powerful for analyzing subsets of data.

### Exploration 3.1: Basic Slicing

Slicing syntax: `list[start:end:step]`
- `start`: First index to include (inclusive)
- `end`: First index to exclude (exclusive)
- `step`: How many items to skip (optional)

```python exec
id: tutorial-06-lists-and-comprehensions-page-1-12
scores = [85, 92, 78, 95, 88, 90, 82, 86]
print("Complete list:", scores)

# Get first three scores
first_three = scores[0:3]    # Indices 0, 1, 2
print("First three:", first_three)

# Get scores from index 2 to end
from_third = scores[2:]      # Start at 2, go to end
print("From third onward:", from_third)

# Get scores up to (but not including) index 5
up_to_fifth = scores[:5]     # Start at beginning, stop before 5
print("Up to fifth:", up_to_fifth)

# Get middle section
middle = scores[2:6]         # Indices 2, 3, 4, 5
print("Middle section:", middle)

# Get last three
last_three = scores[-3:]     # Last three items
print("Last three:", last_three)
```

### Exploration 3.2: Using Step in Slicing

```python exec
id: tutorial-06-lists-and-comprehensions-page-1-13
data = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# Get every second element
every_other = data[::2]
print("Every other:", every_other)

# Get every third element
every_third = data[::3]
print("Every third:", every_third)

# Reverse the list
reversed_data = data[::-1]
print("Reversed:", reversed_data)

# Get every second element from index 1 to 7
subset = data[1:7:2]
print("Subset with step:", subset)
```

### Your Turn: Slicing Practice

Given a list of exam scores, use slicing to extract specific subsets.

```python exec
id: tutorial-06-lists-and-comprehensions-page-1-14
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
exam_scores = [67, 89, 92, 78, 85, 95, 73, 88, 91, 82, 76, 90]

# Your code here:
# 1. Get the top 5 scores (hint: sort first!)
# 2. Get the bottom 3 scores
# 3. Get every other score starting from the first
# 4. Get scores from index 3 to index 8
# 5. Create a reversed version of the list
```

### Application: Training and Test Sets

In machine learning, we often split data into training and test sets. Practice this important technique:

```python exec
id: tutorial-06-lists-and-comprehensions-page-1-15
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
# Complete dataset
all_scores = [85, 92, 78, 95, 88, 90, 82, 86, 91, 87]

# Your code here:
# Split into:
# - training_set: first 70% of data (7 items)
# - test_set: remaining 30% (3 items)
# Print both sets
```

## What we set out to do

These were the aims of this notebook. Now that you have worked through it, they are a check on what happened rather than a promise about it.

- Understand and implement data structures for storing collections (LO 4)
- Develop documented programs that process multiple related data items (LO 7)
- Apply procedural syntax including list operations and comprehensions (LO 4)
- Follow coding standards for writing clean, Pythonic code (LO 11)
- Prepare for working with NumPy arrays in machine learning

---

## Looking back

Before leaving this page, a sentence on each. What you write stays on this device.

```reflect
- Something you expected before running a cell that turned out differently
- The one idea from this page you could explain to someone else now
- Something you would change or try next, if there were time
- A question this page raised for you that it did not answer. Bring it to the next session; these questions are where the next session starts.
```
