---
title: "02-backpropagation-through-data-page-2 (2 of 4)"
slug: 02-backpropagation-through-data-page-2
course: ai-and-ml-foundations
course_title: "AI and ML Foundations"
series: 4-learning-a-line
series_title: "Learning a Line"
version: 2026.09.06.1
---

Before starting this page, run the cell below. It repeats the imports and definitions from the earlier pages that this page uses.

```python exec
id: 02-backpropagation-through-data-page-2-setup
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
```

## Part 2: Classifying Gaussian Clusters in 2D

Now let's move from fitting a line to a classification problem where we can visualize what the network is learning. Imagine you're analyzing coffee shops across a city, measuring them on two dimensions: **ambiance score** (how many vintage typewriters and exposed brick walls) and **menu pretentiousness** (complexity of the coffee naming scheme).

Three distinct types naturally emerge:
- **Cluster 0 (Red):** Practical cafés — decent coffee, minimal fuss
- **Cluster 1 (Blue):** Hipster havens — artisanal everything, bearded baristas
- **Cluster 2 (Green):** Corporate chains — reliable but soulless

Our network needs to learn decision boundaries that separate these coffee shop personalities.

```python exec
id: 02-backpropagation-through-data-page-2-1
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
```

### 3D View of the Clusters

Let's add a third dimension (confidence/activation strength) to visualize how the network will need to separate these clusters in activation space.

```python exec
id: 02-backpropagation-through-data-page-2-2
# Create a 3D visualization with artificial z-axis
fig = plt.figure(figsize=(14, 6))

# Left: 2D view (repeated for comparison)
ax1 = plt.subplot(121)
colors = ['red', 'blue', 'green']
for cluster_id in range(3):
    cluster_points = [p for p, l in zip(points, labels) if l == cluster_id]
    xs = [p[0] for p in cluster_points]
    ys = [p[1] for p in cluster_points]
    ax1.scatter(xs, ys, c=colors[cluster_id], s=60, alpha=0.6,
               edgecolors='black', linewidth=0.5, label=f'Cluster {cluster_id}')
ax1.set_xlabel('Ambiance Score', fontsize=12)
ax1.set_ylabel('Menu Pretentiousness', fontsize=12)
ax1.set_title('2D View', fontsize=14)
ax1.legend(fontsize=12)
ax1.grid(True, alpha=0.3)

# Right: 3D view
ax2 = plt.subplot(122, projection='3d')
for cluster_id in range(3):
    cluster_points = [p for p, l in zip(points, labels) if l == cluster_id]
    xs = [p[0] for p in cluster_points]
    ys = [p[1] for p in cluster_points]
    # Add artificial z-coordinate based on cluster ID for visualization
    zs = [cluster_id * 2 + random.gauss(0, 0.3) for _ in xs]
    ax2.scatter(xs, ys, zs, c=colors[cluster_id], s=60, alpha=0.6,
               edgecolors='black', linewidth=0.5, label=f'Cluster {cluster_id}')

ax2.set_xlabel('Ambiance Score', fontsize=11)
ax2.set_ylabel('Menu Pretentiousness', fontsize=11)
ax2.set_zlabel('Activation Space', fontsize=11)
ax2.set_title('3D View: Clusters in Activation Space', fontsize=13)
ax2.legend(fontsize=11)
ax2.view_init(elev=20, azim=45)

plt.tight_layout()
plt.show()

print("The network learns to map the 2D input space into a higher-dimensional")
print("activation space where the clusters become easier to separate.")
```

### Building a Small Neural Network

To classify these points, we'll build a neural network with:
- **Input layer:** 2 neurons (one for each coordinate)
- **Hidden layer:** 4 neurons with ReLU activation
- **Output layer:** 3 neurons (one for each class) with softmax activation

This is a 2→4→3 network. Before we build the full network, let's implement the individual components we'll need.

### Your turn 2: ReLU Activation

The **ReLU** (Rectified Linear Unit) activation function is defined as:

$$ReLU(x) = \max(0, x)$$

It outputs the input if positive, otherwise zero. This introduces non-linearity into our network, allowing it to learn curved decision boundaries.

**What to try:** Write pseudocode, then implement the ReLU function.

**Pseudocode:**

*(Write your pseudocode here)*

```python exec
id: 02-backpropagation-through-data-page-2-3
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
```

### Your turn 3: Softmax Activation

The **softmax** function converts a list of numbers into probabilities that sum to 1. It's defined as:

$$softmax(x_i) = \frac{e^{x_i}}{\sum_j e^{x_j}}$$

For numerical stability, we subtract the maximum value before exponentiating:

$$softmax(x_i) = \frac{e^{x_i - \max(x)}}{\sum_j e^{x_j - \max(x)}}$$

This prevents overflow when dealing with large numbers.

**What to try:** Write pseudocode, then implement softmax.

**Pseudocode:**

*(Write your pseudocode here)*

```python exec
id: 02-backpropagation-through-data-page-2-4
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
```

### Your turn 4: Dot Product

The fundamental operation in a neural network is the **dot product** between inputs and weights:

$$output = \sum_{i=1}^{n} input_i \times weight_i$$

Plus a bias term:

$$output = bias + \sum_{i=1}^{n} input_i \times weight_i$$

**What to try:** Write pseudocode, then implement the dot product function.

**Pseudocode:**

*(Write your pseudocode here)*

```python exec
id: 02-backpropagation-through-data-page-2-5
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
```

### Forward Pass Through the Network

Now we can build a complete forward pass. Given a 2D point, we:
1. Compute hidden layer activations (4 neurons with ReLU)
2. Compute output layer activations (3 neurons with softmax)

Let's implement this for our 2→4→3 network.

```python exec
id: 02-backpropagation-through-data-page-2-6
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
```

### Visualizing Hidden Neuron Activations

Let's see what each hidden neuron responds to across the input space. This reveals what features each neuron has learned to detect.

```python exec
id: 02-backpropagation-through-data-page-2-7
def visualize_hidden_neurons(network):
    """
    Show what each hidden neuron activates on across the input space.
    """
    # Create grid
    x_min, x_max = 0, 8
    y_min, y_max = 0, 9
    h = 0.2

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

    # Get activations for each hidden neuron
    num_hidden = 4
    activations = [[] for _ in range(num_hidden)]

    for y_val in yy_list:
        for neuron_id in range(num_hidden):
            row = []
            for x_val in xx_list:
                # Compute hidden layer activation for this neuron
                point = [x_val, y_val]
                z = dot_product(point, network['hidden_weights'][neuron_id],
                               network['hidden_biases'][neuron_id])
                activation = relu(z)
                row.append(activation)
            activations[neuron_id].append(row)

    # Plot each neuron's activation map
    fig, axes = plt.subplots(2, 2, figsize=(14, 12))
    axes = axes.flatten()

    for neuron_id in range(4):
        ax = axes[neuron_id]

        # Plot activation heatmap
        im = ax.imshow(activations[neuron_id], extent=[x_min, x_max, y_min, y_max],
                      origin='lower', cmap='hot', aspect='auto')

        ax.set_xlabel('Ambiance', fontsize=11)
        ax.set_ylabel('Pretentiousness', fontsize=11)
        ax.set_title(f'Hidden Neuron {neuron_id} Activation', fontsize=12)
        plt.colorbar(im, ax=ax, label='Activation Strength')
        ax.grid(True, alpha=0.3, color='white', linewidth=0.5)

    plt.tight_layout()
    plt.show()
    print("Each hidden neuron learns to detect different patterns or regions in the input space.")
    print("The output layer combines these activations to make the final classification.")

visualize_hidden_neurons(network)
```

### Cross-Entropy Loss for Classification

For classification, we use **cross-entropy loss**, which measures how different our predicted probabilities are from the true labels. For a single example:

$$L = -\log(p_{correct})$$

where $p_{correct}$ is the probability our network assigned to the correct class.

Why use negative log? When the network is confident and correct ($p_{correct}$ close to 1), the loss is near 0. When confident but wrong ($p_{correct}$ close to 0), the loss becomes very large.

```python exec
id: 02-backpropagation-through-data-page-2-8
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

## Looking back

Before leaving this page, a sentence on each. What you write stays on this device.

```reflect
- Something you expected before running a cell that turned out differently
- The one idea from this page you could explain to someone else now
- Something you would change or try next, if there were time
- A question this page raised for you that it did not answer. Bring it to the next session; these questions are where the next session starts.
```
