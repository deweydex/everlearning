---
title: "practice-lists-and-matrices-page-2 (2 of 2)"
slug: practice-lists-and-matrices-page-2
course: programming-and-design-principles
course_title: "Programming and Design Principles"
series: practice
series_title: "Practice"
version: 2026.09.06.1
---

Before starting this page, run the cell below. It repeats the imports and definitions from the earlier pages that this page uses.

```python exec
id: practice-lists-and-matrices-page-2-setup
numbers = [10, 20, 30, 40, 50]

# Your code here:

# Traditional way: using a loop
squares_loop = []
for i in range(5):
    squares_loop.append(i ** 2)
print("Squares (loop):", squares_loop)

# List comprehension way: one line!
squares_comp = [i ** 2 for i in range(5)]
print("Squares (comprehension):", squares_comp)

# Both produce: [0, 1, 4, 9, 16]

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

---
## Part 4: Introduction to NumPy

**NumPy** (Numerical Python) is THE library for numerical computing. It provides powerful array objects that are:
- Much faster than Python lists
- Easier to work with for mathematical operations
- The foundation for data science and machine learning

NumPy arrays are called **ndarrays** (n-dimensional arrays).

```python exec
id: practice-lists-and-matrices-page-2-1
import numpy as np

# Creating numpy arrays
arr1 = np.array([1, 2, 3, 4, 5])          # From a list
arr2 = np.zeros(5)                         # Array of zeros
arr3 = np.ones(5)                          # Array of ones
arr4 = np.arange(0, 10, 2)                # Like range(): start, stop, step
arr5 = np.linspace(0, 1, 5)               # 5 evenly spaced numbers from 0 to 1

print("Array from list:", arr1)
print("Zeros:", arr2)
print("Ones:", arr3)
print("Range:", arr4)
print("Linspace:", arr5)
```

### Why NumPy is Powerful: Vectorized Operations

With regular Python lists, you need loops. With NumPy, operations work on the entire array at once!

```python exec
id: practice-lists-and-matrices-page-2-2
# With regular lists: need a loop or comprehension
numbers = [1, 2, 3, 4, 5]
doubled_list = [x * 2 for x in numbers]
print("List doubled:", doubled_list)

# With NumPy: just multiply!
arr = np.array([1, 2, 3, 4, 5])
doubled_arr = arr * 2
print("NumPy doubled:", doubled_arr)

# More operations
print("\nSquared:", arr ** 2)
print("Plus 10:", arr + 10)
print("Divided by 2:", arr / 2)
```

### 2D NumPy Arrays (Matrices)

NumPy really shines with matrices. You get true 2D indexing and powerful operations.

```python exec
id: practice-lists-and-matrices-page-2-3
# Creating 2D arrays
matrix1 = np.array([[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]])

matrix2 = np.zeros((3, 4))        # 3 rows, 4 columns of zeros
matrix3 = np.ones((2, 5))         # 2 rows, 5 columns of ones
matrix4 = np.eye(4)               # 4x4 identity matrix

print("Matrix 1:")
print(matrix1)
print("\nShape:", matrix1.shape)   # (3, 3)
print("Size:", matrix1.size)       # 9 total elements

print("\nZeros (3x4):")
print(matrix2)

print("\nIdentity (4x4):")
print(matrix4)
```

### NumPy Indexing and Slicing

NumPy gives us cleaner syntax for 2D indexing: `array[row, column]` instead of `array[row][column]`

```python exec
id: practice-lists-and-matrices-page-2-4
matrix = np.array([[10, 20, 30, 40],
                   [50, 60, 70, 80],
                   [90, 100, 110, 120]])

print("Full matrix:")
print(matrix)

print("\nElement at [1, 2]:", matrix[1, 2])        # 70
print("First row:", matrix[0, :])                  # [10, 20, 30, 40]
print("Second column:", matrix[:, 1])              # [20, 60, 100]
print("Top-left 2x2:", matrix[:2, :2])             # [[10, 20], [50, 60]]
print("Last two rows:", matrix[-2:, :])            # Last 2 rows, all columns
```

### Try this 10: NumPy Basics

1. Create a NumPy array of numbers from 1 to 20
2. Reshape it into a 4x5 matrix
3. Extract the third row
4. Extract the first and last columns (as separate arrays)
5. Find the sum of all elements

```python exec
id: practice-lists-and-matrices-page-2-5
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
# Your code here:
```

---
## Part 5: Basic Matrix Operations

Now let's explore fundamental matrix operations that are crucial in mathematics and computer science.

### Element-wise Operations

These operations work on corresponding elements of arrays.

```python exec
id: practice-lists-and-matrices-page-2-6
A = np.array([[1, 2],
              [3, 4]])

B = np.array([[5, 6],
              [7, 8]])

print("Matrix A:")
print(A)
print("\nMatrix B:")
print(B)

# Element-wise operations
print("\nA + B (element-wise addition):")
print(A + B)

print("\nA * B (element-wise multiplication):")
print(A * B)

print("\nA ** 2 (element-wise square):")
print(A ** 2)
```

### Matrix Multiplication (Dot Product)

**Important:** Matrix multiplication is NOT element-wise! It follows mathematical matrix multiplication rules.

For matrices A (m×n) and B (n×p), the result C (m×p) has elements:
C[i,j] = sum of (A[i,k] × B[k,j]) for all k

```python exec
id: practice-lists-and-matrices-page-2-7
A = np.array([[1, 2],
              [3, 4]])

B = np.array([[5, 6],
              [7, 8]])

# Matrix multiplication (dot product)
C = np.dot(A, B)
# Alternative: C = A @ B

print("A @ B (matrix multiplication):")
print(C)

# Let's verify the calculation manually for element [0,0]:
# C[0,0] = A[0,0]*B[0,0] + A[0,1]*B[1,0] = 1*5 + 2*7 = 5 + 14 = 19
print("\nManual calculation of C[0,0]:", 1*5 + 2*7)
```

### Matrix Transpose

The **transpose** flips a matrix over its diagonal - rows become columns and vice versa.

```python exec
id: practice-lists-and-matrices-page-2-8
A = np.array([[1, 2, 3],
              [4, 5, 6]])

print("Original A (2x3):")
print(A)

print("\nTranspose A.T (3x2):")
print(A.T)

# Notice how rows became columns:
# Original row [1, 2, 3] → Transposed column [1, 4]
# Original row [4, 5, 6] → Transposed columns [2, 5], [3, 6]
```

### Useful Matrix Functions

```python exec
id: practice-lists-and-matrices-page-2-9
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

print("Matrix:")
print(matrix)

# Statistical operations
print("\nSum of all elements:", np.sum(matrix))
print("Mean:", np.mean(matrix))
print("Maximum:", np.max(matrix))
print("Minimum:", np.min(matrix))

# Operations along axes
print("\nSum of each column (axis=0):", np.sum(matrix, axis=0))
print("Sum of each row (axis=1):", np.sum(matrix, axis=1))

print("\nMean of each column:", np.mean(matrix, axis=0))
print("Max of each row:", np.max(matrix, axis=1))
```

### Try this 11: Matrix Arithmetic

Given two matrices:
```
A = [[2, 1],    B = [[1, 0],
     [3, 4]]         [2, 3]]
```

Calculate:
1. A + B
2. 3 × A (scalar multiplication)
3. A @ B (matrix multiplication)
4. B @ A (notice: matrix multiplication is not commutative!)
5. A.T (transpose of A)

```python exec
id: practice-lists-and-matrices-page-2-10
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
A = np.array([[2, 1],
              [3, 4]])

B = np.array([[1, 0],
              [2, 3]])

# Your code here:
```

### Try this 12: Building a Simple Image Filter

Images can be represented as matrices! Each pixel is a number representing brightness (0 = black, 255 = white).

1. Create a 5x5 matrix of random integers between 0 and 255 (use `np.random.randint`)
2. Apply a "brightness filter" by adding 50 to all pixels (but cap at 255)
3. Apply a "contrast filter" by multiplying by 1.5 (but cap at 255)
4. Create a "border detection" by finding the difference between adjacent pixels

```python exec
id: practice-lists-and-matrices-page-2-11
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
# Your code here:
```

### Try this 13: Matrix Analysis

Given a matrix representing test scores (rows = students, columns = tests):

1. Calculate the average score for each student
2. Calculate the average score for each test
3. Find which student had the highest total score
4. Find which test was the hardest (lowest average)
5. Normalize the scores to a 0-100 scale using: `(score - min) / (max - min) * 100`

```python exec
id: practice-lists-and-matrices-page-2-12
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
# Scores: 5 students, 4 tests
scores = np.array([[85, 90, 78, 92],
                   [70, 75, 80, 85],
                   [95, 88, 92, 94],
                   [60, 65, 70, 72],
                   [88, 86, 84, 90]])

# Your code here:
```

---
## Part 6: Practical Applications

Let's apply what we've learned to real-world scenarios!

### Try this 14: Weather Data Analysis

You have temperature data for a week (7 days × 4 measurements per day).

1. Create the matrix from the data below
2. Find the daily average temperature (average of each row)
3. Find the time-of-day average (average of each column)
4. Find the hottest and coldest temperatures recorded
5. Determine which day had the greatest temperature variation

```python exec
id: practice-lists-and-matrices-page-2-13
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
# Temperature data (degrees Celsius)
# Columns: 6am, 12pm, 6pm, 12am
temps = [
    [12, 18, 16, 10],  # Monday
    [13, 20, 18, 11],  # Tuesday
    [11, 19, 17, 12],  # Wednesday
    [14, 22, 19, 13],  # Thursday
    [15, 23, 20, 14],  # Friday
    [16, 25, 21, 15],  # Saturday
    [14, 21, 18, 12]   # Sunday
]

temps = np.array(temps)

# Your code here:
```

### Try this 15: Sales Data

A store tracks sales of 4 products over 6 months.

1. Create a 6×4 matrix with sales data
2. Calculate total sales for each month
3. Calculate total sales for each product
4. Find which product had the highest average monthly sales
5. Calculate the growth rate for each product (last month / first month)
6. Identify any months where total sales were below average

```python exec
id: practice-lists-and-matrices-page-2-14
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
# Sales data (in thousands)
sales = np.array([
    [45, 52, 38, 61],  # January
    [48, 55, 42, 58],  # February
    [52, 58, 45, 64],  # March
    [55, 60, 48, 67],  # April
    [58, 65, 52, 71],  # May
    [62, 68, 55, 75]   # June
])

products = ['Product A', 'Product B', 'Product C', 'Product D']

# Your code here:
```

### Try this 16: Distance Matrix

Create a distance matrix for 4 cities. A distance matrix shows the distance from each city to every other city.

Properties of a distance matrix:
- Diagonal is all zeros (distance from a city to itself)
- Symmetric (distance from A to B equals distance from B to A)

Given partial data:
- Dublin to Cork: 250 km
- Dublin to Galway: 220 km
- Dublin to Limerick: 200 km
- Cork to Galway: 210 km
- Cork to Limerick: 100 km
- Galway to Limerick: 90 km

1. Create the 4×4 distance matrix
2. Verify it's symmetric
3. Find the two closest cities
4. Find the two farthest cities
5. Calculate the total distance for a round trip: Dublin → Cork → Limerick → Galway → Dublin

```python exec
id: practice-lists-and-matrices-page-2-15
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
# Cities: Dublin (0), Cork (1), Galway (2), Limerick (3)

# Your code here:
```

### Try this 17: Creating a Simple Transition Matrix

A **transition matrix** shows probabilities of moving from one state to another. This is used in Markov chains!

Scenario: A customer's app usage patterns
- States: [Browsing, Shopping, Checkout]
- From Browsing: 60% stay browsing, 30% go to shopping, 10% leave
- From Shopping: 20% go back to browsing, 50% stay shopping, 30% go to checkout
- From Checkout: 10% go back to shopping, 90% complete (leave)

1. Create the 3×3 transition matrix
2. Verify each row sums to 1.0 (probabilities must sum to 100%)
3. If we start with [1000, 0, 0] customers in Browsing, where are they after one step? (Hint: multiply the state vector by the transition matrix)
4. Where are they after two steps?

```python exec
id: practice-lists-and-matrices-page-2-16
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
# Your code here:
```

---
## Summary and Next Steps

**What you've learned:**
- List indexing and slicing
- List comprehensions for elegant code
- 2D lists as matrices
- NumPy arrays and operations
- Matrix operations (addition, multiplication, transpose)
- Practical applications (data analysis, transition matrices)

**Next steps:**
- Practice with loops to process these data structures
- Explore more NumPy functions (`np.linalg` for advanced matrix operations)
- Learn about higher-dimensional arrays
- Apply these concepts to machine learning algorithms

**Key Takeaway:** Matrices are everywhere in computing - from graphics and games to data science and AI. Mastering these basics opens doors to countless applications!

## Looking back

Before leaving this page, a sentence on each. What you write stays on this device.

```reflect
- Something you expected before running a cell that turned out differently
- The one idea from this page you could explain to someone else now
- Something you would change or try next, if there were time
- A question this page raised for you that it did not answer. Bring it to the next session; these questions are where the next session starts.
```
