---
title: "Part 4: Matrix Multiplication - Composing Transformations"
slug: 04-matrix-multiplication
course: ai-and-ml-foundations
course_title: "AI and ML Foundations"
series: 1-linear-algebra
series_title: "Linear Algebra"
version: 2026.09.06.1
---

# Part 4: Matrix Multiplication - Composing Transformations

Welcome to the final notebook in our series! We've come a long way:
- We learned about vectors and how to visualize them
- We discovered the dot product and its geometric meaning
- We explored matrices and saw how they transform vectors

Today, we're going to discover **matrix multiplication** - one of the most powerful and beautiful ideas in mathematics. As we'll see, multiplying matrices is really about **composing transformations** - applying one transformation after another.

## What We'll Explore

- Building matrix multiplication from everything we've learned
- Understanding composition of transformations
- Discovering why matrix multiplication works the way it does
- Exploring fascinating properties and patterns
- Completing our linear algebra library!

## Setting Up

Let's gather all our tools from the previous notebooks:

```python exec
id: 04-matrix-multiplication-1
import matplotlib.pyplot as plt
import math

# Vector functions
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

# Matrix functions
def print_matrix(matrix, name="Matrix"):
    """Print a matrix nicely."""
    print(f"{name}:")
    for row in matrix:
        formatted_row = [f"{num:6.2f}" for num in row]
        print("  [" + "  ".join(formatted_row) + "]")
    print()

def matrix_vector_multiply(matrix, vector):
    """Multiply a 2x2 matrix by a 2D vector using dot products."""
    x = dot_product(matrix[0], vector)
    y = dot_product(matrix[1], vector)
    return [x, y]

def extract_column(matrix, col_index):
    """Extract a column from a matrix."""
    return [row[col_index] for row in matrix]

def create_identity_matrix(size):
    """Create an identity matrix."""
    matrix = []
    for i in range(size):
        row = []
        for j in range(size):
            row.append(1 if i == j else 0)
        matrix.append(row)
    return matrix
```

## The Motivation: Composing Transformations

Imagine we have two transformations:
1. Matrix **A** that does something (say, rotation)
2. Matrix **B** that does something else (say, scaling)

What if we want to apply **A** first, then apply **B** to the result? Can we find a single matrix that does both transformations at once?

Let's explore:

```python exec
id: 04-matrix-multiplication-2
# Let's take two simple transformations
A = [[2, 0], [0, 1]]  # Stretch in x-direction
B = [[1, 1], [0, 1]]  # Shear

# Take a test vector
v = [1, 1]

# Apply A first
v_after_A = matrix_vector_multiply(A, v)
print(f"Original vector: {v}")
print(f"After applying A: {v_after_A}")

# Now apply B to the result
v_after_B_then_A = matrix_vector_multiply(B, v_after_A)
print(f"After applying B to the result: {v_after_B_then_A}")

# Question: Can we find a single matrix C where C×v gives the same result?
```

## Building Matrix Multiplication

Here's the key insight: to find the combined transformation, we need to see where the **basis vectors** end up after both transformations.

Let's think through this step by step:

```python exec
id: 04-matrix-multiplication-3
# Basis vectors
e1 = [1, 0]
e2 = [0, 1]

print("Tracking the first basis vector [1, 0]:")
# Apply A first
e1_after_A = matrix_vector_multiply(A, e1)
print(f"  After A: {e1_after_A}")

# Then apply B
e1_final = matrix_vector_multiply(B, e1_after_A)
print(f"  After B: {e1_final}")

print("\nTracking the second basis vector [0, 1]:")
# Apply A first
e2_after_A = matrix_vector_multiply(A, e2)
print(f"  After A: {e2_after_A}")

# Then apply B
e2_final = matrix_vector_multiply(B, e2_after_A)
print(f"  After B: {e2_final}")

print("\nThe combined transformation matrix C should have:")
print(f"  First column: {e1_final}")
print(f"  Second column: {e2_final}")

C = [e1_final, e2_final]
# Wait, this creates a list of columns, but we need rows!
# We need to transpose it
C = [[e1_final[0], e2_final[0]],
     [e1_final[1], e2_final[1]]]

print("\nCombined matrix C:")
print_matrix(C, "C")

# Test it!
result_direct = matrix_vector_multiply(C, v)
print(f"C × {v} = {result_direct}")
print(f"B(A×{v}) = {v_after_B_then_A}")
print(f"They match: {result_direct == v_after_B_then_A}")
```

## Generalizing to Matrix Multiplication

What we just discovered is the essence of matrix multiplication! To multiply matrices B and A:
1. Apply A to each basis vector
2. Apply B to each result
3. Those results become the columns of B×A

But there's an elegant way to compute this using our dot product. Each element of the result is the dot product of a **row** from the first matrix with a **column** from the second matrix.

Let's implement this:

```python exec
id: 04-matrix-multiplication-4
def multiply_matrices(A, B):
    """
    Multiply two 2x2 matrices.

    The element at position (i,j) in the result is the dot product
    of row i from A with column j from B.

    This represents applying transformation B, then transformation A.
    (Note the order: A×B means "first B, then A")

    Parameters:
    - A: first matrix (2x2)
    - B: second matrix (2x2)

    Returns:
    - the product matrix A×B
    """
    # We'll build the result matrix
    result = []

    # For each row in A
    for i in range(len(A)):
        row = []

        # For each column in B
        for j in range(len(B[0])):
            # Get column j from B
            column_j = extract_column(B, j)

            # Compute dot product of row i from A with column j from B
            element = dot_product(A[i], column_j)
            row.append(element)

        result.append(row)

    return result
```

```python exec
id: 04-matrix-multiplication-5
# Test our matrix multiplication
A = [[2, 0], [0, 1]]
B = [[1, 1], [0, 1]]

C = multiply_matrices(B, A)  # Remember: this means "A first, then B"

print_matrix(A, "A")
print_matrix(B, "B")
print_matrix(C, "B×A (first A, then B)")

# Verify with a vector
v = [1, 1]
result1 = matrix_vector_multiply(C, v)
result2 = matrix_vector_multiply(B, matrix_vector_multiply(A, v))

print(f"C × v = {result1}")
print(f"B(A×v) = {result2}")
print(f"They match: {result1 == result2}")
```

## Visualizing Matrix Multiplication

```python exec
id: 04-matrix-multiplication-6
def visualize_composition(A, B, vectors):
    """
    Show how composing two transformations works.
    """
    # Create subplots
    fig, axes = plt.subplots(1, 3, figsize=(18, 6))

    # Original vectors
    plt.sca(axes[0])
    setup_plot()
    for v in vectors:
        draw_vector(v, color='blue')
    plt.title('Original Vectors', fontsize=14)

    # After first transformation (A)
    plt.sca(axes[1])
    setup_plot()
    for v in vectors:
        v_transformed = matrix_vector_multiply(A, v)
        draw_vector(v_transformed, color='green')
    plt.title('After transformation A', fontsize=14)

    # After second transformation (B applied to result)
    plt.sca(axes[2])
    setup_plot()
    for v in vectors:
        v_after_A = matrix_vector_multiply(A, v)
        v_final = matrix_vector_multiply(B, v_after_A)
        draw_vector(v_final, color='red')
    plt.title('After transformation B (composition)', fontsize=14)

    plt.tight_layout()
    plt.show()

# Test with some transformations
A = [[2, 0], [0, 0.5]]  # Scale
B = [[1, 0.5], [0, 1]]  # Shear

test_vectors = [[1, 0], [0, 1], [1, 1], [2, 1]]

print_matrix(A, "Transformation A (scale)")
print_matrix(B, "Transformation B (shear)")
print_matrix(multiply_matrices(B, A), "B×A (combined)")

visualize_composition(A, B, test_vectors)
```

## An Important Discovery: Order Matters!

Unlike regular number multiplication (where 3×5 = 5×3), matrix multiplication is **not commutative**. That is, A×B is usually different from B×A!

Let's explore why:

```python exec
id: 04-matrix-multiplication-7
A = [[2, 0], [0, 1]]
B = [[1, 1], [0, 1]]

AB = multiply_matrices(A, B)  # First B, then A
BA = multiply_matrices(B, A)  # First A, then B

print_matrix(A, "A")
print_matrix(B, "B")
print("\nTwo different orders:")
print_matrix(AB, "A×B")
print_matrix(BA, "B×A")

print(f"Are they the same? {AB == BA}")

# Visualize the difference
test_vector = [1, 1]
result_AB = matrix_vector_multiply(AB, test_vector)
result_BA = matrix_vector_multiply(BA, test_vector)

setup_plot()
draw_vector(test_vector, color='blue', label='original')
draw_vector(result_AB, color='red', label='A×B result')
draw_vector(result_BA, color='green', label='B×A result')
plt.title('Order Matters!')
plt.legend()
plt.show()
```

## Exploration: When Does Order NOT Matter?

**Challenge:** Can you find pairs of matrices where A×B = B×A?

Hint: Try these combinations:
- Two scaling matrices
- A matrix with itself
- The identity matrix with anything

```python exec
id: 04-matrix-multiplication-8
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
# Your experiments here:
```

## The Identity Matrix: Like Multiplying by 1

Remember the identity matrix? It's the matrix with 1s on the diagonal and 0s elsewhere. Let's discover its special property:

```python exec
id: 04-matrix-multiplication-9
I = create_identity_matrix(2)
A = [[3, 1], [2, 4]]

print_matrix(I, "Identity Matrix I")
print_matrix(A, "Some matrix A")

AI = multiply_matrices(A, I)
IA = multiply_matrices(I, A)

print_matrix(AI, "A×I")
print_matrix(IA, "I×A")

print(f"A×I = A? {AI == A}")
print(f"I×A = A? {IA == A}")
print("\nThe identity matrix is like the number 1 for matrices!")
```

## Interesting Patterns to Explore

### Pattern 1: Repeated Transformations

What happens when we apply the same transformation multiple times?

```python exec
id: 04-matrix-multiplication-10
# A scaling matrix
S = [[0.8, 0], [0, 0.8]]

print("Applying scaling repeatedly:")
current = S
for i in range(1, 6):
    print_matrix(current, f"S^{i}")
    current = multiply_matrices(S, current)

# What do you notice about the numbers?
```

### Pattern 2: A Fascinating Matrix

Remember our "mystery" rotation matrix from earlier? Let's multiply it by itself:

```python exec
id: 04-matrix-multiplication-11
R = [[0, -1], [1, 0]]

print_matrix(R, "R (mystery matrix)")

R2 = multiply_matrices(R, R)
print_matrix(R2, "R²")

R3 = multiply_matrices(R, R2)
print_matrix(R3, "R³")

R4 = multiply_matrices(R, R3)
print_matrix(R4, "R⁴")

print("What do you notice? What is this matrix doing?")
```

### Pattern 3: Finding Matrix Squares

**Investigation:** Given a matrix A, can you find a matrix B where B×B = A?

For example:

```python exec
id: 04-matrix-multiplication-12
# Target matrix
A = [[4, 0], [0, 9]]

# Try to find B where B² = A
# Hint for this one: try [[2, 0], [0, 3]]

B = [[2, 0], [0, 3]]
B_squared = multiply_matrices(B, B)

print_matrix(A, "Target A")
print_matrix(B, "Our guess B")
print_matrix(B_squared, "B²")
print(f"Does B² = A? {B_squared == A}")

# Now try finding a square root for different matrices
# What about [[1, 1], [0, 1]]? Does it have a square root?
```

## A Creative Challenge: Building Custom Transformations

Now that we can multiply matrices, we can create complex transformations by composing simple ones!

**Challenge:** Create transformations that:
1. Rotate 90° counterclockwise, then scale by 2
2. Scale by 2 in x-direction, then reflect across y-axis
3. Shear, then rotate, then scale

```python exec
id: 04-matrix-multiplication-13
# Some useful building blocks:
rotate_90 = [[0, -1], [1, 0]]
scale_2 = [[2, 0], [0, 2]]
reflect_y = [[-1, 0], [0, 1]]
shear_x = [[1, 0.5], [0, 1]]

# Build your compositions:
# Example: rotate then scale
rotate_then_scale = multiply_matrices(scale_2, rotate_90)

test_vectors = [[1, 0], [0, 1], [1, 1]]
visualize_composition(rotate_90, scale_2, test_vectors)

# Now try your own combinations!
```

## The Power of Associativity

While matrix multiplication isn't commutative (order matters), it is **associative**. This means:
(A×B)×C = A×(B×C)

In other words, if we're composing three transformations, it doesn't matter which pair we combine first!

```python exec
id: 04-matrix-multiplication-14
A = [[2, 0], [0, 1]]
B = [[1, 1], [0, 1]]
C = [[1, 0], [0, 2]]

# Method 1: Multiply (A×B) first, then multiply by C
AB = multiply_matrices(A, B)
result1 = multiply_matrices(AB, C)

# Method 2: Multiply (B×C) first, then multiply A by the result
BC = multiply_matrices(B, C)
result2 = multiply_matrices(A, BC)

print_matrix(result1, "(A×B)×C")
print_matrix(result2, "A×(B×C)")
print(f"Are they equal? {result1 == result2}")
```

## Understanding Why Matrix Multiplication Works This Way

Let's think deeply about what we've built. Why do we compute matrix multiplication using dot products of rows and columns?

Here's the insight:
- A matrix transforms vectors
- Each column tells us where a basis vector goes
- When we compose transformations, we need to track where basis vectors go through both transformations
- The dot product emerges naturally from this tracking!

Let's verify this understanding:

```python exec
id: 04-matrix-multiplication-15
def multiply_matrices_from_first_principles(A, B):
    """
    Multiply matrices by thinking about where basis vectors go.
    This is conceptually the same as our other implementation,
    but shows the geometric intuition more clearly.
    """
    # The columns of B tell us where the basis vectors go after B
    col1_of_B = extract_column(B, 0)
    col2_of_B = extract_column(B, 1)

    # Now apply A to these results
    col1_of_result = matrix_vector_multiply(A, col1_of_B)
    col2_of_result = matrix_vector_multiply(A, col2_of_B)

    # Build the result matrix from these columns
    result = [
        [col1_of_result[0], col2_of_result[0]],
        [col1_of_result[1], col2_of_result[1]]
    ]

    return result

# Test that both methods give the same answer
A = [[3, 1], [2, 4]]
B = [[1, 2], [3, 1]]

result1 = multiply_matrices(A, B)
result2 = multiply_matrices_from_first_principles(A, B)

print_matrix(result1, "Using dot products")
print_matrix(result2, "Using basis vector tracking")
print(f"Same result? {result1 == result2}")
```

## A Final Reflection Challenge

We've built an entire linear algebra library from scratch! Let's use everything we've learned for one final exploration.

**The Grand Challenge:**

1. Create a transformation that:
   - Rotates by some amount
   - Scales by different amounts in x and y
   - Shears

2. Apply it to several vectors

3. Now try to "reverse" it - find the transformation that undoes it

4. Verify that applying both transformations gets you back where you started

```python exec
id: 04-matrix-multiplication-16
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
# Your grand challenge solution:
```

## Our Complete Linear Algebra Library

Let's gather everything we've created into one place:

```python exec
id: 04-matrix-multiplication-17
# A complete summary of our linear algebra library!

print("="*60)
print("YOUR LINEAR ALGEBRA LIBRARY")
print("="*60)
print("\nVECTOR OPERATIONS:")
print("  • add_vectors(v1, v2) - Add two vectors")
print("  • scale_vector(scalar, v) - Multiply vector by number")
print("  • dot_product(v1, v2) - Compute dot product")
print("\nMATRIX OPERATIONS:")
print("  • matrix_vector_multiply(M, v) - Transform a vector")
print("  • multiply_matrices(A, B) - Compose transformations")
print("  • create_identity_matrix(n) - Create identity matrix")
print("\nVISUALIZATION:")
print("  • draw_vector(v) - Draw a vector")
print("  • print_matrix(M) - Display a matrix")
print("\nKEY INSIGHTS:")
print("  • Vectors represent directions and magnitudes")
print("  • Dot product measures alignment between vectors")
print("  • Matrices represent transformations of space")
print("  • Matrix multiplication composes transformations")
print("  • Everything builds on the dot product!")
print("="*60)
```

## Wrapping Up: What We've Accomplished

Over these four notebooks, we've taken an incredible journey:

**Part 1:** We started with simple Python lists and discovered how to represent and visualize vectors. We learned about vector addition and scalar multiplication.

**Part 2:** We explored the dot product and discovered its geometric meaning. We learned about projections and how to decompose vectors into components.

**Part 3:** We extended our ideas to matrices and discovered how matrices transform vectors. We saw how the columns of a matrix determine its transformation.

**Part 4:** We completed our journey by building matrix multiplication from first principles. We discovered that it represents composition of transformations and explored its properties.

## The Beautiful Connection

Notice how everything we built connects:
- Vectors led to the dot product
- The dot product gave us matrix-vector multiplication
- Matrix-vector multiplication led to matrix multiplication
- Matrix multiplication revealed the nature of transformation composition

Each concept built naturally on the previous ones. This is the beauty of mathematics - complex ideas emerge from simple building blocks!

## Where To Go From Here

You now have a solid foundation in linear algebra. Here are some directions to explore:

1. **Determinants**: What determines if a transformation is reversible?
2. **Eigenvalues**: What directions does a transformation leave unchanged?
3. **3D**: Extend everything to three dimensions
4. **Applications**: Computer graphics, machine learning, physics

Most importantly, you've learned that you can build powerful mathematical tools from scratch, one concept at a time.

Happy exploring!

## Looking back

Before leaving this page, a sentence on each. What you write stays on this device.

```reflect
- Something you expected before running a cell that turned out differently
- The one idea from this page you could explain to someone else now
- Something you would change or try next, if there were time
- A question this page raised for you that it did not answer. Bring it to the next session; these questions are where the next session starts.
```
