---
title: "Lists and Matrices: From 1D to 2D Data Structures (1 of 2)"
slug: 03-lists-and-matrices-practice-page-1
course: ai-and-ml-foundations
course_title: "AI and ML Foundations"
series: 0-python-and-numpy-refresher
series_title: "Python and NumPy Refresher"
version: 2026.09.06.1
---

# Lists and Matrices: From 1D to 2D Data Structures


**How to use this notebook:**
Work through each section in order. Try the challenges before looking at solutions. The goal is to build intuition through experimentation!

---
## Part 1: Lists - The Basics

A **list** is Python's way of storing multiple values in a single variable. Think of it as a numbered container where each item has a position (called an **index**).

```python exec
id: 03-lists-and-matrices-practice-page-1-1
# Creating lists - several ways to do it
temperatures = [20, 22, 19, 25, 23]  # A list of temperatures
names = ['Alice', 'Bob', 'Charlie']   # A list of strings
mixed = [1, 'hello', 3.14, True]      # Lists can mix types!
empty = []                             # An empty list

print("Temperatures:", temperatures)
print("Names:", names)
print("Mixed types:", mixed)
```

### Indexing: Accessing Individual Elements

**Key concept:** Python uses **zero-based indexing** - the first element is at position 0, not 1!

```
List:    ['A',  'B',  'C',  'D',  'E']
Index:     0     1     2     3     4
```

You can also count backwards from the end using negative indices:
```
List:    ['A',  'B',  'C',  'D',  'E']
Index:    -5    -4    -3    -2    -1
```

```python exec
id: 03-lists-and-matrices-practice-page-1-2
# Indexing examples
fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry']

print("First fruit:", fruits[0])      # 'apple'
print("Third fruit:", fruits[2])      # 'cherry'
print("Last fruit:", fruits[-1])      # 'elderberry'
print("Second to last:", fruits[-2])  # 'date'
```

### Try this 1: Basic Indexing

Given the list below, use indexing to:
1. Print the first number
2. Print the last number
3. Print the middle number (index 2)
4. Print the second number using negative indexing

```python exec
id: 03-lists-and-matrices-practice-page-1-3
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
numbers = [10, 20, 30, 40, 50]

# Your code here:
```

### Slicing: Getting Multiple Elements

**Slicing** lets you extract a portion of a list. The syntax is: `list[start:stop:step]`

- `start`: Where to begin (inclusive)
- `stop`: Where to end (exclusive - doesn't include this index)
- `step`: How many positions to jump (default is 1)

**Important:** The `stop` index is NOT included in the result!

```python exec
id: 03-lists-and-matrices-practice-page-1-4
# Slicing examples
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

print("First three:", letters[0:3])        # ['A', 'B', 'C']
print("Middle part:", letters[2:6])        # ['C', 'D', 'E', 'F']
print("From index 3 to end:", letters[3:]) # ['D', 'E', 'F', 'G', 'H']
print("Up to index 5:", letters[:5])       # ['A', 'B', 'C', 'D', 'E']
print("Every second item:", letters[::2])  # ['A', 'C', 'E', 'G']
print("Reversed:", letters[::-1])          # ['H', 'G', 'F', 'E', 'D', 'C', 'B', 'A']
```

### Try this 2: Slicing Practice

Given the list of days, use slicing to:
1. Get the weekdays (first 5 days)
2. Get the weekend (last 2 days)
3. Get every other day starting from Monday
4. Get the days in reverse order

```python exec
id: 03-lists-and-matrices-practice-page-1-5
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

# Your code here:
```

### Try this 3: Understanding Slice Boundaries

Predict what each slice will produce, then run the code to check:

```python exec
id: 03-lists-and-matrices-practice-page-1-6
data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Before running, write down what you think each will print:
print(data[2:7])
print(data[-3:])
print(data[1:8:2])
print(data[5:2:-1])
print(data[::3])
```

---
## Part 2: List Comprehensions

**List comprehensions** are a concise way to create lists. Instead of writing loops, you can build lists in a single line!

**Basic syntax:** `[expression for item in iterable]`

**With condition:** `[expression for item in iterable if condition]`

```python exec
id: 03-lists-and-matrices-practice-page-1-7
# Traditional way: using a loop
squares_loop = []
for i in range(5):
    squares_loop.append(i ** 2)
print("Squares (loop):", squares_loop)

# List comprehension way: one line!
squares_comp = [i ** 2 for i in range(5)]
print("Squares (comprehension):", squares_comp)

# Both produce: [0, 1, 4, 9, 16]
```

```python exec
id: 03-lists-and-matrices-practice-page-1-8
# More examples

# Double each number
numbers = [1, 2, 3, 4, 5]
doubled = [n * 2 for n in numbers]
print("Doubled:", doubled)  # [2, 4, 6, 8, 10]

# Get lengths of strings
words = ['cat', 'elephant', 'dog']
lengths = [len(word) for word in words]
print("Lengths:", lengths)  # [3, 8, 3]

# Filter with a condition: only even numbers
evens = [n for n in range(10) if n % 2 == 0]
print("Even numbers:", evens)  # [0, 2, 4, 6, 8]
```

### Try this 4: Simple List Comprehensions

Use list comprehensions to create:
1. A list of the first 10 cubes (0³, 1³, 2³, ...)
2. A list of the first 6 powers of 2 (2⁰, 2¹, 2², ...)
3. A list containing "Hello!" repeated 5 times

```python exec
id: 03-lists-and-matrices-practice-page-1-9
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
# Your code here:
```

### Try this 5: Filtering with Comprehensions

Given a list of numbers, use list comprehensions to:
1. Extract only the positive numbers
2. Extract numbers divisible by 3
3. Square all the odd numbers

```python exec
id: 03-lists-and-matrices-practice-page-1-10
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
numbers = [-5, 3, -2, 8, 0, 9, -1, 12, 7]

# Your code here:
```

### Try this 6: String Manipulation

Given a list of names:
1. Create a list of names converted to uppercase
2. Create a list of first letters only
3. Create a list of names that are longer than 4 characters

```python exec
id: 03-lists-and-matrices-practice-page-1-11
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
names = ['alice', 'bob', 'charlie', 'dan', 'elizabeth']

# Your code here:
```

---
## Part 3: Two-Dimensional Lists (Matrices)

A **2D list** is a list of lists - think of it as a table with rows and columns. This is how we represent **matrices** in Python.

```
Matrix visualization:
[
  [1, 2, 3],    ← Row 0
  [4, 5, 6],    ← Row 1
  [7, 8, 9]     ← Row 2
]
```

To access an element: `matrix[row][column]`

```python exec
id: 03-lists-and-matrices-practice-page-1-12
# Creating a 2D list (3x3 matrix)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Full matrix:")
for row in matrix:
    print(row)

print("\nAccessing elements:")
print("Top-left corner:", matrix[0][0])      # 1
print("Center element:", matrix[1][1])       # 5
print("Bottom-right:", matrix[2][2])         # 9
print("First row:", matrix[0])               # [1, 2, 3]
print("Second column:", [matrix[i][1] for i in range(3)])  # [2, 5, 8]
```

### Creating 2D Lists with Comprehensions

We can use **nested list comprehensions** to create matrices efficiently.

```python exec
id: 03-lists-and-matrices-practice-page-1-13
# Create a 4x4 matrix filled with zeros
zeros = [[0 for j in range(4)] for i in range(4)]
print("4x4 zeros:")
for row in zeros:
    print(row)

# Create a 3x5 matrix with row number
row_numbers = [[i for j in range(5)] for i in range(3)]
print("\nRow numbers:")
for row in row_numbers:
    print(row)

# Create a 3x3 identity matrix (1s on diagonal, 0s elsewhere)
identity = [[1 if i == j else 0 for j in range(3)] for i in range(3)]
print("\n3x3 identity matrix:")
for row in identity:
    print(row)
```

### Try this 7: 2D Indexing

Given the grid below:
1. Print the element at row 1, column 2
2. Print the entire third row
3. Print the second column (as a list)
4. Print all four corner values

```python exec
id: 03-lists-and-matrices-practice-page-1-14
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
grid = [
    [10, 20, 30, 40],
    [50, 60, 70, 80],
    [90, 100, 110, 120]
]

# Your code here:
```

### Try this 8: Building Matrices

Use list comprehensions to create:
1. A 5x5 matrix filled with the number 7
2. A 3x4 matrix where each element is the product of its row and column indices
3. A 4x4 matrix with True on the main diagonal and False elsewhere

```python exec
id: 03-lists-and-matrices-practice-page-1-15
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
# Your code here:
```

### Try this 9: Multiplication Table

Create a 10x10 multiplication table using a nested list comprehension. Each element at position [i][j] should be (i+1) × (j+1).

Expected output (first few rows):
```
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
[3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
...
```

```python exec
id: 03-lists-and-matrices-practice-page-1-16
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
# Your code here:
```

## What we set out to do

These were the aims of this notebook. Now that you have worked through it, they are a check on what happened rather than a promise about it.

- Master list creation, indexing, and slicing
- Understand 2D lists as matrices
- Practice list comprehensions for elegant code
- Apply basic matrix operations using numpy

## Looking back

Before leaving this page, a sentence on each. What you write stays on this device.

```reflect
- Something you expected before running a cell that turned out differently
- The one idea from this page you could explain to someone else now
- Something you would change or try next, if there were time
- A question this page raised for you that it did not answer. Bring it to the next session; these questions are where the next session starts.
```
