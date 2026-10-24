---
title: "tutorial-00-getting-started-page-2 (2 of 2)"
slug: tutorial-00-getting-started-page-2
course: programming-and-design-principles
course_title: "Programming and Design Principles"
series: tutorials
series_title: "Tutorials"
version: 2026.09.06.1
---

---

## Your First ML-Themed Program

Now let's create something more interesting - a simple prediction system using a linear equation. This is the foundation of many machine learning algorithms!

### The Problem

Imagine we want to predict a student's exam score based on how many hours they study. Based on historical data, we've determined that there's a relationship between study hours and exam performance.

We can express this relationship as a mathematical formula:

**Predicted Score = (Study Hours × 10) + 20**

This is called a **linear model** - one of the simplest and most important concepts in machine learning!

### Understanding the Model

Let's break down our prediction formula:
- **Study Hours × 10**: Each hour of study contributes 10 points to the score
- **+ 20**: This is the base score (like natural ability or prior knowledge)
- **Together**: They give us a prediction of the final exam score

Let's implement this prediction system:

```python exec
id: tutorial-00-getting-started-page-2-1
# Simple Linear Prediction System
# This demonstrates a basic ML concept: using a mathematical model to make predictions

# Input: The number of hours a student studies per week
study_hours = 5

# Model: Our prediction formula (the "trained" model)
# Each study hour contributes 10 points, plus a base score of 20
predicted_score = (study_hours * 10) + 20

# Output: Display our prediction
print("=== Student Score Predictor ===")
print("Study Hours per Week:", study_hours)
print("Predicted Exam Score:", predicted_score)
print("================================")
```

### Understanding the Three Components

This simple program demonstrates the three key components of any machine learning system:

1. **Input**: `study_hours = 5` - This is our input data (also called a "feature" in ML)
2. **Model**: `(study_hours * 10) + 20` - This is our prediction formula (the "trained" model)
3. **Output**: `predicted_score` - This is our prediction (what the model thinks will happen)

Even though this is a very simple example, this is exactly how more complex machine learning systems work! They take input data, apply a mathematical model, and produce predictions.

### Practice: Modifying the Predictor

**Challenge**: Modify the code above to predict scores for different study hours:
1. What score would you predict for someone who studies 8 hours per week?
2. What about 3 hours per week?
3. What about 12 hours per week?

Copy the code to the cell below and experiment with different values:

```python exec
id: tutorial-00-getting-started-page-2-2
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
# Your experimentation here:
# Try different values for study_hours and see how the prediction changes
```

### Think About It

**Question**: What happens to the predicted score as study hours increase? Does this make sense intuitively?

**Question**: What might be limitations of this simple model? Can you think of factors that might affect a student's score that aren't captured by study hours alone?

Write your thoughts below:

*Your reflections here:*

(Double-click to edit)

---

## Practice Exercises

Now let's apply what you've learned! These exercises will help reinforce the concepts we've covered.

### Your turn: Personalized Greeting

**Task**: Create variables for your name and favorite aspect of programming, then print a personalized greeting.

**Requirements**:
- Use descriptive variable names
- Add comments explaining your code
- Use the print() function to display your message

```python exec
id: tutorial-00-getting-started-page-2-3
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
# Foundation Exercise: Personalized Greeting
# Your code here:
```

### Your turn: Learning Rate Calculator

**Background**: In machine learning, we often need to calculate how much a model should adjust its parameters during training. This is called the learning rate adjustment.

**Task**: Create a simple calculator that computes an adjusted learning rate:
- Start with an initial learning rate of 0.1
- Apply a decay factor of 0.95
- Calculate the new learning rate: `new_rate = initial_rate * decay_factor`
- Print both the initial and adjusted learning rates with descriptive labels

**Requirements**:
- Use meaningful variable names (not `x`, `y`, `temp`, etc.)
- Add comments explaining each step
- Display results with clear labels

```python exec
id: tutorial-00-getting-started-page-2-4
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
# Practice Exercise: Learning Rate Calculator
# Your code here:
```

### Try this Exercise: Multi-Feature Predictor

**Background**: Real machine learning models often use multiple features (inputs) to make predictions. Let's extend our exam score predictor to use two features.

**Task**: Create a predictor that estimates exam scores based on both study hours AND class attendance.

Use this formula:
**Predicted Score = (Study Hours × 8) + (Attendance Percentage × 0.3) + 10**

**Example inputs**:
- Study hours: 6
- Attendance percentage: 85 (meaning 85% attendance)

**Requirements**:
- Create variables for both inputs with descriptive names
- Calculate the predicted score using the formula
- Display all values (both inputs and the prediction) with clear labels
- Add comments explaining the calculation

```python exec
id: tutorial-00-getting-started-page-2-5
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
# Challenge Exercise: Multi-Feature Predictor
# Your code here:
```

---

## Common Mistakes to Avoid

As you begin your programming journey, here are some common mistakes that beginners make. Being aware of these will help you write better code from the start.

### Mistake 1: Using Single-Letter Variable Names

**Problem**:

```python exec
id: tutorial-00-getting-started-page-2-6
# Less than wonderful: Hard to understand
x = 5
y = x * 10 + 20
print(y)  # What does this number mean?
```

**Solution**:

```python exec
id: tutorial-00-getting-started-page-2-7
# GOOD: Clear and descriptive
study_hours = 5
predicted_score = (study_hours * 10) + 20
print("Predicted Score:", predicted_score)  # Now we know what this represents!
```

### Mistake 2: Forgetting to Add Comments

**Problem**:

```python exec
id: tutorial-00-getting-started-page-2-8
# Less than wonderful: No explanation of what this does
initial_value = 100
decay = 0.95
result = initial_value * decay
print(result)
```

**Solution**:

```python exec
id: tutorial-00-getting-started-page-2-9
# GOOD: Clear comments explain the purpose
# Calculate adjusted learning rate with decay
initial_learning_rate = 100
decay_factor = 0.95

# Apply decay to get new learning rate
adjusted_learning_rate = initial_learning_rate * decay_factor

print("Adjusted Learning Rate:", adjusted_learning_rate)
```

### Mistake 3: Not Using Descriptive Output Messages

**Problem**:

```python exec
id: tutorial-00-getting-started-page-2-10
# less than wonderful: Just printing numbers without context
training_examples = 1000
test_examples = 200
print(training_examples)
print(test_examples)
```

**Solution**:

```python exec
id: tutorial-00-getting-started-page-2-11
# GOOD: Clear labels for each value
training_examples = 1000
test_examples = 200

print("=== Dataset Information ===")
print("Training examples:", training_examples)
print("Test examples:", test_examples)
print("=========================")
```

---

## Key Takeaways


### Programming Concepts

**Sequential Execution**: Python code runs line by line, from top to bottom. Each statement is executed in order.

**Variables**: Containers for storing data values. Always use descriptive names that clearly indicate what the variable contains.

**Operators**: Symbols that perform operations on values (like +, -, *, /).

**Functions**: Reusable blocks of code that perform specific tasks. We've used `print()` to display output.

**Comments**: Lines starting with # that explain code to humans. Python ignores these, but they're crucial for understanding.

### Machine Learning Concepts Introduced

**Input**: Data we feed into our system (like study hours).

**Model**: Mathematical formula or set of rules (like our prediction equation).

**Prediction**: Output from our system (like the predicted exam score).

**Linear Equations**: Simple mathematical relationships that form the foundation of many ML algorithms.

### Best Practices You've Learned

1. Use descriptive variable names (not single letters)
2. Add comments to explain your code
3. Use clear, labeled output messages
4. Organize your code logically
5. Test your code with different inputs

---

## Next Steps


### Self-Assessment Checklist

Can you do all of the following? Check each item:

- [ ] Run code cells in Jupyter notebooks
- [ ] Use the `print()` function to display information
- [ ] Create variables with descriptive names
- [ ] Perform basic mathematical calculations
- [ ] Write comments to explain code
- [ ] Understand the three components of our simple ML system (input, model, output)
- [ ] Modify existing code to test different values

If you can't check all these boxes, review the relevant sections above and practice more before continuing.

### Before Tutorial 1

To prepare for the next tutorial, you might want to:
- Experiment with the code examples above by changing values
- Try creating your own simple predictor for a different scenario
- Think about how mathematical formulas could be used to make other types of predictions

### What's Coming in Tutorial 1?

In the next tutorial, **The Evolution of Programming & ML Basics**, you'll explore:

- The fascinating history of programming languages
- How computers understand and execute code
- Different types of programming languages and their characteristics
- The evolution of machine learning and AI
- Why Python became the dominant language for ML

---

## Reflection Questions

Before moving on, take a moment to reflect on what you've learned. Write your thoughts in the cell below:

1. What concept from this tutorial did you find most interesting?
2. What was challenging for you?
3. How might you use simple prediction formulas in other areas of your life?
4. What questions do you still have about programming or machine learning?

**Your Reflections:**

(Double-click this cell to write your thoughts)

1. Most interesting:

2. Most challenging:

3. Real-world applications:

4. Questions I have:

## Looking back

Before leaving this page, a sentence on each. What you write stays on this device.

```reflect
- Something you expected before running a cell that turned out differently
- The one idea from this page you could explain to someone else now
- Something you would change or try next, if there were time
- A question this page raised for you that it did not answer. Bring it to the next session; these questions are where the next session starts.
```

---

## Additional Resources

If you'd like to explore further, here are some helpful resources:

**Python Documentation**: https://docs.python.org - Official Python documentation

**Jupyter Notebook Guide**: https://jupyter-notebook.readthedocs.io - Comprehensive guide to Jupyter

**Practice Platform**: https://www.hackinscience.org - Interactive Python exercises

**Python Tutor**: http://pythontutor.com - Visualize code execution step by step

---

**Remember**: Every expert programmer started exactly where you are now. The key to success is consistent practice and maintaining curiosity. Don't be afraid to experiment and make mistakes - that's how we learn!

**Ready for Tutorial 1?** When you're comfortable with the concepts in this tutorial, move on to explore the history of programming and machine learning.

---

**End of Tutorial 0**
