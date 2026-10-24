---
title: "Tutorial 3: The Polynomial Class - General Representation (1 of 2)"
slug: polynomials-3-basic-polynomial-class-page-1
course: programming-and-design-principles
series: oop-polynomials
series_title: "Object-Oriented Programming: A Worked Project"
version: 2026.09.07.1
---

*Page 1 of 2.*

# Tutorial 3: The Polynomial Class - General Representation

## Introduction

In Tutorials 1 and 2, we built three classes: `Constant`, `Linear`, and `Quadratic`. We discovered some serious problems:

**What worked:**
- Beautiful derivative chain: `Quadratic → Linear → Constant → Constant(0)`
- Each class has clear, specific methods
- Mathematical relationships are explicit

**What's broken:**
- Massive code duplication (especially `plot()`)
- Integration only works going from `Constant → Linear`
- We'd need infinite classes (Cubic, Quartic, Quintic, ...)
- Can only work with polynomials of degree 0, 1, or 2

Today, we'll solve these problems by creating **one class** that can represent **any** polynomial.

**The key insight:** Instead of storing separate coefficients (`a`, `b`, `c`), we'll store them in a **list**.

Let's see how this works!

```python exec
id: polynomials-3-basic-polynomial-class-page-1-1
import numpy as np
import matplotlib.pyplot as plt
```

## Part A: The Coefficient List Representation

### The Big Idea

Instead of different classes for each degree:

```python
Constant(c) # f(x) = c
Linear(m, b) # f(x) = mx + b 
Quadratic(a, b, c) # f(x) = ax² + bx + c
Cubic(a, b, c, d) # f(x) = ax³ + bx² + cx + d
```

We'll use **one representation**:

```python
Polynomial([c]) # f(x) = c
Polynomial([b, m]) # f(x) = b + mx
Polynomial([c, b, a]) # f(x) = c + bx + ax²
Polynomial([d, c, b, a]) # f(x) = d + cx + bx² + ax³
```

**Pattern:** `coeffs[i]` is the coefficient of `x^i`

So `[2, -3, 1]` represents: `2 + (-3)x + 1x²` which is `2 - 3x + x²`

### Examples

```python exec
id: polynomials-3-basic-polynomial-class-page-1-2
# Let's think about how we'd represent some polynomials:

print("f(x) = 5")
print("Coefficients: [5]")
print("Because: 5 is the coefficient of x^0")
print()

print("f(x) = 2x + 3")
print("Coefficients: [3, 2]")
print("Because: 3 is coeff of x^0, 2 is coeff of x^1")
print()

print("f(x) = x² - 4x + 3")
print("Coefficients: [3, -4, 1]")
print("Because: 3 is coeff of x^0, -4 is coeff of x^1, 1 is coeff of x^2")
print()

print("f(x) = 2x³ - x + 5")
print("Coefficients: [5, -1, 0, 2]")
print("Because: 5 (x^0), -1 (x^1), 0 (x^2), 2 (x^3)")
print("Note the 0 for the missing x² term!")
```

## Part B: Building the Polynomial Class - Basic Structure

Let's start with initialization and a basic method:

```python exec
id: polynomials-3-basic-polynomial-class-page-1-3
class Polynomial:
    """
    A class representing a polynomial of any degree.
    
    Attributes:
    -----------
    coeffs : list of float
        Coefficients where coeffs[i] is the coefficient of x^i
    """
    
    def __init__(self, coefficients: list):
        """
        Create a polynomial from a list of coefficients.
        
        Parameters:
        -----------
        coefficients : list of float
            coefficients[i] is the coefficient of x^i
            
        Example:
        --------
        Polynomial([2, -3, 1]) represents 2 - 3x + x²
        """
        self.coeffs = coefficients
    
    def degree(self) -> int:
        """
        Return the degree of the polynomial.
        
        The degree is the highest power with a non-zero coefficient.
        
        Returns:
        --------
        int
            The degree of the polynomial
        """
        # Start from the end and work backward to find first non-zero
        for i in range(len(self.coeffs) - 1, -1, -1):
            if self.coeffs[i] != 0:
                return i
        return 0  # All coefficients are zero
```

```python exec
id: polynomials-3-basic-polynomial-class-page-1-4
# Test basic creation and degree
p1 = Polynomial([5])              # Constant
p2 = Polynomial([3, 2])           # Linear
p3 = Polynomial([3, -4, 1])       # Quadratic
p4 = Polynomial([1, 0, -1, 0, 1]) # Quartic

print(f"p1 coeffs: {p1.coeffs}, degree: {p1.degree()}")
print(f"p2 coeffs: {p2.coeffs}, degree: {p2.degree()}")
print(f"p3 coeffs: {p3.coeffs}, degree: {p3.degree()}")
print(f"p4 coeffs: {p4.coeffs}, degree: {p4.degree()}")
```

## YOUR TURN: Implement evaluate()

For a polynomial with coefficients `[c₀, c₁, c₂, c₃, ...]`, we need to compute:

```
f(x) = c₀ + c₁x + c₂x² + c₃x³ + ...
```

**Hint:** Use `enumerate()` to loop through the coefficients with their indices.

```python exec
id: polynomials-3-basic-polynomial-class-page-1-5
class Polynomial:
    def __init__(self, coefficients: list):
        self.coeffs = coefficients
    
    def degree(self) -> int:
        for i in range(len(self.coeffs) - 1, -1, -1):
            if self.coeffs[i] != 0:
                return i
        return 0
    
    def evaluate(self, x: float) -> float:
        """
        Evaluate the polynomial at x.
        
        Parameters:
        -----------
        x : float
            The input value
            
        Returns:
        --------
        float
            The value of c₀ + c₁x + c₂x² + ...
        """
        # YOUR CODE HERE
        pass
```

```python exec
id: polynomials-3-basic-polynomial-class-page-1-6
# Test your implementation
p = Polynomial([3, -4, 1])  # 3 - 4x + x²

print(f"f(0) = {p.evaluate(0)}")  # Should be 3
print(f"f(1) = {p.evaluate(1)}")  # Should be 0 (3 - 4 + 1 = 0)
print(f"f(2) = {p.evaluate(2)}")  # Should be -1 (3 - 8 + 4 = -1)
print(f"f(3) = {p.evaluate(3)}")  # Should be 0 (3 - 12 + 9 = 0)
```

**Solution:**

```python exec
id: polynomials-3-basic-polynomial-class-page-1-7
class Polynomial:
    def __init__(self, coefficients: list):
        self.coeffs = coefficients
    
    def degree(self) -> int:
        for i in range(len(self.coeffs) - 1, -1, -1):
            if self.coeffs[i] != 0:
                return i
        return 0
    
    def evaluate(self, x: float) -> float:
        """Evaluate the polynomial at x."""
        result = 0
        for i, coeff in enumerate(self.coeffs):
            result += coeff * (x ** i)
        return result
```

## YOUR TURN: Implement __str__()

Create a readable string representation. For example:
- `[2, -3, 1]` should display as `"2 - 3x + x²"` or `"2 + -3x + 1x²"`

A simple version is fine - we'll keep it straightforward.

```python exec
id: polynomials-3-basic-polynomial-class-page-1-8
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
        """
        Return a readable string representation.
        
        Returns:
        --------
        str
            String like "2 - 3x + x²"
        """
        # YOUR CODE HERE
        pass
```

```python exec
id: polynomials-3-basic-polynomial-class-page-1-9
# Test your implementation
p1 = Polynomial([5])
p2 = Polynomial([3, 2])
p3 = Polynomial([3, -4, 1])
p4 = Polynomial([1, 0, -1, 0, 1])

print(f"p1: {p1}")
print(f"p2: {p2}")
print(f"p3: {p3}")
print(f"p4: {p4}")
```

**Solution:**

```python exec
id: polynomials-3-basic-polynomial-class-page-1-10
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
        """Return a readable string representation."""
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
```

## YOUR TURN: Implement plot()

Following the **same pattern** as before, implement `plot()`. 

**Notice:** The code should be nearly identical to what we wrote for `Constant`, `Linear`, and `Quadratic`!

```python exec
id: polynomials-3-basic-polynomial-class-page-1-11
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
        """
        Plot the polynomial.
        
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
id: polynomials-3-basic-polynomial-class-page-1-12
# Test your implementation
p = Polynomial([3, -4, 1])  # x² - 4x + 3
p.plot(x_min=-1, x_max=5)
```

**Solution:**

```python exec
id: polynomials-3-basic-polynomial-class-page-1-13
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
        """Plot the polynomial."""
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

## Exploring Different Polynomials

Now we can create polynomials of ANY degree!

```python exec
id: polynomials-3-basic-polynomial-class-page-1-14
# A constant
p_const = Polynomial([3])
print(f"Constant: {p_const}")
p_const.plot(x_min=-5, x_max=5)
```

```python exec
id: polynomials-3-basic-polynomial-class-page-1-15
# A linear function
p_linear = Polynomial([3, 2])
print(f"Linear: {p_linear}")
p_linear.plot(x_min=-5, x_max=5)
```

```python exec
id: polynomials-3-basic-polynomial-class-page-1-16
# A quadratic
p_quad = Polynomial([3, -4, 1])
print(f"Quadratic: {p_quad}")
p_quad.plot(x_min=-1, x_max=5)
```

```python exec
id: polynomials-3-basic-polynomial-class-page-1-17
# A cubic! (We couldn't do this before!)
p_cubic = Polynomial([-6, 11, -6, 1])  # x³ - 6x² + 11x - 6
print(f"Cubic: {p_cubic}")
print(f"Degree: {p_cubic.degree()}")
p_cubic.plot(x_min=-1, x_max=4)
```

```python exec
id: polynomials-3-basic-polynomial-class-page-1-18
# A quartic!
p_quartic = Polynomial([1, 0, -1, 0, 1])  # 1 - x² + x⁴
print(f"Quartic: {p_quartic}")
print(f"Degree: {p_quartic.degree()}")
p_quartic.plot(x_min=-2, x_max=2)
```

## Part C: The Power Rule - Derivatives for Everything

The **power rule** for derivatives says:

```
d/dx(cx^n) = n·c·x^(n-1)
```

So for a polynomial with coefficients `[c₀, c₁, c₂, c₃, ...]`:

```
f(x) = c₀ + c₁x + c₂x² + c₃x³ + ...
f'(x) = c₁ + 2c₂x + 3c₃x² + ...
```

In terms of coefficients:
- The constant term `c₀` disappears
- Each `cᵢ` becomes `i·cᵢ` and moves down one position

**Pattern:** `new_coeffs[i] = (i+1) * old_coeffs[i+1]`

### YOUR TURN: Implement derivative()

```python exec
id: polynomials-3-basic-polynomial-class-page-1-19
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
        """
        Return the derivative using the power rule.
        
        For coefficients [c₀, c₁, c₂, c₃, ...] representing c₀ + c₁x + c₂x² + c₃x³...
        The derivative is [c₁, 2c₂, 3c₃, ...] representing c₁ + 2c₂x + 3c₃x²...
        
        Returns:
        --------
        Polynomial
            A new Polynomial representing the derivative
        """
        # YOUR CODE HERE
        pass
```

```python exec
id: polynomials-3-basic-polynomial-class-page-1-20
# Test your implementation
p = Polynomial([3, -4, 1])  # 3 - 4x + x²
print(f"Function: {p}")

p_prime = p.derivative()
print(f"Derivative: {p_prime}")  # Should be -4 + 2x
```

**Solution:**

```python exec
id: polynomials-3-basic-polynomial-class-page-1-21
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
        """Return the derivative using the power rule."""
        if self.degree() == 0:
            return Polynomial([0])
        
        new_coeffs = []
        for i in range(1, len(self.coeffs)):
            new_coeffs.append(i * self.coeffs[i])
        
        return Polynomial(new_coeffs)
```

## Victory Moment: Derivatives Work for Everything!

Let's test derivatives on polynomials we couldn't handle before:

```python exec
id: polynomials-3-basic-polynomial-class-page-1-22
# Cubic derivative
cubic = Polynomial([-6, 11, -6, 1])  # -6 + 11x - 6x² + x³
print(f"Cubic: {cubic}")
print(f"Derivative: {cubic.derivative()}")  # Should be 11 - 12x + 3x²
print()

# Quartic derivative
quartic = Polynomial([1, 0, -1, 0, 1])  # 1 - x² + x⁴
print(f"Quartic: {quartic}")
print(f"Derivative: {quartic.derivative()}")  # Should be -2x + 4x³
```

### Testing the Derivative Chain

We can take derivatives repeatedly, for ANY degree:

```python exec
id: polynomials-3-basic-polynomial-class-page-1-23
# Start with a quartic
p = Polynomial([1, 0, -1, 0, 1])  # 1 - x² + x⁴

print(f"Original (degree {p.degree()}): {p}")

p1 = p.derivative()
print(f"1st derivative (degree {p1.degree()}): {p1}")

p2 = p1.derivative()
print(f"2nd derivative (degree {p2.degree()}): {p2}")

p3 = p2.derivative()
print(f"3rd derivative (degree {p3.degree()}): {p3}")

p4 = p3.derivative()
print(f"4th derivative (degree {p4.degree()}): {p4}")

p5 = p4.derivative()
print(f"5th derivative (degree {p5.degree()}): {p5}")
```

## Looking back

Before leaving this page, a sentence on each. What you write stays on this device.

```reflect
- Something you expected before running a cell that turned out differently
- The one idea from this page you could explain to someone else now
- A question this page raised that it did not answer
```
