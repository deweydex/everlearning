---
title: "02-neural-networks-complete-introduction-page-2 (2 of 2)"
slug: 02-neural-networks-complete-introduction-page-2
course: ai-and-ml-foundations
course_title: "AI and ML Foundations"
series: 5-neural-networks
series_title: "Neural Networks"
version: 2026.09.06.1
---

Before starting this page, run the cell below. It repeats the imports and definitions from the earlier pages that this page uses.

```python exec
id: 02-neural-networks-complete-introduction-page-2-setup
import numpy as np
import matplotlib.pyplot as plt

# Import the libraries we'll need
import numpy as np
import matplotlib.pyplot as plt

# Make our plots look nice
plt.style.use('seaborn-v0_8-darkgrid')

# Set random seed for reproducibility
np.random.seed(42)

print("Libraries imported successfully!")
print(f"NumPy version: {np.__version__}")

# Let's do a simple example by hand first
A = np.array([[1, 2],
              [3, 4]])

B = np.array([[5, 6],
              [7, 8]])

# Matrix multiplication using @
C = A @ B

print("A @ B:")
print(C)

# Let's verify the top-left element:
# C[0,0] = (1*5) + (2*7) = 5 + 14 = 19 ✓
print("\nVerification:")
print(f"Top-left element: (1*5) + (2*7) = {1*5 + 2*7}")

# Let's implement a simple neuron

def simple_neuron(inputs, weights, bias):
    """
    A simple neuron that computes a weighted sum

    Parameters:
    -----------
    inputs : array
        Input values
    weights : array
        Weight for each input
    bias : float
        Bias term

    Returns:
    --------
    output : float
        Weighted sum + bias
    """
    # Calculate weighted sum
    weighted_sum = np.dot(inputs, weights) + bias
    return weighted_sum

# Example
inputs = np.array([1.0, 2.0, 3.0])
weights = np.array([0.5, -0.3, 0.8])
bias = 1.0

output = simple_neuron(inputs, weights, bias)
print(f"Inputs: {inputs}")
print(f"Weights: {weights}")
print(f"Bias: {bias}")
print(f"Output: {output:.3f}")

# Let's verify by hand
manual = (1.0 * 0.5) + (2.0 * -0.3) + (3.0 * 0.8) + 1.0
print(f"\nManual calculation: {manual:.3f}")

# Implement activation functions

def sigmoid(x):
    """
    Sigmoid activation function
    Squashes values to range (0, 1)
    """
    return 1 / (1 + np.exp(-x))

def relu(x):
    """
    ReLU (Rectified Linear Unit) activation function
    Returns x if x > 0, else 0
    """
    return np.maximum(0, x)

def tanh(x):
    """
    Tanh activation function
    Squashes values to range (-1, 1)
    """
    return np.tanh(x)

# Visualize these functions
x = np.linspace(-5, 5, 100)

plt.figure(figsize=(15, 4))

plt.subplot(1, 3, 1)
plt.plot(x, sigmoid(x), 'b-', linewidth=2)
plt.grid(True, alpha=0.3)
plt.title('Sigmoid Function', fontsize=14, fontweight='bold')
plt.xlabel('Input (x)')
plt.ylabel('Output σ(x)')
plt.axhline(y=0, color='k', linestyle='--', alpha=0.3)
plt.axhline(y=1, color='k', linestyle='--', alpha=0.3)
plt.axvline(x=0, color='k', linestyle='--', alpha=0.3)

plt.subplot(1, 3, 2)
plt.plot(x, relu(x), 'r-', linewidth=2)
plt.grid(True, alpha=0.3)
plt.title('ReLU Function', fontsize=14, fontweight='bold')
plt.xlabel('Input (x)')
plt.ylabel('Output ReLU(x)')
plt.axhline(y=0, color='k', linestyle='--', alpha=0.3)
plt.axvline(x=0, color='k', linestyle='--', alpha=0.3)

plt.subplot(1, 3, 3)
plt.plot(x, tanh(x), 'g-', linewidth=2)
plt.grid(True, alpha=0.3)
plt.title('Tanh Function', fontsize=14, fontweight='bold')
plt.xlabel('Input (x)')
plt.ylabel('Output tanh(x)')
plt.axhline(y=0, color='k', linestyle='--', alpha=0.3)
plt.axhline(y=1, color='k', linestyle='--', alpha=0.3)
plt.axhline(y=-1, color='k', linestyle='--', alpha=0.3)
plt.axvline(x=0, color='k', linestyle='--', alpha=0.3)

plt.tight_layout()
plt.show()

def dense_layer(inputs, weights, biases, activation='relu'):
    """
    A fully-connected (dense) layer

    Parameters:
    -----------
    inputs : array of shape (n_samples, n_features)
        Input data
    weights : array of shape (n_features, n_neurons)
        Weight matrix
    biases : array of shape (n_neurons,)
        Bias vector
    activation : str
        Activation function to use

    Returns:
    --------
    output : array of shape (n_samples, n_neurons)
        Activated output
    """
    # Weighted sum
    z = inputs @ weights + biases

    # Apply activation
    if activation == 'sigmoid':
        return sigmoid(z)
    elif activation == 'relu':
        return relu(z)
    elif activation == 'tanh':
        return tanh(z)
    else:
        return z

# Example: 2 samples, 3 features each, 4 neurons in the layer
X = np.array([[1.0, 2.0, 3.0],
              [4.0, 5.0, 6.0]])

W = np.random.randn(3, 4) * 0.5  # Initialize with small random weights
b = np.zeros(4)  # Initialize biases to zero

output = dense_layer(X, W, b, activation='relu')

print(f"Input shape: {X.shape}")
print(f"Weight shape: {W.shape}")
print(f"Bias shape: {b.shape}")
print(f"Output shape: {output.shape}")
print(f"\nOutput:\n{output}")

def forward_pass(X, W1, b1, W2, b2, W3, b3):
    """
    Forward pass through a 3-layer network

    Returns all intermediate values (we'll need these later for backprop!)
    """
    # Layer 1
    Z1 = X @ W1 + b1
    A1 = relu(Z1)

    # Layer 2
    Z2 = A1 @ W2 + b2
    A2 = relu(Z2)

    # Layer 3 (output)
    Z3 = A2 @ W3 + b3
    A3 = sigmoid(Z3)

    # Store all values for later use
    cache = {
        'Z1': Z1, 'A1': A1,
        'Z2': Z2, 'A2': A2,
        'Z3': Z3, 'A3': A3
    }

    return A3, cache

# Initialize network parameters
np.random.seed(42)

# Layer 1: 3 inputs -> 4 neurons
W1 = np.random.randn(3, 4) * 0.5
b1 = np.zeros(4)

# Layer 2: 4 inputs -> 3 neurons
W2 = np.random.randn(4, 3) * 0.5
b2 = np.zeros(3)

# Layer 3: 3 inputs -> 2 neurons (output)
W3 = np.random.randn(3, 2) * 0.5
b3 = np.zeros(2)

# Test with random input
X_test = np.random.randn(5, 3)  # 5 samples, 3 features
predictions, cache = forward_pass(X_test, W1, b1, W2, b2, W3, b3)

print(f"Input shape: {X_test.shape}")
print(f"Output shape: {predictions.shape}")
print(f"\nPredictions (first 3 samples):")
print(predictions[:3])
print("\nNote: Each row has 2 values (one for each output neuron)")
print("Values are between 0 and 1 due to sigmoid activation")

def mean_squared_error(y_true, y_pred):
    """
    Mean Squared Error loss
    """
    return np.mean((y_true - y_pred) ** 2)

def binary_cross_entropy(y_true, y_pred, epsilon=1e-15):
    """
    Binary Cross-Entropy loss

    epsilon: small value to prevent log(0)
    """
    # Clip predictions to prevent log(0)
    y_pred = np.clip(y_pred, epsilon, 1 - epsilon)

    return -np.mean(
        y_true * np.log(y_pred) +
        (1 - y_true) * np.log(1 - y_pred)
    )

# Example
y_true = np.array([0, 1, 1, 0, 1])
y_pred_good = np.array([0.1, 0.9, 0.8, 0.2, 0.95])  # Good predictions
y_pred_bad = np.array([0.9, 0.1, 0.2, 0.8, 0.05])   # Bad predictions

print("True labels:", y_true)
print("\nGood predictions:", y_pred_good)
print(f"BCE Loss: {binary_cross_entropy(y_true, y_pred_good):.4f}")

print("\nBad predictions:", y_pred_bad)
print(f"BCE Loss: {binary_cross_entropy(y_true, y_pred_bad):.4f}")

print("\n→ Lower loss is better!")

# Visualize how loss changes with predictions
true_label = 1  # True label is 1
predicted_probs = np.linspace(0.01, 0.99, 100)
losses = [binary_cross_entropy(np.array([true_label]), np.array([p])) for p in predicted_probs]

plt.figure(figsize=(10, 6))
plt.plot(predicted_probs, losses, 'b-', linewidth=2)
plt.xlabel('Predicted Probability', fontsize=12)
plt.ylabel('Binary Cross-Entropy Loss', fontsize=12)
plt.title('Loss vs Prediction (True Label = 1)', fontsize=14, fontweight='bold')
plt.grid(True, alpha=0.3)
plt.axvline(x=1.0, color='g', linestyle='--', label='Perfect prediction', alpha=0.5)
plt.legend()
plt.show()

print("Notice: Loss approaches 0 as prediction approaches 1 (the true label)")
print("Loss increases dramatically as prediction moves away from 1")
```

---

## Part 5: Calculus Refresher - Understanding Derivatives

To understand backpropagation, we need to understand **derivatives**. 

### What is a Derivative?

A derivative tells us **how much a function changes** when we change its input slightly.

Think of it as:
- The **slope** of a function at a point
- The **rate of change**
- "If I nudge x a little, how much does y change?"

Notation:
- dy/dx means "derivative of y with respect to x"
- f'(x) means "derivative of f(x)"

### Visual Intuition

```python exec
id: 02-neural-networks-complete-introduction-page-2-1
# Let's visualize derivatives

def f(x):
    """A simple function: f(x) = x²"""
    return x ** 2

def f_derivative(x):
    """Derivative of x²: f'(x) = 2x"""
    return 2 * x

# Plot the function and its tangent lines at different points
x = np.linspace(-3, 3, 100)
y = f(x)

fig, axes = plt.subplots(1, 2, figsize=(15, 5))

# Plot 1: Function with tangent lines
axes[0].plot(x, y, 'b-', linewidth=2, label='f(x) = x²')

# Draw tangent lines at a few points
points = [-2, -1, 0, 1, 2]
for point in points:
    # Point on the curve
    y_point = f(point)
    axes[0].plot(point, y_point, 'ro', markersize=8)

    # Tangent line
    slope = f_derivative(point)
    tangent_x = np.linspace(point - 0.5, point + 0.5, 10)
    tangent_y = y_point + slope * (tangent_x - point)
    axes[0].plot(tangent_x, tangent_y, 'r--', alpha=0.5, linewidth=1.5)

    # Label the slope
    axes[0].text(point, y_point + 1, f"slope={slope:.1f}",
                ha='center', fontsize=9)

axes[0].set_xlabel('x', fontsize=12)
axes[0].set_ylabel('f(x)', fontsize=12)
axes[0].set_title('Function and Tangent Lines\n(red dots show where we computed derivatives)',
                   fontsize=12, fontweight='bold')
axes[0].grid(True, alpha=0.3)
axes[0].legend()

# Plot 2: The derivative function
derivative_y = f_derivative(x)
axes[1].plot(x, derivative_y, 'r-', linewidth=2, label="f'(x) = 2x")
axes[1].axhline(y=0, color='k', linestyle='--', alpha=0.3)
axes[1].axvline(x=0, color='k', linestyle='--', alpha=0.3)
axes[1].set_xlabel('x', fontsize=12)
axes[1].set_ylabel("f'(x)", fontsize=12)
axes[1].set_title('Derivative Function\n(tells us the slope at each point)',
                   fontsize=12, fontweight='bold')
axes[1].grid(True, alpha=0.3)
axes[1].legend()

# Mark the same points
for point in points:
    axes[1].plot(point, f_derivative(point), 'ro', markersize=8)

plt.tight_layout()
plt.show()

print("Key observations:")
print("1. At x = 0, the function is flat (slope = 0)")
print("2. At x = -2, the slope is -4 (steep downward)")
print("3. At x = 2, the slope is 4 (steep upward)")
print("4. The derivative gives us the slope at any point!")
```

### Basic Derivative Rules

Here are the rules we'll need:

1. **Constant Rule**: d/dx(c) = 0
   - The derivative of a constant is 0

2. **Power Rule**: d/dx(x^n) = n·x^(n-1)
   - Example: d/dx(x²) = 2x
   - Example: d/dx(x³) = 3x²

3. **Sum Rule**: d/dx(f + g) = f' + g'
   - The derivative of a sum is the sum of derivatives

4. **Product Rule**: d/dx(f·g) = f'·g + f·g'
   - For multiplying functions

5. **Chain Rule**: d/dx(f(g(x))) = f'(g(x))·g'(x)
   - This is the MOST IMPORTANT one for neural networks!

```python exec
id: 02-neural-networks-complete-introduction-page-2-2
# Let's practice computing derivatives numerically
# (to verify our analytical derivatives)

def numerical_derivative(f, x, h=1e-5):
    """
    Compute derivative numerically using finite differences

    This approximates: f'(x) ≈ [f(x+h) - f(x)] / h
    """
    return (f(x + h) - f(x)) / h

# Test with f(x) = x²
# We know analytically that f'(x) = 2x

x_test = 3.0
analytical_derivative = 2 * x_test  # We know this is 2x
numerical_deriv = numerical_derivative(lambda x: x**2, x_test)

print(f"At x = {x_test}:")
print(f"Analytical derivative (2x): {analytical_derivative}")
print(f"Numerical derivative: {numerical_deriv:.6f}")
print(f"Difference: {abs(analytical_derivative - numerical_deriv):.8f}")
print("\n→ They match! This confirms our analytical calculation.")
```

### The Chain Rule - The Heart of Backpropagation

The **chain rule** is crucial for neural networks because we have functions composed with other functions.

Example: If y = f(g(x)), then:

```
dy/dx = (dy/dg) × (dg/dx)
```

In plain English: "The rate of change of y with respect to x is the rate of change of y with respect to g, times the rate of change of g with respect to x."

Let's see a concrete example:

```python exec
id: 02-neural-networks-complete-introduction-page-2-3
# Example: y = (2x + 3)²
# This is a composition: inner function g(x) = 2x + 3, outer function f(g) = g²

def inner(x):
    """g(x) = 2x + 3"""
    return 2*x + 3

def outer(g):
    """f(g) = g²"""
    return g**2

def composed(x):
    """y = (2x + 3)²"""
    return outer(inner(x))

# Derivatives
def inner_derivative(x):
    """g'(x) = 2"""
    return 2

def outer_derivative(g):
    """f'(g) = 2g"""
    return 2*g

# Chain rule: dy/dx = f'(g(x)) × g'(x)
x_test = 5.0
g_value = inner(x_test)  # g(5) = 2(5) + 3 = 13

dy_dg = outer_derivative(g_value)  # f'(13) = 2(13) = 26
dg_dx = inner_derivative(x_test)   # g'(5) = 2
dy_dx = dy_dg * dg_dx              # Chain rule: 26 × 2 = 52

print(f"At x = {x_test}:")
print(f"g(x) = {g_value}")
print(f"dy/dg = {dy_dg}")
print(f"dg/dx = {dg_dx}")
print(f"dy/dx (chain rule) = {dy_dx}")

# Verify numerically
numerical = numerical_derivative(composed, x_test)
print(f"\nNumerical verification: {numerical:.6f}")
print("→ Chain rule works!")
```

### Derivatives of Activation Functions

We'll need the derivatives of our activation functions for backpropagation.

```python exec
id: 02-neural-networks-complete-introduction-page-2-4
# Derivatives of activation functions

def sigmoid_derivative(x):
    """
    Derivative of sigmoid: σ'(x) = σ(x) × (1 - σ(x))
    """
    s = sigmoid(x)
    return s * (1 - s)

def relu_derivative(x):
    """
    Derivative of ReLU: 1 if x > 0, else 0
    """
    return (x > 0).astype(float)

def tanh_derivative(x):
    """
    Derivative of tanh: 1 - tanh²(x)
    """
    return 1 - np.tanh(x)**2

# Visualize the derivatives
x = np.linspace(-5, 5, 1000)

fig, axes = plt.subplots(2, 3, figsize=(15, 8))

# Sigmoid and its derivative
axes[0, 0].plot(x, sigmoid(x), 'b-', linewidth=2)
axes[0, 0].set_title('Sigmoid', fontweight='bold')
axes[0, 0].grid(True, alpha=0.3)
axes[1, 0].plot(x, sigmoid_derivative(x), 'b-', linewidth=2)
axes[1, 0].set_title('Sigmoid Derivative', fontweight='bold')
axes[1, 0].grid(True, alpha=0.3)

# ReLU and its derivative
axes[0, 1].plot(x, relu(x), 'r-', linewidth=2)
axes[0, 1].set_title('ReLU', fontweight='bold')
axes[0, 1].grid(True, alpha=0.3)
axes[1, 1].plot(x, relu_derivative(x), 'r-', linewidth=2)
axes[1, 1].set_title('ReLU Derivative', fontweight='bold')
axes[1, 1].grid(True, alpha=0.3)

# Tanh and its derivative
axes[0, 2].plot(x, tanh(x), 'g-', linewidth=2)
axes[0, 2].set_title('Tanh', fontweight='bold')
axes[0, 2].grid(True, alpha=0.3)
axes[1, 2].plot(x, tanh_derivative(x), 'g-', linewidth=2)
axes[1, 2].set_title('Tanh Derivative', fontweight='bold')
axes[1, 2].grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

print("Key observations:")
print("1. Sigmoid derivative is largest at x=0, approaches 0 at extremes")
print("2. ReLU derivative is 1 for positive x, 0 for negative x")
print("3. Tanh derivative is largest at x=0, approaches 0 at extremes")
```

---

## Part 6: Backpropagation - How Neural Networks Learn

**Backpropagation** is the algorithm that allows neural networks to learn from their mistakes. It computes how much each weight contributed to the error, so we know how to adjust them.

### The Big Idea

1. **Forward pass**: Make a prediction
2. **Compute loss**: See how wrong we were
3. **Backward pass**: Use chain rule to compute gradients (derivatives of loss with respect to weights)
4. **Update weights**: Adjust weights in the direction that reduces loss

### Mathematical Framework

For a single layer:

```
Z = X @ W + b      (weighted sum)
A = σ(Z)           (activation)
L = loss(A, y)     (loss)
```

We want to find:
- ∂L/∂W: How does loss change when we change W?
- ∂L/∂b: How does loss change when we change b?

Using the chain rule:

```
∂L/∂W = ∂L/∂A × ∂A/∂Z × ∂Z/∂W
```

Let's implement this step by step.

### Simple Example: Single Layer Network

Let's start with the simplest possible network to understand backprop.

```python exec
id: 02-neural-networks-complete-introduction-page-2-5
# Simple dataset: XOR problem (classic non-linear problem)
# Input: two binary values, Output: 1 if they're different, 0 if same

X_simple = np.array([[0, 0],
                     [0, 1],
                     [1, 0],
                     [1, 1]])

y_simple = np.array([[0],
                     [1],
                     [1],
                     [0]])

print("XOR Problem:")
print("Inputs:")
print(X_simple)
print("\nOutputs:")
print(y_simple.ravel())
print("\nGoal: Output 1 when inputs are different, 0 when same")
```

```python exec
id: 02-neural-networks-complete-introduction-page-2-6
# Initialize a simple 2-layer network
# Architecture: 2 inputs -> 3 hidden neurons (ReLU) -> 1 output (Sigmoid)

np.random.seed(42)

# Hidden layer
W1_simple = np.random.randn(2, 3) * 0.5
b1_simple = np.zeros((1, 3))

# Output layer
W2_simple = np.random.randn(3, 1) * 0.5
b2_simple = np.zeros((1, 1))

print("Initial weights:")
print(f"W1 shape: {W1_simple.shape}")
print(f"W2 shape: {W2_simple.shape}")
```

```python exec
id: 02-neural-networks-complete-introduction-page-2-7
def forward_simple(X, W1, b1, W2, b2):
    """
    Forward pass for simple network
    """
    # Hidden layer
    Z1 = X @ W1 + b1
    A1 = relu(Z1)

    # Output layer
    Z2 = A1 @ W2 + b2
    A2 = sigmoid(Z2)

    cache = {'Z1': Z1, 'A1': A1, 'Z2': Z2, 'A2': A2}
    return A2, cache

def backward_simple(X, y, cache, W2):
    """
    Backward pass for simple network

    This is where the magic happens!
    """
    m = X.shape[0]  # Number of samples

    # Get cached values from forward pass
    Z1 = cache['Z1']
    A1 = cache['A1']
    Z2 = cache['Z2']
    A2 = cache['A2']

    # Backward pass - layer 2 (output)
    # dL/dA2: derivative of loss with respect to output
    dA2 = A2 - y  # For binary cross-entropy with sigmoid

    # dL/dZ2 = dL/dA2 × dA2/dZ2 (chain rule)
    dZ2 = dA2 * sigmoid_derivative(Z2)

    # dL/dW2 = A1^T @ dZ2
    dW2 = (A1.T @ dZ2) / m
    db2 = np.sum(dZ2, axis=0, keepdims=True) / m

    # Backward pass - layer 1 (hidden)
    # dL/dA1 = dZ2 @ W2^T (chain rule)
    dA1 = dZ2 @ W2.T

    # dL/dZ1 = dL/dA1 × dA1/dZ1 (chain rule)
    dZ1 = dA1 * relu_derivative(Z1)

    # dL/dW1 = X^T @ dZ1
    dW1 = (X.T @ dZ1) / m
    db1 = np.sum(dZ1, axis=0, keepdims=True) / m

    gradients = {
        'dW1': dW1, 'db1': db1,
        'dW2': dW2, 'db2': db2
    }

    return gradients

# Test forward and backward pass
predictions, cache = forward_simple(X_simple, W1_simple, b1_simple, W2_simple, b2_simple)
gradients = backward_simple(X_simple, y_simple, cache, W2_simple)

print("Forward pass predictions (before training):")
print(predictions.ravel())
print("\nGradients computed successfully!")
print(f"dW1 shape: {gradients['dW1'].shape}")
print(f"dW2 shape: {gradients['dW2'].shape}")
```

### Visualizing the Backward Pass

Let's visualize how gradients flow backward through the network.

```python exec
id: 02-neural-networks-complete-introduction-page-2-8
# Create a visualization of gradient flow
fig, ax = plt.subplots(1, 1, figsize=(14, 8))

# Define layer positions
layer_x = [0.1, 0.5, 0.9]
layer_names = ['Input\nLayer', 'Hidden\nLayer', 'Output\nLayer']
layer_sizes = [2, 3, 1]

# Draw nodes
for i, (x, name, size) in enumerate(zip(layer_x, layer_names, layer_sizes)):
    y_positions = np.linspace(0.2, 0.8, size)
    for y in y_positions:
        circle = plt.Circle((x, y), 0.03, color='lightblue', ec='black', linewidth=2)
        ax.add_patch(circle)

    # Layer label
    ax.text(x, 0.05, name, ha='center', fontsize=12, fontweight='bold')

# Draw forward arrows (thin gray)
for i in range(len(layer_x) - 1):
    x1, x2 = layer_x[i], layer_x[i + 1]
    y1_positions = np.linspace(0.2, 0.8, layer_sizes[i])
    y2_positions = np.linspace(0.2, 0.8, layer_sizes[i + 1])

    for y1 in y1_positions:
        for y2 in y2_positions:
            ax.arrow(x1 + 0.03, y1, x2 - x1 - 0.06, y2 - y1,
                    head_width=0.01, head_length=0.02,
                    fc='gray', ec='gray', alpha=0.3, linewidth=0.5)

# Draw backward arrows (thick red)
for i in range(len(layer_x) - 1, 0, -1):
    x1, x2 = layer_x[i], layer_x[i - 1]
    y1_positions = np.linspace(0.2, 0.8, layer_sizes[i])
    y2_positions = np.linspace(0.2, 0.8, layer_sizes[i - 1])

    for y1 in y1_positions:
        for y2 in y2_positions:
            ax.arrow(x1 - 0.03, y1 + 0.02, x2 - x1 + 0.06, y2 - y1,
                    head_width=0.015, head_length=0.025,
                    fc='red', ec='red', alpha=0.6, linewidth=1.5)

# Add annotations
ax.text(0.3, 0.95, 'Forward Pass →', fontsize=14, color='gray')
ax.text(0.7, 0.95, '← Backpropagation', fontsize=14, color='red', fontweight='bold')

ax.text(0.5, -0.05, 'Gradients flow backward, adjusting weights to reduce error',
        ha='center', fontsize=11, style='italic')

ax.set_xlim(-0.05, 1.05)
ax.set_ylim(-0.1, 1.0)
ax.axis('off')
plt.title('Backpropagation: Gradient Flow', fontsize=16, fontweight='bold', pad=20)
plt.tight_layout()
plt.show()
```

---

## Part 7: Gradient Descent - The Learning Algorithm

**Gradient descent** is the algorithm that updates weights based on the gradients we computed.

### The Core Idea

Imagine you're standing on a hill in fog and want to reach the valley. You:
1. Feel which direction is steepest (compute gradient)
2. Take a step downhill (update weights)
3. Repeat

The **learning rate** (α) controls how big each step is.

**Update rule**:
```
W_new = W_old - α × ∂L/∂W
```

### Learning Rate Matters!

- Too small: Learning is very slow
- Too large: We might overshoot the minimum
- Just right: Efficient learning

```python exec
id: 02-neural-networks-complete-introduction-page-2-9
# Visualize gradient descent on a simple function

def simple_loss(w):
    """A simple quadratic loss: L(w) = (w - 2)²"""
    return (w - 2) ** 2

def simple_loss_derivative(w):
    """Derivative: dL/dw = 2(w - 2)"""
    return 2 * (w - 2)

def gradient_descent_demo(learning_rate, n_steps, start_w):
    """Run gradient descent and track progress"""
    w = start_w
    history = [w]

    for _ in range(n_steps):
        gradient = simple_loss_derivative(w)
        w = w - learning_rate * gradient
        history.append(w)

    return np.array(history)

# Test different learning rates
w_range = np.linspace(-1, 5, 100)
loss_values = simple_loss(w_range)

fig, axes = plt.subplots(1, 3, figsize=(18, 5))
learning_rates = [0.01, 0.1, 0.9]
colors = ['blue', 'green', 'red']

for ax, lr, color in zip(axes, learning_rates, colors):
    # Plot loss function
    ax.plot(w_range, loss_values, 'k-', linewidth=2, alpha=0.3, label='Loss function')

    # Run gradient descent
    history = gradient_descent_demo(lr, 20, start_w=4.5)
    loss_history = simple_loss(history)

    # Plot path
    ax.plot(history, loss_history, 'o-', color=color, markersize=6,
            linewidth=2, label=f'GD path (α={lr})')
    ax.plot(history[0], loss_history[0], 'o', color='orange',
            markersize=12, label='Start')
    ax.plot(history[-1], loss_history[-1], '*', color='gold',
            markersize=15, label='End')

    ax.set_xlabel('Weight (w)', fontsize=11)
    ax.set_ylabel('Loss', fontsize=11)
    ax.set_title(f'Learning Rate = {lr}', fontsize=12, fontweight='bold')
    ax.legend(loc='upper right', fontsize=9)
    ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

print("Observations:")
print("1. α = 0.01 (blue): Slow but steady convergence")
print("2. α = 0.1 (green): Faster convergence, good balance")
print("3. α = 0.9 (red): Very fast but might oscillate")
```

```python exec
id: 02-neural-networks-complete-introduction-page-2-10
# Now let's train our simple network!

def train_simple_network(X, y, W1, b1, W2, b2, learning_rate=0.5, epochs=1000):
    """
    Train the simple network using gradient descent
    """
    loss_history = []

    for epoch in range(epochs):
        # Forward pass
        predictions, cache = forward_simple(X, W1, b1, W2, b2)

        # Compute loss
        loss = binary_cross_entropy(y, predictions)
        loss_history.append(loss)

        # Backward pass
        gradients = backward_simple(X, y, cache, W2)

        # Update weights (gradient descent)
        W1 -= learning_rate * gradients['dW1']
        b1 -= learning_rate * gradients['db1']
        W2 -= learning_rate * gradients['dW2']
        b2 -= learning_rate * gradients['db2']

        # Print progress
        if (epoch + 1) % 200 == 0:
            print(f"Epoch {epoch + 1}/{epochs}, Loss: {loss:.4f}")

    return W1, b1, W2, b2, loss_history

# Train the network
print("Training network on XOR problem...\n")
W1_trained, b1_trained, W2_trained, b2_trained, loss_history = train_simple_network(
    X_simple, y_simple, W1_simple, b1_simple, W2_simple, b2_simple,
    learning_rate=0.5, epochs=2000
)
```

```python exec
id: 02-neural-networks-complete-introduction-page-2-11
# Visualize training progress
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.plot(loss_history, linewidth=2)
plt.xlabel('Epoch', fontsize=12)
plt.ylabel('Loss', fontsize=12)
plt.title('Training Loss Over Time', fontsize=14, fontweight='bold')
plt.grid(True, alpha=0.3)

# Test the trained network
final_predictions, _ = forward_simple(X_simple, W1_trained, b1_trained,
                                      W2_trained, b2_trained)

plt.subplot(1, 2, 2)
x_pos = np.arange(len(X_simple))
plt.bar(x_pos - 0.2, y_simple.ravel(), 0.4, label='True', alpha=0.7)
plt.bar(x_pos + 0.2, final_predictions.ravel(), 0.4, label='Predicted', alpha=0.7)
plt.xlabel('Sample', fontsize=12)
plt.ylabel('Output', fontsize=12)
plt.title('Predictions vs Ground Truth', fontsize=14, fontweight='bold')
plt.xticks(x_pos, ['[0,0]', '[0,1]', '[1,0]', '[1,1]'])
plt.legend()
plt.grid(True, alpha=0.3, axis='y')

plt.tight_layout()
plt.show()

print("\nFinal predictions:")
for i, (inp, true, pred) in enumerate(zip(X_simple, y_simple, final_predictions)):
    print(f"Input: {inp}, True: {true[0]}, Predicted: {pred[0]:.4f}, "
          f"Rounded: {int(pred[0] > 0.5)}")
```

---

## Part 8: Complete Neural Network Class

Now let's create a complete, reusable neural network class that we can use for real problems!

```python exec
id: 02-neural-networks-complete-introduction-page-2-12
class NeuralNetwork:
    """
    A simple feedforward neural network

    Architecture: Input -> Hidden Layer(s) -> Output
    """

    def __init__(self, layer_sizes, learning_rate=0.01):
        """
        Initialize network

        Parameters:
        -----------
        layer_sizes : list
            Number of neurons in each layer (including input and output)
            Example: [784, 128, 64, 10] for MNIST
        learning_rate : float
            Learning rate for gradient descent
        """
        self.layer_sizes = layer_sizes
        self.learning_rate = learning_rate
        self.n_layers = len(layer_sizes)

        # Initialize weights and biases
        self.weights = []
        self.biases = []

        for i in range(self.n_layers - 1):
            # He initialization for ReLU
            W = np.random.randn(layer_sizes[i], layer_sizes[i+1]) * np.sqrt(2.0 / layer_sizes[i])
            b = np.zeros((1, layer_sizes[i+1]))

            self.weights.append(W)
            self.biases.append(b)

    def forward(self, X):
        """
        Forward propagation

        Returns predictions and cache of intermediate values
        """
        cache = {'A0': X}  # Store input
        A = X

        # Through all layers except the last
        for i in range(self.n_layers - 2):
            Z = A @ self.weights[i] + self.biases[i]
            A = relu(Z)

            cache[f'Z{i+1}'] = Z
            cache[f'A{i+1}'] = A

        # Output layer (sigmoid)
        Z = A @ self.weights[-1] + self.biases[-1]
        A = sigmoid(Z)

        cache[f'Z{self.n_layers-1}'] = Z
        cache[f'A{self.n_layers-1}'] = A

        return A, cache

    def backward(self, X, y, cache):
        """
        Backward propagation

        Computes gradients for all weights and biases
        """
        m = X.shape[0]
        gradients = {}

        # Output layer gradient
        A_out = cache[f'A{self.n_layers-1}']
        dA = A_out - y

        # Backward through all layers
        for i in range(self.n_layers - 2, -1, -1):
            # Current layer activations
            A_prev = cache[f'A{i}']
            Z = cache[f'Z{i+1}']

            # Compute dZ based on activation function
            if i == self.n_layers - 2:  # Output layer (sigmoid)
                dZ = dA * sigmoid_derivative(Z)
            else:  # Hidden layers (ReLU)
                dZ = dA * relu_derivative(Z)

            # Compute weight and bias gradients
            dW = (A_prev.T @ dZ) / m
            db = np.sum(dZ, axis=0, keepdims=True) / m

            gradients[f'dW{i}'] = dW
            gradients[f'db{i}'] = db

            # Propagate gradient to previous layer
            if i > 0:
                dA = dZ @ self.weights[i].T

        return gradients

    def update_parameters(self, gradients):
        """
        Update weights and biases using gradient descent
        """
        for i in range(self.n_layers - 1):
            self.weights[i] -= self.learning_rate * gradients[f'dW{i}']
            self.biases[i] -= self.learning_rate * gradients[f'db{i}']

    def train(self, X, y, epochs=1000, verbose=True):
        """
        Train the network
        """
        loss_history = []

        for epoch in range(epochs):
            # Forward pass
            predictions, cache = self.forward(X)

            # Compute loss
            loss = binary_cross_entropy(y, predictions)
            loss_history.append(loss)

            # Backward pass
            gradients = self.backward(X, y, cache)

            # Update parameters
            self.update_parameters(gradients)

            # Print progress
            if verbose and (epoch + 1) % (epochs // 10) == 0:
                accuracy = self.compute_accuracy(X, y)
                print(f"Epoch {epoch + 1}/{epochs}, Loss: {loss:.4f}, Accuracy: {accuracy:.2%}")

        return loss_history

    def predict(self, X):
        """
        Make predictions
        """
        predictions, _ = self.forward(X)
        return (predictions > 0.5).astype(int)

    def compute_accuracy(self, X, y):
        """
        Compute classification accuracy
        """
        predictions = self.predict(X)
        return np.mean(predictions == y)

print("Neural Network class created successfully!")
```

```python exec
id: 02-neural-networks-complete-introduction-page-2-13
# Test the neural network class on XOR
print("Testing Neural Network on XOR problem:\n")

# Create network: 2 inputs -> 4 hidden -> 1 output
nn = NeuralNetwork([2, 4, 1], learning_rate=0.5)

# Train
loss_history = nn.train(X_simple, y_simple, epochs=2000, verbose=True)

# Test
print("\nFinal predictions:")
predictions = nn.predict(X_simple)
for i, (inp, true, pred) in enumerate(zip(X_simple, y_simple, predictions)):
    print(f"Input: {inp}, True: {true[0]}, Predicted: {pred[0]}")
```

---

## Part 9: Real-World Application - MNIST Digit Recognition

Now for the grand finale! Let's train our neural network to recognize handwritten digits from the famous MNIST dataset.

### About MNIST

- 70,000 grayscale images of handwritten digits (0-9)
- Each image is 28×28 pixels
- Training set: 60,000 images
- Test set: 10,000 images

```python exec
id: 02-neural-networks-complete-introduction-page-2-14
# Load MNIST dataset
# We'll use a simple method to download and load the data

from urllib.request import urlretrieve
import gzip
import os

def load_mnist():
    """
    Download and load MNIST dataset
    """
    base_url = 'https://storage.googleapis.com/cvdf-datasets/mnist/'
    files = [
        'train-images-idx3-ubyte.gz',
        'train-labels-idx1-ubyte.gz',
        't10k-images-idx3-ubyte.gz',
        't10k-labels-idx1-ubyte.gz'
    ]

    # Download files if not present
    for file in files:
        if not os.path.exists(file):
            print(f"Downloading {file}...")
            urlretrieve(base_url + file, file)

    # Load training data
    with gzip.open('train-images-idx3-ubyte.gz', 'rb') as f:
        X_train = np.frombuffer(f.read(), np.uint8, offset=16).reshape(-1, 28*28)

    with gzip.open('train-labels-idx1-ubyte.gz', 'rb') as f:
        y_train = np.frombuffer(f.read(), np.uint8, offset=8)

    # Load test data
    with gzip.open('t10k-images-idx3-ubyte.gz', 'rb') as f:
        X_test = np.frombuffer(f.read(), np.uint8, offset=16).reshape(-1, 28*28)

    with gzip.open('t10k-labels-idx1-ubyte.gz', 'rb') as f:
        y_test = np.frombuffer(f.read(), np.uint8, offset=8)

    return X_train, y_train, X_test, y_test

print("Loading MNIST dataset...")
X_train_full, y_train_full, X_test_full, y_test_full = load_mnist()
print("Dataset loaded!")
print(f"Training set: {X_train_full.shape[0]} images")
print(f"Test set: {X_test_full.shape[0]} images")
print(f"Image dimensions: {X_train_full.shape[1]} pixels (28×28 flattened)")
```

```python exec
id: 02-neural-networks-complete-introduction-page-2-15
# Visualize some examples
fig, axes = plt.subplots(2, 5, figsize=(12, 5))
axes = axes.ravel()

for i in range(10):
    # Reshape back to 28x28 for visualization
    image = X_train_full[i].reshape(28, 28)
    axes[i].imshow(image, cmap='gray')
    axes[i].set_title(f'Label: {y_train_full[i]}', fontsize=12)
    axes[i].axis('off')

plt.suptitle('Sample MNIST Digits', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.show()
```

```python exec
id: 02-neural-networks-complete-introduction-page-2-16
# For faster training, let's work with a subset and binary classification first
# Task: Distinguish between 0s and 1s

def prepare_binary_mnist(X, y, digit_a=0, digit_b=1, n_samples=1000):
    """
    Prepare a binary classification dataset from MNIST
    """
    # Find indices of desired digits
    idx_a = np.where(y == digit_a)[0][:n_samples//2]
    idx_b = np.where(y == digit_b)[0][:n_samples//2]
    idx = np.concatenate([idx_a, idx_b])

    # Select samples
    X_binary = X[idx]
    y_binary = y[idx]

    # Convert labels to 0 and 1
    y_binary = (y_binary == digit_b).astype(int).reshape(-1, 1)

    # Normalize pixel values to [0, 1]
    X_binary = X_binary / 255.0

    # Shuffle
    shuffle_idx = np.random.permutation(len(X_binary))
    X_binary = X_binary[shuffle_idx]
    y_binary = y_binary[shuffle_idx]

    return X_binary, y_binary

# Prepare datasets
print("Preparing binary classification task (0 vs 1)...")
X_train, y_train = prepare_binary_mnist(X_train_full, y_train_full,
                                         digit_a=0, digit_b=1, n_samples=2000)
X_test, y_test = prepare_binary_mnist(X_test_full, y_test_full,
                                       digit_a=0, digit_b=1, n_samples=400)

print(f"Training set: {X_train.shape}")
print(f"Test set: {X_test.shape}")
print(f"Label distribution in training: {np.sum(y_train==0)} zeros, {np.sum(y_train==1)} ones")
```

```python exec
id: 02-neural-networks-complete-introduction-page-2-17
# Create and train network for MNIST
print("Creating neural network for MNIST...")
print("Architecture: 784 -> 128 -> 64 -> 1\n")

mnist_nn = NeuralNetwork([784, 128, 64, 1], learning_rate=0.1)

print("Training network...\n")
loss_history = mnist_nn.train(X_train, y_train, epochs=100, verbose=True)

# Evaluate on test set
test_accuracy = mnist_nn.compute_accuracy(X_test, y_test)
print(f"\nTest Accuracy: {test_accuracy:.2%}")
```

```python exec
id: 02-neural-networks-complete-introduction-page-2-18
# Visualize training and results
fig = plt.figure(figsize=(15, 10))

# Plot 1: Loss curve
ax1 = plt.subplot(2, 3, 1)
ax1.plot(loss_history, linewidth=2)
ax1.set_xlabel('Epoch')
ax1.set_ylabel('Loss')
ax1.set_title('Training Loss', fontweight='bold')
ax1.grid(True, alpha=0.3)

# Plot 2-7: Sample predictions
test_predictions, _ = mnist_nn.forward(X_test)
sample_indices = np.random.choice(len(X_test), 6, replace=False)

for i, idx in enumerate(sample_indices):
    ax = plt.subplot(2, 3, i + 2)

    # Show image
    image = X_test[idx].reshape(28, 28)
    ax.imshow(image, cmap='gray')

    # Get prediction
    true_label = "1" if y_test[idx] == 1 else "0"
    pred_prob = test_predictions[idx][0]
    pred_label = "1" if pred_prob > 0.5 else "0"

    # Color based on correctness
    color = 'green' if true_label == pred_label else 'red'

    ax.set_title(f"True: {true_label}, Pred: {pred_label} ({pred_prob:.2f})",
                 color=color, fontweight='bold')
    ax.axis('off')

plt.suptitle('Neural Network Results on MNIST (0 vs 1)',
             fontsize=16, fontweight='bold')
plt.tight_layout()
plt.show()
```

```python exec
id: 02-neural-networks-complete-introduction-page-2-19
# Visualize what the network learned
# Let's look at the first layer weights

first_layer_weights = mnist_nn.weights[0]  # Shape: (784, 128)

# Each column is a weight vector for one neuron
# We can visualize these as 28x28 images

fig, axes = plt.subplots(4, 8, figsize=(16, 8))
axes = axes.ravel()

for i in range(32):  # Show first 32 neurons
    # Get weights for this neuron and reshape to image
    weights = first_layer_weights[:, i].reshape(28, 28)

    axes[i].imshow(weights, cmap='RdBu', vmin=-np.abs(weights).max(),
                   vmax=np.abs(weights).max())
    axes[i].set_title(f'Neuron {i+1}', fontsize=9)
    axes[i].axis('off')

plt.suptitle('First Layer Weight Visualizations\n(What Features Each Neuron Detects)',
             fontsize=14, fontweight='bold')
plt.tight_layout()
plt.show()

print("These visualizations show what patterns each neuron in the first layer has learned to detect!")
print("Blue regions indicate positive weights, red regions indicate negative weights.")
```

---

## Summary and Key Takeaways


### What We Learned

1. **Matrices**: The foundation of neural networks
 - Matrix multiplication is how layers process data
 - Weights are stored as matrices

2. **Neural Networks**: Layers of connected neurons
 - Each neuron computes weighted sum + bias
 - Activation functions introduce non-linearity
 - Stacking layers allows learning complex patterns

3. **Forward Propagation**: Making predictions
 - Data flows forward through layers
 - Each layer transforms the data
 - Output layer gives predictions

4. **Loss Functions**: Measuring errors
 - Quantify how wrong predictions are
 - Goal is to minimize loss

5. **Calculus**: Understanding change
 - Derivatives tell us rates of change
 - Chain rule connects derivatives through layers
 - Gradients point in direction of steepest increase

6. **Backpropagation**: Learning from mistakes
 - Computes gradients by working backward
 - Uses chain rule extensively
 - Tells us how to adjust weights

7. **Gradient Descent**: The optimization algorithm
 - Updates weights to reduce loss
 - Learning rate controls step size
 - Iterative process gradually improves network

### The Big Picture

Neural networks learn by:
1. Making predictions (forward pass)
2. Measuring errors (loss function)
3. Computing gradients (backpropagation)
4. Updating weights (gradient descent)
5. Repeating until loss is minimized

This process is fundamentally the same whether you're recognizing digits, translating languages, or playing games!

### Next Steps

To deepen your understanding, try:
- Experimenting with different network architectures
- Trying different learning rates
- Training on different digit pairs
- Extending to multi-class classification (all 10 digits)
- Implementing other optimization algorithms (momentum, Adam)
- Adding regularization to prevent overfitting
- Exploring convolutional neural networks for images

### Resources for Further Learning

- **Michael Nielsen's Book**: [Neural Networks and Deep Learning](http://neuralnetworksanddeeplearning.com/)
- **3Blue1Brown**: [Neural Network Video Series](https://www.youtube.com/playlist?list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi)
- **Andrew Ng's Course**: [Deep Learning Specialization](https://www.coursera.org/specializations/deep-learning)

Remember: Understanding these fundamentals is crucial. Modern frameworks like TensorFlow and PyTorch handle these details for you, but knowing what's happening under the hood makes you a better practitioner!

---

---

## Exercises for Students

Try these exercises to reinforce your learning:

### Beginner Level

1. Modify the XOR network to solve the AND problem (outputs 1 only when both inputs are 1)
2. Visualize the decision boundary of a trained network on a 2D dataset
3. Experiment with different learning rates and observe the effect on training

### Intermediate Level

4. Implement mini-batch gradient descent (update weights using batches of data)
5. Add momentum to the gradient descent algorithm
6. Create a network that classifies three different digits (0, 1, 2)
7. Implement early stopping (stop training when validation loss stops improving)

### Advanced Level

8. Implement dropout regularization
9. Add a validation set and plot training vs validation loss
10. Implement L2 regularization
11. Create a confusion matrix to visualize classification errors
12. Train a network on all 10 MNIST digits (multi-class classification)

### Try this Projects

13. Implement the Adam optimizer
14. Create an animation showing how the network's predictions improve during training
15. Build a network that can classify Fashion-MNIST (clothing items)
16. Implement batch normalization
17. Create a simple autoencoder for image compression

## Looking back

Before leaving this page, a sentence on each. What you write stays on this device.

```reflect
- Something you expected before running a cell that turned out differently
- The one idea from this page you could explain to someone else now
- Something you would change or try next, if there were time
- A question this page raised for you that it did not answer. Bring it to the next session; these questions are where the next session starts.
```
