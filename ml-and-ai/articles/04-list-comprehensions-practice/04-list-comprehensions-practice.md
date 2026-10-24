---
title: "List Comprehensions"
slug: 04-list-comprehensions-practice
course: ai-and-ml-foundations
course_title: "AI and ML Foundations"
series: 0-python-and-numpy-refresher
series_title: "Python and NumPy Refresher"
version: 2026.09.06.1
---

```python exec
id: 04-list-comprehensions-practice-1
mylist = ['a', 'b', 'd','e']
myotherlist = ['w','x','y','z']
mynumlist = [7, 2, 33, -234, 65]
# make 3 lists with whatever you would like in them! Try to make three with different types and lengths! :)
print(mylist)
#add two of your lists together
addlist = mylist + myotherlist
#muliply one of your lists by a number
multiplylist = mylist * 4
# you just tried addition and multiplication, how about subtraction and division?

# make 3 variables that are different integers: one positive, one positive and large, and one negative (and small)

# can you print the value (or entry) of each of those variables as indicies in your lists?
# Example:
mynum = 2
negnum = -2
bignum = -123
NAN = '2'
mylist = ['a', 'b', 'd','e']
print(mylist[mynum]) # d
print(mylist[negnum]) # d
print(mylist[bignum]) #
#print(mylist[NAN])
```

# List Comprehensions
## From Simple Transformations to Complex Mathematical Operations


**Philosophy:**
List comprehensions are Python's implementation of set-builder notation from mathematics:
- Mathematical: {x² | x ∈ ℕ, x < 10}
- Python: `[x**2 for x in range(10)]`

This notebook progresses through difficulty levels, each requiring deeper mathematical thinking.

---
## Level 1: Foundations
### Basic Transformations

The simplest comprehensions apply a single operation to each element.

```python exec
id: 04-list-comprehensions-practice-2
# Traditional loop approach
numbers = [1, 2, 3, 4, 5]
squares_traditional = []
for number in numbers:
    squares_traditional.append(number ** 2)

print("Traditional:", squares_traditional)

# List comprehension approach
squares_comprehension = [number ** 2 for number in numbers]
print("Comprehension:", squares_comprehension)
```

### Try this 1.1: Simple Transformations

```python exec
id: 04-list-comprehensions-practice-3
# Given this list
values = [3, 7, 12, 18, 23, 29, 31]

# 1. Create a list of values doubled

# 2. Create a list of values cubed

# 3. Create a list of each value plus 10

# 4. Create a list of the reciprocals (1/x) for each value

# 5. Create a list of each value modulo 5
```

```python exec
id: 04-list-comprehensions-practice-4
# in one line, generate a list from 0 through 5,
# step1: square each entry,
# step2: and then double each entry,
# step3: then append one copy of the list onto itself.
```

### Try this 1.2: Range-Based Generation

```python exec
id: 04-list-comprehensions-practice-5
# 1. Generate the first 20 positive integers

# 2. Generate the first 15 odd numbers

# 3. Generate powers of 2 from 2^0 to 2^12

# 4. Generate multiples of 7 from 0 to 100

# 5. Generate the sequence: 0.1, 0.2, 0.3, ..., 1.0

myrange = range(1, 11)
listofrange = list(myrange)
print(listofrange)
print([float(number) for number in listofrange])
print([round(.1 * number, 1) for number in listofrange])
```

---
## Level 2: Filtering with Conditions
### Adding if Clauses

Syntax: `[expression for item in iterable if condition]`

```python exec
id: 04-list-comprehensions-practice-6
# Filter and transform
all_numbers = range(20)

# Only even numbers
even_numbers = [number for number in all_numbers if number % 2 == 0]
print("Even:", even_numbers)

# Squares of odd numbers
odd_squares = [number**2 for number in all_numbers if number % 2 == 1]
print("Odd squares:", odd_squares)

# Numbers divisible by 3 or 5
divisible = [number for number in all_numbers if number % 3 == 0 or number % 5 == 0]
print("Divisible by 3 or 5:", divisible)
```

### Try this 2.1: Conditional Filtering

```python exec
id: 04-list-comprehensions-practice-7
measurements = [12.5, 18.3, 22.7, 15.2, 28.9, 31.4, 19.8, 25.1, 17.6, 29.3]

# 1. Extract measurements greater than 20

# 2. Extract measurements between 15 and 25 (inclusive)

# 3. Square all measurements less than 20

# 4. Get measurements that when rounded are even numbers

# 5. Extract measurements where the integer part is divisible by 3
```

### Try this 2.2: Mathematical Predicates

```python exec
id: 04-list-comprehensions-practice-8
# 1. Find all perfect squares between 1 and 200

# 2. Find all numbers from 1 to 100 that are perfect cubes

# 3. Generate all numbers from 1 to 50 where the number equals the sum of its digits squared
#    Example: 13 -> 1² + 3² = 10 (not equal), 10 -> 1² + 0² = 1 (not equal)

# 4. Find all two-digit numbers where the number equals the product of its digits plus the sum of its digits

# 5. Find all numbers from 1 to 100 where the sum of divisors (excluding the number itself) equals the number
#    (These are perfect numbers)
```

---
## Level 3: Multiple Conditions and Transformations
### Conditional Expressions Inside Comprehensions

Syntax: `[expression_if_true if condition else expression_if_false for item in iterable]`

```python exec
id: 04-list-comprehensions-practice-9
# Absolute value without using abs()
numbers = [-5, 3, -8, 12, -1, 7, -9]
absolute_values = [number if number >= 0 else -number for number in numbers]
print("Absolute values:", absolute_values)

# Categorize numbers
values = range(-5, 6)
signs = ['positive' if value > 0 else 'negative' if value < 0 else 'zero'
         for value in values]
print("Signs:", signs)

# Clamp values to a range [0, 10]
raw_data = [-3, 5, 12, 8, -1, 15, 7, 0, 11]
clamped_data = [max(0, min(10, value)) for value in raw_data]
print("Clamped:", clamped_data)
```

### Try this 3.1: Conditional Transformations

```python exec
id: 04-list-comprehensions-practice-10
data_points = [23, -15, 42, -8, 31, -22, 17, -5, 38, -12]

# 1. Square positive numbers, cube negative numbers

# 2. Divide even numbers by 2, multiply odd numbers by 3

# 3. For numbers > 25, subtract 10; for numbers < 10, add 10; otherwise keep as is

# 4. Replace numbers divisible by 5 with 0, others with 1

# 5. Convert each number to its distance from 20 (absolute difference)
```

### Try this 3.2: Piecewise Functions

```python exec
id: 04-list-comprehensions-practice-11
# Implement these piecewise functions using list comprehensions

x_values = [value * 0.5 for value in range(-20, 21)]  # x from -10 to 10

# 1. f(x) = { x²     if x < 0
#           { 2x     if 0 ≤ x < 5
#           { 10     if x ≥ 5

# 2. g(x) = { -1    if x < 0
#           { 0     if x = 0
#           { 1     if x > 0
#    (This is the sign function)

# 3. h(x) = { x³ + 1      if x < -2
#           { 2x          if -2 ≤ x ≤ 2
#           { x² - 5      if x > 2

# 4. Implement the ReLU function: max(0, x)

# 5. Implement the Heaviside step function: H(x) = 0 if x < 0, else 1
```

---
## Level 4: Working with Indices
### Using enumerate and zip

```python exec
id: 04-list-comprehensions-practice-12
# Using enumerate to access both index and value
coefficients = [2, -3, 5, -1, 7]
# Create pairs (index, coefficient)
indexed_coefficients = [(index, coef) for index, coef in enumerate(coefficients)]
print("Indexed:", indexed_coefficients)

# Evaluate polynomial: 2x^0 - 3x^1 + 5x^2 - 1x^3 + 7x^4 at x=2
x_value = 2
polynomial_terms = [coef * (x_value ** index) for index, coef in enumerate(coefficients)]
polynomial_value = sum(polynomial_terms)
print(f"Polynomial at x={x_value}: {polynomial_value}")

# Using zip to combine lists
latitudes = [12.5, 15.3, 18.7, 22.1]
longitudes = [-75.2, -73.8, -71.5, -69.2]
coordinates = [(lat, lon) for lat, lon in zip(latitudes, longitudes)]
print("Coordinates:", coordinates)
```

### Try this 4.1: Index-Based Operations

```python exec
id: 04-list-comprehensions-practice-13
sequence = [10, 15, 12, 18, 20, 16, 22, 19, 25, 21]

# 1. Create a list where each element is multiplied by its index

# 2. Create a list of differences between consecutive elements
#    Hint: sequence[i+1] - sequence[i]

# 3. Create a list of three-element moving averages
#    (average of elements at indices i-1, i, i+1)

# 4. Create a list where even indices are squared and odd indices are cubed

# 5. Create a list of (index, value, cumulative_sum) tuples
```

### Try this 4.2: Combining Multiple Lists

```python exec
id: 04-list-comprehensions-practice-14
x_coordinates = [1, 2, 3, 4, 5]
y_coordinates = [2, 4, 3, 5, 6]
z_coordinates = [1, 3, 2, 4, 5]

# 1. Create a list of 3D points as tuples (x, y, z)

# 2. Calculate the distance from origin for each point: sqrt(x² + y² + z²)

# 3. Create a list of midpoints between consecutive 3D points

# 4. Find the Manhattan distance from origin: |x| + |y| + |z|

# 5. Create a list showing which coordinate (x, y, or z) has the largest value for each point
```

---
## Level 5: Nested Comprehensions
### Creating 2D Structures

```python exec
id: 04-list-comprehensions-practice-15
# Simple 2D list (3x4 matrix of zeros)
rows, cols = 3, 4
zero_matrix = [[0 for col in range(cols)] for row in range(rows)]
print("Zero matrix:")
for row in zero_matrix:
    print(row)

# Identity matrix
size = 4
identity_matrix = [[1 if row == col else 0 for col in range(size)] for row in range(size)]
print("\nIdentity matrix:")
for row in identity_matrix:
    print(row)

# Multiplication table
table_size = 5
mult_table = [[(row + 1) * (col + 1) for col in range(table_size)] for row in range(table_size)]
print("\nMultiplication table:")
for row in mult_table:
    print(row)
```

### Try this 5.1: Matrix Generation

```python exec
id: 04-list-comprehensions-practice-16
# 1. Create a 6x6 matrix where element [i][j] = i + j

# 2. Create a 5x5 matrix where element [i][j] = i² + j²

# 3. Create a 7x7 matrix where element [i][j] = max(i, j)

# 4. Create an 8x8 checkerboard pattern (alternating 0 and 1)
#    Hint: (row + col) % 2

# 5. Create a 6x6 matrix where element [i][j] = 2^(i+j)
```

### Try this 5.2: Special Matrices

```python exec
id: 04-list-comprehensions-practice-17
# 1. Create a 5x5 upper triangular matrix where non-zero elements equal i*j
#    (zeros below the main diagonal)

# 2. Create a 6x6 tridiagonal matrix (ones on main diagonal, -1 on diagonals above and below)
#    Hint: value is 1 if i==j, -1 if |i-j|==1, else 0

# 3. Create a 7x7 matrix where element [i][j] is the binomial coefficient C(i,j)
#    This is Pascal's triangle in matrix form
#    Hint: Use math.comb(i, j) or implement manually

# 4. Create a 5x5 Hilbert matrix where element [i][j] = 1/(i+j+1)

# 5. Create an 8x8 matrix where element [i][j] = (i-j)²
```

---
## Level 6: Flattening and Nested Iterations
### Working with Nested Structures

```python exec
id: 04-list-comprehensions-practice-18
# Flatten a 2D list
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

flattened = [element for row in matrix for element in row]
print("Flattened:", flattened)

# Create all pairs from two lists
list_a = [1, 2, 3]
list_b = [10, 20]
pairs = [(a, b) for a in list_a for b in list_b]
print("\nAll pairs:", pairs)

# Cartesian product with filtering
coordinates = [(x, y) for x in range(5) for y in range(5) if x + y < 6]
print("\nFiltered coordinates:", coordinates)
```

### Try this 6.1: Flattening Operations

```python exec
id: 04-list-comprehensions-practice-19
nested_data = [
    [12, 15, 18],
    [22, 25, 28, 31],
    [35, 38],
    [42, 45, 48, 51, 54]
]

# 1. Flatten the nested list and square each element

# 2. Extract all elements from nested_data that are divisible by 3

# 3. Find the sum of all elements in nested_data

# 4. Create a flat list of (row_index, element) tuples

# 5. Find the maximum element in each sublist, then return the maximum of those
```

### Try this 6.2: Generating Combinations

```python exec
id: 04-list-comprehensions-practice-20
# 1. Generate all pairs (a, b) where 1 ≤ a, b ≤ 10 and a < b

# 2. Find all Pythagorean triples (a, b, c) where a² + b² = c²
#    and 1 ≤ a ≤ b < c ≤ 25

# 3. Generate all points (x, y) where x² + y² ≤ 25 and x, y are integers
#    (points inside or on a circle of radius 5)

# 4. Create all three-digit numbers where each digit is different
#    and the sum of digits equals 15

# 5. Find all pairs of numbers (a, b) from 1 to 20 where gcd(a, b) = 1
#    (relatively prime pairs)
#    Hint: import math; use math.gcd()
```

---
## Level 7: Advanced Mathematical Applications
### Complex Transformations and Algorithms

```python exec
id: 04-list-comprehensions-practice-21
import math

# Sieve of Eratosthenes using list comprehension
def primes_up_to(limit):
    """Find all primes up to limit using comprehensions"""
    # Start with all numbers marked as potentially prime
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False

    for number in range(2, int(math.sqrt(limit)) + 1):
        if is_prime[number]:
            # Mark all multiples as not prime
            for multiple in range(number * number, limit + 1, number):
                is_prime[multiple] = False

    # Extract the primes
    return [num for num in range(limit + 1) if is_prime[num]]

primes = primes_up_to(50)
print("Primes up to 50:", primes)

# Discrete derivative (finite differences)
function_values = [1, 4, 9, 16, 25, 36, 49]  # f(x) = x²
derivative = [function_values[i+1] - function_values[i]
              for i in range(len(function_values) - 1)]
print("\nDiscrete derivative:", derivative)
```

### Try this 7.1: Number Theory

```python exec
id: 04-list-comprehensions-practice-22
# 1. Find all divisors of 360

# 2. Generate the list of Euler's totient function φ(n) for n from 1 to 20
#    φ(n) = count of numbers k where 1 ≤ k ≤ n and gcd(n,k) = 1

# 3. Find all numbers from 1 to 100 where the sum of proper divisors equals the number
#    (perfect numbers)

# 4. Generate the first 20 terms of the Catalan numbers
#    C_n = (2n)! / ((n+1)! * n!)

# 5. Find all numbers from 1 to 1000 that are both triangular and square
#    Triangular: n(n+1)/2, Square: m²
```

### Try this 7.2: Calculus Operations

```python exec
id: 04-list-comprehensions-practice-23
import math

# 1. Approximate the integral of f(x) = x² from 0 to 1 using Riemann sums
#    with 100 rectangles (use midpoint rule)

# 2. Calculate the numerical derivative of f(x) = sin(x) at x = π/4
#    using the limit definition: f'(x) ≈ [f(x+h) - f(x-h)] / (2h)
#    Try h = 0.01, 0.001, 0.0001

# 3. Find local maxima in the sequence: [3, 7, 5, 12, 8, 15, 11, 9, 18, 14]
#    A local maximum is where f(i-1) < f(i) > f(i+1)

# 4. Generate the Taylor series approximation of e^x at x=1
#    using the first 10 terms: e^x ≈ Σ(x^n / n!) for n=0 to 9

# 5. Implement Newton's method for f(x) = x² - 2 to find √2
#    Generate the sequence of approximations x_{n+1} = (x_n + 2/x_n)/2
#    starting from x_0 = 1, for 10 iterations
```

### Try this 7.3: Linear Algebra with Comprehensions

```python exec
id: 04-list-comprehensions-practice-24
matrix_a = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix_b = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

# 1. Transpose matrix_a using a nested comprehension

# 2. Add matrix_a and matrix_b element-wise

# 3. Multiply matrix_a by matrix_b (proper matrix multiplication)
#    Hint: C[i][j] = sum(A[i][k] * B[k][j] for k in range(len(A[0])))

# 4. Extract the diagonal elements of matrix_a

# 5. Calculate the Frobenius norm of matrix_a: sqrt(Σ(a_ij²))
```

---
## Level 8: Expert Challenges
### These require creative thinking and multiple techniques

### Try this 8.1: Fibonacci Variations

```python exec
id: 04-list-comprehensions-practice-25
# Note: These are very challenging with pure comprehensions!

# 1. Generate the first 20 Fibonacci numbers
#    Hint: You might need to use a helper list or recursion

# 2. Find all Fibonacci numbers less than 10,000 that are also prime

# 3. Generate the Fibonacci sequence modulo 10 until it repeats
#    (the Pisano period for modulo 10)

# 4. Calculate the ratios F(n+1)/F(n) for the first 15 Fibonacci numbers
#    (approaches the golden ratio)

# 5. Generate a generalized Fibonacci sequence where F(0)=a, F(1)=b,
#    and F(n) = F(n-1) + F(n-2), for a=2, b=1 (Lucas numbers)
```

### Try this 8.2: String and Pattern Generation

```python exec
id: 04-list-comprehensions-practice-26
# 1. Generate all possible binary strings of length 5

# 2. Find all permutations of the string "ABC" using comprehensions
#    Hint: This is very difficult with pure comprehensions!

# 3. Generate Pascal's triangle (first 10 rows) as a list of lists
#    where each element is computed from the row above

# 4. Create a list of all possible dice roll sums (2d6) with their frequencies
#    Result should be [(sum, frequency), ...]

# 5. Generate the Collatz sequence for n=27 until reaching 1
#    If even: n/2, if odd: 3n+1
```

### Try this 8.3: Data Analysis

```python exec
id: 04-list-comprehensions-practice-27
# Time series data: daily measurements
measurements = [23.5, 24.1, 23.8, 25.2, 24.7, 26.1, 25.8, 27.3, 26.9, 28.2,
                27.8, 29.1, 28.5, 30.2, 29.7, 28.9, 27.5, 26.8, 25.4, 24.2]

# 1. Calculate a 3-day moving average

# 2. Find all local maxima (peaks) in the data

# 3. Calculate the rate of change between consecutive days

# 4. Normalize the data to range [0, 1]
#    Formula: (x - min) / (max - min)

# 5. Identify "anomalies" - values more than 1.5 standard deviations from the mean
#    First calculate mean and std dev using comprehensions
```

---
## Summary and Best Practices

**When to Use List Comprehensions:**
- Simple transformations (mapping)
- Filtering with conditions
- Creating matrices and grids
- Mathematical operations on sequences

**When NOT to Use List Comprehensions:**
- Complex logic requiring many lines
- Operations with significant side effects
- When a regular loop is clearer
- Deeply nested comprehensions (>3 levels)

**Performance Notes:**
- Comprehensions are often faster than equivalent loops
- They create the entire list in memory at once
- For very large datasets, consider generators instead

**Style Guidelines:**
- Keep comprehensions readable - split long ones across lines
- Use descriptive variable names even in comprehensions
- If explaining the comprehension takes longer than the loop, use the loop
- Prioritize clarity over brevity

**Mathematical Applications:**
- Set operations and filtering
- Vector and matrix operations
- Sequence generation
- Coordinate transformations
- Discrete calculus operations

You've now mastered list comprehensions from basic to expert level!

## What we set out to do

These were the aims of this notebook. Now that you have worked through it, they are a check on what happened rather than a promise about it.

- Build fluency with list comprehension syntax
- Progress from simple to complex transformations
- Apply comprehensions to mathematical problems
- Recognize when comprehensions improve code clarity
- Master nested comprehensions for matrix operations

## Looking back

Before leaving this page, a sentence on each. What you write stays on this device.

```reflect
- Something you expected before running a cell that turned out differently
- The one idea from this page you could explain to someone else now
- Something you would change or try next, if there were time
- A question this page raised for you that it did not answer. Bring it to the next session; these questions are where the next session starts.
```
