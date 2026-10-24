---
title: "Tutorial 5 Part 1: Inheritance - Best of Both Worlds (2 of 2)"
slug: polynomials-5-inheritance-polynomial-classes-part-1-page-2
course: programming-and-design-principles
series: oop-polynomials
series_title: "Object-Oriented Programming: A Worked Project"
version: 2026.09.07.1
---

*Page 2 of 2.*

*Before starting this page, run the cell below. It repeats the setup from the earlier pages that this page uses.*

```python exec
id: polynomials-5-inheritance-polynomial-classes-part-1-page-2-setup
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

# From an earlier page of this tutorial: needed again here.
p = Polynomial([3, -4, 1])  # 3 - 4x + x²
print(f"Polynomial: {p}")
print(f"Degree: {p.degree()}")
print(f"At x=2: {p.evaluate(2)}")
print(f"Derivative: {p.derivative()}")

# From an earlier page of this tutorial: needed again here.
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

# From an earlier page of this tutorial: needed again here.
line = Linear(m=2, b=3)
print(f"Created: {line}")
print(f"Slope: {line.m}")
print(f"Y-intercept: {line.b}")
print(f"Coefficients: {line.coeffs}")
print(f"Degree: {line.degree()}")

# From an earlier page of this tutorial: needed again here.
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

# From an earlier page of this tutorial: needed again here.
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

# From an earlier page of this tutorial: needed again here.
line = Linear(m=2, b=3)
print(f"Linear: {line}")  # Uses our new __str__()

# But Polynomial methods still work!
print(f"Derivative: {line.derivative()}")
print(f"Integral: {line.integrate()}")

# From an earlier page of this tutorial: needed again here.
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

# From an earlier page of this tutorial: needed again here.
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

# From an earlier page of this tutorial: needed again here.
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

# From an earlier page of this tutorial: needed again here.
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

# From an earlier page of this tutorial: needed again here.
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

# From an earlier page of this tutorial: needed again here.
quad = Quadratic(a=1, b=-4, c=3)
print(f"Quadratic: {quad}")
print(f"At x=2: {quad.evaluate(2)}")
print(f"Derivative: {quad.derivative()}")
print(f"Integral: {quad.integrate()}")

# From an earlier page of this tutorial: needed again here.
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

# From an earlier page of this tutorial: needed again here.
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

# From an earlier page of this tutorial: needed again here.
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

# From an earlier page of this tutorial: needed again here.
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

---

## Part E: The Power of Polymorphism

Now comes the really cool part. We can treat all our polynomials uniformly!

### Working with Different Types Together

```python exec
id: polynomials-5-inheritance-polynomial-classes-part-1-page-2-1
# Create a mix of different polynomial types
functions = [
    Linear(m=2, b=3),
    Quadratic(a=1, b=-4, c=3),
    Polynomial([1, 0, -1, 0, 1]),  # 1 - x² + x⁴
    Linear(m=-1, b=5),
    Quadratic(a=-1, b=0, c=4)
]

# We can loop through and call the same methods on all of them!
for f in functions:
    print(f"Function: {f}")
    print(f"  Type: {type(f).__name__}")
    print(f"  Degree: {f.degree()}")
    print(f"  At x=2: {f.evaluate(2)}")
    print(f"  Derivative: {f.derivative()}")
    print()
```

**This is polymorphism in action!** Different types, same interface.

### Type-Specific Methods

We can check the type and call specialized methods when available:

```python exec
id: polynomials-5-inheritance-polynomial-classes-part-1-page-2-2
functions = [
    Linear(m=2, b=-6),
    Quadratic(a=1, b=-3, c=2),
    Polynomial([1, 2, 3, 4])
]

for f in functions:
    print(f"Function: {f}")
    
    # Everyone has these
    print(f"  Derivative: {f.derivative()}")
    
    # Only Linear has find_root() method
    if isinstance(f, Linear):
        print(f"  Root: {f.find_root()}")
    
    # Only Quadratic has vertex() method
    if isinstance(f, Quadratic):
        print(f"  Vertex: {f.vertex()}")
        print(f"  Roots: {f.find_roots()}")
    
    print()
```

### Combining Different Types

```python exec
id: polynomials-5-inheritance-polynomial-classes-part-1-page-2-3
line = Linear(m=2, b=1)
quad = Quadratic(a=1, b=0, c=-1)

# Add a linear and a quadratic
result = line + quad
print(f"Linear + Quadratic: {result}")
print(f"Type: {type(result).__name__}")
print(f"Degree: {result.degree()}")

# Multiply them
product = line * quad
print(f"\nLinear * Quadratic: {product}")
print(f"Type: {type(product).__name__}")
print(f"Degree: {product.degree()}")
```

---

## Part F: Understanding the Inheritance Hierarchy

### The "Is-A" Relationship

When we use inheritance, we create an "is-a" relationship:
- A `Linear` **is a** `Polynomial` (specifically, one of degree ≤ 1)
- A `Quadratic` **is a** `Polynomial` (specifically, one of degree ≤ 2)

Let's verify:

```python exec
id: polynomials-5-inheritance-polynomial-classes-part-1-page-2-4
line = Linear(m=2, b=3)
quad = Quadratic(a=1, b=-4, c=3)
poly = Polynomial([1, 2, 3, 4, 5])

print("Is line a Polynomial?", isinstance(line, Polynomial))
print("Is quad a Polynomial?", isinstance(quad, Polynomial))
print("Is poly a Polynomial?", isinstance(poly, Polynomial))
print()

print("Is line a Linear?", isinstance(line, Linear))
print("Is quad a Linear?", isinstance(quad, Linear))
print("Is poly a Linear?", isinstance(poly, Linear))
print()

print("Is line a Quadratic?", isinstance(line, Quadratic))
print("Is quad a Quadratic?", isinstance(quad, Quadratic))
print("Is poly a Quadratic?", isinstance(poly, Quadratic))
```

### Method Resolution Order

When you call a method, Python looks for it in this order:
1. The object's own class (`Linear` or `Quadratic`)
2. The parent class (`Polynomial`)
3. The parent's parent (if any)

Example:

```python exec
id: polynomials-5-inheritance-polynomial-classes-part-1-page-2-5
line = Linear(m=2, b=3)

# When we call line.__str__()
# Python finds it in Linear class (we overrode it)
print(f"String: {line}")

# When we call line.derivative()
# Python doesn't find it in Linear
# So it looks in Polynomial and finds it there!
print(f"Derivative: {line.derivative()}")

# When we call line.slope()
# Python finds it in Linear (it's specialized)
print(f"Slope: {line.slope()}")
```

---

## Part G: What We've Achieved

Let's take stock of what inheritance has given us.

### Before Inheritance (Tutorial 3)

**With general Polynomial class:**
```python
p = Polynomial([3, -4, 1]) # Hard to read
p.derivative() # Works
p.integrate() # Works
p.vertex() # Doesn't exist
```

**With separate specific classes:**
```python
quad = Quadratic(a=1, b=-4, c=3) # Clear
quad.vertex() # Works
quad.integrate() # Can't - need Cubic class
quad + other # No arithmetic
```

### After Inheritance (Now!)

**We get EVERYTHING:**
```python
quad = Quadratic(a=1, b=-4, c=3) # Clear interface
quad.vertex() # Specialized method
quad.discriminant()# Specialized method
quad.find_roots() # Exact formula
quad.derivative() # Inherited - works!
quad.integrate() # Inherited - works!
quad + other # Inherited - works!
quad * other # Inherited - works!
```

### The Best of Both Worlds

| Feature | General Polynomial | Specific Classes (Old) | With Inheritance |
|---------|-------------------|----------------------|------------------|
| Works for any degree | | | |
| Clear, intuitive interface | | | |
| Derivatives work | | | |
| Integrals work | | | |
| Arithmetic (+, -, *) | | | |
| Specialized methods | | | |
| No code duplication | | | |
| Exact formulas | | | |

**We've achieved everything!**

---

## Exercises

### Your turn 1: Using Linear

```python exec
id: polynomials-5-inheritance-polynomial-classes-part-1-page-2-6
# Create line = Linear(m=3, b=-9)
# Find its root
# Take its derivative
# Take its integral
# Verify that derivative(integral) gives you back the original

# YOUR CODE HERE
```

### Your turn 2: Using Quadratic

```python exec
id: polynomials-5-inheritance-polynomial-classes-part-1-page-2-7
# Create quad = Quadratic(a=1, b=-6, c=8)
# Find its roots
# Find its vertex
# Verify that the vertex x-coordinate is the average of the roots
# Take the derivative and find where it equals zero
# Does this match the vertex x-coordinate?

# YOUR CODE HERE
```

### Your turn 3: Mixing Types

```python exec
id: polynomials-5-inheritance-polynomial-classes-part-1-page-2-8
# Create a Linear and a Quadratic
# Add them together - what type is the result?
# Multiply them together - what degree is the result?
# Can you still call specialized methods on the results?

# YOUR CODE HERE
```

### Your turn 4: Derivative Chain

```python exec
id: polynomials-5-inheritance-polynomial-classes-part-1-page-2-9
# Create quad = Quadratic(a=2, b=-8, c=6)
# Take its derivative (should be Linear)
# Take the derivative of that (should be Polynomial)
# Take the derivative again
# What do you notice about the types?

# YOUR CODE HERE
```

### Your turn 5: Build from Roots

```python exec
id: polynomials-5-inheritance-polynomial-classes-part-1-page-2-10
# You want a quadratic with roots at x=2 and x=5
# It factors as (x-2)(x-5)
# Create two Linear objects representing these factors
# Multiply them together
# What coefficients do you get? (Hint: expand (x-2)(x-5) by hand)
# Verify by creating a Quadratic with those coefficients
# Use find_roots() to check you get [2, 5] back

# YOUR CODE HERE
```

---

## Summary and Looking Ahead

### What We've Learned

**Inheritance** lets us:
1. Create specialized classes based on general ones
2. Automatically inherit all parent methods
3. Override methods when needed
4. Add new specialized methods
5. Get the best of both worlds: generality AND specificity

**Key syntax:**
- `class Child(Parent):` to inherit
- `super().__init__(...)` to call parent initialization
- Override methods by defining them again in child
- Add new methods that parent doesn't have

### The Big Picture

We've solved our design problem!

- **Tutorial 1-2**: Specific classes (good interface, lots of problems)
- **Tutorial 3-4**: General class (powerful, but lost specificity)
- **Tutorial 5 Part 1**: Inheritance (everything we wanted!)

### Next: Tutorial 5 Part 2

In **Part 2**, we'll explore:
- **Polymorphism** in depth (treating different objects uniformly)
- **Design principles** (when to use inheritance vs. composition)
- **Real-world examples** (how this applies beyond polynomials)
- **Advanced patterns** (abstract base classes, multiple inheritance)
- **The Liskov Substitution Principle** (in plain language)

---

**End of Tutorial 5 Part 1**

## Looking back

Before leaving this page, a sentence on each. What you write stays on this device.

```reflect
- Something you expected before running a cell that turned out differently
- The one idea from this page you could explain to someone else now
- A question this page raised that it did not answer
```
