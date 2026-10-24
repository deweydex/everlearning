---
title: "Linear Algebra Fundamentals: Vectors and Matrices from Scratch"
slug: 06-linear-algebra-fundamentals
course: ai-and-ml-foundations
course_title: "AI and ML Foundations"
series: 1-linear-algebra
series_title: "Linear Algebra"
version: 2026.09.06.1
---

# Linear Algebra Fundamentals: Vectors and Matrices from Scratch

In this notebook, we'll build fundamental linear algebra operations from scratch using only Python lists and matplotlib for visualization. By implementing these operations yourself, you'll gain a deeper understanding of how vectors and matrices work.

```python exec
id: 06-linear-algebra-fundamentals-1
import matplotlib.pyplot as plt
import math

# Set up plotting style
plt.style.use('default')

```

## Part 1: Vector Addition and Subtraction

A vector is simply a list of numbers. In 2D space, a vector has two components: [x, y].

### Vector Addition
To add two vectors, we add their corresponding components:
- [a, b] + [c, d] = [a+c, b+d]

### Vector Subtraction
Similarly, subtraction works component-wise:
- [a, b] - [c, d] = [a-c, b-d]

```python exec
id: 06-linear-algebra-fundamentals-2
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
def vector_add(vector1: list, vector2: list ):
    """
    Add two vectors entry-wise.

    Args:
        vector1: First vector as a list [x_1, y_1]
        vector2: Second vector as a list [x_2, y_2]

    Returns:
        Result vector as a list [x, y]

    """
    # first attempt

    x_1 = vector1[0]
    y_1 = vector1[1]
    x_2 = vector2[0]
    y_2 = vector2[1]

    vector_sum = [x_1 + x_2, y_1 + y_2]

    return vector_sum
"""
    # alternate
    vectorsum = [vector1[0] + vector2[0], vector1[1] + vector2[1]]
    return vectorsum

    # alternate
    return [vector1[0] + vector1[0], vector1[1] + vector2[1]]
"""
def vector_subtract(vector1, vector2):
    """
    Subtract vector2 from vector1 component-wise.

    Args:
        vector1: First vector as a list [x, y]
        vector2: Second vector as a list [x, y]

    Returns:
        Result vector as a list [x, y]

    TODO: Implement this function
    """
    # Your code here
    return [vector1[0] - vector2[0], vector1[1] - vector2[1]]
```

```python exec
id: 06-linear-algebra-fundamentals-3
# Test your functions
v1 = [3, 4]
v2 = [1, 2]

print(f"v1 = {v1}")
print(f"v2 = {v2}")
print(f"v1 + v2 = {vector_add(v1, v2)}")
print(f"v1 - v2 = {vector_subtract(v1, v2)}")
```

### Visualizing Vector Addition and Subtraction

Let's create a function to visualize vectors as arrows on a 2D plot.

```python exec
id: 06-linear-algebra-fundamentals-4
def plot_vectors(vectors, colors=None, labels=None, title="Vector Visualization"):
    """
    Plot multiple vectors as arrows from the origin.

    Args:
        vectors: List of vectors, where each vector is [x, y]
        colors: List of colors for each vector (optional)
        labels: List of labels for each vector (optional)
        title: Title for the plot
    """
    fig, ax = plt.subplots(figsize=(8, 8))

    # Set default colors and labels if not provided
    if colors is None:
        colors = ['blue', 'red', 'green', 'orange', 'purple'] * (len(vectors) // 5 + 1)
    if labels is None:
        labels = [f'v{i+1}' for i in range(len(vectors))]

    # Plot each vector
    for vector, color, label in zip(vectors, colors, labels):
        ax.arrow(0, 0, vector[0], vector[1],
                head_width=0.3, head_length=0.2,
                fc=color, ec=color, linewidth=2, label=label)

    # Set up the plot
    max_val = max([abs(v[i]) for v in vectors for i in range(2)]) + 1
    ax.set_xlim(-max_val, max_val)
    ax.set_ylim(-max_val, max_val)
    ax.axhline(y=0, color='k', linewidth=0.5)
    ax.axvline(x=0, color='k', linewidth=0.5)
    ax.grid(True, alpha=0.3)
    ax.set_aspect('equal')
    ax.legend()
    ax.set_title(title)
    ax.set_xlabel('x')
    ax.set_ylabel('y')

    plt.tight_layout()
    plt.show()
```

```python exec
id: 06-linear-algebra-fundamentals-5
# Visualize vector addition
v1 = [3, 2]
v2 = [2, 3]
v_sum = vector_add(v1, v2)

plot_vectors([v1, v2, v_sum],
             colors=['blue', 'red', 'green'],
             labels=['v1', 'v2', 'v1 + v2'],
             title='Vector Addition')
```

```python exec
id: 06-linear-algebra-fundamentals-6
def vector_average(vector1, vector2):
    """
    here we want to take the average of two vectors (which each have 2 entries)
    well, an average of two numbers is just adding them and dividing by two
    so if we have two numbers a and b, the average is (a + b)/2
    so, for vectors, lets just do the same thing!
    so we will have (x_1 + x_2)/2 and (y_1 + y_2)/2 and that is what we will return

    """
    return [(vector1[0] + vector2[0])/2, (vector1[1] + vector2[1])/2 ]
```

```python exec
id: 06-linear-algebra-fundamentals-7
v1 = [3, 2]
v2 = [2, 3]
v_sum = vector_average(v1, v2)

plot_vectors([v1, v2, v_sum],
             colors=['blue', 'red', 'green'],
             labels=['v1', 'v2', '(v1 + v2)/2'],
             title='Vector Average')
```

```python exec
id: 06-linear-algebra-fundamentals-8
# Visualize vector subtraction
v1 = [3, 2]
v2 = [2, 3]
v_diff = vector_subtract(v1, v2)


plot_vectors([v1, v2, v_diff],
             colors=['blue', 'red', 'green'],
             labels=['v1', 'v2', 'v1 - v2'],
             title='Vector Subtraction')
```

```python exec
id: 06-linear-algebra-fundamentals-9
# Visualize vector subtraction
v1 = [3, 2]
v2 = [-1*2, -1*3]
v_average = vector_average(v1, v2)


plot_vectors([v1, v2,  v_average],
             colors=['blue', 'red', 'green'],
             labels=['v1', '-1*v2', '(v1 + -1*v2)/2'],
             title='Vector average')
```

## Part 2: The Dot Product

The dot product (also called scalar product) of two vectors produces a scalar (single number).

For two vectors [a, b] and [c, d], the dot product is:
- $[a, b] · [c, d] = a \cdot c + b \cdot d $

The dot product tells us about the relationship between two vectors:
- If positive: vectors point in similar directions
- If zero: vectors are perpendicular (orthogonal)
- If negative: vectors point in opposite directions

```python exec
id: 06-linear-algebra-fundamentals-10
import math
def dot_product(vector1, vector2):
    """
    Calculate the dot product of two vectors.
    dot_product([a, b, c], [d, e, f]) --> a * d + b * e + c * f
    Arguments:
        vector1: First vector as a list [x_1, y_1]
        vector2: Second vector as a list [x_2, y_2]

    Returns:
        The dot product as a scalar (single number)
        dotprod(v1, v2) = x_1 * x_2 + y_1 * y_2

    """
    # we need a loop! bc otherwise josh can be a jerk and keep adding entries to the end of the vector
    # for, while
    # when do we use for, when do we use while...
    # file = file('myfile.txt')
    """
    while my file has characters left...
        make the characters uppercase
    for each character in file...
        make the charachter uppercase
    for character_number in range(length(file))
        make file[character_number] uppercase"""

    vector_length = len(vector1) # just choose one of the vectors for the length, assume they are the same length for now...
    terms_multiplied_together= vector1.copy()
    for index in range(vector_length):
        terms_multiplied_together[index] = vector1[index] * vector2[index]


    """
    at the end of this loop, we have a list, of all of the terms of our two vectors, multiplied together
    if we have vectors
    X = [x_0, x_1, ... , x_n-1, x_n]
    Y = [y_0, y_1, ... , y_n-1, y_n]
    terms_multiplied together = [x_0 * y_0, x_1 * y_1, ... x_n-1 * y_n-1, x_n * y_n]

    but we want the sum of all the terms in terms_multiplied_together!

    """
    print()
    dot_product = sum(terms_multiplied_together)
    return dot_product
```

```python exec
id: 06-linear-algebra-fundamentals-11
vector_length = 4
print(list(range(vector_length)))
```

```python exec
id: 06-linear-algebra-fundamentals-12
# lets do another test
vector1 = [1, 2, 3, 7]
vector2 = [4, 5, 6, 8]
print(dot_product(vector1, vector2))
```

```python exec
id: 06-linear-algebra-fundamentals-13
# Test dot product
v1 = [3, 4]
v2 = [2, 1]

result = dot_product(v1, v2)
print(f"v1 · v2 = {result}")

# Test with perpendicular vectors
v3 = [1, 0]
v4 = [0, 1]
result2 = dot_product(v3, v4)
print(f"\nPerpendicular vectors: {v3} · {v4} = {result2}")
```

### Visualizing the Dot Product

The dot product is related to the angle between vectors and their magnitudes.

```python exec
id: 06-linear-algebra-fundamentals-14
def visualize_dot_product(v1, v2):
    """
    Visualize two vectors and display their dot product.
    """
    dot_prod = dot_product(v1, v2)

    fig, ax = plt.subplots(figsize=(8, 8))

    # Plot vectors
    ax.arrow(0, 0, v1[0], v1[1],
            head_width=0.3, head_length=0.2,
            fc='blue', ec='blue', linewidth=2, label='v1')
    ax.arrow(0, 0, v2[0], v2[1],
            head_width=0.3, head_length=0.2,
            fc='red', ec='red', linewidth=2, label='v2')

    # Set up the plot
    max_val = max([abs(v1[0]), abs(v1[1]), abs(v2[0]), abs(v2[1])]) + 1
    ax.set_xlim(-max_val, max_val)
    ax.set_ylim(-max_val, max_val)
    ax.axhline(y=0, color='k', linewidth=0.5)
    ax.axvline(x=0, color='k', linewidth=0.5)
    ax.grid(True, alpha=0.3)
    ax.set_aspect('equal')
    ax.legend()

    # Display dot product
    if dot_prod > 0:
        relationship = "(pointing in similar directions)"
    elif dot_prod == 0:
        relationship = "(perpendicular/orthogonal)"
    else:
        relationship = "(pointing in opposite directions)"

    ax.set_title(f'Dot Product: v1 · v2 = {dot_prod:.2f} {relationship}')
    ax.set_xlabel('x')
    ax.set_ylabel('y')

    plt.tight_layout()
    plt.show()

# Test with different vector pairs
print("Similar directions:")
visualize_dot_product([3, 2], [2, 1])

print("\nPerpendicular vectors:")
visualize_dot_product([3, 0], [0, 2])

print("\nOpposite directions:")
visualize_dot_product([3, 2], [-3, -2])
```

## Part 3: Vector Magnitude and Unit Vectors

### Vector Magnitude (Length)
The magnitude of a vector [x, y] is its length, calculated as:
- ||v|| = √(x² + y²)

### Unit Vectors
A unit vector is a vector with magnitude 1. To create a unit vector from any non-zero vector, divide each component by the vector's magnitude:
- unit vector = v / ||v||

```python exec
id: 06-linear-algebra-fundamentals-15
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
def vector_magnitude(v):
    """
    Calculate the magnitude (length) of a vector.

    Args:
        v: Vector as a list [x, y]

    Returns:
        The magnitude as a float

    TODO: Implement this function using math.sqrt()
    """
    # Your code here
    pass

def unit_vector(v):
    """
    Create a unit vector from the given vector.

    Args:
        v: Vector as a list [x, y]

    Returns:
        Unit vector as a list [x, y]

    TODO: Implement this function
    Hint: Divide each component by the magnitude
    """
    # Your code here
    pass
```

```python exec
id: 06-linear-algebra-fundamentals-16
# Test magnitude and unit vector
v = [3, 4]
mag = vector_magnitude(v)
unit = unit_vector(v)
unit_mag = vector_magnitude(unit)

print(f"Vector: {v}")
print(f"Magnitude: {mag}")
print(f"Unit vector: {unit}")
print(f"Magnitude of unit vector: {unit_mag}")
```

```python exec
id: 06-linear-algebra-fundamentals-17
# Visualize a vector and its unit vector
v = [6, 8]
unit = unit_vector(v)

plot_vectors([v, unit],
             colors=['blue', 'red'],
             labels=[f'v (magnitude={vector_magnitude(v):.2f})',
                    f'unit(v) (magnitude={vector_magnitude(unit):.2f})'],
             title='Vector and Its Unit Vector')
```

## Part 4: Coordinate Systems and Standard Basis Vectors

In 2D space, we have two standard basis vectors:
- **i-hat** (or **e₁**): [1, 0] - points along the x-axis
- **j-hat** (or **e₂**): [0, 1] - points along the y-axis

Any 2D vector can be expressed as a combination of these basis vectors:
- [x, y] = x·[1, 0] + y·[0, 1]

```python exec
id: 06-linear-algebra-fundamentals-18
# Standard basis vectors
i_hat = [1, 0]
j_hat = [0, 1]

print(f"i-hat (x-axis unit vector): {i_hat}")
print(f"j-hat (y-axis unit vector): {j_hat}")

# Visualize basis vectors
plot_vectors([i_hat, j_hat],
             colors=['red', 'green'],
             labels=['i-hat', 'j-hat'],
             title='Standard Basis Vectors')
```

```python exec
id: 06-linear-algebra-fundamentals-19
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
def scalar_multiply(scalar, v):
    """
    Multiply a vector by a scalar.

    Args:
        scalar: A number to multiply by
        v: Vector as a list [x, y]

    Returns:
        Scaled vector as a list [x, y]

    TODO: Implement this function
    """
    # Your code here
    pass

# Express a vector as a combination of basis vectors
v = [3, 4]
v_from_basis = vector_add(scalar_multiply(v[0], i_hat),
                          scalar_multiply(v[1], j_hat))

print(f"Vector v = {v}")
print(f"v = {v[0]}·i-hat + {v[1]}·j-hat = {v_from_basis}")
```

## Part 5: Matrices and the Identity Matrix

A matrix is a 2D array of numbers. We'll represent matrices as lists of lists, where each inner list is a row.

### The Identity Matrix
The identity matrix is a special matrix that doesn't change a vector when multiplied:
```
I = [[1, 0],
     [0, 1]]
```

It's called "identity" because multiplying any vector by it returns the same vector.

```python exec
id: 06-linear-algebra-fundamentals-20
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
def create_identity_matrix(n = 2):
    """
    Create an n×n identity matrix.

    Args:
        n: Size of the matrix

    Returns:
        Identity matrix as a list of lists

    TODO: Implement this function
    Hint: The identity matrix has 1s on the diagonal and 0s elsewhere
    """
    # Your code here
    pass

# Create and display 2×2 identity matrix
I = create_identity_matrix(2)
print("2×2 Identity Matrix:")
for row in I:
    print(row)
```

## Part 6: Scaling Transformations

### Uniform Scaling (Scalar Multiplication)
Multiplying a vector by a scalar scales it uniformly in all directions.

### Non-uniform Scaling (Diagonal Matrix)
We can scale x and y independently using a diagonal matrix:
```
D = [[sx, 0 ],
     [0,  sy]]
```
where sx scales the x-component and sy scales the y-component.

```python exec
id: 06-linear-algebra-fundamentals-21
# Uniform scaling visualization
v = [2, 3]
v_scaled = scalar_multiply(2, v)

plot_vectors([v, v_scaled],
             colors=['blue', 'red'],
             labels=['v', '2·v'],
             title='Uniform Scaling (Scalar Multiplication)')
```

```python exec
id: 06-linear-algebra-fundamentals-22
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
def create_diagonal_matrix(diagonal_values):
    """
    Create a diagonal matrix from a list of diagonal values.

    Args:
        diagonal_values: List of values for the diagonal

    Returns:
        Diagonal matrix as a list of lists

    TODO: Implement this function
    Example: [2, 3] should create [[2, 0], [0, 3]]
    """
    # Your code here
    pass

# Create a scaling matrix
D = create_diagonal_matrix([2, 0.5])
print("Diagonal scaling matrix:")
for row in D:
    print(row)
```

## Part 7: Matrix-Vector Multiplication

To multiply a matrix by a vector, we take the dot product of each row of the matrix with the vector:

```
[[a, b],    [x]   [a·x + b·y]
 [c, d]]  × [y] = [c·x + d·y]
```

```python exec
id: 06-linear-algebra-fundamentals-23
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
def matrix_vector_multiply(matrix, vector):
    """
    Multiply a matrix by a vector.

    Args:
        matrix: Matrix as a list of lists (each inner list is a row)
        vector: Vector as a list [x, y]

    Returns:
        Result vector as a list

    TODO: Implement this function
    Hint: The result is a vector where each component is the dot product
          of the corresponding matrix row with the input vector
    """
    # Your code here
    pass

# Test with identity matrix
I = create_identity_matrix(2)
v = [3, 4]
result = matrix_vector_multiply(I, v)

print(f"Identity matrix × v = {result}")
print(f"Original vector v = {v}")
print(f"Are they the same? {result == v}")
```

```python exec
id: 06-linear-algebra-fundamentals-24
# Test with diagonal scaling matrix
D = create_diagonal_matrix([2, 3])
v = [1, 1]
v_scaled = matrix_vector_multiply(D, v)

print(f"Scaling matrix:")
for row in D:
    print(row)
print(f"\nOriginal vector: {v}")
print(f"Scaled vector: {v_scaled}")
```

```python exec
id: 06-linear-algebra-fundamentals-25
def visualize_transformation(matrix, test_vectors=None, title="Matrix Transformation"):
    """
    Visualize how a matrix transforms vectors.

    Args:
        matrix: 2×2 matrix as list of lists
        test_vectors: List of vectors to transform (if None, uses default set)
        title: Title for the plot
    """
    if test_vectors is None:
        test_vectors = [[1, 0], [0, 1], [1, 1], [2, 1]]

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

    colors = ['red', 'green', 'blue', 'orange', 'purple']

    # Plot original vectors
    max_val = 0
    for i, v in enumerate(test_vectors):
        ax1.arrow(0, 0, v[0], v[1],
                 head_width=0.2, head_length=0.15,
                 fc=colors[i % len(colors)], ec=colors[i % len(colors)],
                 linewidth=2, label=f'v{i+1}')
        max_val = max(max_val, abs(v[0]), abs(v[1]))

    # Plot transformed vectors
    for i, v in enumerate(test_vectors):
        v_transformed = matrix_vector_multiply(matrix, v)
        ax2.arrow(0, 0, v_transformed[0], v_transformed[1],
                 head_width=0.2, head_length=0.15,
                 fc=colors[i % len(colors)], ec=colors[i % len(colors)],
                 linewidth=2, label=f'v{i+1}\' ')
        max_val = max(max_val, abs(v_transformed[0]), abs(v_transformed[1]))

    # Set up both plots
    for ax, subtitle in zip([ax1, ax2], ['Original Vectors', 'Transformed Vectors']):
        ax.set_xlim(-max_val-1, max_val+1)
        ax.set_ylim(-max_val-1, max_val+1)
        ax.axhline(y=0, color='k', linewidth=0.5)
        ax.axvline(x=0, color='k', linewidth=0.5)
        ax.grid(True, alpha=0.3)
        ax.set_aspect('equal')
        ax.legend()
        ax.set_title(subtitle)
        ax.set_xlabel('x')
        ax.set_ylabel('y')

    fig.suptitle(title, fontsize=14, fontweight='bold')
    plt.tight_layout()
    plt.show()

# Visualize identity transformation
I = create_identity_matrix(2)
visualize_transformation(I, title="Identity Matrix (No Change)")

# Visualize scaling transformation
D = create_diagonal_matrix([2, 0.5])
visualize_transformation(D, title="Diagonal Scaling Matrix (x→2x, y→0.5y)")
```

## Part 8: Matrix-Matrix Multiplication

Finally, we can multiply two matrices together. The rule is:
- The element at row i, column j of the result is the dot product of row i from the first matrix and column j from the second matrix.

For 2×2 matrices:
```
[[a, b],   [[e, f],   [[a·e+b·g, a·f+b·h],
 [c, d]] ×  [g, h]] =  [c·e+d·g, c·f+d·h]]
```

```python exec
id: 06-linear-algebra-fundamentals-26
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
def get_column(matrix, col_index):
    """
    Extract a column from a matrix.

    Args:
        matrix: Matrix as a list of lists
        col_index: Index of the column to extract

    Returns:
        Column as a list

    TODO: Implement this function
    """
    # Your code here
    pass

def matrix_multiply(A, B):
    """
    Multiply two matrices.

    Args:
        A: First matrix as a list of lists
        B: Second matrix as a list of lists

    Returns:
        Result matrix as a list of lists

    TODO: Implement this function
    Hint: Result[i][j] = dot_product(row i of A, column j of B)
    """
    # Your code here
    pass
```

```python exec
id: 06-linear-algebra-fundamentals-27
# Test matrix multiplication
A = [[2, 3],
     [1, 4]]

B = [[1, 0],
     [0, 2]]

C = matrix_multiply(A, B)

print("Matrix A:")
for row in A:
    print(row)

print("\nMatrix B:")
for row in B:
    print(row)

print("\nA × B:")
for row in C:
    print(row)
```

```python exec
id: 06-linear-algebra-fundamentals-28
# Verify: Matrix × Identity = Matrix
I = create_identity_matrix(2)
result = matrix_multiply(A, I)

print("A × I:")
for row in result:
    print(row)

print("\nOriginal matrix A:")
for row in A:
    print(row)

print(f"\nAre they the same? {result == A}")
```

## Putting It All Together: Composite Transformations

One powerful aspect of matrix multiplication is that we can combine transformations by multiplying their matrices together!

```python exec
id: 06-linear-algebra-fundamentals-29
# Create two scaling matrices
scale_x = create_diagonal_matrix([2, 1])  # Scale x by 2
scale_y = create_diagonal_matrix([1, 3])  # Scale y by 3

# Combine them
combined = matrix_multiply(scale_y, scale_x)

print("Combined transformation matrix:")
for row in combined:
    print(row)

# Test on a vector
v = [1, 1]
v_result = matrix_vector_multiply(combined, v)

print(f"\nOriginal vector: {v}")
print(f"After combined transformation: {v_result}")

# Visualize
visualize_transformation(combined, title="Combined Scaling Transformation (x→2x, y→3y)")
```

## Summary and Next Steps


1. Vector addition and subtraction
2. Dot product
3. Vector magnitude and unit vectors
4. Coordinate systems and basis vectors
5. Identity matrix
6. Scalar and diagonal scaling
7. Matrix-vector multiplication
8. Matrix-matrix multiplication

### Try this Exercises

Try implementing these additional operations:
1. Rotation matrices
2. Reflection matrices
3. Shear transformations
4. Matrix transpose
5. Matrix inverse (for 2×2 matrices)

### Real-world Applications

These operations are fundamental to:
- Computer graphics and 3D rendering
- Machine learning and neural networks
- Physics simulations
- Data science and dimensionality reduction
- Image processing and computer vision

## What we set out to do

These were the aims of this notebook. Now that you have worked through it, they are a check on what happened rather than a promise about it.

1. Implement vector addition and subtraction
2. Understand and visualize the dot product
3. Work with unit vectors and coordinates
4. Create and use the identity matrix
5. Implement scalar and component-wise scaling
6. Build matrix multiplication from scratch

Let's begin!

## Looking back

Before leaving this page, a sentence on each. What you write stays on this device.

```reflect
- Something you expected before running a cell that turned out differently
- The one idea from this page you could explain to someone else now
- Something you would change or try next, if there were time
- A question this page raised for you that it did not answer. Bring it to the next session; these questions are where the next session starts.
```
