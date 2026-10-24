---
title: "tutorial-04-making-decisions-page-3 (3 of 3)"
slug: tutorial-04-making-decisions-page-3
course: programming-and-design-principles
course_title: "Programming and Design Principles"
series: tutorials
series_title: "Tutorials"
version: 2026.09.06.1
---

Before starting this page, run the cell below. It repeats the imports and definitions from the earlier pages that this page uses.

```python exec
id: tutorial-04-making-decisions-page-3-setup
import math

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

## Part 9: Testing Every Branch

### Exploration 9.1: Branch Coverage

A decision has as many paths as it has branches, and a test that only tries one path has only tested one path. The habit worth building is to list the branches first, then write one test per branch, then one more for each boundary. Let's do that for the grade bands from Part 4.

```python exec
id: tutorial-04-making-decisions-page-3-1
def grade_band(score):
    if score >= 80:
        return "Distinction"
    elif score >= 65:
        return "Merit"
    elif score >= 50:
        return "Pass"
    else:
        return "Not yet"

# one test per branch, plus each boundary
tests = [
    (95, "Distinction"),
    (80, "Distinction"),   # boundary
    (79, "Merit"),         # just below a boundary
    (65, "Merit"),         # boundary
    (50, "Pass"),          # boundary
    (49, "Not yet"),
    (0,  "Not yet"),
]

for score, expected in tests:
    result = grade_band(score)
    status = "ok " if result == expected else "FAIL"
    print(f"{status}  grade_band({score}) = {result!r}, expected {expected!r}")
```

Every branch runs at least once, and every threshold is tested from both sides. When a test line says FAIL, the table tells you which branch is wrong before you open the function. This is the testing process LO 10 asks for, applied to selection.

### Exploration 9.2: Three Errors to Recognise

Let's meet the common mistakes on purpose, so that their error messages are familiar when they arrive uninvited. Each cell below is *meant* to fail or misbehave; read the message, then fix the line.

```python exec
id: tutorial-04-making-decisions-page-3-2
# Error 1: assignment where a comparison was meant.
# Python refuses to run this, which is helpful. Fix it and run again.
score = 73
try:
    exec("if score = 73:\n    print('equal')")
except SyntaxError as error:
    print("SyntaxError:", error)
```

```python exec
id: tutorial-04-making-decisions-page-3-3
# Error 2: an indentation mistake. The second print looks like part of the if, and is not.
score = 40
if score >= 50:
    print("passed")
print("well done")      # runs whatever the score is; indent it to make it part of the block
```

```python exec
id: tutorial-04-making-decisions-page-3-4
# Error 3: comparing floats for exact equality.
total = 0.1 + 0.2
if total == 0.3:
    print("equal")
else:
    print(f"not equal: total is {total!r}")
    print("closer than 1e-9?", abs(total - 0.3) < 1e-9)
```

The third one is not a bug in Python. Decimal fractions cannot all be stored exactly in binary, so two calculations that should agree can differ in the last digit. The fix is to ask whether two numbers are *close*, as the last line does, rather than *equal*. You will meet this again whenever a loss or an accuracy is compared to a target.

### Your Turn 9.1

Write the branch table for your `activate` function from Part 7: one test per activation name, one for an unknown name, and one boundary for `relu` at exactly 0. Run it.

```python exec
id: tutorial-04-making-decisions-page-3-5
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
# Your code here
```

## Part 10: Project: A Prediction Decision System

### Project Brief

Bring the parts together in one documented program. Given a student's study hours, attendance and previous average, the program should first validate the inputs (Part 8), then compute the prediction score from Tutorial 3, then place it in a band (Part 4), then produce a recommendation that depends on both the band and the attendance (Part 5), and finally print a short report.

### Requirements

1. Reject impossible inputs with a clear message: study hours outside 0 to 40, attendance outside 0 to 100, an average outside 0 to 100.
2. Use the formula `prediction = study_hours * 3.5 + 30`, capped at 100.
3. Bands as in Part 4.
4. At least one recommendation that depends on two conditions, such as a high band with low attendance.
5. A test table with one case per branch and one per boundary, in the style of Part 9.
6. Comments that say *why*, and names that read as words (LO 11).

Use the variables below as your inputs for now; Tutorial 5 will show how to process many students, and Tutorial 7 how to turn this into a function you can call for each of them.

```python exec
id: tutorial-04-making-decisions-page-3-6
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
student_name = "Ana Lindqvist"
study_hours = 14
attendance = 68.0
previous_average = 71.5

# Your program here
```

## Looking back

Before leaving this page, a sentence on each. What you write stays on this device.

```reflect
- Something you expected before running a cell that turned out differently
- The one idea from this page you could explain to someone else now
- Something you would change or try next, if there were time
- A question this page raised for you that it did not answer. Bring it to the next session; these questions are where the next session starts.
```

---

## Summary and Next Steps

**What you can do now**

- Read and write boolean expressions, and use a truth table to check one you are unsure of
- Choose between actions with `if`, `if`/`else` and `elif`, and order a chain so that no branch is unreachable
- Decide between combining conditions and nesting them, on the basis of what the output needs to explain
- Write a decision tree by hand, and recognise a trained one as the same structure
- Validate settings before a long computation, using chained comparisons and truthiness
- Test every branch and every boundary, and recognise the three common selection errors

### Self-Assessment Checklist

- [ ] I can explain the difference between `=` and `==`
- [ ] I can predict the output of an `elif` chain without running it
- [ ] I can say when nested conditions read better than a combined one
- [ ] I can list the branches of a decision and write a test for each
- [ ] I know why `0.1 + 0.2 == 0.3` is `False` and what to write instead

### What's Coming in Tutorial 5?

Every decision in this tutorial was made once, for one student. Tutorial 5, *Iteration and Loops*, is about making it for a hundred students, or a thousand training steps, without writing the code a hundred times. The truth table in Part 1 was a preview.

### Reflections

(Double-click to edit)

1. A decision in a program you use every day, and what its branches might be:

2. A case where an `elif` chain in the wrong order would give a wrong answer silently:

3. The branch you would most easily forget to test, and why:

---

## Additional Resources

- Python documentation, *More Control Flow Tools*: https://docs.python.org/3/tutorial/controlflow.html
- Python documentation, *Boolean Operations*: https://docs.python.org/3/reference/expressions.html#boolean-operations
- Computerphile, *Floating Point Numbers*: https://www.youtube.com/watch?v=PZRI1IfStY0 (why Part 9's third error happens)
- scikit-learn, *Decision Trees* user guide: https://scikit-learn.org/stable/modules/tree.html (the trained version of Part 6)
