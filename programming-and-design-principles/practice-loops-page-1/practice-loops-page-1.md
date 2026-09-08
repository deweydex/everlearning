---
title: "Loops: For and While (1 of 2)"
slug: practice-loops-page-1
course: programming-and-design-principles
course_title: "Programming and Design Principles"
series: practice
series_title: "Practice"
version: 2026.09.06.1
---

# Loops: For and While


**How to use this notebook:**
Loops are all about repetition - doing something over and over. Work through each section, try the challenges, and experiment! The best way to learn loops is by writing lots of them.

---
## Part 1: For Loops - Definite Iteration

A **for loop** is used when you know **how many times** you want to repeat something, or when you want to **iterate through a sequence** (like a list, string, or range).

**Syntax:**
```python
for variable in sequence:
    # do something with variable
```

### Looping Through a Range

The `range()` function is your friend for counting loops!

```python exec
id: practice-loops-page-1-1
# Basic counting from 0 to 4
print("Counting to 5:")
for i in range(5):
    print(i)

# Counting from start to stop
print("\nCounting from 1 to 5:")
for i in range(1, 6):  # Remember: stop is exclusive!
    print(i)

# Counting with a step
print("\nEven numbers:")
for i in range(0, 11, 2):  # start=0, stop=11, step=2
    print(i)

# Counting backwards
print("\nCountdown:")
for i in range(5, 0, -1):  # start=5, stop=0, step=-1
    print(i)
print("Blast off!")
```

### Try this 1: Range Practice

Use for loops to:
1. Print numbers from 10 to 20
2. Print odd numbers from 1 to 20
3. Print multiples of 5 from 0 to 50
4. Print numbers from 20 down to 10

```python exec
id: practice-loops-page-1-2
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
# Your code here:
```

### Looping Through Lists

For loops excel at processing each item in a collection.

```python exec
id: practice-loops-page-1-3
# Loop through a list of names
names = ['Alice', 'Bob', 'Charlie', 'Diana']

print("Greetings:")
for name in names:
    print(f"Hello, {name}!")

# Loop through numbers
prices = [19.99, 5.50, 12.00, 8.75]

print("\nPrices with tax (10%):")
for price in prices:
    price_with_tax = price * 1.10
    print(f"€{price:.2f} → €{price_with_tax:.2f}")
```

### Looping with Indices: enumerate()

Sometimes you need both the **item** and its **position**. Use `enumerate()`!

```python exec
id: practice-loops-page-1-4
fruits = ['apple', 'banana', 'cherry', 'date']

# Without enumerate (the hard way)
print("Method 1: Manual indexing")
for i in range(len(fruits)):
    print(f"{i}: {fruits[i]}")

# With enumerate (the elegant way)
print("\nMethod 2: Using enumerate")
for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")

# Start counting from 1 instead of 0
print("\nNumbered list (starting from 1):")
for i, fruit in enumerate(fruits, start=1):
    print(f"{i}. {fruit}")
```

### Try this 2: List Processing

Given the list of temperatures:
1. Print each temperature with "°C" suffix
2. Count how many temperatures are above 20°C
3. Create a new list with temperatures converted to Fahrenheit (F = C × 9/5 + 32)
4. Print each temperature with its index position

```python exec
id: practice-loops-page-1-5
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
temperatures = [18, 22, 19, 25, 17, 23, 20]

# Your code here:
```

### Looping Through Strings

Strings are sequences too! You can loop through each character.

```python exec
id: practice-loops-page-1-6
word = "Python"

print("Each character:")
for char in word:
    print(char)

# Counting vowels
text = "Hello World"
vowels = "aeiouAEIOU"
count = 0

for char in text:
    if char in vowels:
        count += 1

print(f"\nThe text '{text}' has {count} vowels.")
```

### Try this 3: String Analysis

Given a sentence:
1. Count the number of spaces
2. Count the number of uppercase letters
3. Create a string with only the vowels from the sentence
4. Print each word on a separate line (hint: use `.split()`)

```python exec
id: practice-loops-page-1-7
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
sentence = "The Quick Brown Fox Jumps Over The Lazy Dog"

# Your code here:
```

### Accumulation Pattern

A very common pattern: **start with an initial value and build it up** in a loop.

```python exec
id: practice-loops-page-1-8
# Sum all numbers from 1 to 10
total = 0  # Start with 0
for i in range(1, 11):
    total += i  # Add each number
print(f"Sum of 1 to 10: {total}")

# Product (factorial)
product = 1  # Start with 1 (multiplying by 0 would give 0!)
for i in range(1, 6):
    product *= i
print(f"5! = {product}")

# Building a string
result = ""
for i in range(5):
    result += "*"
print(f"Stars: {result}")

# Building a list
squares = []
for i in range(1, 6):
    squares.append(i ** 2)
print(f"Squares: {squares}")
```

### Try this 4: Accumulation Practice

1. Calculate the product of all numbers from 1 to 8
2. Build a string that counts down: "5-4-3-2-1-Blast off!"
3. Create a list of the first 10 even numbers
4. Calculate the sum of squares from 1 to 5 (1² + 2² + 3² + 4² + 5²)

```python exec
id: practice-loops-page-1-9
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
# Your code here:
```

### Nested For Loops

Loops inside loops! Useful for processing 2D data, creating patterns, or combinations.

```python exec
id: practice-loops-page-1-10
# Printing a rectangle of stars
print("Rectangle:")
for row in range(3):  # 3 rows
    for col in range(5):  # 5 columns
        print("*", end="")  # end="" prevents newline
    print()  # Newline after each row

# Multiplication table
print("\nMultiplication table (3x3):")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} × {j} = {i*j}")
    print()  # Blank line between each i value
```

### Try this 5: Nested Loop Patterns

1. Print a triangle of stars:
 ```
 *
 **
 ***
 ****
 *****
 ```

2. Print a numbered grid:
 ```
 1 2 3 4
 1 2 3 4
 1 2 3 4
 ```

3. Print coordinates:
 ```
 (0,0) (0,1) (0,2)
 (1,0) (1,1) (1,2)
 (2,0) (2,1) (2,2)
 ```

```python exec
id: practice-loops-page-1-11
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
# Your code here:
```

---
## Part 2: While Loops - Indefinite Iteration

A **while loop** runs as long as a condition is True. Use it when you **don't know in advance** how many iterations you need.

**Syntax:**
```python
while condition:
 # do something
 # usually modify something to eventually make condition False
```

** Warning:** Always make sure your while loop will eventually stop! Otherwise, it runs forever (infinite loop).

```python exec
id: practice-loops-page-1-12
# Basic while loop: countdown
count = 5
while count > 0:
    print(count)
    count -= 1  # IMPORTANT: change the condition variable!
print("Done!")

# Building up to a target
total = 0
while total < 50:
    total += 7
    print(f"Current total: {total}")
print(f"Final total: {total}")
```

### While vs For: Which to Use?

**Use FOR when:**
- You know how many iterations you need
- You're iterating through a collection
- You're counting a specific range

**Use WHILE when:**
- You're waiting for a condition to become True/False
- You don't know how many iterations you'll need
- You're implementing game loops, user input validation, or searching

```python exec
id: practice-loops-page-1-13
# Same result, different approaches:

# FOR: We know we want exactly 5 iterations
print("Using for:")
for i in range(5):
    print(i)

# WHILE: We track a counter and stop when we reach a condition
print("\nUsing while:")
i = 0
while i < 5:
    print(i)
    i += 1
```

### Try this 6: While Loop Basics

1. Print numbers from 1 to 10 using a while loop
2. Start with 100 and keep dividing by 2 until the value is less than 1 (print each step)
3. Start with 1 and keep doubling until the value exceeds 1000 (print each step)

```python exec
id: practice-loops-page-1-14
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
# Your code here:
```

### While Loops with User Input

While loops are perfect for input validation - keep asking until you get what you want!

**Note:** In Jupyter notebooks, `input()` can be tricky. These examples show the pattern.

```python exec
id: practice-loops-page-1-15
# Simulating input validation (pseudo-code pattern)
# In a real program, you would use input()

# Pattern for input validation:
def validate_age_example():
    """
    Example pattern for input validation
    
    # Actual code would be:
    age = -1
    while age < 0 or age > 120:
        age = int(input("Enter your age: "))
        if age < 0 or age > 120:
            print("Invalid age! Try again.")
    print(f"Thank you! Age {age} recorded.")
    """
    pass

# Pattern for sentinel-based loop (stop when user types 'quit')
def sentinel_example():
    """
    # Actual code would be:
    response = ""
    total = 0
    while response.lower() != "quit":
        response = input("Enter a number (or 'quit' to stop): ")
        if response.lower() != "quit":
            total += int(response)
            print(f"Running total: {total}")
    print(f"Final total: {total}")
    """
    pass

print("Input validation patterns shown above as examples.")
print("These work well in regular Python scripts!")
```

### While with break and continue

- **break**: Exit the loop immediately
- **continue**: Skip the rest of this iteration and start the next one

```python exec
id: practice-loops-page-1-16
# Using break: stop early
print("Finding first number divisible by 7 and 13:")
n = 1
while True:  # Infinite loop!
    if n % 7 == 0 and n % 13 == 0:
        print(f"Found it: {n}")
        break  # Exit the loop
    n += 1

# Using continue: skip certain iterations
print("\nNumbers from 1 to 10, skipping multiples of 3:")
i = 0
while i < 10:
    i += 1
    if i % 3 == 0:
        continue  # Skip the rest and go to next iteration
    print(i)
```

### Try this 7: Break and Continue

1. Find the first square number (1, 4, 9, 16, ...) that is greater than 200
2. Print all numbers from 1 to 30, but skip numbers divisible by both 2 and 3
3. Find the sum of numbers 1, 2, 3, ... but stop when the sum exceeds 100

```python exec
id: practice-loops-page-1-17
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
# Your code here:
```

## What we set out to do

These were the aims of this notebook. Now that you have worked through it, they are a check on what happened rather than a promise about it.

- Understand when and how to use `for` loops
- Understand when and how to use `while` loops
- Master common loop patterns
- Recognize which loop type to use for different problems
- Practice with nested loops

## Looking back

Before leaving this page, a sentence on each. What you write stays on this device.

```reflect
- Something you expected before running a cell that turned out differently
- The one idea from this page you could explain to someone else now
- Something you would change or try next, if there were time
- A question this page raised for you that it did not answer. Bring it to the next session; these questions are where the next session starts.
```
