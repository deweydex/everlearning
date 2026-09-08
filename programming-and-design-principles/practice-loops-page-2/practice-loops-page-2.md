---
title: "practice-loops-page-2 (2 of 2)"
slug: practice-loops-page-2
course: programming-and-design-principles
course_title: "Programming and Design Principles"
series: practice
series_title: "Practice"
version: 2026.09.06.1
---

Before starting this page, run the cell below. It repeats the imports and definitions from the earlier pages that this page uses.

```python exec
id: practice-loops-page-2-setup
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

---
## Part 3: Practical Applications and Patterns

### Pattern 1: Searching

Find an element in a collection that meets certain criteria.

```python exec
id: practice-loops-page-2-1
# Linear search: find a specific item
numbers = [4, 7, 2, 9, 1, 5, 8]
target = 9
found = False
position = -1

for i, num in enumerate(numbers):
    if num == target:
        found = True
        position = i
        break  # Stop once we find it

if found:
    print(f"Found {target} at position {position}")
else:
    print(f"{target} not found")
```

### Try this 8: Search Problems

Given the list of students and scores:
1. Find the first student who scored above 85
2. Find all students who scored exactly 90
3. Check if any student scored below 50
4. Find the position of the highest score

```python exec
id: practice-loops-page-2-2
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
students = ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve', 'Frank']
scores = [78, 92, 85, 90, 88, 75]

# Your code here:
```

### Pattern 2: Validation

Check if all elements meet a condition.

```python exec
id: practice-loops-page-2-3
# Check if all numbers are positive
numbers = [1, 5, 8, 12, 3]
all_positive = True

for num in numbers:
    if num <= 0:
        all_positive = False
        break

if all_positive:
    print("All numbers are positive!")
else:
    print("Found a non-positive number.")

# Check if password meets requirements
password = "MyP@ssw0rd"
has_upper = False
has_lower = False
has_digit = False
has_special = False

for char in password:
    if char.isupper():
        has_upper = True
    elif char.islower():
        has_lower = True
    elif char.isdigit():
        has_digit = True
    elif char in "!@#$%^&*":
        has_special = True

valid = has_upper and has_lower and has_digit and has_special and len(password) >= 8
print(f"\nPassword valid: {valid}")
```

### Try this 9: Validation Tasks

1. Check if a list contains only even numbers
2. Check if a string is a palindrome (reads same forwards and backwards)
3. Validate an email: must contain exactly one '@' and at least one '.'
4. Check if a list is sorted in ascending order

```python exec
id: practice-loops-page-2-4
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
# Your code here:
```

### Pattern 3: Transformation

Create a new collection by modifying each element.

```python exec
id: practice-loops-page-2-5
# Convert temperatures from Celsius to Fahrenheit
celsius = [0, 10, 20, 30, 40]
fahrenheit = []

for temp in celsius:
    f = temp * 9/5 + 32
    fahrenheit.append(f)

print("Celsius:", celsius)
print("Fahrenheit:", fahrenheit)

# Clean and standardize text data
raw_names = ["  alice  ", "BOB", "  Charlie"]
clean_names = []

for name in raw_names:
    clean = name.strip().title()  # Remove spaces and capitalize properly
    clean_names.append(clean)

print("\nRaw names:", raw_names)
print("Clean names:", clean_names)
```

### Try this 10: Data Transformation

1. Convert a list of prices in euros to dollars (1 EUR = 1.10 USD)
2. Take a list of words and create a list of their lengths
3. Given a list of numbers, create a new list with "even" or "odd" labels
4. Normalize grades: convert scores to percentages if they're out of 50

```python exec
id: practice-loops-page-2-6
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
prices_eur = [10.99, 25.50, 5.00, 42.00]
words = ['cat', 'elephant', 'dog', 'butterfly']
numbers = [1, 2, 3, 4, 5, 6]
scores = [42, 38, 45, 30, 47]  # Out of 50

# Your code here:
```

### Pattern 4: Filtering

Create a new collection with only elements that meet certain criteria.

```python exec
id: practice-loops-page-2-7
# Filter out negative numbers
numbers = [-3, 7, -1, 5, -8, 2, 0, 9]
positive = []

for num in numbers:
    if num > 0:
        positive.append(num)

print("Original:", numbers)
print("Positive only:", positive)

# Filter long words
words = ['cat', 'elephant', 'dog', 'hippopotamus', 'ant']
long_words = []

for word in words:
    if len(word) > 5:
        long_words.append(word)

print("\nLong words:", long_words)
```

### Try this 11: Filtering Data

1. From a list of ages, extract only adults (18 and over)
2. From a list of emails, extract only gmail addresses
3. From a list of scores, extract only passing grades (60 or above)
4. From a list of words, extract only palindromes

```python exec
id: practice-loops-page-2-8
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
ages = [12, 18, 25, 16, 30, 14, 21]
emails = ['alice@gmail.com', 'bob@yahoo.com', 'charlie@gmail.com', 'diana@outlook.com']
scores = [85, 55, 72, 48, 91, 63, 44]
words = ['level', 'hello', 'radar', 'python', 'noon', 'world']

# Your code here:
```

---
## Part 4: Advanced Challenges

These problems combine multiple concepts!

### Try this 12: Prime Numbers

Write code to:
1. Check if a given number is prime
2. Find all prime numbers up to 50
3. Find the first 10 prime numbers

```python exec
id: practice-loops-page-2-9
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
# Hint: A prime number is only divisible by 1 and itself
# Your code here:
```

### Try this 13: Fibonacci Sequence

The Fibonacci sequence starts with 0, 1, and each next number is the sum of the previous two:
0, 1, 1, 2, 3, 5, 8, 13, 21, ...

1. Generate the first 15 Fibonacci numbers
2. Find the first Fibonacci number greater than 1000
3. Calculate the sum of all even Fibonacci numbers below 100

```python exec
id: practice-loops-page-2-10
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
# Your code here:
```

### Try this 14: Digital Root

The digital root is found by repeatedly summing digits until you get a single digit.

Example: 38 → 3+8=11 → 1+1=2 (digital root is 2)

Write code to find the digital root of any number.

```python exec
id: practice-loops-page-2-11
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
number = 9875

# Your code here:
```

### Try this 15: Caesar Cipher

A Caesar cipher shifts each letter by a fixed number of positions in the alphabet.

Example: "HELLO" with shift 3 becomes "KHOOR"

Write code to:
1. Encrypt a message with a given shift
2. Decrypt a message (hint: shift in the opposite direction)

For simplicity, only handle uppercase letters.

```python exec
id: practice-loops-page-2-12
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
# Hint: ord('A') gives 65, chr(65) gives 'A'
message = "HELLO WORLD"
shift = 3

# Your code here:
```

### Try this 16: Simple Game - Guess the Number

Create a number guessing game:
1. The "secret" number is hardcoded (e.g., 42)
2. User has 5 attempts to guess
3. After each guess, tell them if they're too high or too low
4. Celebrate if they win, reveal the number if they lose

Note: Use a while loop with a counter!

```python exec
id: practice-loops-page-2-13
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
# For Jupyter, simulate guesses with a list
secret = 42
guesses = [30, 50, 40, 43, 42]  # Simulated user guesses

# Your code here:
```

### Try this 17: Processing 2D Data

Given a 2D list representing a grid:
1. Calculate the sum of each row
2. Calculate the sum of each column
3. Find the maximum value in the entire grid
4. Find the position (row, col) of that maximum
5. Count how many values are above the average

```python exec
id: practice-loops-page-2-14
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
grid = [
    [12, 15, 18, 10],
    [20, 25, 22, 19],
    [14, 16, 21, 17],
    [23, 11, 13, 24]
]

# Your code here:
```

### Try this 18: Run-Length Encoding

Implement run-length encoding: compress consecutive repeated characters.

Example: "AAABBCCCCAA" → "A3B2C4A2"

Write code to encode a string.

```python exec
id: practice-loops-page-2-15
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
text = "AAABBCCCCAA"

# Your code here:
```

---
## Summary

**What you've mastered:**
- For loops for definite iteration
- While loops for conditional repetition
- Break and continue for loop control
- Common patterns: accumulation, searching, filtering, transformation
- Nested loops for 2D data
- Choosing the right loop for the job

**Key Principles:**
1. **For loops**: When you know how many times (or have a sequence)
2. **While loops**: When you're waiting for a condition to change
3. **Always ensure loops will terminate** (avoid infinite loops)
4. **Break early**: Don't do unnecessary work
5. **Build complexity gradually**: Start simple, add features

**Practice makes perfect!** The more loops you write, the more natural they become. Try creating your own challenges and variations!

## Looking back

Before leaving this page, a sentence on each. What you write stays on this device.

```reflect
- Something you expected before running a cell that turned out differently
- The one idea from this page you could explain to someone else now
- Something you would change or try next, if there were time
- A question this page raised for you that it did not answer. Bring it to the next session; these questions are where the next session starts.
```
