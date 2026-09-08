---
title: "01-forward-pass-colour-classifier-page-2 (2 of 3)"
slug: 01-forward-pass-colour-classifier-page-2
course: ai-and-ml-foundations
course_title: "AI and ML Foundations"
series: 5-neural-networks
series_title: "Neural Networks"
version: 2026.09.06.1
---

Before starting this page, run the cell below. It repeats the imports and definitions from the earlier pages that this page uses.

```python exec
id: 01-forward-pass-colour-classifier-page-2-setup
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
```

## Part 3: A complete forward pass by hand

Before we write any code, we trace the colour **(150, 20, 180)** — a moderately purple lavender — through the network using the parameter values from the table above. This sequence of steps is called the **forward pass**, and every run of the network, on any input, follows exactly this sequence.

There is no shortcut here. Working through each step once by hand means that when we write the code, we are translating something we already understand rather than copying something we do not.

---

### Step 1: Normalise the inputs

Raw RGB values run from 0 to 255. Before they enter the network we divide each channel by 255, bringing every value into the range 0 to 1. This is called **normalisation**. It prevents large numbers from dominating the weighted sums — a red value of 200 should not outweigh a weight of 0.5 simply because it is expressed on a bigger scale. We will revisit this in Tutorial B when we discuss what happens if we skip it.

```
red_normalised   = 150 / 255 ≈ 0.588
green_normalised =  20 / 255 ≈ 0.078
blue_normalised  = 180 / 255 ≈ 0.706
```

---

### Step 2: Hidden node H1 — the weighted sum

Each input is multiplied by its weight and the products are added together. This is called the **dot product**.

```
dot product = (0.4 × 0.588) + (−0.1 × 0.078) + (0.7 × 0.706)
            =  0.2353        +  (−0.0078)      +  0.4941
            =  0.7216
```

Adding the bias gives the **pre-activation value** — the raw signal before the activation function shapes it.

```
pre_activation_value = 0.7216 + 0.1 = 0.8216
```

---

### Step 3: Hidden node H1 — apply ReLU

The hidden layer uses **ReLU** (Rectified Linear Unit): pass positive values through unchanged, and replace any negative value with zero.

```
relu(0.8216) = 0.8216     ← positive, so it passes through unchanged
```

**H1 outputs 0.8216.**

---

### Step 4: Hidden node H2 — weighted sum and bias

```
dot product = (−0.2 × 0.588) + (0.3 × 0.078) + (0.5 × 0.706)
            =  −0.1176        +  0.0235        +  0.3529
            =   0.2588

pre_activation_value = 0.2588 + (−0.05) = 0.2088
```

---

### Step 5: Hidden node H2 — apply ReLU

```
relu(0.2088) = 0.2088     ← positive, so it passes through unchanged
```

**H2 outputs 0.2088.**

---

### Step 6: Output node — weighted sum and bias

The output node receives the two hidden outputs [0.8216, 0.2088] as its inputs.

```
dot product = (0.9 × 0.8216) + (0.6 × 0.2088)
            =  0.7394         +  0.1253
            =  0.8647

pre_activation_value = 0.8647 + (−0.3) = 0.5647
```

---

### Step 7: Output node — apply sigmoid

The output layer uses **sigmoid** rather than ReLU. Sigmoid squashes any real number into the range (0, 1), which makes the result interpretable as a confidence score. A score of 0.5 means maximum uncertainty; scores toward 1.0 mean strong confidence that the colour is purple.

```
sigmoid(x) = 1 / (1 + e^(−x))

sigmoid(0.5647) = 1 / (1 + e^(−0.5647))
               ≈ 1 / 1.5684
               ≈ 0.6375
```

---

### Step 8: The decision

```
confidence score = 0.6375
threshold        = 0.5

0.6375 ≥ 0.5  →  prediction: PURPLE
```

The network is not certain — fully confident would be close to 1.0 — but it leans in the right direction for this colour.

---

### The pattern we just followed

Every forward pass, on every colour, follows this exact sequence: normalise, then for each layer compute the dot product, add the bias, apply the activation function. Our target for the code: `network.forward([0.588, 0.078, 0.706])` returns `[0.6375]`.

## Part 4: What we need to implement

The walkthrough used three distinct calculations and needed two classes to organise them. Here is the full list of what we are about to build, in the order we will build it.

**Three standalone functions** — each one corresponds directly to a step in the walkthrough:
- `dot_product(weights, input_values)` — the weighted sum in Steps 2, 4, 6
- `relu(pre_activation_value)` — the hidden layer activation in Steps 3, 5
- `sigmoid(pre_activation_value)` — the output layer activation in Step 7

**Two classes:**
- `Node` — holds one node's weights, bias, and activation type; its `forward()` method runs one pair of steps from the walkthrough (dot product + bias + activation)
- `NeuralNetwork` — holds the layers as lists of nodes; its `forward()` method chains everything together

We will verify each piece against the walkthrough numbers before moving on. By the time we reach `NeuralNetwork`, the only new thing it introduces is the idea of chaining — everything else is already familiar.

## Part 5: Implementing the building blocks

### 5a. The dot product

The dot product multiplies corresponding elements of two lists and sums the results. In the walkthrough this appeared in Steps 2, 4, and 6 — once per node. It is the single most repeated operation in the forward pass, so naming it clearly matters.

The function takes `weights` and `input_values` as separate arguments because they play different roles: weights are owned by the node and change during training, inputs arrive fresh with each forward pass.

```python exec
id: 01-forward-pass-colour-classifier-page-2-1
def dot_product(weights: list[float], input_values: list[float]) -> float:
    """Returns the weighted sum of input_values under weights."""
    return sum(weight * input_value
               for weight, input_value in zip(weights, input_values))
```

```python exec
id: 01-forward-pass-colour-classifier-page-2-2
# Verify against Step 2 of the walkthrough — expected 0.7216
normalised_red   = 150 / 255
normalised_green =  20 / 255
normalised_blue  = 180 / 255

result = dot_product([0.4, -0.1, 0.7],
                     [normalised_red, normalised_green, normalised_blue])
print(f"dot_product result: {result:.4f}   (expected 0.7216)")
```

### 5b. ReLU

ReLU is the activation function for the hidden layer. Its job is to decide how strongly a node "fires" given its pre-activation value. Positive values pass through unchanged — the node fires proportionally. Negative values become zero — the node does not fire at all.

This gating behaviour is what allows different nodes to specialise. A node that produces a negative pre-activation value for a given input contributes nothing to the next layer for that input. It has learned not to respond to that pattern.

```python exec
id: 01-forward-pass-colour-classifier-page-2-3
def relu(pre_activation_value: float) -> float:
    """Returns pre_activation_value if positive, zero otherwise."""
    return max(0.0, pre_activation_value)
```

```python exec
id: 01-forward-pass-colour-classifier-page-2-4
# Both walkthrough values were positive — both should pass through unchanged
print(f"relu(0.8216) = {relu(0.8216):.4f}   (Step 3, expected 0.8216)")
print(f"relu(0.2088) = {relu(0.2088):.4f}   (Step 5, expected 0.2088)")
print(f"relu(-0.400) = {relu(-0.400):.4f}   (negative input — output is zero)")
```

### 5c. Sigmoid

Sigmoid is the activation function for the output layer. Unlike ReLU, which can produce any non-negative value, sigmoid always outputs a number strictly between 0 and 1. This makes the output directly interpretable as a degree of confidence.

The key behaviours to notice: sigmoid(0) = 0.5 exactly (no information either way), large positive inputs approach 1.0, and large negative inputs approach 0.0. The function is never exactly 0 or 1 — it can only approach those limits asymptotically.

```python exec
id: 01-forward-pass-colour-classifier-page-2-5
import math

def sigmoid(pre_activation_value: float) -> float:
    """Maps any real number to a value strictly between 0 and 1."""
    return 1.0 / (1.0 + math.exp(-pre_activation_value))
```

```python exec
id: 01-forward-pass-colour-classifier-page-2-6
# Verify against Step 7 of the walkthrough — expected 0.6375
print(f"sigmoid(0.5647) = {sigmoid(0.5647):.4f}   (Step 7, expected 0.6375)")
print()
# Explore its shape across a range of inputs
for value in [-5.0, -2.0, 0.0, 2.0, 5.0]:
    print(f"  sigmoid({value:5.1f}) = {sigmoid(value):.4f}")
```

```python exec
id: 01-forward-pass-colour-classifier-page-2-7
import matplotlib.pyplot as plt

input_range     = [x / 10.0 for x in range(-50, 51)]
sigmoid_outputs = [sigmoid(value) for value in input_range]

plt.figure(figsize=(7, 3.5))
plt.plot(input_range, sigmoid_outputs, color="steelblue", linewidth=2)
plt.axhline(0.5, color="black", linestyle="-", linewidth=0.8, label="threshold = 0.5")
plt.axvline(0.0, color="red", linestyle=":",  linewidth=0.8)
plt.xlabel("pre-activation value")
plt.ylabel("confidence score")
plt.title("The sigmoid function")
plt.legend()
plt.tight_layout()
plt.show()
```

## Looking back

Before leaving this page, a sentence on each. What you write stays on this device.

```reflect
- Something you expected before running a cell that turned out differently
- The one idea from this page you could explain to someone else now
- Something you would change or try next, if there were time
- A question this page raised for you that it did not answer. Bring it to the next session; these questions are where the next session starts.
```
