---
title: "Tutorial 8: Testing and Debugging"
slug: tutorial-08-testing-and-debugging
course: programming-and-design-principles
course_title: "Programming and Design Principles"
series: tutorials
series_title: "Tutorials"
version: 2026.09.06.1
---

# Tutorial 8: Testing and Debugging

**Module**: Programming & Design Principles 5N2927  
**Level**: QQI Level 5  
**Theme**: Ensuring ML System Reliability

---

## Introduction: Why Testing Matters

In previous tutorials, you've built increasingly complex programs. But how do you know they work correctly? In machine learning systems:
- Wrong predictions can lead to poor decisions
- Data processing errors corrupt entire datasets
- Hidden bugs may only appear with certain inputs
- Edge cases reveal flaws in logic

Professional programmers spend as much time testing as writing code. This tutorial teaches you systematic approaches to ensure your programs work correctly.

---

## Part 1: Understanding Different Types of Errors

Not all errors are the same. Understanding error types helps you fix them faster.

### Exploration 1.1: Syntax Errors

Syntax errors occur when code violates Python's grammatical rules. Python catches these before running.

```python exec
id: tutorial-08-testing-and-debugging-1
# Examples of syntax errors (each line has a problem)
# Uncomment ONE at a time to see the error:

# Missing colon
# if hours > 10
#     print("Good")

# Misspelled keyword
# deff calculate():
#     return 42

# Unclosed string
# name = "Alice

# Invalid indentation
# def test():
# print("Hello")

# Unmatched parentheses
# result = (5 + 3

print("If you see this, all syntax is correct!")
```

### Reading Syntax Error Messages:

When Python finds a syntax error, it shows:
- The file and line number
- The problematic line
- A caret (^) pointing to where Python noticed the problem
- A description of what's wrong

Note: The caret often points *after* the actual error!

### Exploration 1.2: Runtime Errors

Runtime errors occur when syntactically correct code tries to do something impossible.

```python exec
id: tutorial-08-testing-and-debugging-2
# Examples of runtime errors
# Uncomment ONE at a time:

# Division by zero
# result = 100 / 0

# Type error
# number = "10"
# doubled = number * 2  # This works but not as intended
# tripled = number + 2  # This causes TypeError

# Index error
# scores = [85, 90, 78]
# print(scores[10])  # Only indices 0-2 exist

# Name error
# print(undefined_variable)

# Value error
# number = int("not a number")

print("No runtime errors occurred!")
```

### Common Runtime Errors:

- **ZeroDivisionError**: Dividing by zero
- **TypeError**: Wrong type for an operation
- **ValueError**: Right type, wrong value
- **IndexError**: List index out of range
- **KeyError**: Dictionary key doesn't exist
- **NameError**: Variable not defined
- **AttributeError**: Object doesn't have that attribute

### Exploration 1.3: Logical Errors

The most dangerous errors - code runs without crashing but produces wrong results.

```python exec
id: tutorial-08-testing-and-debugging-3
# Logical error example 1: Wrong formula
def calculate_average_wrong(numbers):
    """BUG: Uses wrong formula."""
    total = sum(numbers)
    average = total / len(numbers) + 1  # BUG: Should not add 1
    return average

scores = [80, 90, 70]
avg = calculate_average_wrong(scores)
print(f"Average: {avg}")  # Wrong! Should be 80, not 81

# Logical error example 2: Wrong condition
def classify_score_wrong(score):
    """BUG: Uses wrong comparison."""
    if score > 50:  # BUG: Should be >= 50
        return "Pass"
    else:
        return "Fail"

print(f"Score 50: {classify_score_wrong(50)}")  # Wrong! Should pass

# Logical error example 3: Wrong variable
hours = 10
attendance = 0.85
prediction = (hours * 3.5) + (hours * 20) + 30  # BUG: Should use attendance
print(f"Prediction: {prediction}")  # Wrong calculation!
```

### Your Turn: Identify Error Types

```python exec
id: tutorial-08-testing-and-debugging-4
# For each code snippet, identify if it has:
# S = Syntax Error (won't run)
# R = Runtime Error (crashes when executed)
# L = Logical Error (runs but wrong answer)
# N = No Error

# Write your answers as comments, then test:

# Example 1:
# def calculate(x)
#     return x * 2
# Answer: ___

# Example 2:
# result = 10 + "5"
# Answer: ___

# Example 3:
# def double(x):
#     return x + x  # Intended to return x * 2
# print(double("5"))  # Prints "55" not 10
# Answer: ___

# Example 4:
# numbers = [1, 2, 3]
# total = sum(numbers)
# Answer: ___
```

---

## Part 2: Developing Test Data

Good testing requires systematic test data that covers different scenarios.

### Exploration 2.1: Test Data Categories

Consider a function that classifies exam scores:

```python exec
id: tutorial-08-testing-and-debugging-5
def classify_score(score):
    """
    Classify exam score into grade.
    A: 90-100
    B: 80-89
    C: 70-79
    D: 60-69
    F: 0-59
    """
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"
```

### What test data should we use?

1. **Normal values** - Typical expected inputs
2. **Boundary values** - At the edges of ranges
3. **Extreme values** - Maximum and minimum possible
4. **Invalid values** - Unexpected or wrong inputs

### Developing Comprehensive Test Data:

```python exec
id: tutorial-08-testing-and-debugging-6
# Test data for classify_score function
test_cases = [
    # (input, expected_output, description)
    
    # Normal values
    (95, "A", "Normal A"),
    (85, "B", "Normal B"),
    (75, "C", "Normal C"),
    (65, "D", "Normal D"),
    (45, "F", "Normal F"),
    
    # Boundary values (critical!)
    (90, "A", "Boundary A (lower)"),
    (100, "A", "Boundary A (upper)"),
    (89, "B", "Just below A"),
    (80, "B", "Boundary B (lower)"),
    (79, "C", "Just below B"),
    (70, "C", "Boundary C (lower)"),
    (60, "D", "Boundary D (lower)"),
    (59, "F", "Just below D"),
    
    # Extreme values
    (0, "F", "Minimum score"),
    
    # Invalid values (what should happen?)
    # (-10, "?", "Negative score"),
    # (150, "?", "Score over 100"),
]

# Run tests
print("Testing classify_score function:")
print("=" * 50)

passed = 0
failed = 0

for score, expected, description in test_cases:
    result = classify_score(score)
    status = "PASS" if result == expected else "FAIL"
    
    if status == "PASS":
        passed += 1
    else:
        failed += 1
    
    print(f"{status}: {description}")
    print(f"   Input: {score}, Expected: {expected}, Got: {result}")

print("=" * 50)
print(f"Results: {passed} passed, {failed} failed")
```

### Principles of Good Test Data:

1. **Cover all branches** - Test every if/elif/else path
2. **Test boundaries** - Values at the edges of conditions
3. **Include normal cases** - Typical expected inputs
4. **Test extremes** - Minimum and maximum values
5. **Consider invalid input** - What if users enter wrong data?
6. **Test edge cases** - Unusual but possible scenarios

### Your Turn: Develop Test Data

```python exec
id: tutorial-08-testing-and-debugging-7
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
def needs_support(hours, attendance):
    """
    Determine if student needs support.
    Criteria: hours < 8 OR attendance < 0.75
    """
    return hours < 8 or attendance < 0.75

# Your code here:
# Create comprehensive test data for needs_support function
# Include:
# - Normal values (both True and False results)
# - Boundary values (exactly 8 hours, exactly 0.75 attendance)
# - Extreme values (0 hours, 0.0 attendance, 24 hours, 1.0 attendance)
# - Cases where only one condition is true
# - Cases where both conditions are true
# - Cases where neither condition is true
#
# Format: [(hours, attendance, expected_result, description), ...]
```

---

## Part 3: Systematic Testing Process

### Exploration 3.1: Manual Testing with Tables

Let's test a prediction function systematically:

```python exec
id: tutorial-08-testing-and-debugging-8
def calculate_prediction(hours, attendance):
    """Calculate predicted exam score."""
    return (hours * 3.5) + (attendance * 20) + 30

# Manual test table
print("Manual Test Results")
print("=" * 70)
print(f"{'Hours':<8} {'Attendance':<12} {'Expected':<12} {'Actual':<12} {'Status'}")
print("=" * 70)

# Test case 1: Normal values
h, a = 10, 0.80
expected = 10*3.5 + 0.80*20 + 30  # Calculate by hand
actual = calculate_prediction(h, a)
status = "PASS" if abs(expected - actual) < 0.01 else "FAIL"
print(f"{h:<8} {a:<12.2f} {expected:<12.1f} {actual:<12.1f} {status}")

# Test case 2: Minimum values
h, a = 0, 0.0
expected = 30.0  # Only base score
actual = calculate_prediction(h, a)
status = "PASS" if abs(expected - actual) < 0.01 else "FAIL"
print(f"{h:<8} {a:<12.2f} {expected:<12.1f} {actual:<12.1f} {status}")

# Test case 3: Maximum values
h, a = 20, 1.0
expected = 20*3.5 + 1.0*20 + 30
actual = calculate_prediction(h, a)
status = "PASS" if abs(expected - actual) < 0.01 else "FAIL"
print(f"{h:<8} {a:<12.2f} {expected:<12.1f} {actual:<12.1f} {status}")

print("=" * 70)
```

### Exploration 3.2: Automated Testing

Automating tests makes them repeatable and faster:

```python exec
id: tutorial-08-testing-and-debugging-9
def test_calculate_prediction():
    """Automated test suite for calculate_prediction."""
    test_cases = [
        # (hours, attendance, expected_score, description)
        (10, 0.80, 81.0, "Normal values"),
        (0, 0.0, 30.0, "Minimum values"),
        (20, 1.0, 120.0, "Maximum values"),
        (15, 0.90, 100.5, "High performer"),
        (5, 0.60, 59.5, "Low values"),
    ]
    
    print("Running automated tests...")
    passed = 0
    failed = 0
    
    for hours, attendance, expected, desc in test_cases:
        actual = calculate_prediction(hours, attendance)
        
        # Allow small floating-point differences
        if abs(actual - expected) < 0.01:
            print(f"✓ PASS: {desc}")
            passed += 1
        else:
            print(f"✗ FAIL: {desc}")
            print(f"  Expected: {expected}, Got: {actual}")
            failed += 1
    
    print(f"\nTest Summary: {passed} passed, {failed} failed")
    return failed == 0

# Run the test suite
test_calculate_prediction()
```

### Your Turn: Create Test Suite

```python exec
id: tutorial-08-testing-and-debugging-10
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
def calculate_grade(score):
    """Convert numeric score to letter grade."""
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

# Your code here:
# Create test_calculate_grade() function
# Include at least 10 test cases
# Cover all boundaries and normal values
# Print clear pass/fail messages
# Return True if all tests pass
```

---

## Part 4: Debugging Techniques

When tests fail, you need to find and fix the bug. Here are systematic approaches.

### Exploration 4.1: Print Debugging

The simplest debugging technique - add print statements to see what's happening:

```python exec
id: tutorial-08-testing-and-debugging-11
def calculate_average_buggy(numbers):
    """BUG: This function has an error."""
    total = 0
    for num in numbers:
        total = total + num
    average = total / len(numbers) - 1  # BUG HERE!
    return average

# Test reveals the bug
scores = [80, 90, 70]
result = calculate_average_buggy(scores)
print(f"Average: {result}")  # Expected 80, got 79

# Add debugging prints
def calculate_average_debug(numbers):
    """Same function with debug prints."""
    print(f"DEBUG: Input numbers: {numbers}")
    
    total = 0
    for num in numbers:
        total = total + num
        print(f"DEBUG: Added {num}, total now {total}")
    
    print(f"DEBUG: Total: {total}, Count: {len(numbers)}")
    
    average = total / len(numbers) - 1
    print(f"DEBUG: Calculated average: {average}")
    print(f"DEBUG: Formula used: {total} / {len(numbers)} - 1")
    
    return average

print("\nWith debugging:")
result = calculate_average_debug([80, 90, 70])
print(f"\nSpot the bug! We subtract 1, but shouldn't.")
```

### Exploration 4.2: The Rubber Duck Method

Explaining your code line-by-line (even to a rubber duck!) often reveals bugs:

```python exec
id: tutorial-08-testing-and-debugging-12
def find_maximum_buggy(numbers):
    """BUG: Find maximum value in list."""
    max_value = 0  # BUG: What if all numbers are negative?
    for num in numbers:
        if num > max_value:
            max_value = num
    return max_value

# Test with negative numbers
print("Test 1:", find_maximum_buggy([5, 10, 3, 8]))  # Works: 10
print("Test 2:", find_maximum_buggy([-5, -2, -10]))  # Bug! Returns 0, should be -2

# Rubber duck explanation:
# "Line 1: I set max_value to 0
#  Line 2: I look at each number
#  Line 3: If the number is bigger than max_value...
#  Wait! If all numbers are negative, none are bigger than 0!
#  I should start with the first number instead!"

# Fixed version
def find_maximum_fixed(numbers):
    """Correctly find maximum value."""
    if not numbers:
        return None
    
    max_value = numbers[0]  # Start with first number
    for num in numbers:
        if num > max_value:
            max_value = num
    return max_value

print("Fixed test:", find_maximum_fixed([-5, -2, -10]))  # Correct: -2
```

### Exploration 4.3: Binary Search Debugging

For large programs, narrow down where the bug is:

```python exec
id: tutorial-08-testing-and-debugging-13
def complex_calculation(hours, attendance, previous_score):
    """Multi-step calculation - bug somewhere!"""
    
    # Step 1: Calculate base prediction
    base = (hours * 3.5) + (attendance * 20) + 30
    print(f"After step 1 (base): {base}")
    
    # Step 2: Apply previous score adjustment
    adjustment = (previous_score - 70) * 0.1
    print(f"After step 2 (adjustment): {adjustment}")
    
    # Step 3: Combine (BUG: should add, not subtract)
    final = base - adjustment  # BUG HERE!
    print(f"After step 3 (final): {final}")
    
    # Step 4: Ensure reasonable range
    final = max(0, min(100, final))
    print(f"After step 4 (clamped): {final}")
    
    return final

result = complex_calculation(10, 0.80, 75)
print(f"\nFinal result: {result}")
print("By printing after each step, we can see where the logic goes wrong!")
```

### Your Turn: Debug These Functions

```python exec
id: tutorial-08-testing-and-debugging-14
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
# Each function has a bug. Find and fix them!

def count_passing_buggy(scores):
    """Count how many scores are passing (>= 50)."""
    count = 0
    for score in scores:
        if score > 50:  # BUG: Should be >=
            count = count + 1
    return count

# Test: Should return 3, but returns 2
print("Bug 1:", count_passing_buggy([60, 50, 45, 75]))  

# Your code: Fix the function and test again


def calculate_percentage_buggy(part, whole):
    """Calculate percentage."""
    percentage = (part / whole)  # BUG: Need to * 100
    return percentage

# Test: Should return 75.0, but returns 0.75
print("Bug 2:", calculate_percentage_buggy(15, 20))

# Your code: Fix the function and test again


def is_in_range_buggy(value, minimum, maximum):
    """Check if value is in range [minimum, maximum]."""
    return value > minimum and value < maximum  # BUG: Should be >=  and <=

# Test: Should return True, but returns False
print("Bug 3:", is_in_range_buggy(50, 50, 100))

# Your code: Fix the function and test again
```

---

## Part 5: Structured Walkthroughs

A structured walkthrough means tracing through code step-by-step, tracking all variable values.

### Exploration 5.1: Manual Trace Table

```python exec
id: tutorial-08-testing-and-debugging-15
def process_scores(scores):
    """Calculate statistics on scores."""
    total = 0
    count = 0
    passing = 0
    
    for score in scores:
        total = total + score
        count = count + 1
        
        if score >= 50:
            passing = passing + 1
    
    average = total / count
    pass_rate = passing / count
    
    return average, pass_rate

# Manual walkthrough with [60, 45, 75]
print("MANUAL WALKTHROUGH")
print("=" * 60)
print("Starting values: total=0, count=0, passing=0")
print()
print("Iteration 1: score=60")
print("  total = 0 + 60 = 60")
print("  count = 0 + 1 = 1")
print("  60 >= 50? Yes, so passing = 0 + 1 = 1")
print()
print("Iteration 2: score=45")
print("  total = 60 + 45 = 105")
print("  count = 1 + 1 = 2")
print("  45 >= 50? No, so passing stays 1")
print()
print("Iteration 3: score=75")
print("  total = 105 + 75 = 180")
print("  count = 2 + 1 = 3")
print("  75 >= 50? Yes, so passing = 1 + 1 = 2")
print()
print("After loop: total=180, count=3, passing=2")
print("  average = 180 / 3 = 60.0")
print("  pass_rate = 2 / 3 = 0.667")
print()
print("=" * 60)

# Verify with actual execution
avg, rate = process_scores([60, 45, 75])
print(f"Actual result: average={avg:.1f}, pass_rate={rate:.3f}")
```

### Exploration 5.2: Trace Table Format

Professional programmers use trace tables:

```python exec
id: tutorial-08-testing-and-debugging-16
print("TRACE TABLE for process_scores([60, 45, 75])")
print("=" * 80)
print(f"{'Step':<8} {'score':<8} {'total':<8} {'count':<8} {'passing':<10} {'Condition'}")
print("=" * 80)
print(f"{'Start':<8} {'-':<8} {'0':<8} {'0':<8} {'0':<10} {'-'}")
print(f"{'Loop 1':<8} {'60':<8} {'60':<8} {'1':<8} {'1':<10} {'60>=50: Yes'}")
print(f"{'Loop 2':<8} {'45':<8} {'105':<8} {'2':<8} {'1':<10} {'45>=50: No'}")
print(f"{'Loop 3':<8} {'75':<8} {'180':<8} {'3':<8} {'2':<10} {'75>=50: Yes'}")
print(f"{'After':<8} {'-':<8} {'180':<8} {'3':<8} {'2':<10} {'-'}")
print("=" * 80)
print("Final: average = 180/3 = 60.0, pass_rate = 2/3 = 0.667")
```

### Your Turn: Create Trace Table

```python exec
id: tutorial-08-testing-and-debugging-17
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
def find_minimum(numbers):
    """Find minimum value in list."""
    min_val = numbers[0]
    for num in numbers:
        if num < min_val:
            min_val = num
    return min_val

# Your code here:
# Create a trace table for find_minimum([85, 72, 90, 68, 95])
# Track: iteration, num, min_val, condition result
# Show step-by-step execution
```

---

## Part 6: Comprehensive Testing Project

Let's apply all testing concepts to a complete system.

### Project 6.1: Test an ML Prediction System

```python exec
id: tutorial-08-testing-and-debugging-18
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
# Student prediction system to test
def calculate_prediction(hours, attendance):
    """Calculate predicted score."""
    return (hours * 3.5) + (attendance * 20) + 30

def classify_risk(hours, attendance):
    """Classify student risk level."""
    engagement = hours * attendance
    if engagement >= 10:
        return "Low"
    elif engagement >= 7:
        return "Medium"
    else:
        return "High"

def recommend_action(prediction, risk):
    """Recommend action based on prediction and risk."""
    if risk == "High":
        return "Immediate intervention needed"
    elif risk == "Medium" and prediction < 70:
        return "Monitor closely"
    elif prediction >= 85:
        return "Encourage continued excellence"
    else:
        return "Continue current support"

# Your code here:
# Create comprehensive test suite:
#
# 1. Test calculate_prediction:
#    - At least 8 test cases
#    - Include boundaries, extremes, normal values
#
# 2. Test classify_risk:
#    - Cover all three risk levels
#    - Test boundary values for engagement
#
# 3. Test recommend_action:
#    - Test all possible recommendation paths
#    - Combine different risk levels with different predictions
#
# 4. Create integration tests:
#    - Test complete workflows
#    - Verify functions work together correctly
#
# 5. Document all test results in clear format
```

---

## Reflection Questions

Consider your understanding of testing and debugging:

1. **Why is testing with boundary values more important than testing with random values?**
   
   (Your answer here)

2. **How do systematic testing approaches save time compared to random testing?**
   
   (Your answer here)

3. **When would you use print debugging versus trace tables?**
   
   (Your answer here)

4. **How does creating test data before writing code improve program quality?**
   
   (Your answer here)

---

## Summary and Key Takeaways

Excellent progress! You now understand:

### Error Types
- Syntax errors (won't run)
- Runtime errors (crashes during execution)
- Logical errors (runs but wrong results)
- How to interpret error messages

### Test Data Development
- Categories: normal, boundary, extreme, invalid
- Importance of boundary testing
- Covering all code paths
- Edge case identification

### Testing Processes
- Manual testing with tables
- Automated test suites
- Test case documentation
- Pass/fail criteria

### Debugging Techniques
- Print debugging
- Rubber duck method
- Binary search debugging
- Isolating problems

### Structured Walkthroughs
- Manual code tracing
- Trace tables
- Variable tracking
- Step-by-step verification

---

## What we set out to do

These were the aims of this notebook. Now that you have worked through it, they are a check on what happened rather than a promise about it.

- Interpret compiler and runtime error messages (LO 9)
- Identify syntax, logical, and runtime errors (LO 9)
- Develop comprehensive test data for programs (LO 10)
- Apply test data systematically to validate programs (LO 10)
- Use structured walkthroughs and debugging tools (LO 10)
- Revise code until it is accurate and reliable (LO 10)

---

## Looking back

Before leaving this page, a sentence on each. What you write stays on this device.

```reflect
- Something you expected before running a cell that turned out differently
- The one idea from this page you could explain to someone else now
- Something you would change or try next, if there were time
- A question this page raised for you that it did not answer. Bring it to the next session; these questions are where the next session starts.
```

## Course Completion


- [ ] Understand programming history and concepts
- [ ] Design algorithms systematically
- [ ] Work with variables, data types, and operators
- [ ] Make decisions with selection structures
- [ ] Process data with iteration
- [ ] Organize data in lists
- [ ] Create reusable functions
- [ ] Test and debug programs professionally

### Next Steps:
- Apply these skills to your assessments
- Build complete systems combining all concepts
- Continue to NumPy and pandas for data science
- Explore object-oriented programming
- Work on team projects

---

## Additional Resources

- **Python Debugging**: realpython.com/python-debugging-pdb
- **Testing Best Practices**: realpython.com/python-testing
- **Unit Testing**: docs.python.org/3/library/unittest.html
- **Test-Driven Development**: testdriven.io/test-driven-development

---
