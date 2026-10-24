---
title: "Series and the Shape of a Curve"
slug: series-and-the-shape-of-a-curve
course: ai-and-ml-foundations
series: 2-calculus
series_title: "Calculus"
version: 2026.09.07.1
---

# Series and the Shape of a Curve

The sigmoid function, $\dfrac{1}{1 + e^{-x}}$, has no simpler form than the one it is already written in. And yet $e^x$ itself, the piece inside it, can be built entirely out of the one operation this course has used since Part 1: multiplying and adding. This page is about that fact, and about a shortcut it buys.

## Building $e^x$ Out of Powers

$$e^x = 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \frac{x^4}{4!} + \cdots$$

Every term is a power of $x$ divided by a factorial. Adding more terms gets closer to the true value of $e^x$; this is called a **series**, and stopping after a finite number of terms gives a polynomial that *approximates* the function. Let's build one and watch it close in.

```python exec
id: series-and-the-shape-of-a-curve-1
import math

def exp_series(x, n_terms):
    """The first n_terms of the series for e^x."""
    total = 0
    for k in range(n_terms):
        total += x**k / math.factorial(k)
    return total

x_value = 1.0
for n in (1, 2, 3, 5, 8, 15):
    print(f"{n:2d} terms: {exp_series(x_value, n):.8f}   (true value: {math.exp(x_value):.8f})")
```

By fifteen terms the approximation and the true value agree to as many digits as the print statement shows. Nothing here used a special "exponential" operation; every term is a power and a division, both of which Part 1 built from scratch.

### Your turn

Try `x_value = 5.0` instead of `1.0`. How many terms does it take before the approximation is close? Then try `x_value = -3.0`. Does the series still work for a negative input?

```python exec
id: series-and-the-shape-of-a-curve-2
hint: A larger |x| makes each term x**k/k! larger before the factorial catches up, so more terms are needed before the sum settles down. Negative x alternates the sign of each term, which is still a valid series — try it and compare against math.exp(-3.0).

```

## Differentiating and Integrating a Series Term by Term

Once a function is written as a sum of powers, the power rule from *Derivatives at Sea* can differentiate every term separately, and the two rules from the last page — the ones for products and chains — are not even needed.

```python exec
id: series-and-the-shape-of-a-curve-3
import sympy as sp

x = sp.symbols('x')
n_terms = 8
series = sum(x**k / sp.factorial(k) for k in range(n_terms))

print("the series itself:      ", series)
print("its derivative:         ", sp.diff(series, x))
print("the series one term shorter:", sum(x**k / sp.factorial(k) for k in range(n_terms - 1)))
```

Differentiating the eight-term series gives back the seven-term series, exactly. This is the fact underneath a famous property of $e^x$: it is its own derivative, because differentiating shifts every power down by one and the factorial in the denominator absorbs the change perfectly. The same term-by-term idea works in reverse for integration, and it is how a computer can integrate a function it has no closed formula for at all: build the series, integrate each power with the rule from *Integrals at Sea*, add the results.

## Building the Sigmoid From the Series

The sigmoid function is $1 / (1 + e^{-x})$, and now $e^{-x}$ is something we can build ourselves rather than call.

```python exec
id: series-and-the-shape-of-a-curve-4
def exp_series(x, n_terms=12):
    total = 0
    for k in range(n_terms):
        total += x**k / math.factorial(k)
    return total

def sigmoid_from_series(x, n_terms=12):
    return 1 / (1 + exp_series(-x, n_terms))

def sigmoid_exact(x):
    return 1 / (1 + math.exp(-x))

for z in (0.0, 0.5, 1.5, 3.0):
    approx = sigmoid_from_series(z)
    exact = sigmoid_exact(z)
    print(f"z={z}: exact={exact:.6f}, from series={approx:.6f}, difference={abs(exact - approx):.2e}")
```

### Your turn

The difference grows as $z$ grows, and at $z = 3.0$ with twelve terms it is no longer small. Increase `n_terms` in the call for $z = 3.0$ until the difference drops below `1e-6`. How many terms did it take, and does that match what you found for $e^5$ two cells ago?

```python exec
id: series-and-the-shape-of-a-curve-5
hint: Call sigmoid_from_series(3.0, n_terms) with a larger n_terms and compare to sigmoid_exact(3.0); increase it until the gap is small enough.
know: somewhere around 17 or 18 terms, which is a larger number than you might expect for such a small input — a series converges more slowly the further its input sits from zero, which is exactly what the last "your turn" on this page already showed you.

```

## Why This Matters Here, Not Just in Calculus

Nobody writing a neural network computes `math.exp` by hand from a series; the library does it, faster and more accurately, using tricks beyond this page. What the series buys is understanding rather than speed: it says that $e^x$, and therefore the sigmoid, and therefore every activation function built from it, is at heart nothing but the powers and additions this whole course has been built from since Part 1. There is no new kind of mathematics hiding inside a neural network. There is arithmetic, applied at a scale that makes it look like something else.

## Looking back

Before leaving this page, a sentence on each. What you write stays on this device.

```reflect
- What surprised you about how many terms a series needs for a larger input
- The one idea from this page you could explain to someone else now
- A question this page raised that it did not answer
```
