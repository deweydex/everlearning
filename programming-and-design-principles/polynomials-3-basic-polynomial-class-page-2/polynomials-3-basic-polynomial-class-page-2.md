---
title: "Tutorial 3: The Polynomial Class - General Representation (2 of 2)"
slug: polynomials-3-basic-polynomial-class-page-2
course: programming-and-design-principles
series: oop-polynomials
series_title: "Object-Oriented Programming: A Worked Project"
version: 2026.09.07.1
---

*Page 2 of 2.*

*Before starting this page, run the cell below. It repeats the setup from the earlier pages that this page uses.*

```python exec
id: polynomials-3-basic-polynomial-class-page-2-setup
# From an earlier page of this tutorial: needed again here.
import numpy as np
import matplotlib.pyplot as plt

# From an earlier page of this tutorial: needed again here.
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

# From an earlier page of this tutorial: needed again here.
# Test basic creation and degree
p1 = Polynomial([5])              # Constant
p2 = Polynomial([3, 2])           # Linear
p3 = Polynomial([3, -4, 1])       # Quadratic
p4 = Polynomial([1, 0, -1, 0, 1]) # Quartic

print(f"p1 coeffs: {p1.coeffs}, degree: {p1.degree()}")
print(f"p2 coeffs: {p2.coeffs}, degree: {p2.degree()}")
print(f"p3 coeffs: {p3.coeffs}, degree: {p3.degree()}")
print(f"p4 coeffs: {p4.coeffs}, degree: {p4.degree()}")

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

# From an earlier page of this tutorial: needed again here.
# Test your implementation
p = Polynomial([3, -4, 1])  # 3 - 4x + x²

print(f"f(0) = {p.evaluate(0)}")  # Should be 3
print(f"f(1) = {p.evaluate(1)}")  # Should be 0 (3 - 4 + 1 = 0)
print(f"f(2) = {p.evaluate(2)}")  # Should be -1 (3 - 8 + 4 = -1)
print(f"f(3) = {p.evaluate(3)}")  # Should be 0 (3 - 12 + 9 = 0)

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
        """Evaluate the polynomial at x."""
        result = 0
        for i, coeff in enumerate(self.coeffs):
            result += coeff * (x ** i)
        return result

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
        """
        Return a readable string representation.
        
        Returns:
        --------
        str
            String like "2 - 3x + x²"
        """
        # YOUR CODE HERE
        pass

# From an earlier page of this tutorial: needed again here.
# Test your implementation
p1 = Polynomial([5])
p2 = Polynomial([3, 2])
p3 = Polynomial([3, -4, 1])
p4 = Polynomial([1, 0, -1, 0, 1])

print(f"p1: {p1}")
print(f"p2: {p2}")
print(f"p3: {p3}")
print(f"p4: {p4}")

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

# From an earlier page of this tutorial: needed again here.
# Test your implementation
p = Polynomial([3, -4, 1])  # x² - 4x + 3
p.plot(x_min=-1, x_max=5)

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

# From an earlier page of this tutorial: needed again here.
# A constant
p_const = Polynomial([3])
print(f"Constant: {p_const}")
p_const.plot(x_min=-5, x_max=5)

# From an earlier page of this tutorial: needed again here.
# A linear function
p_linear = Polynomial([3, 2])
print(f"Linear: {p_linear}")
p_linear.plot(x_min=-5, x_max=5)

# From an earlier page of this tutorial: needed again here.
# A quadratic
p_quad = Polynomial([3, -4, 1])
print(f"Quadratic: {p_quad}")
p_quad.plot(x_min=-1, x_max=5)

# From an earlier page of this tutorial: needed again here.
# A cubic! (We couldn't do this before!)
p_cubic = Polynomial([-6, 11, -6, 1])  # x³ - 6x² + 11x - 6
print(f"Cubic: {p_cubic}")
print(f"Degree: {p_cubic.degree()}")
p_cubic.plot(x_min=-1, x_max=4)

# From an earlier page of this tutorial: needed again here.
# A quartic!
p_quartic = Polynomial([1, 0, -1, 0, 1])  # 1 - x² + x⁴
print(f"Quartic: {p_quartic}")
print(f"Degree: {p_quartic.degree()}")
p_quartic.plot(x_min=-2, x_max=2)

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

# From an earlier page of this tutorial: needed again here.
# Test your implementation
p = Polynomial([3, -4, 1])  # 3 - 4x + x²
print(f"Function: {p}")

p_prime = p.derivative()
print(f"Derivative: {p_prime}")  # Should be -4 + 2x

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
        """Return the derivative using the power rule."""
        if self.degree() == 0:
            return Polynomial([0])
        
        new_coeffs = []
        for i in range(1, len(self.coeffs)):
            new_coeffs.append(i * self.coeffs[i])
        
        return Polynomial(new_coeffs)

# From an earlier page of this tutorial: needed again here.
# Cubic derivative
cubic = Polynomial([-6, 11, -6, 1])  # -6 + 11x - 6x² + x³
print(f"Cubic: {cubic}")
print(f"Derivative: {cubic.derivative()}")  # Should be 11 - 12x + 3x²
print()

# Quartic derivative
quartic = Polynomial([1, 0, -1, 0, 1])  # 1 - x² + x⁴
print(f"Quartic: {quartic}")
print(f"Derivative: {quartic.derivative()}")  # Should be -2x + 4x³

# From an earlier page of this tutorial: needed again here.
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

**Beautiful!** The degree decreases by 1 each time, until we reach the zero polynomial.

## Part D: Integration - The Reverse Power Rule

The **reverse power rule** for integrals says:

```
∫cx^n dx = c·x^(n+1)/(n+1) + C
```

For coefficients `[c₀, c₁, c₂, c₃, ...]`:

```
∫(c₀ + c₁x + c₂x² + c₃x³ + ...) dx = C + c₀x + c₁x²/2 + c₂x³/3 + c₃x⁴/4 + ...
```

**Pattern:** `new_coeffs[0] = C`, `new_coeffs[i+1] = old_coeffs[i]/(i+1)`

### YOUR TURN: Implement integrate()

```python exec
id: polynomials-3-basic-polynomial-class-page-2-1
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
        """
        Return the integral using the reverse power rule.
        
        For coefficients [c₀, c₁, c₂, ...] representing c₀ + c₁x + c₂x²...
        The integral is [C, c₀, c₁/2, c₂/3, ...] representing C + c₀x + c₁x²/2 + c₂x³/3...
        
        Parameters:
        -----------
        C : float
            The constant of integration (default: 0)
        
        Returns:
        --------
        Polynomial
            A new Polynomial representing the integral
        """
        # YOUR CODE HERE
        pass
```

```python exec
id: polynomials-3-basic-polynomial-class-page-2-2
# Test your implementation
p = Polynomial([3, -4, 1])  # 3 - 4x + x²
print(f"Function: {p}")

integral = p.integrate(C=0)
print(f"Integral: {integral}")  # Should be 3x - 2x² + (1/3)x³

# Verify: derivative of integral should give original
check = integral.derivative()
print(f"Derivative of integral: {check}")
```

**Solution:**

```python exec
id: polynomials-3-basic-polynomial-class-page-2-3
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
        """Return the integral using the reverse power rule."""
        new_coeffs = [C]
        for i, coeff in enumerate(self.coeffs):
            new_coeffs.append(coeff / (i + 1))
        
        return Polynomial(new_coeffs)
```

## VICTORY: Integration Finally Works!

Remember when we couldn't integrate quadratics because we didn't have a Cubic class? Now we can!

```python exec
id: polynomials-3-basic-polynomial-class-page-2-4
# Integrate a quadratic - we couldn't do this before!
quad = Polynomial([2, -3, 1])  # 2 - 3x + x²
print(f"Quadratic: {quad}")

quad_integral = quad.integrate(C=0)
print(f"Integral: {quad_integral}")
print(f"Integral degree: {quad_integral.degree()}")  # Should be 3 (cubic!)

# Verify
check = quad_integral.derivative()
print(f"\nDerivative of integral: {check}")
print(f"Original: {quad}")
print(f"Match? They should!")
```

```python exec
id: polynomials-3-basic-polynomial-class-page-2-5
# Integrate a cubic!
cubic = Polynomial([-6, 11, -6, 1])
print(f"Cubic: {cubic}")

cubic_integral = cubic.integrate(C=0)
print(f"Integral: {cubic_integral}")
print(f"Integral degree: {cubic_integral.degree()}")  # Should be 4 (quartic!)
```

```python exec
id: polynomials-3-basic-polynomial-class-page-2-6
# We can keep going!
p = Polynomial([1])
print(f"Start: {p}")

p1 = p.integrate(C=0)
print(f"Integral 1: {p1}")

p2 = p1.integrate(C=0)
print(f"Integral 2: {p2}")

p3 = p2.integrate(C=0)
print(f"Integral 3: {p3}")

p4 = p3.integrate(C=0)
print(f"Integral 4: {p4}")
```

## Part E: What We've Gained and Lost

### What We've GAINED:

Let's celebrate what now works:

```python exec
id: polynomials-3-basic-polynomial-class-page-2-7
print("✓ Can represent ANY polynomial degree")
print("✓ Derivatives work for everything")
print("✓ Integrals work for everything")
print("✓ Only ONE class instead of infinite")
print("✓ No code duplication (plot() defined once!)")
print("✓ Can work with polynomials we couldn't before (cubic, quartic, ...)")
```

### What We've LOST:

But there are trade-offs. Let's see what we gave up.

#### 1. Easy Exact Root Formulas

For quadratics, we had the quadratic formula. For the general `Polynomial` class, we don't have easy exact formulas:

```python exec
id: polynomials-3-basic-polynomial-class-page-2-8
# With Quadratic class (from Tutorial 2), we had:
# roots = quad.find_roots()  # Exact, using quadratic formula

# With Polynomial class, we need numerical methods
# (We'll add this soon, but it won't be exact)
```

#### 2. Special Methods Like vertex()

Quadratics have a `vertex()`. But not all polynomials have vertices:

```python exec
id: polynomials-3-basic-polynomial-class-page-2-9
# With Quadratic class:
# vertex_x, vertex_y = quad.vertex()  # Easy!

# With Polynomial class:
# No vertex() method - only makes sense for degree 2
# We'd have to manually check degree and extract coefficients
```

#### 3. No discriminant()

The discriminant is specific to quadratics:

```python exec
id: polynomials-3-basic-polynomial-class-page-2-10
# With Quadratic class:
# disc = quad.discriminant()  # Tells us about roots

# With Polynomial class:
# No discriminant() - concept only applies to degree 2
```

#### 4. Less Intuitive Interface

Compare creating the same quadratic:

```python exec
id: polynomials-3-basic-polynomial-class-page-2-11
# Old way (Quadratic class):
# quad = Quadratic(a=1, b=-4, c=3)
# Clear what a, b, c mean!

# New way (Polynomial class):
quad = Polynomial([3, -4, 1])
# Have to remember: constant, x, x² order
# Easy to make mistakes!
```

### The Central Trade-off

We traded **SPECIFICITY** for **GENERALITY**:

**Specific classes** (Constant, Linear, Quadratic):
- Clear, intuitive interfaces
- Fast, exact methods
- Special methods for special properties
- Easy to understand and use
- BUT: Limited to specific degrees, lots of code duplication

**General class** (Polynomial):
- Works for any degree
- No code duplication
- Clean, elegant implementation
- BUT: Less intuitive, no special methods, harder to use

## The Question Emerges

**Can we have BOTH?**

- Keep the generality of `Polynomial`
- Recover the specificity of `Quadratic` and `Linear`
- Avoid code duplication
- Get the best of both worlds?

**Answer: Inheritance!** (Coming in Tutorial 4)

We'll create `Linear` and `Quadratic` classes that **inherit** from `Polynomial`, so they:
- Get all the general methods (derivative, integrate, plot)
- Can add specialized methods (vertex, discriminant)
- Have clear, intuitive interfaces
- Work together seamlessly

But first, let's explore more of what we can do with our general `Polynomial` class!

## Part F: A Useful Tool - Newton's Method

Since we don't have exact formulas for roots of general polynomials, we'll use **Newton's method** - a numerical approach that uses derivatives!

Here's the implementation (we're providing this as a tool):

```python exec
id: polynomials-3-basic-polynomial-class-page-2-12
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
    
    def find_root_newton(self, initial_guess: float, tolerance: float = 1e-6, 
                        max_iterations: int = 100):
        """
        Find a root using Newton's method: x_new = x_old - f(x_old)/f'(x_old)
        
        Parameters:
        -----------
        initial_guess : float
            Starting point for the search
        tolerance : float
            How close to zero is "close enough"
        max_iterations : int
            Maximum number of steps to take
            
        Returns:
        --------
        float or None
            The root if found, None if method fails
        """
        x = initial_guess
        deriv = self.derivative()
        
        for _ in range(max_iterations):
            fx = self.evaluate(x)
            
            # Check if we found a root
            if abs(fx) < tolerance:
                return x
            
            # Get derivative at current point
            fpx = deriv.evaluate(x)
            
            # Check for zero derivative (method fails)
            if abs(fpx) < tolerance:
                return None
            
            # Newton's method update
            x = x - fx / fpx
        
        return None  # Didn't converge
```

### Using Newton's Method

```python exec
id: polynomials-3-basic-polynomial-class-page-2-13
# This cubic has roots at 1, 2, and 3
# It factors as (x-1)(x-2)(x-3)
cubic = Polynomial([-6, 11, -6, 1])  # -6 + 11x - 6x² + x³

print(f"Finding roots of {cubic}")
print()

# Try different starting points
for guess in [0, 1.5, 2.5, 3.5]:
    root = cubic.find_root_newton(guess)
    if root:
        print(f"Starting from {guess}: found root at {root:.6f}")
        print(f"  Check: f({root:.6f}) = {cubic.evaluate(root):.10f}")
    else:
        print(f"Starting from {guess}: method failed")
```

**Notice:** Different starting points find different roots! This is expected - the method finds whichever root is "closest" to the initial guess.

## Exercises

### Your turn 1: Creating Polynomials

```python exec
id: polynomials-3-basic-polynomial-class-page-2-14
# Create polynomials for:
# 1. f(x) = 2x³ - 5x + 3
# 2. f(x) = x⁴ - 16
# 3. f(x) = 1 + x + x² + x³ + x⁴

# For each one:
# - Print it
# - Find its degree
# - Evaluate it at x=2
# - Plot it

# YOUR CODE HERE
```

### Your turn 2: Derivative Chain

```python exec
id: polynomials-3-basic-polynomial-class-page-2-15
# Start with p(x) = x⁵
# Take successive derivatives until you reach 0
# At each step, print the polynomial and its degree
# How many derivatives does it take?

# YOUR CODE HERE
```

### Your turn 3: Integration Verification

```python exec
id: polynomials-3-basic-polynomial-class-page-2-16
# Pick any polynomial
# Integrate it (with C=0)
# Take the derivative of the integral
# Do you get back the original polynomial?

# Try this with polynomials of different degrees

# YOUR CODE HERE
```

### Your turn 4: Finding Roots

```python exec
id: polynomials-3-basic-polynomial-class-page-2-17
# Create p(x) = x³ - 2x² - x + 2
# This factors as (x-1)(x+1)(x-2), so roots are -1, 1, 2

# Use Newton's method with different starting guesses to find all three roots
# Verify each root by evaluating the polynomial there

# YOUR CODE HERE
```

### Your turn 5: Representing Old Classes

```python exec
id: polynomials-3-basic-polynomial-class-page-2-18
# Create Polynomial objects that represent:
# 1. The constant function f(x) = 7
# 2. The linear function f(x) = 3x - 5
# 3. The quadratic f(x) = 2x² - 4x + 1

# For each one:
# - Take the derivative
# - Compare to what we got with the specific classes in Tutorials 1-2
# - Do they match?

# YOUR CODE HERE
```

## Reflection

We've created a powerful, general `Polynomial` class that solves many of our problems:

**Problems Solved:**
- No more code duplication
- Can represent any degree
- Derivatives work everywhere
- Integrals work everywhere
- Only one class needed

**New Trade-offs:**
- Lost specific methods (vertex, discriminant)
- Less intuitive interface
- No exact root formulas
- Harder to use for common cases

**Next time** (Tutorial 4), we'll learn about **inheritance** - a way to keep the general `Polynomial` class while also having specific `Linear` and `Quadratic` classes that get the best of both worlds!

---

**End of Tutorial 3**

## Looking back

Before leaving this page, a sentence on each. What you write stays on this device.

```reflect
- Something you expected before running a cell that turned out differently
- The one idea from this page you could explain to someone else now
- A question this page raised that it did not answer
```
