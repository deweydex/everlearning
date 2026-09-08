---
title: "Understanding Backpropagation Through Data (1 of 4)"
slug: 02-backpropagation-through-data-page-1
course: ai-and-ml-foundations
course_title: "AI and ML Foundations"
series: 4-learning-a-line
series_title: "Learning a Line"
version: 2026.09.06.1
---

# Understanding Backpropagation Through Data

This tutorial builds your understanding of how neural networks learn by starting with concrete, visual problems and progressively revealing the mathematical structure underneath. We begin by fitting a line to noisy measurements, move to classifying colorful clusters in 2D space where you can see decision boundaries form, and finally scale to recognizing handwritten digits.

Throughout, we focus on one central question: how do we adjust our model's parameters to reduce prediction error? The answer — backpropagation — turns out to be the chain rule applied systematically through a network's layers.

```python exec
id: 02-backpropagation-through-data-page-1-1
import random
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np  # For mesh grids in 3D plots
```

## Part 1: Fitting a Line to Noisy Data

Suppose you're tracking a crucial life metric: the relationship between Terry Pratchett books read and witty things said at parties. You've been collecting data points, but there's noise — maybe you were tired at some parties, or the conversations took unexpected turns. Your goal is to find the line that best captures the underlying relationship.

Let's generate some noisy observations where the true relationship is roughly `witty_remarks = 3 * books_read + 5`, but each observation has random variation.

```python exec
id: 02-backpropagation-through-data-page-1-2
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
```

### Defining the Loss Function

How do we measure how well a line fits our data? We use a **loss function** — a way to quantify the total error across all data points. The most common choice is **mean squared error** (MSE), which measures the average squared distance between our predictions and the actual values.

For a line defined by `prediction = slope * x + intercept`, the loss is:

$$L = \frac{1}{n} \sum_{i=1}^{n} (y_i - (slope \cdot x_i + intercept))^2$$

Squaring the errors serves two purposes: it makes all errors positive (so they don't cancel out), and it penalizes large errors more heavily than small ones.

```python exec
id: 02-backpropagation-through-data-page-1-3
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
```

### Visualizing the Loss Landscape

The loss function creates a landscape where each point represents a different line (defined by its slope and intercept), and the height at that point represents how poorly that line fits our data. Our goal is to find the lowest point in this landscape — the line with minimal loss.

Let's create a contour plot to visualize this landscape.

```python exec
id: 02-backpropagation-through-data-page-1-4
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
```

### 3D Loss Landscape

Let's visualize the same loss landscape in 3D. This gives us a better sense of the "bowl" shape we're trying to descend.

```python exec
id: 02-backpropagation-through-data-page-1-5
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

### Your turn 1: Gradient Descent for Line Fitting

Now we face the central question: how do we find the lowest point in the loss landscape? The answer is **gradient descent** — we compute the direction of steepest descent and take small steps in that direction.

The gradient tells us how the loss changes when we adjust each parameter. For our line, we need two gradients:
- How does loss change with respect to slope?
- How does loss change with respect to intercept?

These gradients can be computed by taking partial derivatives of the loss function. For mean squared error with a linear model:

$$\frac{\partial L}{\partial slope} = \frac{-2}{n} \sum_{i=1}^{n} x_i (y_i - prediction_i)$$

$$\frac{\partial L}{\partial intercept} = \frac{-2}{n} \sum_{i=1}^{n} (y_i - prediction_i)$$

**What to try:** Write pseudocode describing how to update the slope and intercept using these gradients.

**Pseudocode:**

*(Write your pseudocode here. Describe the process of computing gradients, then updating parameters.)*

```python exec
id: 02-backpropagation-through-data-page-1-6
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

### 3D View of the Clusters

Let's add a third dimension (confidence/activation strength) to visualize how the network will need to separate these clusters in activation space.

**Test your implementation:**

```python exec
id: 02-backpropagation-through-data-page-1-7
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
```

### Visualizing the Gradient Descent Path

Let's plot the path that gradient descent took through the loss landscape. This shows how the algorithm navigates from its initial guess toward the optimal parameters.

```python exec
id: 02-backpropagation-through-data-page-1-8
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
```

## Looking back

Before leaving this page, a sentence on each. What you write stays on this device.

```reflect
- Something you expected before running a cell that turned out differently
- The one idea from this page you could explain to someone else now
- Something you would change or try next, if there were time
- A question this page raised for you that it did not answer. Bring it to the next session; these questions are where the next session starts.
```
