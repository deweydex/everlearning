---
title: "Tutorial 7: Functions and Modularization"
slug: tutorial-07-functions-and-modularisation
course: programming-and-design-principles
course_title: "Programming and Design Principles"
series: tutorials
series_title: "Tutorials"
version: 2026.09.06.1
---

# Tutorial 7: Functions and Modularization

**Module**: Programming & Design Principles 5N2927  
**Level**: QQI Level 5  
**Theme**: Building Reusable ML Components

---

## Introduction: The Power of Reusable Code

In previous tutorials, you've written increasingly complex programs. As programs grow, you've likely noticed patterns:
- Repeating the same calculations multiple times
- Similar code blocks for different data
- Difficulty making changes without updating code in many places

Functions solve these problems by packaging code into reusable blocks. In machine learning systems:
- Prediction calculations need to run on many data points
- Data preprocessing steps repeat across different datasets
- Evaluation metrics need computation for various models

Functions make these operations clean, maintainable, and reusable.

---

## Part 1: Why Modularization Matters

### Exploration 1.1: The Problem Without Functions

Consider a program that calculates student predictions:

```python exec
id: tutorial-07-functions-and-modularisation-1
# Without functions - repetitive and error-prone

# Student 1
hours1 = 12
attendance1 = 0.85
prediction1 = (hours1 * 3.5) + (attendance1 * 20) + 30
print(f"Student 1 prediction: {prediction1}")

# Student 2
hours2 = 15
attendance2 = 0.90
prediction2 = (hours2 * 3.5) + (attendance2 * 20) + 30
print(f"Student 2 prediction: {prediction2}")

# Student 3
hours3 = 8
attendance3 = 0.75
prediction3 = (hours3 * 3.5) + (attendance3 * 20) + 30
print(f"Student 3 prediction: {prediction3}")

# What if the formula changes? You'd need to update it in 3 places!
```

### Critical Thinking:

What problems do you see with this approach?
- What if you need to calculate predictions for 100 students?
- What if the formula changes?
- What if you make a typo in one calculation?

Write your thoughts:

```python exec
id: tutorial-07-functions-and-modularisation-2
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
# Your analysis:
#
#
#
```

### Advantages of Modularization

Functions provide several key benefits:

1. **Reusability**: Write once, use many times
2. **Maintainability**: Changes in one place affect all uses
3. **Readability**: Clear names describe what code does
4. **Testing**: Test individual components separately
5. **Abstraction**: Hide complexity behind simple interfaces
6. **Organization**: Break large problems into manageable pieces

---

## Part 2: Creating Simple Functions

### Exploration 2.1: Functions Without Parameters

Let's start with the simplest functions - those that take no input and return no value.

```python exec
id: tutorial-07-functions-and-modularisation-3
# Define a simple function
def greet_user():
    """Display a welcome message."""
    print("Welcome to the ML Prediction System!")
    print("Please provide student data for analysis.")

# Call the function
greet_user()
print()

# Call it again - same code, no duplication!
greet_user()
```

### Function Anatomy:

```python
def function_name():
    """Optional docstring explaining what function does."""
    # Function body - code to execute
    statement1
    statement2
```

- `def`: Keyword to define a function
- `function_name`: Descriptive name (follow same rules as variables)
- `()`: Parentheses (will hold parameters later)
- `:`: Colon to start function body
- Indented code: The function's actions

### Your Turn: Create Simple Functions

```python exec
id: tutorial-07-functions-and-modularisation-4
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
# Your code here:
# Create three functions:
# 1. display_menu() - shows program options
# 2. show_credits() - displays your name and course
# 3. print_separator() - prints a line of dashes
# Call each function at least once
```

### Exploration 2.2: Why Use Docstrings?

Docstrings document what a function does. Python can display them as help:

```python exec
id: tutorial-07-functions-and-modularisation-5
def calculate_statistics():
    """
    Calculate and display basic statistics for student data.
    
    This function processes a dataset and computes mean,
    median, and standard deviation.
    """
    print("Calculating statistics...")

# Access the docstring
help(calculate_statistics)
print()
print(calculate_statistics.__doc__)
```

---

## Part 3: Functions with Parameters

Parameters allow functions to work with different data each time they're called.

### Exploration 3.1: Single Parameter Functions

```python exec
id: tutorial-07-functions-and-modularisation-6
# Function that accepts one parameter
def display_student_hours(hours):
    """Display a student's study hours with formatting."""
    print(f"Student studied for {hours} hours this week.")
    if hours >= 15:
        print("Excellent commitment!")
    elif hours >= 10:
        print("Good effort.")
    else:
        print("Consider increasing study time.")

# Call with different values
display_student_hours(12)
print()
display_student_hours(18)
print()
display_student_hours(7)
```

### Exploration 3.2: Multiple Parameters

```python exec
id: tutorial-07-functions-and-modularisation-7
# Function with multiple parameters
def analyze_student(name, hours, attendance):
    """
    Analyze and display student performance metrics.
    
    Parameters:
        name (str): Student's name
        hours (float): Weekly study hours
        attendance (float): Attendance rate (0.0 to 1.0)
    """
    print(f"=== Analysis for {name} ===")
    print(f"Study hours: {hours}")
    print(f"Attendance: {attendance * 100:.1f}%")
    
    # Engagement score
    engagement = hours * attendance
    print(f"Engagement score: {engagement:.2f}")
    
    # Assessment
    if engagement >= 10:
        print("Status: High performer")
    elif engagement >= 7:
        print("Status: On track")
    else:
        print("Status: Needs support")

# Call with different students
analyze_student("Alice", 12, 0.85)
print()
analyze_student("Bob", 8, 0.75)
```

### Parameter Naming:

Notice how parameters work:
- They're like variables that receive values when the function is called
- The names in the function definition can be different from the names when calling
- Order matters: first argument goes to first parameter, etc.

### Your Turn: Create Parameterized Functions

```python exec
id: tutorial-07-functions-and-modularisation-8
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
# Your code here:
# Create these functions:
#
# 1. calculate_bmi(weight, height)
#    - Calculate BMI = weight / (height ** 2)
#    - Display the result with appropriate message
#
# 2. describe_score(student_name, score)
#    - Display student name and score
#    - Add grade: A (>=90), B (>=80), C (>=70), D (>=60), F (<60)
#
# 3. calculate_average(value1, value2, value3)
#    - Calculate and display average of three values
#
# Test each function with at least two different sets of values
```

---

## Part 4: Functions That Return Values

So far, our functions have displayed output. Often, we want functions to calculate and return values for use elsewhere.

### Exploration 4.1: Simple Return Values

```python exec
id: tutorial-07-functions-and-modularisation-9
# Function that returns a value
def calculate_prediction(hours, attendance):
    """
    Calculate predicted exam score.
    
    Parameters:
        hours (float): Weekly study hours
        attendance (float): Attendance rate (0.0 to 1.0)
    
    Returns:
        float: Predicted exam score
    """
    prediction = (hours * 3.5) + (attendance * 20) + 30
    return prediction

# Use the returned value
score1 = calculate_prediction(12, 0.85)
score2 = calculate_prediction(15, 0.90)
score3 = calculate_prediction(8, 0.75)

print(f"Prediction 1: {score1}")
print(f"Prediction 2: {score2}")
print(f"Prediction 3: {score3}")
print(f"Average prediction: {(score1 + score2 + score3) / 3:.2f}")
```

### Key Insight:

Notice how `return` works:
- The function calculates a value
- `return` sends that value back to whoever called the function
- We can store the returned value in a variable
- We can use it in calculations or other function calls

### Exploration 4.2: Using Return Values in Decisions

```python exec
id: tutorial-07-functions-and-modularisation-10
def needs_support(hours, attendance):
    """
    Determine if student needs additional support.
    
    Returns:
        bool: True if support needed, False otherwise
    """
    prediction = calculate_prediction(hours, attendance)
    return prediction < 70

# Use in decision making
students = [
    ("Alice", 12, 0.85),
    ("Bob", 8, 0.75),
    ("Charlie", 15, 0.90)
]

print("Support Assessment:")
for name, hours, attendance in students:
    if needs_support(hours, attendance):
        print(f"{name}: Requires support")
    else:
        print(f"{name}: On track")
```

### Your Turn: Functions That Return Values

```python exec
id: tutorial-07-functions-and-modularisation-11
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
# Your code here:
# Create these functions that return values:
#
# 1. calculate_grade(score)
#    - Return letter grade as string (A, B, C, D, or F)
#
# 2. is_passing(score)
#    - Return True if score >= 50, False otherwise
#
# 3. calculate_engagement(hours, attendance)
#    - Return hours * attendance
#
# 4. get_risk_level(engagement_score)
#    - Return "low" if >= 10, "medium" if >= 7, "high" otherwise
#
# Test each function and use the returned values
```

### Exploration 4.3: Returning Multiple Values

```python exec
id: tutorial-07-functions-and-modularisation-12
def analyze_dataset(hours_list):
    """
    Calculate statistics for a dataset.
    
    Returns:
        tuple: (mean, minimum, maximum, total)
    """
    total = sum(hours_list)
    mean = total / len(hours_list)
    minimum = min(hours_list)
    maximum = max(hours_list)
    
    return mean, minimum, maximum, total

# Use the multiple return values
study_data = [12, 15, 8, 20, 10, 18]
avg, min_val, max_val, sum_val = analyze_dataset(study_data)

print(f"Average: {avg:.2f}")
print(f"Range: {min_val} to {max_val}")
print(f"Total: {sum_val}")
```

---

## Part 5: Variable Scope

Understanding where variables exist and can be accessed is crucial for writing correct programs.

### Exploration 5.1: Local Variables

```python exec
id: tutorial-07-functions-and-modularisation-13
def calculate_score():
    """Demonstrate local variables."""
    # These variables are LOCAL to this function
    hours = 12
    attendance = 0.85
    score = (hours * 3.5) + (attendance * 20) + 30
    print(f"Inside function: {score}")
    return score

result = calculate_score()
print(f"Returned value: {result}")

# Try to access local variables outside function
# Uncomment the next line to see the error:
# print(hours)  # NameError: hours is not defined!
```

### Critical Understanding:

Local variables:
- Are created when the function runs
- Only exist inside the function
- Are destroyed when the function ends
- Cannot be accessed from outside the function

### Exploration 5.2: Global Variables

```python exec
id: tutorial-07-functions-and-modularisation-14
# Global variable - defined outside any function
program_name = "ML Prediction System"
version = "1.0"

def display_header():
    """Functions can read global variables."""
    print(f"{program_name} v{version}")
    print("=" * 40)

def display_info():
    """Another function accessing same globals."""
    print(f"Running {program_name}")

# Both functions can access global variables
display_header()
display_info()
```

### Exploration 5.3: Best Practices with Scope

While functions can read global variables, modifying them requires care:

```python exec
id: tutorial-07-functions-and-modularisation-15
# Global counter
prediction_count = 0

def make_prediction_bad():
    """BAD: Modifying global without declaration."""
    # This creates a NEW local variable!
    prediction_count = prediction_count + 1  # Error!

def make_prediction_correct():
    """CORRECT: Using global keyword."""
    global prediction_count
    prediction_count = prediction_count + 1
    return prediction_count

# Better approach: Pass and return values
def make_prediction_best(count):
    """BEST: Avoid global variables entirely."""
    return count + 1

# Demonstrate best approach
my_count = 0
my_count = make_prediction_best(my_count)
my_count = make_prediction_best(my_count)
print(f"Predictions made: {my_count}")
```

### Scope Best Practices:

1. **Prefer local variables** - Keep data contained in functions
2. **Pass values as parameters** - Make dependencies explicit
3. **Return values** - Don't modify globals
4. **Use global variables sparingly** - Only for true constants
5. **Avoid `global` keyword** - Usually indicates poor design

### Your Turn: Understand Scope

```python exec
id: tutorial-07-functions-and-modularisation-16
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
# Your code here:
# Predict the output of this code, then run it:

x = 10  # Global

def function_a():
    x = 20  # Local to function_a
    print(f"Inside function_a: {x}")

def function_b():
    print(f"Inside function_b: {x}")  # Reads global x

def function_c(x):
    x = 30  # Local parameter
    print(f"Inside function_c: {x}")

# What will each print?
# function_a()
# function_b()
# function_c(x)
# print(f"Global x: {x}")

# Write your predictions as comments, then uncomment to test
```

---

## Part 6: System-Defined Functions

Python provides many built-in functions. You've been using them all along!

### Exploration 6.1: Common Built-in Functions

```python exec
id: tutorial-07-functions-and-modularisation-17
# Functions you've been using
data = [85, 92, 78, 95, 88]

print("Built-in functions:")
print(f"print() - displays output")
print(f"len() - length: {len(data)}")
print(f"max() - maximum: {max(data)}")
print(f"min() - minimum: {min(data)}")
print(f"sum() - total: {sum(data)}")
print(f"sorted() - ordered: {sorted(data)}")
print(f"type() - data type: {type(data)}")
print(f"range() - sequences: {list(range(5))}")
print(f"abs() - absolute: {abs(-42)}")
print(f"round() - rounding: {round(3.14159, 2)}")
```

### Exploration 6.2: The math Module

Python's `math` module provides advanced mathematical functions:

```python exec
id: tutorial-07-functions-and-modularisation-18
import math

# Mathematical functions
print("Math module functions:")
print(f"sqrt(25) = {math.sqrt(25)}")
print(f"pow(2, 10) = {math.pow(2, 10)}")
print(f"floor(3.7) = {math.floor(3.7)}")
print(f"ceil(3.2) = {math.ceil(3.2)}")
print(f"pi = {math.pi}")
print(f"sin(pi/2) = {math.sin(math.pi/2)}")

# Useful for calculations
def calculate_distance(x1, y1, x2, y2):
    """Calculate distance between two points."""
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

dist = calculate_distance(0, 0, 3, 4)
print(f"\nDistance: {dist}")
```

### Exploration 6.3: The statistics Module

```python exec
id: tutorial-07-functions-and-modularisation-19
import statistics

scores = [85, 92, 78, 95, 88, 90, 82, 86]

print("Statistics module:")
print(f"Mean: {statistics.mean(scores):.2f}")
print(f"Median: {statistics.median(scores)}")
print(f"Mode: {statistics.mode([1, 1, 2, 3, 3, 3, 4])}")
print(f"Std Dev: {statistics.stdev(scores):.2f}")
print(f"Variance: {statistics.variance(scores):.2f}")
```

---

## Part 7: Building an ML Prediction Library

Let's combine everything to create a reusable library of ML prediction functions.

### Project 7.1: Complete Prediction System

```python exec
id: tutorial-07-functions-and-modularisation-20
import statistics

# Core prediction functions
def calculate_prediction(hours, attendance):
    """Calculate predicted exam score."""
    return (hours * 3.5) + (attendance * 20) + 30

def calculate_engagement(hours, attendance):
    """Calculate engagement score."""
    return hours * attendance

def classify_performance(prediction):
    """Classify performance level."""
    if prediction >= 85:
        return "Excellent"
    elif prediction >= 70:
        return "Good"
    elif prediction >= 60:
        return "Satisfactory"
    else:
        return "Needs Support"

def get_risk_level(engagement):
    """Determine risk level."""
    if engagement >= 10:
        return "Low"
    elif engagement >= 7:
        return "Medium"
    else:
        return "High"

def analyze_student(name, hours, attendance):
    """
    Complete student analysis using all prediction functions.
    
    Returns:
        dict: Analysis results
    """
    prediction = calculate_prediction(hours, attendance)
    engagement = calculate_engagement(hours, attendance)
    performance = classify_performance(prediction)
    risk = get_risk_level(engagement)
    
    return {
        'name': name,
        'prediction': prediction,
        'engagement': engagement,
        'performance': performance,
        'risk': risk
    }

def display_analysis(analysis):
    """Display analysis results in formatted way."""
    print(f"\n=== Analysis: {analysis['name']} ===")
    print(f"Predicted Score: {analysis['prediction']:.1f}")
    print(f"Engagement: {analysis['engagement']:.2f}")
    print(f"Performance: {analysis['performance']}")
    print(f"Risk Level: {analysis['risk']}")

def analyze_cohort(students):
    """
    Analyze entire cohort and provide summary statistics.
    
    Parameters:
        students (list): List of (name, hours, attendance) tuples
    """
    all_predictions = []
    high_risk_count = 0
    
    for name, hours, attendance in students:
        analysis = analyze_student(name, hours, attendance)
        display_analysis(analysis)
        
        all_predictions.append(analysis['prediction'])
        if analysis['risk'] == "High":
            high_risk_count += 1
    
    # Cohort statistics
    print("\n" + "=" * 40)
    print("COHORT SUMMARY")
    print("=" * 40)
    print(f"Total students: {len(students)}")
    print(f"Average prediction: {statistics.mean(all_predictions):.1f}")
    print(f"Prediction range: {min(all_predictions):.1f} - {max(all_predictions):.1f}")
    print(f"High risk students: {high_risk_count}")

# Test the complete system
student_data = [
    ("Alice", 12, 0.85),
    ("Bob", 15, 0.90),
    ("Charlie", 8, 0.75),
    ("Diana", 20, 0.95),
    ("Eve", 6, 0.70)
]

analyze_cohort(student_data)
```

### Your Turn: Extend the Library

```python exec
id: tutorial-07-functions-and-modularisation-21
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
# Your code here:
# Add these functions to the prediction library:
#
# 1. calculate_grade(prediction)
#    - Return letter grade (A, B, C, D, F)
#
# 2. needs_intervention(hours, attendance)
#    - Return True if either hours < 8 OR attendance < 0.75
#
# 3. compare_students(student1_data, student2_data)
#    - Each is (name, hours, attendance)
#    - Return name of student with better prediction
#
# 4. find_best_performer(students_list)
#    - Return tuple: (name, prediction) of top student
#
# Test all new functions
```

---

## Reflection Questions

Consider your understanding of functions and modularization:

1. **How do functions improve code maintainability compared to repetitive code?**
   
   (Your answer here)

2. **When would you choose to use a global variable versus passing parameters?**
   
   (Your answer here)

3. **How does returning values differ from printing values? When would you choose each?**
   
   (Your answer here)

4. **What makes a function reusable? What design choices support reusability?**
   
   (Your answer here)

---

## Summary and Key Takeaways

Excellent progress! You now understand:

### Modularization Benefits
- Code reusability and maintainability
- Improved organization and readability
- Easier testing and debugging
- Abstraction and encapsulation

### Function Fundamentals
- Defining functions with `def`
- Function naming and documentation
- Calling functions
- Functions without parameters

### Parameters and Arguments
- Single and multiple parameters
- Passing values to functions
- Order of arguments matters
- Making functions flexible

### Return Values
- Using `return` to send values back
- Storing and using returned values
- Returning multiple values
- Functions that return vs print

### Variable Scope
- Local variables (function-level)
- Global variables (program-level)
- Best practices for scope
- Avoiding scope-related bugs

### System Functions
- Built-in Python functions
- The `math` module
- The `statistics` module
- Importing and using modules

---

## What we set out to do

These were the aims of this notebook. Now that you have worked through it, they are a check on what happened rather than a promise about it.

- Identify the advantages of modularization within programs (LO 8)
- Differentiate between local and global variables and understand scope (LO 8)
- Create functions with and without parameters (LO 8)
- Create functions that return values (LO 8)
- Use system-defined functions effectively (LO 8)
- Develop modular, reusable code following best practices (LO 7, LO 11)

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

Before continuing to Tutorial 8:
- [ ] Complete all practice exercises
- [ ] Create at least 10 different functions
- [ ] Practice using parameters and return values
- [ ] Build a small library of reusable functions
- [ ] Understand scope thoroughly

### In Tutorial 8, we'll explore:
- **Testing and Debugging** - ensuring code correctness
- **Developing test data** - systematic validation
- **Error interpretation** - understanding what went wrong
- **Debugging techniques** - finding and fixing bugs
- **Structured walkthroughs** - verifying program logic

---

## Additional Resources

- **Python Functions**: docs.python.org/3/tutorial/controlflow.html#defining-functions
- **Python Scope**: realpython.com/python-scope-legb-rule
- **Built-in Functions**: docs.python.org/3/library/functions.html
- **Math Module**: docs.python.org/3/library/math.html

---
