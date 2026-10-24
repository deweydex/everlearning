---
title: "Tutorial 5 Part 2: Polymorphism and Design Principles (1 of 2)"
slug: polynomials-5-inheritance-polynomial-classes-part-2-page-1
course: programming-and-design-principles
series: oop-polynomials
series_title: "Object-Oriented Programming: A Worked Project"
version: 2026.09.07.1
---

*Page 1 of 2.*

# Tutorial 5 Part 2: Polymorphism and Design Principles

## Introduction

In Part 1, we discovered **inheritance** - how to create specialized classes that inherit functionality from a general parent class. We built `Linear` and `Quadratic` classes that:
- Have clear, intuitive interfaces (`Linear(m=2, b=3)`)
- Include specialized methods (`vertex()`, `discriminant()`, `find_roots()`)
- Inherit all the power of `Polynomial` (derivatives, integrals, arithmetic)

In Part 2, we'll explore the deeper principles and patterns that make this work, and understand **why** this is such a powerful design approach.

## What We'll Cover

1. **Polymorphism** - treating different types uniformly
2. **The Liskov Substitution Principle** - when inheritance is done right
3. **Design patterns** that emerge
4. **When to use inheritance** vs. other approaches
5. **Real-world applications** beyond polynomials

Let's dive in!

---

```python exec
id: polynomials-5-inheritance-polynomial-classes-part-2-page-1-1
import numpy as np
import matplotlib.pyplot as plt
```

## Part A: Polymorphism in Depth

### What is Polymorphism?

**Polymorphism** (from Greek: "many forms") means we can use different objects through the same interface. 

In Python, it's often called **duck typing**: "If it walks like a duck and quacks like a duck, it's a duck."

For us: "If it has `evaluate()` and `derivative()`, it's a polynomial."

### Bringing Back Our Classes

Let's load all our polynomial classes:

```python exec
id: polynomials-5-inheritance-polynomial-classes-part-2-page-1-2
# First, the parent Polynomial class
class Polynomial:
    def __init__(self, coefficients: list):
        self.coeffs = coefficients
    
    def degree(self) -> int:
        for i in range(len(self.coeffs) - 1, -1, -1):
            if self.coeffs[i] != 0:
                return i
        return 0
    
    def evaluate(self, x: float) -> float:
        result = 0
        for i, coeff in enumerate(self.coeffs):
            result += coeff * (x ** i)
        return result
    
    def __str__(self) -> str:
        terms = []
        for i, coeff in enumerate(self.coeffs):
            if coeff == 0:
                continue
            if i == 0:
                terms.append(f"{coeff}")
            elif i == 1:
                terms.append(f"{coeff}x")
            else:
                terms.append(f"{coeff}x^{i}")
        if not terms:
            return "0"
        return " + ".join(terms)
    
    def plot(self, x_min: float = -10, x_max: float = 10, step: float = 0.1):
        x_values = np.arange(x_min, x_max + step, step)
        y_values = [self.evaluate(x) for x in x_values]
        
        plt.plot(x_values, y_values, label=str(self), linewidth=2)
        plt.axhline(y=0, color='k', linestyle='-', linewidth=0.5)
        plt.axvline(x=0, color='k', linestyle='-', linewidth=0.5)
        plt.grid(True, alpha=0.3)
        plt.legend()
        plt.xlabel('x')
        plt.ylabel('f(x)')
        plt.title(f'Graph of f(x) = {self}')
        plt.show()
    
    def derivative(self):
        if self.degree() == 0:
            return Polynomial([0])
        new_coeffs = []
        for i in range(1, len(self.coeffs)):
            new_coeffs.append(i * self.coeffs[i])
        return Polynomial(new_coeffs)
    
    def integrate(self, C: float = 0):
        new_coeffs = [C]
        for i, coeff in enumerate(self.coeffs):
            new_coeffs.append(coeff / (i + 1))
        return Polynomial(new_coeffs)
    
    def __add__(self, other):
        len1 = len(self.coeffs)
        len2 = len(other.coeffs)
        max_len = max(len1, len2)
        new_coeffs = []
        for i in range(max_len):
            c1 = self.coeffs[i] if i < len1 else 0
            c2 = other.coeffs[i] if i < len2 else 0
            new_coeffs.append(c1 + c2)
        return Polynomial(new_coeffs)
    
    def __sub__(self, other):
        len1 = len(self.coeffs)
        len2 = len(other.coeffs)
        max_len = max(len1, len2)
        new_coeffs = []
        for i in range(max_len):
            c1 = self.coeffs[i] if i < len1 else 0
            c2 = other.coeffs[i] if i < len2 else 0
            new_coeffs.append(c1 - c2)
        return Polynomial(new_coeffs)
    
    def __mul__(self, other):
        result_degree = self.degree() + other.degree()
        new_coeffs = [0] * (result_degree + 1)
        for i, coeff_a in enumerate(self.coeffs):
            for j, coeff_b in enumerate(other.coeffs):
                power = i + j
                new_coeffs[power] += coeff_a * coeff_b
        return Polynomial(new_coeffs)

# Linear inherits from Polynomial
class Linear(Polynomial):
    def __init__(self, m: float, b: float):
        self.m = m
        self.b = b
        super().__init__([b, m])
    
    def __str__(self) -> str:
        return f"{self.m}x + {self.b}"
    
    def find_root(self):
        if self.m == 0:
            if self.b == 0:
                return "All x values are roots"
            else:
                return "No roots"
        else:
            return -self.b / self.m
    
    def slope(self) -> float:
        return self.m
    
    def y_intercept(self) -> float:
        return self.b

# Quadratic inherits from Polynomial
class Quadratic(Polynomial):
    def __init__(self, a: float, b: float, c: float):
        self.a = a
        self.b = b
        self.c = c
        super().__init__([c, b, a])
    
    def __str__(self) -> str:
        return f"{self.a}x² + {self.b}x + {self.c}"
    
    def discriminant(self) -> float:
        return self.b**2 - 4*self.a*self.c
    
    def find_roots(self):
        disc = self.discriminant()
        if disc < 0:
            return []
        elif disc == 0:
            root = -self.b / (2 * self.a)
            return [root]
        else:
            sqrt_disc = disc ** 0.5
            root1 = (-self.b + sqrt_disc) / (2 * self.a)
            root2 = (-self.b - sqrt_disc) / (2 * self.a)
            return [root1, root2]
    
    def vertex(self):
        x_vertex = -self.b / (2 * self.a)
        y_vertex = self.evaluate(x_vertex)
        return (x_vertex, y_vertex)
    
    def opens_upward(self) -> bool:
        return self.a > 0
```

### Example 1: Functions that Work with Any Polynomial

Because all our classes share the same interface, we can write functions that work with any of them:

```python exec
id: polynomials-5-inheritance-polynomial-classes-part-2-page-1-3
def analyze_function(f):
    """
    Analyze any polynomial function.
    
    Works with Polynomial, Linear, or Quadratic!
    """
    print(f"Function: {f}")
    print(f"Type: {type(f).__name__}")
    print(f"Degree: {f.degree()}")
    print(f"At x=0: {f.evaluate(0)}")
    print(f"At x=1: {f.evaluate(1)}")
    print(f"Derivative: {f.derivative()}")
    print(f"Integral: {f.integrate()}")
    print("-" * 50)
```

```python exec
id: polynomials-5-inheritance-polynomial-classes-part-2-page-1-4
# Works with all types!
analyze_function(Linear(m=2, b=3))
analyze_function(Quadratic(a=1, b=-4, c=3))
analyze_function(Polynomial([1, 0, -1, 0, 1]))
```

**This is polymorphism!** One function, many types.

### Example 2: Collections of Mixed Types

```python exec
id: polynomials-5-inheritance-polynomial-classes-part-2-page-1-5
def find_all_derivatives(functions):
    """
    Take derivatives of a list of functions.
    
    Doesn't care what type they are!
    """
    derivatives = []
    for f in functions:
        derivatives.append(f.derivative())
    return derivatives
```

```python exec
id: polynomials-5-inheritance-polynomial-classes-part-2-page-1-6
functions = [
    Linear(m=3, b=-2),
    Quadratic(a=1, b=0, c=-4),
    Polynomial([1, 2, 3, 4]),
    Linear(m=-1, b=7),
    Quadratic(a=2, b=-8, c=6)
]

derivs = find_all_derivatives(functions)

for original, deriv in zip(functions, derivs):
    print(f"f(x) = {original}")
    print(f"f'(x) = {deriv}")
    print()
```

### Example 3: Plotting Multiple Functions Together

```python exec
id: polynomials-5-inheritance-polynomial-classes-part-2-page-1-7
def plot_together(functions, x_min=-5, x_max=5):
    """
    Plot multiple functions on the same axes.
    
    Works with any polynomial type!
    """
    x_values = np.arange(x_min, x_max, 0.1)
    
    for f in functions:
        y_values = [f.evaluate(x) for x in x_values]
        plt.plot(x_values, y_values, label=str(f), linewidth=2)
    
    plt.axhline(y=0, color='k', linestyle='-', linewidth=0.5)
    plt.axvline(x=0, color='k', linestyle='-', linewidth=0.5)
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Multiple Functions')
    plt.show()
```

```python exec
id: polynomials-5-inheritance-polynomial-classes-part-2-page-1-8
functions = [
    Linear(m=1, b=0),           # y = x
    Quadratic(a=1, b=0, c=0),   # y = x²
    Polynomial([0, 0, 0, 1])    # y = x³
]

plot_together(functions, x_min=-2, x_max=2)
```

---

## Part B: The Liskov Substitution Principle

### What is it?

The **Liskov Substitution Principle** (LSP) says:

> If you have code that works with a parent class, it should also work with any child class, without knowing which specific child class it is.

In plain English:
> Anywhere you can use a `Polynomial`, you should be able to use a `Linear` or `Quadratic` instead.

### Testing the Principle

Let's write a function that expects a `Polynomial`:

```python exec
id: polynomials-5-inheritance-polynomial-classes-part-2-page-1-9
def compute_change(poly, x1, x2):
    """
    Compute how much the function changes from x1 to x2.
    
    Expects a Polynomial object.
    """
    y1 = poly.evaluate(x1)
    y2 = poly.evaluate(x2)
    change = y2 - y1
    
    print(f"Function: {poly}")
    print(f"From x={x1} to x={x2}:")
    print(f"  f({x1}) = {y1}")
    print(f"  f({x2}) = {y2}")
    print(f"  Change: {change}")
    return change
```

Now let's use it with different types:

```python exec
id: polynomials-5-inheritance-polynomial-classes-part-2-page-1-10
# With a Polynomial
compute_change(Polynomial([1, 2, 3]), 0, 2)
print()

# With a Linear (substituted for Polynomial!)
compute_change(Linear(m=2, b=1), 0, 2)
print()

# With a Quadratic (substituted for Polynomial!)
compute_change(Quadratic(a=1, b=0, c=-1), 0, 2)
```

## Looking back

Before leaving this page, a sentence on each. What you write stays on this device.

```reflect
- Something you expected before running a cell that turned out differently
- The one idea from this page you could explain to someone else now
- A question this page raised that it did not answer
```
