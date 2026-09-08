---
title: "Neural Networks From Scratch: A Complete Introduction (1 of 2)"
slug: 02-neural-networks-complete-introduction-page-1
course: ai-and-ml-foundations
course_title: "AI and ML Foundations"
series: 5-neural-networks
series_title: "Neural Networks"
version: 2026.09.06.1
---

# Neural Networks From Scratch: A Complete Introduction

**For QQI Level 5 Students**

---

## Welcome!

In this notebook, we're going to build a complete neural network from scratch. We'll start with the absolute basics—matrices and how to work with them—and gradually build up to understanding and implementing:

- **Matrix operations** (the foundation of neural networks)
- **Forward propagation** (how neural networks make predictions)
- **Loss functions** (how we measure errors)
- **Derivatives and calculus** (the math behind learning)
- **Backpropagation** (how neural networks learn from mistakes)
- **Gradient descent** (the optimization algorithm)
- **Training a real neural network** (putting it all together)

By the end, you'll have trained a neural network to recognize handwritten digits!

### What You Need to Know Before Starting

- Basic Python (variables, loops, functions)
- Basic algebra (adding, multiplying, simple equations)
- Curiosity and patience!

### What We'll Use

- **NumPy**: For efficient numerical operations
- **Matplotlib**: For visualizations
- **MNIST Dataset**: Handwritten digits (0-9)

Let's begin!

---

## Part 1: Matrices - The Foundation

### What is a Matrix?

A **matrix** is just a rectangular grid of numbers. Think of it like a spreadsheet or a table.

Example of a 2×3 matrix (2 rows, 3 columns):

```
[ 1  2  3 ]
[ 4  5  6 ]
```

Why do we care about matrices? Because neural networks are essentially chains of matrix operations!

### Setting Up Our Environment

```python exec
id: 02-neural-networks-complete-introduction-page-1-1
# Import the libraries we'll need
import numpy as np
import matplotlib.pyplot as plt

# Make our plots look nice
plt.style.use('seaborn-v0_8-darkgrid')

# Set random seed for reproducibility
np.random.seed(42)

print("Libraries imported successfully!")
print(f"NumPy version: {np.__version__}")
```

### Creating Matrices in NumPy

```python exec
id: 02-neural-networks-complete-introduction-page-1-2
# Create a simple matrix (2D array)
matrix_a = np.array([[1, 2, 3],
                     [4, 5, 6]])

print("Matrix A:")
print(matrix_a)
print(f"\nShape: {matrix_a.shape}")  # (2, 3) means 2 rows, 3 columns
print(f"Total elements: {matrix_a.size}")
```

```python exec
id: 02-neural-networks-complete-introduction-page-1-3
# Create a vector (1D array) - think of it as a single row or column
vector = np.array([1, 2, 3])

print("Vector:")
print(vector)
print(f"Shape: {vector.shape}")  # (3,) means 3 elements
```

```python exec
id: 02-neural-networks-complete-introduction-page-1-4
# Common ways to create matrices

# Matrix of zeros
zeros = np.zeros((3, 4))  # 3 rows, 4 columns
print("Matrix of zeros:")
print(zeros)

# Matrix of ones
ones = np.ones((2, 3))
print("\nMatrix of ones:")
print(ones)

# Random matrix (values between 0 and 1)
random_matrix = np.random.rand(2, 3)
print("\nRandom matrix:")
print(random_matrix)
```

### Matrix Operations

#### 1. Element-wise Operations

These operations work on each element individually.

```python exec
id: 02-neural-networks-complete-introduction-page-1-5
matrix_a = np.array([[1, 2],
                     [3, 4]])

matrix_b = np.array([[5, 6],
                     [7, 8]])

# Addition
print("Matrix A:")
print(matrix_a)
print("\nMatrix B:")
print(matrix_b)
print("\nA + B (element-wise):")
print(matrix_a + matrix_b)

# Multiplication (element-wise)
print("\nA * B (element-wise):")
print(matrix_a * matrix_b)
```

```python exec
id: 02-neural-networks-complete-introduction-page-1-6
# Scalar operations (applying a single number to all elements)
print("Matrix A * 2:")
print(matrix_a * 2)

print("\nMatrix A + 10:")
print(matrix_a + 10)
```

#### 2. Matrix Multiplication (The Important One!)

Matrix multiplication is different from element-wise multiplication. It's the fundamental operation in neural networks.

**Rule**: To multiply matrix A (shape m×n) by matrix B (shape n×p), the number of columns in A must equal the number of rows in B. The result is a matrix of shape m×p.

**How it works**: Each element in the result is the dot product of a row from A and a column from B.

```python exec
id: 02-neural-networks-complete-introduction-page-1-7
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
```

```python exec
id: 02-neural-networks-complete-introduction-page-1-8
# Visualizing matrix multiplication
def visualize_matrix_multiplication(A, B):
    """
    Visualize how matrix multiplication works
    """
    fig, axes = plt.subplots(1, 3, figsize=(15, 4))

    # Matrix A
    axes[0].imshow(A, cmap='Blues', alpha=0.6)
    axes[0].set_title(f'Matrix A\nShape: {A.shape}', fontsize=12, fontweight='bold')
    for i in range(A.shape[0]):
        for j in range(A.shape[1]):
            axes[0].text(j, i, f'{A[i,j]:.1f}', ha='center', va='center', fontsize=14)
    axes[0].set_xticks([])
    axes[0].set_yticks([])

    # Matrix B
    axes[1].imshow(B, cmap='Greens', alpha=0.6)
    axes[1].set_title(f'Matrix B\nShape: {B.shape}', fontsize=12, fontweight='bold')
    for i in range(B.shape[0]):
        for j in range(B.shape[1]):
            axes[1].text(j, i, f'{B[i,j]:.1f}', ha='center', va='center', fontsize=14)
    axes[1].set_xticks([])
    axes[1].set_yticks([])

    # Result
    C = A @ B
    axes[2].imshow(C, cmap='Reds', alpha=0.6)
    axes[2].set_title(f'Result A @ B\nShape: {C.shape}', fontsize=12, fontweight='bold')
    for i in range(C.shape[0]):
        for j in range(C.shape[1]):
            axes[2].text(j, i, f'{C[i,j]:.1f}', ha='center', va='center', fontsize=14)
    axes[2].set_xticks([])
    axes[2].set_yticks([])

    plt.tight_layout()
    plt.show()

# Example
A = np.array([[1, 2, 3],
              [4, 5, 6]])
B = np.array([[7, 8],
              [9, 10],
              [11, 12]])

visualize_matrix_multiplication(A, B)
```

#### 3. The Transpose Operation

Transposing a matrix means flipping it along its diagonal - rows become columns and columns become rows.

```python exec
id: 02-neural-networks-complete-introduction-page-1-9
matrix = np.array([[1, 2, 3],
                   [4, 5, 6]])

print("Original matrix:")
print(matrix)
print(f"Shape: {matrix.shape}")

transposed = matrix.T
print("\nTransposed matrix:")
print(transposed)
print(f"Shape: {transposed.shape}")
```

### Your turn: Matrix Operations

Before moving on, let's make sure we understand these operations!

```python exec
id: 02-neural-networks-complete-introduction-page-1-10
# Exercise: Create two matrices and perform operations

# Create a 3x2 matrix of your choice
my_matrix_1 = np.array([[1, 2],
                        [3, 4],
                        [5, 6]])

# Create a 2x3 matrix of your choice
my_matrix_2 = np.array([[7, 8, 9],
                        [10, 11, 12]])

# Multiply them
result = my_matrix_1 @ my_matrix_2
print("Matrix multiplication result:")
print(result)
print(f"Shape: {result.shape}")

# Try transposing the result
print("\nTransposed result:")
print(result.T)
```

---

## Part 2: What is a Neural Network?

### The Big Picture

A neural network is inspired by how the human brain works. It consists of:

- **Input layer**: Where data comes in (e.g., pixels of an image)
- **Hidden layers**: Where the "thinking" happens
- **Output layer**: Where predictions come out

Each layer contains **neurons** (also called nodes or units). Neurons are connected by **weights** that control how much influence one neuron has on another.

### A Simple Neuron

A single neuron does three things:

1. **Takes inputs** (multiple values)
2. **Multiplies each input by a weight** and adds them up, plus a bias
3. **Applies an activation function** to produce an output

Mathematically:

```
output = activation(w₁x₁ + w₂x₂ + ... + wₙxₙ + b)
```

Where:
- x₁, x₂, ..., xₙ are the inputs
- w₁, w₂, ..., wₙ are the weights
- b is the bias
- activation is a function we'll discuss soon

```python exec
id: 02-neural-networks-complete-introduction-page-1-11
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
```

### Activation Functions

Activation functions introduce **non-linearity** into the network. Without them, a neural network would just be a series of linear operations, which can only solve simple linear problems.

#### Common Activation Functions:

1. **Sigmoid**: Squashes values between 0 and 1
   - Formula: σ(x) = 1 / (1 + e^(-x))
   - Good for: Binary classification (yes/no problems)

2. **ReLU (Rectified Linear Unit)**: Returns x if x > 0, otherwise 0
   - Formula: ReLU(x) = max(0, x)
   - Good for: Hidden layers (most popular choice)

3. **Tanh**: Squashes values between -1 and 1
   - Formula: tanh(x) = (e^x - e^(-x)) / (e^x + e^(-x))
   - Good for: Hidden layers

```python exec
id: 02-neural-networks-complete-introduction-page-1-12
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
```

```python exec
id: 02-neural-networks-complete-introduction-page-1-13
# Now let's add activation to our neuron

def neuron_with_activation(inputs, weights, bias, activation='sigmoid'):
    """
    A complete neuron with activation function
    """
    # Weighted sum
    z = np.dot(inputs, weights) + bias

    # Apply activation
    if activation == 'sigmoid':
        return sigmoid(z)
    elif activation == 'relu':
        return relu(z)
    elif activation == 'tanh':
        return tanh(z)
    else:
        return z  # Linear (no activation)

# Test with different activations
inputs = np.array([1.0, 2.0, 3.0])
weights = np.array([0.5, -0.3, 0.8])
bias = 1.0

print("Same inputs as before:")
print(f"Inputs: {inputs}")
print(f"Weights: {weights}")
print(f"Bias: {bias}\n")

print("With different activations:")
print(f"Sigmoid output: {neuron_with_activation(inputs, weights, bias, 'sigmoid'):.3f}")
print(f"ReLU output: {neuron_with_activation(inputs, weights, bias, 'relu'):.3f}")
print(f"Tanh output: {neuron_with_activation(inputs, weights, bias, 'tanh'):.3f}")
```

---

## Part 3: Building a Neural Network Layer

A **layer** is a collection of neurons that all receive the same inputs but have different weights.

If we have:
- 3 input features
- 4 neurons in the layer

Then we need:
- A weight matrix of shape (3, 4) - one column of weights for each neuron
- A bias vector of shape (4,) - one bias for each neuron

The computation for a layer is:

```
Z = X @ W + b
A = activation(Z)
```

Where:
- X is the input matrix
- W is the weight matrix
- b is the bias vector
- Z is the weighted sum (before activation)
- A is the activation output

```python exec
id: 02-neural-networks-complete-introduction-page-1-14
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
```

### Building a Multi-Layer Network

Now we can stack multiple layers! Let's build a network with:
- Input: 3 features
- Hidden layer 1: 4 neurons (ReLU activation)
- Hidden layer 2: 3 neurons (ReLU activation)
- Output layer: 2 neurons (Sigmoid activation for binary classification)

```python exec
id: 02-neural-networks-complete-introduction-page-1-15
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
```

---

## Part 4: Loss Functions - Measuring Our Mistakes

A **loss function** (or **cost function**) measures how wrong our predictions are. The goal of training is to minimize this loss.

### Common Loss Functions:

1. **Mean Squared Error (MSE)**: For regression
   - Formula: MSE = (1/n) Σ(y_true - y_pred)²

2. **Binary Cross-Entropy**: For binary classification
   - Formula: BCE = -(1/n) Σ[y·log(ŷ) + (1-y)·log(1-ŷ)]
   - Where y is the true label (0 or 1) and ŷ is the predicted probability

3. **Categorical Cross-Entropy**: For multi-class classification
   - Similar to binary cross-entropy but for multiple classes

```python exec
id: 02-neural-networks-complete-introduction-page-1-16
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
```

```python exec
id: 02-neural-networks-complete-introduction-page-1-17
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

## Looking back

Before leaving this page, a sentence on each. What you write stays on this device.

```reflect
- Something you expected before running a cell that turned out differently
- The one idea from this page you could explain to someone else now
- Something you would change or try next, if there were time
- A question this page raised for you that it did not answer. Bring it to the next session; these questions are where the next session starts.
```
