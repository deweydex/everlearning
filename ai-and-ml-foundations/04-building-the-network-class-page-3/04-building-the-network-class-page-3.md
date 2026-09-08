---
title: "04-building-the-network-class-page-3 (3 of 3)"
slug: 04-building-the-network-class-page-3
course: ai-and-ml-foundations
course_title: "AI and ML Foundations"
series: 5-neural-networks
series_title: "Neural Networks"
version: 2026.09.06.1
---

Before starting this page, run the cell below. It repeats the imports and definitions from the earlier pages that this page uses.

```python exec
id: 04-building-the-network-class-page-3-setup
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

def predict(net, inputs):
    """
    Run inputs through the network and return the predicted digit.

    Use your forward function to get the output probabilities.
    Return the index of the maximum value in the output.
    """
    # Your code here.
    pass

# Test it on a few examples from the dataset.
# At this point the predictions will almost certainly be wrong —
# the network has not learned anything yet.
for label, pixels in data[:8]:
    pred = predict(net, pixels)
    correct = '✓' if pred == label else '✗'
    print(f'  True label: {label}   Prediction: {pred}   {correct}')

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

# Final test for Day 2.
nn = NeuralNetwork([784, 128, 64, 10])
print(nn)

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

# Load data and make an 80/20 split.
# Adjust max_rows to taste — 1000 trains in a reasonable time,
# more gives better curves.
all_data   = load_mnist_csv('mnist_train.csv', max_rows=1000)
split      = int(len(all_data) * 0.8)
train_data = all_data[:split]
test_data  = all_data[split:]

print(f'Training:  {len(train_data)} examples')
print(f'Test:      {len(test_data)} examples')

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

print('--- Tiny ---')
losses_tiny, accs_tiny = tiny.train(train_data, epochs=5, learning_rate=0.01)

print('--- Medium ---')
losses_med, accs_med = medium.train(train_data, epochs=5, learning_rate=0.01)

print('--- Large ---')
losses_large, accs_large = large.train(train_data, epochs=5, learning_rate=0.01)
```

---

## The Loss Curves

Plot the curves for each network. Look at the shape of the loss — not just the final value, but how it moves over the course of training.

```python exec
id: 04-building-the-network-class-page-3-1
plot_curves(losses_tiny,  accs_tiny,  title='Tiny   [784 → 8 → 10]')
```

```python exec
id: 04-building-the-network-class-page-3-2
plot_curves(losses_med,   accs_med,   title='Medium [784 → 64 → 32 → 10]')
```

```python exec
id: 04-building-the-network-class-page-3-3
plot_curves(losses_large, accs_large, title='Large  [784 → 512 → 256 → 10]')
```

In calculus, the **rate of change** of a function describes how steeply it is rising or falling at any given point. If the loss were a smooth function `L(t)`, its derivative `L'(t)` would give the slope of the curve at each step. When the curve is falling steeply, `L'(t)` is a large negative number. When it has flattened out, `L'(t)` is near zero.

Answer the following, with reference to your curves:

1. Which network's loss falls the most steeply early on? Which flattens soonest?
2. If you were implementing **early stopping** — halting training automatically when improvement stalls — what quantity would you check at the end of each epoch, and what condition would trigger the stop?
3. A large negative derivative means the network is still learning rapidly. A derivative near zero means it has largely stopped improving. Given this, is a flat loss curve always a bad sign, or could it be a good sign in some circumstances?

```python exec
id: 04-building-the-network-class-page-3-4
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
# Your answers:
#
# 1.
# 2.
# 3.
```

---

## Training vs Test Accuracy

Now let us measure how well each network performs on data it has *not* seen during training.

```python exec
id: 04-building-the-network-class-page-3-5
results = {}
for name, nn in [('Tiny', tiny), ('Medium', medium), ('Large', large)]:
    tr = accuracy_on(nn, train_data)
    te = accuracy_on(nn, test_data)
    results[name] = (tr, te)
    print(f'{name:<8}  train: {tr:.2%}   test: {te:.2%}   gap: {tr - te:+.2%}')
```

The gap between training accuracy and test accuracy is the key number. Answer the following:

1. Which network has the largest gap? What does a large gap suggest about what that network has learned?
2. Which network has the smallest gap? Does that mean it is the best network, or is there another way to read the result?
3. A network that achieves high training accuracy but low test accuracy has effectively memorised its training data. We call this **overfitting**. In your own words: why does having many more parameters than training examples make overfitting more likely?

```python exec
id: 04-building-the-network-class-page-3-6
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
# Your answers:
#
# 1.
# 2.
# 3.
```

---

## The Dimensionality of the Problem

Here is another way to think about what is happening.

The tiny network has very few parameters. In a sense, it has a very limited vocabulary for describing what it has learned — it can only represent simple, coarse patterns. It may not even be capable of learning a good solution, no matter how long you train it. This is called **underfitting**.

The large network has far more parameters than training examples. It has enough capacity to assign a unique combination of weights to every individual training image — it can memorise each one rather than finding a general pattern. When it sees a new image it has never encountered, it has no general knowledge to draw on.

Think of it this way: if a student studies for an exam by memorising exactly 40 past exam questions word for word, they will score perfectly on those 40 questions. But if the real exam has even slightly different phrasing or new examples of the same concept, that memorisation offers very little.

```python exec
id: 04-building-the-network-class-page-3-7
# Look at the misclassified examples for each network.
print('Tiny — misclassified:')
show_misclassified(tiny, test_data)
```

```python exec
id: 04-building-the-network-class-page-3-8
print('Medium — misclassified:')
show_misclassified(medium, test_data)
```

```python exec
id: 04-building-the-network-class-page-3-9
print('Large — misclassified:')
show_misclassified(large, test_data)
```

Look at the images that each network gets wrong. Then answer:

1. The tiny network's errors likely include digits that look quite clear to you. What does this tell you about what it has (and has not) learned?
2. If any errors from the large network surprise you — cases where the image looks unambiguous but the prediction is wrong — what might explain that?
3. If you were to choose one of the three architectures to deploy in a real application, which would you choose, and what evidence from today's experiments supports that choice?

```python exec
id: 04-building-the-network-class-page-3-10
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
# Your answers:
#
# 1.
# 2.
# 3.
```

---

That is the end of Day 3 and the end of the assessment. If you have time remaining, go back and tighten anything from Days 1 or 2 — particularly the class assembly and any test cells that are still incomplete.

## Looking back

Before leaving this page, a sentence on each. What you write stays on this device.

```reflect
- Something you expected before running a cell that turned out differently
- The one idea from this page you could explain to someone else now
- Something you would change or try next, if there were time
- A question this page raised for you that it did not answer. Bring it to the next session; these questions are where the next session starts.
```
