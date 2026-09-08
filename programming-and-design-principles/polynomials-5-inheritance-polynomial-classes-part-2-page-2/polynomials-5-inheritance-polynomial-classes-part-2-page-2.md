---
title: "Tutorial 5 Part 2: Polymorphism and Design Principles (2 of 2)"
slug: polynomials-5-inheritance-polynomial-classes-part-2-page-2
course: programming-and-design-principles
series: oop-polynomials
series_title: "Object-Oriented Programming: A Worked Project"
version: 2026.09.07.1
---

*Page 2 of 2.*

*Before starting this page, run the cell below. It repeats the setup from the earlier pages that this page uses.*

```python exec
id: polynomials-5-inheritance-polynomial-classes-part-2-page-2-setup
# From an earlier page of this tutorial: needed again here.
import numpy as np
import matplotlib.pyplot as plt

# From an earlier page of this tutorial: needed again here.
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

# From an earlier page of this tutorial: needed again here.
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

# From an earlier page of this tutorial: needed again here.
# Works with all types!
analyze_function(Linear(m=2, b=3))
analyze_function(Quadratic(a=1, b=-4, c=3))
analyze_function(Polynomial([1, 0, -1, 0, 1]))

# From an earlier page of this tutorial: needed again here.
def find_all_derivatives(functions):
    """
    Take derivatives of a list of functions.
    
    Doesn't care what type they are!
    """
    derivatives = []
    for f in functions:
        derivatives.append(f.derivative())
    return derivatives

# From an earlier page of this tutorial: needed again here.
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

# From an earlier page of this tutorial: needed again here.
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

# From an earlier page of this tutorial: needed again here.
functions = [
    Linear(m=1, b=0),           # y = x
    Quadratic(a=1, b=0, c=0),   # y = x²
    Polynomial([0, 0, 0, 1])    # y = x³
]

plot_together(functions, x_min=-2, x_max=2)

# From an earlier page of this tutorial: needed again here.
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

# From an earlier page of this tutorial: needed again here.
# With a Polynomial
compute_change(Polynomial([1, 2, 3]), 0, 2)
print()

# With a Linear (substituted for Polynomial!)
compute_change(Linear(m=2, b=1), 0, 2)
print()

# With a Quadratic (substituted for Polynomial!)
compute_change(Quadratic(a=1, b=0, c=-1), 0, 2)
```

**It works perfectly!** We can substitute child classes for the parent.

### When LSP is Violated

LSP would be **violated** if:
- Child classes removed or changed essential methods
- Child classes threw errors where parent didn't
- Child classes had completely different behavior

**Bad example (don't do this!):**
```python
class BadLinear(Polynomial):
 def evaluate(self, x):
 raise NotImplementedError("Can't evaluate!")
```

This breaks LSP because code expecting `Polynomial.evaluate()` to work would fail!

**Our implementation is good** because:
- `Linear` and `Quadratic` keep all `Polynomial` methods
- They add new methods (which is fine)
- They override `__str__()` but still return a string (behavior preserved)

---

## Part C: Design Patterns That Emerge

### Pattern 1: Template Method

The parent class provides the **template** (general algorithm), and children fill in details.

Example: Our `plot()` method in `Polynomial` is a template:
```python
def plot(self, ...):
 x_values = np.arange(...)
 y_values = [self.evaluate(x) for x in x_values] # Calls child's evaluate()!
 # ... plotting code ...
```

The child classes don't need to override `plot()` because they inherit it, but if they have different `evaluate()` behavior, it automatically works!

### Pattern 2: Strategy Pattern

Different classes represent different "strategies" for the same task.

Example: Finding roots
- `Linear.find_root()` uses exact formula
- `Quadratic.find_roots()` uses quadratic formula
- `Polynomial` could use Newton's method (numerical)

Each is a different **strategy** for finding roots.

### Pattern 3: Specialization Hierarchy

More specific classes extend more general ones:

```
Polynomial (most general)
 ├── Linear (degree ≤ 1)
 └── Quadratic (degree ≤ 2)
```

We could extend this:

```
Polynomial
 ├── Constant (degree 0)
 ├── Linear (degree ≤ 1)
 │ └── Proportional (degree ≤ 1, b=0)
 ├── Quadratic (degree ≤ 2)
 ├── Cubic (degree ≤ 3)
 └── ...
```

Each level adds more specialization.

---

## Part D: When to Use Inheritance

### Good Reasons to Use Inheritance

Use inheritance when:

1. **"Is-A" relationship**: Child truly **is a** type of parent
 - `Linear` is a `Polynomial` 
 - `Square` is a `Rectangle` 
 - `Dog` is an `Animal` 

2. **Shared behavior**: Multiple classes need the same methods
 - All polynomials need `evaluate()`, `derivative()` 

3. **Specialization**: Child adds specific features to general parent
 - `Quadratic` adds `vertex()` to `Polynomial` 

4. **Polymorphism needed**: You want to treat different types uniformly
 - We want all polynomials to work with `plot_together()` 

### When NOT to Use Inheritance

**Don't use inheritance when:**

1. **"Has-A" relationship**: One class contains another
 - Bad: `Car` inherits from `Engine`
 - Good: `Car` has an `Engine` as an attribute

2. **Unrelated classes**: Just happen to share some methods
 - Bad: `File` and `Database` both have `open()`, so inherit from common parent
 - Good: Keep them separate, they're unrelated concepts

3. **Implementation reuse only**: Just want to reuse code, no conceptual relationship
 - Use composition or functions instead

4. **Deep hierarchies**: More than 2-3 levels gets confusing
 - Polynomial → Linear → Proportional is probably deep enough

### Alternatives to Inheritance

**Composition** ("has-a"):
```python
class Car:
 def __init__(self):
 self.engine = Engine() # Car HAS an Engine
 self.wheels = [Wheel(), Wheel(), Wheel(), Wheel()]
```

**Duck typing** (just implement the interface):
```python
# Don't need inheritance if classes just implement same methods
class TextFile:
 def read(self): ...

class Database:
 def read(self): ...

# Both can be used anywhere read() is called
```

---

## Part E: Real-World Applications Beyond Polynomials

### Example 1: Shapes

```python
class Shape:
 def area(self):
 raise NotImplementedError
 
 def perimeter(self):
 raise NotImplementedError

class Circle(Shape):
 def __init__(self, radius):
 self.radius = radius
 
 def area(self):
 return 3.14159 * self.radius ** 2
 
 def perimeter(self):
 return 2 * 3.14159 * self.radius

class Rectangle(Shape):
 def __init__(self, width, height):
 self.width = width
 self.height = height
 
 def area(self):
 return self.width * self.height
 
 def perimeter(self):
 return 2 * (self.width + self.height)

# Can treat all shapes uniformly
def total_area(shapes):
 return sum(s.area() for s in shapes)
```

### Example 2: File Formats

```python
class DataFile:
 def read(self):
 raise NotImplementedError
 
 def write(self, data):
 raise NotImplementedError

class CSVFile(DataFile):
 def read(self):
 # CSV-specific reading
 pass
 
 def write(self, data):
 # CSV-specific writing
 pass

class JSONFile(DataFile):
 def read(self):
 # JSON-specific reading
 pass
 
 def write(self, data):
 # JSON-specific writing
 pass

# Code that works with any file format
def process_file(file):
 data = file.read()
 # ... process ...
 file.write(processed_data)
```

### Example 3: Machine Learning Models

```python
class Model:
 def fit(self, X, y):
 raise NotImplementedError
 
 def predict(self, X):
 raise NotImplementedError
 
 def score(self, X, y):
 predictions = self.predict(X)
 return accuracy(predictions, y)

class LinearRegression(Model):
 def fit(self, X, y):
 # Find best-fit line
 pass
 
 def predict(self, X):
 # Linear prediction
 pass

class NeuralNetwork(Model):
 def fit(self, X, y):
 # Train neural network
 pass
 
 def predict(self, X):
 # Neural network prediction
 pass

# Can evaluate any model the same way
def compare_models(models, X_test, y_test):
 for model in models:
 score = model.score(X_test, y_test)
 print(f"{type(model).__name__}: {score}")
```

---

## Part F: Advanced Concepts

### Multiple Inheritance

Python allows a class to inherit from multiple parents:

```python
class A:
 def method_a(self):
 print("From A")

class B:
 def method_b(self):
 print("From B")

class C(A, B): # Inherits from both A and B!
 pass

c = C()
c.method_a() # Works!
c.method_b() # Works!
```

**Use sparingly** - can get confusing!

### Abstract Base Classes

Sometimes we want a parent class that **must** be inherited, never used directly:

```python
from abc import ABC, abstractmethod

class Shape(ABC):
 @abstractmethod
 def area(self):
 pass # Children MUST implement this

# Can't create a Shape directly:
# s = Shape() # ERROR!

# But can create children:
class Circle(Shape):
 def area(self):
 return 3.14159 * self.radius ** 2
```

This enforces that children implement required methods.

---

## Exercises

### Your turn 1: Understanding Polymorphism

```python exec
id: polynomials-5-inheritance-polynomial-classes-part-2-page-2-1
# Write a function that takes a list of polynomials
# and returns a list of their second derivatives
# Test it with a mix of Linear, Quadratic, and Polynomial objects

# YOUR CODE HERE
```

### Your turn 2: Testing LSP

```python exec
id: polynomials-5-inheritance-polynomial-classes-part-2-page-2-2
# Write a function that expects a Polynomial
# It should:
# - Evaluate the function at 3 points
# - Take the derivative
# - Evaluate the derivative at the same 3 points
#
# Test that it works when you pass:
# - A Polynomial
# - A Linear
# - A Quadratic
#
# This demonstrates LSP!

# YOUR CODE HERE
```

### Your turn 3: Create a Constant Class

```python exec
id: polynomials-5-inheritance-polynomial-classes-part-2-page-2-3
# Create a Constant class that inherits from Polynomial
# It should:
# - Have init(self, c) that takes a single constant value
# - Override str() to just show the constant
# - Maybe add a value() method to get the constant
#
# Test that:
# - It can be created with Constant(5)
# - derivative() works (should return Constant(0))
# - integrate() works (should return Linear)
# - It works in a list with other polynomial types

# YOUR CODE HERE
```

### Your turn 4: Design a New Hierarchy

```python exec
id: polynomials-5-inheritance-polynomial-classes-part-2-page-2-4
# Design (don't fully implement) an inheritance hierarchy for geometric shapes:
# - Base class: Shape
#   - What methods should all shapes have?
# - Child classes: Circle, Rectangle, Triangle
#   - What specific attributes does each need?
#   - What specialized methods make sense?
#
# Write pseudocode or just outline the structure

# YOUR DESIGN HERE
```

### Your turn 5: Inheritance vs. Composition

```python exec
id: polynomials-5-inheritance-polynomial-classes-part-2-page-2-5
# For each scenario, decide: Inheritance or Composition?
#
# 1. A University has Departments
# 2. A SportsCar is a type of Car
# 3. A Computer has a CPU, RAM, and Storage
# 4. A Manager is a type of Employee
# 5. A Book has Pages
# 6. A ElectricCar is a type of Car
#
# For each, explain your reasoning

# YOUR ANSWERS HERE (as comments)
```

---

## Summary: The Journey Complete

### What We've Learned Across All Tutorials

Tutorial 1-2: Simple specific classes
- Easy to use, clear interfaces
- But: code duplication, limited functionality

Tutorial 3: General Polynomial class
- Universal! Works for any degree
- But: lost clarity, lost special methods

Tutorial 4: Polynomial arithmetic
- Powerful operations (+, -, *)
- But: still missing the nice specific interfaces

Tutorial 5: Inheritance
- Everything we wanted!
- Clear interfaces + General power + Specialized methods

### Key Principles Discovered

1. DRY (Don't Repeat Yourself): Inheritance lets us write code once
2. Polymorphism: Different objects, same interface
3. LSP: Children can substitute for parents
4. Specialization: Add specific features to general concepts
5. "Is-A" vs "Has-A": Know when to inherit vs. compose

### Design Wisdom

When designing classes:
1. Start simple - specific classes for specific needs
2. Notice patterns - when code repeats, look for commonality
3. Generalize carefully - create parent classes for shared behavior
4. Specialize thoughtfully - use inheritance when "is-a" makes sense
5. Test substitutability - can children replace parents?

Good inheritance:
- Clear conceptual relationship (is-a)
- Shared behavior (same methods)
- Useful specialization (added value)
- Preserves expectations (LSP)

Bad inheritance:
- Just for code reuse (use composition)
- Forced relationship (unnatural)
- Deep hierarchies (confusing)
- Breaking parent contracts (violates LSP)

### Beyond This Tutorial

You now understand:
- Object-Oriented Programming fundamentals
- Design patterns that emerge naturally
- Trade-offs in software design
- When and why to use different approaches

These principles apply far beyond polynomials:
- Web applications (Model-View-Controller)
- Game development (Entity hierarchies)
- Data science (Model interfaces)
- System design (Plugin architectures)

### Final Thoughts

Good design isn't about following rules - it's about:
- Understanding trade-offs
- Making conscious choices
- Balancing competing concerns
- Letting solutions emerge naturally

We didn't start with "here's inheritance, use it everywhere." We:
1. Built simple solutions
2. Noticed problems
3. Tried different approaches
4. Discovered inheritance as the answer to our specific problems

This is how real software development works!

---


You've learned more than just Python syntax - you've learned how to think about software design, recognize patterns, and make good engineering decisions.

Keep exploring, keep building, keep learning!

## Looking back

Before leaving this page, a sentence on each. What you write stays on this device.

```reflect
- Something you expected before running a cell that turned out differently
- The one idea from this page you could explain to someone else now
- A question this page raised that it did not answer
```
