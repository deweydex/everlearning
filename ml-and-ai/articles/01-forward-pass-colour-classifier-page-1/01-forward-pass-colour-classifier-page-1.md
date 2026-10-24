---
title: "Tutorial A: Building a Neural Network from Scratch (1 of 3)"
slug: 01-forward-pass-colour-classifier-page-1
course: ai-and-ml-foundations
course_title: "AI and ML Foundations"
series: 5-neural-networks
series_title: "Neural Networks"
version: 2026.09.06.1
---

# Tutorial A: Building a Neural Network from Scratch
## The Colour Classifier — learning what purple is

---

### What this tutorial is about

We are going to build a small neural network using nothing beyond Python's standard library and Matplotlib. By the end you will have a working network that takes a colour described in red, green, and blue and produces a number expressing how confident it is that the colour is purple.

We do not start with code. We start with the problem, draw the network, and work through the arithmetic by hand — so that every implementation decision we make later has a reason behind it, not just a tradition. Nothing here should feel like magic. Every calculation is something we can point to and explain.

Some of this material takes time to settle. If a step feels unclear on first reading, that is not a sign that you are missing something — it is a normal part of working with ideas that took researchers decades to develop. The by-hand walkthrough in Part 3 is always the thing to return to.

---

### Contents

1. What does purple look like in RGB?
2. The network we are building — diagram and parameters
3. A complete forward pass by hand
4. What we need to implement
5. Implementing the building blocks — `dot_product`, `relu`, `sigmoid`
6. The `Node` class
7. The `NeuralNetwork` class
8. Verifying against the walkthrough
9. Exploring what the network thinks
10. Extending to two outputs
11. Exercises
12. What we covered — and where we are going next

## Part 1: What does purple look like in RGB?

Every colour on a screen is described by three numbers: how much red, how much green, and how much blue, each running from 0 (none) to 255 (full). Purple sits where red and blue are both elevated and green is low. Orange has high red, moderate green, and very little blue.

Before running the cell below, take a moment to predict: what RGB values would you expect for a deep purple? What about orange? There are no wrong answers here — we are building intuition that will matter when we design our training data later.

```python exec
id: 01-forward-pass-colour-classifier-page-1-1
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
```

Look at the purple colours: red and blue are both elevated, green is suppressed. This is the pattern we want a network to detect — and the question this tutorial answers is: what exactly happens inside the network when it processes a colour?

## Part 2: The network we are building

Our network has three layers:

- an **input layer** of three values — R, G, B
- a **hidden layer** of two nodes, each receiving all three inputs
- an **output layer** of one node, receiving the outputs of both hidden nodes

Each arrow in the diagram below represents a **weight**: a number that scales the signal as it travels along that connection. Each non-input node also has a **bias**: a private offset that lets the node shift its sensitivity independently of the inputs.

The job of the complete network is to take three numbers (R, G, B) and return one number — a **confidence score** between 0 and 1. Values above 0.5 mean the network thinks the colour is purple; values below mean it does not.

```python exec
id: 01-forward-pass-colour-classifier-page-1-2
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

### The parameters of this network

Every arrow in the diagram is a weight. Every `+b` label on a node is a bias. Weights and biases together are called the **parameters** of the network — they are the numbers that training will adjust. Right now they are set by hand; in Tutorial B they will be learned from data.

The table below names every parameter and gives the values we will use for the worked example in Part 3.

| Input → Hidden layer | | | Hidden → Output layer | | |
|---|---|---|---|---|---|
| **Edge** | **Name** | **Value** | **Edge** | **Name** | **Value** |
| R → H1 | w_R_H1 | 0.4 | H1 → out | w_H1_out | 0.9 |
| G → H1 | w_G_H1 | −0.1 | H2 → out | w_H2_out | 0.6 |
| B → H1 | w_B_H1 | 0.7 | bias of out | b_out | −0.3 |
| bias of H1 | b_H1 | 0.1 | | | |
| R → H2 | w_R_H2 | −0.2 | | | |
| G → H2 | w_G_H2 | 0.3 | | | |
| B → H2 | w_B_H2 | 0.5 | | | |
| bias of H2 | b_H2 | −0.05 | | | |
| **8 parameters** | | | **3 parameters** | | |

This network has **11 parameters** in total. Something worth sitting with before we move on: if we added a second hidden layer with 3 nodes, how many parameters would the network have? What if the hidden layer grew from 2 nodes to 4? We will return to this question in the exercises.

```python exec
id: 01-forward-pass-colour-classifier-page-1-3
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
# Your code here
```

## Looking back

Before leaving this page, a sentence on each. What you write stays on this device.

```reflect
- Something you expected before running a cell that turned out differently
- The one idea from this page you could explain to someone else now
- Something you would change or try next, if there were time
- A question this page raised for you that it did not answer. Bring it to the next session; these questions are where the next session starts.
```
