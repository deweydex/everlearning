---
title: "Learning a Line — and What That Has to Do with a Neuron"
slug: 01-learning-a-line
course: ai-and-ml-foundations
course_title: "AI and ML Foundations"
series: 4-learning-a-line
series_title: "Learning a Line"
version: 2026.09.06.1
---

# Learning a Line — and What That Has to Do with a Neuron

There is a question that sits at the heart of machine learning: given some data, how does a program figure out the relationship hiding inside it?

We are going to answer that question in the simplest possible setting — fitting a straight line to noisy measurements — and then notice that everything we build along the way is exactly what an artificial neuron does.

By the end we will have written, from scratch, a tiny learning algorithm. We will be able to watch it search for the best parameters, trace the path it takes through the space of all possible lines, and see the loss fall iteration by iteration. More importantly, we will understand *why* each piece is there.

---

**What we need before starting**

This notebook uses `matplotlib` for plots and a small amount of `numpy` for building the visualisation surface. The core learning logic uses only plain Python. If you are running in Google Colab, uncomment the install line in the next cell.

```python exec
id: 01-learning-a-line-1
# Uncomment if running in Google Colab
# (nothing to install here: the libraries load with the page)

# %matplotlib widget enables interactive 3D plots (click-drag to rotate)
# If that causes trouble in your environment, swap it for %matplotlib inline
#%matplotlib widget

import matplotlib.pyplot as plt
import numpy as np
import random
from typing import List, Tuple
```

---

## Part 1: The data

Imagine we are measuring something in the real world — perhaps the distance a spring stretches as we add weight to it, or the time it takes a student to solve a puzzle as they practise more. The underlying relationship is a straight line, but our measurements are imperfect. Every reading has a little noise in it.

Let's generate some data like that. We will pick a line — a true slope and a true bias — and then add a random wobble to each point.

```python exec
id: 01-learning-a-line-2
def generate_noisy_line(
    true_slope: float,         # the slope of the underlying line
    true_bias: float,          # the y-intercept of the underlying line
    num_points: int,           # how many measurements to generate
    noise_scale: float,        # how large the random wobble can be
    x_min: float = 0.0,
    x_max: float = 10.0,
    seed: int = 42,
) -> Tuple[List[float], List[float]]:
    """
    Generate x values spread evenly across [x_min, x_max] and y values
    sampled from the true line plus uniform noise in [-noise_scale, +noise_scale].
    Returns (data_x, data_y).
    """
    random.seed(seed)
    step = (x_max - x_min) / (num_points - 1)
    data_x = [x_min + i * step for i in range(num_points)]
    data_y = [
        true_slope * x + true_bias + random.uniform(-noise_scale, noise_scale)
        for x in data_x
    ]
    return data_x, data_y
```

```python exec
id: 01-learning-a-line-3
# Let's generate a dataset and see what it looks like.
# We will keep these true values secret from the optimizer — it has to discover them.
TRUE_SLOPE = 2.5
TRUE_BIAS  = -1.0

data_x, data_y = generate_noisy_line(
    true_slope=TRUE_SLOPE,
    true_bias=TRUE_BIAS,
    num_points=30,
    noise_scale=1.5,
)

fig, ax = plt.subplots(figsize=(8, 5))
ax.scatter(data_x, data_y, color="black", alpha=0.6, s=30, label="Noisy measurements")
ax.set(xlabel="x", ylabel="y", title="Our noisy data")
ax.legend()
plt.tight_layout()
plt.show()
```

Take a moment to look at the scatter plot. We can see that the points trend upward — there is clearly a line hiding in there — but no individual point sits exactly on it.

**A question worth sitting with**: without looking at the code above, could you estimate roughly what the slope is just from the plot? What about the bias (where the line crosses the y-axis)? Hold those estimates in mind — we will see how close our optimizer gets.

---

## Part 2: Making a prediction

A straight line is described completely by two numbers: its slope and its bias. Given any slope and bias, we can predict a y value for each x in our dataset.

The equation is the familiar one: `y = slope × x + bias`.

Let's write a function that takes a slope, a bias, and a list of x values, and returns the predicted y values.

```python exec
id: 01-learning-a-line-4
def predict(
    slope: float,
    bias: float,
    data_x: List[float],
) -> List[float]:
    """
    Compute predicted y values for each x using y = slope * x + bias.
    """
    return [slope * x + bias for x in data_x]
```

Now let's try a few guesses by hand and overlay them on the data. We have not looked at the true slope or bias — we are pretending to be the optimizer.

```python exec
id: 01-learning-a-line-5
# Three hand-picked guesses — adjust these if you like
guesses = [
    (1.0,  0.0),   # shallow line through origin
    (3.0, -3.0),   # too steep, too low
    (2.0, -0.5),   # closer
]

fig, ax = plt.subplots(figsize=(8, 5))
ax.scatter(data_x, data_y, color="black", alpha=0.6, s=30, label="Data")

colors = ["tomato", "goldenrod", "steelblue"]
for (s, b), color in zip(guesses, colors):
    predicted = predict(s, b, data_x)
    ax.plot(data_x, predicted, color=color, label=f"slope={s}, bias={b}")

ax.set(xlabel="x", ylabel="y", title="Three guesses overlaid on the data")
ax.legend()
plt.tight_layout()
plt.show()
```

Which of those three guesses looks closest to the data? We need a way to answer that question precisely — something better than squinting at a plot. That means we need a way to *measure* how wrong a guess is.

---

## Part 3: Measuring error

For each data point, a given slope and bias produce a predicted y value. The *residual* at that point is the gap between the prediction and the actual measurement. A good line has small residuals everywhere; a bad line has large ones.

We want to collapse all those individual gaps into a single number — the **loss** — so we can compare guesses and track improvement.

The most natural approach would be to average the residuals. But residuals can be positive or negative, and they would cancel each other out: a line that is too high on the left and too low on the right might look like a perfect fit if we just added the errors. To avoid that, we square each residual before averaging. This is **Mean Squared Error (MSE)**:

```
MSE = (1/n) × Σ (predicted_i − actual_i)²
```

Squaring does two things: it makes all errors positive, and it penalises large errors more heavily than small ones — a prediction that is 4 units off contributes 16 to the sum, not just 4.

```python exec
id: 01-learning-a-line-6
def mse(
    predictions: List[float],
    actuals: List[float],
) -> float:
    """
    Mean Squared Error: average of squared differences between predictions and actuals.
    Lower values mean a better fit.
    """
    squared_errors = [(p - a) ** 2 for p, a in zip(predictions, actuals)]
    return sum(squared_errors) / len(squared_errors)
```

```python exec
id: 01-learning-a-line-7
# Let's see how each of our hand-picked guesses scores.
print(f"{'Guess':<25} {'MSE':>8}")
print("-" * 35)
for s, b in guesses:
    loss = mse(predict(s, b, data_x), data_y)
    print(f"slope={s}, bias={b:<8} {loss:>8.2f}")

# And the true line, for comparison
true_loss = mse(predict(TRUE_SLOPE, TRUE_BIAS, data_x), data_y)
print(f"True line ({TRUE_SLOPE}, {TRUE_BIAS})   {true_loss:>8.2f}")
```

Notice that the true line does not score zero — it cannot, because the data has noise. The best any line can do is bring the loss down close to the average noise level. That floor is set by the data, not by the optimizer.

**Something to think about**: the guess with the lowest MSE in your table — is it the one that looked best visually? MSE and visual judgement usually agree, but they are not identical.

---

## Part 4: The loss surface

So far we have evaluated the loss at a handful of specific slope/bias pairs. But there is an infinite space of possible pairs. What does the loss look like across all of them?

Let's sweep over a grid of slopes and biases, compute the MSE at each combination, and plot the result. This gives us the **loss surface** — a landscape where low points are good parameter combinations and high points are bad ones.

We use numpy here only for building the grid arrays that `matplotlib` needs for its surface plot. The loss calculation itself uses our plain Python `mse` and `predict` functions.

```python exec
id: 01-learning-a-line-8
def build_loss_surface(
    data_x: List[float],
    data_y: List[float],
    slope_range: Tuple[float, float] = (-1.0, 5.0),
    bias_range: Tuple[float, float] = (-5.0, 3.0),
    resolution: int = 50,
) -> Tuple:
    """
    Evaluate MSE at every point on a slope × bias grid.
    Returns (slope_grid, bias_grid, loss_grid) as 2D numpy arrays,
    ready for matplotlib surface and contour plots.
    """
    slopes = np.linspace(slope_range[0], slope_range[1], resolution)
    biases = np.linspace(bias_range[0], bias_range[1], resolution)

    # Build 2D grids: slope_grid[i][j] = slopes[j], bias_grid[i][j] = biases[i]
    slope_grid = np.array([[s for s in slopes] for _ in biases])
    bias_grid  = np.array([[b] * resolution    for b in biases])

    # Evaluate loss at every (slope, bias) pair on the grid
    loss_grid = np.array([
        [mse(predict(s, b, data_x), data_y) for s in slopes]
        for b in biases
    ])

    return slope_grid, bias_grid, loss_grid
```

```python exec
id: 01-learning-a-line-9
slope_grid, bias_grid, loss_grid = build_loss_surface(data_x, data_y)

# 3D surface — click and drag to rotate
fig = plt.figure(figsize=(10, 7))
ax  = fig.add_subplot(111, projection="3d")
ax.plot_surface(slope_grid, bias_grid, loss_grid, cmap="viridis", alpha=0.8)
ax.set(xlabel="Slope", ylabel="Bias", zlabel="MSE", title="Loss surface")
plt.tight_layout()
plt.show()
```

```python exec
id: 01-learning-a-line-10
# The contour view — easier to read the valley floor
fig, ax = plt.subplots(figsize=(8, 6))
cf = ax.contourf(slope_grid, bias_grid, loss_grid, levels=40, cmap="viridis")
fig.colorbar(cf, ax=ax, label="MSE")
ax.plot(TRUE_SLOPE, TRUE_BIAS, "wX", ms=12, label="True parameters")
ax.set(xlabel="Slope", ylabel="Bias", title="Loss surface — contour view")
ax.legend()
plt.tight_layout()
plt.show()
```

The surface has a single bowl-shaped minimum. That minimum is close to the true slope and bias, but not exactly there — again because the data is noisy. Our job is to find the bottom of that bowl.

Notice the shape: the loss changes quickly in some directions and slowly in others. The valley is elongated. That asymmetry matters — it affects how quickly different search strategies converge.

---

## Part 5: Finding the minimum — coordinate search

Now we need a strategy for walking down to the bottom of that bowl starting from some initial guess.

The approach we will use is called **coordinate search**. At each step, we try four small moves: nudge the slope up, nudge the slope down, nudge the bias up, nudge the bias down. Each nudge has the same size — the **learning rate**. We keep whichever of the five options (including staying still) produces the lowest loss, and that becomes our new position.

This is not the most efficient optimizer — we will see why when we connect it to a neuron — but it is completely transparent. Every decision is visible.

```python exec
id: 01-learning-a-line-11
def coordinate_search(
    data_x: List[float],
    data_y: List[float],
    initial_slope: float = 0.0,
    initial_bias: float = 0.0,
    learning_rate: float = 0.1,
    num_iterations: int = 50,
) -> Tuple[List[float], List[float], List[float]]:
    """
    Minimize MSE over (slope, bias) by coordinate search.
    At each step, try nudging each parameter ±learning_rate and keep
    whichever candidate has the lowest loss.

    Returns three parallel lists: path_slopes, path_biases, path_losses,
    recording the optimizer's position and loss at every iteration.
    """
    def loss(s: float, b: float) -> float:
        """Convenience wrapper: MSE for a given slope and bias on our data."""
        return mse(predict(s, b, data_x), data_y)

    slope, bias = initial_slope, initial_bias
    current_loss = loss(slope, bias)

    path_slopes = [slope]
    path_biases = [bias]
    path_losses = [current_loss]

    for _ in range(num_iterations):
        # Build a dict of candidates: each key is a (slope, bias) pair,
        # each value is the loss at that position.
        candidates = {
            (slope,                  bias):                 current_loss,
            (slope + learning_rate,  bias):                 loss(slope + learning_rate,  bias),
            (slope - learning_rate,  bias):                 loss(slope - learning_rate,  bias),
            (slope,                  bias + learning_rate): loss(slope, bias + learning_rate),
            (slope,                  bias - learning_rate): loss(slope, bias - learning_rate),
        }
        # Move to whichever candidate has the lowest loss
        slope, bias = min(candidates, key=candidates.get)
        current_loss = candidates[(slope, bias)]

        path_slopes.append(slope)
        path_biases.append(bias)
        path_losses.append(current_loss)

    return path_slopes, path_biases, path_losses
```

```python exec
id: 01-learning-a-line-12
path_slopes, path_biases, path_losses = coordinate_search(data_x, data_y)

learned_slope = path_slopes[-1]
learned_bias  = path_biases[-1]

print(f"True:    slope = {TRUE_SLOPE},  bias = {TRUE_BIAS}")
print(f"Learned: slope = {learned_slope:.2f}, bias = {learned_bias:.2f}")
print(f"Loss:    {path_losses[0]:.2f}  →  {path_losses[-1]:.4f}")
```

The learned parameters should be reasonably close to the true ones, though probably not identical — noise in the data means there is no guarantee the best-fit line passes through the exact true parameters.

Let's look at the path the optimizer took.

---

## Part 6: Watching it learn

Four plots give us different views of the same learning process.

```python exec
id: 01-learning-a-line-13
# Plot 1: Optimization path on the 3D loss surface
fig = plt.figure(figsize=(10, 7))
ax  = fig.add_subplot(111, projection="3d")
ax.plot_surface(slope_grid, bias_grid, loss_grid, cmap="viridis", alpha=0.6)
ax.scatter(path_slopes, path_biases, path_losses, color="red", s=12, zorder=5,
           label="Search path")
ax.set(xlabel="Slope", ylabel="Bias", zlabel="MSE",
       title="Optimizer walking down the loss surface")
ax.legend()
plt.tight_layout()
plt.show()
```

```python exec
id: 01-learning-a-line-14
# Plot 2: Path overlaid on the contour map
fig, ax = plt.subplots(figsize=(8, 6))
cf = ax.contourf(slope_grid, bias_grid, loss_grid, levels=40, cmap="viridis")
fig.colorbar(cf, ax=ax, label="MSE")
ax.scatter(path_slopes, path_biases, color="red", s=12, label="Search path")
ax.plot(TRUE_SLOPE, TRUE_BIAS, "wX", ms=12, label="True parameters")
ax.set(xlabel="Slope", ylabel="Bias", title="Loss surface — search path")
ax.legend()
plt.tight_layout()
plt.show()
```

```python exec
id: 01-learning-a-line-15
# Plot 3: How the guessed line evolved across training
num_lines_to_show = 8
indices = [int(i * len(path_slopes) / (num_lines_to_show - 1))
           for i in range(num_lines_to_show)]
# Clamp the last index to the final position
indices[-1] = len(path_slopes) - 1

fig, ax = plt.subplots(figsize=(9, 6))
ax.scatter(data_x, data_y, color="black", alpha=0.5, s=30, label="Data")

for rank, idx in enumerate(indices):
    alpha = 0.15 + 0.7 * (rank / (num_lines_to_show - 1))
    ax.plot(data_x, predict(path_slopes[idx], path_biases[idx], data_x),
            color="tomato", alpha=alpha)

ax.plot(data_x, predict(TRUE_SLOPE, TRUE_BIAS, data_x),
        "b--", lw=2, label="True line")
ax.plot(data_x, predict(learned_slope, learned_bias, data_x),
        "r-", lw=2, label="Learned line")
ax.set(xlabel="x", ylabel="y", title="Line at different stages of training")
ax.legend()
plt.tight_layout()
plt.show()
```

```python exec
id: 01-learning-a-line-16
# Plot 4: The loss curve
fig, ax = plt.subplots(figsize=(9, 4))
ax.plot(range(len(path_losses)), path_losses, color="steelblue", lw=2)
ax.set(xlabel="Iteration", ylabel="MSE", title="Loss curve — how quickly did it improve?")
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
```

A few things to notice across these four plots.

The search path on the contour map moves in a staircase pattern — always axis-aligned — because coordinate search only ever adjusts one parameter at a time. Gradient descent, which we will meet later, can move diagonally and converges faster on elongated bowls like this one.

The line evolution plot shows early guesses that are clearly wrong and later ones converging toward the data. The faint red lines are early iterations; the solid red is the final result.

The loss curve usually drops steeply at first and then flattens. This is typical: large improvements are easy early on (any direction helps), but near the minimum the landscape is nearly flat and progress slows.

---

## Part 7: This is a neuron

Everything we have built is exactly what a single artificial neuron with one input does.

A neuron receives an input value, multiplies it by a **weight**, adds a **bias**, and produces an output. In our case:

```
output = weight × input + bias
```

That is our `predict` function. The weight plays the role of the slope; the bias plays the role of the bias. Training the neuron means adjusting the weight and bias to minimize the loss on some dataset — which is exactly what `coordinate_search` does.

Let's make the renaming explicit.

```python exec
id: 01-learning-a-line-17
# Everything below is identical to what we have already written.
# Only the names have changed.

def neuron_output(
    weight: float,   # formerly: slope
    bias: float,
    inputs: List[float],
) -> List[float]:
    """
    A single linear neuron: output = weight * input + bias.
    Identical to predict(); renamed to reflect the neural network context.
    """
    return [weight * x + bias for x in inputs]


def train_neuron(
    inputs: List[float],
    targets: List[float],
    initial_weight: float = 0.0,
    initial_bias: float = 0.0,
    learning_rate: float = 0.1,
    num_iterations: int = 50,
) -> Tuple[float, float, List[float]]:
    """
    Train a single linear neuron on (inputs, targets) using coordinate search.
    Returns (learned_weight, learned_bias, loss_history).
    """
    def loss(w: float, b: float) -> float:
        return mse(neuron_output(w, b, inputs), targets)

    weight, bias = initial_weight, initial_bias
    loss_history = [loss(weight, bias)]

    for _ in range(num_iterations):
        candidates = {
            (weight,                  bias):                 loss(weight,                  bias),
            (weight + learning_rate,  bias):                 loss(weight + learning_rate,  bias),
            (weight - learning_rate,  bias):                 loss(weight - learning_rate,  bias),
            (weight,                  bias + learning_rate): loss(weight, bias + learning_rate),
            (weight,                  bias - learning_rate): loss(weight, bias - learning_rate),
        }
        weight, bias = min(candidates, key=candidates.get)
        loss_history.append(candidates[(weight, bias)])

    return weight, bias, loss_history


learned_weight, learned_bias, loss_history = train_neuron(data_x, data_y)
print(f"Learned weight (slope): {learned_weight:.2f}")
print(f"Learned bias:           {learned_bias:.2f}")
```

The neuron we have just trained is **linear** — its output is a direct linear function of its input. Real neurons in deep networks usually apply an **activation function** on top of that linear step (sigmoid, ReLU, and others), which allows them to represent non-linear relationships.

But the training loop is the same idea: forward pass (compute the output), measure the loss, adjust the parameters. The difference in real networks is that the adjustment step uses the calculus of the chain rule rather than coordinate search — which is faster and scales to thousands of parameters. That is backpropagation.

For now, the key insight is this: **fitting a line to noisy data and training a neuron are the same problem**. The vocabulary of machine learning — weights, biases, loss, learning rate, training loop — is already present in the simple case we just worked through.

---

## Part 8: Experiments

The best way to build intuition about this system is to change its parameters and watch what happens. Here are some directions worth exploring.

**Learning rate effects.** What happens if the learning rate is very large (say 2.0)? What if it is very small (say 0.001)? Try both and look at the resulting loss curves.

```python exec
id: 01-learning-a-line-18
# See if you can spot where large learning rate causes the optimizer to overshoot,
# and where a small learning rate causes it to converge very slowly.

for lr in [0.01, 0.1, 0.5, 2.0]:
    _, _, losses = coordinate_search(data_x, data_y, learning_rate=lr)
    plt.plot(losses, label=f"lr = {lr}")

plt.xlabel("Iteration")
plt.ylabel("MSE")
plt.title("Loss curves at different learning rates")
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
```

**Starting point sensitivity.** Does it matter where we start? Try initialising slope and bias far from the true values and see whether the optimizer still finds the minimum.

```python exec
id: 01-learning-a-line-19
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
# Try starting at (slope=10, bias=10) — far from the true values
path_s, path_b, path_l = coordinate_search(
    data_x, data_y,
    initial_slope=10.0,
    initial_bias=10.0,
    num_iterations=150,
)
print(f"Learned: slope = {path_s[-1]:.2f}, bias = {path_b[-1]:.2f}")
print(f"Final loss: {path_l[-1]:.4f}")

# Your reflection: did it converge? How many iterations did it need?
```

**More noise, less signal.** What happens to the learned parameters and the final loss when the data is very noisy? Try `noise_scale=5.0` and see how the loss surface and the learned line change.

```python exec
id: 01-learning-a-line-20
# Generate a noisier dataset and retrain
data_x_noisy, data_y_noisy = generate_noisy_line(
    true_slope=TRUE_SLOPE,
    true_bias=TRUE_BIAS,
    num_points=30,
    noise_scale=5.0,
)
_, _, loss_history_noisy = coordinate_search(data_x_noisy, data_y_noisy)

fig, axes = plt.subplots(1, 2, figsize=(12, 4))

axes[0].scatter(data_x_noisy, data_y_noisy, color="black", alpha=0.5, s=25, label="Noisy data")
axes[0].plot(data_x, predict(TRUE_SLOPE, TRUE_BIAS, data_x), "b--", lw=2, label="True line")
axes[0].set(title="High-noise data", xlabel="x", ylabel="y")
axes[0].legend()

axes[1].plot(path_losses, label="Original noise")
axes[1].plot(loss_history_noisy, label="High noise")
axes[1].set(title="Loss curves compared", xlabel="Iteration", ylabel="MSE")
axes[1].legend()
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.show()
```

---

## Where this leads

We have a working optimizer, but coordinate search has a significant limitation: it tries five candidate positions at every step regardless of how many parameters we have. Adding a second input to our neuron would mean a second weight — now we would need to try seven candidates. A network with a thousand weights would need two thousand evaluations per step. That does not scale.

Gradient descent solves this by computing the direction of steepest descent mathematically, using derivatives, so that a single calculation tells us how to adjust *all* parameters at once. For our two-parameter line, the gradient can be written down in closed form:

```
∂MSE/∂slope = (2/n) × Σ (predicted_i − actual_i) × x_i
∂MSE/∂bias  = (2/n) × Σ (predicted_i − actual_i)
```

In the next tutorial we will derive these, implement them, and see why the neuron's training rule takes the form it does — and why that same rule, applied layer by layer through a network, is called backpropagation.

## Looking back

Before leaving this page, a sentence on each. What you write stays on this device.

```reflect
- Something you expected before running a cell that turned out differently
- The one idea from this page you could explain to someone else now
- Something you would change or try next, if there were time
- A question this page raised for you that it did not answer. Bring it to the next session; these questions are where the next session starts.
```
