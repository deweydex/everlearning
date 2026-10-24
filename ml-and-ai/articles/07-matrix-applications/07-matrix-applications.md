---
title: "The Hidden Power of 2×2 Matrices"
slug: 07-matrix-applications
course: ai-and-ml-foundations
course_title: "AI and ML Foundations"
series: 1-linear-algebra
series_title: "Linear Algebra"
version: 2026.09.06.1
---

# The Hidden Power of 2×2 Matrices

In this notebook, we'll discover how 2×2 matrices can represent some surprising mathematical concepts:

1. **The Fibonacci Sequence** - A recursive sequence that appears throughout nature
2. **Complex Numbers and √(-1)** - How matrices can represent imaginary numbers
3. **Markov Chains** - A model for predicting probabilistic systems

## Prerequisites

This notebook builds on the functions we created in the Linear Algebra Fundamentals notebook. We'll import those key functions here.

```python exec
id: 07-matrix-applications-1
import matplotlib.pyplot as plt
import math

# Set up plotting style
plt.style.use('default')

```

## Core Functions from Previous Notebook

Let's implement the key functions we'll need:

```python exec
id: 07-matrix-applications-2
def matrix_multiply(A, B):
    """
    Multiply two 2×2 matrices.
    Result[i][j] = dot product of row i of A with column j of B
    """
    result = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            result[i][j] = A[i][0] * B[0][j] + A[i][1] * B[1][j]
    return result

def matrix_vector_multiply(matrix, vector):
    """
    Multiply a 2×2 matrix by a 2D vector.
    """
    result = [0, 0]
    for i in range(2):
        result[i] = matrix[i][0] * vector[0] + matrix[i][1] * vector[1]
    return result

def matrix_power(M, n):
    """
    Raise a matrix to the power n.

    Args:
        M: A 2×2 matrix
        n: The power (positive integer)

    Returns:
        M^n as a 2×2 matrix
    """
    if n == 0:
        return [[1, 0], [0, 1]]  # Identity matrix

    result = [[1, 0], [0, 1]]  # Start with identity
    for _ in range(n):
        result = matrix_multiply(result, M)
    return result

def print_matrix(M, name="Matrix"):
    """
    Pretty print a matrix.
    """
    print(f"{name}:")
    for row in M:
        print(f"  {row}")
```

---

## Part 1: The Fibonacci Sequence

## What is the Fibonacci Sequence?

The Fibonacci sequence is one of the most famous sequences in mathematics:
```
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
```

Each number is the sum of the previous two:
- F(0) = 0
- F(1) = 1
- F(n) = F(n-1) + F(n-2)

This sequence appears everywhere in nature: spiral patterns in shells, flower petals, pinecones, and even galaxy formations!

## The Fibonacci Matrix

Here's the magic: we can compute Fibonacci numbers using matrix multiplication!

Consider this special matrix:
```
F = [[1, 1],
     [1, 0]]
```

When we multiply it by the vector [F(n), F(n-1)], we get [F(n+1), F(n)]!

```python exec
id: 07-matrix-applications-3
# The Fibonacci matrix
F = [[1, 1],
     [1, 0]]

print_matrix(F, "Fibonacci Matrix")
```

```python exec
id: 07-matrix-applications-4
# Let's verify this works!
# Start with [F(1), F(0)] = [1, 0]

state = [1, 0]  # [F(1), F(0)]
print(f"Start: F(1)={state[0]}, F(0)={state[1]}")

# Multiply by F to get the next Fibonacci numbers
for i in range(10):
    state = matrix_vector_multiply(F, state)
    print(f"Step {i+1}: F({i+2})={state[0]}, F({i+1})={state[1]}")
```

### Your turn 1: Implement Fibonacci Using Matrix Powers


When we compute F^n, the top-left element is F(n+1), and the bottom-left element is F(n).

```python exec
id: 07-matrix-applications-5
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
def fibonacci_matrix(n):
    """
    Calculate the nth Fibonacci number using matrix exponentiation.

    Args:
        n: The index in the Fibonacci sequence

    Returns:
        The nth Fibonacci number

    TODO: Implement this function using matrix_power

    """
    if n == 0:
        return 0

    # Your code here
    pass

# Test your implementation
print("Fibonacci numbers using matrices:")
for i in range(15):
    print(f"F({i}) = {fibonacci_matrix(i)}")
```

```python exec
id: 07-matrix-applications-6
# Let's visualize F^n for different values of n
print("\nFibonacci Matrix Powers:\n")

for n in [1, 2, 3, 5, 8]:
    F_n = matrix_power(F, n)
    print_matrix(F_n, f"F^{n}")
    print(f"  F({n}) = {F_n[1][0]}, F({n+1}) = {F_n[0][0]}")
    print()
```

### Why Does This Work?

The Fibonacci matrix encodes the recurrence relation:

```
[[1, 1],        [[F(n)  ],   [[F(n) + F(n-1)],   [[F(n+1)],
 [1, 0]] \cdot  [F(n-1)]] =  [F(n) + 0     ]] =  [F(n)  ]]
```

Each multiplication advances the sequence by one step!

```python exec
id: 07-matrix-applications-7
# Visualize the growth of Fibonacci numbers
fib_numbers = [fibonacci_matrix(i) for i in range(15)]

plt.figure(figsize=(10, 6))
plt.plot(fib_numbers, 'bo-', linewidth=2, markersize=8)
plt.xlabel('n', fontsize=12)
plt.ylabel('F(n)', fontsize=12)
plt.title('Fibonacci Sequence Growth', fontsize=14, fontweight='bold')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

# Show the ratio between consecutive Fibonacci numbers (approaches golden ratio)
ratios = [fib_numbers[i+1] / fib_numbers[i] for i in range(1, len(fib_numbers)-1)]
golden_ratio = (1 + math.sqrt(5)) / 2

plt.figure(figsize=(10, 6))
plt.plot(ratios, 'ro-', linewidth=2, markersize=8, label='F(n+1) / F(n)')
plt.axhline(y=golden_ratio, color='g', linestyle='--', linewidth=2, label=f'Golden Ratio φ = {golden_ratio:.6f}')
plt.xlabel('n', fontsize=12)
plt.ylabel('Ratio', fontsize=12)
plt.title('Fibonacci Ratios Converge to the Golden Ratio', fontsize=14, fontweight='bold')
plt.legend(fontsize=11)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
```

---

## Part 2: Complex Numbers and √(-1) as Matrices

## What are Complex Numbers?

Complex numbers extend the real numbers by adding **i**, where i² = -1.

A complex number looks like: **a + bi** where a and b are real numbers.
- **a** is the "real part"
- **b** is the "imaginary part"

## The Shocking Truth: i is Just a Matrix!

We can represent any complex number **a + bi** as a 2×2 matrix:

```
a + bi  →  [[a, -b],
            [b,  a]]
```

In particular, **i** (the square root of -1) is:

```
i = [[0, -1],
     [1,  0]]
```

Let's verify that i² = -1!

```python exec
id: 07-matrix-applications-8
# Define i as a matrix
i_matrix = [[0, -1],
            [1,  0]]

print_matrix(i_matrix, "i (imaginary unit)")

# Compute i²
i_squared = matrix_multiply(i_matrix, i_matrix)

print("\ni² = i × i =")
print_matrix(i_squared, "i²")

# This should be -1 in matrix form: [[-1, 0], [0, -1]]
negative_one = [[-1, 0],
                [0, -1]]

print("\nExpected -1 (as a matrix):")
print_matrix(negative_one, "-1")

print(f"\nDoes i² = -1? {i_squared == negative_one}")
```

### Your turn 2: Implement Complex Number Operations

Let's create functions to work with complex numbers as matrices!

```python exec
id: 07-matrix-applications-9
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
def complex_to_matrix(a, b):
    """
    Convert a complex number a + bi to its matrix representation.

    Args:
        a: Real part
        b: Imaginary part

    Returns:
        2×2 matrix representing a + bi

    TODO: Implement this function
    The matrix should be [[a, -b], [b, a]]
    """
    # Your code here
    pass

def matrix_to_complex(M):
    """
    Convert a matrix back to a complex number a + bi.

    Args:
        M: 2×2 matrix representing a complex number

    Returns:
        Tuple (a, b) representing a + bi

    TODO: Implement this function
    Hint: a is M[0][0] and b is M[1][0]
    """
    # Your code here
    pass

# Test your functions
z1 = complex_to_matrix(3, 4)  # 3 + 4i
print_matrix(z1, "3 + 4i")

a, b = matrix_to_complex(z1)
print(f"\nConverted back: {a} + {b}i")
```

```python exec
id: 07-matrix-applications-10
# Complex multiplication using matrices!
# (a + bi) × (c + di) = (ac - bd) + (ad + bc)i

z1 = complex_to_matrix(2, 3)   # 2 + 3i
z2 = complex_to_matrix(1, 4)   # 1 + 4i

product = matrix_multiply(z1, z2)

print_matrix(z1, "z1 = 2 + 3i")
print()
print_matrix(z2, "z2 = 1 + 4i")
print()
print_matrix(product, "z1 × z2")

a, b = matrix_to_complex(product)
print(f"\nResult: {a} + {b}i")

# Verify: (2 + 3i)(1 + 4i) = 2 + 8i + 3i + 12i² = 2 + 11i - 12 = -10 + 11i
print(f"Expected: -10 + 11i")
```

### What Does the i Matrix Represent Geometrically?

The matrix for i is actually a **90-degree counterclockwise rotation**!

```python exec
id: 07-matrix-applications-11
def plot_complex_multiplication(a, b, steps=4):
    """
    Visualize multiplying by a complex number repeatedly.
    """
    fig, ax = plt.subplots(figsize=(10, 10))

    # Start with the vector [1, 0]
    vector = [1, 0]
    z = complex_to_matrix(a, b)

    colors = ['red', 'blue', 'green', 'orange', 'purple', 'brown']

    for i in range(steps):
        # Plot current vector
        ax.arrow(0, 0, vector[0], vector[1],
                head_width=0.15, head_length=0.1,
                fc=colors[i % len(colors)], ec=colors[i % len(colors)],
                linewidth=2, label=f'Step {i}')

        # Multiply by the complex number
        vector = matrix_vector_multiply(z, vector)

    # Plot the final vector
    ax.arrow(0, 0, vector[0], vector[1],
            head_width=0.15, head_length=0.1,
            fc=colors[steps % len(colors)], ec=colors[steps % len(colors)],
            linewidth=2, label=f'Step {steps}')

    # Set up plot
    max_val = 3
    ax.set_xlim(-max_val, max_val)
    ax.set_ylim(-max_val, max_val)
    ax.axhline(y=0, color='k', linewidth=0.5)
    ax.axvline(x=0, color='k', linewidth=0.5)
    ax.grid(True, alpha=0.3)
    ax.set_aspect('equal')
    ax.legend()
    ax.set_title(f'Repeatedly Multiplying by {a} + {b}i', fontsize=14, fontweight='bold')
    ax.set_xlabel('Real axis', fontsize=12)
    ax.set_ylabel('Imaginary axis', fontsize=12)

    plt.tight_layout()
    plt.show()

# Multiply by i repeatedly (should rotate by 90° each time)
print("Multiplying by i (0 + 1i):")
plot_complex_multiplication(0, 1, steps=4)

# Try a different complex number
print("\nMultiplying by (0.8 + 0.6i):")
plot_complex_multiplication(0.8, 0.6, steps=8)
```

### Powers of i

One of the most famous patterns in mathematics:
- i⁰ = 1
- i¹ = i
- i² = -1
- i³ = -i
- i⁴ = 1 (the cycle repeats!)

Let's verify this using matrices!

```python exec
id: 07-matrix-applications-12
i_matrix = complex_to_matrix(0, 1)

print("Powers of i:\n")
for n in range(8):
    i_n = matrix_power(i_matrix, n)
    a, b = matrix_to_complex(i_n)

    # Format the output nicely
    if b == 0:
        result = f"{int(a)}"
    elif a == 0:
        if b == 1:
            result = "i"
        elif b == -1:
            result = "-i"
        else:
            result = f"{int(b)}i"
    else:
        result = f"{int(a)} + {int(b)}i"

    print(f"i^{n} = {result}")
```

---

## Part 3: Two-State Markov Chains

## What is a Markov Chain?

A Markov chain is a mathematical system that transitions from one state to another with certain probabilities. The key property: **the future depends only on the present, not the past**.

### Example: Weather Prediction

Imagine we're modeling weather with two states:
- **Sunny** (S)
- **Rainy** (R)

Based on historical data:
- If today is sunny, tomorrow has an 80% chance of being sunny and 20% chance of rain
- If today is rainy, tomorrow has a 40% chance of being sunny and 60% chance of rain

We can represent this with a **transition matrix**:

```
              To
         [Sunny, Rain]
From S  [[0.8,  0.2],
From R   [0.4,  0.6]]
```

Each row sums to 1 (probabilities must sum to 100%)!

```python exec
id: 07-matrix-applications-13
# Weather transition matrix
# Rows: current state [Sunny, Rainy]
# Columns: next state [Sunny, Rainy]
P = [[0.8, 0.2],   # If sunny today: 80% sunny, 20% rainy tomorrow
     [0.4, 0.6]]   # If rainy today: 40% sunny, 60% rainy tomorrow

print_matrix(P, "Weather Transition Matrix")
print("\nRows sum to 1 (100%):")
for i, row in enumerate(P):
    print(f"  State {i}: {sum(row)}")
```

### Your turn 3: Predicting Future States

If we know today's weather, we can predict tomorrow's weather using matrix-vector multiplication!

We represent the current state as a probability vector:
- [1, 0] means "definitely sunny"
- [0, 1] means "definitely rainy"
- [0.7, 0.3] means "70% chance sunny, 30% chance rainy"

```python exec
id: 07-matrix-applications-14
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
def predict_next_state(transition_matrix, current_state):
    """
    Predict the next state given current state and transition matrix.

    Args:
        transition_matrix: 2×2 matrix of transition probabilities
        current_state: Current probability distribution [p_state0, p_state1]

    Returns:
        Next state probability distribution

    TODO: Implement this using matrix_vector_multiply
    Hint: We need to multiply the TRANSPOSE of the matrix by the state vector,
          or equivalently, take dot products of columns with the state.
    """
    # Your code here
    # Hint: next_state[i] = sum(current_state[j] * transition_matrix[j][i] for j in range(2))
    pass

# Start with a sunny day
state = [1.0, 0.0]  # 100% sunny
print(f"Day 0: Sunny={state[0]:.2%}, Rainy={state[1]:.2%}")

# Predict next 7 days
for day in range(1, 8):
    state = predict_next_state(P, state)
    print(f"Day {day}: Sunny={state[0]:.2%}, Rainy={state[1]:.2%}")
```

### Steady State: Long-term Behavior

What happens if we keep applying the transition matrix many times? The probabilities converge to a **steady state** (also called stationary distribution)!

```python exec
id: 07-matrix-applications-15
def simulate_markov_chain(transition_matrix, initial_state, steps):
    """
    Simulate a Markov chain for multiple steps.

    Args:
        transition_matrix: 2×2 transition matrix
        initial_state: Starting probability distribution
        steps: Number of steps to simulate

    Returns:
        List of states at each time step
    """
    states = [initial_state]
    current_state = initial_state[:]

    for _ in range(steps):
        current_state = predict_next_state(transition_matrix, current_state)
        states.append(current_state[:])

    return states

# Simulate from different starting points
sunny_start = simulate_markov_chain(P, [1.0, 0.0], 50)
rainy_start = simulate_markov_chain(P, [0.0, 1.0], 50)
mixed_start = simulate_markov_chain(P, [0.5, 0.5], 50)

# Extract probabilities for plotting
sunny_probs_1 = [state[0] for state in sunny_start]
sunny_probs_2 = [state[0] for state in rainy_start]
sunny_probs_3 = [state[0] for state in mixed_start]

# Plot convergence
plt.figure(figsize=(12, 6))
plt.plot(sunny_probs_1, 'b-', linewidth=2, label='Starting: 100% Sunny')
plt.plot(sunny_probs_2, 'r-', linewidth=2, label='Starting: 100% Rainy')
plt.plot(sunny_probs_3, 'g-', linewidth=2, label='Starting: 50% Sunny')

# The steady state (can be computed analytically)
steady_state_sunny = 2/3  # 66.67%
plt.axhline(y=steady_state_sunny, color='k', linestyle='--', linewidth=2,
            label=f'Steady State: {steady_state_sunny:.2%} Sunny')

plt.xlabel('Days', fontsize=12)
plt.ylabel('Probability of Sunny Weather', fontsize=12)
plt.title('Markov Chain Convergence to Steady State', fontsize=14, fontweight='bold')
plt.legend(fontsize=11)
plt.grid(True, alpha=0.3)
plt.ylim(0, 1)
plt.tight_layout()
plt.show()

print(f"\nAfter 50 days:")
print(f"  Starting sunny: {sunny_probs_1[-1]:.4f} sunny")
print(f"  Starting rainy: {sunny_probs_2[-1]:.4f} sunny")
print(f"  Starting mixed: {sunny_probs_3[-1]:.4f} sunny")
print(f"\nAll converge to the steady state!")
```

### Your turn 4: Create Your Own Markov Chain

Let's model a different system: **Student Study Habits**

States:
- **Focused**: Student is studying attentively
- **Distracted**: Student is not focused on studying

Create your own transition matrix and analyze the system!

```python exec
id: 07-matrix-applications-16
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
def create_study_transition_matrix():
    """
    Create a transition matrix for studying behavior.

    TODO: Fill in realistic probabilities

    Example interpretation:
    - If focused: 70% chance to stay focused, 30% chance to get distracted
    - If distracted: 40% chance to refocus, 60% chance to stay distracted

    Returns:
        2×2 transition matrix
    """
    # Your code here
    # Remember: each row must sum to 1!
    pass

# Create and test your matrix
study_matrix = create_study_transition_matrix()
print_matrix(study_matrix, "Study Habits Transition Matrix")

# Verify rows sum to 1
print("\nRow sums (should be 1.0):")
for i, row in enumerate(study_matrix):
    print(f"  Row {i}: {sum(row)}")

# Simulate a study session starting focused
study_states = simulate_markov_chain(study_matrix, [1.0, 0.0], 30)

focused_probs = [state[0] for state in study_states]

plt.figure(figsize=(12, 6))
plt.plot(focused_probs, 'b-', linewidth=2, label='Probability of Being Focused')
plt.fill_between(range(len(focused_probs)), 0, focused_probs, alpha=0.3)
plt.xlabel('Minutes', fontsize=12)
plt.ylabel('Probability of Being Focused', fontsize=12)
plt.title('Study Session: Focus Over Time', fontsize=14, fontweight='bold')
plt.legend(fontsize=11)
plt.grid(True, alpha=0.3)
plt.ylim(0, 1)
plt.tight_layout()
plt.show()
```

### Computing the Steady State Analytically

The steady state π satisfies: π = P^T × π

This means π is an eigenvector of P^T with eigenvalue 1!

For a 2×2 matrix, we can solve this system directly:

```python exec
id: 07-matrix-applications-17
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
def compute_steady_state(transition_matrix):
    """
    Compute the steady state distribution of a 2-state Markov chain.

    The steady state satisfies:
    π₀ = π₀ * P[0][0] + π₁ * P[1][0]
    π₁ = π₀ * P[0][1] + π₁ * P[1][1]
    π₀ + π₁ = 1

    Args:
        transition_matrix: 2×2 transition matrix

    Returns:
        Steady state distribution [π₀, π₁]

    TODO: Implement this
    Hint: From π₀ + π₁ = 1, we get π₁ = 1 - π₀
          Substitute into the first equation and solve for π₀
    """
    P = transition_matrix

    # From the equation π₀ = π₀ * P[0][0] + π₁ * P[1][0]
    # and π₁ = 1 - π₀
    # we get: π₀ = π₀ * P[0][0] + (1 - π₀) * P[1][0]
    # Solving: π₀ * (1 - P[0][0] + P[1][0]) = P[1][0]

    # Your code here
    pass

# Test with weather matrix
steady = compute_steady_state(P)
print(f"Weather steady state:")
print(f"  Sunny: {steady[0]:.2%}")
print(f"  Rainy: {steady[1]:.2%}")

# Verify by simulation
simulated = simulate_markov_chain(P, [1.0, 0.0], 1000)
final_state = simulated[-1]
print(f"\nVerification (after 1000 steps):")
print(f"  Sunny: {final_state[0]:.2%}")
print(f"  Rainy: {final_state[1]:.2%}")
```

### Visualizing the Markov Chain as a Graph

Let's create a visual representation of our Markov chain:

```python exec
id: 07-matrix-applications-18
def plot_markov_chain(transition_matrix, state_names=['State 0', 'State 1']):
    """
    Create a visual diagram of a 2-state Markov chain.
    """
    fig, ax = plt.subplots(figsize=(10, 8))

    # State positions
    pos = {0: (0.2, 0.5), 1: (0.8, 0.5)}

    # Draw states as circles
    for state, (x, y) in pos.items():
        circle = plt.Circle((x, y), 0.1, color='lightblue', ec='black', linewidth=2)
        ax.add_patch(circle)
        ax.text(x, y, state_names[state], ha='center', va='center',
               fontsize=12, fontweight='bold')

    P = transition_matrix

    # Draw transition arrows
    # Self-loops (curved)
    for state in [0, 1]:
        x, y = pos[state]
        prob = P[state][state]
        if prob > 0:
            arc = plt.Circle((x, y + 0.15), 0.08, fill=False,
                           color='red', linewidth=2)
            ax.add_patch(arc)
            ax.annotate(f'{prob:.0%}', xy=(x, y + 0.24),
                       ha='center', fontsize=11, color='red', fontweight='bold')

    # Transitions between states
    # 0 -> 1 (top arrow)
    if P[0][1] > 0:
        ax.annotate('', xy=(0.7, 0.55), xytext=(0.3, 0.55),
                   arrowprops=dict(arrowstyle='->', lw=2, color='blue'))
        ax.text(0.5, 0.6, f'{P[0][1]:.0%}', ha='center',
               fontsize=11, color='blue', fontweight='bold')

    # 1 -> 0 (bottom arrow)
    if P[1][0] > 0:
        ax.annotate('', xy=(0.3, 0.45), xytext=(0.7, 0.45),
                   arrowprops=dict(arrowstyle='->', lw=2, color='green'))
        ax.text(0.5, 0.4, f'{P[1][0]:.0%}', ha='center',
               fontsize=11, color='green', fontweight='bold')

    ax.set_xlim(0, 1)
    ax.set_ylim(0.2, 0.8)
    ax.axis('off')
    ax.set_aspect('equal')
    plt.title('Markov Chain Transition Diagram', fontsize=14, fontweight='bold', pad=20)
    plt.tight_layout()
    plt.show()

# Visualize the weather Markov chain
plot_markov_chain(P, ['Sunny', 'Rainy'])
```

## Summary: The Power of 2×2 Matrices

In this notebook, we've seen how 2×2 matrices are far more than just grids of numbers:

### 1. Fibonacci Sequence
- A simple matrix [[1,1],[1,0]] encodes the entire Fibonacci sequence
- Matrix exponentiation gives us an efficient way to compute Fibonacci numbers
- The eigenvalues of this matrix are related to the golden ratio!

### 2. Complex Numbers
- Every complex number a + bi can be represented as a 2×2 matrix
- The "imaginary" number i is just a 90° rotation matrix
- Complex multiplication is matrix multiplication
- This shows that complex numbers are as "real" as real numbers!

### 3. Markov Chains
- Stochastic processes can be modeled with transition matrices
- Matrix-vector multiplication predicts future probabilities
- Systems converge to steady states (eigenvectors)
- Applications: weather prediction, page rank, text generation, finance, and more

### Key Insight

Matrices are not just computational tools—they are a **language for expressing transformations, relationships, and dynamics**. The same mathematical structure (2×2 matrices) can model wildly different phenomena!

### Next Steps

Explore these extensions:
1. **Eigenvalues and eigenvectors**: The "DNA" of matrices
2. **Matrix diagonalization**: Simplifying complex transformations
3. **Higher-dimensional Markov chains**: More than 2 states
4. **Rotation matrices**: 3D graphics and computer vision
5. **Principal Component Analysis (PCA)**: Data science applications

## Looking back

Before leaving this page, a sentence on each. What you write stays on this device.

```reflect
- Something you expected before running a cell that turned out differently
- The one idea from this page you could explain to someone else now
- Something you would change or try next, if there were time
- A question this page raised for you that it did not answer. Bring it to the next session; these questions are where the next session starts.
```
