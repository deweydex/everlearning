---
title: "Gaussian Elimination: Building a Matrix Solver"
slug: 05-gaussian-elimination
course: ai-and-ml-foundations
course_title: "AI and ML Foundations"
series: 1-linear-algebra
series_title: "Linear Algebra"
version: 2026.09.06.1
---

# Gaussian Elimination: Building a Matrix Solver
## From Linear Equations to Row Operations


**The Journey:**
We'll build a complete matrix solver step by step, understanding each piece before combining them. By the end, you'll have a working implementation that solves any system of linear equations.

---
## Part 1: Understanding the Problem
### From Equations to Matrices

Consider this system of linear equations:

```
2x + 3y - z = 5
4x + 4y - 3z = 3  
-2x + 3y - z = 1
```

We can represent this as a matrix equation **Ax = b**:

```
⎡ 2   3  -1 ⎤   ⎡x⎤   ⎡ 5⎤
⎢ 4   4  -3 ⎥ × ⎢y⎥ = ⎢ 3⎥
⎣-2   3  -1 ⎦   ⎣z⎦   ⎣ 1⎦
```

We work with the **augmented matrix** [A|b]:

```
⎡ 2   3  -1 | 5⎤
⎢ 4   4  -3 | 3⎥
⎣-2   3  -1 | 1⎦
```

```python exec
id: 05-gaussian-elimination-1
import numpy as np

# Define the system
coefficient_matrix = np.array([
    [2.0,  3.0, -1.0],
    [4.0,  4.0, -3.0],
    [-2.0, 3.0, -1.0]
], dtype=float)

constants_vector = np.array([5.0, 3.0, 1.0], dtype=float)

# Create augmented matrix
def create_augmented_matrix(coefficient_matrix, constants_vector):
    """
    Combine coefficient matrix and constants vector into augmented matrix.

    Args:
        coefficient_matrix: n×n matrix of coefficients
        constants_vector: n×1 vector of constants

    Returns:
        n×(n+1) augmented matrix
    """
    # Reshape constants to column vector and concatenate
    constants_column = constants_vector.reshape(-1, 1)
    return np.column_stack((coefficient_matrix, constants_column))

augmented_matrix = create_augmented_matrix(coefficient_matrix, constants_vector)

print("Augmented matrix [A|b]:")
print(augmented_matrix)
print(f"Shape: {augmented_matrix.shape}")
```

### Your turn 1.1: Understanding Representation

```python exec
id: 05-gaussian-elimination-2
# Given this system of equations:
# x + 2y + 3z = 14
# 2x - y + z = 5
# 3x + y - z = 4

# 1. Create the coefficient matrix

# 2. Create the constants vector

# 3. Create the augmented matrix

# 4. Verify by checking that the dimensions are correct
```

---
## Part 2: Elementary Row Operations
### The Three Basic Operations

We can solve systems by performing three types of operations on rows:

1. **Row swapping**: Exchange two rows
2. **Row scaling**: Multiply a row by a non-zero constant
3. **Row addition**: Add a multiple of one row to another

These operations don't change the solution of the system!

### Operation 1: Row Swapping

```python exec
id: 05-gaussian-elimination-3
def swap_rows(matrix, row_index_1, row_index_2):
    """
    Swap two rows in a matrix.

    Args:
        matrix: The matrix to modify
        row_index_1: Index of first row
        row_index_2: Index of second row

    Returns:
        Modified matrix (modifies in place and returns)
    """
    matrix[row_index_1], matrix[row_index_2] = \
        matrix[row_index_2].copy(), matrix[row_index_1].copy()
    return matrix

# Example
test_matrix = np.array([
    [1.0, 2.0, 3.0],
    [4.0, 5.0, 6.0],
    [7.0, 8.0, 9.0]
])

print("Original:")
print(test_matrix)

swap_rows(test_matrix, 0, 2)
print("\nAfter swapping rows 0 and 2:")
print(test_matrix)
```

### Operation 2: Row Scaling

```python exec
id: 05-gaussian-elimination-4
def scale_row(matrix, row_index, scalar):
    """
    Multiply a row by a scalar.

    Args:
        matrix: The matrix to modify
        row_index: Index of row to scale
        scalar: Value to multiply by

    Returns:
        Modified matrix
    """
    if scalar == 0:
        raise ValueError("Cannot scale by zero")

    matrix[row_index] = matrix[row_index] * scalar
    return matrix

# Example
test_matrix = np.array([
    [2.0, 4.0, 6.0],
    [1.0, 3.0, 5.0],
    [3.0, 6.0, 9.0]
])

print("Original:")
print(test_matrix)

scale_row(test_matrix, 0, 0.5)
print("\nAfter scaling row 0 by 0.5:")
print(test_matrix)
```

### Operation 3: Row Addition (Combination)

```python exec
id: 05-gaussian-elimination-5
def add_scaled_row(matrix, target_row_index, source_row_index, scalar):
    """
    Add a scaled version of one row to another row.

    Operation: row[target] = row[target] + scalar * row[source]

    Args:
        matrix: The matrix to modify
        target_row_index: Row to be modified
        source_row_index: Row to scale and add
        scalar: Scaling factor

    Returns:
        Modified matrix
    """
    matrix[target_row_index] = \
        matrix[target_row_index] + scalar * matrix[source_row_index]
    return matrix

# Example
test_matrix = np.array([
    [1.0, 2.0, 3.0],
    [4.0, 5.0, 6.0],
    [7.0, 8.0, 9.0]
])

print("Original:")
print(test_matrix)

# Add -4 times row 0 to row 1
add_scaled_row(test_matrix, target_row_index=1, source_row_index=0, scalar=-4)
print("\nAfter: row[1] = row[1] - 4*row[0]")
print(test_matrix)
```

### Your turn 2.1: Practice Row Operations

```python exec
id: 05-gaussian-elimination-6
practice_matrix = np.array([
    [2.0, 4.0, 2.0, 8.0],
    [1.0, 3.0, 1.0, 5.0],
    [3.0, 1.0, 5.0, 11.0]
])

print("Starting matrix:")
print(practice_matrix)

# 1. Scale row 0 by 0.5 to make the leading entry 1

# 2. Add -1 times row 0 to row 1 to eliminate the first entry of row 1

# 3. Add -3 times row 0 to row 2 to eliminate the first entry of row 2

# 4. Verify that column 0 now has the pattern [1, 0, 0, ...]
```

---
## Part 3: Forward Elimination
### Converting to Upper Triangular Form

**Goal**: Transform the matrix into upper triangular form (also called row echelon form).

Upper triangular matrix has zeros below the main diagonal:
```
⎡ a  b  c | d⎤
⎢ 0  e  f | g⎥
⎣ 0  0  h | i⎦
```

We do this column by column, from left to right.

### Sub-function: Find Pivot

A **pivot** is a non-zero element we use to eliminate other entries in its column.

```python exec
id: 05-gaussian-elimination-7
def find_pivot_row(matrix, column_index, starting_row):
    """
    Find the row with the largest absolute value in a column (partial pivoting).

    Args:
        matrix: The matrix to search
        column_index: Which column to search in
        starting_row: Only consider rows from this index onward

    Returns:
        Index of row with largest absolute value, or None if all are zero
    """
    num_rows = matrix.shape[0]
    max_value = 0.0
    max_row_index = None

    for row_index in range(starting_row, num_rows):
        abs_value = abs(matrix[row_index, column_index])
        if abs_value > max_value:
            max_value = abs_value
            max_row_index = row_index

    return max_row_index if max_value > 1e-10 else None

# Example
test_matrix = np.array([
    [1.0, 2.0, 3.0],
    [0.0, 4.0, 5.0],
    [0.0, -6.0, 7.0]
])

print("Matrix:")
print(test_matrix)

pivot_row = find_pivot_row(test_matrix, column_index=1, starting_row=1)
print(f"\nLargest pivot in column 1 (from row 1 onward): row {pivot_row}")
print(f"Value: {test_matrix[pivot_row, 1]}")
```

### Sub-function: Eliminate Column Below Pivot

```python exec
id: 05-gaussian-elimination-8
def eliminate_below_pivot(matrix, pivot_row, pivot_column):
    """
    Eliminate all entries below the pivot in a column.

    Args:
        matrix: The matrix to modify
        pivot_row: Row index of pivot
        pivot_column: Column index of pivot

    Returns:
        Modified matrix
    """
    num_rows = matrix.shape[0]
    pivot_value = matrix[pivot_row, pivot_column]

    if abs(pivot_value) < 1e-10:
        raise ValueError(f"Pivot at ({pivot_row}, {pivot_column}) is too small")

    # For each row below the pivot
    for row_index in range(pivot_row + 1, num_rows):
        # Calculate the multiplier needed to eliminate this entry
        multiplier = -matrix[row_index, pivot_column] / pivot_value

        # Add scaled pivot row to current row
        add_scaled_row(matrix,
                      target_row_index=row_index,
                      source_row_index=pivot_row,
                      scalar=multiplier)

    return matrix

# Example
test_matrix = np.array([
    [2.0, 4.0, 2.0],
    [1.0, 3.0, 1.0],
    [3.0, 1.0, 5.0]
])

print("Before elimination:")
print(test_matrix)

eliminate_below_pivot(test_matrix, pivot_row=0, pivot_column=0)
print("\nAfter eliminating column 0 below pivot:")
print(test_matrix)
```

### Complete Forward Elimination

```python exec
id: 05-gaussian-elimination-9
def forward_elimination(matrix):
    """
    Perform forward elimination to convert matrix to upper triangular form.

    Args:
        matrix: Augmented matrix to transform

    Returns:
        Upper triangular matrix
    """
    num_rows, num_cols = matrix.shape
    matrix = matrix.copy()  # Don't modify original

    # Process each column
    for current_column in range(min(num_rows, num_cols - 1)):
        # Find the best pivot in this column
        pivot_row = find_pivot_row(matrix, current_column, current_column)

        if pivot_row is None:
            print(f"Warning: No pivot found in column {current_column}")
            continue

        # Swap pivot row to current position if needed
        if pivot_row != current_column:
            swap_rows(matrix, current_column, pivot_row)
            print(f"Swapped row {current_column} with row {pivot_row}")

        # Eliminate all entries below the pivot
        eliminate_below_pivot(matrix, current_column, current_column)

        print(f"\nAfter eliminating column {current_column}:")
        print(matrix)
        print()

    return matrix

# Test with our original system
test_augmented = np.array([
    [2.0,  3.0, -1.0, 5.0],
    [4.0,  4.0, -3.0, 3.0],
    [-2.0, 3.0, -1.0, 1.0]
])

print("Starting matrix:")
print(test_augmented)
print()

upper_triangular = forward_elimination(test_augmented)
print("\nFinal upper triangular form:")
print(upper_triangular)
```

### Your turn 3.1: Forward Elimination Practice

```python exec
id: 05-gaussian-elimination-10
# Perform forward elimination on this system:
# x + 2y + z = 4
# 3x + 8y + 7z = 20
# 2x + 7y + 9z = 23

exercise_matrix = np.array([
    [1.0, 2.0, 1.0, 4.0],
    [3.0, 8.0, 7.0, 20.0],
    [2.0, 7.0, 9.0, 23.0]
])

# Apply forward elimination

# Verify the result is upper triangular
```

---
## Part 4: Back Substitution
### Solving from Bottom to Top

Once we have an upper triangular matrix, we can solve for variables starting from the bottom row.

Example:
```
⎡1  2  3 | 14⎤    →  x + 2y + 3z = 14
⎢0  1  2 |  8⎥    →      y + 2z = 8
⎣0  0  1 |  3⎦    →          z = 3
```

Start with z=3, then substitute back to find y, then x.

```python exec
id: 05-gaussian-elimination-11
def back_substitution(upper_triangular_matrix):
    """
    Solve an upper triangular system using back substitution.

    Args:
        upper_triangular_matrix: Upper triangular augmented matrix

    Returns:
        Solution vector
    """
    num_rows, num_cols = upper_triangular_matrix.shape
    num_variables = num_cols - 1  # Last column is constants

    if num_rows != num_variables:
        raise ValueError("Matrix must be square (excluding augmented column)")

    # Initialize solution vector
    solution = np.zeros(num_variables)

    # Start from bottom row and work upward
    for row_index in range(num_variables - 1, -1, -1):
        # Get the constant term from the last column
        right_hand_side = upper_triangular_matrix[row_index, -1]

        # Subtract the contributions from already-solved variables
        for col_index in range(row_index + 1, num_variables):
            right_hand_side -= \
                upper_triangular_matrix[row_index, col_index] * solution[col_index]

        # Divide by the coefficient of the current variable
        diagonal_element = upper_triangular_matrix[row_index, row_index]

        if abs(diagonal_element) < 1e-10:
            raise ValueError(f"Zero or near-zero diagonal at row {row_index}")

        solution[row_index] = right_hand_side / diagonal_element

    return solution

# Example
upper_triangular_example = np.array([
    [1.0, 2.0, 3.0, 14.0],
    [0.0, 1.0, 2.0, 8.0],
    [0.0, 0.0, 1.0, 3.0]
])

print("Upper triangular system:")
print(upper_triangular_example)

solution = back_substitution(upper_triangular_example)
print(f"\nSolution: x={solution[0]:.2f}, y={solution[1]:.2f}, z={solution[2]:.2f}")

# Verify solution
print("\nVerification:")
print(f"x + 2y + 3z = {solution[0] + 2*solution[1] + 3*solution[2]:.2f} (should be 14)")
print(f"y + 2z = {solution[1] + 2*solution[2]:.2f} (should be 8)")
print(f"z = {solution[2]:.2f} (should be 3)")
```

### Your turn 4.1: Back Substitution Practice

```python exec
id: 05-gaussian-elimination-12
# Solve this upper triangular system by hand, then verify with code:
# 2x + 3y - z = 7
#      4y + 2z = 18
#           3z = 9

practice_upper = np.array([
    [2.0, 3.0, -1.0, 7.0],
    [0.0, 4.0, 2.0, 18.0],
    [0.0, 0.0, 3.0, 9.0]
])

# 1. Solve by hand
# z = ?
# y = ?
# x = ?

# 2. Verify with back_substitution function

# 3. Check your solution by substituting back into original equations
```

---
## Part 5: The Complete Gaussian Elimination Solver
### Putting It All Together

```python exec
id: 05-gaussian-elimination-13
def gaussian_elimination_solve(coefficient_matrix, constants_vector, verbose=True):
    """
    Solve a system of linear equations using Gaussian elimination.

    Args:
        coefficient_matrix: n×n matrix of coefficients
        constants_vector: n×1 vector of constants
        verbose: If True, print steps

    Returns:
        Solution vector
    """
    if verbose:
        print("=" * 60)
        print("GAUSSIAN ELIMINATION SOLVER")
        print("=" * 60)

    # Step 1: Create augmented matrix
    if verbose:
        print("\nStep 1: Create augmented matrix [A|b]")

    augmented = create_augmented_matrix(coefficient_matrix, constants_vector)

    if verbose:
        print(augmented)

    # Step 2: Forward elimination
    if verbose:
        print("\n" + "=" * 60)
        print("Step 2: Forward elimination (convert to upper triangular)")
        print("=" * 60)

    upper_triangular = forward_elimination(augmented) if verbose else \
        forward_elimination_quiet(augmented)

    # Step 3: Back substitution
    if verbose:
        print("\n" + "=" * 60)
        print("Step 3: Back substitution")
        print("=" * 60)

    solution = back_substitution(upper_triangular)

    if verbose:
        print("\nSolution found:")
        for i, value in enumerate(solution):
            print(f"x{i} = {value:.6f}")

    # Step 4: Verification
    if verbose:
        print("\n" + "=" * 60)
        print("Step 4: Verification")
        print("=" * 60)

        computed_constants = coefficient_matrix @ solution
        print("\nOriginal constants vs Computed (Ax):")
        for i in range(len(constants_vector)):
            print(f"Row {i}: {constants_vector[i]:.6f} vs {computed_constants[i]:.6f}")

        residual = np.linalg.norm(computed_constants - constants_vector)
        print(f"\nResidual (error): {residual:.2e}")

        if residual < 1e-6:
            print("✓ Solution verified!")
        else:
            print("⚠ Warning: Large residual")

    return solution

def forward_elimination_quiet(matrix):
    """Forward elimination without printing steps."""
    num_rows, num_cols = matrix.shape
    matrix = matrix.copy()

    for current_column in range(min(num_rows, num_cols - 1)):
        pivot_row = find_pivot_row(matrix, current_column, current_column)
        if pivot_row is None:
            continue
        if pivot_row != current_column:
            swap_rows(matrix, current_column, pivot_row)
        eliminate_below_pivot(matrix, current_column, current_column)

    return matrix
```

### Test the Complete Solver

```python exec
id: 05-gaussian-elimination-14
# Test system 1: Our original example
A1 = np.array([
    [2.0,  3.0, -1.0],
    [4.0,  4.0, -3.0],
    [-2.0, 3.0, -1.0]
])
b1 = np.array([5.0, 3.0, 1.0])

solution1 = gaussian_elimination_solve(A1, b1, verbose=True)
```

```python exec
id: 05-gaussian-elimination-15
# Test system 2: A different example
A2 = np.array([
    [1.0, 2.0, 3.0],
    [2.0, -1.0, 1.0],
    [3.0, 0.0, -1.0]
])
b2 = np.array([9.0, 8.0, 3.0])

solution2 = gaussian_elimination_solve(A2, b2, verbose=True)
```

### Your turn 5.1: Solve Your Own Systems

```python exec
id: 05-gaussian-elimination-16
# 1. Solve this system:
# 3x + 2y - z = 1
# 2x - 2y + 4z = -2
# -x + 0.5y - z = 0

# 2. Create a random 4×4 system and solve it
# Hint: Use np.random.rand() or np.random.randn()

# 3. Compare your solver's results with numpy's built-in: np.linalg.solve()
```

---
## Part 6: Handling Special Cases
### What Can Go Wrong?

### Case 1: No Unique Solution (Inconsistent System)

```python exec
id: 05-gaussian-elimination-17
# This system has no solution:
# x + y = 2
# x + y = 3  (contradicts first equation!)

A_inconsistent = np.array([
    [1.0, 1.0],
    [1.0, 1.0]
])
b_inconsistent = np.array([2.0, 3.0])

try:
    solution = gaussian_elimination_solve(A_inconsistent, b_inconsistent, verbose=False)
except Exception as e:
    print(f"Error: {e}")
    print("\nThis system is inconsistent - no solution exists.")
```

### Case 2: Infinitely Many Solutions (Dependent Equations)

```python exec
id: 05-gaussian-elimination-18
# This system has infinitely many solutions:
# x + y = 2
# 2x + 2y = 4  (same as first equation!)

A_dependent = np.array([
    [1.0, 1.0],
    [2.0, 2.0]
])
b_dependent = np.array([2.0, 4.0])

try:
    solution = gaussian_elimination_solve(A_dependent, b_dependent, verbose=False)
except Exception as e:
    print(f"Error: {e}")
    print("\nThis system has infinitely many solutions.")
```

### Case 3: Ill-Conditioned Matrices

```python exec
id: 05-gaussian-elimination-19
# Hilbert matrix is notoriously ill-conditioned
def create_hilbert_matrix(size):
    """Create a Hilbert matrix - very ill-conditioned!"""
    return np.array([[1.0 / (i + j + 1) for j in range(size)] for i in range(size)])

n = 5
A_hilbert = create_hilbert_matrix(n)
b_hilbert = np.ones(n)  # All ones

print("Solving ill-conditioned Hilbert system:")
print("Hilbert matrix:")
print(A_hilbert)

solution_mine = gaussian_elimination_solve(A_hilbert, b_hilbert, verbose=False)
solution_numpy = np.linalg.solve(A_hilbert, b_hilbert)

print("\nOur solution:")
print(solution_mine)
print("\nNumPy's solution:")
print(solution_numpy)
print("\nDifference:")
print(solution_mine - solution_numpy)

# Check condition number
condition_number = np.linalg.cond(A_hilbert)
print(f"\nCondition number: {condition_number:.2e}")
print("(Higher = worse conditioning, expect numerical errors)")
```

### Improved Solver with Error Handling

```python exec
id: 05-gaussian-elimination-20
def robust_gaussian_elimination(coefficient_matrix, constants_vector,
                               tolerance=1e-10, verbose=False):
    """
    Robust Gaussian elimination with better error handling.

    Args:
        coefficient_matrix: n×n matrix
        constants_vector: n×1 vector
        tolerance: Threshold for considering values as zero
        verbose: Print detailed information

    Returns:
        solution vector or None if no unique solution
    """
    augmented = create_augmented_matrix(coefficient_matrix, constants_vector)
    num_rows, num_cols = augmented.shape

    # Forward elimination
    for col in range(min(num_rows, num_cols - 1)):
        # Find pivot
        pivot_row = find_pivot_row(augmented, col, col)

        if pivot_row is None:
            if verbose:
                print(f"No pivot in column {col} - system may be singular")

            # Check if system is inconsistent
            for row in range(col, num_rows):
                if abs(augmented[row, -1]) > tolerance:
                    if verbose:
                        print("System is inconsistent - no solution")
                    return None

            if verbose:
                print("System has infinitely many solutions")
            return None

        if pivot_row != col:
            swap_rows(augmented, col, pivot_row)

        eliminate_below_pivot(augmented, col, col)

    # Check for zero on diagonal
    for i in range(num_rows):
        if abs(augmented[i, i]) < tolerance:
            if verbose:
                print(f"Zero on diagonal at row {i}")
            return None

    # Back substitution
    try:
        solution = back_substitution(augmented)
        return solution
    except Exception as e:
        if verbose:
            print(f"Error in back substitution: {e}")
        return None

# Test with various cases
print("Test 1: Normal system")
A = np.array([[2.0, 1.0], [1.0, 3.0]])
b = np.array([5.0, 7.0])
sol = robust_gaussian_elimination(A, b, verbose=True)
print(f"Solution: {sol}\n")

print("Test 2: Singular system")
A = np.array([[1.0, 2.0], [2.0, 4.0]])
b = np.array([3.0, 6.0])
sol = robust_gaussian_elimination(A, b, verbose=True)
print(f"Solution: {sol}\n")
```

---
## Part 7: Applications and Extensions

### Application 1: Polynomial Interpolation

```python exec
id: 05-gaussian-elimination-21
def polynomial_interpolation(x_points, y_points):
    """
    Find polynomial coefficients that pass through given points.

    For n points, finds polynomial of degree n-1:
    p(x) = a₀ + a₁x + a₂x² + ... + aₙ₋₁xⁿ⁻¹
    """
    n = len(x_points)

    # Build Vandermonde matrix
    vandermonde = np.array([[x**power for power in range(n)]
                           for x in x_points])

    # Solve for coefficients
    coefficients = gaussian_elimination_solve(vandermonde, y_points, verbose=False)

    return coefficients

# Example: fit polynomial through points
x_data = np.array([0.0, 1.0, 2.0, 3.0])
y_data = np.array([1.0, 3.0, 7.0, 13.0])

coeffs = polynomial_interpolation(x_data, y_data)

print("Points to fit:")
for x, y in zip(x_data, y_data):
    print(f"  ({x}, {y})")

print(f"\nPolynomial coefficients: {coeffs}")
print(f"p(x) = {coeffs[0]:.3f} + {coeffs[1]:.3f}x + {coeffs[2]:.3f}x² + {coeffs[3]:.3f}x³")

# Verify
print("\nVerification:")
for x, y_true in zip(x_data, y_data):
    y_pred = sum(coeffs[i] * x**i for i in range(len(coeffs)))
    print(f"p({x}) = {y_pred:.6f}, actual = {y_true:.6f}")
```

### Application 2: Electrical Circuit Analysis

```python exec
id: 05-gaussian-elimination-22
# Circuit with resistors and voltage sources
# Using Kirchhoff's laws leads to system of equations

print("Circuit Analysis Example:")
print("Three-loop circuit with resistors and voltage sources")
print()

# System represents: Resistance matrix × Current vector = Voltage vector
resistance_matrix = np.array([
    [10.0, -5.0,  0.0],  # Loop 1
    [-5.0, 15.0, -8.0],  # Loop 2
    [0.0,  -8.0, 18.0]   # Loop 3
])

voltage_vector = np.array([12.0, 0.0, 6.0])  # Voltage sources

print("Solving for currents...")
currents = gaussian_elimination_solve(resistance_matrix, voltage_vector, verbose=False)

print("\nLoop currents (Amperes):")
for i, current in enumerate(currents):
    print(f"Loop {i+1}: {current:.4f} A")
```

### Your turn 7.1: Final Challenges

```python exec
id: 05-gaussian-elimination-23
# Challenge 1: Solve a 5×5 random system

# Challenge 2: Implement matrix inversion using Gaussian elimination
# Hint: Solve AX = I where I is the identity matrix

# Challenge 3: Solve a system with complex numbers

# Challenge 4: Implement LU decomposition (factor A = LU)

# Challenge 5: Calculate the determinant using Gaussian elimination
# Hint: Product of diagonal elements after elimination
```

---
## Summary

**What You've Built:**
- Complete understanding of Gaussian elimination
- Modular functions for each operation:
  - Row swapping, scaling, addition
  - Pivot finding
  - Forward elimination
  - Back substitution
- A working matrix solver
- Error handling for special cases
- Real-world applications

**Key Concepts:**
- Linear systems ↔ Matrix equations
- Elementary row operations preserve solutions
- Upper triangular form enables easy solving
- Pivoting improves numerical stability
- Not all systems have unique solutions

**Extensions to Explore:**
- LU decomposition
- Cholesky decomposition (for symmetric positive definite matrices)
- QR decomposition
- Iterative methods (Jacobi, Gauss-Seidel)
- Sparse matrix solvers
- Least squares and overdetermined systems

**Performance Notes:**
- Time complexity: O(n³) for n×n systems
- Space complexity: O(n²)
- Numerical stability critical for large systems
- Partial pivoting usually sufficient
- Full pivoting more stable but slower

You now have the tools to solve any system of linear equations!

## What we set out to do

These were the aims of this notebook. Now that you have worked through it, they are a check on what happened rather than a promise about it.

- Understand systems of linear equations
- Learn how matrices represent equation systems
- Master elementary row operations
- Build sub-functions for each transformation
- Construct a complete Gaussian elimination solver
- Handle edge cases and special matrices

## Looking back

Before leaving this page, a sentence on each. What you write stays on this device.

```reflect
- Something you expected before running a cell that turned out differently
- The one idea from this page you could explain to someone else now
- Something you would change or try next, if there were time
- A question this page raised for you that it did not answer. Bring it to the next session; these questions are where the next session starts.
```
