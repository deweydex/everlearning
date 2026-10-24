---
title: "Tutorial 1: Linear and Constant Functions - Our First Classes (1 of 3)"
slug: polynomials-1-constants-lines-page-1
course: programming-and-design-principles
series: oop-polynomials
series_title: "Object-Oriented Programming: A Worked Project"
version: 2026.09.07.1
---

*Page 1 of 3.*

# Tutorial 1: Linear and Constant Functions - Our First Classes

## Introduction

Welcome to our exploration of polynomials through programming! Over the next several tutorials, we'll build a mathematical toolkit for working with polynomial functions - from simple constants and lines all the way to polynomials of any degree.

**Our approach**: We'll start simple and let complexity emerge naturally. Each new concept will build on what we've already created, and we'll learn as much from what *doesn't* work as from what does.

**Why polynomials?** Polynomials are fundamental in mathematics and appear everywhere:
- Physics (trajectories, energy functions)
- Economics (cost and revenue models)
- Machine Learning (polynomial features, activation functions)
- Computer Graphics (curves and surfaces)

**What we'll build today**: Two simple classes representing constant and linear functions. These are the building blocks for everything that follows.

---

## Setup

First, let's import the libraries we'll need:

```python exec
id: polynomials-1-constants-lines-page-1-1
import numpy as np
import matplotlib.pyplot as plt
```

---

## Part A: The Constant Function

### What is a constant function?

A **constant function** always returns the same value, no matter what input you give it:

```
f(x) = c
```

For example:
- `f(x) = 5` is a constant function (always returns 5)
- `f(x) = -3` is a constant function (always returns -3)
- `f(x) = 0` is a constant function (always returns 0)

When we graph a constant function, we get a **horizontal line** at height `c`.

### Why make a class?

We *could* just use numbers:
```python
c = 5
result = c # Always 5, regardless of x
```

But a **class** lets us bundle together:
- The data (the value `c`)
- The operations we can do with it (evaluate, plot, take derivatives, etc.)
- A clear, organized structure

Let's build our `Constant` class step by step.

---

### Step 1: Basic Structure and Initialization

```python exec
id: polynomials-1-constants-lines-page-1-2
class Constant:
    def __init__(self, c: float):
        """
        Create a constant function f(x) = c
        
        Parameters:
        -----------
        c : float
            The constant value
        """
        self.c = c
```

**Let's test it:**

```python exec
id: polynomials-1-constants-lines-page-1-3
# Create some constant functions
f1 = Constant(5)
f2 = Constant(-3)
f3 = Constant(0)

print(f"f1 has value: {f1.c}")
print(f"f2 has value: {f2.c}")
print(f"f3 has value: {f3.c}")
```

### Step 2: Adding the evaluate() method

A function needs to be **evaluated** at different points. For a constant, this is simple - it always returns the same value!

```python exec
id: polynomials-1-constants-lines-page-1-4
class Constant:
    def __init__(self, c: float):
        """
        Create a constant function f(x) = c
        
        Parameters:
        -----------
        c : float
            The constant value
        """
        self.c = c
    
    def evaluate(self, x: float) -> float:
        """
        Evaluate the constant function at x.
        
        For a constant function, this always returns c,
        regardless of what x is!
        
        Parameters:
        -----------
        x : float
            The input value (not actually used for constants!)
            
        Returns:
        --------
        float
            The constant value c
        """
        return self.c
```

**Let's test it:**

```python exec
id: polynomials-1-constants-lines-page-1-5
f = Constant(7)

# Try different x values - should always get 7
print(f"f(0) = {f.evaluate(0)}")
print(f"f(5) = {f.evaluate(5)}")
print(f"f(100) = {f.evaluate(100)}")
print(f"f(-42) = {f.evaluate(-42)}")

# They're all the same!
```

### Step 3: Adding the __str__() method

It would be nice to print our function in a readable way:

```python exec
id: polynomials-1-constants-lines-page-1-6
class Constant:
    def __init__(self, c: float):
        self.c = c
    
    def evaluate(self, x: float) -> float:
        return self.c
    
    def __str__(self) -> str:
        """
        Return a readable string representation of the function.
        
        Returns:
        --------
        str
            String representation like "5" or "-3"
        """
        return f"{self.c}"
```

**Let's test it:**

```python exec
id: polynomials-1-constants-lines-page-1-7
f1 = Constant(5)
f2 = Constant(-3.5)
f3 = Constant(0)

print(f"f1: {f1}")
print(f"f2: {f2}")
print(f"f3: {f3}")
```

### Step 4: Adding the plot() method

Now for something visual! We'll plot our constant function by:
1. Creating many x values across a range
2. Evaluating the function at each x value
3. Plotting the results

**Notice**: We'll use `evaluate()` to build `plot()`. This is a key design principle - build complex methods from simpler ones!

```python exec
id: polynomials-1-constants-lines-page-1-8
class Constant:
    def __init__(self, c: float):
        self.c = c
    
    def evaluate(self, x: float) -> float:
        return self.c
    
    def __str__(self) -> str:
        return f"{self.c}"
    
    def plot(self, x_min: float = -10, x_max: float = 10, step: float = 0.1):
        """
        Plot the constant function.
        
        Parameters:
        -----------
        x_min : float
            Minimum x value to plot (default: -10)
        x_max : float
            Maximum x value to plot (default: 10)
        step : float
            Distance between x values (default: 0.1)
            Smaller step = smoother curve, but slower
        """
        # Create x values from x_min to x_max
        x_values = np.arange(x_min, x_max + step, step)
        
        # Evaluate the function at each x value
        # Notice: we use self.evaluate()!
        y_values = [self.evaluate(x) for x in x_values]
        
        # Create the plot
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

**Let's test it:**

```python exec
id: polynomials-1-constants-lines-page-1-9
f1 = Constant(5)
f1.plot()
```

```python exec
id: polynomials-1-constants-lines-page-1-10
f2 = Constant(-3)
f2.plot()
```

```python exec
id: polynomials-1-constants-lines-page-1-11
f3 = Constant(0)
f3.plot()
```

**What do you notice?** All constant functions are horizontal lines! The height of the line is determined by the value of `c`.

### Exploring the step parameter

The `step` parameter controls how many points we sample. Let's see what happens when we change it:

```python exec
id: polynomials-1-constants-lines-page-1-12
f = Constant(3)

print("With step = 2 (very coarse):")
f.plot(x_min=-5, x_max=5, step=2)
```

```python exec
id: polynomials-1-constants-lines-page-1-13
print("With step = 0.1 (default):")
f.plot(x_min=-5, x_max=5, step=0.1)
```

```python exec
id: polynomials-1-constants-lines-page-1-14
print("With step = 0.01 (very fine):")
f.plot(x_min=-5, x_max=5, step=0.01)
```

**Questions to think about:**
1. Why do they all look the same for a constant function?
2. What happens if `step` is larger than `(x_max - x_min)`?
3. For a constant function, do we actually need many points?

---

### Step 5: Adding the derivative() method

In calculus, the **derivative** measures how fast a function is changing.

For a constant function, the value **never changes** - it's always `c`. So the rate of change is **zero**!

```
If f(x) = c, then f'(x) = 0
```

Importantly, the derivative is **also a constant function** (the constant function `0`).

```python exec
id: polynomials-1-constants-lines-page-1-15
class Constant:
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
        """
        Return the derivative of this constant function.
        
        The derivative of a constant is always 0.
        
        Returns:
        --------
        Constant
            A new Constant object representing 0
        """
        return Constant(0)
```

**Let's test it:**

```python exec
id: polynomials-1-constants-lines-page-1-16
f = Constant(5)
print(f"Function: {f}")

f_prime = f.derivative()
print(f"Derivative: {f_prime}")

# We can take the derivative again!
f_double_prime = f_prime.derivative()
print(f"Second derivative: {f_double_prime}")

# And again...
print(f"Third derivative: {f_double_prime.derivative()}")
```

**What do you notice?** Once we hit zero, all further derivatives are also zero!

---

### Step 6: Adding the find_root() method

A **root** of a function is an x value where `f(x) = 0`.

For a constant function:
- If `c = 0`, then **every** x is a root (the function is always zero)
- If `c ≠ 0`, then there are **no** roots (the function never touches zero)

```python exec
id: polynomials-1-constants-lines-page-1-17
class Constant:
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
        """
        Find where the constant function equals zero.
        
        Returns:
        --------
        str
            Description of the roots
        """
        if self.c == 0:
            return "All x values are roots (function is always zero)"
        else:
            return "No roots (function never equals zero)"
```

**Let's test it:**

```python exec
id: polynomials-1-constants-lines-page-1-18
f1 = Constant(5)
print(f"{f1}: {f1.find_root()}")

f2 = Constant(0)
print(f"{f2}: {f2.find_root()}")

f3 = Constant(-3.7)
print(f"{f3}: {f3.find_root()}")
```

---

## Complete Constant Class

Here's our complete `Constant` class with all methods:

```python exec
id: polynomials-1-constants-lines-page-1-19
class Constant:
    """
    A class representing a constant function f(x) = c.
    
    Attributes:
    -----------
    c : float
        The constant value
    """
    
    def __init__(self, c: float):
        """Create a constant function f(x) = c"""
        self.c = c
    
    def evaluate(self, x: float) -> float:
        """Evaluate the constant function at x."""
        return self.c
    
    def __str__(self) -> str:
        """Return a readable string representation."""
        return f"{self.c}"
    
    def plot(self, x_min: float = -10, x_max: float = 10, step: float = 0.1):
        """Plot the constant function."""
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
        """Return the derivative (always 0)."""
        return Constant(0)
    
    def find_root(self) -> str:
        """Find where the function equals zero."""
        if self.c == 0:
            return "All x values are roots (function is always zero)"
        else:
            return "No roots (function never equals zero)"
```

## Looking back

Before leaving this page, a sentence on each. What you write stays on this device.

```reflect
- Something you expected before running a cell that turned out differently
- The one idea from this page you could explain to someone else now
- A question this page raised that it did not answer
```
