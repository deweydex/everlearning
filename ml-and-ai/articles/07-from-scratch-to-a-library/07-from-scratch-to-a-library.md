---
title: "From Scratch to a Library"
slug: 07-from-scratch-to-a-library
course: ai-and-ml-foundations
course_title: "AI and ML Foundations"
series: 5-neural-networks
series_title: "Neural Networks"
version: 2026.09.06.1
---

# From Scratch to a Library
## The Same Network in scikit-learn, and What PyTorch Calls Each Piece

### What this notebook is about

Over the last five notebooks we built a neural network out of nothing but NumPy: random weight matrices, a weighted sum, an activation, a loss, backpropagation, a training loop. Nobody does that at work. At work you call a library. This notebook is the handover: we build one more small network by hand, then build the same one with scikit-learn in four lines, and compare the two. Along the way every name the library uses is matched to the function we wrote for it, so that when you read library documentation you recognise old friends.

By the end you will know what the from-scratch work bought you, which is not the ability to avoid libraries, but the ability to read them.

### What you need

Parts 1, 4 and the first five notebooks of Part 5. NumPy and Matplotlib from Part 0. Nothing new to install: scikit-learn is included with Colab.

## Part 1: A Small Dataset We Can Hold in Our Heads

The MNIST digits we used before are 28 by 28 pixels. scikit-learn ships a smaller cousin, 8 by 8 pixels, 1797 images, which loads instantly and trains in seconds. Small is what we want here: the point is to compare two implementations, and a dataset that trains in a blink lets us run the comparison many times.

```python exec
id: 07-from-scratch-to-a-library-1
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split

digits = load_digits()
images, labels = digits.data, digits.target       # images: 1797 rows of 64 pixel values
print("shape of the data:", images.shape, "  labels from", labels.min(), "to", labels.max())

fig, axes = plt.subplots(1, 10, figsize=(12, 1.6))
for ax, index in zip(axes, range(10)):
    ax.imshow(images[index].reshape(8, 8), cmap="gray_r"); ax.set_title(labels[index]); ax.axis("off")
```

```python exec
id: 07-from-scratch-to-a-library-2
# Scale pixels to 0..1, as we did before, and hold back a test set the network never trains on
X = images / 16.0
X_train, X_test, y_train, y_test = train_test_split(X, labels, test_size=0.25, random_state=0)
print("training examples:", X_train.shape[0], "  test examples:", X_test.shape[0])
```

## Part 2: The Network by Hand, One Last Time

This is the network from *Building the Network Class*, condensed: 64 inputs, one hidden layer of 32 neurons with ReLU, 10 outputs turned into probabilities by *softmax* (the function that makes ten numbers non-negative and sum to one), and *cross-entropy* as the loss (how surprised the network is by the true label). If any line here is unfamiliar, the notebook it comes from is named in the comment.

```python exec
id: 07-from-scratch-to-a-library-3
rng = np.random.default_rng(0)

def one_hot(y, classes=10):
    '''Turn a label like 3 into [0,0,0,1,0,0,0,0,0,0].'''
    out = np.zeros((len(y), classes)); out[np.arange(len(y)), y] = 1; return out

def relu(z): return np.maximum(0, z)                                   # notebook 4, Part 5
def softmax(z):
    z = z - z.max(axis=1, keepdims=True)                                # for numerical safety
    e = np.exp(z); return e / e.sum(axis=1, keepdims=True)

hidden = 32
W1 = rng.normal(0, np.sqrt(2 / 64), (64, hidden)); b1 = np.zeros(hidden)     # notebook 4, Part 3
W2 = rng.normal(0, np.sqrt(2 / hidden), (hidden, 10)); b2 = np.zeros(10)

learning_rate = 0.5
epochs = 300
Y_train = one_hot(y_train)
losses = []

for epoch in range(epochs):
    # forward pass                                                       notebook 4, Parts 8-9
    z1 = X_train @ W1 + b1
    a1 = relu(z1)
    z2 = a1 @ W2 + b2
    probs = softmax(z2)
    loss = -np.mean(np.sum(Y_train * np.log(probs + 1e-12), axis=1))    # notebook 4, Part 11
    losses.append(loss)

    # backward pass                                                      notebook 4, Part 12
    n = len(X_train)
    d_z2 = (probs - Y_train) / n
    d_W2 = a1.T @ d_z2;            d_b2 = d_z2.sum(axis=0)
    d_a1 = d_z2 @ W2.T
    d_z1 = d_a1 * (z1 > 0)
    d_W1 = X_train.T @ d_z1;       d_b1 = d_z1.sum(axis=0)

    # the step downhill                                                  notebook 4, Part 13
    W1 -= learning_rate * d_W1;  b1 -= learning_rate * d_b1
    W2 -= learning_rate * d_W2;  b2 -= learning_rate * d_b2

def predict_scratch(X):
    return np.argmax(softmax(relu(X @ W1 + b1) @ W2 + b2), axis=1)

scratch_accuracy = np.mean(predict_scratch(X_test) == y_test)
print(f"from-scratch network: final loss {losses[-1]:.3f}, test accuracy {scratch_accuracy:.3f}")
```

Around 95 percent of unseen digits are read correctly, from about forty lines of NumPy. Keep the count of lines in mind.

### Your turn 2.1

Change `hidden` to 8 and run the cell again, then to 128. Note the accuracy and how long the cell takes each time. Which of the two changes cost more than it gained?

## Part 3: The Same Network in scikit-learn

scikit-learn's `MLPClassifier` is a *multi-layer perceptron*, which is the library's name for exactly the network we just wrote. Every argument below is a choice we made by hand in Part 2.

```python exec
id: 07-from-scratch-to-a-library-4
from sklearn.neural_network import MLPClassifier

mlp = MLPClassifier(hidden_layer_sizes=(32,),    # one hidden layer of 32 neurons: our W1 shape
                    activation="relu",           # our relu()
                    solver="sgd",                # plain gradient descent, like our update lines
                    learning_rate_init=0.5,      # our learning_rate
                    batch_size=len(X_train),     # the whole training set in each step, as we did
                    max_iter=300,                # our epochs
                    momentum=0,                  # off, so the comparison is fair
                    random_state=0)
mlp.fit(X_train, y_train)

library_accuracy = mlp.score(X_test, y_test)
print(f"scikit-learn network: final loss {mlp.loss_:.3f}, test accuracy {library_accuracy:.3f}")
print("shape of the library's first weight matrix:", mlp.coefs_[0].shape, "  ours:", W1.shape)
```

Four lines, the same accuracy, and the same shapes inside. `mlp.coefs_[0]` is our `W1`; `mlp.intercepts_[0]` is our `b1`. The library did not do anything we did not do. It did it with checks, with a better initialisation, with the option of many more settings, and without us being able to make an indexing mistake.

Let's put the two loss curves on one plot.

```python exec
id: 07-from-scratch-to-a-library-5
fig, ax = plt.subplots(figsize=(8, 4))
ax.plot(losses, label="from scratch")
ax.plot(mlp.loss_curve_, label="scikit-learn")
ax.set_xlabel("epoch"); ax.set_ylabel("cross-entropy loss"); ax.legend(); ax.grid(alpha=0.3)
ax.set_title("Two implementations of one idea")
```

The curves are not identical, because the two started from different random weights and the library's learning rate schedule and stopping rule differ a little from ours. They have the same shape, and that is the point: a loss curve is something you can now read, because you know what produced it.

### Your turn 3.1

Two settings we never wrote: `solver="adam"` (a smarter step that adapts its size per weight) and `alpha=0.01` (a penalty on large weights, called *regularisation*). Try each on its own and compare the loss curve and the test accuracy with the plain version. Which one changes the curve's shape, and which changes only where it ends?

## Part 4: A Dictionary Between the Two

Library documentation is written in the library's words. This table translates them into the functions you wrote.

| The library says | We wrote | Where |
|---|---|---|
| `hidden_layer_sizes=(32,)` | the shape of `W1` and `W2` | notebook 4, Part 3 |
| `activation="relu"` | `relu(z)` | notebook 4, Part 5 |
| parameters, `coefs_` and `intercepts_` | the weights and biases | notebook 1 |
| forward pass, `predict` | `X @ W1 + b1`, then `relu`, then `@ W2 + b2` | notebook 4, Parts 8 and 9 |
| `loss_`, cross-entropy | `-np.mean(np.sum(Y * np.log(probs)))` | notebook 4, Part 11 |
| backpropagation, `solver="sgd"` | the `d_` lines and the two `-=` updates | notebook 4, Part 12 and Part 13 |
| `learning_rate_init` | `learning_rate` | *Learning a Line* |
| `max_iter`, epochs | `for epoch in range(epochs)` | notebook 4, Part 13 |
| `batch_size` | how many rows of `X_train` go through one step | notebook 5 |
| `score` | `np.mean(predictions == y_test)` | notebook 4, Day 3 |
| `random_state` | the seed of `rng` | notebook 4, Part 3 |
| `alpha`, regularisation | nothing yet: a penalty added to the loss | new here |
| `momentum`, `solver="adam"` | nothing yet: smarter versions of the step | new here |

## Part 5: The Same Network in PyTorch, to Read

PyTorch is the library most research and much industry uses. It is not installed for this notebook and the cell below is for reading, not running, but every line has a match in Part 2. The one new idea is `loss.backward()`: PyTorch records every operation in the forward pass and works out the backward pass itself, which is the whole of our Part 12 done automatically. That facility is called *autograd*.

```python
import torch
from torch import nn

model = nn.Sequential(          # the forward pass, as a list of layers
    nn.Linear(64, 32),          # W1 and b1: 64 inputs, 32 neurons
    nn.ReLU(),                  # relu()
    nn.Linear(32, 10),          # W2 and b2
)                               # softmax is folded into the loss below
loss_function = nn.CrossEntropyLoss()
optimizer = torch.optim.SGD(model.parameters(), lr=0.5)

inputs = torch.tensor(X_train, dtype=torch.float32)
targets = torch.tensor(y_train)

for epoch in range(300):
    optimizer.zero_grad()                       # forget last step's gradients
    outputs = model(inputs)                     # forward pass
    loss = loss_function(outputs, targets)      # cross-entropy
    loss.backward()                             # backpropagation, done for us
    optimizer.step()                            # W -= learning_rate * gradient, for every W
```

Read the loop against the dictionary in Part 4 and it should feel familiar rather than magical. Everything in it, you have written.

## Part 6: What Building It Yourself Bought You

Three things, none of which the four-line version teaches.

You can read a shape error. When a library complains that it cannot multiply a `(64, 32)` by a `(64, 32)`, you know it means a transpose is missing, because you have made that mistake in your own code and fixed it.

You can read a loss curve. A curve that falls and then rises means the learning rate is too large; one that barely moves means it is too small or the network is too small; one that reaches zero on training data and stays high on test data means the network has memorised rather than learned. Each of those you have seen happen in a network whose every number you could print.

You can choose. `hidden_layer_sizes`, `activation`, `learning_rate_init` and `max_iter` are not incantations; they are the four decisions you made yourself in Part 2, and you know what each does to the curve.

From here, use the library. Reach for the from-scratch version when the library does something you do not understand, which is exactly when it will be worth having.

### Your turn 6.1

Find a digit the library network gets wrong (`mlp.predict(X_test) != y_test`), draw it, and print both the true label and the predicted one. Then look at `mlp.predict_proba` for that image: how confident was the network in its wrong answer? Was it a reasonable mistake?

```python exec
id: 07-from-scratch-to-a-library-6
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

## Where to Read More

Nielsen, M. (2015). *Neural Networks and Deep Learning*. <http://neuralnetworksanddeeplearning.com/>. Free online book; chapter 1 builds the same network we did and chapter 3 explains cross-entropy and regularisation.

scikit-learn developers. *Neural network models (supervised)*. <https://scikit-learn.org/stable/modules/neural_networks_supervised.html>. The documentation for `MLPClassifier`, readable now with the dictionary in Part 4.

PyTorch. *Learn the Basics*. <https://pytorch.org/tutorials/beginner/basics/intro.html>. The official first tutorial; its "Optimizing Model Parameters" page is Part 5 of this notebook at full length.

3Blue1Brown. *But what is a neural network?* <https://www.3blue1brown.com/topics/neural-networks>. The visual version of the whole of Part 5 of this course.
