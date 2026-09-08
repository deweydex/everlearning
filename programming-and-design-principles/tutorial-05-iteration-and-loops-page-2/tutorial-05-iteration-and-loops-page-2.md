---
title: "tutorial-05-iteration-and-loops-page-2 (2 of 3)"
slug: tutorial-05-iteration-and-loops-page-2
course: programming-and-design-principles
course_title: "Programming and Design Principles"
series: tutorials
series_title: "Tutorials"
version: 2026.09.06.1
---

Before starting this page, run the cell below. It repeats the imports and definitions from the earlier pages that this page uses.

```python exec
id: tutorial-05-iteration-and-loops-page-2-setup
# Basic while loop
count = 1

while count <= 5:
    print(f"Iteration {count}")
    count = count + 1

print("Loop finished")
```

---

## Part 3: For Loops - Iteration Over Sequences

### Exploration 3.1: Introducing the Range Function

Before learning for loops, understand the range() function:

```python exec
id: tutorial-05-iteration-and-loops-page-2-1
# Exploring range()
print("range(5):")
for number in range(5):
    print(number)

print("\nrange(1, 6):")
for number in range(1, 6):
    print(number)

print("\nrange(0, 10, 2):")
for number in range(0, 10, 2):
    print(number)
```

### Investigation:

Analyze the patterns:
1. What does range(5) produce?
2. What does range(1, 6) produce?
3. What does range(0, 10, 2) produce?
4. How many arguments can range() accept?
5. What does each argument control?

Write your findings:

```python exec
id: tutorial-05-iteration-and-loops-page-2-2
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
# Your analysis of range():
# range(5) produces:
#
# range(start, stop) produces:
#
# range(start, stop, step) produces:
#
# Important: Does range include the stop value?
#
```

### Exploration 3.2: Basic For Loops

Study this for loop structure:

```python exec
id: tutorial-05-iteration-and-loops-page-2-3
# Basic for loop
for i in range(1, 6):
    prediction = i * 3.5 + 30
    print(f"Student {i}: Predicted score = {prediction:.1f}")

print("All predictions complete")
```

### Comparison: For vs While

Compare this for loop to an equivalent while loop:

```python exec
id: tutorial-05-iteration-and-loops-page-2-4
# Equivalent while loop
i = 1
while i <= 5:
    prediction = i * 3.5 + 30
    print(f"Student {i}: Predicted score = {prediction:.1f}")
    i = i + 1

print("All predictions complete")
```

### Critical Thinking:

Which version do you prefer? Consider:
1. Which is easier to read?
2. Which is easier to write correctly?
3. Which is less prone to errors?
4. When would you choose one over the other?

Write your analysis:

```python exec
id: tutorial-05-iteration-and-loops-page-2-5
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
# Your comparison:
#
#
#
#
```

### Your Turn: Write For Loops

Create for loops for these tasks:

1. Print the numbers 1 to 10
2. Print the even numbers from 0 to 20
3. Count down from 10 to 1
4. Print the 5 times table (5, 10, 15, 20, 25)

Think carefully about the range() arguments:

```python exec
id: tutorial-05-iteration-and-loops-page-2-6
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
# Task 1: Numbers 1 to 10
# Your code:


# Task 2: Even numbers 0 to 20
# Your code:


# Task 3: Countdown from 10 to 1
# Your code:


# Task 4: Five times table
# Your code:
```

### Exploration 3.3: For Loops with Input and Accumulation

Combining for loops with the accumulator pattern:

```python exec
id: tutorial-05-iteration-and-loops-page-2-7
# Collecting and processing multiple inputs
total_hours = 0
passing_count = 0

for student_num in range(1, 6):
    hours = int(input(f"Enter study hours for student {student_num}: "))
    total_hours = total_hours + hours

    # Check if meets passing criteria
    if hours >= 10:
        passing_count = passing_count + 1

average_hours = total_hours / 5
print(f"\nTotal study hours: {total_hours}")
print(f"Average study hours: {average_hours:.1f}")
print(f"Students meeting criteria: {passing_count} out of 5")
```

### Your Turn: Statistics Calculator

Create a program that:
1. Asks for exam scores for 10 students
2. Calculates total, average, minimum, and maximum
3. Counts how many passed (score >= 50)
4. Displays all statistics

Plan your approach first:

```python exec
id: tutorial-05-iteration-and-loops-page-2-8
# Planning:
# What variables do I need?
#
# How do I initialize them?
#
# What happens inside the loop?
#
# What happens after the loop?
#
```

```python exec
id: tutorial-05-iteration-and-loops-page-2-9
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
# Your statistics calculator:
```

---

## Part 4: Nested Loops

### Exploration 4.1: Loops Within Loops

Sometimes you need to repeat something within a repetition. Study this pattern:

```python exec
id: tutorial-05-iteration-and-loops-page-2-10
# Simple nested loop
for week in range(1, 4):
    print(f"\nWeek {week}:")

    for day in range(1, 6):  # Days 1-5 (Mon-Fri)
        print(f"  Day {day}")
```

### Analysis:

1. How many times does the outer loop execute?
2. How many times does the inner loop execute per outer iteration?
3. How many times does the inner loop execute in total?
4. What gets printed?

Trace through manually:

```python exec
id: tutorial-05-iteration-and-loops-page-2-11
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
# Your trace:
# Outer loop iteration 1 (week=1):
#   Inner iterations: day=1, day=2, day=3, day=4, day=5
#
# Outer loop iteration 2 (week=2):
#   Inner iterations:
#
# Outer loop iteration 3 (week=3):
#   Inner iterations:
#
# Total inner iterations:
#
```

### Exploration 4.2: Practical Nested Loop Example

Processing data for multiple weeks and multiple students:

```python exec
id: tutorial-05-iteration-and-loops-page-2-12
# Weekly study hour tracker
total_all_weeks = 0

for week in range(1, 4):
    print(f"\nWeek {week}")
    week_total = 0

    for student in range(1, 4):
        hours = int(input(f"  Student {student} hours: "))
        week_total = week_total + hours

    week_average = week_total / 3
    print(f"  Week {week} average: {week_average:.1f} hours")
    total_all_weeks = total_all_weeks + week_total

overall_average = total_all_weeks / (3 * 3)  # 3 weeks, 3 students
print(f"\nOverall average: {overall_average:.1f} hours")
```

### Investigation:

Identify:
1. Which variables are used in the outer loop?
2. Which variables are used in the inner loop?
3. Which variable accumulates across all iterations?
4. Why is week_total initialized inside the outer loop?

Write your analysis:

```python exec
id: tutorial-05-iteration-and-loops-page-2-13
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
# Your analysis:
#
#
#
#
```

### Your Turn: Grade Processing System

Create a nested loop program that:
1. Processes grades for 3 classes
2. Each class has 4 students
3. For each class, calculates and displays the class average
4. Calculates and displays the overall average across all classes

Plan your nested structure:

```python exec
id: tutorial-05-iteration-and-loops-page-2-14
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
# Your nested loop program:
```

### Try this: Multiplication Table

Create a program that displays a multiplication table from 1 to 5:

```python exec
id: tutorial-05-iteration-and-loops-page-2-15
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
# Expected output:
# 1  2  3  4  5
# 2  4  6  8  10
# 3  6  9  12 15
# 4  8  12 16 20
# 5  10 15 20 25

# Your implementation:
```

---

## Part 5: Loop Control - Break and Continue

### Exploration 5.1: The break Statement

Sometimes you need to exit a loop early:

```python exec
id: tutorial-05-iteration-and-loops-page-2-16
# Using break to exit early
for i in range(1, 11):
    score = int(input(f"Enter score {i} (or -1 to stop): "))

    if score == -1:
        print("Stopping input early")
        break

    print(f"Recorded score: {score}")

print("Input complete")
```

### Investigation:

Test this program:
1. What happens when you enter -1 on the third input?
2. How many iterations execute?
3. Does the loop continue after break?

Write your findings:

```python exec
id: tutorial-05-iteration-and-loops-page-2-17
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
# Your findings on break:
#
#
#
```

### Exploration 5.2: The continue Statement

Continue skips the rest of the current iteration:

```python exec
id: tutorial-05-iteration-and-loops-page-2-18
# Using continue to skip iterations
valid_count = 0
total = 0

for i in range(1, 6):
    score = int(input(f"Enter score {i}: "))

    if score < 0 or score > 100:
        print("Invalid score - skipping")
        continue

    # This only executes for valid scores
    valid_count = valid_count + 1
    total = total + score
    print(f"Recorded score: {score}")

if valid_count > 0:
    average = total / valid_count
    print(f"\nAverage of {valid_count} valid scores: {average:.1f}")
else:
    print("\nNo valid scores entered")
```

### Comparison: break vs continue

Explain the difference:
- What does break do?
- What does continue do?
- When would you use each?

Write your explanation:

```python exec
id: tutorial-05-iteration-and-loops-page-2-19
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
# Your explanation:
# break:
#
# continue:
#
# When to use break:
#
# When to use continue:
#
```

### Your Turn: Input Processing with Control

Create a program that:
1. Processes up to 10 attendance rates
2. Allows the user to enter -1 to stop early (break)
3. Skips any values outside 0.0-1.0 (continue)
4. Calculates average of valid entries
5. Counts how many were valid

```python exec
id: tutorial-05-iteration-and-loops-page-2-20
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
# Your program:
```

## Looking back

Before leaving this page, a sentence on each. What you write stays on this device.

```reflect
- Something you expected before running a cell that turned out differently
- The one idea from this page you could explain to someone else now
- Something you would change or try next, if there were time
- A question this page raised for you that it did not answer. Bring it to the next session; these questions are where the next session starts.
```
