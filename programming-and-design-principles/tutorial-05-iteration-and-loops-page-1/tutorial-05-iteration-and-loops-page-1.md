---
title: "Tutorial 5: Iteration and Loops (1 of 3)"
slug: tutorial-05-iteration-and-loops-page-1
course: programming-and-design-principles
course_title: "Programming and Design Principles"
series: tutorials
series_title: "Tutorials"
version: 2026.09.06.1
---

# Tutorial 5: Iteration and Loops

**Module**: Programming & Design Principles 5N2927  
**Level**: QQI Level 5  
**Theme**: Machine Learning Batch Processing and Training Iterations

---

## Introduction: Repetition in Programs

In previous tutorials, you learned to make decisions with conditional statements. However, these programs still execute each section of code only once. Real programs often need to repeat operations multiple times.

Consider a machine learning system that needs to:
- Process predictions for 100 students
- Train a model through multiple iterations
- Validate input until it's correct
- Calculate statistics across a dataset

Without loops, you would need to write the same code hundreds or thousands of times. Iteration allows you to repeat operations efficiently.

---

## Part 1: The Need for Repetition

### Exploration 1.1: The Problem with Repetitive Code

Imagine you need to calculate predictions for 5 students. Without loops, you might write:

```python exec
id: tutorial-05-iteration-and-loops-page-1-1
# Calculating predictions without loops - tedious and error-prone
student1_hours = 12
student1_prediction = student1_hours * 3.5 + 30
print(f"Student 1 prediction: {student1_prediction}")

student2_hours = 15
student2_prediction = student2_hours * 3.5 + 30
print(f"Student 2 prediction: {student2_prediction}")

student3_hours = 8
student3_prediction = student3_hours * 3.5 + 30
print(f"Student 3 prediction: {student3_prediction}")

# And so on...
```

### Critical Thinking Questions:

1. What problems do you see with this approach?
2. What would happen if you needed to change the prediction formula?
3. How would you handle 100 students? 1000 students?
4. What if you didn't know in advance how many students there would be?

Write your analysis:

```python exec
id: tutorial-05-iteration-and-loops-page-1-2
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
# Your analysis of repetitive code problems:
#
#
#
#
```

### The Solution: Loops

Loops allow you to repeat a block of code multiple times. Python provides two main types:
- **while loops**: Repeat while a condition is true
- **for loops**: Repeat for each item in a sequence

---

## Part 2: While Loops - Condition-Based Repetition

### Exploration 2.1: Your First While Loop

Study the structure of this while loop:

```python exec
id: tutorial-05-iteration-and-loops-page-1-3
# Basic while loop
count = 1

while count <= 5:
    print(f"Iteration {count}")
    count = count + 1

print("Loop finished")
```

### Structural Analysis:

Identify these components:
1. The loop variable (initialized before the loop)
2. The while keyword
3. The condition
4. The colon
5. The indented loop body
6. The update statement (changes the loop variable)

### Investigation: What Happens Step by Step?

Trace through this loop manually. For each iteration, record:
- The value of count
- Whether the condition is true or false
- What gets printed

```python exec
id: tutorial-05-iteration-and-loops-page-1-4
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
# Your trace:
# Before loop: count =
#
# Iteration 1: count = , condition = , output =
# Iteration 2: count = , condition = , output =
# Iteration 3: count = , condition = , output =
# Iteration 4: count = , condition = , output =
# Iteration 5: count = , condition = , output =
# After loop: count = , condition =
#
```

### Critical Concept: The Update Statement

What would happen if you forgot to update the loop variable? Try it:

```python exec
id: tutorial-05-iteration-and-loops-page-1-5
# WARNING: This will create an infinite loop!
# Uncomment carefully and be ready to interrupt

# count = 1
# while count <= 5:
#     print(f"Iteration {count}")
#     # Missing: count = count + 1
```

### Question:

Why does forgetting the update statement create an infinite loop? What does this tell you about how while loops work?

```python exec
id: tutorial-05-iteration-and-loops-page-1-6
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
# Your explanation:
#
#
#
```

### Your Turn: Write a Simple While Loop

Create a while loop that:
1. Starts at 10
2. Counts down to 1
3. Prints each number
4. Prints "Liftoff!" after the loop ends

Think about:
- Initial value
- Condition
- Update (increment or decrement?)

```python exec
id: tutorial-05-iteration-and-loops-page-1-7
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
# Your countdown loop:
# Add comments explaining your choices
```

### Exploration 2.2: While Loops for Input Validation

A common use of while loops is repeating until valid input is received:

```python exec
id: tutorial-05-iteration-and-loops-page-1-8
# Input validation with while loop
score = -1  # Initialize with invalid value

while score < 0 or score > 100:
    score = int(input("Enter a score (0-100): "))

    if score < 0 or score > 100:
        print("Invalid score. Please try again.")

print(f"Valid score entered: {score}")
```

### Analysis:

1. Why is score initialized to -1?
2. What would happen if the user enters 150? Trace through the loop.
3. When does the loop end?

Write your analysis:

```python exec
id: tutorial-05-iteration-and-loops-page-1-9
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
# Your analysis:
#
#
#
```

### Your Turn: Validate Attendance Rate

Create a while loop that repeatedly asks for an attendance rate until the user enters a valid value (between 0.0 and 1.0). Include helpful error messages.

```python exec
id: tutorial-05-iteration-and-loops-page-1-10
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
# Your validation loop:
# Add comments explaining the logic
```

### Exploration 2.3: Accumulator Pattern

A fundamental programming pattern uses loops to accumulate a result:

```python exec
id: tutorial-05-iteration-and-loops-page-1-11
# Accumulator pattern: calculating total
total = 0
count = 1

while count <= 5:
    study_hours = int(input(f"Enter study hours for student {count}: "))
    total = total + study_hours
    count = count + 1

average = total / 5
print(f"Total study hours: {total}")
print(f"Average study hours: {average:.1f}")
```

### Investigation:

Trace through this program with sample inputs. Track the values of:
- count
- study_hours
- total

After each iteration:

```python exec
id: tutorial-05-iteration-and-loops-page-1-12
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
# Your trace (assume inputs: 10, 12, 8, 15, 14):
# Before loop: count = , total =
#
# Iteration 1: count = , study_hours = , total =
# Iteration 2: count = , study_hours = , total =
# Iteration 3: count = , study_hours = , total =
# Iteration 4: count = , study_hours = , total =
# Iteration 5: count = , study_hours = , total =
#
# Final: total = , average =
#
```

### Your Turn: Find Maximum Value

Create a program that:
1. Asks for 5 test scores
2. Finds and displays the highest score
3. Calculates and displays the average

Hint: You'll need variables for count, total, and maximum.

```python exec
id: tutorial-05-iteration-and-loops-page-1-13
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
# Your maximum finder:
# Think about:
# - How to initialize the maximum variable
# - When to update it
# - How to track the total simultaneously
```

## What we set out to do

These were the aims of this notebook. Now that you have worked through it, they are a check on what happened rather than a promise about it.

- Understand and implement iteration control structures including loops (LO 6)
- Develop documented programs that process multiple items of data (LO 7)
- Apply iteration to solve real-world problems (LO 2)
- Debug programs with loops (LO 9, LO 10)
- Follow coding standards in iterative structures (LO 11)

---

## Looking back

Before leaving this page, a sentence on each. What you write stays on this device.

```reflect
- Something you expected before running a cell that turned out differently
- The one idea from this page you could explain to someone else now
- Something you would change or try next, if there were time
- A question this page raised for you that it did not answer. Bring it to the next session; these questions are where the next session starts.
```
