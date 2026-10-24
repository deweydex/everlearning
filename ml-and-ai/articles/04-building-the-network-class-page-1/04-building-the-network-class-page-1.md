---
title: "Building a Neural Network from Scratch (1 of 3)"
slug: 04-building-the-network-class-page-1
course: ai-and-ml-foundations
course_title: "AI and ML Foundations"
series: 5-neural-networks
series_title: "Neural Networks"
version: 2026.09.06.1
---

# Building a Neural Network from Scratch

We are going to write a neural network that can look at a handwritten digit and tell us which number it is. Not by using a library that does it for us, but by writing every piece ourselves, from the maths up.

By the end of Day 2 we will have a working `NeuralNetwork` class. In Day 3 we will train it on real data and see what it can learn.

The approach here is to build each piece as a standalone function, test it, understand it, and only at the end collect everything into a class. That way, when you write the class, you are not guessing — you have already seen every method work.

---

## Day 1

### Part 1: The Data

Before we build anything, let us look at what we are trying to classify.

The MNIST dataset is a collection of 70,000 handwritten digits. Each digit has been photographed and rescaled to a 28×28 grid of pixel values. The pixel values run from 0 (white) to 255 (black). We normalise them to the range 0–1 before feeding them into a network.

Each image comes with a **label** — the actual digit it represents. Our job is to build something that can look at the pixels and guess the label.

The code below loads a sample from a CSV file and shows you some examples. Run it, look at the images, and notice what you are working with: each digit is just a flat list of 784 numbers.

```python exec
id: 04-building-the-network-class-page-1-1
# Provided: make sure the digit data is here.
# The notebook reads MNIST digits from two CSV files, one row per digit: the label, then 784 pixel values.
# If the files are not beside the notebook, this cell downloads the standard test set (10,000 digits,
# about 1.6 MB compressed) and writes mnist_train.csv (the first 8,000) and mnist_test.csv (the rest).
import os, gzip, struct, urllib.request

def write_mnist_csvs():
    base = 'https://storage.googleapis.com/cvdf-datasets/mnist/'
    images_file, labels_file = 't10k-images-idx3-ubyte.gz', 't10k-labels-idx1-ubyte.gz'
    for name in (images_file, labels_file):
        if not os.path.exists(name):
            urllib.request.urlretrieve(base + name, name)
    with gzip.open(labels_file) as f:
        f.read(8)                                   # header: magic number and count
        labels = list(f.read())
    with gzip.open(images_file) as f:
        _, count, rows, cols = struct.unpack('>IIII', f.read(16))
        pixels = f.read()
    size = rows * cols
    lines = [str(labels[i]) + ',' + ','.join(str(p) for p in pixels[i * size:(i + 1) * size]) + '\n' for i in range(count)]
    with open('mnist_train.csv', 'w') as f: f.writelines(lines[:8000])
    with open('mnist_test.csv', 'w') as f: f.writelines(lines[8000:])

if not (os.path.exists('mnist_train.csv') and os.path.exists('mnist_test.csv')):
    print('Fetching digit data ...'); write_mnist_csvs(); print('Wrote mnist_train.csv and mnist_test.csv')
else:
    print('Digit data already here.')
```

```python exec
id: 04-building-the-network-class-page-1-2
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
```

```python exec
id: 04-building-the-network-class-page-1-3
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
```

```python exec
id: 04-building-the-network-class-page-1-4
# Load the data.
# The provided cell above makes sure this file exists.
data = load_mnist_csv('mnist_test.csv', max_rows=10000)

print(f'Loaded {len(data)} examples.')
print(f'Each input is a list of {len(data[0][1])} values.')
print(f'Labels range from {min(d[0] for d in data)} to {max(d[0] for d in data)}.')

show_sample(data, n=10)
```

Look at those ten images. Each one is genuinely different — different handwriting, different thickness, different angle. The network we build will have to learn what it means for a clump of pixels to be a "3" versus a "5" just from the numbers.

Before you move on: how would *you* tell a 1 from a 7? What features are you actually using?

---

### Part 2: What Our Network Will Look Like

A neural network is a chain of layers. Each layer takes a list of numbers as input, does some arithmetic, and passes the result to the next layer.

Our network will have this shape:

- **Input layer**: 784 values — one per pixel
- **Hidden layer 1**: 128 values
- **Hidden layer 2**: 64 values
- **Output layer**: 10 values — one per digit (0 through 9)

The output layer will give us ten numbers. The largest one is our prediction: whichever digit has the highest score is the one the network thinks it is looking at.

Between every pair of adjacent layers, every node in one layer is connected to every node in the next. Each connection has a **weight** — a number that controls how much influence one node has on another. Each node also has a **bias** — a value that shifts its output up or down regardless of the input.

The weights and biases start as small random numbers. Training means adjusting them until the network gets better at recognising digits.

We will build this piece by piece.

---

### Part 3: Random Matrices

The first thing we need is a way to create a matrix of small random numbers. A matrix here is a list of lists: each inner list is one row.

We use small numbers near zero for initialisation so that the network does not immediately produce enormous outputs before it has learned anything.

```python exec
id: 04-building-the-network-class-page-1-5
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
import random

def random_matrix(rows, cols):
    """
    Return a matrix with the given number of rows and columns,
    filled with random floats between -0.1 and 0.1.
    """
    # Your code here.
    pass
```

```python exec
id: 04-building-the-network-class-page-1-6
# Test it.
m = random_matrix(3, 4)
print(f'Rows: {len(m)}')
print(f'Columns: {len(m[0])}')
print(f'First row: {m[0]}')
print(f'All values between -0.1 and 0.1: {all(-0.1 <= v <= 0.1 for row in m for v in row)}')
```

---

### Part 4: Weighted Sum

Each node in the network computes a **weighted sum** of its inputs. If the inputs are `[x0, x1, x2]` and the weights for one particular node are `[w0, w1, w2]` with bias `b`, that node's output (before any activation) is:

```
z = w0*x0 + w1*x1 + w2*x2 + b
```

This is also called a dot product plus a bias. You may have written a dot product before — it is exactly that, with `b` added at the end.

```python exec
id: 04-building-the-network-class-page-1-7
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
def weighted_sum(weights, inputs, bias):
    """
    Compute the dot product of weights and inputs, then add bias.

    weights: a list of floats, one per input
    inputs:  a list of floats, one per input
    bias:    a single float

    Returns a single float.
    """
    # Your code here.
    pass
```

```python exec
id: 04-building-the-network-class-page-1-8
# Test it.
# 0.5*1.0 + (-0.3)*2.0 + 0.8*0.5 + 0.1
# = 0.5 - 0.6 + 0.4 + 0.1
# = 0.4

result = weighted_sum([0.5, -0.3, 0.8], [1.0, 2.0, 0.5], 0.1)
print(f'Result: {result}')
print(f'Expected: 0.4')
```

---

### Part 5: Activation Functions

After computing a weighted sum, we pass the result through an **activation function**. Without this step, a neural network with multiple layers would collapse into a single linear transformation — adding more layers would not help. Activation functions introduce the non-linearity that lets deep networks learn complex patterns.

**ReLU** (Rectified Linear Unit) is the one we will use in our hidden layers. It is extremely simple: if the input is positive, pass it through unchanged. Otherwise, return zero.

```python exec
id: 04-building-the-network-class-page-1-9
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
def relu(x):
    """
    Return x if x is positive, otherwise return 0.
    """
    # Your code here.
    pass
```

```python exec
id: 04-building-the-network-class-page-1-10
# Test it.
for val in [-2.0, -0.5, 0.0, 0.3, 1.7]:
    print(f'relu({val:5.1f}) = {relu(val)}')
```

**Softmax** is what we will use on the output layer. It takes a list of numbers and converts them into a probability distribution: values between 0 and 1 that sum to exactly 1. The digit with the highest softmax score is the one the network is "most confident" about.

The formula is:

```
softmax(z_i) = exp(z_i) / sum(exp(z_j) for all j)
```

We subtract the maximum value before exponentiating — this is a standard numerical stability trick that prevents overflow and does not change the result.

```python exec
id: 04-building-the-network-class-page-1-11
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
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
```

```python exec
id: 04-building-the-network-class-page-1-12
# Test it.
scores = [2.0, 1.0, 0.5]
probs = softmax(scores)
print(f'Probabilities: {[round(p, 4) for p in probs]}')
print(f'Sum: {round(sum(probs), 8)}')  # Should be 1.0

# The highest score (2.0) should have the highest probability.
# The values should all be positive.
```

---

### Part 6: Setting Up the Network

We now have the building blocks. The next step is to set up the data structure that will hold our network's weights and biases.

Given a list of layer sizes like `[784, 128, 64, 10]`, we need:
- A weight matrix **between each pair of adjacent layers**
- A bias vector **for each layer except the input**

For our network:
- Weights from layer 0 to layer 1: 128 rows × 784 columns (each of the 128 nodes needs one weight per input)
- Weights from layer 1 to layer 2: 64 rows × 128 columns
- Weights from layer 2 to layer 3: 10 rows × 64 columns

Notice the pattern: for a connection from a layer of size `a` to a layer of size `b`, the weight matrix has shape `b × a`.

```python exec
id: 04-building-the-network-class-page-1-13
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
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
```

```python exec
id: 04-building-the-network-class-page-1-14
# Test it.
net = make_network([784, 128, 64, 10])

print(f'Number of weight matrices: {len(net["weights"])}')

for i, (W, b) in enumerate(zip(net['weights'], net['biases'])):
    print(f'  Layer {i + 1}: weights {len(W)} x {len(W[0])}, biases length {len(b)}')
```

---

### Part 7: Describing the Network

Before we use our network, let us write a function that describes it clearly: what shape are the layers, and how many parameters does it have in total?

A weight matrix with `rows` rows and `cols` columns has `rows * cols` parameters. Each bias vector of length `n` has `n` parameters.

```python exec
id: 04-building-the-network-class-page-1-15
def describe_network(net):
    """
    Print a summary: the shape of each weight matrix, the length of
    each bias vector, and the total number of parameters.
    """
    total = 0
    for i, (W, b) in enumerate(zip(net['weights'], net['biases'])):
        params = len(W) * len(W[0]) + len(b)
        total += params
        print(f'  Layer {i + 1}: {len(W[0])} inputs -> {len(W)} nodes  ({params:,} parameters)')
    print(f'\n  Total parameters: {total:,}')
```

```python exec
id: 04-building-the-network-class-page-1-16
net = make_network([784, 128, 64, 10])
describe_network(net)
```

Think about that number for a moment. Every one of those parameters will be adjusted during training.

---

### Part 8: One Layer Forward

Now let us move data through a single layer. Given:
- A list of input values
- The weight matrix for this layer
- The bias vector for this layer
- An activation function

...we compute two things:
1. The **pre-activation output** — the raw weighted sums, before the activation function
2. The **post-activation output** — after applying the activation function

We return both because we will need the pre-activation values when we do backpropagation in Day 2.

```python exec
id: 04-building-the-network-class-page-1-17
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
```

```python exec
id: 04-building-the-network-class-page-1-18
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
```

---

### Part 9: Full Forward Pass

Now let us pass an input all the way through every layer. Hidden layers use ReLU; the output layer uses softmax.

```python exec
id: 04-building-the-network-class-page-1-19
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
```

```python exec
id: 04-building-the-network-class-page-1-20
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

The probabilities sum to 1 because of softmax. The network's prediction at this point is essentially random — the weights are random, so every digit is roughly equally likely. That is exactly where we should be.

That is the end of Day 1.

---

## Looking back

Before leaving this page, a sentence on each. What you write stays on this device.

```reflect
- Something you expected before running a cell that turned out differently
- The one idea from this page you could explain to someone else now
- Something you would change or try next, if there were time
- A question this page raised for you that it did not answer. Bring it to the next session; these questions are where the next session starts.
```
