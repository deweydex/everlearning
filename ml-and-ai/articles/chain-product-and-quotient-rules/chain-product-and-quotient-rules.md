---
title: "Chain, Product and Quotient Rules"
slug: chain-product-and-quotient-rules
course: ai-and-ml-foundations
series: 2-calculus
series_title: "Calculus"
version: 2026.09.07.1
---

# Chain, Product and Quotient Rules

*Derivatives at Sea* differentiated functions built from one moving part: a single power of $x$, a sine, an exponential. Most of the functions this course actually meets are built from several moving parts multiplied, divided or nested inside one another — a loss that is one function of a network's output, which is itself a function of the weights. This page is the three rules for taking those apart.

## When One Thing Sits Inside Another

$\sin(x^2)$ is not a sine of $x$; it is a sine of *whatever $x^2$ happens to be*. Differentiating it means asking two questions at once: how fast does the sine change as its input changes, and how fast does that input, $x^2$, change as $x$ changes. The **chain rule** multiplies the two answers together.

$$\frac{d}{dx}f(g(x)) = f'(g(x)) \cdot g'(x)$$

Let's check it against SymPy before trying it by hand.

```python exec
id: chain-product-and-quotient-rules-1
import sympy as sp

x = sp.symbols('x')
inner = x**2
outer_of_inner = sp.sin(inner)

derivative = sp.diff(outer_of_inner, x)
print(derivative)
```

The output is `2*x*cos(x**2)`: the derivative of the outer function, $\cos$, evaluated at the inner function, times the derivative of the inner function, $2x$. That is the chain rule read off directly: outer-derivative-at-inner, times inner-derivative.

### Your turn

Differentiate $(3x + 1)^4$ by hand first: the outer function is "something to the 4th power," so its derivative is 4 times that something cubed; the inner function is $3x+1$, whose derivative is 3. Write your answer, then check it.

```python exec
id: chain-product-and-quotient-rules-2
hint: The outer derivative, evaluated at the inner function, is 4*(3*x + 1)**3. Multiply by the inner derivative.
know: 12*(3*x + 1)**3
your_answer = None  # replace with your expression in x

sp.diff((3*x + 1)**4, x)
```

## When Two Things Are Multiplied

The derivative of a product is *not* the product of the derivatives — a mistake worth making once on paper so it is never made again.

```python exec
id: chain-product-and-quotient-rules-3
u = x**2
v = (x + 1)**3

wrong = sp.diff(u, x) * sp.diff(v, x)
right = sp.diff(u * v, x)
print("u' times v':", sp.expand(wrong))
print("derivative of u*v:", sp.expand(right))
```

They are different expressions. The correct rule, the **product rule**, keeps both terms: the first function times the derivative of the second, plus the derivative of the first times the second.

$$\frac{d}{dx}[u \cdot v] = u \cdot v' + u' \cdot v$$

Notice that $v = (x+1)^3$ itself needed the chain rule to differentiate — the two rules are used together constantly, not one after the other in separate problems.

### Your turn

$f(x) = x^2(x+1)^3$ is the product above. Write out $u$, $v$, $u'$ and $v'$ separately, then combine them with the product rule, then check the expanded result against `sp.expand(sp.diff(x**2 * (x+1)**3, x))`.

```python exec
id: chain-product-and-quotient-rules-4
hint: u = x**2 so u' = 2*x. v = (x+1)**3 so v' needs the chain rule: 3*(x+1)**2.
know: 5*x**4 + 12*x**3 + 9*x**2 + 2*x

```

## When One Thing Is Divided by Another

The **quotient rule** is the product rule's cousin, for $u / v$:

$$\frac{d}{dx}\left[\frac{u}{v}\right] = \frac{u' \cdot v - u \cdot v'}{v^2}$$

The order inside the top line matters, unlike in the product rule, because subtraction is not symmetric.

```python exec
id: chain-product-and-quotient-rules-5
u = x**2 + 1
v = x - 3

by_hand = (sp.diff(u, x) * v - u * sp.diff(v, x)) / v**2
by_sympy = sp.diff(u / v, x)
print("by hand:     ", sp.simplify(by_hand))
print("sympy:       ", sp.simplify(by_sympy))
print("same thing?  ", sp.simplify(by_hand - by_sympy) == 0)
```

### Your turn

A network's cross-entropy loss involves a ratio like $\dfrac{1}{1 + e^{-x}}$ — this is the sigmoid function itself, written as a quotient with $u = 1$ and $v = 1 + e^{-x}$. Use the quotient rule to differentiate it by hand, then check.

```python exec
id: chain-product-and-quotient-rules-6
hint: u = 1, so u' = 0 and the first term of the quotient rule vanishes entirely. v' needs the chain rule on e**(-x): its derivative is -e**(-x).
know: exp(-x)/(exp(-x) + 1)**2, which is the same value as sigmoid(x) * (1 - sigmoid(x)) once you simplify it — a fact you will meet again when you write backpropagation by hand.

sp.diff(1 / (1 + sp.exp(-x)), x)
```

## Where This Meets Backpropagation

A neural network's loss is a chain of functions: the loss depends on the output, the output depends on the last layer's weighted sum, that sum depends on the layer before it, and so on back to the input. Finding how the loss changes with respect to an early weight is one long application of the chain rule, multiplying a derivative at each link. That is the whole content of backpropagation, and the three rules on this page are the arithmetic underneath it. When you meet backpropagation in the Neural Networks part, the `d_` variables in the code are exactly the pieces this page has been computing by hand.

## Looking back

Before leaving this page, a sentence on each. What you write stays on this device.

```reflect
- The rule you would be most likely to forget under exam pressure, and a way to remember it
- Where you saw the chain rule and the product rule needed in the same problem
- A question this page raised that it did not answer
```
