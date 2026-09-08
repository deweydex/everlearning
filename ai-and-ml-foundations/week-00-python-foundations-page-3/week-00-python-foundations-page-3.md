---
title: "week-00-python-foundations-page-3 (3 of 3)"
slug: week-00-python-foundations-page-3
course: ai-and-ml-foundations
course_title: "AI and ML Foundations"
series: 6-projects-from-0-to-markov
series_title: "Projects / From 0 to Markov"
version: 2026.09.06.1
---

Before starting this page, run the cell below. It repeats the imports and definitions from the earlier pages that this page uses.

```python exec
id: week-00-python-foundations-page-3-setup
import random
```

## Week 0 Summary: What You've Learned


 **Variables & Types**
- Storing and manipulating values
- Different data types (int, float, string)
- Type conversion

 **Control Flow**
- `for` loops with `range()`
- `while` loops
- `if/elif/else` conditionals

 **Data Structures**
- Lists and list operations
- Dictionaries for counting and storage
- Indexing and slicing

 **Functions**
- Defining functions with parameters
- Returning values
- Writing docstrings
- Combining functions and loops

 **Problem Solving**
- Breaking problems into steps
- Debugging errors
- Testing code incrementally

### Looking Ahead

Next week, we'll use these tools to:
- Explore probability through simulation
- Understand random walks
- Discover how patterns emerge from randomness

Eventually, these skills will let us build Markov chains that can generate text, predict weather, and model complex random processes.

**Keep this notebook handy** - you'll reference these patterns constantly!

---

## Practice Problems

Before moving on, try these challenges:

### 1. Fibonacci Generator
Write a function that generates the first N Fibonacci numbers.
(Each number is the sum of the previous two: 1, 1, 2, 3, 5, 8, 13...)

```python exec
id: week-00-python-foundations-page-3-1
hint: Look at the variables already defined above this cell, and finish the line the same way the pattern before it was finished.
know: fibonacci(10) prints [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
def fibonacci(n):
    """Generate the first n Fibonacci numbers."""
    # Your code here!
    pass
```

<details class="dl-answer"><summary>answer</summary>

```python
def fibonacci(n):
    """Generate the first n Fibonacci numbers."""
    fib_numbers = []
    a, b = 1, 1
    for _ in range(n):
        fib_numbers.append(a)
        a, b = b, a + b
    return fib_numbers

# Test it
print(fibonacci(10))
```

</details>

### 2. Password Validator
Write a function that checks if a password meets these requirements:
- At least 8 characters long
- Contains at least one number
- Contains at least one uppercase letter

```python exec
id: week-00-python-foundations-page-3-2
hint: Look at the variables already defined above this cell, and finish the line the same way the pattern before it was finished.
know: the three test calls print False, False, True, in that order
def is_valid_password(password):
    """Check if password meets security requirements."""
    # Your code here!
    pass
```

<details class="dl-answer"><summary>answer</summary>

```python
def is_valid_password(password):
    """Check if password meets security requirements."""
    if len(password) < 8:
        return False

    has_number = False
    has_upper = False
    for char in password:
        if char.isdigit():
            has_number = True
        if char.isupper():
            has_upper = True

    return has_number and has_upper

# Test it
print(is_valid_password("short1A"))     # False - too short
print(is_valid_password("longenough")) # False - no number or uppercase
print(is_valid_password("LongEnough1")) # True
```

</details>

### 3. Shopping Cart
Create a program that:
- Starts with a list of items and prices
- Calculates the subtotal
- Applies a 10% discount if total > €50
- Adds 20% tax
- Returns the final price

```python exec
id: week-00-python-foundations-page-3-3
hint: Look at the variables already defined above this cell, and finish the line the same way the pattern before it was finished.
know: with the cart given, the total is €5.64 (no discount, since the subtotal is under 50, then 20 percent tax)
def calculate_total(items):
    """
    Calculate total with discount and tax.
    items: list of tuples like ("apple", 1.50)
    """
    # Your code here!
    pass

# Test with:
# cart = [("apple", 1.50), ("bread", 2.00), ("milk", 1.20)]
# print(f"Total: €{calculate_total(cart):.2f}")
```

<details class="dl-answer"><summary>answer</summary>

```python
def calculate_total(items):
    """
    Calculate total with discount and tax.
    items: list of tuples like ("apple", 1.50)
    """
    subtotal = 0
    for name, price in items:
        subtotal += price

    if subtotal > 50:
        subtotal = subtotal * 0.9  # 10% discount

    total = subtotal * 1.20  # 20% tax
    return total

# Test with:
cart = [("apple", 1.50), ("bread", 2.00), ("milk", 1.20)]
print(f"Total: €{calculate_total(cart):.2f}")
```

</details>

---

## Ready for Week 1?

Once you're comfortable with these concepts, you're ready to dive into **probability through simulation**!

We'll start exploring random walks, probability distributions, and the mathematics that governs randomness.

See you in Week 1! 

## Looking back

Before leaving this page, a sentence on each. What you write stays on this device.

```reflect
- Something you expected before running a cell that turned out differently
- The one idea from this page you could explain to someone else now
- Something you would change or try next, if there were time
- A question this page raised for you that it did not answer. Bring it to the next session; these questions are where the next session starts.
```
