---
title: "tutorial-04-making-decisions-page-2 (2 of 3)"
slug: tutorial-04-making-decisions-page-2
course: programming-and-design-principles
course_title: "Programming and Design Principles"
series: tutorials
series_title: "Tutorials"
version: 2026.09.06.1
---

Before starting this page, run the cell below. It repeats the imports and definitions from the earlier pages that this page uses.

```python exec
id: tutorial-04-making-decisions-page-2-setup
study_hours = 12
attendance = 87.5

print(study_hours > 10)
print(attendance >= 90)
print(study_hours == 12)
print(attendance != 100)
print(type(study_hours > 10))
```

## Part 4: More Than Two Outcomes with elif

### Exploration 4.1: Grade Bands

Many decisions have several outcomes. A chain of `elif` (short for "else if") checks conditions one after another and runs the first block whose condition is true.

```python exec
id: tutorial-04-making-decisions-page-2-1
score = 73

if score >= 80:
    band = "Distinction"
elif score >= 65:
    band = "Merit"
elif score >= 50:
    band = "Pass"
else:
    band = "Not yet"

print(f"{score} -> {band}")
```

### Investigation: Order Matters

The conditions are checked from the top, and the chain stops at the first one that is true. A score of 73 is also `>= 50`, but the chain never gets that far, because `>= 65` was true first. Let's see what happens when the order is wrong.

```python exec
id: tutorial-04-making-decisions-page-2-2
score = 73

if score >= 50:
    band = "Pass"
elif score >= 65:
    band = "Merit"
elif score >= 80:
    band = "Distinction"
else:
    band = "Not yet"

print(f"{score} -> {band}   (wrong: the first condition catches everything above 50)")
```

Every score of 50 or more is called a Pass, and the Merit and Distinction blocks can never run. Code that can never run is called *unreachable*, and Python will not warn you about it. The order of an `elif` chain is part of the logic, so when the bands are thresholds, write them from the highest down (or from the lowest up with `<`), and never mixed.

### Your Turn 4.1

A classifier reports a confidence between 0 and 1. Write an `elif` chain that describes it in words: at least 0.9 is `"very confident"`, at least 0.7 is `"confident"`, at least 0.5 is `"unsure"`, and anything lower is `"guessing"`. Test it with 0.95, 0.7, 0.5 and 0.2, and say which of those four is a boundary case.

```python exec
id: tutorial-04-making-decisions-page-2-3
hint: Write the bands from the highest down, so that the first true condition is the right one.
know: 0.95, 0.7, 0.5 and 0.2 give `very confident`, `confident`, `unsure`, `guessing`. The boundary cases are 0.7 and 0.5, which each land on the higher band.
confidence = 0.7

# Your code here
```

```python exec
id: tutorial-04-making-decisions-page-2-3-check
# When you have an answer above, run this cell.
check([describe(c) for c in (0.95, 0.7, 0.5, 0.2)], ["very confident", "confident", "unsure", "guessing"])
```

<details class="dl-answer"><summary>answer</summary>

```python
def describe(confidence):
    if confidence >= 0.9:
        return "very confident"
    elif confidence >= 0.7:
        return "confident"
    elif confidence >= 0.5:
        return "unsure"
    else:
        return "guessing"

for value in (0.95, 0.7, 0.5, 0.2):
    print(value, describe(value))
```

Writing it as a function lets the check call it four times. The boundary cases are 0.7 and 0.5: each is "at least" its band, so each lands on the higher one. Written from the lowest band up with `>=`, every value would be caught by the first condition, which is the error from Part 4.

</details>

## Part 5: Combining and Nesting Conditions

### Exploration 5.1: Two Ways to Say the Same Thing

A decision that depends on two things can be written as one condition with `and`, or as one `if` inside another. Both are correct. Let's write both and compare how they read.

```python exec
id: tutorial-04-making-decisions-page-2-4
attendance = 85.0
average_grade = 62.0

# Version A: one combined condition
if attendance >= 80 and average_grade >= 60:
    print("A: eligible for the advanced group")
else:
    print("A: not eligible")

# Version B: one condition nested inside another
if attendance >= 80:
    if average_grade >= 60:
        print("B: eligible for the advanced group")
    else:
        print("B: attendance is fine, but the grade is below 60")
else:
    print("B: attendance is below 80")
```

Version A is shorter. Version B can say *why* somebody was not eligible, because each condition has its own `else`. Neither is better in general; the question to ask is what the reader of the output needs to know. When a program only needs the yes or no, combine the conditions. When it needs to explain the no, nest them.

Nesting deeper than two or three levels is hard to read, and when you find yourself there, an `elif` chain or a combined condition usually says the same thing more plainly.

### Your Turn 5.1

A student passes the module when they scored at least 50 in the exam **or** at least 60 in the project, **and** their attendance was at least 70. Write the condition once with `and`/`or`, and be careful with brackets: `a or b and c` does not mean what it looks like, because `and` binds more tightly than `or`. Print the decision for a few students.

```python exec
id: tutorial-04-making-decisions-page-2-5
hint: Put the `or` inside brackets. `and` binds more tightly than `or`, so without brackets Python reads `a or (b and c)`.
know: the student as given passes (the project rescues the exam, and attendance is over 70). Set attendance to 69 and they do not, whatever the marks.
exam = 45
project = 68
attendance = 74

# Your code here
```

```python exec
id: tutorial-04-making-decisions-page-2-5-check
# When you have an answer above, run this cell.
check(passed, True, label="student as given")
```

<details class="dl-answer"><summary>answer</summary>

```python
passed = (exam >= 50 or project >= 60) and attendance >= 70
print(passed)
```

The brackets are the whole exercise. Without them, `exam >= 50 or project >= 60 and attendance >= 70` means "exam at least 50, or (project at least 60 and attendance at least 70)", so a student with a good exam and no attendance would pass. With attendance at 69 the student as given fails whatever the marks, which is what the rule says.

</details>

## Part 6: A Decision Tree by Hand

### Exploration 6.1: Classifying Flowers with Nested Ifs

A *decision tree* is a classifier made entirely of questions with yes or no answers. Each question splits the data, and the leaves at the bottom are the labels. Here is one for three species of iris, using two measurements in centimetres. The thresholds are the ones a standard library finds on the well-known iris dataset; here we write them by hand.

```python exec
id: tutorial-04-making-decisions-page-2-6
def classify_iris(petal_length, petal_width):
    '''Return the species predicted by a two-question decision tree.'''
    if petal_length < 2.45:
        return "setosa"
    else:
        if petal_width < 1.75:
            return "versicolor"
        else:
            return "virginica"

samples = [(1.4, 0.2), (4.7, 1.4), (5.9, 2.3), (2.5, 1.0), (4.9, 1.8)]
for length, width in samples:
    print(f"petal {length} x {width} cm -> {classify_iris(length, width)}")
```

That function *is* a decision tree. The only thing a machine learning library adds is a way of choosing the thresholds 2.45 and 1.75 from data instead of from a person. When you meet decision trees later, remember that you have already written one, and that reading a trained tree is reading nested `if` statements.

### Your Turn 6.1

Add a third measurement. If the species is `"virginica"` but the petal length is below 4.9, return `"virginica (check)"` instead, so that a borderline sample is flagged for a person to look at. Run the samples again and see which one changes.

```python exec
id: tutorial-04-making-decisions-page-2-7
hint: The new question sits inside the `else` that returns "virginica": one more `if` there, before the return.
know: only the sample `(4.9, 1.8)` changes, to `virginica (check)`.
# Your code here: copy classify_iris and extend it
```

```python exec
id: tutorial-04-making-decisions-page-2-7-check
# When you have an answer above, run this cell.
check(classify_iris(4.9, 1.8), "virginica (check)", label="the borderline sample")
```

<details class="dl-answer"><summary>answer</summary>

```python
def classify_iris(petal_length, petal_width):
    if petal_length < 2.45:
        return "setosa"
    else:
        if petal_width < 1.75:
            return "versicolor"
        else:
            if petal_length < 4.9:
                return "virginica (check)"
            return "virginica"

for length, width in samples:
    print(f"petal {length} x {width} cm -> {classify_iris(length, width)}")
```

Only the sample `(4.9, 1.8)` changes. Notice that 4.9 is not below 4.9, so if your version flagged it, the comparison was `<=` rather than `<`. Three questions deep is about as far as nested conditions stay readable; a fourth would be a case for rewriting.

</details>

## Part 7: Selection Inside a Machine Learning Program

### Exploration 7.1: Choosing an Activation Function

In the AI and ML Foundations course you will build a neural network, and one of its settings is the *activation function*, the function applied to each neuron's sum. Code that supports more than one activation has to choose between them, and it does so with exactly the selection you have been writing. Let's write a small version.

```python exec
id: tutorial-04-making-decisions-page-2-8
import math

def activate(value, name):
    '''Apply the activation function called `name` to `value`.'''
    if name == "relu":
        return max(0.0, value)
    elif name == "sigmoid":
        return 1 / (1 + math.exp(-value))
    elif name == "linear":
        return value
    else:
        return None   # an unknown name: Part 8 improves on this

for name in ("relu", "sigmoid", "linear", "step"):
    print(f"{name:8} of -2.0 -> {activate(-2.0, name)}")
```

The comparison here is between *strings*: `name == "relu"` is true when the two pieces of text are identical, capital letters included. That is why an unexpected spelling falls through to the `else`. Returning `None` is a quiet way of saying "I did not recognise that", and quiet is not always good, which is the subject of the next part.

### Your Turn 7.1

Add a `"tanh"` branch using `math.tanh`, and a `"step"` branch that returns 1 when the value is positive and 0 otherwise. Check each with a positive and a negative value.

```python exec
id: tutorial-04-making-decisions-page-2-9
hint: Two more `elif` branches. `math.tanh` exists; the step function is a comparison that returns 1 or 0.
# Your code here
```

```python exec
id: tutorial-04-making-decisions-page-2-9-check
# When you have an answer above, run this cell.
check(round(activate(2.0, "tanh"), 3), 0.964, label="tanh of 2.0")
check(activate(-0.5, "step"), 0, label="step of -0.5")
```

<details class="dl-answer"><summary>answer</summary>

```python
def activate(value, name):
    if name == "relu":
        return max(0.0, value)
    elif name == "sigmoid":
        return 1 / (1 + math.exp(-value))
    elif name == "tanh":
        return math.tanh(value)
    elif name == "step":
        return 1 if value > 0 else 0
    elif name == "linear":
        return value
    else:
        return None

for name in ("tanh", "step"):
    print(name, activate(2.0, name), activate(-2.0, name))
```

The step function is the oldest activation there is and the one nobody uses now, because a derivative of zero everywhere gives training nothing to work with; Part 5 of the AI course says why. Note that `step` returns 0 at exactly 0, which is a choice: the exercise said "positive".

</details>

## Part 8: Validating Inputs and Settings

### Exploration 8.1: Refusing Bad Settings Early

A training run can take hours, so a program should check its settings before it starts rather than fail half way through. A *hyperparameter* is a setting chosen by the person, such as the learning rate or the number of epochs, as opposed to a parameter learned from data. Let's validate two of them.

```python exec
id: tutorial-04-making-decisions-page-2-10
learning_rate = 1.5
epochs = 20

problems = []

if not (0 < learning_rate <= 1):
    problems.append(f"learning_rate must be between 0 and 1, got {learning_rate}")

if type(epochs) is not int or epochs <= 0:
    problems.append(f"epochs must be a positive whole number, got {epochs}")

if problems:
    print("Cannot start training:")
    for problem in problems:
        print(" -", problem)
else:
    print("Settings look fine; starting training")
```

Two things in this cell are worth a second look. `0 < learning_rate <= 1` is a *chained comparison*: Python reads it as "0 is less than the rate, and the rate is at most 1", which is the way a mathematician would write it. And `if problems:` has no comparison at all. A list is treated as `True` when it has something in it and `False` when it is empty, so the line reads "if there are any problems". Numbers behave the same way: zero counts as `False`, anything else as `True`. This is called *truthiness*, and it is convenient in exactly this kind of check.

### Your Turn 8.1

Add a check that `batch_size` is a positive whole number no larger than the number of training examples, `n_examples`. Then set the values so that all three checks fail at once and confirm that all three messages appear.

```python exec
id: tutorial-04-making-decisions-page-2-11
hint: A third `if` in the same shape as the first two, with two conditions joined by `or`, since either one is a problem.
learning_rate = 0.1
epochs = 20
batch_size = 500
n_examples = 300

# Your code here
```

```python exec
id: tutorial-04-making-decisions-page-2-11-check
# When you have an answer above, run this cell.
check(len(problems), 3, label="number of problems found")
```

<details class="dl-answer"><summary>answer</summary>

```python
problems = []

if not (0 < learning_rate <= 1):
    problems.append(f"learning_rate must be between 0 and 1, got {learning_rate}")

if type(epochs) is not int or epochs <= 0:
    problems.append(f"epochs must be a positive whole number, got {epochs}")

if type(batch_size) is not int or batch_size <= 0 or batch_size > n_examples:
    problems.append(f"batch_size must be a positive whole number no larger than {n_examples}, got {batch_size}")

if problems:
    print("Cannot start training:")
    for problem in problems:
        print(" -", problem)
else:
    print("Settings look fine; starting training")
```

To make all three fail at once, learning_rate 1.5, epochs 0 and batch_size 500 will do. The order of the three `or` conditions in the batch check matters a little: `type(batch_size) is not int` is tested first so that a value like `"500"` is caught before it is compared to a number, which would be an error.

</details>

## Looking back

Before leaving this page, a sentence on each. What you write stays on this device.

```reflect
- Something you expected before running a cell that turned out differently
- The one idea from this page you could explain to someone else now
- Something you would change or try next, if there were time
- A question this page raised for you that it did not answer. Bring it to the next session; these questions are where the next session starts.
```
