---
title: "05-handwritten-letters-emnist-page-2 (2 of 2)"
slug: 05-handwritten-letters-emnist-page-2
course: ai-and-ml-foundations
course_title: "AI and ML Foundations"
series: 5-neural-networks
series_title: "Neural Networks"
version: 2026.09.06.1
---

Before starting this page, run the cell below. It repeats the imports and definitions from the earlier pages that this page uses.

```python exec
id: 05-handwritten-letters-emnist-page-2-setup
import numpy as np
import matplotlib.pyplot as plt
from random import random, seed, shuffle
from math import exp

import numpy as np
import matplotlib.pyplot as plt
from random import random, seed, shuffle
from math import exp

# For reproducible results
seed(42)
np.random.seed(42)

print("Setup complete.")

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

# A neuron with 2 inputs
weights = [0.5, -0.3, 0.1]  # Two weights plus bias
inputs = [2.0, 4.0]

# Step 1: Calculate weighted sum
pre_activation = calculate_activation(weights, inputs)
print(f"Pre_activation (weighted sum): {pre_activation}")

# Step 2: Apply sigmoid
output = sigmoid(pre_activation)
print(f"Output (after sigmoid): {output}")

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

## Part 3: Learning from Mistakes - Backpropagation

Here's the key insight: if we know how wrong the network is, we can figure out how to adjust each weight to make it less wrong. This is backpropagation - sending error signals backward through the network.

### Step 3.1: The Sigmoid Derivative

To know how much to adjust a weight, we need to know how sensitive the output is to changes. For the sigmoid function, there's a beautiful result:

$$\frac{d}{dx}\sigma(x) = \sigma(x) \times (1 - \sigma(x))$$

In other words, once we know the output, we can easily calculate the derivative!

```python exec
id: 05-handwritten-letters-emnist-page-2-1
def sigmoid_derivative(output: float) -> float:
    """
    Calculate the derivative of sigmoid given its output.

    This tells us how sensitive the output is to changes in input.

    Parameters:
        output: The output of the sigmoid function (not the input!)

    Returns:
        The derivative at that point
    """
    return output * (1.0 - output)
```

### Exploration 3.1: Visualising the Derivative

Let's see how the derivative varies:

```python exec
id: 05-handwritten-letters-emnist-page-2-2
# Output values range from 0 to 1
output_values = np.linspace(0.01, 0.99, 100)

# Calculate derivative for each
derivative_values = [sigmoid_derivative(o) for o in output_values]

plt.figure(figsize=(10, 5))
plt.plot(output_values, derivative_values, linewidth=2)
plt.xlabel('Sigmoid Output')
plt.ylabel('Derivative')
plt.title('Sigmoid Derivative: How Sensitive is the Output?')
plt.grid(True, alpha=0.3)
plt.show()

print("Notice: The derivative is highest at output = 0.5")
print(f"At output = 0.5, derivative = {sigmoid_derivative(0.5):.4f}")
print(f"At output = 0.1, derivative = {sigmoid_derivative(0.1):.4f}")
print(f"At output = 0.9, derivative = {sigmoid_derivative(0.9):.4f}")
```

### Reflection 3.1

The derivative is largest around 0.5 and smallest near 0 or 1. What does this mean?
- When the neuron is "uncertain" (output near 0.5), small changes in weights have big effects
- When the neuron is "confident" (output near 0 or 1), it's harder to change

This can cause the "vanishing gradient" problem in deep networks, but for our simple network it's fine.

---

### Step 3.2: Calculating Error Signals

Backpropagation works in two stages:

**For output neurons**: The error is simply how wrong we were:
$$\text{error} = (\text{output} - \text{expected})$$

Then we multiply by the derivative to get the "delta" (how much to blame this neuron):
$$\delta = \text{error} \times \sigma'(\text{output})$$

**For hidden neurons**: We don't have a direct expected value, so we use the errors from the next layer:
$$\text{error} = \sum (\text{weight}_{ij} \times \delta_j)$$

Then multiply by the derivative as before.

```python exec
id: 05-handwritten-letters-emnist-page-2-3
def backward_propagate_error(network: list, expected: list) -> None:
    """
    Propagate error backward through the network.

    Calculates the 'delta' (error signal) for each neuron,
    storing it in the neuron dictionary.

    Parameters:
        network: The neural network (must have 'output' values from forward pass)
        expected: The expected output values

    Returns:
        None (modifies network in place)
    """
    # Work backward through layers
    for layer_index in reversed(range(len(network))):
        layer = network[layer_index]
        errors = []

        if layer_index == len(network) - 1:
            # Output layer: error = output - expected
            for neuron_index, neuron in enumerate(layer):
                error = neuron['output'] - expected[neuron_index]
                errors.append(error)
        else:
            # Hidden layer: error comes from next layer
            for neuron_index in range(len(layer)):
                error = 0.0
                next_layer = network[layer_index + 1]
                for neuron in next_layer:
                    # This neuron's contribution to the next layer's error
                    error = error + neuron['weights'][neuron_index] * neuron['delta']
                errors.append(error)

        # Calculate delta for each neuron
        for neuron_index, neuron in enumerate(layer):
            neuron['delta'] = errors[neuron_index] * sigmoid_derivative(neuron['output'])
```

### Exploration 3.2: Seeing Backpropagation in Action

Let's trace through backpropagation:

```python exec
id: 05-handwritten-letters-emnist-page-2-4
# Use our tiny network from before
seed(1)
tiny_network = create_network(n_inputs=2, n_hidden=2, n_outputs=2)

# Forward pass
test_input = [1.0, 0.5]
outputs = forward_propagate(tiny_network, test_input)
print("Forward pass:")
print(f"  Outputs: {[round(o, 4) for o in outputs]}")

# Suppose we wanted [1, 0] (first class)
expected = [1.0, 0.0]
print(f"  Expected: {expected}")
print()

# Backward pass
backward_propagate_error(tiny_network, expected)

print("Backward pass (deltas):")
print("  Output layer:")
for i, neuron in enumerate(tiny_network[1]):
    print(f"    Neuron {i}: output={neuron['output']:.4f}, delta={neuron['delta']:.4f}")

print("  Hidden layer:")
for i, neuron in enumerate(tiny_network[0]):
    print(f"    Neuron {i}: output={neuron['output']:.4f}, delta={neuron['delta']:.4f}")
```

---

## Part 4: Updating Weights - The Learning Step

Now we know each neuron's delta. The final step is using this to update the weights.

The update rule is:
$$\text{new weight} = \text{old weight} - \text{learning rate} \times \delta \times \text{input}$$

The **learning rate** controls how big the steps are. Too big and we might overshoot; too small and learning is slow.

```python exec
id: 05-handwritten-letters-emnist-page-2-5
def update_weights(network: list, row: list, learning_rate: float) -> None:
    """
    Update network weights using the calculated deltas.

    Parameters:
        network: The neural network (must have 'delta' values from backprop)
        row: The input that was used (for the hidden layer inputs)
        learning_rate: How much to adjust weights (typically 0.1 to 0.5)

    Returns:
        None (modifies network in place)
    """
    for layer_index in range(len(network)):
        # Get inputs for this layer
        if layer_index == 0:
            inputs = row
        else:
            inputs = [neuron['output'] for neuron in network[layer_index - 1]]

        # Update each neuron's weights
        for neuron in network[layer_index]:
            for input_index in range(len(inputs)):
                neuron['weights'][input_index] -= learning_rate * neuron['delta'] * inputs[input_index]
            # Update bias (last weight)
            neuron['weights'][-1] -= learning_rate * neuron['delta']
```

---

## Part 5: Putting It All Together - Training

Training is just repeating these steps many times:
1. Forward propagate an example
2. Calculate the error
3. Backpropagate the error
4. Update the weights

Do this for all examples, and repeat the whole process (called an "epoch") until the network learns.

```python exec
id: 05-handwritten-letters-emnist-page-2-6
def train_network(network: list, training_data: list, learning_rate: float,
                  n_epochs: int, n_outputs: int) -> list:
    """
    Train the network on the provided data.

    Parameters:
        network: The neural network to train
        training_data: List of samples, each sample is a list with features + class label
        learning_rate: How much to adjust weights each step
        n_epochs: How many times to go through all the data
        n_outputs: Number of output classes

    Returns:
        List of errors for each epoch (for plotting)
    """
    error_history = []

    for epoch in range(n_epochs):
        sum_error = 0.0

        for row in training_data:
            # Forward pass
            outputs = forward_propagate(network, row)

            # Create expected output (one-hot encoding)
            expected = [0.0] * (n_outputs) # the number of outputs are the number of possible "labels" in this case 0, 1, 2, 3, 4, ..., 9
            digit_label = int(row[-1]) # label is last entry of row (in our data)
            expected[digit_label] = 1.0 # the last entry of row is the digit (say, 7)

            # Calculate error for this sample
            for i in range(n_outputs):
                sum_error += (expected[i] - outputs[i]) ** 2

            # Backward pass
            backward_propagate_error(network, expected)

            # Update weights
            update_weights(network, row, learning_rate)

        error_history.append(sum_error)

        # Print progress every 100 epochs
        if (epoch + 1) % 100 == 0 or epoch == 0:
            print(f"Epoch {epoch + 1:4d}: error = {sum_error:.4f}")

    return error_history
```

### Step 5.1: Making Predictions

Once trained, making predictions is simple - just forward propagate and pick the output with the highest value:

```python exec
id: 05-handwritten-letters-emnist-page-2-7
def predict(network: list, row: list) -> int:
    """
    Make a prediction with a trained network.

    Parameters:
        network: A trained neural network
        row: Input features

    Returns:
        The predicted class (index of highest output)
    """
    outputs = forward_propagate(network, row)
    return outputs.index(max(outputs))
```

---

## Part 6: Testing on Simple Data

Before tackling handwritten letters, let's make sure everything works on a simple problem.

```python exec
id: 05-handwritten-letters-emnist-page-2-8
# A simple 2-class dataset (the same one used in the original tutorial)
# Each row: [x1, x2, class]
simple_dataset = [
    [2.7810836, 2.550537003, 0],
    [1.465489372, 2.362125076, 0],
    [3.396561688, 4.400293529, 0],
    [1.38807019, 1.850220317, 0],
    [3.06407232, 3.005305973, 0],
    [7.627531214, 2.759262235, 1],
    [5.332441248, 2.088626775, 1],
    [6.922596716, 1.77106367, 1],
    [8.675418651, -0.242068655, 1],
    [7.673756466, 3.508563011, 1]
]

# Visualise it
plt.figure(figsize=(8, 6))
for row in simple_dataset:
    color = 'blue' if row[2] == 0 else 'red'
    plt.scatter(row[0], row[1], c=color, s=100)
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.title('Simple Dataset: Can the Network Separate Blue from Red?')
plt.legend(['Class 0 (blue)', 'Class 1 (red)'])
plt.grid(True, alpha=0.3)
plt.show()
```

```python exec
id: 05-handwritten-letters-emnist-page-2-9
# Create and train a network
seed(1)
n_inputs = 2
n_hidden = 5
n_outputs = 2

network = create_network(n_inputs, n_hidden, n_outputs)

print("Training...")
print()
error_history = train_network(network, simple_dataset, learning_rate=0.5,
                              n_epochs=500, n_outputs=n_outputs)
```

```python exec
id: 05-handwritten-letters-emnist-page-2-10
# Plot the learning curve
plt.figure(figsize=(10, 5))
plt.plot(error_history)
plt.xlabel('Epoch')
plt.ylabel('Sum Squared Error')
plt.title('Learning Curve: Error Decreases Over Time')
plt.grid(True, alpha=0.3)
plt.show()
```

```python exec
id: 05-handwritten-letters-emnist-page-2-11
# Test predictions
print("Testing predictions:")
print()
correct = 0
for row in simple_dataset:
    prediction = predict(network, row)
    actual = int(row[-1])
    match = "correct" if prediction == actual else "WRONG"
    print(f"Expected: {actual}, Predicted: {prediction} ({match})")
    if prediction == actual:
        correct += 1

print()
print(f"Accuracy: {correct}/{len(simple_dataset)} = {100*correct/len(simple_dataset):.1f}%")
```

### Reflection 6.1

The network learned to classify this simple dataset. Notice how:
- The error decreases over epochs (the learning curve)
- The network achieves high accuracy on the training data

This confirms our implementation is working. Now let's try something more challenging.

---

---

## Part 8: Understanding What We Built

Let's step back and see the complete picture.

### The Complete Neural Network Code

Here are all our functions together - remarkably few lines for something so powerful:

```python exec
id: 05-handwritten-letters-emnist-page-2-12
# ============================================================
# COMPLETE NEURAL NETWORK FROM SCRATCH
# ============================================================

from random import random, seed
from math import exp

# --- Building Blocks ---

def calculate_activation(weights, inputs):
    """Calculate weighted sum of inputs plus bias."""
    activation = weights[-1]  # Bias
    for i in range(len(weights) - 1):
        activation += weights[i] * inputs[i]
    return activation

def sigmoid(x):
    """Squash value to range (0, 1)."""
    return 1.0 / (1.0 + exp(-x))

def sigmoid_derivative(output):
    """Derivative of sigmoid for backpropagation."""
    return output * (1.0 - output)

# --- Network Structure ---

def create_network(n_inputs, n_hidden, n_outputs):
    """Create a network with random weights."""
    network = []
    hidden = [{'weights': [random() for _ in range(n_inputs + 1)]}
              for _ in range(n_hidden)]
    output = [{'weights': [random() for _ in range(n_hidden + 1)]}
              for _ in range(n_outputs)]
    network.append(hidden)
    network.append(output)
    return network

# --- Forward Pass ---

def forward_propagate(network, row):
    """Push input through the network."""
    inputs = row
    for layer in network:
        new_inputs = []
        for neuron in layer:
            activation = calculate_activation(neuron['weights'], inputs)
            neuron['output'] = sigmoid(activation)
            new_inputs.append(neuron['output'])
        inputs = new_inputs
    return inputs

# --- Backward Pass ---

def backward_propagate_error(network, expected):
    """Calculate error signals for all neurons."""
    for i in reversed(range(len(network))):
        layer = network[i]
        errors = []
        if i == len(network) - 1:
            for j, neuron in enumerate(layer):
                errors.append(neuron['output'] - expected[j])
        else:
            for j in range(len(layer)):
                error = sum(n['weights'][j] * n['delta'] for n in network[i + 1])
                errors.append(error)
        for j, neuron in enumerate(layer):
            neuron['delta'] = errors[j] * sigmoid_derivative(neuron['output'])

def update_weights(network, row, learning_rate):
    """Adjust weights based on error signals."""
    for i, layer in enumerate(network):
        inputs = row if i == 0 else [n['output'] for n in network[i - 1]]
        for neuron in layer:
            for j in range(len(inputs)):
                neuron['weights'][j] -= learning_rate * neuron['delta'] * inputs[j]
            neuron['weights'][-1] -= learning_rate * neuron['delta']

# --- Training and Prediction ---

def train_network(network, data, learning_rate, n_epochs, n_outputs):
    """Train the network on data."""
    for epoch in range(n_epochs):
        for row in data:
            forward_propagate(network, row)
            expected = [0.0] * n_outputs
            expected[int(row[-1])] = 1.0
            backward_propagate_error(network, expected)
            update_weights(network, row, learning_rate)

def predict(network, row):
    """Make a prediction."""
    outputs = forward_propagate(network, row)
    return outputs.index(max(outputs))

print("Complete neural network implementation: ~60 lines of core code.")
```

---

## Your Turn: Experiments

Now that you understand how it works, try some experiments:

### Experiment 1: Network Architecture

What happens if you change the number of hidden neurons?

```python exec
id: 05-handwritten-letters-emnist-page-2-13
# Try different numbers of hidden neurons (5, 10, 20, 50)
# How does it affect accuracy? Training time?
```

---

## Summary

We've built a complete neural network from scratch. The key ideas:

**Forward Propagation**: Information flows from input to output
- Each neuron computes a weighted sum
- The sigmoid function squashes outputs to (0, 1)
- One layer's outputs become the next layer's inputs

**Backpropagation**: Errors flow backward to update weights
- Output error: how wrong were we?
- Hidden error: weighted sum of downstream errors
- Delta: error multiplied by sigmoid derivative
- Weight update: move in the direction that reduces error

**Training**: Repeat forward and backward passes many times
- Each epoch goes through all training data
- Error decreases over time (usually!)
- Learning rate controls step size

### What's Next?

This foundation prepares you for:
- Deeper networks (more hidden layers)
- Different activation functions (ReLU, tanh)
- Convolutional networks (for better image recognition)
- Regularisation (preventing overfitting)
- Modern frameworks (PyTorch, TensorFlow)

The principles remain the same - forward pass, backward pass, update weights. Libraries just make it faster and easier to build complex architectures.

---

## Reflection

Take a moment to think about:
1. What part of the neural network was most surprising to you?
2. Where do you see the mathematics at work?
3. What would you want to explore further?
4. How might you apply this to a problem you care about?

```python exec
id: 05-handwritten-letters-emnist-page-2-14
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
# Your reflections here:
#
#
#
```

## Looking back

Before leaving this page, a sentence on each. What you write stays on this device.

```reflect
- Something you expected before running a cell that turned out differently
- The one idea from this page you could explain to someone else now
- Something you would change or try next, if there were time
- A question this page raised for you that it did not answer. Bring it to the next session; these questions are where the next session starts.
```
