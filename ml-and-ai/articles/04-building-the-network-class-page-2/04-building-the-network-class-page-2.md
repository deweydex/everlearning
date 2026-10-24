---
title: "04-building-the-network-class-page-2 (2 of 3)"
slug: 04-building-the-network-class-page-2
course: ai-and-ml-foundations
course_title: "AI and ML Foundations"
series: 5-neural-networks
series_title: "Neural Networks"
version: 2026.09.06.1
---

Before starting this page, run the cell below. It repeats the imports and definitions from the earlier pages that this page uses.

```python exec
id: 04-building-the-network-class-page-2-setup
import os, gzip, struct, urllib.request
import matplotlib.pyplot as plt
import random
import math

# Provided: loading MNIST data from a CSV file.
# Each row has 785 values: the label first, then 784 pixel values.

def load_mnist_csv(filepath, max_rows=500):
    data = []
    with open(filepath, 'r') as f:
        for line in f:
            line = line.strip()
            if not line or not line[0].isdigit():
                continue
            parts = line.split(',')
            label = int(parts[0])
            pixels = [int(p) / 255.0 for p in parts[1:]]
            if len(pixels) == 784:
                data.append((label, pixels))
            if len(data) >= max_rows:
                break
    return data

# Provided: visualisation helpers.
import matplotlib.pyplot as plt

def show_digit(pixels, label=None):
    grid = [pixels[i * 28:(i + 1) * 28] for i in range(28)]
    plt.figure(figsize=(2, 2))
    plt.imshow(grid, cmap='gray_r')
    plt.axis('off')
    if label is not None:
        plt.title(f'Label: {label}', fontsize=10)
    plt.show()

def show_sample(data, n=10):
    fig, axes = plt.subplots(1, n, figsize=(n * 1.5, 2))
    for i, ax in enumerate(axes):
        if i >= len(data):
            ax.axis('off')
            continue
        label, pixels = data[i]
        ax.imshow([pixels[j * 28:(j + 1) * 28] for j in range(28)], cmap='gray_r')
        ax.axis('off')
        ax.set_title(str(label), fontsize=10)
    plt.tight_layout()
    plt.show()

# Load the data.
# The provided cell above makes sure this file exists.
data = load_mnist_csv('mnist_test.csv', max_rows=10000)

print(f'Loaded {len(data)} examples.')
print(f'Each input is a list of {len(data[0][1])} values.')
print(f'Labels range from {min(d[0] for d in data)} to {max(d[0] for d in data)}.')

show_sample(data, n=10)

import random

def random_matrix(rows, cols):
    """
    Return a matrix with the given number of rows and columns,
    filled with random floats between -0.1 and 0.1.
    """
    # Your code here.
    pass

def relu(x):
    """
    Return x if x is positive, otherwise return 0.
    """
    # Your code here.
    pass

import math

def softmax(values):
    """
    Convert a list of values into a probability distribution.

    Subtract the maximum value first (numerical stability).
    Then exponentiate each value and divide by the total.

    Returns a list of floats that sum to 1.0.
    """
    # Your code here.
    pass

# Test it.
scores = [2.0, 1.0, 0.5]
probs = softmax(scores)
print(f'Probabilities: {[round(p, 4) for p in probs]}')
print(f'Sum: {round(sum(probs), 8)}')  # Should be 1.0

# The highest score (2.0) should have the highest probability.
# The values should all be positive.

def make_network(layer_sizes):
    """
    Given a list of layer sizes, return a dict with:
    - 'layer_sizes': the original list
    - 'weights': a list of weight matrices (one per pair of adjacent layers)
    - 'biases':  a list of bias vectors (one per non-input layer)

    Initialise weights using random_matrix.
    Initialise biases as lists of zeros.
    """
    # Your code here.
    pass

# Test it.
net = make_network([784, 128, 64, 10])

print(f'Number of weight matrices: {len(net["weights"])}')

for i, (W, b) in enumerate(zip(net['weights'], net['biases'])):
    print(f'  Layer {i + 1}: weights {len(W)} x {len(W[0])}, biases length {len(b)}')

def forward_layer(inputs, weights, biases, activation):
    """
    Compute the output of one layer.

    inputs:     list of floats (input to this layer)
    weights:    list of lists (each inner list is one node's weights)
    biases:     list of floats (one bias per node in this layer)
    activation: a function to apply element-wise after the weighted sums

    Returns: (pre_activation, post_activation)
    Both are lists of floats, one value per node in this layer.
    """
    # For each node in this layer:
    #   compute weighted_sum(weights[node], inputs, biases[node])
    # Collect those into pre_activation.
    # Apply activation to each value to get post_activation.
    # Return both.
    pass

# Test it with a tiny example.
W = [[0.5, -0.3],
     [0.2,  0.8]]    # 2 nodes, each with 2 weights
b = [0.1, -0.1]
inputs = [1.0, 0.5]

pre, post = forward_layer(inputs, W, b, relu)

print(f'Pre-activation: {pre}')
print(f'Post-activation: {post}')

# Check by hand:
# Node 0: 0.5*1.0 + (-0.3)*0.5 + 0.1 = 0.5 - 0.15 + 0.1 = 0.45  -> relu(0.45) = 0.45
# Node 1: 0.2*1.0 +   0.8*0.5 - 0.1 = 0.2 + 0.40 - 0.1 = 0.50  -> relu(0.50) = 0.50

def forward(net, inputs):
    """
    Pass inputs through all layers of the network.

    Use relu for all layers except the last, which uses softmax.

    Returns a list of (pre_activation, post_activation) tuples,
    one per non-input layer.

    The final post_activation is the network's raw output —
    ten probability values, one per digit.
    """
    # Start with the inputs.
    # For each layer in the network:
    #   determine which activation to use (relu or softmax)
    #   call forward_layer
    #   the output of this layer becomes the input to the next
    # Collect and return all the (pre, post) pairs.
    pass

# Test it: pass a random 784-value input through the full network.
test_input = [random.uniform(0, 1) for _ in range(784)]
layer_outputs = forward(net, test_input)

print(f'Number of layer outputs: {len(layer_outputs)}')
print(f'Final output length: {len(layer_outputs[-1][1])}')
print(f'Sum of output probabilities: {round(sum(layer_outputs[-1][1]), 6)}')

# Show the output as a bar chart.
probs = layer_outputs[-1][1]
for digit, p in enumerate(probs):
    bar = '#' * int(p * 50)
    print(f'  {digit}: {bar:<50} {p:.4f}')
```

## Day 2

### Part 10: Predicting a Digit

We have a forward pass. Now let us turn the output into an actual prediction: which digit does the network think it is looking at?

The answer is simply the index of the highest probability. If the output layer gives the highest value to index 3, the network's prediction is "3".

```python exec
id: 04-building-the-network-class-page-2-1
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
def predict(net, inputs):
    """
    Run inputs through the network and return the predicted digit.

    Use your forward function to get the output probabilities.
    Return the index of the maximum value in the output.
    """
    # Your code here.
    pass
```

```python exec
id: 04-building-the-network-class-page-2-2
# Test it on a few examples from the dataset.
# At this point the predictions will almost certainly be wrong —
# the network has not learned anything yet.
for label, pixels in data[:8]:
    pred = predict(net, pixels)
    correct = '✓' if pred == label else '✗'
    print(f'  True label: {label}   Prediction: {pred}   {correct}')
```

Wrong predictions at this stage are expected and normal. We need a way to measure how wrong, and then a way to correct the weights.

---

### Part 11: How Wrong Are We? (Loss)

To train a network, we need a number that captures how bad a given prediction was. That number is called the **loss**.

We use **cross-entropy loss**. The idea is simple: if the network assigned probability `p` to the correct class, the loss is `-log(p)`. If `p` is close to 1 (confident and correct), the loss is close to 0. If `p` is close to 0 (confident and wrong), the loss is very large.

```
L = -log(p_correct)
```

```python exec
id: 04-building-the-network-class-page-2-3
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
def cross_entropy_loss(output_probs, label):
    """
    Compute the cross-entropy loss for one prediction.

    output_probs: the softmax output, a list of 10 floats
    label:        the correct class as an integer (0-9)

    Returns a single float.

    Hint: add a tiny value (1e-12) inside the log to avoid log(0).
    """
    # Your code here.
    pass
```

```python exec
id: 04-building-the-network-class-page-2-4
# Test it.
# If the network assigns probability 1.0 to the correct class, loss should be 0.
# If it assigns 0.1 (ten percent), loss should be higher.

perfect = [0.0] * 10
perfect[3] = 1.0
print(f'Loss when correct class gets 1.0:  {cross_entropy_loss(perfect, 3):.4f}')

uncertain = [0.1] * 10
print(f'Loss when correct class gets 0.1:  {cross_entropy_loss(uncertain, 3):.4f}')

# Try constructing a case where the network is confident but wrong.
# What is the loss?
```

---

### Part 12: Fixing the Weights (Backpropagation)

We know how wrong we were. Now we need to fix the weights.

**Backpropagation** is the method. The idea is to work backwards through the network, computing how much each weight contributed to the error, then nudging each weight slightly in the direction that would reduce it. The size of each nudge is controlled by the **learning rate** — a small number, typically something like 0.01.

This uses the chain rule from calculus. The cross-entropy loss and softmax combine to give a particularly clean expression for the output layer gradient:

```
delta_output[i] = output[i] - target[i]
```

where `target` is the one-hot vector for the correct class (all zeros except a 1 at the correct index). For subsequent layers we propagate this delta backwards, multiplying by the weights and by the derivative of ReLU at each step.

The derivative of ReLU is 1 where the pre-activation value was positive, and 0 otherwise.

The function below is provided. Read through it carefully. Notice:

- We save the current weights **before** updating them. Think about why this matters before moving on.
- We work backwards through the layers using `range(n_layers - 1, -1, -1)`.
- Each step computes a new `delta` for the layer below using the saved weights.

```python exec
id: 04-building-the-network-class-page-2-5
# Provided: backpropagation.
# Read through this carefully before moving to Part 13.

def backprop(net, inputs, label, layer_outputs, learning_rate=0.01):
    """
    Update the weights and biases in net using one training example.

    net:           the network dict (modified in place)
    inputs:        the original input vector
    label:         the correct digit (integer, 0-9)
    layer_outputs: the (pre, post) pairs returned by forward()
    learning_rate: step size for weight updates
    """
    n_layers = len(net['weights'])

    # One-hot target: all zeros except a 1 at the correct class.
    target = [0.0] * 10
    target[label] = 1.0

    # Output layer gradient: cross-entropy + softmax simplify to output - target.
    output_probs = layer_outputs[-1][1]
    delta = [output_probs[i] - target[i] for i in range(len(output_probs))]

    for layer_idx in range(n_layers - 1, -1, -1):

        # The input to this layer is either the original input (layer 0)
        # or the post-activation output of the previous layer.
        if layer_idx == 0:
            layer_input = inputs
        else:
            layer_input = layer_outputs[layer_idx - 1][1]

        # Save current weights before updating.
        # We need the original weights to compute the gradient for the layer below.
        saved_weights = [row[:] for row in net['weights'][layer_idx]]

        # Update each weight and bias.
        for j in range(len(net['weights'][layer_idx])):
            for k in range(len(net['weights'][layer_idx][j])):
                # The gradient of the loss with respect to this weight is
                # delta[j] * layer_input[k].
                net['weights'][layer_idx][j][k] -= learning_rate * delta[j] * layer_input[k]
            net['biases'][layer_idx][j] -= learning_rate * delta[j]

        # Compute delta for the layer below (chain rule).
        if layer_idx > 0:
            pre_activation = layer_outputs[layer_idx - 1][0]
            new_delta = []
            for k in range(len(layer_input)):
                # Sum contributions from all nodes in the current layer.
                grad = sum(saved_weights[j][k] * delta[j]
                           for j in range(len(delta)))
                # ReLU's derivative: 1 if pre-activation was positive, else 0.
                relu_deriv = 1.0 if pre_activation[k] > 0 else 0.0
                new_delta.append(grad * relu_deriv)
            delta = new_delta
```

Before moving on, answer these two questions in the cell below:

1. Why do we save the weights before updating them? What would go wrong if we used the already-updated weights when computing the next layer's delta?

2. The output layer gradient simplifies to `output[i] - target[i]`. What does this expression equal when the network assigns a very high probability to the correct class?

```python exec
id: 04-building-the-network-class-page-2-6
# Write your answers here as comments or a print statement.
# Q1:
# Q2:
```

---

### Part 13: The Training Loop

We have forward, loss, and backprop. Now we can write a training loop that puts them all together.

The loop goes through the training data one example at a time, runs a forward pass, records the loss and whether the prediction was correct, and runs backprop to update the weights. We record the loss and accuracy as we go so we can see whether the network is improving.

```python exec
id: 04-building-the-network-class-page-2-7
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
def train(net, data, epochs=1, learning_rate=0.01):
    """
    Train the network on data for the given number of epochs.

    An epoch is one full pass through all the training examples.

    For each example:
    1. Run forward() to get layer_outputs.
    2. Record the loss using cross_entropy_loss.
    3. Record whether predict() returns the correct label.
    4. Run backprop() to update the weights.

    Print the average loss and accuracy after each epoch.

    Returns (loss_history, accuracy_history), where each is a list
    of per-example values across all epochs.
    """
    loss_history = []
    accuracy_history = []

    for epoch in range(epochs):
        epoch_loss = 0.0
        epoch_correct = 0

        for label, pixels in data:
            # Your code here.
            pass

        avg_loss = epoch_loss / len(data)
        avg_acc = epoch_correct / len(data)
        print(f'Epoch {epoch + 1}: loss = {avg_loss:.4f}   accuracy = {avg_acc:.2%}')

    return loss_history, accuracy_history
```

```python exec
id: 04-building-the-network-class-page-2-8
# Test it: train for a few epochs on our 200-example dataset.
# With only 200 examples and a randomly initialised network,
# do not expect dramatic results — but you should see the loss
# moving in the right direction.
net = make_network([784, 128, 64, 10])
losses, accs = train(net, data, epochs=3, learning_rate=0.01)
```

---

### Part 14: Testing with a Random Input

Before we move to the full dataset (that is Day 3), let us do a final sanity check: feed a random 784-value input through the trained network and look at what comes out.

```python exec
id: 04-building-the-network-class-page-2-9
# Create a random input the right size.
random_input = [random.uniform(0, 1) for _ in range(784)]

# Run it through and look at the output.
layer_outputs = forward(net, random_input)
pred = predict(net, random_input)
output_probs = layer_outputs[-1][1]

print(f'Prediction: {pred}')
print(f'Confidence: {output_probs[pred]:.2%}')
print()
print('Full probability distribution:')
for digit, p in enumerate(output_probs):
    bar = '#' * int(p * 50)
    print(f'  {digit}: {bar:<50} {p:.4f}')
```

---

### Part 15: Assembling the Class

You now have every piece of the network working as a standalone function. Let us bring them all together into a single `NeuralNetwork` class.

Each function you wrote becomes a method. Where a function took `net` as its first argument, that becomes `self`. The internal helpers (random matrix, relu, softmax, weighted sum, forward layer) become private methods prefixed with an underscore.

```python exec
id: 04-building-the-network-class-page-2-10
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
import random
import math

class NeuralNetwork:
    """A feedforward neural network for digit classification."""

    def __init__(self, layer_sizes):
        """
        Initialise the network.
        layer_sizes: e.g. [784, 128, 64, 10]
        """
        self.layer_sizes = layer_sizes
        self.weights = []
        self.biases = []
        for i in range(len(layer_sizes) - 1):
            self.weights.append(self._random_matrix(layer_sizes[i + 1], layer_sizes[i]))
            self.biases.append([0.0] * layer_sizes[i + 1])

    def __str__(self):
        """Return a readable summary of the network architecture."""
        # Your code here.
        pass

    def _random_matrix(self, rows, cols):
        """Return a matrix of random values between -0.1 and 0.1."""
        # Bring your random_matrix function here.
        pass

    def _relu(self, x):
        """Return x if positive, otherwise 0."""
        # Your code here.
        pass

    def _softmax(self, values):
        """Convert a list of values to a probability distribution."""
        # Your code here.
        pass

    def _weighted_sum(self, weights, inputs, bias):
        """Dot product of weights and inputs, plus bias."""
        # Your code here.
        pass

    def _forward_layer(self, inputs, layer_idx, activation):
        """
        Compute the output of one layer.
        Returns (pre_activation, post_activation).
        """
        # Your code here.
        pass

    def forward(self, inputs):
        """
        Pass inputs through all layers.
        Returns a list of (pre, post) tuples, one per non-input layer.
        """
        # Your code here.
        pass

    def predict(self, inputs):
        """Return the predicted digit for a given input."""
        # Your code here.
        pass

    def _cross_entropy_loss(self, output_probs, label):
        """Compute cross-entropy loss for one example."""
        # Your code here.
        pass

    def _backprop(self, inputs, label, layer_outputs, learning_rate):
        """
        Update weights using backpropagation.
        Bring across the provided backprop function,
        replacing net['weights'] with self.weights and so on.
        """
        # Your code here.
        pass

    def train(self, data, epochs=1, learning_rate=0.01):
        """
        Train on data. Print loss and accuracy per epoch.
        Returns (loss_history, accuracy_history).
        """
        # Your code here.
        pass
```

```python exec
id: 04-building-the-network-class-page-2-11
# Final test for Day 2.
nn = NeuralNetwork([784, 128, 64, 10])
print(nn)
```

```python exec
id: 04-building-the-network-class-page-2-12
# Quick training run to confirm the class works end-to-end.
losses, accs = nn.train(data, epochs=3, learning_rate=0.01)
```

```python exec
id: 04-building-the-network-class-page-2-13
# Test the predict method directly on a few examples.
for label, pixels in data[:5]:
    pred = nn.predict(pixels)
    print(f'  True: {label}   Predicted: {pred}')
```

That is the end of Day 2. Your `NeuralNetwork` class is complete and working. In Day 3 we will load the full MNIST dataset, train for several epochs, and look carefully at what the network has learned.

---

## Building a Neural Network from Scratch — Day 3

Your `NeuralNetwork` class is complete. Today we use it to run three experiments and think carefully about what happens when a network has too few parameters, too many, or roughly the right number.

If you are still finishing Day 2 parts, that is fine — work through this and come back to tighten earlier cells when there is time.

---

## Setup

Paste your `NeuralNetwork` class in the cell below, or import it. The helpers provided here are all you will need today.

```python exec
id: 04-building-the-network-class-page-2-14
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
# Your NeuralNetwork class here (or import it).

import random
import math
import matplotlib.pyplot as plt
```

```python exec
id: 04-building-the-network-class-page-2-15
# Provided: data loading.

def load_mnist_csv(filepath, max_rows=None):
    data = []
    with open(filepath, 'r') as f:
        for line in f:
            line = line.strip()
            if not line or not line[0].isdigit():
                continue
            parts = line.split(',')
            label = int(parts[0])
            pixels = [int(p) / 255.0 for p in parts[1:]]
            if len(pixels) == 784:
                data.append((label, pixels))
            if max_rows and len(data) >= max_rows:
                break
    return data
```

```python exec
id: 04-building-the-network-class-page-2-16
# Provided: plotting and accuracy helpers.

def plot_curves(loss_history, accuracy_history, title='Training'):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 3.5))
    ax1.plot(loss_history, linewidth=0.8, alpha=0.85)
    ax1.set_title(f'{title} — Loss')
    ax1.set_xlabel('Example (all epochs)')
    ax1.set_ylabel('Loss')
    ax2.plot(accuracy_history, linewidth=0.8, alpha=0.85, color='steelblue')
    ax2.set_title(f'{title} — Running accuracy')
    ax2.set_xlabel('Example (all epochs)')
    ax2.set_ylabel('Accuracy')
    ax2.set_ylim(0, 1)
    plt.tight_layout()
    plt.show()

def accuracy_on(nn, dataset):
    correct = sum(1 for label, pixels in dataset if nn.predict(pixels) == label)
    return correct / len(dataset)

def show_misclassified(nn, test_data, n=12):
    errors = [(label, pixels) for label, pixels in test_data
              if nn.predict(pixels) != label]
    n = min(n, len(errors))
    if n == 0:
        print('No misclassified examples found.')
        return
    cols = 6
    rows = (n + cols - 1) // cols
    fig, axes = plt.subplots(rows, cols, figsize=(cols * 1.6, rows * 2.0))
    axes = axes.flat if rows > 1 else [axes] if cols == 1 else axes
    for i, ax in enumerate(axes):
        if i >= n:
            ax.axis('off')
            continue
        label, pixels = errors[i]
        pred = nn.predict(pixels)
        ax.imshow([pixels[j * 28:(j + 1) * 28] for j in range(28)], cmap='gray_r')
        ax.axis('off')
        ax.set_title(f'T:{label}  P:{pred}', fontsize=8, color='firebrick')
    plt.suptitle('Misclassified examples', fontsize=10)
    plt.tight_layout()
    plt.show()
    print(f'{len(errors)} errors out of {len(test_data)} test examples.')
```

```python exec
id: 04-building-the-network-class-page-2-17
# Load data and make an 80/20 split.
# Adjust max_rows to taste — 1000 trains in a reasonable time,
# more gives better curves.
all_data   = load_mnist_csv('mnist_train.csv', max_rows=1000)
split      = int(len(all_data) * 0.8)
train_data = all_data[:split]
test_data  = all_data[split:]

print(f'Training:  {len(train_data)} examples')
print(f'Test:      {len(test_data)} examples')
```

---

## The Experiment

We are going to train three networks on exactly the same data. The only thing that changes is their architecture — the number of layers and nodes.

Before we run anything, look at each architecture and use your `describe_network` function (or the `__str__` method on the class) to see the parameter count. This matters.

```python exec
id: 04-building-the-network-class-page-2-18
# Three architectures.
tiny   = NeuralNetwork([784,  8,       10])   # very few nodes
medium = NeuralNetwork([784, 64, 32,   10])   # moderate
large  = NeuralNetwork([784, 512, 256, 10])   # many nodes

print('Tiny:')
print(tiny)
print()
print('Medium:')
print(medium)
print()
print('Large:')
print(large)
```

Look at those parameter counts. The large network has orders of magnitude more parameters than the tiny one, but they are all being trained on exactly the same number of examples. Write a brief prediction in the cell below: what do you expect will happen to each network?

```python exec
id: 04-building-the-network-class-page-2-19
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
# Your prediction before training:
# Tiny   —
# Medium —
# Large  —
```

---

## Training All Three

```python exec
id: 04-building-the-network-class-page-2-20
print('--- Tiny ---')
losses_tiny, accs_tiny = tiny.train(train_data, epochs=5, learning_rate=0.01)
```

```python exec
id: 04-building-the-network-class-page-2-21
print('--- Medium ---')
losses_med, accs_med = medium.train(train_data, epochs=5, learning_rate=0.01)
```

```python exec
id: 04-building-the-network-class-page-2-22
print('--- Large ---')
losses_large, accs_large = large.train(train_data, epochs=5, learning_rate=0.01)
```

## Looking back

Before leaving this page, a sentence on each. What you write stays on this device.

```reflect
- Something you expected before running a cell that turned out differently
- The one idea from this page you could explain to someone else now
- Something you would change or try next, if there were time
- A question this page raised for you that it did not answer. Bring it to the next session; these questions are where the next session starts.
```
