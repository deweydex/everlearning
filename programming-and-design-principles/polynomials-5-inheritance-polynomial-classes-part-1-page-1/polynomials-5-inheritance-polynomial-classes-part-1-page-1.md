---
title: "Tutorial 5 Part 1: Inheritance - Best of Both Worlds (1 of 2)"
slug: polynomials-5-inheritance-polynomial-classes-part-1-page-1
course: programming-and-design-principles
series: oop-polynomials
series_title: "Object-Oriented Programming: A Worked Project"
version: 2026.09.07.1
---

*Page 1 of 2.*

# Tutorial 5 Part 1: Inheritance - Best of Both Worlds

## Introduction

We've come a long way! Let's review our journey:

**Tutorial 1**: Built `Constant` and `Linear` classes
- Simple, clear interfaces
- But lots of code duplication
- Can't integrate (need more classes)

**Tutorial 2**: Added `Quadratic` class
- Beautiful derivative chain: Quadratic → Linear → Constant → 0
- Special methods: `vertex()`, `discriminant()`
- But problems got worse (more duplication, still can't integrate)

**Tutorial 3**: Created general `Polynomial` class
- Can represent ANY degree
- Derivatives and integrals work universally
- No code duplication
- But lost special methods and intuitive interfaces

**Tutorial 4**: Added polynomial arithmetic
- Can add, subtract, multiply polynomials
- Build from roots, verify identities
- Very powerful, but still miss the specialized classes

## The Central Question

**Can we have BOTH?**

- The **generality** of `Polynomial` (derivatives/integrals work everywhere, arithmetic operations)
- The **specificity** of `Linear` and `Quadratic` (clear interfaces, special methods)

**Answer: YES! Through INHERITANCE.**

Today we'll discover how.

---

```python exec
id: polynomials-5-inheritance-polynomial-classes-part-1-page-1-1
import numpy as np
import matplotlib.pyplot as plt
```

## Part A: What is Inheritance?

### The Concept

**Inheritance** lets us create a new class based on an existing class:
- The **parent class** (or **base class** or **superclass**) provides general functionality
- The **child class** (or **derived class** or **subclass**) inherits that functionality and can:
 - Add new methods
 - Override existing methods
 - Extend or modify behavior

### A Simple Analogy

Think about vehicles:
- All vehicles have wheels, can move, need fuel
- But a `Car` is different from a `Motorcycle`
- We could create a general `Vehicle` class
- Then `Car` and `Motorcycle` **inherit** from `Vehicle`
- They get all the vehicle features for free
- But can add their own specific features (Car has 4 doors, Motorcycle has handlebars)

### Why This Solves Our Problem

We'll:
1. Keep our general `Polynomial` class as the parent
2. Create `Linear` and `Quadratic` that **inherit** from `Polynomial`
3. They automatically get: `derivative()`, `integrate()`, `+`, `-`, `*`, `evaluate()`, `plot()`
4. But we can add specialized methods: `vertex()`, `discriminant()`, exact `find_roots()`
5. And override methods to make them prettier: nicer `__init__`, better `__str__()`

Let's see it in action!

---

## Part B: Our Foundation - The Polynomial Class

First, let's bring back our complete `Polynomial` class from Tutorials 3 and 4:

```python exec
id: polynomials-5-inheritance-polynomial-classes-part-1-page-1-2
class Polynomial:
    """
    A class representing a polynomial of any degree.
    
    Attributes:
    -----------
    coeffs : list of float
        Coefficients where coeffs[i] is the coefficient of x^i
    """
    
    def __init__(self, coefficients: list):
        """Create a polynomial from coefficient list."""
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
        """Return string representation."""
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
        """Return the derivative."""
        if self.degree() == 0:
            return Polynomial([0])
        
        new_coeffs = []
        for i in range(1, len(self.coeffs)):
            new_coeffs.append(i * self.coeffs[i])
        
        return Polynomial(new_coeffs)
    
    def integrate(self, C: float = 0):
        """Return the integral."""
        new_coeffs = [C]
        for i, coeff in enumerate(self.coeffs):
            new_coeffs.append(coeff / (i + 1))
        
        return Polynomial(new_coeffs)
    
    def __add__(self, other):
        """Add two polynomials."""
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
        """Subtract two polynomials."""
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
        """Multiply two polynomials."""
        result_degree = self.degree() + other.degree()
        new_coeffs = [0] * (result_degree + 1)
        
        for i, coeff_a in enumerate(self.coeffs):
            for j, coeff_b in enumerate(other.coeffs):
                power = i + j
                new_coeffs[power] += coeff_a * coeff_b
        
        return Polynomial(new_coeffs)
    
    def __eq__(self, other):
        """Test equality."""
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

Let's verify it works:

```python exec
id: polynomials-5-inheritance-polynomial-classes-part-1-page-1-3
p = Polynomial([3, -4, 1])  # 3 - 4x + x²
print(f"Polynomial: {p}")
print(f"Degree: {p.degree()}")
print(f"At x=2: {p.evaluate(2)}")
print(f"Derivative: {p.derivative()}")
```

---

## Part C: Creating Linear - Our First Inherited Class

### The Basic Syntax

To make `Linear` inherit from `Polynomial`, we use:

```python
class Linear(Polynomial):
 # Linear-specific code here
```

The `(Polynomial)` means "Linear inherits from Polynomial".

### What We Want

We want to create a linear function like:
```python
line = Linear(m=2, b=3) # f(x) = 2x + 3
```

But internally, this should be stored as a `Polynomial` with coefficients `[b, m]` = `[3, 2]`.

### Step 1: Basic Inheritance

```python exec
id: polynomials-5-inheritance-polynomial-classes-part-1-page-1-4
class Linear(Polynomial):
    """
    A class representing a linear function f(x) = mx + b.
    
    This inherits from Polynomial, so it gets all polynomial
    methods for free (derivative, integrate, +, -, *, etc.)
    
    Attributes:
    -----------
    m : float
        The slope
    b : float
        The y-intercept
    coeffs : list
        Inherited from Polynomial: [b, m]
    """
    
    def __init__(self, m: float, b: float):
        """
        Create a linear function f(x) = mx + b
        
        Parameters:
        -----------
        m : float
            The slope
        b : float
            The y-intercept
        """
        # Store m and b for easy access
        self.m = m
        self.b = b
        
        # Initialize the parent Polynomial class
        # [b, m] represents b + mx
        super().__init__([b, m])
```

**Key line:** `super().__init__([b, m])`

- `super()` refers to the parent class (`Polynomial`)
- We call its `__init__` method
- We pass `[b, m]` as the coefficient list
- This sets `self.coeffs = [b, m]`

Now our `Linear` object has:
- `self.m` and `self.b` (easy to access)
- `self.coeffs = [b, m]` (for Polynomial methods)

Let's test it:

```python exec
id: polynomials-5-inheritance-polynomial-classes-part-1-page-1-5
line = Linear(m=2, b=3)
print(f"Created: {line}")
print(f"Slope: {line.m}")
print(f"Y-intercept: {line.b}")
print(f"Coefficients: {line.coeffs}")
print(f"Degree: {line.degree()}")
```

**Notice:** We automatically have `degree()` method! We inherited it from `Polynomial`.

Let's try more inherited methods:

```python exec
id: polynomials-5-inheritance-polynomial-classes-part-1-page-1-6
line = Linear(m=2, b=3)

# Evaluate - inherited!
print(f"f(0) = {line.evaluate(0)}")
print(f"f(5) = {line.evaluate(5)}")

# Derivative - inherited!
deriv = line.derivative()
print(f"\nDerivative: {deriv}")
print(f"Type: {type(deriv).__name__}")

# Integrate - inherited!
integral = line.integrate(C=0)
print(f"\nIntegral: {integral}")
print(f"Type: {type(integral).__name__}")
```

And they work correctly because internally we're just a `Polynomial` with the right coefficients.

### Step 2: Overriding __str__() for Better Output

The current `__str__()` from `Polynomial` gives us `"3 + 2x"`. But we'd prefer `"2x + 3"` (slope first).

We can **override** the method:

```python exec
id: polynomials-5-inheritance-polynomial-classes-part-1-page-1-7
class Linear(Polynomial):
    def __init__(self, m: float, b: float):
        self.m = m
        self.b = b
        super().__init__([b, m])
    
    def __str__(self) -> str:
        """
        Return a nice string representation.
        
        Overrides Polynomial.__str__() to show mx + b format.
        """
        return f"{self.m}x + {self.b}"
```

```python exec
id: polynomials-5-inheritance-polynomial-classes-part-1-page-1-8
line = Linear(m=2, b=3)
print(f"Linear: {line}")  # Uses our new __str__()

# But Polynomial methods still work!
print(f"Derivative: {line.derivative()}")
print(f"Integral: {line.integrate()}")
```

### Step 3: Adding Specialized Methods

Now we can add methods that only make sense for linear functions:

```python exec
id: polynomials-5-inheritance-polynomial-classes-part-1-page-1-9
class Linear(Polynomial):
    def __init__(self, m: float, b: float):
        self.m = m
        self.b = b
        super().__init__([b, m])
    
    def __str__(self) -> str:
        return f"{self.m}x + {self.b}"
    
    def find_root(self):
        """
        Find where the linear function equals zero.
        
        This is a specialized method - only Linear has it!
        Uses the exact formula x = -b/m
        
        Returns:
        --------
        float or str
            The root, or a message if no unique root
        """
        if self.m == 0:
            if self.b == 0:
                return "All x values are roots"
            else:
                return "No roots"
        else:
            return -self.b / self.m
    
    def slope(self) -> float:
        """
        Return the slope.
        
        Another specialized method!
        """
        return self.m
    
    def y_intercept(self) -> float:
        """
        Return the y-intercept.
        """
        return self.b
```

**Let's test everything:**

```python exec
id: polynomials-5-inheritance-polynomial-classes-part-1-page-1-10
line = Linear(m=2, b=-6)

# Our new specialized methods
print(f"Function: {line}")
print(f"Slope: {line.slope()}")
print(f"Y-intercept: {line.y_intercept()}")
print(f"Root: {line.find_root()}")

# Inherited general methods
print(f"\nAt x=3: {line.evaluate(3)}")
print(f"Derivative: {line.derivative()}")
print(f"Integral: {line.integrate()}")
print(f"Degree: {line.degree()}")
```

### Step 4: Arithmetic Operations Work Too!

```python exec
id: polynomials-5-inheritance-polynomial-classes-part-1-page-1-11
line1 = Linear(m=2, b=3)   # 2x + 3
line2 = Linear(m=-1, b=5)  # -x + 5

# Addition
sum_lines = line1 + line2
print(f"({line1}) + ({line2}) = {sum_lines}")
print(f"Type: {type(sum_lines).__name__}")

# Multiplication
product = line1 * line2
print(f"\n({line1}) * ({line2}) = {product}")
print(f"Type: {type(product).__name__}")
print(f"Degree: {product.degree()}")
# Multiplying two linears gives a quadratic (degree 2)!
```

**Notice:** When we add two `Linear` objects, we get a `Polynomial` back (not another `Linear`). That's okay! The operations work correctly.

---

## Complete Linear Class with Inheritance

Here's our complete `Linear` class:

```python exec
id: polynomials-5-inheritance-polynomial-classes-part-1-page-1-12
class Linear(Polynomial):
    """
    A linear function f(x) = mx + b that inherits from Polynomial.
    
    Attributes:
    -----------
    m : float
        The slope
    b : float
        The y-intercept
    coeffs : list
        Inherited: [b, m]
    """
    
    def __init__(self, m: float, b: float):
        """Create a linear function f(x) = mx + b"""
        self.m = m
        self.b = b
        super().__init__([b, m])
    
    def __str__(self) -> str:
        """Return string representation (overrides Polynomial)."""
        return f"{self.m}x + {self.b}"
    
    def find_root(self):
        """Find the root using exact formula."""
        if self.m == 0:
            if self.b == 0:
                return "All x values are roots"
            else:
                return "No roots"
        else:
            return -self.b / self.m
    
    def slope(self) -> float:
        """Return the slope."""
        return self.m
    
    def y_intercept(self) -> float:
        """Return the y-intercept."""
        return self.b
```

---

## Part D: Creating Quadratic - More Complex Inheritance

Now let's create `Quadratic` following the same pattern, but adding even more specialized methods.

### Step 1: Basic Structure

```python exec
id: polynomials-5-inheritance-polynomial-classes-part-1-page-1-13
class Quadratic(Polynomial):
    """
    A quadratic function f(x) = ax² + bx + c that inherits from Polynomial.
    
    Attributes:
    -----------
    a : float
        Coefficient of x²
    b : float
        Coefficient of x
    c : float
        Constant term
    coeffs : list
        Inherited: [c, b, a]
    """
    
    def __init__(self, a: float, b: float, c: float):
        """Create a quadratic function f(x) = ax² + bx + c"""
        self.a = a
        self.b = b
        self.c = c
        # Coefficients: c + bx + ax²
        super().__init__([c, b, a])
    
    def __str__(self) -> str:
        """Return string representation."""
        return f"{self.a}x² + {self.b}x + {self.c}"
```

**Test it:**

```python exec
id: polynomials-5-inheritance-polynomial-classes-part-1-page-1-14
quad = Quadratic(a=1, b=-4, c=3)
print(f"Quadratic: {quad}")
print(f"At x=2: {quad.evaluate(2)}")
print(f"Derivative: {quad.derivative()}")
print(f"Integral: {quad.integrate()}")
```

### Step 2: Adding Specialized Methods

Now let's add all the quadratic-specific methods:

```python exec
id: polynomials-5-inheritance-polynomial-classes-part-1-page-1-15
class Quadratic(Polynomial):
    def __init__(self, a: float, b: float, c: float):
        self.a = a
        self.b = b
        self.c = c
        super().__init__([c, b, a])
    
    def __str__(self) -> str:
        return f"{self.a}x² + {self.b}x + {self.c}"
    
    def discriminant(self) -> float:
        """
        Calculate the discriminant b² - 4ac.
        
        This is a specialized method - only makes sense for quadratics!
        
        Returns:
        --------
        float
            The discriminant value
        """
        return self.b**2 - 4*self.a*self.c
    
    def find_roots(self):
        """
        Find the roots using the quadratic formula.
        
        This is exact! (Unlike Newton's method)
        
        Returns:
        --------
        list
            List of roots (empty, one, or two roots)
        """
        disc = self.discriminant()
        
        if disc < 0:
            return []  # No real roots
        elif disc == 0:
            # One root (vertex on x-axis)
            root = -self.b / (2 * self.a)
            return [root]
        else:
            # Two roots
            sqrt_disc = disc ** 0.5
            root1 = (-self.b + sqrt_disc) / (2 * self.a)
            root2 = (-self.b - sqrt_disc) / (2 * self.a)
            return [root1, root2]
    
    def vertex(self):
        """
        Find the vertex (turning point).
        
        Another specialized method!
        
        Returns:
        --------
        tuple
            (x, y) coordinates of vertex
        """
        # Vertex occurs where derivative = 0
        deriv = self.derivative()
        # For a quadratic, derivative is linear: 2ax + b
        # Setting to 0: 2ax + b = 0, so x = -b/(2a)
        x_vertex = -self.b / (2 * self.a)
        y_vertex = self.evaluate(x_vertex)
        
        return (x_vertex, y_vertex)
    
    def axis_of_symmetry(self) -> float:
        """
        Return the x-coordinate of the axis of symmetry.
        """
        return -self.b / (2 * self.a)
    
    def opens_upward(self) -> bool:
        """
        Check if parabola opens upward.
        
        Returns:
        --------
        bool
            True if a > 0 (opens up), False if a < 0 (opens down)
        """
        return self.a > 0
```

### Testing Quadratic

Let's explore all the features:

```python exec
id: polynomials-5-inheritance-polynomial-classes-part-1-page-1-16
quad = Quadratic(a=1, b=-4, c=3)

print(f"Quadratic: {quad}")
print()

# Specialized methods
print("Specialized Quadratic Methods:")
print(f"Discriminant: {quad.discriminant()}")
print(f"Roots: {quad.find_roots()}")
print(f"Vertex: {quad.vertex()}")
print(f"Axis of symmetry: x = {quad.axis_of_symmetry()}")
print(f"Opens upward? {quad.opens_upward()}")
print()

# Inherited methods
print("Inherited Polynomial Methods:")
print(f"Degree: {quad.degree()}")
print(f"At x=2: {quad.evaluate(2)}")
print(f"Derivative: {quad.derivative()}")
print(f"Integral: {quad.integrate()}")
```

**This is beautiful!** We have:
- Specialized methods that only make sense for quadratics
- All the general polynomial methods
- A clear, intuitive interface

### Connecting Roots and Vertex

```python exec
id: polynomials-5-inheritance-polynomial-classes-part-1-page-1-17
quad = Quadratic(a=1, b=-4, c=3)

roots = quad.find_roots()
print(f"Roots: {roots}")

# Average of roots
avg_roots = (roots[0] + roots[1]) / 2
print(f"Average of roots: {avg_roots}")

# Vertex
vertex_x, vertex_y = quad.vertex()
print(f"Vertex x-coordinate: {vertex_x}")

print(f"\nAre they equal? {abs(avg_roots - vertex_x) < 1e-10}")
```

### Arithmetic with Quadratics

```python exec
id: polynomials-5-inheritance-polynomial-classes-part-1-page-1-18
q1 = Quadratic(a=1, b=0, c=-1)  # x² - 1
q2 = Quadratic(a=1, b=0, c=1)   # x² + 1

# Add them
sum_q = q1 + q2
print(f"({q1}) + ({q2}) = {sum_q}")

# Multiply them
product = q1 * q2
print(f"\n({q1}) * ({q2}) = {product}")
print(f"Degree: {product.degree()}")
# Degree 4! (Quartic)
```

## Looking back

Before leaving this page, a sentence on each. What you write stays on this device.

```reflect
- Something you expected before running a cell that turned out differently
- The one idea from this page you could explain to someone else now
- A question this page raised that it did not answer
```
