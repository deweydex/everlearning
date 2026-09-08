---
title: "Tutorial 4: Polynomial Arithmetic - Combining Polynomials (1 of 2)"
slug: polynomials-4-polynomial-methods-page-1
course: programming-and-design-principles
series: oop-polynomials
series_title: "Object-Oriented Programming: A Worked Project"
version: 2026.09.07.1
---

*Page 1 of 2.*

# Tutorial 4: Polynomial Arithmetic - Combining Polynomials

## Introduction

In Tutorial 3, we created a general `Polynomial` class that can represent any degree polynomial using coefficient lists. We discovered:

**What we gained:**
- Can represent ANY polynomial degree
- Derivatives and integrals work for everything
- Only ONE class instead of infinite
- No code duplication

**What we lost:**
- Easy exact root formulas (like the quadratic formula)
- Special methods (`vertex()`, `discriminant()`)
- Intuitive interface for common cases

Today, we'll explore what we can **DO** with polynomials:
- **Add** them together
- **Subtract** them
- **Multiply** them
- **Compose** them (substitute one into another)
- **Test equality**

This will show us the full power of our general representation, and set us up for Tutorial 5 where we'll use **inheritance** to get the best of both worlds.

Let's start!

```python exec
id: polynomials-4-polynomial-methods-page-1-1
import numpy as np
import matplotlib.pyplot as plt
```

## Part A: Starting with Our Complete Polynomial Class

Let's bring in the `Polynomial` class we built in Tutorial 3:

```python exec
id: polynomials-4-polynomial-methods-page-1-2
class Polynomial:
    """
    A class representing a polynomial of any degree.
    
    Attributes:
    -----------
    coeffs : list of float
        Coefficients where coeffs[i] is the coefficient of x^i
    """
    
    def __init__(self, coefficients: list):
        self.coeffs = coefficients
    
    def degree(self) -> int:
        """Return the degree of the polynomial."""
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
    
    def derivative(self):
        """Return the derivative using the power rule."""
        if self.degree() == 0:
            return Polynomial([0])
        
        new_coeffs = []
        for i in range(1, len(self.coeffs)):
            new_coeffs.append(i * self.coeffs[i])
        
        return Polynomial(new_coeffs)
    
    def integrate(self, C: float = 0):
        """Return the integral using the reverse power rule."""
        new_coeffs = [C]
        for i, coeff in enumerate(self.coeffs):
            new_coeffs.append(coeff / (i + 1))
        
        return Polynomial(new_coeffs)
```

```python exec
id: polynomials-4-polynomial-methods-page-1-3
# Quick test
p = Polynomial([3, -4, 1])  # 3 - 4x + x²
print(f"Polynomial: {p}")
print(f"Degree: {p.degree()}")
print(f"At x=2: {p.evaluate(2)}")
print(f"Derivative: {p.derivative()}")
```

## Part B: Addition - Combining Like Terms

### The Mathematical Idea

When we add polynomials, we combine **like terms** (terms with the same power):

```
(2 + 3x + x²) + (1 + x + 2x²) = (2+1) + (3+1)x + (1+2)x²
 = 3 + 4x + 3x²
```

In terms of coefficient lists:
```
[2, 3, 1] + [1, 1, 2] = [2+1, 3+1, 1+2] = [3, 4, 3]
```

**The challenge:** The lists might have different lengths!

```
(2 + 3x) + (1 + x²) = 2 + 3x + x²
[2, 3] + [1, 0, 1] = [2+1, 3+0, 0+1] = [3, 3, 1]
```

We need to handle the missing coefficients as zeros.

### YOUR TURN: Implement __add__()

The `__add__` method lets us use the `+` operator between polynomials.

**Hints:**
- Find the maximum length of the two coefficient lists
- Loop through indices up to that maximum
- For each index, get the coefficient from each polynomial (use 0 if index is out of bounds)
- Add the coefficients
- Return a new `Polynomial` with the sum coefficients

```python exec
id: polynomials-4-polynomial-methods-page-1-4
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
        """
        Add two polynomials by adding corresponding coefficients.
        
        Parameters:
        -----------
        other : Polynomial
            The polynomial to add
            
        Returns:
        --------
        Polynomial
            A new polynomial representing the sum
        """
        # YOUR CODE HERE
        pass
```

```python exec
id: polynomials-4-polynomial-methods-page-1-5
# Test your implementation
p1 = Polynomial([2, 3, 1])      # 2 + 3x + x²
p2 = Polynomial([1, 1, 0, 2])   # 1 + x + 2x³

p3 = p1 + p2
print(f"({p1}) + ({p2})")
print(f"= {p3}")

# Verify by evaluating
x = 5
print(f"\nAt x={x}:")
print(f"p1({x}) = {p1.evaluate(x)}")
print(f"p2({x}) = {p2.evaluate(x)}")
print(f"p1({x}) + p2({x}) = {p1.evaluate(x) + p2.evaluate(x)}")
print(f"p3({x}) = {p3.evaluate(x)}")
print(f"Match? {abs(p3.evaluate(x) - (p1.evaluate(x) + p2.evaluate(x))) < 1e-10}")
```

**Solution:**

```python exec
id: polynomials-4-polynomial-methods-page-1-6
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
        """Add two polynomials."""
        # Find the maximum length
        len1 = len(self.coeffs)
        len2 = len(other.coeffs)
        max_len = max(len1, len2)
        
        # Add corresponding coefficients
        new_coeffs = []
        for i in range(max_len):
            c1 = self.coeffs[i] if i < len1 else 0
            c2 = other.coeffs[i] if i < len2 else 0
            new_coeffs.append(c1 + c2)
        
        return Polynomial(new_coeffs)
```

## Exploring Addition

```python exec
id: polynomials-4-polynomial-methods-page-1-7
p1 = Polynomial([2, 3, 1])      # 2 + 3x + x²
p2 = Polynomial([1, 1, 0, 2])   # 1 + x + 2x³

p3 = p1 + p2
print(f"({p1}) + ({p2}) = {p3}")
```

```python exec
id: polynomials-4-polynomial-methods-page-1-8
# What if we add a polynomial to itself?
p = Polynomial([1, 2, 3])
print(f"p = {p}")

double = p + p
print(f"p + p = {double}")
# All coefficients should be doubled!
```

```python exec
id: polynomials-4-polynomial-methods-page-1-9
# What about adding opposites?
p1 = Polynomial([1, 2, 3])
p2 = Polynomial([-1, -2, -3])

zero = p1 + p2
print(f"({p1}) + ({p2}) = {zero}")
# Should be the zero polynomial!
```

## Part C: Subtraction - The Opposite Operation

Subtraction is very similar to addition - we just subtract corresponding coefficients instead of adding them.

### YOUR TURN: Implement __sub__()

```python exec
id: polynomials-4-polynomial-methods-page-1-10
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
        """
        Subtract two polynomials by subtracting corresponding coefficients.
        
        Parameters:
        -----------
        other : Polynomial
            The polynomial to subtract
            
        Returns:
        --------
        Polynomial
            A new polynomial representing the difference
        """
        # YOUR CODE HERE
        pass
```

```python exec
id: polynomials-4-polynomial-methods-page-1-11
# Test your implementation
p1 = Polynomial([5, 3, 1])
p2 = Polynomial([2, 1, 0, 2])

p3 = p1 - p2
print(f"({p1}) - ({p2}) = {p3}")

# Verify
x = 3
print(f"\nAt x={x}:")
print(f"p1({x}) - p2({x}) = {p1.evaluate(x) - p2.evaluate(x)}")
print(f"p3({x}) = {p3.evaluate(x)}")
```

**Solution:**

```python exec
id: polynomials-4-polynomial-methods-page-1-12
# Just change + to - in the __add__ method!
def __sub__(self, other):
    """Subtract two polynomials."""
    len1 = len(self.coeffs)
    len2 = len(other.coeffs)
    max_len = max(len1, len2)
    
    new_coeffs = []
    for i in range(max_len):
        c1 = self.coeffs[i] if i < len1 else 0
        c2 = other.coeffs[i] if i < len2 else 0
        new_coeffs.append(c1 - c2)  # Subtract instead of add!
    
    return Polynomial(new_coeffs)
```

Let's add this to our complete class:

```python exec
id: polynomials-4-polynomial-methods-page-1-13
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
```

```python exec
id: polynomials-4-polynomial-methods-page-1-14
# Test subtraction
p1 = Polynomial([5, 3, 1])
p2 = Polynomial([2, 1])

print(f"p1 = {p1}")
print(f"p2 = {p2}")
print(f"p1 - p2 = {p1 - p2}")
print(f"p2 - p1 = {p2 - p1}")
```

```python exec
id: polynomials-4-polynomial-methods-page-1-15
# Subtract from itself - should get zero
p = Polynomial([1, 2, 3, 4])
zero = p - p
print(f"({p}) - ({p}) = {zero}")
```

## Part D: Multiplication - A More Complex Operation

### The Mathematical Idea

When we multiply polynomials, **each term in the first** multiplies **each term in the second**:

```
(2 + x)(3 + x) = 2·3 + 2·x + x·3 + x·x
 = 6 + 2x + 3x + x²
 = 6 + 5x + x²
```

More systematically, using the distributive property:
```
(c₀ + c₁x)(d₀ + d₁x) = c₀d₀ + c₀d₁x + c₁d₀x + c₁d₁x²
 = c₀d₀ + (c₀d₁ + c₁d₀)x + c₁d₁x²
```

**Key insight:** When we multiply `cᵢxⁱ` by `dⱼxʲ`, we get `cᵢdⱼx^(i+j)`

**Pattern:** 
- The degree of the product is the sum of the degrees
- `result[i+j] += coeffs1[i] * coeffs2[j]`

### YOUR TURN: Implement __mul__()

**Hints:**
- Create a result list with length `degree(p1) + degree(p2) + 1`
- Initialize all coefficients to 0
- Use nested loops: for each i in first polynomial, for each j in second polynomial
- Add `coeffs1[i] * coeffs2[j]` to `result[i+j]`

```python exec
id: polynomials-4-polynomial-methods-page-1-16
class Polynomial:
    # ... (previous methods) ...
    
    def __mul__(self, other):
        """
        Multiply two polynomials.
        
        Each term in self multiplies each term in other:
        (Σ aᵢxⁱ) * (Σ bⱼxʲ) = Σᵢ Σⱼ aᵢbⱼx^(i+j)
        
        Parameters:
        -----------
        other : Polynomial
            The polynomial to multiply by
            
        Returns:
        --------
        Polynomial
            A new polynomial representing the product
        """
        # YOUR CODE HERE
        pass
```

**Think about it first:**

If we multiply:
- A polynomial of degree 1 (linear)
- By another polynomial of degree 1 (linear)
- What degree should the result be?

```python
# (1 + x)(1 + x) = 1 + x + x + x² = 1 + 2x + x²
# Degree 1 * degree 1 = degree 2
```

```python exec
id: polynomials-4-polynomial-methods-page-1-17
# Test once you've implemented it
p1 = Polynomial([1, 1])  # 1 + x
p2 = Polynomial([1, 1])  # 1 + x

product = p1 * p2
print(f"({p1}) * ({p2}) = {product}")
# Should be 1 + 2x + x²
```

**Solution:**

```python exec
id: polynomials-4-polynomial-methods-page-1-18
def __mul__(self, other):
    """Multiply two polynomials."""
    # Result has degree = degree(self) + degree(other)
    result_degree = self.degree() + other.degree()
    new_coeffs = [0] * (result_degree + 1)
    
    # Multiply each term in self by each term in other
    for i, coeff_a in enumerate(self.coeffs):
        for j, coeff_b in enumerate(other.coeffs):
            # Term aᵢxⁱ * bⱼxʲ = aᵢbⱼx^(i+j)
            power = i + j
            new_coeffs[power] += coeff_a * coeff_b
    
    return Polynomial(new_coeffs)
```

Let's add multiplication to our complete class and test it:

```python exec
id: polynomials-4-polynomial-methods-page-1-19
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
```

## Exploring Multiplication

```python exec
id: polynomials-4-polynomial-methods-page-1-20
# Simple case: (1 + x)(1 + x)
p = Polynomial([1, 1])
p_squared = p * p
print(f"({p})² = {p_squared}")
# Should be 1 + 2x + x²
```

```python exec
id: polynomials-4-polynomial-methods-page-1-21
# Verify a factorization: x² - 1 = (x + 1)(x - 1)
p1 = Polynomial([1, 1])    # 1 + x (which is x + 1)
p2 = Polynomial([-1, 1])   # -1 + x (which is x - 1)

product = p1 * p2
print(f"({p1}) * ({p2}) = {product}")

expected = Polynomial([-1, 0, 1])  # -1 + 0x + x²
print(f"Expected: {expected}")
```

```python exec
id: polynomials-4-polynomial-methods-page-1-22
# Build higher powers
p = Polynomial([1, 1])  # 1 + x

print(f"(1 + x)⁰ = 1")
print(f"(1 + x)¹ = {p}")
print(f"(1 + x)² = {p * p}")
print(f"(1 + x)³ = {p * p * p}")
print(f"(1 + x)⁴ = {p * p * p * p}")

# Notice the coefficients - they're binomial coefficients!
# Pascal's triangle!
```

```python exec
id: polynomials-4-polynomial-methods-page-1-23
# Verify by evaluation
p1 = Polynomial([2, 3])
p2 = Polynomial([1, -1])
product = p1 * p2

x = 7
print(f"At x={x}:")
print(f"p1({x}) = {p1.evaluate(x)}")
print(f"p2({x}) = {p2.evaluate(x)}")
print(f"p1({x}) * p2({x}) = {p1.evaluate(x) * p2.evaluate(x)}")
print(f"product({x}) = {product.evaluate(x)}")
print(f"Match? {abs(product.evaluate(x) - p1.evaluate(x) * p2.evaluate(x)) < 1e-10}")
```

## Looking back

Before leaving this page, a sentence on each. What you write stays on this device.

```reflect
- Something you expected before running a cell that turned out differently
- The one idea from this page you could explain to someone else now
- A question this page raised that it did not answer
```
