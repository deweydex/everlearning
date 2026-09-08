---
title: "tutorial-02-algorithms-and-problem-solving-page-2 (2 of 3)"
slug: tutorial-02-algorithms-and-problem-solving-page-2
course: programming-and-design-principles
course_title: "Programming and Design Principles"
series: tutorials
series_title: "Tutorials"
version: 2026.09.06.1
---

Before starting this page, run the cell below. It repeats the imports and definitions from the earlier pages that this page uses.

```python exec
id: tutorial-02-algorithms-and-problem-solving-page-2-setup
# Sequential Problem Solving: Grade Calculator

print("=== Student Grade Calculator ===")
print("Demonstrating Sequential Problem Solving")
print("=" * 40)
print()

# STEP 1: Understand and define the problem
print("STEP 1: Problem Definition")
print("Calculate average and grade from 3 exam scores")
print("Input: 3 scores (0-100)")
print("Output: Average and grade category")
print()

# STEP 2: Get input data
print("STEP 2: Input Data")
exam1 = 75
exam2 = 82
exam3 = 68
print(f"Exam 1: {exam1}")
print(f"Exam 2: {exam2}")
print(f"Exam 3: {exam3}")
print()

# STEP 3: Process - Calculate average
print("STEP 3: Process - Calculate Average")
total = exam1 + exam2 + exam3
average = total / 3
print(f"Total: {exam1} + {exam2} + {exam3} = {total}")
print(f"Average: {total} / 3 = {average:.2f}")
print()

# STEP 4: Process - Determine grade
print("STEP 4: Process - Determine Grade Category")
if average >= 80:
    grade = "Distinction"
    print(f"{average:.2f} >= 80: Distinction")
elif average >= 65:
    grade = "Merit"
    print(f"{average:.2f} >= 65: Merit")
elif average >= 50:
    grade = "Pass"
    print(f"{average:.2f} >= 50: Pass")
else:
    grade = "Fail"
    print(f"{average:.2f} < 50: Fail")
print()

# STEP 5: Output results
print("STEP 5: Output Final Results")
print("=" * 40)
print(f"Student's Average: {average:.2f}%")
print(f"Grade Category: {grade}")
print("=" * 40)
print()
print("✓ Sequential solving: One clear step at a time!")

# Implementation of Number Doubler pseudocode
number = 15
result = number * 2
print("Result:", result)
```

## Part 4: Flowcharts - Visual Algorithms

### What is a Flowchart?

A **flowchart** is:
- Visual representation of an algorithm
- Uses standard shapes and arrows
- Shows flow of control
- Alternative to pseudocode

### Standard Flowchart Symbols

```
┌─────────┐
│ START │ ← Oval: Start/End
│ END │
└─────────┘

┌──────────────┐
│ Process │ ← Rectangle: Process/Action
│ statement │
└──────────────┘

 ╱────╲
 ╱ Deci ╲ ← Diamond: Decision (if/then)
 ╱ sion ╲
 ╱────────╲

 ╱────────────╲
│ Input or │ ← Parallelogram: Input/Output
│ Output │
 ╲────────────╱

 ↓
 → ← Arrows: Flow direction
```

### Example 1: Simple Number Check

**Problem**: Check if a number is positive, negative, or zero

**Text Flowchart:**
```
 START
 ↓
 [INPUT number]
 ↓
 ╱ number > 0? ╲
 YES↙ ↘NO
 ↓ ↓
[PRINT ╱ number < 0? ╲
"Positive"] YES↙ ↘NO
 ↓ ↓ ↓
 ↓ [PRINT [PRINT
 ↓ "Negative"] "Zero"]
 ↓ ↓ ↓
 └───────────┴─────────────┘
 ↓
 END
```

**Python Implementation:**

```python exec
id: tutorial-02-algorithms-and-problem-solving-page-2-1
# Implementation of Number Check flowchart

number = -5

if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")
```

### Example 2: Grade Calculator Flowchart

**Text Flowchart:**
```
                START
                  ↓
       [INPUT exam1, exam2, exam3]
                  ↓
         [total = exam1 + exam2 + exam3]
                  ↓
         [average = total / 3]
                  ↓
          ╱ average >= 80? ╲
        YES↙              ↘NO
          ↓                 ↓
    [grade =          ╱ average >= 65? ╲
    "Distinction"]  YES↙              ↘NO
          ↓            ↓                 ↓
          ↓      [grade =          ╱ average >= 50? ╲
          ↓       "Merit"]       YES↙              ↘NO
          ↓            ↓            ↓                 ↓
          ↓            ↓      [grade =          [grade =
          ↓            ↓       "Pass"]           "Fail"]
          ↓            ↓            ↓                 ↓
          └────────────┴────────────┴─────────────────┘
                               ↓
                    [OUTPUT average, grade]
                               ↓
                             END
```

### Example 3: ML Predictor Flowchart

**Text Flowchart:**
```
                    START
                      ↓
        [INPUT study_hours, attendance]
                      ↓
    [score = (study_hours * 10) + (attendance * 0.5)]
                      ↓
              ╱ score >= 80? ╲
            YES↙            ↘NO
              ↓               ↓
        [prediction =    ╱ score >= 60? ╲
        "Pass with      YES↙           ↘NO
        Distinction"]    ↓               ↓
              ↓      [prediction =  [prediction =
              ↓       "Pass"]        "At Risk"]
              ↓           ↓               ↓
              └───────────┴───────────────┘
                          ↓
              [OUTPUT score, prediction]
                          ↓
                        END
```

### When to Use Flowcharts vs Pseudocode

**Use Flowcharts When:**
- Complex decision logic
- Need to show to non-programmers
- Visual learner
- Documenting existing code

**Use Pseudocode When:**
- Detailed algorithm design
- Working with other programmers
- Closer to actual coding
- Easier to type/share

**Many professionals use BOTH!**

---

## Part 5: Data Dictionaries

### What is a Data Dictionary?

A **data dictionary** documents:
- All variables in your program
- Their data types
- Their purpose
- Example values

### Why Use Data Dictionaries?

 Planning tool - Think before coding 
 Documentation - Others understand your code 
 Debugging aid - Track variable usage 
 Professional practice - Industry standard 

### Example: Grade Calculator Data Dictionary

| Variable Name | Data Type | Purpose | Example Value |
|--------------|-----------|---------|---------------|
| exam1 | Integer | First exam score (0-100) | 75 |
| exam2 | Integer | Second exam score (0-100) | 82 |
| exam3 | Integer | Third exam score (0-100) | 68 |
| total | Integer | Sum of all exam scores | 225 |
| average | Float | Average of three exams | 75.0 |
| grade | String | Grade category | "Merit" |

### Example: ML Predictor Data Dictionary

| Variable Name | Data Type | Purpose | Example Value |
|--------------|-----------|---------|---------------|
| study_hours | Integer | Weekly study hours | 6 |
| attendance_percentage | Integer | Class attendance % (0-100) | 85 |
| score | Float | Calculated prediction score | 102.5 |
| prediction | String | Prediction result | "Likely to Pass" |

### Creating Your Data Dictionary

**Steps:**
1. List all variables you'll need
2. Determine data type for each
3. Write clear purpose statement
4. Provide example value

**Python Data Types:**
- `int` - Whole numbers (42, -5, 0)
- `float` - Decimal numbers (3.14, -0.5, 100.0)
- `str` - Text/strings ("Hello", 'Python')
- `bool` - True/False values

Let's see data types in action:

**A question before moving on.** This program makes a judgement about a person. Who chose the threshold, and what happens to the person just on the wrong side of it? What does the program not know about them? What would you want said to them? Write a sentence or two; there is no right answer, and the question is the point.

```python exec
id: tutorial-02-algorithms-and-problem-solving-page-2-2
# Demonstrating data types from our data dictionary

print("=== Data Dictionary in Action ===")
print()

# Integer variables
exam1 = 75
exam2 = 82
print(f"exam1 = {exam1}, type: {type(exam1)}")
print(f"exam2 = {exam2}, type: {type(exam2)}")
print()

# Float variable
average = 75.5
print(f"average = {average}, type: {type(average)}")
print()

# String variable
grade = "Merit"
print(f"grade = '{grade}', type: {type(grade)}")
print()

# Boolean variable
passed = True
print(f"passed = {passed}, type: {type(passed)}")
print()

print("Choosing correct data types is crucial!")
```

---

## Part 6: Complete Algorithm Design Example

### Problem: BMI Calculator with Health Advice

**Problem Statement:**
Create a Body Mass Index (BMI) calculator that provides health category advice.

**Requirements:**
- Input: Weight (kg) and Height (m)
- Calculate: BMI = weight / (height²)
- Output: BMI value and category
- Categories:
 - Underweight: BMI < 18.5
 - Normal: 18.5 ≤ BMI < 25
 - Overweight: 25 ≤ BMI < 30
 - Obese: BMI ≥ 30

### Step 1: Data Dictionary

| Variable Name | Data Type | Purpose | Example Value |
|--------------|-----------|---------|---------------|
| weight | Float | Person's weight in kg | 70.5 |
| height | Float | Person's height in meters | 1.75 |
| bmi | Float | Calculated BMI value | 23.02 |
| category | String | Health category | "Normal" |

### Step 2: Pseudocode

```
START
    // Input Section
    INPUT weight (in kilograms)
    INPUT height (in meters)
    
    // Processing - Calculate BMI
    SET bmi = weight / (height * height)
    
    // Decision Logic - Determine Category
    IF bmi < 18.5 THEN
        SET category = "Underweight"
    ELSE IF bmi < 25 THEN
        SET category = "Normal"
    ELSE IF bmi < 30 THEN
        SET category = "Overweight"
    ELSE
        SET category = "Obese"
    END IF
    
    // Output Section
    OUTPUT "BMI:", bmi
    OUTPUT "Category:", category
END
```

### Step 3: Flowchart

```
                    START
                      ↓
            [INPUT weight, height]
                      ↓
          [bmi = weight / (height²)]
                      ↓
              ╱ bmi < 18.5? ╲
            YES↙           ↘NO
              ↓              ↓
        [category =    ╱ bmi < 25? ╲
        "Underweight"] YES↙        ↘NO
              ↓         ↓             ↓
              ↓    [category =   ╱ bmi < 30? ╲
              ↓     "Normal"]  YES↙        ↘NO
              ↓         ↓        ↓             ↓
              ↓         ↓   [category =   [category =
              ↓         ↓   "Overweight"]  "Obese"]
              ↓         ↓        ↓             ↓
              └─────────┴────────┴─────────────┘
                         ↓
              [OUTPUT bmi, category]
                         ↓
                       END
```

### Step 4: Python Implementation

```python exec
id: tutorial-02-algorithms-and-problem-solving-page-2-3
# BMI Calculator - Complete Implementation
# Following our design: Data Dictionary → Pseudocode → Code

print("=== BMI Calculator with Health Advice ===")
print()

# Input Section
weight = 70.5  # kg
height = 1.75  # meters

print(f"Weight: {weight} kg")
print(f"Height: {height} m")
print()

# Processing - Calculate BMI
bmi = weight / (height * height)
print(f"Calculating: {weight} / ({height} × {height})")
print(f"BMI: {bmi:.2f}")
print()

# Decision Logic - Determine Category
if bmi < 18.5:
    category = "Underweight"
elif bmi < 25:
    category = "Normal"
elif bmi < 30:
    category = "Overweight"
else:
    category = "Obese"

# Output Section
print("=" * 40)
print(f"Your BMI: {bmi:.2f}")
print(f"Category: {category}")
print("=" * 40)
print()
print("✓ Algorithm successfully implemented!")
```

### Design Process Review

Notice how we followed the professional process:

1. **Understood the problem** - Clear requirements
2. **Created data dictionary** - Planned variables
3. **Wrote pseudocode** - Designed logic
4. **Drew flowchart** - Visualized flow
5. **Implemented code** - Translated to Python

**This is how professionals work!**

---

## Looking back

Before leaving this page, a sentence on each. What you write stays on this device.

```reflect
- Something you expected before running a cell that turned out differently
- The one idea from this page you could explain to someone else now
- Something you would change or try next, if there were time
- A question this page raised for you that it did not answer. Bring it to the next session; these questions are where the next session starts.
```
