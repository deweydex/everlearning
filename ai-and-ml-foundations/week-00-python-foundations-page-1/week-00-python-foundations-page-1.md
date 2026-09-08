---
title: "Week 0: Python Foundations - Your Programming Toolkit (1 of 3)"
slug: week-00-python-foundations-page-1
course: ai-and-ml-foundations
course_title: "AI and ML Foundations"
series: 6-projects-from-0-to-markov
series_title: "Projects / From 0 to Markov"
version: 2026.09.06.1
---

# Week 0: Python Foundations - Your Programming Toolkit

**Welcome to the adventure!**

Over the next few weeks, you're going to build something genuinely cool: programs that can predict weather, generate text that sounds almost human, and model random processes. But before we get there, we need to build your toolkit.


## What We're Building Toward

By Week 10, you'll have created programs that:
- Generate surprisingly realistic text
- Predict tomorrow's weather based on patterns
- Simulate random processes
- Understand probability through code

But first: the basics.

---

## Part 1: Your First Programs

Let's start with something simple. Run this cell and see what happens:

```python exec
id: week-00-python-foundations-page-1-1
print("Hello, World!")
print("My name is [YOUR NAME HERE]")
print("I'm about to learn Python!")
```

**Question for you:** What happens if you remove the quotation marks? Try it! Break things! That's how you learn.

### Python as a Calculator

Python can do math. Try these:

```python exec
id: week-00-python-foundations-page-1-2
print(5 + 3)
print(10 * 7)
print(2 ** 10)  # What does ** do? Experiment!
print(100 / 3)
```

**Your turn:** In the cell below, calculate:
1. How many hours are in a year?
2. What's 2 to the power of 20?
3. What's 17 divided by 5? Now try 17 // 5 and 17 % 5 - what do these do?

```python exec
id: week-00-python-foundations-page-1-3
hint: Try a big number with **, and try // and % on two numbers you already know the answer for by hand, to see what each one gives back.
know: there is no single right answer here — try a few operators and see what each one does; the point is to notice a pattern, not match a target
# Your experiments here!
```

<details class="dl-answer"><summary>answer</summary>

```python
# Your experiments here!
hours_in_a_year = 24 * 365
print(f"Hours in a year: {hours_in_a_year}")

two_to_the_20 = 2 ** 20
print(f"2 to the power of 20: {two_to_the_20}")

print(f"17 / 5 = {17 / 5}")     # true division: gives a decimal
print(f"17 // 5 = {17 // 5}")   # floor division: rounds down to a whole number
print(f"17 % 5 = {17 % 5}")     # modulo: the remainder left over
```

</details>

---

## Part 2: Variables - Giving Names to Things

Variables are like labeled boxes that hold values. You'll use them *constantly*.

```python exec
id: week-00-python-foundations-page-1-4
my_age = 20
years_until_30 = 30 - my_age
print(f"Years until I'm 30: {years_until_30}")
```

Notice the `f` before the string? That makes it a "formatted string" where you can insert variables directly.

### Variables Can Change

```python exec
id: week-00-python-foundations-page-1-5
score = 0
print(f"Starting score: {score}")

score = score + 10
print(f"After bonus: {score}")

score = score + 5
print(f"After another bonus: {score}")

# Shortcut: score += 5 does the same as score = score + 5
```

### Try this: The Coffee Economics Calculator

Create variables to calculate your yearly coffee spending:

```python exec
id: week-00-python-foundations-page-1-6
hint: Look at the variables already defined above this cell, and finish the line the same way the pattern before it was finished.
know: the cell prints something starting "That's"
coffee_per_day = 3.50
days_in_week = 7

# You calculate:
weekly_cost = # Your code
yearly_cost = # Your code

print(f"Weekly coffee cost: €{weekly_cost:.2f}")
print(f"Yearly coffee cost: €{yearly_cost:.2f}")
print(f"That's {yearly_cost / 1000:.1f} thousand euros!")
```

<details class="dl-answer"><summary>answer</summary>

```python
coffee_per_day = 3.50
days_in_week = 7

# You calculate:
weekly_cost = coffee_per_day * days_in_week
yearly_cost = weekly_cost * 52

print(f"Weekly coffee cost: €{weekly_cost:.2f}")
print(f"Yearly coffee cost: €{yearly_cost:.2f}")
print(f"That's {yearly_cost / 1000:.1f} thousand euros!")
```

</details>

**Think about it:** If you invested that money instead at 5% annual return, how much would you have after 10 years?

---

## Part 3: Loops - When Repetition Meets Elegance

### The Problem with Repetition

Imagine you want to print "I will learn Python!" 100 times. You *could* do this:

```python exec
id: week-00-python-foundations-page-1-7
print("I will learn Python!")
print("I will learn Python!")
print("I will learn Python!")
# ... 97 more times? No thanks!
```

### Enter: The For Loop

Loops let you repeat actions without repeating code:

```python exec
id: week-00-python-foundations-page-1-8
for i in range(5):
    print("I will learn Python!")

print("Done! That was easy.")
```

**What just happened?**

`range(5)` creates a sequence: 0, 1, 2, 3, 4

The loop runs once for each number, storing it in `i`

```python exec
id: week-00-python-foundations-page-1-9
# Let's see what range actually creates
print("range(5):", list(range(5)))
print("range(2, 7):", list(range(2, 7)))
print("range(0, 10, 2):", list(range(0, 10, 2)))  # Every 2nd number
```

### Using the Loop Variable

```python exec
id: week-00-python-foundations-page-1-10
print("Counting:")
for i in range(1, 6):
    print(f"Count {i}")

print("\nCountdown:")
for i in range(10, 0, -1):
    print(i)
print("Blast off! 🚀")
```

### Visual Pattern Challenge

Can you figure out how these work?

```python exec
id: week-00-python-foundations-page-1-11
# Pattern 1: Growing line
for i in range(1, 6):
    print("*" * i)
```

```python exec
id: week-00-python-foundations-page-1-12
# Pattern 2: Pyramid
for i in range(1, 6):
    spaces = " " * (5 - i)
    stars = "*" * (2 * i - 1)
    print(spaces + stars)
```

**Your turn:** Can you make:
1. A diamond shape?
2. A Christmas tree?
3. Your initials in stars?

Use the cell below to experiment:

```python exec
id: week-00-python-foundations-page-1-13
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
# Your patterns here!
```

---

## Part 4: Lists - Collections of Things

What if you want to store multiple values together? Enter: lists.

```python exec
id: week-00-python-foundations-page-1-14
fruits = ["apple", "banana", "cherry", "date"]

print("First fruit:", fruits[0])  # Lists start at 0!
print("Last fruit:", fruits[-1])  # Negative indices count from the end
print("Second and third:", fruits[1:3])  # Slicing
```

### Looping Through Lists

```python exec
id: week-00-python-foundations-page-1-15
print("All fruits:")
for fruit in fruits:
    print(f"I like {fruit}s!")
```

### Building Lists with Loops

```python exec
id: week-00-python-foundations-page-1-16
# Method 1: Start empty, then append
squares = []
for i in range(1, 11):
    squares.append(i ** 2)

print("Square numbers:", squares)
```

```python exec
id: week-00-python-foundations-page-1-17
# Method 2: List comprehension (Pythonic shortcut!)
cubes = [i ** 3 for i in range(1, 11)]
print("Cube numbers:", cubes)
```

### Your turn: Grade Calculator

Let's calculate statistics from test scores:

```python exec
id: week-00-python-foundations-page-1-18
scores = [78, 85, 92, 88, 76, 95, 89]

# Calculate average
total = 0
for score in scores:
    total = total + score

average = total / len(scores)
print(f"Average score: {average:.1f}")

# Find highest
highest = scores[0]
for score in scores:
    if score > highest:
        highest = score

print(f"Highest score: {highest}")
```

**Your turn:** In the cell below:
1. Find the lowest score
2. Count how many scores are above 85
3. Calculate the range (highest - lowest)

```python exec
id: week-00-python-foundations-page-1-19
hint: Look at the variables already defined above this cell, and finish the line the same way the pattern before it was finished.
know: the cell prints something starting "Range (highest - lowest):"
scores = [78, 85, 92, 88, 76, 95, 89]

# Your code here!
```

<details class="dl-answer"><summary>answer</summary>

```python
scores = [78, 85, 92, 88, 76, 95, 89]

# Your code here!
lowest = scores[0]
for score in scores:
    if score < lowest:
        lowest = score
print(f"Lowest score: {lowest}")

above_85 = 0
for score in scores:
    if score > 85:
        above_85 += 1
print(f"Scores above 85: {above_85}")

highest = scores[0]
for score in scores:
    if score > highest:
        highest = score
score_range = highest - lowest
print(f"Range (highest - lowest): {score_range}")
```

</details>

---

## Looking back

Before leaving this page, a sentence on each. What you write stays on this device.

```reflect
- Something you expected before running a cell that turned out differently
- The one idea from this page you could explain to someone else now
- Something you would change or try next, if there were time
- A question this page raised for you that it did not answer. Bring it to the next session; these questions are where the next session starts.
```
