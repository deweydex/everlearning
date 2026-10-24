---
title: "Tutorial 4: Polynomial Arithmetic - Combining Polynomials (2 of 2)"
slug: polynomials-4-polynomial-methods-page-2
course: programming-and-design-principles
series: oop-polynomials
series_title: "Object-Oriented Programming: A Worked Project"
version: 2026.09.07.1
---

*Page 2 of 2.*

*Before starting this page, run the cell below. It repeats the setup from the earlier pages that this page uses.*

```python exec
id: polynomials-4-polynomial-methods-page-2-setup
# From an earlier page of this tutorial: needed again here.
import numpy as np
import matplotlib.pyplot as plt

# From an earlier page of this tutorial: needed again here.
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

# From an earlier page of this tutorial: needed again here.
# Quick test
p = Polynomial([3, -4, 1])  # 3 - 4x + x²
print(f"Polynomial: {p}")
print(f"Degree: {p.degree()}")
print(f"At x=2: {p.evaluate(2)}")
print(f"Derivative: {p.derivative()}")

# From an earlier page of this tutorial: needed again here.
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

# From an earlier page of this tutorial: needed again here.
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

# From an earlier page of this tutorial: needed again here.
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

# From an earlier page of this tutorial: needed again here.
p1 = Polynomial([2, 3, 1])      # 2 + 3x + x²
p2 = Polynomial([1, 1, 0, 2])   # 1 + x + 2x³

p3 = p1 + p2
print(f"({p1}) + ({p2}) = {p3}")

# From an earlier page of this tutorial: needed again here.
# What if we add a polynomial to itself?
p = Polynomial([1, 2, 3])
print(f"p = {p}")

double = p + p
print(f"p + p = {double}")
# All coefficients should be doubled!

# From an earlier page of this tutorial: needed again here.
# What about adding opposites?
p1 = Polynomial([1, 2, 3])
p2 = Polynomial([-1, -2, -3])

zero = p1 + p2
print(f"({p1}) + ({p2}) = {zero}")
# Should be the zero polynomial!

# From an earlier page of this tutorial: needed again here.
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

# From an earlier page of this tutorial: needed again here.
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

# From an earlier page of this tutorial: needed again here.
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

# From an earlier page of this tutorial: needed again here.
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

# From an earlier page of this tutorial: needed again here.
# Test subtraction
p1 = Polynomial([5, 3, 1])
p2 = Polynomial([2, 1])

print(f"p1 = {p1}")
print(f"p2 = {p2}")
print(f"p1 - p2 = {p1 - p2}")
print(f"p2 - p1 = {p2 - p1}")

# From an earlier page of this tutorial: needed again here.
# Subtract from itself - should get zero
p = Polynomial([1, 2, 3, 4])
zero = p - p
print(f"({p}) - ({p}) = {zero}")

# From an earlier page of this tutorial: needed again here.
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

# From an earlier page of this tutorial: needed again here.
# Test once you've implemented it
p1 = Polynomial([1, 1])  # 1 + x
p2 = Polynomial([1, 1])  # 1 + x

product = p1 * p2
print(f"({p1}) * ({p2}) = {product}")
# Should be 1 + 2x + x²

# From an earlier page of this tutorial: needed again here.
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

# From an earlier page of this tutorial: needed again here.
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

# From an earlier page of this tutorial: needed again here.
# Simple case: (1 + x)(1 + x)
p = Polynomial([1, 1])
p_squared = p * p
print(f"({p})² = {p_squared}")
# Should be 1 + 2x + x²

# From an earlier page of this tutorial: needed again here.
# Verify a factorization: x² - 1 = (x + 1)(x - 1)
p1 = Polynomial([1, 1])    # 1 + x (which is x + 1)
p2 = Polynomial([-1, 1])   # -1 + x (which is x - 1)

product = p1 * p2
print(f"({p1}) * ({p2}) = {product}")

expected = Polynomial([-1, 0, 1])  # -1 + 0x + x²
print(f"Expected: {expected}")

# From an earlier page of this tutorial: needed again here.
# Build higher powers
p = Polynomial([1, 1])  # 1 + x

print(f"(1 + x)⁰ = 1")
print(f"(1 + x)¹ = {p}")
print(f"(1 + x)² = {p * p}")
print(f"(1 + x)³ = {p * p * p}")
print(f"(1 + x)⁴ = {p * p * p * p}")

# Notice the coefficients - they're binomial coefficients!
# Pascal's triangle!

# From an earlier page of this tutorial: needed again here.
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

## Part E: Testing Equality

It's useful to check if two polynomials are the same. But there's a subtlety:

```python
[1, 2, 0] and [1, 2] represent the same polynomial (1 + 2x)
```

We need to compare them based on their **actual degrees**, not just list equality.

### Implementing __eq__()

```python exec
id: polynomials-4-polynomial-methods-page-2-1
class Polynomial:
    # ... all previous methods ...
    
    def __eq__(self, other):
        """
        Test if two polynomials are equal.
        
        Careful: [1, 2, 0] and [1, 2] represent the same polynomial!
        
        Parameters:
        -----------
        other : Polynomial
            The polynomial to compare to
            
        Returns:
        --------
        bool
            True if polynomials are equal
        """
        # First check degrees
        d1 = self.degree()
        d2 = other.degree()
        
        if d1 != d2:
            return False
        
        # Compare coefficients up to the degree
        for i in range(d1 + 1):
            c1 = self.coeffs[i] if i < len(self.coeffs) else 0
            c2 = other.coeffs[i] if i < len(other.coeffs) else 0
            # Allow tiny numerical errors
            if abs(c1 - c2) > 1e-10:
                return False
        
        return True
```

Let's add this to our complete class and use it to verify algebraic identities:

```python exec
id: polynomials-4-polynomial-methods-page-2-2
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
    
    def __eq__(self, other):
        d1 = self.degree()
        d2 = other.degree()
        
        if d1 != d2:
            return False
        
        for i in range(d1 + 1):
            c1 = self.coeffs[i] if i < len(self.coeffs) else 0
            c2 = other.coeffs[i] if i < len(other.coeffs) else 0
            if abs(c1 - c2) > 1e-10:
                return False
        
        return True
```

## Part F: Verifying Algebraic Identities

Now we can use our polynomial arithmetic to verify famous algebraic identities!

```python exec
id: polynomials-4-polynomial-methods-page-2-3
# Identity: (a + b)² = a² + 2ab + b²
a = Polynomial([0, 1])  # x
b = Polynomial([1])     # 1

lhs = (a + b) * (a + b)
rhs = a*a + Polynomial([2])*a*b + b*b

print(f"(a + b)² = {lhs}")
print(f"a² + 2ab + b² = {rhs}")
print(f"Equal? {lhs == rhs}")
```

```python exec
id: polynomials-4-polynomial-methods-page-2-4
# Identity: (a + b)(a - b) = a² - b²
a = Polynomial([0, 1])  # x
b = Polynomial([1])     # 1

lhs = (a + b) * (a - b)
rhs = a*a - b*b

print(f"(a + b)(a - b) = {lhs}")
print(f"a² - b² = {rhs}")
print(f"Equal? {lhs == rhs}")
```

```python exec
id: polynomials-4-polynomial-methods-page-2-5
# Identity: (a + b)³ = a³ + 3a²b + 3ab² + b³
a = Polynomial([0, 1])  # x
b = Polynomial([1])     # 1

lhs = (a + b) * (a + b) * (a + b)
rhs = (a*a*a + 
       Polynomial([3])*a*a*b + 
       Polynomial([3])*a*b*b + 
       b*b*b)

print(f"(a + b)³ = {lhs}")
print(f"a³ + 3a²b + 3ab² + b³ = {rhs}")
print(f"Equal? {lhs == rhs}")
```

## Part G: Building Polynomials from Roots

If we know the roots of a polynomial, we can build it by multiplying linear factors:

```python exec
id: polynomials-4-polynomial-methods-page-2-6
def polynomial_from_roots(roots: list):
    """
    Build a polynomial with given roots.
    
    If roots are r₁, r₂, r₃, then polynomial is:
    (x - r₁)(x - r₂)(x - r₃)
    
    Parameters:
    -----------
    roots : list
        List of roots
        
    Returns:
    --------
    Polynomial
        The polynomial with those roots
    """
    result = Polynomial([1])  # Start with 1
    
    for root in roots:
        # Multiply by (x - root)
        factor = Polynomial([-root, 1])  # -root + x
        result = result * factor
    
    return result
```

```python exec
id: polynomials-4-polynomial-methods-page-2-7
# Build a polynomial with roots at 1, 2, 3
p = polynomial_from_roots([1, 2, 3])
print(f"Polynomial with roots 1, 2, 3: {p}")

# Verify the roots
for root in [1, 2, 3]:
    print(f"p({root}) = {p.evaluate(root)}")

# Expand manually to check:
# (x-1)(x-2)(x-3) = (x-1)(x² - 5x + 6)
#                  = x³ - 5x² + 6x - x² + 5x - 6
#                  = x³ - 6x² + 11x - 6
# Coefficients: [-6, 11, -6, 1] ✓
```

```python exec
id: polynomials-4-polynomial-methods-page-2-8
# Build and plot a polynomial with roots at -2, 0, 1, 3
p = polynomial_from_roots([-2, 0, 1, 3])
print(f"Polynomial: {p}")
p.plot(x_min=-3, x_max=4)
```

## Summary: The Power of Polynomial Arithmetic

We've now implemented:

### Operations:
- **Addition** (`+`): Combine like terms
- **Subtraction** (`-`): Subtract coefficients
- **Multiplication** (`*`): Each term multiplies each term
- **Equality** (`==`): Compare degrees and coefficients

### From Tutorial 3:
- **Derivatives**: Power rule
- **Integrals**: Reverse power rule
- **Evaluation**: Calculate f(x)
- **Plotting**: Visualize

### What we can do now:
- Verify algebraic identities
- Build polynomials from roots
- Explore binomial expansions
- Factor and expand
- Work with polynomials of ANY degree!

## Exercises

### Your turn 1: Binomial Coefficients

```python exec
id: polynomials-4-polynomial-methods-page-2-9
# Compute (1 + x)^n for n = 0, 1, 2, 3, 4, 5
# Print each result
# Notice the coefficients - do they form a pattern?
# This is Pascal's triangle!

# YOUR CODE HERE
```

### Your turn 2: Factoring Check

```python exec
id: polynomials-4-polynomial-methods-page-2-10
# Verify these factorizations by multiplying:
# 1. x² - 4 = (x + 2)(x - 2)
# 2. x² - 5x + 6 = (x - 2)(x - 3)
# 3. x³ - 1 = (x - 1)(x² + x + 1)

# YOUR CODE HERE
```

### Your turn 3: Building from Roots

```python exec
id: polynomials-4-polynomial-methods-page-2-11
# Use polynomial_from_roots to build polynomials with:
# 1. Roots at -1 and 1
# 2. Roots at 0, 0, and 2 (a repeated root!)
# 3. Roots at -2, -1, 1, 2

# For each one:
# - Print the polynomial
# - Verify the roots by evaluation
# - Plot it

# YOUR CODE HERE
```

### Your turn 4: Derivative of a Product

```python exec
id: polynomials-4-polynomial-methods-page-2-12
# The product rule says: (fg)' = f'g + fg'

# Let f(x) = x² and g(x) = x + 1
# Compute (fg)' two ways:
# 1. Multiply f and g, then take derivative
# 2. Use product rule: f'g + fg'

# Do they match?

# YOUR CODE HERE
```

### Your turn 5: Working with Differences

```python exec
id: polynomials-4-polynomial-methods-page-2-13
# Create p(x) = x³ - 3x² + 3x - 1
# Create q(x) = x³

# Compute p - q
# What do you get?

# Now try: is (x - 1)³ equal to p?
# Hint: Use multiplication to expand (x - 1)³

# YOUR CODE HERE
```

## Reflection and Looking Ahead

Our `Polynomial` class is now very powerful! We can:
- Represent any polynomial
- Add, subtract, multiply them
- Take derivatives and integrals
- Verify algebraic identities
- Build polynomials from roots

### But we still have the trade-off from Tutorial 3:

**What we gained:**
- Generality (any degree)
- Rich operations (+, -, *, derivative, integral)
- No code duplication
- Clean, elegant implementation

**What we lost:**
- Easy exact root formulas (quadratic formula)
- Special methods (vertex, discriminant)
- Intuitive interface for common cases
- Clear names (have to remember coefficient order)

### Next Time: Tutorial 5 - Inheritance

In Tutorial 5, we'll learn about **inheritance** - a way to create specialized `Linear` and `Quadratic` classes that:
- **Inherit** all the general methods from `Polynomial` (derivative, integrate, +, -, *, etc.)
- **Add** specialized methods (vertex, discriminant, exact root formulas)
- **Override** methods where needed (prettier `__str__`)
- **Work together** seamlessly

This will give us **the best of both worlds**!

---

**End of Tutorial 4**

## Looking back

Before leaving this page, a sentence on each. What you write stays on this device.

```reflect
- Something you expected before running a cell that turned out differently
- The one idea from this page you could explain to someone else now
- A question this page raised that it did not answer
```
