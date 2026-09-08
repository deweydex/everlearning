---
title: "tutorial-02-algorithms-and-problem-solving-page-3 (3 of 3)"
slug: tutorial-02-algorithms-and-problem-solving-page-3
course: programming-and-design-principles
course_title: "Programming and Design Principles"
series: tutorials
series_title: "Tutorials"
version: 2026.09.06.1
---

## Part 7: ML Application - Simple Classifier

### Building Your First ML Classifier

Let's design a simple ML-style classifier from scratch!

**Problem**: Email Priority Classifier
- Classify emails as High, Medium, or Low priority
- Based on: sender type and keywords

### Design Process

#### Data Dictionary

| Variable Name | Data Type | Purpose | Example Value |
|--------------|-----------|---------|---------------|
| sender | String | Type of sender | "manager" |
| has_urgent | Boolean | Contains urgent keywords | True |
| has_deadline | Boolean | Contains deadline keywords | False |
| priority_score | Integer | Calculated priority score | 75 |
| priority | String | Final priority category | "High" |

#### Pseudocode

```
START
 // Input
 INPUT sender (manager/colleague/newsletter)
 INPUT has_urgent (true/false)
 INPUT has_deadline (true/false)
 
 // Initialize score
 SET priority_score = 0
 
 // Calculate score based on features
 IF sender == "manager" THEN
 SET priority_score = priority_score + 40
 ELSE IF sender == "colleague" THEN
 SET priority_score = priority_score + 20
 ELSE
 SET priority_score = priority_score + 5
 END IF
 
 IF has_urgent == true THEN
 SET priority_score = priority_score + 30
 END IF
 
 IF has_deadline == true THEN
 SET priority_score = priority_score + 25
 END IF
 
 // Classify based on score
 IF priority_score >= 70 THEN
 SET priority = "High"
 ELSE IF priority_score >= 40 THEN
 SET priority = "Medium"
 ELSE
 SET priority = "Low"
 END IF
 
 // Output
 OUTPUT priority_score, priority
END
```

#### Implementation

```python exec
id: tutorial-02-algorithms-and-problem-solving-page-3-1
# Email Priority Classifier (ML-style Algorithm)

print("=== Email Priority Classifier ===")
print("ML-Style Rule-Based Classification")
print("=" * 40)
print()

# Input - Email features
sender = "manager"  # Can be: manager, colleague, newsletter
has_urgent = True
has_deadline = False

print("Email Features:")
print(f"Sender: {sender}")
print(f"Has 'urgent' keyword: {has_urgent}")
print(f"Has deadline mentioned: {has_deadline}")
print()

# Initialize priority score
priority_score = 0

# Feature scoring (our "model weights")
print("Calculating Priority Score:")

if sender == "manager":
    priority_score = priority_score + 40
    print(f"  Manager email: +40 points (score: {priority_score})")
elif sender == "colleague":
    priority_score = priority_score + 20
    print(f"  Colleague email: +20 points (score: {priority_score})")
else:
    priority_score = priority_score + 5
    print(f"  Newsletter/Other: +5 points (score: {priority_score})")

if has_urgent:
    priority_score = priority_score + 30
    print(f"  Urgent keyword: +30 points (score: {priority_score})")

if has_deadline:
    priority_score = priority_score + 25
    print(f"  Deadline mentioned: +25 points (score: {priority_score})")

print()
print(f"Final Priority Score: {priority_score}")
print()

# Classification based on score
if priority_score >= 70:
    priority = "High"
elif priority_score >= 40:
    priority = "Medium"
else:
    priority = "Low"

# Output
print("=" * 40)
print(f"PRIORITY: {priority}")
print("=" * 40)
print()
print("This is how ML classifiers work:")
print("1. Extract features from data")
print("2. Calculate scores/probabilities")
print("3. Make classification decision")
```

### Understanding This as ML

This algorithm demonstrates ML concepts:

1. **Features**: sender, has_urgent, has_deadline
2. **Weights**: +40 for manager, +30 for urgent, etc.
3. **Scoring**: Weighted sum of features
4. **Classification**: Threshold-based decision

**In Real ML:**
- Features would be learned from data
- Weights would be optimized automatically
- Thresholds would be determined by training

But the **fundamental logic is the same**!

---

## Practice Exercises

### Your turn 1: Temperature Converter with Advice

**Problem**: Create a Celsius to Fahrenheit converter that also gives weather advice.

**Requirements:**
- Input: Temperature in Celsius
- Convert to Fahrenheit: F = (C × 9/5) + 32
- Provide advice:
 - Below 0°C: "Freezing - Stay warm!"
 - 0-15°C: "Cold - Wear a jacket"
 - 15-25°C: "Comfortable"
 - Above 25°C: "Warm - Stay hydrated"

**Tasks:**
1. Create a data dictionary
2. Write pseudocode
3. Draw a simple flowchart (text-based is fine)
4. Implement in Python

**Your Data Dictionary:**

| Variable Name | Data Type | Purpose | Example Value |
|--------------|-----------|---------|---------------|
| | | | |
| | | | |
| | | | |

**Your Pseudocode:**
```
START
    // Your pseudocode here
    
END
```

```python exec
id: tutorial-02-algorithms-and-problem-solving-page-3-2
# Exercise 1: Your Python Implementation

celsius = 20  # Change this to test

# YOUR CODE HERE
```

### Your turn 2: Student Loan Eligibility Checker

**Problem**: Check if a student is eligible for a loan.

**Requirements:**
- Input: Age, enrolled status (True/False), GPA
- Eligibility rules:
  - Must be 18 or older
  - Must be enrolled
  - GPA must be 2.0 or higher
- Output: Eligible or Not Eligible with reason

**Tasks:** Complete data dictionary, pseudocode, and implementation

**A question before moving on.** This program makes a judgement about a person. Who chose the threshold, and what happens to the person just on the wrong side of it? What does the program not know about them? What would you want said to them? Write a sentence or two; there is no right answer, and the question is the point.

**Your Data Dictionary:**

| Variable Name | Data Type | Purpose | Example Value |
|--------------|-----------|---------|---------------|
| | | | |
| | | | |

**Your Pseudocode:**
```
START
    // Your pseudocode here
    
END
```

```python exec
id: tutorial-02-algorithms-and-problem-solving-page-3-3
# Exercise 2: Your Python Implementation

age = 19
enrolled = True
gpa = 3.2

# YOUR CODE HERE
```

### Your turn 3: Simple Product Recommender

**Problem**: Recommend a laptop based on user needs (ML-style)

**Requirements:**
- Input: budget (low/medium/high), usage (gaming/work/student)
- Scoring system:
  - Budget: low=10, medium=20, high=30
  - Usage: gaming=25, work=20, student=15
- Recommendations based on total score:
  - Score >= 45: "Premium Model Recommended"
  - Score >= 30: "Mid-Range Model Recommended"
  - Score < 30: "Budget Model Recommended"

**Tasks:** Complete full design process

**Your Data Dictionary:**

| Variable Name | Data Type | Purpose | Example Value |
|--------------|-----------|---------|---------------|
| | | | |

**Your Pseudocode:**
```
START
    // Your pseudocode here
END
```

```python exec
id: tutorial-02-algorithms-and-problem-solving-page-3-4
# Exercise 3: Your Python Implementation

budget = "medium"  # low, medium, or high
usage = "work"     # gaming, work, or student

# YOUR CODE HERE
```

### Your turn 4: Fitness Level Assessor

**Problem**: Assess fitness level and recommend workout intensity.

**Requirements:**
- Input: age, resting heart rate, exercise frequency (days/week)
- Calculate fitness score:
  - Base score = 100 - age
  - Adjust for heart rate: if heart_rate < 60: +20, if > 80: -20
  - Add exercise bonus: exercise_days * 5
- Recommendations:
  - Score >= 90: "Excellent - Maintain intensity"
  - Score 70-89: "Good - Moderate intensity"
  - Score 50-69: "Fair - Start slowly"
  - Score < 50: "Consult physician"

**Tasks:** Complete all design steps and implementation

```python exec
id: tutorial-02-algorithms-and-problem-solving-page-3-5
# Exercise 4: Complete Design and Implementation

# 1. Create your data dictionary (in markdown cell above)
# 2. Write your pseudocode (in markdown cell above)
# 3. Implement below

age = 25
resting_heart_rate = 65
exercise_days = 4

# YOUR CODE HERE
```

---

## Key Concepts Summary

### Algorithms
- Step-by-step procedures to solve problems
- Must be clear, finite, and effective
- Foundation of all programming
- Essential for ML development

### Sequential Problem Solving
1. Understand the problem
2. Design the solution
3. Code the solution
4. Test thoroughly
5. Refine and document

### Pseudocode
- Plain language algorithm description
- Language independent
- Focus on logic, not syntax
- Planning tool before coding
- Uses keywords: START, END, IF, INPUT, OUTPUT

### Flowcharts
- Visual representation of algorithms
- Standard shapes for different operations
- Shows flow of control clearly
- Good for complex decision logic

### Data Dictionaries
- Document all variables
- Specify data types
- Explain purpose
- Professional documentation standard

### Design Before Code
 Saves time in the long run 
 Reduces bugs 
 Improves code quality 
 Makes debugging easier 
 Professional practice 

---

## Assessment Preparation

This tutorial prepares you for:

### Skills Demonstration 1
You'll need to:
- Develop an algorithm using pseudocode or flowchart
- Create a data dictionary
- Implement solution with selection and iteration
- Develop and apply test data

### Theory Exam
**Potential Questions:**

1. Explain what an algorithm is and list three properties of a good algorithm.

2. Describe the sequential steps in professional software development.

3. What is pseudocode and why is it used before programming?

4. Compare and contrast pseudocode and flowcharts. When would you use each?

5. Explain the purpose of a data dictionary in program design.

---

## Reflection Questions

**Your Reflections:**

1. **Why is designing before coding important?**
   
   (Your answer here)

2. **Which do you prefer - pseudocode or flowcharts? Why?**
   
   (Your answer here)

3. **How does algorithmic thinking apply to ML problems?**
   
   (Your answer here)

4. **What was the most challenging concept in this tutorial?**
   
   (Your answer here)

## Looking back

Before leaving this page, a sentence on each. What you write stays on this device.

```reflect
- Something you expected before running a cell that turned out differently
- The one idea from this page you could explain to someone else now
- Something you would change or try next, if there were time
- A question this page raised for you that it did not answer. Bring it to the next session; these questions are where the next session starts.
```

---

## Next Steps


- What algorithms are and how to design them
- Sequential problem-solving methodology
- How to write pseudocode
- How to create flowcharts
- The importance of data dictionaries
- How to apply these to ML problems

### Before Tutorial 3:
- [ ] Complete ALL exercises
- [ ] Practice writing pseudocode for everyday tasks
- [ ] Try drawing flowcharts for simple decisions
- [ ] Review data types in Python

### In Tutorial 3, we'll explore:
- **Variables and Data Types** in depth
- **Type conversion** between data types
- **Operators** - mathematical, relational, Boolean
- **Operator precedence** - order of operations
- **Building scoring systems** for ML

---

## Additional Resources

- **Flowchart Tool**: draw.io (free online)
- **Algorithm Practice**: HackerRank, LeetCode
- **Python Tutor**: pythontutor.com (visualize code execution)

---

**Great progress! See you in Tutorial 3!** 
