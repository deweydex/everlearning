---
title: "Tutorial 2: Algorithms & Problem Solving (1 of 3)"
slug: tutorial-02-algorithms-and-problem-solving-page-1
course: programming-and-design-principles
course_title: "Programming and Design Principles"
series: tutorials
series_title: "Tutorials"
version: 2026.09.06.1
---

# Tutorial 2: Algorithms & Problem Solving

## What You'll Learn
- What algorithms are and why they matter
- Sequential problem-solving methodology
- How to write clear pseudocode
- How to create flowcharts
- Data dictionaries and documentation
- Building ML prediction algorithms from scratch

---

## Part 1: Understanding Algorithms

### What is an Algorithm?

An **algorithm** is:
- A step-by-step procedure to solve a problem
- A recipe for accomplishing a task
- A finite sequence of well-defined instructions
- The **blueprint** before writing code

### Why Design Before Coding?

**Bad Approach:**
```
Problem → Code → Debug → More Debug → Eventually Works?
```

**Good Approach:**
```
Problem → Algorithm → Code → Works First Time!
```

**Professional developers spend more time designing than coding!**

### Real-World Algorithm Examples

#### Making Tea (Everyday Algorithm)
1. Fill kettle with water
2. Boil water
3. Place tea bag in cup
4. Pour hot water into cup
5. Wait 3-5 minutes
6. Remove tea bag
7. Add milk (if desired)
8. Add sugar (if desired)
9. Stir
10. Enjoy!

**Notice**: Clear, sequential, unambiguous steps

#### Finding Maximum Number
Let's see this in action:

```python exec
id: tutorial-02-algorithms-and-problem-solving-page-1-1
# Algorithm: Find the largest of three numbers

print("=== Finding Largest Number ===")
print()

# Input
num1 = 45
num2 = 67
num3 = 23

print("Numbers:", num1, num2, num3)
print()

# Algorithm steps
print("Algorithm Steps:")
print("1. Assume first number is largest")
largest = num1
print(f"   Currently largest = {largest}")
print()

print("2. Compare with second number")
if num2 > largest:
    largest = num2
    print(f"   Found larger: {largest}")
else:
    print(f"   No change: {largest} still largest")
print()

print("3. Compare with third number")
if num3 > largest:
    largest = num3
    print(f"   Found larger: {largest}")
else:
    print(f"   No change: {largest} still largest")
print()

# Output
print(f"Result: Largest number is {largest}")
```

### Properties of Good Algorithms

1. **Clear Instructions**: Each step is unambiguous
2. **Finite**: Will eventually complete (no infinite loops)
3. **Well-defined Input**: Knows what data it needs
4. **Well-defined Output**: Produces expected result
5. **Effective**: Each step can actually be performed
6. **Efficient**: Solves problem in reasonable time

---

## Part 2: Sequential Problem Solving

### The Development Cycle

Professional software development follows these steps:

```
1. UNDERSTAND THE PROBLEM
 ↓
2. DESIGN THE SOLUTION
 - Algorithm (pseudocode or flowchart)
 - Data dictionary
 ↓
3. CODE THE SOLUTION
 - Implement in programming language
 ↓
4. TEST THE SOLUTION
 - Develop test data
 - Run tests
 - Debug if needed
 ↓
5. REFINE AND DOCUMENT
 - Add comments
 - Improve efficiency
 - Document decisions
```

### Step 1: Understand the Problem

**Ask These Questions:**
- What are the inputs?
- What are the outputs?
- What are the requirements?
- What are the constraints?
- Are there edge cases (unusual scenarios)?

### Example Problem: Student Grade Calculator

**Problem Statement:**
Create a program that calculates a student's average score from three exams and determines their grade category.

**Requirements Analysis:**
- **Inputs**: Three exam scores (0-100)
- **Processing**: Calculate average
- **Output**: Average score and grade category
- **Rules**: 
 - Distinction: 80-100
 - Merit: 65-79
 - Pass: 50-64 
 - Fail: 0-49
- **Edge Cases**: What if score > 100 or < 0?

Let's solve this step by step:

```python exec
id: tutorial-02-algorithms-and-problem-solving-page-1-2
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
```

### Why Sequential Thinking Matters

**Benefits:**
- Breaks complex problems into manageable steps
- Easier to debug (know which step failed)
- Can test each step individually
- Others can understand your logic
- Foundation for all programming

**In Machine Learning:**
- Data collection → Data cleaning → Model training → Prediction → Evaluation
- Each step depends on the previous one
- Sequential thinking is essential!

---

## Part 3: Pseudocode - Planning Your Programs

### What is Pseudocode?

**Pseudocode** is:
- An informal description of an algorithm
- Written in plain English (or your language)
- Uses programming-like structure
- **Not** actual code (won't run on computer)
- A **planning tool** before coding

### Why Use Pseudocode?

1. **Focus on logic, not syntax** - 
2. **Language independent** - Can implement in any language
3. **Easy to modify** - Change logic before coding
4. **Communication tool** - Discuss with team
5. **Documentation** - Explains what code should do

### Pseudocode Conventions

Common keywords and structures:

```
START / END - Beginning and end of algorithm
INPUT / READ - Getting user input
OUTPUT / PRINT / DISPLAY - Showing results
SET / ASSIGN - Setting variable values
IF...THEN...ELSE - Conditional logic
WHILE / FOR - Loops
```

### Example 1: Simple Number Doubler

**Pseudocode:**
```
START
    INPUT number
    SET result = number * 2
    OUTPUT result
END
```

**Python Implementation:**

```python exec
id: tutorial-02-algorithms-and-problem-solving-page-1-3
# Implementation of Number Doubler pseudocode
number = 15
result = number * 2
print("Result:", result)
```

### Example 2: Grade Calculator (Full Pseudocode)

**Pseudocode:**
```
START
    // Input Section
    INPUT exam1
    INPUT exam2
    INPUT exam3
    
    // Processing Section
    SET total = exam1 + exam2 + exam3
    SET average = total / 3
    
    // Decision Logic
    IF average >= 80 THEN
        SET grade = "Distinction"
    ELSE IF average >= 65 THEN
        SET grade = "Merit"
    ELSE IF average >= 50 THEN
        SET grade = "Pass"
    ELSE
        SET grade = "Fail"
    END IF
    
    // Output Section
    OUTPUT "Average:", average
    OUTPUT "Grade:", grade
END
```

**Python Implementation:**

```python exec
id: tutorial-02-algorithms-and-problem-solving-page-1-4
# Implementation of Grade Calculator pseudocode

# Input Section
exam1 = 85
exam2 = 78
exam3 = 92

# Processing Section
total = exam1 + exam2 + exam3
average = total / 3

# Decision Logic
if average >= 80:
    grade = "Distinction"
elif average >= 65:
    grade = "Merit"
elif average >= 50:
    grade = "Pass"
else:
    grade = "Fail"

# Output Section
print("Average:", average)
print("Grade:", grade)
```

### Example 3: ML Prediction Algorithm

**Problem**: Predict if a student will pass based on study hours and attendance.

**Pseudocode:**
```
START
    // Our "trained model" rules (expert system)
    
    INPUT study_hours
    INPUT attendance_percentage
    
    // Calculate prediction score
    SET score = (study_hours * 10) + (attendance_percentage * 0.5)
    
    // Make prediction based on score
    IF score >= 80 THEN
        SET prediction = "Likely to Pass with Distinction"
    ELSE IF score >= 60 THEN
        SET prediction = "Likely to Pass"
    ELSE
        SET prediction = "At Risk - Need More Study"
    END IF
    
    OUTPUT "Prediction Score:", score
    OUTPUT "Prediction:", prediction
END
```

**Python Implementation:**

**A question before moving on.** This program makes a judgement about a person. Who chose the threshold, and what happens to the person just on the wrong side of it? What does the program not know about them? What would you want said to them? Write a sentence or two; there is no right answer, and the question is the point.

```python exec
id: tutorial-02-algorithms-and-problem-solving-page-1-5
# Student Success Predictor (ML-style algorithm)

print("=== Student Success Predictor ===")
print("Using rule-based ML approach")
print()

# Input data
study_hours = 6
attendance_percentage = 85

print(f"Study Hours per Week: {study_hours}")
print(f"Attendance: {attendance_percentage}%")
print()

# Calculate prediction score (our "model")
score = (study_hours * 10) + (attendance_percentage * 0.5)

# Make prediction
if score >= 80:
    prediction = "Likely to Pass with Distinction"
elif score >= 60:
    prediction = "Likely to Pass"
else:
    prediction = "At Risk - Need More Study"

# Output results
print(f"Prediction Score: {score:.1f}")
print(f"Prediction: {prediction}")
print()
print("This is how simple ML models work!")
```

### Pseudocode Best Practices

 **DO:**
- Use clear, descriptive variable names
- Indent to show structure
- Add comments to explain logic
- Use consistent keywords
- Focus on **what** to do, not **how**

 **DON'T:**
- Use actual programming syntax
- Worry about semicolons, brackets, etc.
- Make it too detailed
- Use unclear abbreviations

---

## What we set out to do

These were the aims of this notebook. Now that you have worked through it, they are a check on what happened rather than a promise about it.

1. **Demonstrate understanding of algorithms** and their applications (LO 2)
2. **Explain sequential nature** of problem solving (LO 5)
3. **Summarize structured programming concepts** including pseudo-code (LO 6)
4. Design solutions using pseudocode and flowcharts
5. Create data dictionaries for your programs

## Looking back

Before leaving this page, a sentence on each. What you write stays on this device.

```reflect
- Something you expected before running a cell that turned out differently
- The one idea from this page you could explain to someone else now
- Something you would change or try next, if there were time
- A question this page raised for you that it did not answer. Bring it to the next session; these questions are where the next session starts.
```
