---
title: "02-backpropagation-through-data-page-3 (3 of 4)"
slug: 02-backpropagation-through-data-page-3
course: ai-and-ml-foundations
course_title: "AI and ML Foundations"
series: 4-learning-a-line
series_title: "Learning a Line"
version: 2026.09.06.1
---

Before starting this page, run the cell below. It repeats the imports and definitions from the earlier pages that this page uses.

```python exec
id: 02-backpropagation-through-data-page-3-setup
import random
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np  # For mesh grids in 3D plots
import numpy as np

import random
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np  # For mesh grids in 3D plots

# Generate noisy data
random.seed(42)
true_slope = 3
true_intercept = 5

books_read = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
witty_remarks = [true_slope * b + true_intercept + random.gauss(0, 2) for b in books_read]

# Plot the data
plt.figure(figsize=(10, 6))
plt.scatter(books_read, witty_remarks, c='steelblue', s=100, alpha=0.7, edgecolors='black')
plt.xlabel('Terry Pratchett Books Read', fontsize=12)
plt.ylabel('Witty Remarks at Parties', fontsize=12)
plt.title('Noisy Observations: Pratchett Books vs Party Wit', fontsize=14)
plt.grid(True, alpha=0.3)
plt.show()

print(f"True relationship: witty_remarks = {true_slope} * books_read + {true_intercept}")
print(f"Data points: {list(zip(books_read, [round(w, 1) for w in witty_remarks]))}")

def compute_loss(books_read, witty_remarks, slope, intercept):
    """
    Compute mean squared error for a line.

    Args:
        books_read: list of x values
        witty_remarks: list of y values
        slope: current slope parameter
        intercept: current intercept parameter

    Returns:
        float: mean squared error
    """
    total_error = 0
    for h, s in zip(books_read, witty_remarks):
        prediction = slope * h + intercept
        error = s - prediction
        total_error += error ** 2
    return total_error / len(books_read)

# Try a few different lines
test_lines = [
    (5, 60),   # too shallow
    (10, 50),  # close to true
    (15, 40),  # too steep
]

for slope, intercept in test_lines:
    loss = compute_loss(books_read, witty_remarks, slope, intercept)
    print(f"Line: score = {slope} * books_read + {intercept}  →  Loss: {loss:.2f}")

# Create grid of slope and intercept values
slopes = [s * 0.5 for s in range(10, 31)]  # 5 to 15
intercepts = [i * 2 for i in range(20, 41)]  # 40 to 80

# Compute loss for each combination
loss_grid = []
for intercept in intercepts:
    row = []
    for slope in slopes:
        loss = compute_loss(books_read, witty_remarks, slope, intercept)
        row.append(loss)
    loss_grid.append(row)

# Plot contours
fig, ax = plt.subplots(figsize=(12, 8))
contour = ax.contour(slopes, intercepts, loss_grid, levels=20, cmap='viridis')
ax.clabel(contour, inline=True, fontsize=8)
ax.set_xlabel('Slope', fontsize=12)
ax.set_ylabel('Intercept', fontsize=12)
ax.set_title('Loss Landscape: Each Point is a Different Line', fontsize=14)
ax.plot(true_slope, true_intercept, 'r*', markersize=20, label='True Parameters')
ax.legend(fontsize=12)
plt.colorbar(contour, label='Loss (MSE)')
plt.show()

print("The red star shows the true parameters we used to generate the data.")
print("Notice how the loss increases as we move away from this optimal point.")

from mpl_toolkits.mplot3d import Axes3D

# Create 3D plot
fig = plt.figure(figsize=(14, 6))

# Left: 3D surface
ax1 = fig.add_subplot(121, projection='3d')

# Convert lists to 2D arrays for surface plot
import numpy as np
slopes_array = np.array(slopes)
intercepts_array = np.array(intercepts)
slopes_grid, intercepts_grid = np.meshgrid(slopes_array, intercepts_array)
loss_grid_array = np.array(loss_grid)

surf = ax1.plot_surface(slopes_grid, intercepts_grid, loss_grid_array, cmap='viridis',
                        alpha=0.8, edgecolor='none', antialiased=True)
ax1.plot([true_slope], [true_intercept], [compute_loss(books_read, witty_remarks, true_slope, true_intercept)],
         'r*', markersize=20, label='True Parameters')
ax1.set_xlabel('Slope', fontsize=11)
ax1.set_ylabel('Intercept', fontsize=11)
ax1.set_zlabel('Loss (MSE)', fontsize=11)
ax1.set_title('3D Loss Landscape', fontsize=13)
ax1.view_init(elev=20, azim=45)
fig.colorbar(surf, ax=ax1, shrink=0.5, aspect=5)

# Right: Different viewing angle
ax2 = fig.add_subplot(122, projection='3d')
surf2 = ax2.plot_surface(slopes_grid, intercepts_grid, loss_grid_array, cmap='viridis',
                         alpha=0.8, edgecolor='none', antialiased=True)
ax2.plot([true_slope], [true_intercept], [compute_loss(books_read, witty_remarks, true_slope, true_intercept)],
         'r*', markersize=20, label='True Parameters')
ax2.set_xlabel('Slope', fontsize=11)
ax2.set_ylabel('Intercept', fontsize=11)
ax2.set_zlabel('Loss (MSE)', fontsize=11)
ax2.set_title('3D Loss Landscape (Different Angle)', fontsize=13)
ax2.view_init(elev=30, azim=135)
fig.colorbar(surf2, ax=ax2, shrink=0.5, aspect=5)

plt.tight_layout()
plt.show()

print("The red star marks the true parameters that generated our noisy data.")
print("Notice how the loss increases as we move away from this optimal point in any direction.")

def gradient_descent_line(books_read, witty_remarks, initial_slope, initial_intercept,
                         learning_rate, epochs):
    """
    Fit a line using gradient descent.

    Args:
        books_read: list of x values
        witty_remarks: list of y values
        initial_slope: starting slope
        initial_intercept: starting intercept
        learning_rate: step size for updates
        epochs: number of iterations

    Returns:
        tuple: (final_slope, final_intercept, history)
    """
    slope = initial_slope
    intercept = initial_intercept
    history = {'slope': [slope], 'intercept': [intercept], 'loss': []}

    # Record initial loss for consistency with slope and intercept history
    initial_loss = compute_loss(books_read, witty_remarks, initial_slope, initial_intercept)
    history['loss'].append(initial_loss)

    n = len(books_read)

    for epoch in range(epochs):
        predictions = []
        errors = []
        for x, y in zip(books_read, witty_remarks):
            # 1. Compute predictions for all data points
            prediction = slope * x + intercept
            predictions.append(prediction)
            # 2. Compute errors (actual - predicted)
            errors.append(y - prediction)

        # 3. Compute gradients using the formulas above
        dL_d_slope_sum = 0
        dL_d_intercept_sum = 0
        for i in range(n):
            dL_d_slope_sum += books_read[i] * errors[i]
            dL_d_intercept_sum += errors[i]

        dL_d_slope = (-2 / n) * dL_d_slope_sum
        dL_d_intercept = (-2 / n) * dL_d_intercept_sum

        # 4. Update slope and intercept
        slope = slope - learning_rate * dL_d_slope
        intercept = intercept - learning_rate * dL_d_intercept

        # 5. Record current loss
        current_loss = compute_loss(books_read, witty_remarks, slope, intercept)
        history['slope'].append(slope)
        history['intercept'].append(intercept)
        history['loss'].append(current_loss)

    return slope, intercept, history

# Start with poor initial guess
final_slope, final_intercept, history = gradient_descent_line(
    books_read, witty_remarks,
    initial_slope=0,
    initial_intercept=70,
    learning_rate=0.01,
    epochs=100
)

print(f"Final line: score = {final_slope:.2f} * books_read + {final_intercept:.2f}")
print(f"True line:  score = {true_slope} * books_read + {true_intercept}")
print(f"Final loss: {history['loss'][-1]:.2f}")

# Plot the fitted line
plt.figure(figsize=(10, 6))
plt.scatter(books_read, witty_remarks, c='steelblue', s=100, alpha=0.7, edgecolors='black', label='Data')
x_line = [0, 9]
y_line = [final_slope * x + final_intercept for x in x_line]
plt.plot(x_line, y_line, 'r-', linewidth=2, label='Fitted Line')
plt.xlabel('Terry Pratchett Books Read', fontsize=12)
plt.ylabel('Witty Remarks at Parties', fontsize=12)
plt.title('Line Fitted by Gradient Descent', fontsize=14)
plt.legend(fontsize=12)
plt.grid(True, alpha=0.3)
plt.show()

# Plot the gradient descent path on the loss landscape
fig = plt.figure(figsize=(18, 12))

# Top left: 2D contour with path
ax1 = plt.subplot(2, 2, 1)
contour = ax1.contour(slopes, intercepts, loss_grid, levels=20, cmap='viridis', alpha=0.6)
ax1.clabel(contour, inline=True, fontsize=8)
ax1.plot(history['slope'], history['intercept'], 'r.-', linewidth=2, markersize=8, label='GD Path')
ax1.plot(history['slope'][0], history['intercept'][0], 'go', markersize=12, label='Start')
ax1.plot(history['slope'][-1], history['intercept'][-1], 'r*', markersize=15, label='End')
ax1.set_xlabel('Slope', fontsize=12)
ax1.set_ylabel('Intercept', fontsize=12)
ax1.set_title('2D View: Path Through Parameter Space', fontsize=13)
ax1.legend(fontsize=11)
ax1.grid(True, alpha=0.3)

# Top right: Loss over time
ax2 = plt.subplot(2, 2, 2)
ax2.plot(history['loss'], linewidth=2, color='crimson')
ax2.set_xlabel('Epoch', fontsize=12)
ax2.set_ylabel('Loss (MSE)', fontsize=12)
ax2.set_title('Loss Decreasing Over Time', fontsize=13)
ax2.grid(True, alpha=0.3)

# Bottom left: 3D surface with path (angle 1)
ax3 = plt.subplot(2, 2, 3, projection='3d')
surf = ax3.plot_surface(slopes_grid, intercepts_grid, loss_grid_array, cmap='viridis',
                        alpha=0.6, edgecolor='none', antialiased=True)
ax3.plot(history['slope'], history['intercept'], history['loss'],
         'r.-', linewidth=3, markersize=8, label='Gradient Descent Path')
ax3.plot([history['slope'][0]], [history['intercept'][0]], [history['loss'][0]],
         'go', markersize=12, label='Start')
ax3.plot([history['slope'][-1]], [history['intercept'][-1]], [history['loss'][-1]],
         'r*', markersize=15, label='End')
ax3.set_xlabel('Slope', fontsize=10)
ax3.set_ylabel('Intercept', fontsize=10)
ax3.set_zlabel('Loss', fontsize=10)
ax3.set_title('3D View: Descending the Loss Surface', fontsize=12)
ax3.view_init(elev=25, azim=45)
ax3.legend(fontsize=9)

# Bottom right: 3D surface with path (angle 2)
ax4 = plt.subplot(2, 2, 4, projection='3d')
surf2 = ax4.plot_surface(slopes_grid, intercepts_grid, loss_grid_array, cmap='viridis',
                         alpha=0.6, edgecolor='none', antialiased=True)
ax4.plot(history['slope'], history['intercept'], history['loss'],
         'r.-', linewidth=3, markersize=8, label='Gradient Descent Path')
ax4.plot([history['slope'][0]], [history['intercept'][0]], [history['loss'][0]],
         'go', markersize=12, label='Start')
ax4.plot([history['slope'][-1]], [history['intercept'][-1]], [history['loss'][-1]],
         'r*', markersize=15, label='End')
ax4.set_xlabel('Slope', fontsize=10)
ax4.set_ylabel('Intercept', fontsize=10)
ax4.set_zlabel('Loss', fontsize=10)
ax4.set_title('3D View: Side Angle', fontsize=12)
ax4.view_init(elev=10, azim=135)
ax4.legend(fontsize=9)

plt.tight_layout()
plt.show()

print(f"Loss decreased from {history['loss'][0]:.2f} to {history['loss'][-1]:.2f}")
print(f"Final parameters: slope = {history['slope'][-1]:.2f}, intercept = {history['intercept'][-1]:.2f}")
print(f"True parameters: slope = {true_slope}, intercept = {true_intercept}")

def generate_gaussian_clusters(n_points=50):
    """
    Generate three types of coffee shops in 2D space.

    Returns:
        tuple: (points, labels) where points is list of [ambiance, pretentiousness] and labels is list of 0, 1, 2
    """
    random.seed(42)

    # Coffee shop archetypes
    centers = [
        [2, 2],   # Practical cafés
        [6, 3],   # Hipster havens
        [4, 7],   # Corporate chains
    ]

    points = []
    labels = []

    for cluster_id, center in enumerate(centers):
        for _ in range(n_points):
            x = center[0] + random.gauss(0, 0.8)
            y = center[1] + random.gauss(0, 0.8)
            points.append([x, y])
            labels.append(cluster_id)

    return points, labels

# Generate and visualize
points, labels = generate_gaussian_clusters()

plt.figure(figsize=(10, 8))
colors = ['red', 'blue', 'green']
for cluster_id in range(3):
    cluster_points = [p for p, l in zip(points, labels) if l == cluster_id]
    xs = [p[0] for p in cluster_points]
    ys = [p[1] for p in cluster_points]
    plt.scatter(xs, ys, c=colors[cluster_id], s=60, alpha=0.6,
               edgecolors='black', linewidth=0.5, label=f'Type {cluster_id}')

plt.xlabel('Ambiance Score', fontsize=12)
plt.ylabel('Menu Pretentiousness', fontsize=12)
plt.title('Three Types of Coffee Shops', fontsize=14)
plt.legend(fontsize=12)
plt.grid(True, alpha=0.3)
plt.show()

print(f"Total points: {len(points)}")
print(f"Classes: {set(labels)}")

def relu(x):
    """
    Apply ReLU activation.

    Args:
        x: single number or list of numbers

    Returns:
        Activated value(s)
    """
    # TODO: Implement ReLU
    pass

# Test cases
test_values = [-2, -0.5, 0, 0.5, 2]
print("Testing ReLU:")
for val in test_values:
    result = relu(val)
    print(f"  relu({val:4.1f}) = {result}")

# Expected: relu(-2) = 0, relu(-0.5) = 0, relu(0) = 0, relu(0.5) = 0.5, relu(2) = 2

def softmax(values):
    """
    Convert values to probabilities using softmax.

    Args:
        values: list of numbers

    Returns:
        list of probabilities that sum to 1
    """
    # TODO: Implement softmax with numerical stability
    pass

# Test cases
test_inputs = [
    [1, 2, 3],
    [0, 0, 0],
    [100, 200, 300],  # Test numerical stability
]

print("Testing Softmax:")
for vals in test_inputs:
    probs = softmax(vals)
    print(f"  softmax({vals}) = {[round(p, 4) for p in probs]}")
    print(f"    Sum: {sum(probs):.6f}")

# Expected: all probabilities should be between 0 and 1, and sum to 1.0

def dot_product(inputs, weights, bias):
    """
    Compute weighted sum of inputs plus bias.

    Args:
        inputs: list of input values
        weights: list of weight values (same length as inputs)
        bias: bias term

    Returns:
        float: dot product result
    """
    # TODO: Implement dot product
    pass

# Test cases
test_cases = [
    ([1, 2, 3], [4, 5, 6], 0),    # Expected: 1*4 + 2*5 + 3*6 = 32
    ([1, 0, 1], [2, 3, 2], 1),    # Expected: 1*2 + 0*3 + 1*2 + 1 = 5
    ([0.5, 0.5], [1, -1], 0),     # Expected: 0.5*1 + 0.5*(-1) = 0
]

print("Testing Dot Product:")
for inputs, weights, bias in test_cases:
    result = dot_product(inputs, weights, bias)
    print(f"  dot({inputs}, {weights}, {bias}) = {result}")

def initialize_network():
    """
    Create random weights and biases for a 2->4->3 network.

    Returns:
        dict: network parameters
    """
    random.seed(42)

    # Hidden layer: 2 inputs -> 4 neurons
    hidden_weights = [[random.gauss(0, 0.5) for _ in range(2)] for _ in range(4)]
    hidden_biases = [random.gauss(0, 0.5) for _ in range(4)]

    # Output layer: 4 inputs -> 3 neurons
    output_weights = [[random.gauss(0, 0.5) for _ in range(4)] for _ in range(3)]
    output_biases = [random.gauss(0, 0.5) for _ in range(3)]

    return {
        'hidden_weights': hidden_weights,
        'hidden_biases': hidden_biases,
        'output_weights': output_weights,
        'output_biases': output_biases,
    }

def forward_pass(point, network):
    """
    Run forward pass through 2->4->3 network.

    Args:
        point: [x, y] coordinates
        network: dict with weights and biases

    Returns:
        list: output probabilities for 3 classes
    """
    # Hidden layer
    hidden = []
    for neuron_idx in range(4):
        z = dot_product(point,
                       network['hidden_weights'][neuron_idx],
                       network['hidden_biases'][neuron_idx])
        hidden.append(relu(z))

    # Output layer
    output_logits = []
    for neuron_idx in range(3):
        z = dot_product(hidden,
                       network['output_weights'][neuron_idx],
                       network['output_biases'][neuron_idx])
        output_logits.append(z)

    return softmax(output_logits)

# Test the forward pass
network = initialize_network()
test_point = [3.0, 4.0]
predictions = forward_pass(test_point, network)

print(f"Point: {test_point}")
print(f"Predictions: {[round(p, 4) for p in predictions]}")
print(f"Predicted class: {predictions.index(max(predictions))}")

def cross_entropy_loss(predictions, true_label):
    """
    Compute cross-entropy loss for a single example.

    Args:
        predictions: list of probabilities
        true_label: integer label (0, 1, or 2)

    Returns:
        float: loss value
    """
    # Add small epsilon to avoid log(0)
    epsilon = 1e-10
    return -math.log(predictions[true_label] + epsilon)

# Test cross-entropy
test_cases = [
    ([0.7, 0.2, 0.1], 0),  # Confident and correct
    ([0.1, 0.2, 0.7], 0),  # Confident and wrong
    ([0.33, 0.33, 0.34], 0),  # Uncertain
]

print("Testing Cross-Entropy Loss:")
for probs, label in test_cases:
    loss = cross_entropy_loss(probs, label)
    print(f"  Predictions: {probs}, True label: {label} → Loss: {loss:.4f}")
```

## Part 3: The Chain Rule and Backpropagation

Now we reach the heart of how neural networks learn. To improve our network, we need to know: *how does changing each weight affect the loss?* The answer comes from the **chain rule** — a fundamental concept from calculus.

Consider a tiny network with just 2 inputs, 2 hidden neurons, and 3 outputs:

```
Input:  x₀=0.5, x₁=0.8
Hidden: h₀=relu(w₀₀*x₀ + w₀₁*x₁ + b₀)
        h₁=relu(w₁₀*x₀ + w₁₁*x₁ + b₁)
Output: [y₀, y₁, y₂] = softmax([w'₀₀*h₀ + w'₀₁*h₁ + b'₀, ...])
Loss:   L = -log(y_correct)
```

How does changing hidden weight `w₀₀` affect the loss? The loss depends on the output, which depends on the hidden layer, which depends on `w₀₀`. We need to trace this chain backwards.

### Your turn 5: Hand-Calculate Gradients

Let's work through a concrete example by hand. Consider this tiny 2→2→3 network with specific values:

**Given:**
- Input: `x = [0.5, 0.8]`
- Hidden weights: `w_h = [[1.0, 0.5], [-0.5, 1.0]]`  (2 neurons, 2 weights each)
- Hidden biases: `b_h = [0.2, -0.1]`
- Output weights: `w_o = [[0.3, -0.2], [0.1, 0.4], [-0.2, 0.3]]`  (3 neurons, 2 weights each)
- Output biases: `b_o = [0, 0, 0]`
- True label: `1`

**What to try:**

1. Compute the forward pass step by step:
   - Calculate hidden layer pre-activations (before ReLU)
   - Apply ReLU to get hidden activations
   - Calculate output layer logits
   - Apply softmax to get probabilities
   - Calculate the cross-entropy loss

2. Calculate the gradient of loss with respect to one hidden weight (e.g., `w_h[0][0]`):
   - Start from the loss
   - Work backwards through the chain: loss → output → hidden → weight

Show your work in the cell below.

**Your calculations:**

*(Show your step-by-step calculations here)*

Forward pass:

Backward pass (chain rule):

```python exec
id: 02-backpropagation-through-data-page-3-1
# Verify your hand calculations
def verify_gradient_calculation():
    """Check your hand-calculated gradient against numerical gradient."""
    # Network parameters from exercise
    x = [0.5, 0.8]
    w_h = [[1.0, 0.5], [-0.5, 1.0]]
    b_h = [0.2, -0.1]
    w_o = [[0.3, -0.2], [0.1, 0.4], [-0.2, 0.3]]
    b_o = [0, 0, 0]
    true_label = 1

    # Helper to compute loss for given network
    def compute_loss_for_network(w_h_modified):
        # Hidden layer
        hidden = []
        for i in range(2):
            z = dot_product(x, w_h_modified[i], b_h[i])
            hidden.append(relu(z))

        # Output layer
        logits = []
        for i in range(3):
            z = dot_product(hidden, w_o[i], b_o[i])
            logits.append(z)

        probs = softmax(logits)
        return cross_entropy_loss(probs, true_label), probs, hidden

    # Compute base loss
    loss, probs, hidden = compute_loss_for_network(w_h)

    print(f"Forward pass results:")
    print(f"  Hidden activations: {[round(h, 4) for h in hidden]}")
    print(f"  Output probabilities: {[round(p, 4) for p in probs]}")
    print(f"  Loss: {loss:.4f}")
    print()

    # Numerical gradient for w_h[0][0]
    epsilon = 1e-5
    w_h_plus = [row[:] for row in w_h]
    w_h_plus[0][0] += epsilon
    loss_plus, _, _ = compute_loss_for_network(w_h_plus)

    numerical_grad = (loss_plus - loss) / epsilon

    print(f"Numerical gradient of L with respect to w_h[0][0]: {numerical_grad:.6f}")
    print()
    print("Compare this to your hand-calculated gradient!")

verify_gradient_calculation()
```

### Understanding Backpropagation

What you just calculated by hand is exactly what backpropagation does automatically for every weight in the network. The algorithm works backwards from the loss, applying the chain rule at each layer.

For a network with layers L → M → N:

1. **Output layer gradients:** How does loss change with respect to output weights?
   $$\frac{\partial L}{\partial w^{out}} = \frac{\partial L}{\partial y} \cdot \frac{\partial y}{\partial w^{out}}$$

2. **Hidden layer gradients:** How does loss change with respect to hidden weights?
   $$\frac{\partial L}{\partial w^{hidden}} = \frac{\partial L}{\partial y} \cdot \frac{\partial y}{\partial h} \cdot \frac{\partial h}{\partial w^{hidden}}$$

Notice how the chain gets longer as we move backwards through the network. Each ∂ term can be computed using the derivatives of our activation functions and the values we stored during the forward pass.

The beauty of backpropagation is that it computes all these gradients efficiently in one backwards sweep, reusing intermediate results.

### Implementing Backpropagation

Below is a complete implementation of backpropagation for our 2→4→3 network. Read through the code carefully — every line corresponds to applying the chain rule at a specific layer. The comments show which derivative we're computing at each step.

```python exec
id: 02-backpropagation-through-data-page-3-2
def forward_pass_with_history(point, network):
    """
    Forward pass that saves intermediate values needed for backprop.

    Returns:
        tuple: (predictions, history_dict)
    """
    history = {}
    history['input'] = point

    # Hidden layer
    hidden_z = []  # Pre-activation
    hidden_a = []  # Post-activation
    for i in range(4):
        z = dot_product(point, network['hidden_weights'][i], network['hidden_biases'][i])
        hidden_z.append(z)
        hidden_a.append(relu(z))

    history['hidden_z'] = hidden_z
    history['hidden_a'] = hidden_a

    # Output layer
    output_z = []  # Logits before softmax
    for i in range(3):
        z = dot_product(hidden_a, network['output_weights'][i], network['output_biases'][i])
        output_z.append(z)

    predictions = softmax(output_z)
    history['output_z'] = output_z
    history['predictions'] = predictions

    return predictions, history

def backpropagation(history, true_label, network):
    """
    Compute gradients using backpropagation.

    Args:
        history: saved forward pass values
        true_label: correct class (0, 1, or 2)
        network: current parameters

    Returns:
        dict: gradients for all weights and biases
    """
    gradients = {}

    # STEP 1: Output layer gradients
    # For cross-entropy with softmax, the gradient is simply (prediction - target)
    output_errors = history['predictions'][:]
    output_errors[true_label] -= 1  # derivative of cross-entropy loss with softmax

    # Gradients for output weights: error * hidden_activation
    output_weight_grads = []
    output_bias_grads = []
    for i in range(3):
        weight_grad = [output_errors[i] * h for h in history['hidden_a']]
        output_weight_grads.append(weight_grad)
        output_bias_grads.append(output_errors[i])

    gradients['output_weights'] = output_weight_grads
    gradients['output_biases'] = output_bias_grads

    # STEP 2: Backpropagate error to hidden layer
    # Error at hidden neuron = sum of (output_error * weight_from_that_hidden_neuron)
    hidden_errors = [0] * 4
    for h_idx in range(4):
        error = 0
        for o_idx in range(3):
            error += output_errors[o_idx] * network['output_weights'][o_idx][h_idx]
        hidden_errors[h_idx] = error

    # STEP 3: Apply ReLU derivative
    # ReLU derivative is 1 if input > 0, else 0
    for i in range(4):
        if history['hidden_z'][i] <= 0:
            hidden_errors[i] = 0

    # STEP 4: Hidden layer weight gradients
    hidden_weight_grads = []
    hidden_bias_grads = []
    for i in range(4):
        weight_grad = [hidden_errors[i] * inp for inp in history['input']]
        hidden_weight_grads.append(weight_grad)
        hidden_bias_grads.append(hidden_errors[i])

    gradients['hidden_weights'] = hidden_weight_grads
    gradients['hidden_biases'] = hidden_bias_grads

    return gradients
```

### Your turn 6: Training Loop

Now you have all the pieces to train the network:
1. Forward pass (compute predictions and save history)
2. Backpropagation (compute gradients)
3. Parameter update (adjust weights using gradients)

**What to try:** Implement the training loop that ties these pieces together. For each epoch:
- Loop through all training examples
- For each example, compute gradients and update parameters
- Track the average loss and accuracy

**Pseudocode:**

*(Write your pseudocode for the training loop here)*

```python exec
id: 02-backpropagation-through-data-page-3-3
def train_network(points, labels, epochs, learning_rate):
    """
    Train the network using gradient descent.

    Args:
        points: list of [x, y] coordinates
        labels: list of class labels
        epochs: number of training iterations
        learning_rate: step size for updates

    Returns:
        tuple: (trained_network, training_history)
    """
    network = initialize_network()
    history = {'loss': [], 'accuracy': []}

    for epoch in range(epochs):
        # TODO: Implement training loop
        # 1. For each training example:
        #    a. Forward pass with history
        #    b. Compute loss
        #    c. Backpropagation
        #    d. Update weights (weight -= learning_rate * gradient)
        # 2. Compute average loss and accuracy for this epoch
        # 3. Store in history

        pass

    return network, history
```

**Test your training loop:**

```python exec
id: 02-backpropagation-through-data-page-3-4
# Train the network
trained_network, train_history = train_network(
    points, labels,
    epochs=200,
    learning_rate=0.1
)

print(f"Initial loss: {train_history['loss'][0]:.4f}")
print(f"Final loss: {train_history['loss'][-1]:.4f}")
print(f"Final accuracy: {train_history['accuracy'][-1]:.2%}")
```

### Your turn 7: Visualizing Training Progress

Create two plots showing how the network improved during training:
1. Loss over time (should decrease)
2. Accuracy over time (should increase)

**What to try:** Implement the plotting function.

```python exec
id: 02-backpropagation-through-data-page-3-5
def plot_training_progress(history):
    """
    Visualize loss and accuracy curves.

    Args:
        history: dict with 'loss' and 'accuracy' lists
    """
    # TODO: Create side-by-side plots
    # Left plot: Loss vs Epoch
    # Right plot: Accuracy vs Epoch
    pass

plot_training_progress(train_history)
```

### Your turn 8: Visualizing Decision Boundaries

The real power of visualization comes from seeing what the network learned. We can create a heatmap showing which class the network predicts for every point in 2D space, then overlay our actual data points.

We'll create multiple views: the final decision boundaries, and an animated version showing how they evolved during training.

**What to try:** Create visualizations of the decision boundaries.

```python exec
id: 02-backpropagation-through-data-page-3-6
def visualize_decision_boundaries(network, points, labels, title="Decision Boundaries"):
    """
    Show learned decision boundaries with colorful regions.

    Args:
        network: trained network
        points: training data points
        labels: training data labels
        title: plot title
    """
    # Create a fine grid covering the space
    x_min, x_max = 0, 8
    y_min, y_max = 0, 9
    h = 0.1  # step size

    xx_list = []
    yy_list = []
    x = x_min
    while x <= x_max:
        xx_list.append(x)
        x += h

    y = y_min
    while y <= y_max:
        yy_list.append(y)
        y += h

    # Predict for each point in grid
    Z = []
    for y_val in yy_list:
        row = []
        for x_val in xx_list:
            probs = network.forward([x_val, y_val])
            pred_class = probs.index(max(probs))
            row.append(pred_class)
        Z.append(row)

    # Create the plot
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 7))

    # Left: Decision regions with data points
    colors = ['#FFB6C1', '#ADD8E6', '#90EE90']  # Light red, blue, green

    # Plot decision regions
    for i, y_val in enumerate(yy_list):
        for j, x_val in enumerate(xx_list):
            ax1.plot(x_val, y_val, 's', color=colors[Z[i][j]],
                    markersize=3, alpha=0.3)

    # Plot actual data points on top
    colors_dark = ['red', 'blue', 'green']
    for cluster_id in range(3):
        cluster_points = [p for p, l in zip(points, labels) if l == cluster_id]
        xs = [p[0] for p in cluster_points]
        ys = [p[1] for p in cluster_points]
        ax1.scatter(xs, ys, c=colors_dark[cluster_id], s=80, alpha=0.8,
                   edgecolors='black', linewidth=1.5, label=f'Cluster {cluster_id}')

    ax1.set_xlabel('Ambiance Score', fontsize=12)
    ax1.set_ylabel('Menu Pretentiousness', fontsize=12)
    ax1.set_title(f'{title}: Coffee Shop Types', fontsize=14)
    ax1.legend(fontsize=11)
    ax1.set_xlim(x_min, x_max)
    ax1.set_ylim(y_min, y_max)
    ax1.grid(True, alpha=0.3)

    # Right: Confidence heatmap
    confidence_map = []
    for y_val in yy_list:
        row = []
        for x_val in xx_list:
            probs = network.forward([x_val, y_val])
            max_confidence = max(probs)
            row.append(max_confidence)
        confidence_map.append(row)

    # Plot confidence as heatmap
    im = ax2.imshow(confidence_map, extent=[x_min, x_max, y_min, y_max],
                    origin='lower', cmap='YlOrRd', alpha=0.6, aspect='auto')

    # Overlay data points
    for cluster_id in range(3):
        cluster_points = [p for p, l in zip(points, labels) if l == cluster_id]
        xs = [p[0] for p in cluster_points]
        ys = [p[1] for p in cluster_points]
        ax2.scatter(xs, ys, c=colors_dark[cluster_id], s=80, alpha=0.8,
                   edgecolors='black', linewidth=1.5)

    ax2.set_xlabel('Ambiance Score', fontsize=12)
    ax2.set_ylabel('Menu Pretentiousness', fontsize=12)
    ax2.set_title(f'{title}: Prediction Confidence', fontsize=14)
    plt.colorbar(im, ax=ax2, label='Confidence')
    ax2.set_xlim(x_min, x_max)
    ax2.set_ylim(y_min, y_max)
    ax2.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.show()

visualize_decision_boundaries(trained_network, points, labels)
```

### Animated Training Process

Let's create snapshots showing how the decision boundaries evolved during training. This reveals how the network progressively learned to separate the clusters.

```python exec
id: 02-backpropagation-through-data-page-3-7
def visualize_training_snapshots(points, labels, epochs_to_show=[0, 3, 7, 15]):
    """
    Show decision boundaries at different points during training.
    """
    fig, axes = plt.subplots(2, 2, figsize=(16, 14))
    axes = axes.flatten()

    for idx, epoch in enumerate(epochs_to_show):
        # Train a network for this many epochs
        snapshot_network = NeuralNetwork()

        for e in range(epoch):
            for point, label in zip(points, labels):
                probs, history = snapshot_network.forward_with_history(point)
                gradients = snapshot_network.backpropagation(history, label)
                snapshot_network.update_weights(gradients, learning_rate=0.1)

        # Create grid for decision boundary
        x_min, x_max = 0, 8
        y_min, y_max = 0, 9
        h = 0.15

        xx_list = []
        x = x_min
        while x <= x_max:
            xx_list.append(x)
            x += h

        yy_list = []
        y = y_min
        while y <= y_max:
            yy_list.append(y)
            y += h

        # Predict for grid
        Z = []
        for y_val in yy_list:
            row = []
            for x_val in xx_list:
                probs = snapshot_network.forward([x_val, y_val])
                pred_class = probs.index(max(probs))
                row.append(pred_class)
            Z.append(row)

        # Plot
        ax = axes[idx]
        colors = ['#FFB6C1', '#ADD8E6', '#90EE90']

        for i, y_val in enumerate(yy_list):
            for j, x_val in enumerate(xx_list):
                ax.plot(x_val, y_val, 's', color=colors[Z[i][j]],
                       markersize=4, alpha=0.3)

        # Plot data points
        colors_dark = ['red', 'blue', 'green']
        for cluster_id in range(3):
            cluster_points = [p for p, l in zip(points, labels) if l == cluster_id]
            xs = [p[0] for p in cluster_points]
            ys = [p[1] for p in cluster_points]
            ax.scatter(xs, ys, c=colors_dark[cluster_id], s=60, alpha=0.8,
                      edgecolors='black', linewidth=1.5)

        ax.set_xlabel('Ambiance', fontsize=11)
        ax.set_ylabel('Pretentiousness', fontsize=11)
        ax.set_title(f'After Epoch {epoch}', fontsize=13)
        ax.set_xlim(x_min, x_max)
        ax.set_ylim(y_min, y_max)
        ax.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.show()
    print("Notice how the decision boundaries start random and gradually align with the clusters!")

# Show the evolution
visualize_training_snapshots(points, labels, epochs_to_show=[0, 5, 10, 20])
```

### Your turn 9: Interpretation Questions

Now that you've built, trained, and visualized a neural network, reflect on what you've learned:

1. **Loss curve:** Did the loss decrease smoothly or did it have plateaus? What might cause plateaus?

2. **Decision boundaries:** Are the boundaries straight lines or curves? Why?

3. **Learning rate:** What happens if you increase the learning rate to 1.0? What about decreasing it to 0.01?

4. **Hidden layer size:** Try changing the hidden layer from 4 neurons to 2 neurons. How does this affect the decision boundaries?

5. **Chain rule:** In your own words, explain why we need to multiply gradients as we move backwards through the network.

Answer these questions in the cell below, experimenting with the code as needed.

**Your answers:**

1.

2.

3.

4.

5.

### The Complete Training Journey: A Visual Summary

Before we scale to MNIST, let's create one comprehensive visualization showing everything we've learned: the data, the training dynamics, the learned representations, and the final decision boundaries all in one view.

```python exec
id: 02-backpropagation-through-data-page-3-8
def create_comprehensive_visualization(network, points, labels, history):
    """
    Create a comprehensive 6-panel visualization of the complete training process.
    """
    fig = plt.figure(figsize=(20, 12))

    # Panel 1: Training curves (loss and accuracy)
    ax1 = plt.subplot(2, 3, 1)
    ax1_twin = ax1.twinx()

    loss_line = ax1.plot(history['loss'], 'crimson', linewidth=3, label='Loss')
    acc_line = ax1_twin.plot(history['accuracy'], 'forestgreen', linewidth=3,
                             label='Accuracy', linestyle='--')

    ax1.set_xlabel('Epoch', fontsize=12)
    ax1.set_ylabel('Loss', fontsize=12, color='crimson')
    ax1_twin.set_ylabel('Accuracy', fontsize=12, color='forestgreen')
    ax1.set_title('Training Dynamics', fontsize=14, fontweight='bold')
    ax1.tick_params(axis='y', labelcolor='crimson')
    ax1_twin.tick_params(axis='y', labelcolor='forestgreen')
    ax1.grid(True, alpha=0.3)

    # Combine legends
    lines = loss_line + acc_line
    labels_legend = [l.get_label() for l in lines]
    ax1.legend(lines, labels_legend, loc='center right', fontsize=10)

    # Panel 2: Raw data
    ax2 = plt.subplot(2, 3, 2)
    colors_dark = ['red', 'blue', 'green']
    labels_text = ['Practical Cafés', 'Hipster Havens', 'Corporate Chains']
    for cluster_id in range(3):
        cluster_points = [p for p, l in zip(points, labels) if l == cluster_id]
        xs = [p[0] for p in cluster_points]
        ys = [p[1] for p in cluster_points]
        ax2.scatter(xs, ys, c=colors_dark[cluster_id], s=100, alpha=0.7,
                   edgecolors='black', linewidth=2, label=labels_text[cluster_id])
    ax2.set_xlabel('Ambiance Score', fontsize=12)
    ax2.set_ylabel('Menu Pretentiousness', fontsize=12)
    ax2.set_title('Original Data', fontsize=14, fontweight='bold')
    ax2.legend(fontsize=10)
    ax2.grid(True, alpha=0.3)
    ax2.set_xlim(0, 8)
    ax2.set_ylim(0, 9)

    # Panel 3: Decision boundaries
    ax3 = plt.subplot(2, 3, 3)
    x_min, x_max, y_min, y_max = 0, 8, 0, 9
    h = 0.15

    xx_list = []
    x = x_min
    while x <= x_max:
        xx_list.append(x)
        x += h
    yy_list = []
    y = y_min
    while y <= y_max:
        yy_list.append(y)
        y += h

    Z = []
    for y_val in yy_list:
        row = []
        for x_val in xx_list:
            probs = network.forward([x_val, y_val])
            pred_class = probs.index(max(probs))
            row.append(pred_class)
        Z.append(row)

    colors_light = ['#FFB6C1', '#ADD8E6', '#90EE90']
    for i, y_val in enumerate(yy_list):
        for j, x_val in enumerate(xx_list):
            ax3.plot(x_val, y_val, 's', color=colors_light[Z[i][j]],
                    markersize=4, alpha=0.4)

    for cluster_id in range(3):
        cluster_points = [p for p, l in zip(points, labels) if l == cluster_id]
        xs = [p[0] for p in cluster_points]
        ys = [p[1] for p in cluster_points]
        ax3.scatter(xs, ys, c=colors_dark[cluster_id], s=80, alpha=0.9,
                   edgecolors='black', linewidth=2)

    ax3.set_xlabel('Ambiance Score', fontsize=12)
    ax3.set_ylabel('Menu Pretentiousness', fontsize=12)
    ax3.set_title('Learned Decision Boundaries', fontsize=14, fontweight='bold')
    ax3.grid(True, alpha=0.3)
    ax3.set_xlim(x_min, x_max)
    ax3.set_ylim(y_min, y_max)

    # Panel 4: Hidden neuron activations (average)
    ax4 = plt.subplot(2, 3, 4)
    hidden_strengths = [0, 0, 0, 0]

    for point in points:
        for neuron_id in range(4):
            z = dot_product(point, network['hidden_weights'][neuron_id],
                           network['hidden_biases'][neuron_id])
            activation = relu(z)
            hidden_strengths[neuron_id] += activation

    hidden_strengths = [s / len(points) for s in hidden_strengths]

    bars = ax4.bar(['H1', 'H2', 'H3', 'H4'], hidden_strengths,
                   color=['coral', 'skyblue', 'lightgreen', 'plum'],
                   edgecolor='black', linewidth=2, alpha=0.7)
    ax4.set_ylabel('Average Activation', fontsize=12)
    ax4.set_title('Hidden Layer Activity', fontsize=14, fontweight='bold')
    ax4.grid(True, alpha=0.3, axis='y')

    # Panel 5: 3D decision surface
    ax5 = plt.subplot(2, 3, 5, projection='3d')

    # Create confidence surface
    confidence_surface = []
    for y_val in yy_list:
        row = []
        for x_val in xx_list:
            probs = network.forward([x_val, y_val])
            max_conf = max(probs)
            row.append(max_conf)
        confidence_surface.append(row)

    # Create meshgrid for surface
    xx_array = np.array(xx_list)
    yy_array = np.array(yy_list)
    XX, YY = np.meshgrid(xx_array, yy_array)
    ZZ = np.array(confidence_surface)

    surf = ax5.plot_surface(XX, YY, ZZ, cmap='viridis', alpha=0.7,
                           edgecolor='none', antialiased=True)

    # Plot data points above surface
    for cluster_id in range(3):
        cluster_points = [p for p, l in zip(points, labels) if l == cluster_id]
        xs = [p[0] for p in cluster_points]
        ys = [p[1] for p in cluster_points]
        zs = [1.0] * len(xs)  # Place at top
        ax5.scatter(xs, ys, zs, c=colors_dark[cluster_id], s=50, alpha=0.9,
                   edgecolors='black', linewidth=1.5)

    ax5.set_xlabel('Ambiance', fontsize=10)
    ax5.set_ylabel('Pretentiousness', fontsize=10)
    ax5.set_zlabel('Confidence', fontsize=10)
    ax5.set_title('3D Confidence Surface', fontsize=13, fontweight='bold')
    ax5.view_init(elev=25, azim=135)

    # Panel 6: Prediction accuracy by class
    ax6 = plt.subplot(2, 3, 6)

    correct_by_class = [0, 0, 0]
    total_by_class = [0, 0, 0]

    for point, label in zip(points, labels):
        probs = network.forward(point)
        pred = probs.index(max(probs))
        total_by_class[label] += 1
        if pred == label:
            correct_by_class[label] += 1

    accuracy_by_class = [c/t if t > 0 else 0 for c, t in zip(correct_by_class, total_by_class)]

    bars = ax6.bar(labels_text, [a*100 for a in accuracy_by_class],
                   color=colors_dark, edgecolor='black', linewidth=2, alpha=0.7)
    ax6.set_ylabel('Accuracy (%)', fontsize=12)
    ax6.set_title('Per-Class Accuracy', fontsize=14, fontweight='bold')
    ax6.set_ylim(0, 105)
    ax6.grid(True, alpha=0.3, axis='y')

    # Add percentage labels on bars
    for i, (bar, acc) in enumerate(zip(bars, accuracy_by_class)):
        height = bar.get_height()
        ax6.text(bar.get_x() + bar.get_width()/2., height + 2,
                f'{acc*100:.1f}%', ha='center', va='bottom', fontsize=11, fontweight='bold')

    plt.suptitle('Neural Network Training: The Complete Picture',
                fontsize=18, fontweight='bold', y=0.995)
    plt.tight_layout()
    plt.show()

    print("\n" + "="*80)
    print("SUMMARY: Our network successfully learned to classify coffee shops!")
    print("="*80)
    print(f"Final Loss: {history['loss'][-1]:.3f}")
    print(f"Final Accuracy: {history['accuracy'][-1]*100:.1f}%")
    print(f"Training Epochs: {len(history['loss'])}")
    print("\nThe network learned curved decision boundaries by:")
    print("  1. Transforming 2D inputs through 4 hidden neurons")
    print("  2. Each hidden neuron detecting different spatial patterns")
    print("  3. Combining these detections to make the final classification")
    print("="*80)

# Create the comprehensive visualization
create_comprehensive_visualization(trained_network, points, labels, train_history)
```

## Looking back

Before leaving this page, a sentence on each. What you write stays on this device.

```reflect
- Something you expected before running a cell that turned out differently
- The one idea from this page you could explain to someone else now
- Something you would change or try next, if there were time
- A question this page raised for you that it did not answer. Bring it to the next session; these questions are where the next session starts.
```
