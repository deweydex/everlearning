---
title: "01-forward-pass-colour-classifier-page-3 (3 of 3)"
slug: 01-forward-pass-colour-classifier-page-3
course: ai-and-ml-foundations
course_title: "AI and ML Foundations"
series: 5-neural-networks
series_title: "Neural Networks"
version: 2026.09.06.1
---

Before starting this page, run the cell below. It repeats the imports and definitions from the earlier pages that this page uses.

```python exec
id: 01-forward-pass-colour-classifier-page-3-setup
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import math

import matplotlib.pyplot as plt
import matplotlib.patches as patches

colour_samples = [
    ((148,   0, 211), "violet\n(148, 0, 211)"),
    ((128,   0, 128), "purple\n(128, 0, 128)"),
    ((180,  50, 200), "lavender\n(180, 50, 200)"),
    ((255, 165,   0), "orange\n(255, 165, 0)"),
    ((255, 140,   0), "dark orange\n(255, 140, 0)"),
    ((  0, 128,   0), "green\n(0, 128, 0)"),
    ((  0,   0, 255), "blue\n(0, 0, 255)"),
]

fig, axes = plt.subplots(1, len(colour_samples), figsize=(14, 2.5))
for axis, (rgb_values, label) in zip(axes, colour_samples):
    normalised_rgb = tuple(channel / 255 for channel in rgb_values)
    axis.add_patch(patches.Rectangle((0, 0), 1, 1, color=normalised_rgb))
    axis.set_xlim(0, 1)
    axis.set_ylim(0, 1)
    axis.axis("off")
    axis.set_title(label, fontsize=8)

plt.suptitle("Colour samples with RGB values", y=1.05)
plt.tight_layout()
plt.show()

import matplotlib.pyplot as plt
import math

fig, ax = plt.subplots(figsize=(10, 6))
ax.set_xlim(0, 10)
ax.set_ylim(0, 6.5)
ax.axis("off")

node_radius = 0.40
input_nodes  = {"R": (1.5, 5.0), "G": (1.5, 3.0), "B": (1.5, 1.0)}
hidden_nodes = {"H1": (5.0, 4.3), "H2": (5.0, 1.7)}
output_nodes = {"out": (8.5, 3.0)}

def draw_node(ax, x, y, label, face_color, edge_color, fontsize=12):
    ax.add_patch(plt.Circle((x, y), node_radius,
                             facecolor=face_color, edgecolor=edge_color,
                             linewidth=2.0, zorder=3))
    ax.text(x, y, label, ha="center", va="center", fontsize=fontsize,
            color="white", fontweight="bold", zorder=4)

def draw_edge(ax, x1, y1, x2, y2, color="#BBBBBB"):
    dx, dy = x2 - x1, y2 - y1
    length = math.sqrt(dx**2 + dy**2)
    ux, uy = dx / length, dy / length
    ax.annotate("", xy=(x2 - ux*(node_radius+0.05), y2 - uy*(node_radius+0.05)),
                xytext=(x1 + ux*node_radius, y1 + uy*node_radius),
                arrowprops=dict(arrowstyle="-|>", color=color, lw=1.4, mutation_scale=15),
                zorder=2)

for ix, iy in input_nodes.values():
    for hx, hy in hidden_nodes.values():
        draw_edge(ax, ix, iy, hx, hy)
for hx, hy in hidden_nodes.values():
    draw_edge(ax, hx, hy, *output_nodes["out"], color="#999999")

for label, (x, y) in input_nodes.items():
    draw_node(ax, x, y, label, "#3A7DC9", "#2260A8")
    ax.annotate("", xy=(x - node_radius, y), xytext=(0.55, y),
                arrowprops=dict(arrowstyle="-|>", color="#3A7DC9", lw=1.4, mutation_scale=14))
for label, (x, y) in hidden_nodes.items():
    draw_node(ax, x, y, label, "#7040A0", "#5A2D80")
    ax.text(x + 0.48, y - 0.48, "+b", fontsize=8, color="#9966CC",
            ha="left", va="top", style="italic")

ox, oy = output_nodes["out"]
draw_node(ax, ox, oy, "out", "#2A7A50", "#1D5C3A")
ax.text(ox + 0.48, oy - 0.48, "+b", fontsize=8, color="#44AA77",
        ha="left", va="top", style="italic")
ax.annotate("", xy=(9.75, oy), xytext=(ox + node_radius, oy),
            arrowprops=dict(arrowstyle="-|>", color="#2A7A50", lw=1.4, mutation_scale=14))
ax.text(9.82, oy + 0.12, "confidence", ha="left", va="bottom", fontsize=8.5, color="#2A7A50")
ax.text(9.82, oy - 0.12, "score",      ha="left", va="top",    fontsize=8.5, color="#2A7A50")

for x, label, color in [
    (1.5, "Input layer",             "#3A7DC9"),
    (5.0, "Hidden layer  (ReLU)",    "#7040A0"),
    (8.5, "Output layer  (Sigmoid)", "#2A7A50"),
]:
    ax.text(x, 6.15, label, ha="center", fontsize=10.5, color=color, fontweight="bold")

for x in [3.0, 6.8]:
    ax.axvline(x, color="#DDDDDD", lw=1.0, zorder=0)

plt.tight_layout()
plt.show()

def dot_product(weights: list[float], input_values: list[float]) -> float:
    """Returns the weighted sum of input_values under weights."""
    return sum(weight * input_value
               for weight, input_value in zip(weights, input_values))

# Verify against Step 2 of the walkthrough — expected 0.7216
normalised_red   = 150 / 255
normalised_green =  20 / 255
normalised_blue  = 180 / 255

result = dot_product([0.4, -0.1, 0.7],
                     [normalised_red, normalised_green, normalised_blue])
print(f"dot_product result: {result:.4f}   (expected 0.7216)")

def relu(pre_activation_value: float) -> float:
    """Returns pre_activation_value if positive, zero otherwise."""
    return max(0.0, pre_activation_value)

import math

def sigmoid(pre_activation_value: float) -> float:
    """Maps any real number to a value strictly between 0 and 1."""
    return 1.0 / (1.0 + math.exp(-pre_activation_value))
```

## Part 6: The Node class

We now have the three functions. A `Node` wraps them together with the parameters they operate on: a list of weights (one per input the node receives) and a bias.

The `activation` argument is a string — `"relu"` for hidden nodes, `"sigmoid"` for the output node. Keeping it as a string rather than passing the function directly makes the object easy to inspect: we can print a node and read its activation type without needing to decode a function reference.

Two design decisions in `__init__` are worth understanding:

- Weights are initialised with small random values from a normal distribution centred at zero. If all weights started at the same value, every node in a layer would compute the same output and update in the same direction — the layer would never differentiate. Random initialisation breaks that symmetry.
- The bias starts at zero. Unlike weights, there is no symmetry problem with identical biases, and zero is a neutral starting point that does not push the node in any direction before training begins.

```python exec
id: 01-forward-pass-colour-classifier-page-3-1
import random

class Node:
    """A single neuron: weights, bias, and an activation function."""

    def __init__(self, num_inputs: int, activation: str = "relu"):
        # Small random weights to break symmetry between nodes in the same layer
        self.weights: list[float] = [random.gauss(0, 0.5) for _ in range(num_inputs)]
        self.bias: float = 0.0          # neutral starting point
        self.activation: str = activation

    def forward(self, input_values: list[float]) -> float:
        """Returns the output of this node for the given input_values."""
        pre_activation_value = dot_product(self.weights, input_values) + self.bias
        if self.activation == "relu":
            return relu(pre_activation_value)
        elif self.activation == "sigmoid":
            return sigmoid(pre_activation_value)
```

```python exec
id: 01-forward-pass-colour-classifier-page-3-2
# Set up H1 and H2 with the walkthrough weights and verify
normalised_inputs = [normalised_red, normalised_green, normalised_blue]

node_H1 = Node(num_inputs=3, activation="relu")
node_H1.weights = [0.4, -0.1, 0.7]
node_H1.bias    = 0.1

node_H2 = Node(num_inputs=3, activation="relu")
node_H2.weights = [-0.2, 0.3, 0.5]
node_H2.bias    = -0.05

print(f"H1 output: {node_H1.forward(normalised_inputs):.4f}   (expected 0.8216)")
print(f"H2 output: {node_H2.forward(normalised_inputs):.4f}   (expected 0.2088)")
```

## Part 7: The NeuralNetwork class

The network groups nodes into layers and provides a single `forward()` method that chains them together. The constructor takes three arguments:

- `num_inputs` — how many values flow in (3 for R, G, B)
- `hidden_sizes` — a list of node counts, one per hidden layer (e.g. `[2]` for our single hidden layer of two nodes)
- `num_outputs` — how many output nodes to create

One line in the constructor is worth reading carefully:

```python
num_inputs_per_layer = [num_inputs] + hidden_sizes[:-1]
```

This builds a list where `num_inputs_per_layer[i]` is the input count for hidden layer `i`. For our 3-2-1 network it produces `[3]` — meaning the one hidden layer has 3 inputs. If we had two hidden layers of sizes `[4, 2]` it would produce `[3, 4]`, meaning the first hidden layer takes 3 inputs and the second takes 4 (the outputs of the first). The slice `[:-1]` drops the last hidden size because no hidden layer needs to receive its own outputs as inputs.

The `forward()` method is the direct translation of our walkthrough: pass the inputs through each hidden layer in turn, then through the output layer.

```python exec
id: 01-forward-pass-colour-classifier-page-3-3
class NeuralNetwork:
    """A feedforward network of Node objects, built from layer size specifications."""

    def __init__(self, num_inputs: int, hidden_sizes: list[int], num_outputs: int):
        # Each hidden layer receives outputs from the layer before it.
        # Prepend num_inputs so index i gives the input count for hidden layer i.
        num_inputs_per_layer = [num_inputs] + hidden_sizes[:-1]

        self.hidden_layers: list[list[Node]] = [
            [Node(num_inputs_per_layer[layer_index], activation="relu")
             for _ in range(num_nodes_in_this_layer)]
            for layer_index, num_nodes_in_this_layer in enumerate(hidden_sizes)
        ]

        num_inputs_to_output_layer = hidden_sizes[-1] if hidden_sizes else num_inputs
        self.output_layer: list[Node] = [
            Node(num_inputs_to_output_layer, activation="sigmoid")
            for _ in range(num_outputs)
        ]

    def forward(self, input_values: list[float]) -> list[float]:
        """Passes input_values through all layers and returns the output layer values."""
        current_layer_inputs = input_values
        for hidden_layer in self.hidden_layers:
            current_layer_inputs = [
                node.forward(current_layer_inputs) for node in hidden_layer
            ]
        outputs = [node.forward(current_layer_inputs) for node in self.output_layer]
        return outputs
    def predict(self, input_values: list[float], threshold: float = 0.5) -> list[int]:
        """Returns 1 for each output where confidence >= threshold, 0 elsewhere."""
        return [1 if score >= threshold else 0
                for score in self.forward(input_values)]
```

## Part 8: Verifying against the walkthrough

We now have everything. Let us set the network's weights and biases to match the walkthrough exactly and confirm that `forward()` returns 0.6375. If it does, the implementation is correct. If it does not, we have a specific discrepancy to investigate.

```python exec
id: 01-forward-pass-colour-classifier-page-3-4
random.seed(0)
purple_detector = NeuralNetwork(num_inputs=3, hidden_sizes=[2], num_outputs=1)

purple_detector.hidden_layers[0][0].weights = [ 0.4, -0.1,  0.7]
purple_detector.hidden_layers[0][0].bias    =  0.1
purple_detector.hidden_layers[0][1].weights = [-0.2,  0.3,  0.5]
purple_detector.hidden_layers[0][1].bias    = -0.05
purple_detector.output_layer[0].weights     = [ 0.9,  0.6]
purple_detector.output_layer[0].bias        = -0.3

confidence_scores = purple_detector.forward(normalised_inputs)
decision          = purple_detector.predict(normalised_inputs)

print(f"forward() output:   {confidence_scores[0]:.4f}   (expected 0.6375)")
print(f"predict() decision: {decision}             (expected [1])")
```

```python exec
id: 01-forward-pass-colour-classifier-page-3-5
import matplotlib.pyplot as plt
import matplotlib.patches as patches

fig, ax = plt.subplots(figsize=(3, 2))
ax.add_patch(patches.Rectangle((0, 0), 1, 1, color=(150/255, 20/255, 180/255)))
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis("off")
ax.set_title(f"(150, 20, 180)\nconfidence: {confidence_scores[0]:.4f}  →  purple")
plt.tight_layout()
plt.show()
```

## Part 9: Exploring what the network thinks

The walkthrough gave us one input and one output. Let us now ask the network to score a whole grid of colours, varying red and blue while holding green low. This will show us what region of colour space the current hand-crafted weights consider purple.

This is not training — the weights are still the values from the table. The purpose is to develop intuition for what a decision boundary looks like and why training is needed to sharpen it.

```python exec
id: 01-forward-pass-colour-classifier-page-3-6
import matplotlib.pyplot as plt

green_fixed = 20 / 255
grid_size   = 40

confidence_grid = []
for blue_step in reversed(range(grid_size)):
    blue_normalised = blue_step / (grid_size - 1)
    confidence_row = []
    for red_step in range(grid_size):
        red_normalised = red_step / (grid_size - 1)
        score = purple_detector.forward([red_normalised, green_fixed, blue_normalised])[0]
        confidence_row.append(score)
    confidence_grid.append(confidence_row)

plt.figure(figsize=(6, 5))
plt.imshow(confidence_grid, extent=[0, 255, 0, 255], aspect="auto",
           cmap="Purples", vmin=0, vmax=1)
plt.colorbar(label="purple confidence score")
plt.xlabel("Red channel (0–255)")
plt.ylabel("Blue channel (0–255)")
plt.title(f"Purple confidence across red/blue space  (green fixed at {green_fixed*255:.0f})")
plt.tight_layout()
plt.show()
```

The gradient from light to dark shows high confidence where both red and blue are elevated — which is where purple genuinely lives. The boundary is smooth rather than sharp because sigmoid produces a gradual transition. Training will learn to move and steepen this boundary to match our labelled examples rather than our hand-crafted guesses.

## Part 10: Extending to two outputs — purple and orange

One of the satisfying things about this architecture is how little changes when we add a second output. We pass `num_outputs=2` and the constructor creates a second sigmoid node in the output layer. Each output node learns its own independent set of weights from the hidden layer. Everything else — the hidden layer, `forward()`, `predict()` — works without modification.

With two outputs, `output[0]` is the purple confidence score and `output[1]` is the orange confidence score.

```python exec
id: 01-forward-pass-colour-classifier-page-3-7
random.seed(1)
colour_classifier = NeuralNetwork(num_inputs=3, hidden_sizes=[2], num_outputs=2)

colour_classifier.hidden_layers[0][0].weights = [ 0.4, -0.1, 0.7]
colour_classifier.hidden_layers[0][0].bias    =  0.1
colour_classifier.hidden_layers[0][1].weights = [-0.2,  0.3, 0.5]
colour_classifier.hidden_layers[0][1].bias    = -0.05

colour_classifier.output_layer[0].weights = [ 0.9,  0.6]   # purple output
colour_classifier.output_layer[0].bias    = -0.3
colour_classifier.output_layer[1].weights = [ 0.7, -0.4]   # orange output (hand-crafted)
colour_classifier.output_layer[1].bias    = -0.2

test_colours = [
    ([150/255,  20/255, 180/255], "purple (150,  20, 180)"),
    ([255/255, 165/255,   0/255], "orange (255, 165,   0)"),
    ([  0/255, 128/255,   0/255], "green  (  0, 128,   0)"),
    ([  0/255,   0/255, 255/255], "blue   (  0,   0, 255)"),
]

print(f"{'Colour':<28} {'Purple':>10} {'Orange':>10}   Decision")
print("-" * 68)
for normalised_colour, colour_label in test_colours:
    scores = colour_classifier.forward(normalised_colour)
    p, o   = scores[0], scores[1]
    if   p >= 0.5 and o <  0.5: decision = "purple"
    elif o >= 0.5 and p <  0.5: decision = "orange"
    elif p >= 0.5 and o >= 0.5: decision = "both above threshold"
    else:                        decision = "neither"
    print(f"{colour_label:<28} {p:>10.4f} {o:>10.4f}   {decision}")
```

Several colours score above 0.5 on both outputs simultaneously. This is not a bug — it is what hand-crafted weights produce when they have not been optimised against real data. It is actually a useful thing to observe: it illustrates exactly why training is necessary. Getting weights that discriminate cleanly between multiple colour classes by hand is much harder than it looks. Tutorial B introduces the algorithm that does this automatically.

## Exercises

These are things worth exploring, not tests to pass. Work through whichever feel interesting and skip any that do not land right now — they will mean more after Tutorial B.

**1. Parameter counting.** The parameter table shows 11 parameters for our 3-2-1 network. Work out how many parameters a 3-4-1 network would have, and how many a 3-2-2 network (two outputs) would have. Write out the count layer by layer — the structure of the count is as useful as the final number.

**2. The gating effect.** Node H1 has weights [0.4, −0.1, 0.7]. In your own words, what combination of R, G, B values would cause this node to produce a large positive pre-activation value? What would cause it to produce a negative one, which ReLU would then gate to zero?

**3. Finding the gate.** Given H2's weights [−0.2, 0.3, 0.5] and bias −0.05, try to construct an RGB colour that you expect will produce a negative pre-activation value for H2. Verify it by calling `node_H2.forward()` on the normalised version and checking that the output is 0.0. It is fine if your first guess is wrong — adjust and try again.

**4. Thresholds.** Call `purple_detector.predict()` with `threshold=0.3` and `threshold=0.7` on several colours. What changes? In what real-world situation might you want a higher threshold? A lower one?

```python exec
id: 01-forward-pass-colour-classifier-page-3-8
# Work through the exercises here
```

## What we covered — and where we are going next

---

### What we covered in this tutorial

We built a complete neural network from scratch, using three standalone functions and two classes:

- **`dot_product`** — the weighted sum at the heart of every node's calculation
- **`relu`** — the hidden layer activation that gates negative signals to zero
- **`sigmoid`** — the output activation that converts any value to a confidence score between 0 and 1
- **`Node`** — a single neuron with its own weights, bias, and activation type
- **`NeuralNetwork`** — a full network that chains nodes into layers and runs the forward pass

We traced one colour all the way through the network by hand before writing any code. That walkthrough is the thing to return to if any part of the implementation feels unclear.

We also saw the network's limitation: with hand-crafted weights it produces reasonable but imprecise decisions. Several colours scored above 0.5 on both outputs, and the confidence heatmap showed a fuzzy boundary. The weights were reasonable guesses, not learned values.

---

### What comes next — and why it matters

Tutorial B introduces **backpropagation**: the algorithm that adjusts the weights and biases automatically, using labelled examples of colours we know to be purple or orange.

The key idea is that the network's error on a training example can be used to compute a gradient — a direction in which each weight should change to reduce that error. Backpropagation works backwards through the network from the output to the input, applying the chain rule from calculus at each step.

This is genuinely the hard part of neural networks, and it took the field decades to develop a clean formulation. We will work through it by hand first, using the same colour and the same network we used here, so the connection between the two tutorials is direct. The code we add to `NeuralNetwork` in Tutorial B will be a translation of that by-hand working — nothing more.

When you come back to this tutorial after completing Tutorial B, the parameter table and the forward pass walkthrough will mean something different: they will be the thing that backpropagation is trying to improve.

## Looking back

Before leaving this page, a sentence on each. What you write stays on this device.

```reflect
- Something you expected before running a cell that turned out differently
- The one idea from this page you could explain to someone else now
- Something you would change or try next, if there were time
- A question this page raised for you that it did not answer. Bring it to the next session; these questions are where the next session starts.
```
