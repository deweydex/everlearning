---
title: "02-backpropagation-through-data-page-4 (4 of 4)"
slug: 02-backpropagation-through-data-page-4
course: ai-and-ml-foundations
course_title: "AI and ML Foundations"
series: 4-learning-a-line
series_title: "Learning a Line"
version: 2026.09.06.1
---

Before starting this page, run the cell below. It repeats the imports and definitions from the earlier pages that this page uses.

```python exec
id: 02-backpropagation-through-data-page-4-setup
import random
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np  # For mesh grids in 3D plots
import numpy as np
```

## Part 4: Scaling to MNIST Digit Recognition

Everything we've done with 2D clusters scales directly to higher dimensions. An MNIST digit is a 28×28 image, which we can flatten into a 784-dimensional vector. Each pixel is just another input feature, like x and y were in our 2D case.

The network architecture becomes 784→32→10:
- 784 input neurons (one per pixel)
- 32 hidden neurons (smaller than before to keep computation manageable)
- 10 output neurons (one per digit 0-9)

The code is nearly identical — only the dimensions change. The forward pass, backpropagation, and training loop all work the same way.

```python exec
id: 02-backpropagation-through-data-page-4-1
# Load a small subset of MNIST digits
# (In practice, you'd load this from a file or library)
def load_mnist_sample():
    """
    Load a small sample of MNIST digits for demonstration.
    In a real implementation, this would load from keras.datasets or similar.

    Returns:
        tuple: (images, labels) where images are 784-dimensional vectors
    """
    # This is placeholder code - in practice you would load real MNIST data
    print("Note: This is a placeholder. In the actual notebook, we would load real MNIST data.")
    print("The architecture and training code would be identical to the 2D case,")
    print("just with different input dimensions.")
    return [], []

mnist_images, mnist_labels = load_mnist_sample()
```

### Visualizing MNIST Digits

Let's look at a few example digits to understand what our network will be learning to classify.

```python exec
id: 02-backpropagation-through-data-page-4-2
# Visualization code for MNIST digits
# Would show a grid of 28x28 grayscale images
```

### From Clusters to Digits: What Changed?

Compare what we've built:

| Aspect | 2D Clusters | MNIST Digits |
|--------|-------------|---------------|
| Input dimensions | 2 | 784 |
| Hidden neurons | 4 | 32 |
| Output classes | 3 | 10 |
| Total parameters | ~30 | ~25,000 |
| Forward pass | Same algorithm | Same algorithm |
| Backpropagation | Same algorithm | Same algorithm |
| Training loop | Same algorithm | Same algorithm |

The only difference is scale. The fundamental principles — minimizing loss through gradient descent, using the chain rule to compute gradients, updating parameters iteratively — remain identical.

This is the power of neural networks: the same simple building blocks (dot products, activation functions, gradients) scale from toy problems to real-world applications.

## Summary and Further Exploration

### What You've Learned

1. **Loss functions** quantify how wrong our predictions are. Mean squared error for regression, cross-entropy for classification.

2. **Gradient descent** finds the parameters that minimize loss by taking small steps in the direction of steepest descent.

3. **The chain rule** lets us compute how loss changes with respect to any parameter by multiplying derivatives backwards through the network.

4. **Backpropagation** is just the chain rule applied systematically to compute all gradients in one efficient backwards pass.

5. **Visualization** helps us understand what the network learns, especially in 2D where we can see decision boundaries form.

6. **Scaling** from 2D clusters to 784D digits changes the dimensions but not the fundamental algorithm.

### Connections to Skills Demo 2

In the upcoming skills demo, you'll implement a neural network class that builds on everything you've practiced here. The main difference is that you'll structure your code using object-oriented principles — creating a class that encapsulates the network's parameters and methods.

The mathematics and algorithms are exactly what you've worked through in this tutorial. The challenge will be organizing that code cleanly and testing each component independently.

### Resources for Further Study

If you want to deepen your understanding, these resources provide excellent explanations of the concepts we've covered:

- **3Blue1Brown**, "But what is a neural network?" and "Gradient descent, how neural networks learn" and "What is backpropagation really doing?" (YouTube, three videos ~15-20 minutes each) — Outstanding visual explanations of neural networks and backpropagation

- **Michael Nielsen**, *Neural Networks and Deep Learning*, Chapters 1-2 (neuralnetworksanddeeplearning.com) — Free online book with interactive visualizations

- **StatQuest with Josh Starmer**, "Neural Networks" playlist (YouTube) — Clear explanations from a statistical perspective

- **The MNIST Database** (yann.lecun.com/exdb/mnist/) — Original MNIST dataset documentation and background

## Looking back

Before leaving this page, a sentence on each. What you write stays on this device.

```reflect
- Something you expected before running a cell that turned out differently
- The one idea from this page you could explain to someone else now
- Something you would change or try next, if there were time
- A question this page raised for you that it did not answer. Bring it to the next session; these questions are where the next session starts.
```
