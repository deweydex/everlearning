---
title: "Part 3: Discovering Matrices - Tables of Numbers with Power"
slug: 03-matrices-and-transformations
course: ai-and-ml-foundations
course_title: "AI and ML Foundations"
series: 1-linear-algebra
series_title: "Linear Algebra"
version: 2026.09.06.1
---

# Part 3: Discovering Matrices - Tables of Numbers with Power

Welcome to Part 3! So far, we've been working with vectors - lists of numbers that we can visualize as arrows. Today, we're going to explore **matrices**, which are rectangular arrays of numbers.

You might wonder: why do we need matrices? As we'll discover, matrices let us organize information in powerful ways and perform transformations that would be cumbersome with vectors alone.

## What We'll Explore Today

- Creating matrices as lists of lists
- Adding and subtracting matrices
- Multiplying matrices by scalars
- Visualizing what matrices do to vectors
- Building everything from our vector functions

Let's begin our journey into the world of matrices!

## Setting Up

As always, let's import our tools and bring back our vector functions:

```python exec
id: 03-matrices-and-transformations-1
import matplotlib.pyplot as plt
import math

# Our vector functions from before
def draw_vector(vector, color='blue', label=None):
    """Draw a vector as an arrow from the origin."""
    x, y = vector[0], vector[1]
    plt.arrow(0, 0, x, y, head_width=0.2, head_length=0.2,
              fc=color, ec=color, linewidth=2)
    if label:
        plt.text(x*0.5, y*0.5, label, fontsize=12)

def setup_plot(x_range=5, y_range=5):
    """Set up a coordinate system."""
    plt.figure(figsize=(8, 8))
    plt.axhline(y=0, color='k', linewidth=0.5)
    plt.axvline(x=0, color='k', linewidth=0.5)
    plt.xlim(-x_range, x_range)
    plt.ylim(-y_range, y_range)
    plt.grid(True, alpha=0.3)
    plt.gca().set_aspect('equal')
    plt.xlabel('x', fontsize=12)
    plt.ylabel('y', fontsize=12)

def add_vectors(v1, v2):
    """Add two vectors."""
    return [v1[0] + v2[0], v1[1] + v2[1]]

def scale_vector(scalar, vector):
    """Multiply a vector by a scalar."""
    return [scalar * vector[0], scalar * vector[1]]

def dot_product(v1, v2):
    """Calculate the dot product."""
    return v1[0] * v2[0] + v1[1] * v2[1]
```

## What Is a Matrix?

A **matrix** is a rectangular array of numbers arranged in rows and columns. In Python, we can represent a matrix as a list of lists, where each inner list is a row.

Here's a simple example:

```python exec
id: 03-matrices-and-transformations-2
# A 2x2 matrix (2 rows, 2 columns)
matrix_A = [
    [1, 2],  # First row
    [3, 4]   # Second row
]

print("Matrix A:")
for row in matrix_A:
    print(row)
```

Let's create a helper function to display matrices nicely:

```python exec
id: 03-matrices-and-transformations-3
def print_matrix(matrix, name="Matrix"):
    """
    Print a matrix in a readable format.

    Parameters:
    - matrix: a list of lists representing the matrix
    - name: optional name to display
    """
    print(f"{name}:")
    for row in matrix:
        # Format each number to have consistent spacing
        formatted_row = [f"{num:6.2f}" for num in row]
        print("  [" + "  ".join(formatted_row) + "]")
    print()  # Empty line for spacing

# Test it
print_matrix(matrix_A, "A")
```

## Accessing Matrix Elements

To access an element in a matrix, we use two indices: one for the row and one for the column.

```python exec
id: 03-matrices-and-transformations-4
# Remember: Python counts from 0!
element = matrix_A[0][1]  # Row 0 (first row), Column 1 (second column)
print(f"Element at row 0, column 1: {element}")
print(f"This is the number in the top-right position.")

# Let's get all elements
print(f"\nTop-left (0,0): {matrix_A[0][0]}")
print(f"Top-right (0,1): {matrix_A[0][1]}")
print(f"Bottom-left (1,0): {matrix_A[1][0]}")
print(f"Bottom-right (1,1): {matrix_A[1][1]}")
```

### Create Your Own Matrix

Try creating a few different matrices:

```python exec
id: 03-matrices-and-transformations-5
# Create a 2x2 matrix with your own numbers
my_matrix = [
    [0, 0],
    [0, 0]
]

# Try a 3x2 matrix (3 rows, 2 columns)
tall_matrix = [
    [1, 2],
    [3, 4],
    [5, 6]
]

print_matrix(my_matrix, "My Matrix")
print_matrix(tall_matrix, "Tall Matrix")
```

## Adding Matrices

Just like with vectors, we can add matrices by adding corresponding elements. The matrices must have the same dimensions (same number of rows and columns).

Let's build this operation from scratch:

```python exec
id: 03-matrices-and-transformations-6
def add_matrices(A, B):
    """
    Add two matrices element by element.

    Parameters:
    - A: first matrix (list of lists)
    - B: second matrix (list of lists)

    Returns:
    - a new matrix where result[i][j] = A[i][j] + B[i][j]
    """
    # Get the dimensions
    num_rows = len(A)  # How many rows?
    num_cols = len(A[0])  # How many columns? (looking at first row)

    # Create a new matrix to hold the result
    # We start with a matrix of zeros
    result = []

    # Go through each row
    for i in range(num_rows):
        # Create a new row for the result
        new_row = []

        # Go through each column in this row
        for j in range(num_cols):
            # Add the corresponding elements
            sum_element = A[i][j] + B[i][j]
            new_row.append(sum_element)

        # Add this row to our result matrix
        result.append(new_row)

    return result
```

```python exec
id: 03-matrices-and-transformations-7
# Test matrix addition
A = [
    [1, 2],
    [3, 4]
]

B = [
    [5, 6],
    [7, 8]
]

C = add_matrices(A, B)

print_matrix(A, "A")
print_matrix(B, "B")
print_matrix(C, "A + B")
```

## Subtracting Matrices

Subtraction works the same way - we subtract corresponding elements.

**Your turn:** Can you write a function to subtract matrices? Try using the pattern from `add_matrices()` as a guide.

```python exec
id: 03-matrices-and-transformations-8
def subtract_matrices(A, B):
    """
    Subtract matrix B from matrix A.

    Your implementation here!
    """
    # Hint: This is almost identical to add_matrices,
    # but with subtraction instead of addition
    pass  # Replace with your solution

# Test your function:
# result = subtract_matrices(A, B)
# print_matrix(result, "A - B")
```

## Scaling a Matrix

Just as we can multiply a vector by a scalar, we can multiply a matrix by a scalar - we multiply every element by that number.

```python exec
id: 03-matrices-and-transformations-9
def scale_matrix(scalar, matrix):
    """
    Multiply every element of a matrix by a scalar.

    Parameters:
    - scalar: the number to multiply by
    - matrix: the matrix to scale

    Returns:
    - a new matrix where result[i][j] = scalar * matrix[i][j]
    """
    result = []

    for row in matrix:
        new_row = []
        for element in row:
            new_row.append(scalar * element)
        result.append(new_row)

    return result

# Test it
A = [[1, 2], [3, 4]]
A_times_3 = scale_matrix(3, A)

print_matrix(A, "A")
print_matrix(A_times_3, "3 × A")
```

## Special Matrices: Identity and Zero

Some matrices have special properties. Let's explore a few:

```python exec
id: 03-matrices-and-transformations-10
def create_zero_matrix(rows, cols):
    """
    Create a matrix filled with zeros.

    Parameters:
    - rows: number of rows
    - cols: number of columns

    Returns:
    - a matrix of zeros
    """
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(0)
        matrix.append(row)
    return matrix

def create_identity_matrix(size):
    """
    Create an identity matrix - ones on the diagonal, zeros elsewhere.

    The identity matrix has a special property (we'll explore this later).

    Parameters:
    - size: the size of the square matrix

    Returns:
    - an identity matrix
    """
    matrix = []
    for i in range(size):
        row = []
        for j in range(size):
            # Put 1 on the diagonal (where row index equals column index)
            # Put 0 everywhere else
            if i == j:
                row.append(1)
            else:
                row.append(0)
        matrix.append(row)
    return matrix

# Create and display these special matrices
zero_matrix = create_zero_matrix(3, 3)
identity_matrix = create_identity_matrix(3)

print_matrix(zero_matrix, "Zero Matrix (3×3)")
print_matrix(identity_matrix, "Identity Matrix (3×3)")
```

## Exploring Patterns

**Question to ponder:**
- What happens when you add any matrix to a zero matrix?
- What do you think might be special about the identity matrix? (We'll discover this in the next notebook!)
- Can you create a matrix that, when added to itself, gives the zero matrix?

```python exec
id: 03-matrices-and-transformations-11
# Explore here:
```

## Matrices as Transformations: A First Look

Here's where things get really interesting. A matrix can be thought of as a transformation - it takes a vector as input and produces a new vector as output.

Let's create a simple function to apply a 2×2 matrix to a 2D vector:

```python exec
id: 03-matrices-and-transformations-12
def matrix_vector_multiply(matrix, vector):
    """
    Multiply a 2x2 matrix by a 2D vector.

    For a matrix [[a, b], [c, d]] and vector [x, y]:
    Result is [a*x + b*y, c*x + d*y]

    Notice: We're using the dot product! Each element of the result
    is the dot product of a row of the matrix with the vector.

    Parameters:
    - matrix: a 2x2 matrix
    - vector: a 2D vector

    Returns:
    - the transformed vector
    """
    # First row of matrix dot product with vector
    x = dot_product(matrix[0], vector)

    # Second row of matrix dot product with vector
    y = dot_product(matrix[1], vector)

    return [x, y]

# Try it out
M = [[2, 0], [0, 2]]  # What do you think this will do?
v = [1, 1]

result = matrix_vector_multiply(M, v)

print(f"Matrix M:")
print_matrix(M, "M")
print(f"Vector v: {v}")
print(f"M × v = {result}")
```

## Visualizing Matrix Transformations

Let's see what different matrices do to vectors visually:

```python exec
id: 03-matrices-and-transformations-13
def visualize_transformation(matrix, vectors, title="Transformation"):
    """
    Show how a matrix transforms a set of vectors.

    Parameters:
    - matrix: the transformation matrix
    - vectors: list of vectors to transform
    - title: title for the plot
    """
    setup_plot(6, 6)

    # Draw original vectors in blue
    for v in vectors:
        draw_vector(v, color='lightblue')

    # Draw transformed vectors in red
    for v in vectors:
        transformed = matrix_vector_multiply(matrix, v)
        draw_vector(transformed, color='red')

    plt.title(title)
    plt.legend(['Original (light blue)', 'Transformed (red)'])
    plt.show()

# Let's try different transformations
test_vectors = [[1, 0], [0, 1], [1, 1], [2, 1]]

# Scaling transformation
scale_matrix = [[2, 0], [0, 2]]
visualize_transformation(scale_matrix, test_vectors, "Scaling by 2")

# Stretching in x-direction only
stretch_x = [[3, 0], [0, 1]]
visualize_transformation(stretch_x, test_vectors, "Stretch in X")

# A rotation-like matrix
rotation_ish = [[0, -1], [1, 0]]
visualize_transformation(rotation_ish, test_vectors, "Mystery Transformation")
```

## What's Happening?

Look at the different transformations we just visualized. What patterns do you notice?

**Investigate:** Try creating your own transformation matrices. What happens when:
- Both diagonal elements are the same? (like [[2, 0], [0, 2]])
- The diagonal elements are different? (like [[2, 0], [0, 1]])
- The off-diagonal elements are non-zero? (like [[1, 0.5], [0, 1]])
- You use negative numbers?

```python exec
id: 03-matrices-and-transformations-14
# Create your own transformation matrices and test them:
```

## An Interesting Discovery Challenge

Remember that "mystery transformation" with the matrix [[0, -1], [1, 0]]?

**Challenge:**
1. What does this matrix do to the vector [1, 0]?
2. What does it do to [0, 1]?
3. If you apply this transformation **twice** to a vector (transform the result again), what happens?
4. What if you apply it **four times**?

```python exec
id: 03-matrices-and-transformations-15
mystery_matrix = [[0, -1], [1, 0]]
v = [1, 0]

# Apply once
v1 = matrix_vector_multiply(mystery_matrix, v)
print(f"After 1 transformation: {v} -> {v1}")

# Apply twice
v2 = matrix_vector_multiply(mystery_matrix, v1)
print(f"After 2 transformations: {v1} -> {v2}")

# Apply three times
v3 = matrix_vector_multiply(mystery_matrix, v2)
print(f"After 3 transformations: {v2} -> {v3}")

# Apply four times
v4 = matrix_vector_multiply(mystery_matrix, v3)
print(f"After 4 transformations: {v3} -> {v4}")

# What pattern do you see?
```

## Thinking About Matrix Columns

Here's a fascinating way to think about matrices: **the columns of a matrix tell you where the basis vectors go**.

The "basis vectors" are [1, 0] and [0, 1] - the arrows that point along the x and y axes.

Let's explore this:

```python exec
id: 03-matrices-and-transformations-16
def extract_column(matrix, col_index):
    """
    Extract a column from a matrix as a vector.

    Parameters:
    - matrix: the matrix
    - col_index: which column (0 for first, 1 for second, etc.)

    Returns:
    - a vector containing that column
    """
    column = []
    for row in matrix:
        column.append(row[col_index])
    return column

# Take any matrix
M = [[2, 1], [1, 2]]

# The basis vectors
e1 = [1, 0]
e2 = [0, 1]

# Where do they go?
Me1 = matrix_vector_multiply(M, e1)
Me2 = matrix_vector_multiply(M, e2)

# Extract the columns
col1 = extract_column(M, 0)
col2 = extract_column(M, 1)

print("Matrix M:")
print_matrix(M, "M")
print(f"First basis vector [1,0] transforms to: {Me1}")
print(f"First column of M: {col1}")
print(f"They match! {Me1 == col1}")
print()
print(f"Second basis vector [0,1] transforms to: {Me2}")
print(f"Second column of M: {col2}")
print(f"They match! {Me2 == col2}")
```

## Visualizing This Insight

```python exec
id: 03-matrices-and-transformations-17
def visualize_basis_transformation(matrix):
    """
    Show how a matrix transforms the basis vectors.
    """
    e1 = [1, 0]
    e2 = [0, 1]

    Me1 = matrix_vector_multiply(matrix, e1)
    Me2 = matrix_vector_multiply(matrix, e2)

    setup_plot(4, 4)

    # Original basis
    draw_vector(e1, color='lightblue', label='e1')
    draw_vector(e2, color='lightgreen', label='e2')

    # Transformed basis
    draw_vector(Me1, color='blue', label="M×e1")
    draw_vector(Me2, color='green', label="M×e2")

    # Draw grid to show how space is transformed
    for i in range(-3, 4):
        # Vertical lines (multiples of e1)
        start = add_vectors(scale_vector(i, Me1), scale_vector(-3, Me2))
        end = add_vectors(scale_vector(i, Me1), scale_vector(3, Me2))
        plt.plot([start[0], end[0]], [start[1], end[1]], 'k-', alpha=0.2, linewidth=0.5)

        # Horizontal lines (multiples of e2)
        start = add_vectors(scale_vector(-3, Me1), scale_vector(i, Me2))
        end = add_vectors(scale_vector(3, Me1), scale_vector(i, Me2))
        plt.plot([start[0], end[0]], [start[1], end[1]], 'k-', alpha=0.2, linewidth=0.5)

    plt.title('How the matrix transforms space')
    plt.show()

# Try different matrices
print("Identity matrix (no change):")
visualize_basis_transformation([[1, 0], [0, 1]])

print("Shear transformation:")
visualize_basis_transformation([[1, 1], [0, 1]])

print("Rotation-ish transformation:")
visualize_basis_transformation([[0, -1], [1, 0]])
```

## A Creative Exploration

Now that we understand how matrices transform space, let's experiment!

**Try creating matrices that:**
1. Flip vectors across the x-axis (hint: y-coordinates should become negative)
2. Flip vectors across the y-axis  
3. Flip vectors across the line y=x (swapping x and y coordinates)
4. Compress everything toward the x-axis

For each one, think about where [1, 0] and [0, 1] should go, and make those your matrix columns!

```python exec
id: 03-matrices-and-transformations-18
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
# Your creative matrices here:

# Example: flip across x-axis
# [1, 0] should stay [1, 0]
# [0, 1] should become [0, -1]
flip_x = [[1, 0], [0, -1]]

test_vectors = [[1, 0], [0, 1], [1, 1], [2, 1]]
visualize_transformation(flip_x, test_vectors, "Flip across X-axis")

# Now try your own!
```

## Wrapping Up Part 3

What we've discovered today:

1. **Matrices** are rectangular arrays of numbers, represented as lists of lists in Python
2. We can add, subtract, and scale matrices (element-wise operations)
3. **Matrices transform vectors** - they take a vector as input and produce a new vector
4. We built matrix-vector multiplication using our dot product function!
5. The columns of a matrix show where the basis vectors [1,0] and [0,1] go
6. Matrices can represent many transformations: scaling, flipping, rotating, shearing

Our growing library now includes:
- `add_matrices(A, B)`
- `scale_matrix(scalar, matrix)`
- `create_zero_matrix(rows, cols)`
- `create_identity_matrix(size)`
- `matrix_vector_multiply(matrix, vector)`
- `extract_column(matrix, col_index)`

In the next notebook, we'll explore the most powerful operation: **matrix multiplication**. We'll discover how combining transformations leads to one of the most important ideas in linear algebra!

## Looking back

Before leaving this page, a sentence on each. What you write stays on this device.

```reflect
- Something you expected before running a cell that turned out differently
- The one idea from this page you could explain to someone else now
- Something you would change or try next, if there were time
- A question this page raised for you that it did not answer. Bring it to the next session; these questions are where the next session starts.
```
