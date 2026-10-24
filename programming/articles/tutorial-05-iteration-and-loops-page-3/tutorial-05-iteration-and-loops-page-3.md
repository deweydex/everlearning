---
title: "tutorial-05-iteration-and-loops-page-3 (3 of 3)"
slug: tutorial-05-iteration-and-loops-page-3
course: programming-and-design-principles
course_title: "Programming and Design Principles"
series: tutorials
series_title: "Tutorials"
version: 2026.09.06.1
---

Before starting this page, run the cell below. It repeats the imports and definitions from the earlier pages that this page uses.

```python exec
id: tutorial-05-iteration-and-loops-page-3-setup
# Basic while loop
count = 1

while count <= 5:
    print(f"Iteration {count}")
    count = count + 1

print("Loop finished")

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

# Basic for loop
for i in range(1, 6):
    prediction = i * 3.5 + 30
    print(f"Student {i}: Predicted score = {prediction:.1f}")

print("All predictions complete")
```

---

## Part 6: Common Loop Patterns

### Pattern 1: Counting

Counting items that meet a condition:

```python exec
id: tutorial-05-iteration-and-loops-page-3-1
# Counting pattern
passing_count = 0

for i in range(1, 11):
    score = int(input(f"Enter score {i}: "))

    if score >= 50:
        passing_count = passing_count + 1

print(f"Number passing: {passing_count} out of 10")
percentage = (passing_count / 10) * 100
print(f"Pass rate: {percentage:.1f}%")
```

### Pattern 2: Searching

Finding if a value exists:

```python exec
id: tutorial-05-iteration-and-loops-page-3-2
# Searching pattern
target_score = 100
found = False

for i in range(1, 6):
    score = int(input(f"Enter score {i}: "))

    if score == target_score:
        found = True
        print(f"Perfect score found at position {i}!")
        break

if not found:
    print("No perfect scores")
```

### Pattern 3: Filtering

Processing only items that meet criteria:

```python exec
id: tutorial-05-iteration-and-loops-page-3-3
# Filtering pattern
high_performer_count = 0
high_performer_total = 0

for i in range(1, 11):
    score = int(input(f"Enter score {i}: "))

    # Only process scores above 80
    if score >= 80:
        high_performer_count = high_performer_count + 1
        high_performer_total = high_performer_total + score
        print(f"  High performer: {score}")

if high_performer_count > 0:
    average = high_performer_total / high_performer_count
    print(f"\nAverage of high performers: {average:.1f}")
else:
    print("\nNo high performers")
```

### Your Turn: Apply These Patterns

Create a program that processes study hours for 20 students and:
1. Counts how many study 15+ hours (exceptional)
2. Searches for anyone studying exactly 20 hours
3. Calculates average for those studying 10+ hours (meeting criteria)

Combine the three patterns:

```python exec
id: tutorial-05-iteration-and-loops-page-3-4
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
# Your combined pattern program:
```

---

## Part 7: Debugging Loops

### Common Loop Errors

### Error 1: Off-by-One Errors

Find what's wrong:

```python exec
id: tutorial-05-iteration-and-loops-page-3-5
# Intended: Process 10 students
for student in range(1, 10):
    score = int(input(f"Student {student}: "))
    print(f"Recorded score: {score}")
```

```python exec
id: tutorial-05-iteration-and-loops-page-3-6
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
# Your analysis:
# What's wrong:
#
# Why it's wrong:
#
# Your fix:
```

### Error 2: Wrong Variable in Loop

Find the bug:

```python exec
id: tutorial-05-iteration-and-loops-page-3-7
# Calculating squares
for i in range(1, 6):
    square = i * i
    print(f"{square} squared is {square}")
```

```python exec
id: tutorial-05-iteration-and-loops-page-3-8
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
# Your analysis:
# What's wrong:
#
# Your fix:
```

### Error 3: Accumulator Not Initialized

Find the problem:

```python exec
id: tutorial-05-iteration-and-loops-page-3-9
# Calculating total
for i in range(1, 6):
    number = int(input(f"Enter number {i}: "))
    total = total + number

print(f"Total: {total}")
```

```python exec
id: tutorial-05-iteration-and-loops-page-3-10
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
# Your analysis:
# What's wrong:
#
# Your fix:
```

### Debugging Technique: Adding Print Statements

```python exec
id: tutorial-05-iteration-and-loops-page-3-11
# Debugging with prints
total = 0
count = 0

print("Before loop: total =", total, "count =", count)

for i in range(1, 4):
    score = int(input(f"Score {i}: "))
    print(f"  Loop {i}: score = {score}")

    total = total + score
    count = count + 1
    print(f"  Loop {i}: total = {total}, count = {count}")

average = total / count
print(f"\nAfter loop: total = {total}, count = {count}")
print(f"Average: {average:.1f}")
```

### Your Turn: Debug This Program

This program has multiple errors. Find and fix them all:

```python exec
id: tutorial-05-iteration-and-loops-page-3-12
# Buggy program
passing = 0
failing = 0

for student in range(1, 5):
    score = int(input("Enter score: "))

    if score > 50:
        passing = passing + 1
    else:
        failing = passing + 1

total_students = passing + failing
print(f"Passing: {passing}")
print(f"Failing: {failing}")
print(f"Total: {total_students}")
```

```python exec
id: tutorial-05-iteration-and-loops-page-3-13
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
# Your analysis and fixes:
# Error 1:
#
# Error 2:
#
# Error 3:
#
# Your corrected version:
```

---

## Part 8: ML Application - Batch Processing

### Simulating Training Iterations

Machine learning models improve through multiple training iterations. Simulate this:

```python exec
id: tutorial-05-iteration-and-loops-page-3-14
# Simulating model training iterations
initial_accuracy = 0.60
accuracy = initial_accuracy
improvement_per_iteration = 0.03

print("Training Progress:")
print(f"Initial accuracy: {accuracy:.2%}")

for iteration in range(1, 11):
    # Simulate training improvement
    accuracy = accuracy + improvement_per_iteration

    # Accuracy can't exceed 100%
    if accuracy > 1.0:
        accuracy = 1.0

    print(f"Iteration {iteration}: {accuracy:.2%}")

    # Stop if we reach target accuracy
    if accuracy >= 0.90:
        print(f"Target accuracy reached in {iteration} iterations!")
        break

total_improvement = accuracy - initial_accuracy
print(f"\nTotal improvement: {total_improvement:.2%}")
```

### Your Turn: Batch Prediction System

Create a system that:
1. Processes predictions for multiple students in batches
2. For each student, collects study hours and attendance
3. Calculates prediction: (hours * 3) + (attendance * 20) + 30
4. Classifies each as: High (80+), Medium (65-79), Low (<65)
5. Tracks statistics for each category
6. Displays summary report

```python exec
id: tutorial-05-iteration-and-loops-page-3-15
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
# Your batch processing system:
```

---

## Part 9: Complete Project - Student Performance Analysis System

### Project Brief

Create a comprehensive student performance analysis system that demonstrates mastery of loops.

### Requirements:

Your program must:
1. Use a for loop to process data for multiple students
2. Use a while loop for input validation
3. Use nested loops for multiple data points per student
4. Implement the accumulator pattern
5. Use conditional logic within loops
6. Calculate and display multiple statistics
7. Use break or continue appropriately
8. Be well-commented and formatted

### Suggested Features:

- Process 5 students
- For each student, collect:
  - Study hours (validate 0-40)
  - Attendance rate (validate 0.0-1.0)
  - Previous score (validate 0-100)
- Calculate weighted prediction
- Classify each student
- Track overall statistics
- Generate summary report

### Planning:

```python exec
id: tutorial-05-iteration-and-loops-page-3-16
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
# Your project plan:
#
# Main loop structure:
#
#
# Validation loops needed:
#
#
# Variables to track:
#
#
# Calculations per student:
#
#
# Overall statistics:
#
#
```

### Implementation:

```python exec
id: tutorial-05-iteration-and-loops-page-3-17
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
# Your complete analysis system:
```

### Testing:

```python exec
id: tutorial-05-iteration-and-loops-page-3-18
# Test cases:
#
# Test 1: Normal data
#   Input:
#   Expected output:
#   Actual output:
#
# Test 2: Invalid inputs
#   Input:
#   Expected behavior:
#   Actual behavior:
#
# Test 3: Edge cases
#   Input:
#   Expected output:
#   Actual output:
#
```

### Reflection:

```python exec
id: tutorial-05-iteration-and-loops-page-3-19
# Project reflection:
#
# Which loop type was most useful?
#
#
# What was most challenging?
#
#
# How did you debug issues?
#
#
# What would you improve?
#
#
```

---

## Summary and Key Takeaways

In this tutorial, you explored:

### While Loops
- Condition-based repetition
- Loop variable initialization and update
- Input validation with loops
- Accumulator pattern
- Risk of infinite loops

### For Loops
- Counting with range()
- Iteration over sequences
- When to use for vs while
- Cleaner syntax for known iterations

### Nested Loops
- Loops within loops
- Processing multi-dimensional data
- Tracking variables across loop levels

### Loop Control
- break: exit loop early
- continue: skip to next iteration
- When to use each

### Common Patterns
- Counting items
- Searching for values
- Filtering data
- Accumulating totals
- Finding minimums/maximums

### Debugging
- Off-by-one errors
- Uninitialized accumulators
- Wrong loop variables
- Using print statements for debugging

### Connection to Machine Learning
- Batch processing of predictions
- Training iterations
- Data validation and cleaning
- Statistical analysis

---

## Next Steps

In Tutorials 6-7, you will explore:
- Functions and modularization
- Defining reusable code blocks
- Parameters and return values
- Variable scope
- Building ML prediction functions

---

## Self-Assessment Checklist

Before moving to the next tutorial, ensure you can:

- [ ] Write while loops with proper initialization and update
- [ ] Write for loops using range()
- [ ] Choose between for and while appropriately
- [ ] Implement the accumulator pattern
- [ ] Create nested loops
- [ ] Use break and continue correctly
- [ ] Apply counting pattern
- [ ] Apply searching pattern
- [ ] Apply filtering pattern
- [ ] Debug off-by-one errors
- [ ] Avoid infinite loops
- [ ] Trace loop execution
- [ ] Process multiple items with loops
- [ ] Validate input using loops
- [ ] Calculate statistics across datasets

If you cannot check all these boxes, review the relevant sections and practice more before continuing.

---

**End of Tutorial 5**

## Looking back

Before leaving this page, a sentence on each. What you write stays on this device.

```reflect
- Something you expected before running a cell that turned out differently
- The one idea from this page you could explain to someone else now
- Something you would change or try next, if there were time
- A question this page raised for you that it did not answer. Bring it to the next session; these questions are where the next session starts.
```
