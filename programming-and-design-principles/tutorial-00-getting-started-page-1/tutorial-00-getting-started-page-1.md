---
title: "Tutorial 0: Getting Started with Python & Jupyter (1 of 2)"
slug: tutorial-00-getting-started-page-1
course: programming-and-design-principles
course_title: "Programming and Design Principles"
series: tutorials
series_title: "Tutorials"
version: 2026.09.06.1
---

# Tutorial 0: Getting Started with Python & Jupyter

**Module**: Programming & Design Principles 5N2927  
**Level**: QQI Level 5  
**Theme**: Introduction to Machine Learning Concepts

---

   - Printing Output
   - Variables and Data Storage
   - Basic Mathematics
5. [Your First ML-Themed Program](#ml-program)
6. [Practice Exercises](#exercises)
7. [Common Mistakes to Avoid](#common-mistakes)
8. [Key Takeaways](#takeaways)
9. [Next Steps](#next-steps)

---

## Introduction

Welcome to your first programming tutorial! In this notebook, we'll explore the fundamentals of Python programming through the lens of machine learning concepts. By the end of this tutorial, you'll understand how to write simple programs and create your first prediction system.

### What You'll Learn

- How to use Jupyter Notebooks for interactive programming
- How to write and execute Python code
- Fundamental programming concepts like variables and operations
- How to create a simple machine learning-style predictor

## What is a Jupyter Notebook?

A Jupyter Notebook is an interactive document that combines three important elements:

**Text Cells**: These cells (like the one you're reading now) contain formatted text, explanations, and instructions. They're written in Markdown format.

**Code Cells**: These cells contain Python code that you can execute directly in the notebook.

**Output Cells**: When you run code cells, the results appear immediately below them.

### How to Use This Notebook

Let's learn how to interact with this notebook:

1. **Reading Content**: Simply scroll through to read the explanations
2. **Running Code**: Click on a code cell and press `Shift + Enter` to execute it
3. **Editing Code**: Click inside a code cell to modify its contents
4. **Creating New Cells**: Use the + button in the toolbar to add cells

**Try it now**: Run the code cell below by clicking on it and pressing `Shift + Enter`.

---

## Your First Python Program

Let's start with the traditional first program that every programmer writes. This program simply displays a message on the screen.

**Task**: Run the code cell below to see your first program in action.

```python exec
id: tutorial-00-getting-started-page-1-1
# This is a comment - Python ignores everything after the # symbol
# Comments help us explain what our code does

# The print() function displays text on the screen
print("Hello, World!")
print("Welcome to Programming & Design Principles!")
```

### Understanding What Just Happened


**The `print()` Function**: This is a built-in Python function that displays information to the user. Think of it as Python's way of "speaking" to you.

**Strings**: The text inside the quotes (" ") is called a **string**. Strings are sequences of characters that represent text.

**Comments**: Lines starting with `#` are comments. Python ignores these completely - they're just for humans to read and understand the code.

**Why Comments Matter**: As your programs become more complex, comments help you (and others) understand what each part does. It's like leaving notes for your future self!

---

## Basic Python Concepts

Now let's explore some fundamental programming concepts that form the foundation of all programs.

### 1. Printing Output

The `print()` function is one of the most important tools we have. Let's explore what we can do with it.

```python exec
id: tutorial-00-getting-started-page-1-2
# We can print multiple lines
print("Line 1: Introduction")
print("Line 2: Body")
print("Line 3: Conclusion")

# We can print numbers directly
print(42)
print(3.14159)

# We can print the results of calculations
print(10 + 5)
```

### 2. Variables - Storing Information

Variables are like labeled containers that store data. They're one of the most important concepts in programming. Think of a variable as a box with a label on it - you can put something inside the box and refer to it by the label whenever you need it.

### Foundation: Understanding Variable Names

When we create variables, we should use descriptive names that clearly indicate what the variable contains. This makes our code much easier to understand.

**Good variable names**:
- `student_score` (tells us this contains a student's score)
- `learning_rate` (clearly indicates this is a learning rate parameter)
- `number_of_iterations` (describes what the number represents)

**Poor variable names**:
- `x` (what does x represent?)
- `temp` (temporary what?)
- `data` (what kind of data?)

Let's see variables in action:

```python exec
id: tutorial-00-getting-started-page-1-3
# Creating variables with descriptive names
programming_language = "Python"
version_number = 3.11
is_beginner_friendly = True

# Using variables in print statements
print("Language:", programming_language)
print("Version:", version_number)
print("Beginner friendly?", is_beginner_friendly)
```

### Think About It

**Question**: Why do you think using descriptive variable names like `programming_language` is better than using short names like `lang` or just `p`?

**Reflection**: Write your thoughts in the cell below (double-click to edit).

*Your answer here:*

(Double-click this cell to write your thoughts)

### 3. Basic Mathematics

Python can perform calculations just like a calculator. This is essential for machine learning, where we often need to process numerical data and apply mathematical formulas.

Let's explore the mathematical operators available in Python:

```python exec
id: tutorial-00-getting-started-page-1-4
# Basic arithmetic operations
print("Addition: 5 + 3 =", 5 + 3)
print("Subtraction: 10 - 4 =", 10 - 4)
print("Multiplication: 6 * 7 =", 6 * 7)
print("Division: 15 / 3 =", 15 / 3)

# Using variables in calculations
first_number = 10
second_number = 5
sum_result = first_number + second_number

print("\nUsing variables:")
print("First number:", first_number)
print("Second number:", second_number)
print("Sum:", sum_result)
```

### Practice: Variable Naming

**Challenge**: In the code cell below, create three variables to store information about a machine learning model:
1. The accuracy of the model (use a number between 0 and 1)
2. The number of training examples used
3. Whether the model has been trained or not (True/False)

Use descriptive variable names and print all three values.

```python exec
id: tutorial-00-getting-started-page-1-5
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
# Your code here:
# Create three variables with descriptive names
```

## What we set out to do

These were the aims of this notebook. Now that you have worked through it, they are a check on what happened rather than a promise about it.

By completing this tutorial, you will be able to:
1. Run Python code in Jupyter notebooks
2. Use the `print()` function to display output
3. Create and use variables with meaningful names
4. Perform basic mathematical operations
5. Write comments to document your code
6. Create simple prediction systems using linear equations

---

## Looking back

Before leaving this page, a sentence on each. What you write stays on this device.

```reflect
- Something you expected before running a cell that turned out differently
- The one idea from this page you could explain to someone else now
- Something you would change or try next, if there were time
- A question this page raised for you that it did not answer. Bring it to the next session; these questions are where the next session starts.
```
