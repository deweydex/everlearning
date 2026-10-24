---
title: "Tutorial 4: Selection and Decision Making (1 of 3)"
slug: tutorial-04-making-decisions-page-1
course: programming-and-design-principles
course_title: "Programming and Design Principles"
series: tutorials
series_title: "Tutorials"
version: 2026.09.06.1
---

# Tutorial 4: Selection and Decision Making

**Module**: Programming & Design Principles 5N2927
**Level**: QQI Level 5
**Theme**: Thresholds, decision rules and classification

---

## Introduction: Programs That Choose

Every program you have written so far runs from the top to the bottom, one line after another. That is enough for a calculation, and not enough for a decision. A machine learning system does not only compute a score; it has to act on it. A spam filter computes how spam-like an email looks and then decides whether to hide it. A medical model computes a risk and then decides whether to flag the patient. The score is arithmetic, which Tutorial 3 covered. The decision is *selection*, and it is what this tutorial is about.

Selection means running one piece of code or another depending on whether a condition is true. Python spells it `if`. By the end you will have written a small decision tree by hand, and seen that a decision tree from a machine learning library is the same thing, only with the thresholds chosen by data instead of by you.

## Part 1: Conditions Are Values

### Exploration 1.1: True and False

A comparison is an expression, and its value is one of two things. Let's look at a few and see what comes back.

```python exec
id: tutorial-04-making-decisions-page-1-1
study_hours = 12
attendance = 87.5

print(study_hours > 10)
print(attendance >= 90)
print(study_hours == 12)
print(attendance != 100)
print(type(study_hours > 10))
```

Each line prints `True` or `False`. These two words are values of a type called *boolean* (named after George Boole, who wrote the algebra of true and false in the 1850s). A boolean is as much a value as the number 12 is. It can be stored in a variable, printed, and, in a moment, used to choose what happens next.

Notice the difference between `=` and `==`. One equals sign *stores* a value in a name. Two equals signs *ask* whether two values are the same. Mixing them up is the most common mistake in this tutorial, and Python usually refuses to run the wrong one, so the error message will tell you.

### Exploration 1.2: Combining Conditions

Three words combine booleans: `and`, `or` and `not`. Rather than memorise their rules, let's print them.

```python exec
id: tutorial-04-making-decisions-page-1-2
print("a      b      a and b   a or b   not a")
for a in (True, False):
    for b in (True, False):
        print(f"{a!s:6} {b!s:6} {a and b!s:9} {a or b!s:8} {not a!s}")
```

This table is a *truth table*: every combination of inputs, with the output beside it. Reading down the columns, `and` is `True` only when both sides are true, `or` is `True` when at least one side is true, and `not` flips whatever it is given. (The loop that produced the table is the subject of Tutorial 5; for now it is only a way of printing four rows without writing them out.)

### Your Turn 1.1

A student is eligible for a bonus mark when their attendance is at least 80 percent **and** they studied more than 10 hours a week. Write the condition as one boolean expression, store it in a variable called `eligible`, and print it. Then change the numbers until it flips.

```python exec
id: tutorial-04-making-decisions-page-1-3
hint: Two comparisons joined by the word that needs both to be true.
know: with the values as given, `eligible` prints `True`; change attendance to 79.9 and it prints `False`.
attendance = 87.5
study_hours = 12

# Your code here: eligible = ...
```

```python exec
id: tutorial-04-making-decisions-page-1-3-check
# When you have an answer above, run this cell.
check(eligible, True, label="values as given")
```

<details class="dl-answer"><summary>answer</summary>

```python
eligible = attendance >= 80 and study_hours > 10
print(eligible)
```

Both conditions hold for the values given, so `and` gives `True`. The common mistake is `or`, which is `True` whenever either side is, so a student with perfect attendance and no study would be eligible. To make it flip, 79.9 for attendance is enough, because 79.9 is not at least 80.

</details>

## Part 2: The if Statement

### Exploration 2.1: A Threshold Classifier

Tutorial 3 built a prediction score from study hours. The simplest possible classifier turns that score into a label with one threshold. Let's write it.

```python exec
id: tutorial-04-making-decisions-page-1-4
study_hours = 12
prediction = study_hours * 3.5 + 30   # the formula from Tutorial 3

if prediction >= 70:
    print("Likely to pass")

print(f"Prediction score: {prediction}")
```

### Structural Analysis

Look at the shape of the `if` before reading on. There are three parts, and each matters.

First comes the keyword `if`, then a condition, then a colon. The colon says "the block that belongs to this condition starts on the next line". Then the block itself, indented by four spaces. Everything indented under the `if` runs only when the condition is true. Finally, the first line that is *not* indented, the second `print`, is outside the block, so it runs every time.

### Investigation

Try changing `study_hours` to 8 and running the cell again. What is printed, and what is not? Then change the threshold from 70 to 60. Where in the code did the *decision rule* live, and where did the *data* live?

### Your Turn 2.1

Write an `if` that prints a warning when `attendance` is below 75. Test it with a value that triggers the warning and one that does not.

```python exec
id: tutorial-04-making-decisions-page-1-5
hint: The condition is "below 75", so the comparison is `<`, and the block under it is the print.
know: with attendance at 68.0 a warning is printed; set it to 75.0 and nothing is printed, because 75 is not below 75.
attendance = 68.0

# Your code here
```

<details class="dl-answer"><summary>answer</summary>

```python
if attendance < 75:
    print("Warning: attendance is below 75 percent")
```

There is no `else`, because nothing needs to happen when attendance is fine. Try 75.0 as well as 68.0: 75 is not below 75, so nothing prints, which is the boundary this rule has.

</details>

## Part 3: if and else

### Exploration 3.1: Two Outcomes

A threshold usually has two sides. `else` gives the second side a block of its own.

```python exec
id: tutorial-04-making-decisions-page-1-6
spam_score = 0.83   # a score between 0 and 1 from a spam filter

if spam_score > 0.5:
    label = "spam"
else:
    label = "not spam"

print(f"Score {spam_score} -> {label}")
```

Exactly one of the two blocks runs. There is no value of `spam_score` for which both run, and none for which neither does, which is what makes `if`/`else` a *binary* decision. That is worth noticing because it is what a test has to cover: one case for each side, and one right on the boundary.

### Investigation: The Boundary

What does `0.5` itself produce? Read the condition again before running it. Then change `>` to `>=` and see which way the boundary moves. In a real filter this choice decides whether a borderline email is hidden, so it is never an accident.

### Your Turn 3.1

A model's output is a probability that a loan will be repaid. Write an `if`/`else` that stores `"approve"` when the probability is at least 0.7 and `"refer to a person"` otherwise. Print the decision.

**A question before moving on.** This program makes a judgement about a person. Who chose the threshold, and what happens to the person just on the wrong side of it? What does the program not know about them? What would you want said to them? Write a sentence or two; there is no right answer, and the question is the point.

Then the harder part. Somebody decided that 0.7 is the line, and somebody with a probability of 0.69 is refused by a machine that will never meet them. Who should choose that number, what might the model not know about the person, and what would you want the refusal to say? Write two or three sentences under your code. Programs that decide about people are the ones most worth questioning, and this course will keep asking.

```python exec
id: tutorial-04-making-decisions-page-1-7
hint: "At least 0.7" is `>=`, and the two outcomes are the two branches of an if and an else.
know: 0.64 prints `refer to a person`; 0.7 prints `approve`, because the condition is "at least".
repay_probability = 0.64

# Your code here
```

```python exec
id: tutorial-04-making-decisions-page-1-7-check
# When you have an answer above, run this cell.
check(decision, "refer to a person", label="with 0.64")
```

<details class="dl-answer"><summary>answer</summary>

```python
if repay_probability >= 0.7:
    decision = "approve"
else:
    decision = "refer to a person"
print(decision)
```

With 0.64 the first condition is false, so the `else` runs. Change the value to 0.7 and it is approved, because `>=` includes the boundary; change `>=` to `>` and 0.7 is referred instead. Which of those two the bank meant is exactly the question the paragraph above asked.

</details>

## What we set out to do

These were the aims of this notebook. Now that you have worked through it, they are a check on what happened rather than a promise about it.

- Write boolean expressions and read a truth table (LO 4)
- Use `if`, `if`/`else` and `elif` chains to choose between actions (LO 6)
- Combine and nest conditions, and decide which of the two reads better (LO 6)
- Design a test for every branch of a decision, and find the branch a test missed (LO 9, LO 10)
- Write a documented program that turns a prediction into a decision (LO 7, LO 11)

---

## Looking back

Before leaving this page, a sentence on each. What you write stays on this device.

```reflect
- Something you expected before running a cell that turned out differently
- The one idea from this page you could explain to someone else now
- Something you would change or try next, if there were time
- A question this page raised for you that it did not answer. Bring it to the next session; these questions are where the next session starts.
```
