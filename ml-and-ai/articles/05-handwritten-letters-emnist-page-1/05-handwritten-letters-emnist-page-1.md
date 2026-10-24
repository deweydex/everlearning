---
title: "Building a Neural Network from Scratch (1 of 2)"
slug: 05-handwritten-letters-emnist-page-1
course: ai-and-ml-foundations
course_title: "AI and ML Foundations"
series: 5-neural-networks
series_title: "Neural Networks"
version: 2026.09.06.1
---

# Building a Neural Network from Scratch

## Teaching a Computer to Recognise Handwritten Letters

---

In this tutorial, we're going to build a neural network from scratch using only basic Python and a bit of NumPy. No machine learning libraries, no magic - just the fundamental mathematics and code that makes neural networks work.

By the end, we'll have a working system that can look at a handwritten letter and tell us which letter it is. More importantly, we'll understand *how* it works, not just *that* it works.

### What We're Building

Our network will:
- Take pixel values from a small image of a handwritten letter
- Pass those values through layers of connected "neurons"
- Learn from its mistakes using **backpropagation**
- Gradually improve until it can recognise letters accurately

### Why Build from Scratch?

Libraries like TensorFlow or PyTorch make neural networks easy to use, but they hide the mechanics. Building from scratch helps us understand:
- How information flows forward through a network
- How errors flow backward to improve the network
- Why certain choices matter (learning rate, network structure, etc.)

This understanding makes us better practitioners when we do use those libraries.

### Our Approach

We'll build progressively, testing each piece before moving on:
1. Start with single neurons and simple operations
2. Connect neurons into layers
3. Stack layers into a network
4. Teach the network to learn from mistakes
5. Apply it to real handwritten letters

Each function we write will build on the ones before. By the end, the complete picture will emerge from these small, understandable pieces.

---

## Setup

We only need two libraries:

```python exec
id: 05-handwritten-letters-emnist-page-1-1
import numpy as np
import matplotlib.pyplot as plt
from random import random, seed, shuffle
from math import exp

# For reproducible results
seed(42)
np.random.seed(42)

print("Setup complete.")
```

---

## Part 1: The Building Block - A Single Neuron

Before building a network, let's understand what a single neuron does. A neuron is surprisingly simple - it just:
1. Takes some inputs
2. Multiplies each input by a weight
3. Adds them all up (plus a bias)
4. Applies an "activation function" to squash the result

### Step 1.1: Weighted Sum (Activation)

The weighted sum is like a vote where each input gets a different voting power (weight):

$$\text{activation} = (w_1 \times x_1) + (w_2 \times x_2) + ... + \text{bias}$$

Let's write a function to calculate this:

```python exec
id: 05-handwritten-letters-emnist-page-1-2
def calculate_activation(weights: list, inputs: list) -> float:
    """
    Calculate the weighted sum of inputs.

    The bias is stored as the last element of weights.

    Parameters:
        weights: List of weights, with bias as the last element
        inputs: List of input values (one fewer than weights)

    Returns:
        The weighted sum (activation value)
    """
    # Start with the bias (last weight)
    pre_activation = weights[-1]

    # Add each input multiplied by its weight
    for i in range(len(weights) - 1):
        pre_activation = pre_activation + weights[i] * inputs[i]

    return pre_activation
```

### Exploration 1.1: Testing the Weighted Sum

Let's see this in action. Before running the cell below, try to predict what the result will be:

```python exec
id: 05-handwritten-letters-emnist-page-1-3
# Example: A neuron with 2 inputs
# weights = [weight_for_input_1, weight_for_input_2, bias]
example_weights = [0.5, -0.3, 0.1]
example_inputs = [2.0, 4.0]

# What do we expect?
# (0.5 * 2.0) + (-0.3 * 4.0) + 0.1
# = 1.0 + (-1.2) + 0.1
# = -0.1

result = calculate_activation(example_weights, example_inputs)
print(f"Activation: {result}")
```

### Your Turn 1.1

Create your own example with 3 inputs. Calculate the expected result by hand first, then verify with the function.

```python exec
id: 05-handwritten-letters-emnist-page-1-4
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
# Your code here:
# Create weights for 3 inputs (so 4 values total, including bias)
# Create 3 input values
# Calculate expected result by hand
# Verify with the function
```

### Step 1.2: The Sigmoid Transfer Function

The weighted sum can be any number - positive, negative, huge, tiny. We often want to squash this into a useful range, typically between 0 and 1.

The **sigmoid function** does exactly this:

$$\sigma(x) = \frac{1}{1 + e^{-x}}$$

- Large positive inputs → close to 1
- Large negative inputs → close to 0
- Zero → exactly 0.5

Let's implement it:

```python exec
id: 05-handwritten-letters-emnist-page-1-5
def sigmoid(x: float) -> float:
    """
    The sigmoid activation function.

    Squashes any input into the range (0, 1).

    Parameters:
        x: Any real number

    Returns:
        A value between 0 and 1
    """
    return 1.0 / (1.0 + exp(-x))
```

### Exploration 1.2: Visualising the Sigmoid

Let's see what this function looks like:

```python exec
id: 05-handwritten-letters-emnist-page-1-6
# Generate x values from -10 to 10
x_values = np.linspace(-10, 10, 100)

# Calculate sigmoid for each x
y_values = [sigmoid(x) for x in x_values]

# Plot
plt.figure(figsize=(10, 5))
plt.plot(x_values, y_values, linewidth=2)
plt.axhline(y=0.5, color='gray', linestyle='--', alpha=0.5, label='y = 0.5')
plt.axvline(x=0, color='gray', linestyle='--', alpha=0.5, label='x = 0')
plt.xlabel('Input (activation)')
plt.ylabel('Output (after sigmoid)')
plt.title('The Sigmoid Function')
plt.grid(True, alpha=0.3)
plt.legend()
plt.show()

# Let's verify some specific values
print(f"sigmoid(-10) = {sigmoid(-10):.6f}  (close to 0)")
print(f"sigmoid(0)   = {sigmoid(0):.6f}  (exactly 0.5)")
print(f"sigmoid(10)  = {sigmoid(10):.6f}  (close to 1)")
```

### Reflection 1.2

Notice the S-shape. This is why it's sometimes called the "logistic" function. Think about:
- Why might squashing outputs between 0 and 1 be useful?
- What happens if the input is already between 0 and 1?
- How steep is the curve around x=0?

### Step 1.3: A Complete Neuron

Now we can put these together. A neuron:
1. Calculates the weighted sum (activation)
2. Applies the sigmoid function (transfer)

We already have both pieces. Let's test them together:

```python exec
id: 05-handwritten-letters-emnist-page-1-7
# A neuron with 2 inputs
weights = [0.5, -0.3, 0.1]  # Two weights plus bias
inputs = [2.0, 4.0]

# Step 1: Calculate weighted sum
pre_activation = calculate_activation(weights, inputs)
print(f"Pre_activation (weighted sum): {pre_activation}")

# Step 2: Apply sigmoid
output = sigmoid(pre_activation)
print(f"Output (after sigmoid): {output}")
```

---

## Part 2: Forward Propagation - From Input to Output

A neural network is made of layers of neurons. Information flows forward:
- **Input layer**: Our raw data (e.g., pixel values)
- **Hidden layer(s)**: Intermediate processing
- **Output layer**: The final answer (e.g., which letter is it?)

Each neuron in a layer connects to every neuron in the next layer - this is called a "fully connected" or "dense" network.

### Step 2.1: Representing a Network

We'll represent each neuron as a dictionary with a 'weights' key. A layer is a list of neurons. A network is a list of layers.

Let's write a function to create a random network:

```python exec
id: 05-handwritten-letters-emnist-page-1-8
def create_network(n_inputs: int, n_hidden: int, n_outputs: int) -> list:
    """
    Create a neural network with random weights.

    Creates a network with one hidden layer.

    Parameters:
        n_inputs: Number of input features
        n_hidden: Number of neurons in the hidden layer
        n_outputs: Number of output neurons (usually number of classes)

    Returns:
        A network (list of layers, each layer is a list of neurons)
    """
    network = []

    # Hidden layer: each neuron has n_inputs weights + 1 bias
    hidden_layer = []
    for node in range(n_hidden):
        neuron_weights = [random() for input_node in range(n_inputs + 1)]
        # input_node is "which input node we are "connecting" to"
        # my +1 at the end takes care of my bias
        neuron = {'weights': neuron_weights}
        hidden_layer.append(neuron)
    network.append(hidden_layer)

    # Output layer: each neuron has n_hidden weights + 1 bias
    output_layer = []
    for node in range(n_outputs):
        neuron_weights = [random() for hidden_node in range(n_hidden + 1)]
        # our +1 is our bias :)
        neuron = {'weights': neuron_weights}
        output_layer.append(neuron)
    network.append(output_layer)

    return network
```

### Exploration 2.1: Understanding Network Structure

Let's create a small network and examine its structure:

```python exec
id: 05-handwritten-letters-emnist-page-1-9
# Create a network with:
# - 2 inputs
# - 3 hidden neurons
# - 2 outputs
seed(1)  # For reproducibility
test_network = create_network(n_inputs=2, n_hidden=3, n_outputs=2)

print("Network structure:")
print(f"Number of layers: {len(test_network)}")
print()

for layer_index, layer in enumerate(test_network):
    layer_name = "Hidden" if layer_index == 0 else "Output"
    print(f"{layer_name} Layer ({len(layer)} neurons):")
    for neuron_index, neuron in enumerate(layer):
        n_weights = len(neuron['weights'])
        print(f"  Neuron {neuron_index}: {n_weights} weights (including bias)")
    print()
```

### Your Turn 2.1

Before looking at the answer:
- If we have 5 inputs and 4 hidden neurons, how many weights does each hidden neuron have?
- If we have 4 hidden neurons and 3 outputs, how many weights does each output neuron have?

Create such a network and verify your answers.

```python exec
id: 05-handwritten-letters-emnist-page-1-10
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
# Your code here:
```

### Step 2.2: Forward Propagation

Now let's write the function that pushes data through the network:
1. Take the inputs
2. For each layer:
   - Calculate each neuron's output
   - These outputs become the inputs for the next layer
3. Return the final outputs

```python exec
id: 05-handwritten-letters-emnist-page-1-11
def forward_propagate(network: list, row: list) -> list:
    """
    Propagate an input through the network.

    Calculates the output for each neuron in each layer,
    storing the output in the neuron dictionary.

    Parameters:
        network: The neural network
        row: A single input sample (list of values)

    Returns:
        The outputs from the final layer
    """
    inputs = row

    for layer in network:
        new_inputs = []

        for neuron in layer:
            # Calculate weighted sum and apply activation function
            neuron['output']  = sigmoid(calculate_activation(neuron['weights'], inputs))
            # Collect outputs for the next layer
            new_inputs.append(neuron['output'])

        # This layer's outputs become next layer's inputs
        inputs = new_inputs

    return inputs
```

### Exploration 2.2: Watching Data Flow

Let's trace through a forward pass step by step:

```python exec
id: 05-handwritten-letters-emnist-page-1-12
# Create a tiny network we can follow
seed(1)
tiny_network = create_network(n_inputs=2, n_hidden=2, n_outputs=2)

# Our input
test_input = [1.0, 0.5]

print("Input:", test_input)
print()

# Forward propagate
outputs = forward_propagate(tiny_network, test_input)

# Let's see what happened
print("Hidden layer outputs:")
for i, neuron in enumerate(tiny_network[0]):
    print(f"  Neuron {i}: {neuron['output']:.4f}")

print()
print("Output layer outputs (final):")
for i, neuron in enumerate(tiny_network[1]):
    print(f"  Neuron {i}: {neuron['output']:.4f}")

print()
print("Final outputs:", [round(o, 4) for o in outputs])
```

### Reflection 2.2

At this point, the outputs are meaningless - the weights are random! But the machinery is in place:
- Data flows in
- Each neuron computes something
- We get outputs

The magic happens when we teach the network to adjust its weights to produce *useful* outputs. That's what backpropagation is for.

---

## Looking back

Before leaving this page, a sentence on each. What you write stays on this device.

```reflect
- Something you expected before running a cell that turned out differently
- The one idea from this page you could explain to someone else now
- Something you would change or try next, if there were time
- A question this page raised for you that it did not answer. Bring it to the next session; these questions are where the next session starts.
```
