---
title: "Tutorial 2: Quadratic Functions - Patterns Strengthen (1 of 3)"
slug: polynomials-2-quadratics-page-1
course: programming-and-design-principles
series: oop-polynomials
series_title: "Object-Oriented Programming: A Worked Project"
version: 2026.09.07.1
---

*Page 1 of 3.*

# Tutorial 2: Quadratic Functions - Patterns Strengthen

## Introduction

In Tutorial 1, we built `Constant` and `Linear` classes. We noticed:
- They share similar structure (same method names)
- Derivatives connect them: `Linear → Constant → Constant(0)`
- We have code duplication (especially in `plot()`)
- We can't integrate because we'd need a `Quadratic` class

Today, we'll add the `Quadratic` class. As we build it, we'll see:
- The derivative chain becomes more interesting
- Code duplication gets worse
- Integration is *still* broken (now we'd need `Cubic`)
- The pattern is beautiful but unsustainable

Let's start by importing what we need and bringing in our previous classes.

```python exec
id: polynomials-2-quadratics-page-1-1
import numpy as np
import matplotlib.pyplot as plt
```

## Bringing Back Our Previous Classes

First, let's include our `Constant` and `Linear` classes from Tutorial 1:

```python exec
id: polynomials-2-quadratics-page-1-2
class Constant:
    """
    A class representing a constant function f(x) = c.
    
    Attributes:
    -----------
    c : float
        The constant value
    """
    
    def __init__(self, c: float):
        self.c = c
    
    def evaluate(self, x: float) -> float:
        return self.c
    
    def __str__(self) -> str:
        return f"{self.c}"
    
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
        return Constant(0)
    
    def find_root(self) -> str:
        if self.c == 0:
            return "All x values are roots (function is always zero)"
        else:
            return "No roots (function never equals zero)"
    
    def integrate(self, C: float = 0):
        """
        Return the integral of this constant function.
        ∫c dx = cx + C
        
        Parameters:
        -----------
        C : float
            The constant of integration (default: 0)
        
        Returns:
        --------
        Linear
            A new Linear object representing cx + C
        """
        return Linear(m=self.c, b=C)
```

```python exec
id: polynomials-2-quadratics-page-1-3
class Linear:
    """
    A class representing a linear function f(x) = mx + b.
    
    Attributes:
    -----------
    m : float
        The slope
    b : float
        The y-intercept
    """
    
    def __init__(self, m: float, b: float):
        self.m = m
        self.b = b
    
    def evaluate(self, x: float) -> float:
        return self.m * x + self.b
    
    def __str__(self) -> str:
        return f"{self.m}x + {self.b}"
    
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
        return Constant(self.m)
    
    def find_root(self):
        if self.m == 0:
            if self.b == 0:
                return "All x values are roots (function is always zero)"
            else:
                return "No roots (function never equals zero)"
        else:
            return -self.b / self.m
```

Let's quickly verify they still work:

```python exec
id: polynomials-2-quadratics-page-1-4
# Test Constant
c = Constant(3)
print(f"Constant: {c}")
print(f"Derivative: {c.derivative()}")

# Test Linear  
line = Linear(m=2, b=-4)
print(f"\nLinear: {line}")
print(f"Derivative: {line.derivative()}")
print(f"Root: {line.find_root()}")
```

## Part A: What is a Quadratic Function?

A **quadratic function** has the form:

```
f(x) = ax² + bx + c
```

Where:
- `a` is the coefficient of x² (determines if parabola opens up or down)
- `b` is the coefficient of x
- `c` is the constant term (y-intercept)

For example:
- `f(x) = x² - 4x + 3` has a=1, b=-4, c=3
- `f(x) = -2x² + 5` has a=-2, b=0, c=5
- `f(x) = x²` has a=1, b=0, c=0

When we graph a quadratic, we get a **parabola** - a U-shaped (or upside-down U) curve.

### Key Properties of Quadratics:

1. **Vertex**: The turning point (maximum or minimum)
2. **Roots**: Where the parabola crosses the x-axis (can be 0, 1, or 2 roots)
3. **Axis of symmetry**: Vertical line through the vertex
4. **Direction**: Opens up if a > 0, down if a < 0

## Part B: Building the Quadratic Class - Basic Structure

Following the pattern from `Constant` and `Linear`, let's start building our `Quadratic` class:

```python exec
id: polynomials-2-quadratics-page-1-5
class Quadratic:
    """
    A class representing a quadratic function f(x) = ax² + bx + c.
    
    Attributes:
    -----------
    a : float
        Coefficient of x²
    b : float
        Coefficient of x
    c : float
        Constant term
    """
    
    def __init__(self, a: float, b: float, c: float):
        """
        Create a quadratic function f(x) = ax² + bx + c
        
        Parameters:
        -----------
        a : float
            Coefficient of x²
        b : float
            Coefficient of x
        c : float
            Constant term
        """
        self.a = a
        self.b = b
        self.c = c
```

```python exec
id: polynomials-2-quadratics-page-1-6
# Test basic creation
q1 = Quadratic(a=1, b=-4, c=3)
q2 = Quadratic(a=-2, b=0, c=5)
q3 = Quadratic(a=1, b=0, c=0)

print(f"q1: a={q1.a}, b={q1.b}, c={q1.c}")
print(f"q2: a={q2.a}, b={q2.b}, c={q2.c}")
print(f"q3: a={q3.a}, b={q3.b}, c={q3.c}")
```

## YOUR TURN: Implement evaluate()

For a quadratic `f(x) = ax² + bx + c`, implement the `evaluate()` method.

**Hint:** Remember that `x**2` means x squared in Python.

```python exec
id: polynomials-2-quadratics-page-1-7
class Quadratic:
    def __init__(self, a: float, b: float, c: float):
        self.a = a
        self.b = b
        self.c = c
    
    def evaluate(self, x: float) -> float:
        """
        Evaluate the quadratic function at x.
        
        Parameters:
        -----------
        x : float
            The input value
            
        Returns:
        --------
        float
            The value ax² + bx + c
        """
        # YOUR CODE HERE
        pass
```

```python exec
id: polynomials-2-quadratics-page-1-8
# Test your implementation
quad = Quadratic(a=1, b=-4, c=3)
print(f"f(0) = {quad.evaluate(0)}")   # Should be 3
print(f"f(1) = {quad.evaluate(1)}")   # Should be 0  (1 - 4 + 3 = 0)
print(f"f(2) = {quad.evaluate(2)}")   # Should be -1 (4 - 8 + 3 = -1)
print(f"f(3) = {quad.evaluate(3)}")   # Should be 0  (9 - 12 + 3 = 0)
```

**Solution:**

```python exec
id: polynomials-2-quadratics-page-1-9
class Quadratic:
    def __init__(self, a: float, b: float, c: float):
        self.a = a
        self.b = b
        self.c = c
    
    def evaluate(self, x: float) -> float:
        """Evaluate the quadratic function at x."""
        return self.a * x**2 + self.b * x + self.c
```

## YOUR TURN: Implement __str__()

Implement the `__str__()` method to return a readable string like `"x² - 4x + 3"` or `"-2x² + 5"`.

You can use `x²` or `x^2` for the squared term.

```python exec
id: polynomials-2-quadratics-page-1-10
class Quadratic:
    def __init__(self, a: float, b: float, c: float):
        self.a = a
        self.b = b
        self.c = c
    
    def evaluate(self, x: float) -> float:
        return self.a * x**2 + self.b * x + self.c
    
    def __str__(self) -> str:
        """
        Return a readable string representation of the function.
        
        Returns:
        --------
        str
            String representation like "x² - 4x + 3"
        """
        # YOUR CODE HERE
        pass
```

```python exec
id: polynomials-2-quadratics-page-1-11
# Test your implementation
q1 = Quadratic(a=1, b=-4, c=3)
print(f"q1: {q1}")

q2 = Quadratic(a=-2, b=0, c=5)
print(f"q2: {q2}")

q3 = Quadratic(a=1, b=0, c=0)
print(f"q3: {q3}")
```

**Solution:**

```python exec
id: polynomials-2-quadratics-page-1-12
class Quadratic:
    def __init__(self, a: float, b: float, c: float):
        self.a = a
        self.b = b
        self.c = c
    
    def evaluate(self, x: float) -> float:
        return self.a * x**2 + self.b * x + self.c
    
    def __str__(self) -> str:
        """Return a readable string representation."""
        return f"{self.a}x² + {self.b}x + {self.c}"
```

## YOUR TURN: Implement plot()

Following the **exact same pattern** as `Constant.plot()` and `Linear.plot()`, implement the `plot()` method.

**Remember:** The structure is identical - we just call `self.evaluate()` which now does quadratic evaluation.

```python exec
id: polynomials-2-quadratics-page-1-13
class Quadratic:
    def __init__(self, a: float, b: float, c: float):
        self.a = a
        self.b = b
        self.c = c
    
    def evaluate(self, x: float) -> float:
        return self.a * x**2 + self.b * x + self.c
    
    def __str__(self) -> str:
        return f"{self.a}x² + {self.b}x + {self.c}"
    
    def plot(self, x_min: float = -10, x_max: float = 10, step: float = 0.1):
        """
        Plot the quadratic function.
        
        Parameters:
        -----------
        x_min : float
            Minimum x value to plot
        x_max : float
            Maximum x value to plot
        step : float
            Distance between x values
        """
        # YOUR CODE HERE
        pass
```

```python exec
id: polynomials-2-quadratics-page-1-14
# Test your implementation
quad = Quadratic(a=1, b=-4, c=3)
quad.plot()
```

**Solution:**

```python exec
id: polynomials-2-quadratics-page-1-15
class Quadratic:
    def __init__(self, a: float, b: float, c: float):
        self.a = a
        self.b = b
        self.c = c
    
    def evaluate(self, x: float) -> float:
        return self.a * x**2 + self.b * x + self.c
    
    def __str__(self) -> str:
        return f"{self.a}x² + {self.b}x + {self.c}"
    
    def plot(self, x_min: float = -10, x_max: float = 10, step: float = 0.1):
        """Plot the quadratic function."""
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
```

## Exploring Quadratic Graphs

Let's plot several quadratics to see their shapes:

```python exec
id: polynomials-2-quadratics-page-1-16
# Parabola opening upward (a > 0)
q1 = Quadratic(a=1, b=0, c=-4)
print(f"Opening upward: {q1}")
q1.plot(x_min=-5, x_max=5)
```

```python exec
id: polynomials-2-quadratics-page-1-17
# Parabola opening downward (a < 0)
q2 = Quadratic(a=-1, b=0, c=4)
print(f"Opening downward: {q2}")
q2.plot(x_min=-5, x_max=5)
```

```python exec
id: polynomials-2-quadratics-page-1-18
# Parabola shifted to the side
q3 = Quadratic(a=1, b=-4, c=3)
print(f"Shifted parabola: {q3}")
q3.plot(x_min=-1, x_max=5)
```

### Exploring step with Quadratics

For curves, the `step` parameter matters more than for straight lines:

```python exec
id: polynomials-2-quadratics-page-1-19
quad = Quadratic(a=1, b=0, c=-4)

print("With step = 2 (very coarse):")
quad.plot(x_min=-5, x_max=5, step=2)
```

```python exec
id: polynomials-2-quadratics-page-1-20
print("With step = 0.5:")
quad.plot(x_min=-5, x_max=5, step=0.5)
```

```python exec
id: polynomials-2-quadratics-page-1-21
print("With step = 0.1 (default):")
quad.plot(x_min=-5, x_max=5, step=0.1)
```

**Notice:** With large steps, we might miss the smooth curve! The parabola changes faster near the vertex.

## Looking back

Before leaving this page, a sentence on each. What you write stays on this device.

```reflect
- Something you expected before running a cell that turned out differently
- The one idea from this page you could explain to someone else now
- A question this page raised that it did not answer
```
