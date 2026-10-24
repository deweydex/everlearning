---
title: "Tutorial 1: Linear and Constant Functions - Our First Classes (3 of 3)"
slug: polynomials-1-constants-lines-page-3
course: programming-and-design-principles
series: oop-polynomials
series_title: "Object-Oriented Programming: A Worked Project"
version: 2026.09.07.1
---

*Page 3 of 3.*

*Before starting this page, run the cell below. It repeats the setup from the earlier pages that this page uses.*

```python exec
id: polynomials-1-constants-lines-page-3-setup
# From an earlier page of this tutorial: needed again here.
import numpy as np
import matplotlib.pyplot as plt

# From an earlier page of this tutorial: needed again here.
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

# From an earlier page of this tutorial: needed again here.
# Create some constant functions
f1 = Constant(5)
f2 = Constant(-3)
f3 = Constant(0)

print(f"f1 has value: {f1.c}")
print(f"f2 has value: {f2.c}")
print(f"f3 has value: {f3.c}")

# From an earlier page of this tutorial: needed again here.
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

# From an earlier page of this tutorial: needed again here.
f = Constant(7)

# Try different x values - should always get 7
print(f"f(0) = {f.evaluate(0)}")
print(f"f(5) = {f.evaluate(5)}")
print(f"f(100) = {f.evaluate(100)}")
print(f"f(-42) = {f.evaluate(-42)}")

# They're all the same!

# From an earlier page of this tutorial: needed again here.
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

# From an earlier page of this tutorial: needed again here.
f1 = Constant(5)
f2 = Constant(-3.5)
f3 = Constant(0)

print(f"f1: {f1}")
print(f"f2: {f2}")
print(f"f3: {f3}")

# From an earlier page of this tutorial: needed again here.
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

# From an earlier page of this tutorial: needed again here.
f1 = Constant(5)
f1.plot()

# From an earlier page of this tutorial: needed again here.
f2 = Constant(-3)
f2.plot()

# From an earlier page of this tutorial: needed again here.
f3 = Constant(0)
f3.plot()

# From an earlier page of this tutorial: needed again here.
f = Constant(3)

print("With step = 2 (very coarse):")
f.plot(x_min=-5, x_max=5, step=2)

# From an earlier page of this tutorial: needed again here.
print("With step = 0.1 (default):")
f.plot(x_min=-5, x_max=5, step=0.1)

# From an earlier page of this tutorial: needed again here.
print("With step = 0.01 (very fine):")
f.plot(x_min=-5, x_max=5, step=0.01)

# From an earlier page of this tutorial: needed again here.
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

# From an earlier page of this tutorial: needed again here.
f = Constant(5)
print(f"Function: {f}")

f_prime = f.derivative()
print(f"Derivative: {f_prime}")

# We can take the derivative again!
f_double_prime = f_prime.derivative()
print(f"Second derivative: {f_double_prime}")

# And again...
print(f"Third derivative: {f_double_prime.derivative()}")

# From an earlier page of this tutorial: needed again here.
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

# From an earlier page of this tutorial: needed again here.
f1 = Constant(5)
print(f"{f1}: {f1.find_root()}")

f2 = Constant(0)
print(f"{f2}: {f2.find_root()}")

f3 = Constant(-3.7)
print(f"{f3}: {f3.find_root()}")

# From an earlier page of this tutorial: needed again here.
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

# From an earlier page of this tutorial: needed again here.
class Linear:
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
        self.m = m
        self.b = b

# From an earlier page of this tutorial: needed again here.
line1 = Linear(m=2, b=3)    # f(x) = 2x + 3
line2 = Linear(m=-1, b=0)   # f(x) = -x
line3 = Linear(m=0, b=5)    # f(x) = 5 (wait, this is a constant!)

print(f"line1: slope={line1.m}, y-intercept={line1.b}")
print(f"line2: slope={line2.m}, y-intercept={line2.b}")
print(f"line3: slope={line3.m}, y-intercept={line3.b}")

# From an earlier page of this tutorial: needed again here.
class Linear:
    def __init__(self, m: float, b: float):
        self.m = m
        self.b = b
    
    def evaluate(self, x: float) -> float:
        """
        Evaluate the linear function at x.
        
        Parameters:
        -----------
        x : float
            The input value
            
        Returns:
        --------
        float
            The value mx + b
        """
        # YOUR CODE HERE
        pass

# From an earlier page of this tutorial: needed again here.
line = Linear(m=2, b=3)
print(f"f(0) = {line.evaluate(0)}")   # Should be 3
print(f"f(1) = {line.evaluate(1)}")   # Should be 5
print(f"f(5) = {line.evaluate(5)}")   # Should be 13
print(f"f(-1) = {line.evaluate(-1)}") # Should be 1

# From an earlier page of this tutorial: needed again here.
class Linear:
    def __init__(self, m: float, b: float):
        self.m = m
        self.b = b
    
    def evaluate(self, x: float) -> float:
        """Evaluate the linear function at x."""
        return self.m * x + self.b

# From an earlier page of this tutorial: needed again here.
class Linear:
    def __init__(self, m: float, b: float):
        self.m = m
        self.b = b
    
    def evaluate(self, x: float) -> float:
        return self.m * x + self.b
    
    def __str__(self) -> str:
        """
        Return a readable string representation of the function.
        
        Returns:
        --------
        str
            String representation like "2x + 3" or "-x + 1"
        """
        # YOUR CODE HERE
        pass

# From an earlier page of this tutorial: needed again here.
line1 = Linear(m=2, b=3)
print(f"line1: {line1}")  # Should print something like "2x + 3"

line2 = Linear(m=-1, b=1)
print(f"line2: {line2}")  # Should print something like "-1x + 1"

line3 = Linear(m=3, b=0)
print(f"line3: {line3}")  # Should print something like "3x + 0"

# From an earlier page of this tutorial: needed again here.
class Linear:
    def __init__(self, m: float, b: float):
        self.m = m
        self.b = b
    
    def evaluate(self, x: float) -> float:
        return self.m * x + self.b
    
    def __str__(self) -> str:
        """Return a readable string representation."""
        return f"{self.m}x + {self.b}"

# From an earlier page of this tutorial: needed again here.
class Linear:
    def __init__(self, m: float, b: float):
        self.m = m
        self.b = b
    
    def evaluate(self, x: float) -> float:
        return self.m * x + self.b
    
    def __str__(self) -> str:
        return f"{self.m}x + {self.b}"
    
    def plot(self, x_min: float = -10, x_max: float = 10, step: float = 0.1):
        """
        Plot the linear function.
        
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
line1 = Linear(m=2, b=3)
line1.plot()

# From an earlier page of this tutorial: needed again here.
line2 = Linear(m=-1, b=5)
line2.plot()

# From an earlier page of this tutorial: needed again here.
line3 = Linear(m=0, b=2)
line3.plot()  # What do you notice about this one?

# From an earlier page of this tutorial: needed again here.
class Linear:
    def __init__(self, m: float, b: float):
        self.m = m
        self.b = b
    
    def evaluate(self, x: float) -> float:
        return self.m * x + self.b
    
    def __str__(self) -> str:
        return f"{self.m}x + {self.b}"
    
    def plot(self, x_min: float = -10, x_max: float = 10, step: float = 0.1):
        """Plot the linear function."""
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
line = Linear(m=2, b=1)

print("With step = 2:")
line.plot(x_min=-5, x_max=5, step=2)

# From an earlier page of this tutorial: needed again here.
print("With step = 0.5:")
line.plot(x_min=-5, x_max=5, step=0.5)

# From an earlier page of this tutorial: needed again here.
print("With step = 0.1:")
line.plot(x_min=-5, x_max=5, step=0.1)

# From an earlier page of this tutorial: needed again here.
class Linear:
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
        """
        Return the derivative of this linear function.
        
        The derivative of mx + b is m (a constant).
        
        Returns:
        --------
        Constant
            A new Constant object representing the slope m
        """
        return Constant(self.m)

# From an earlier page of this tutorial: needed again here.
line = Linear(m=2, b=3)
print(f"Function: {line}")

line_deriv = line.derivative()
print(f"Derivative: {line_deriv}")
print(f"Type of derivative: {type(line_deriv).__name__}")

# The derivative is a Constant, so we can evaluate it
print(f"\nDerivative at x=0: {line_deriv.evaluate(0)}")
print(f"Derivative at x=100: {line_deriv.evaluate(100)}")
# Same everywhere - it's constant!

# We can take the derivative again!
second_deriv = line_deriv.derivative()
print(f"\nSecond derivative: {second_deriv}")

# From an earlier page of this tutorial: needed again here.
class Linear:
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
        """
        Find where the linear function equals zero.
        
        Returns:
        --------
        float or str
            The x value where f(x) = 0, or a message if no unique root exists
        """
        if self.m == 0:
            # It's actually a constant function
            if self.b == 0:
                return "All x values are roots (function is always zero)"
            else:
                return "No roots (function never equals zero)"
        else:
            # Standard case: x = -b/m
            return -self.b / self.m

# From an earlier page of this tutorial: needed again here.
line1 = Linear(m=2, b=-6)
print(f"{line1}: root at x = {line1.find_root()}")
# Check: 2(3) + (-6) = 0 ✓

line2 = Linear(m=-1, b=5)
print(f"{line2}: root at x = {line2.find_root()}")
# Check: -(5) + 5 = 0 ✓

# Edge cases
line3 = Linear(m=0, b=5)
print(f"{line3}: {line3.find_root()}")

line4 = Linear(m=0, b=0)
print(f"{line4}: {line4.find_root()}")

# From an earlier page of this tutorial: needed again here.
line = Linear(m=2, b=-6)
print(f"Root at x = {line.find_root()}")
line.plot()
# Look at where the line crosses the x-axis!
```

---

## Complete Linear Class

Here's our complete `Linear` class:

```python exec
id: polynomials-1-constants-lines-page-3-1
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
        """Create a linear function f(x) = mx + b"""
        self.m = m
        self.b = b
    
    def evaluate(self, x: float) -> float:
        """Evaluate the linear function at x."""
        return self.m * x + self.b
    
    def __str__(self) -> str:
        """Return a readable string representation."""
        return f"{self.m}x + {self.b}"
    
    def plot(self, x_min: float = -10, x_max: float = 10, step: float = 0.1):
        """Plot the linear function."""
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
        """Return the derivative (the slope m, as a Constant)."""
        return Constant(self.m)
    
    def find_root(self):
        """Find where the linear function equals zero."""
        if self.m == 0:
            if self.b == 0:
                return "All x values are roots (function is always zero)"
            else:
                return "No roots (function never equals zero)"
        else:
            return -self.b / self.m
```

---

## Part C: Noticing Patterns

Now that we have both `Constant` and `Linear`, let's see what they have in common!

### Same method names

```python exec
id: polynomials-1-constants-lines-page-3-2
const = Constant(5)
line = Linear(m=2, b=3)

# Both have evaluate()
print(f"const.evaluate(2) = {const.evaluate(2)}")
print(f"line.evaluate(2) = {line.evaluate(2)}")

# Both have __str__()
print(f"\nconst: {const}")
print(f"line: {line}")

# Both have derivative()
print(f"\nconst.derivative(): {const.derivative()}")
print(f"line.derivative(): {line.derivative()}")

# Both have find_root()
print(f"\nconst.find_root(): {const.find_root()}")
print(f"line.find_root(): {line.find_root()}")
```

**Why is this useful?** We can write code that works with **either** class!

### Working with multiple functions at once

```python exec
id: polynomials-1-constants-lines-page-3-3
# Create a list of different functions
functions = [
    Constant(3),
    Linear(m=1, b=0),
    Constant(-2),
    Linear(m=-0.5, b=4)
]

# We can loop through and do the same operations on all of them!
for f in functions:
    print(f"Function: {f}")
    print(f"  At x=2: {f.evaluate(2)}")
    print(f"  Derivative: {f.derivative()}")
    print(f"  Root: {f.find_root()}")
    print()
```

This is a preview of **polymorphism** - different classes with the same interface!

### Methods that return instances

Notice something interesting:

```python exec
id: polynomials-1-constants-lines-page-3-4
line = Linear(m=2, b=3)
print(f"Original function: {line}")
print(f"Type: {type(line).__name__}")

deriv = line.derivative()
print(f"\nDerivative: {deriv}")
print(f"Type: {type(deriv).__name__}")  # It's a Constant!

# We can call methods on the derivative
second_deriv = deriv.derivative()
print(f"\nSecond derivative: {second_deriv}")
print(f"Type: {type(second_deriv).__name__}")  # Also a Constant!
```

**This is powerful!** Methods can return new objects that we can keep working with.

### The derivative chain

Let's trace what happens when we take derivatives:

```python exec
id: polynomials-1-constants-lines-page-3-5
# Start with a linear function
f = Linear(m=5, b=2)
print(f"f(x) = {f}")

# First derivative (returns Constant)
f_prime = f.derivative()
print(f"f'(x) = {f_prime}")

# Second derivative (Constant.derivative() returns Constant(0))
f_double_prime = f_prime.derivative()
print(f"f''(x) = {f_double_prime}")

# Third derivative (still 0)
f_triple_prime = f_double_prime.derivative()
print(f"f'''(x) = {f_triple_prime}")
```

**Pattern:**
```
Linear → Constant → Constant(0) → Constant(0) → ...
```

### Edge cases connect the classes

What happens when `Linear` has `m = 0`?

```python exec
id: polynomials-1-constants-lines-page-3-6
almost_constant = Linear(m=0, b=7)
print(f"Function: {almost_constant}")

# Evaluate it
print(f"\nAt x=0: {almost_constant.evaluate(0)}")
print(f"At x=100: {almost_constant.evaluate(100)}")
print(f"At x=-50: {almost_constant.evaluate(-50)}")
# Always 7!

# Plot it
almost_constant.plot()
# It's a horizontal line - just like a Constant!

# Derivative
deriv = almost_constant.derivative()
print(f"\nDerivative: {deriv}")  # Constant(0)

# Find root
print(f"Root: {almost_constant.find_root()}")
```

**Observation:** A `Linear` with `m=0` behaves exactly like a `Constant`! They're different classes but represent the same mathematical object.

---

## Part D: Problems We Notice

### Problem 1: Code Repetition

Look at the `plot()` method:

**In Constant:**
```python
def plot(self, x_min=-10, x_max=10, step=0.1):
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

**In Linear:**
```python
def plot(self, x_min=-10, x_max=10, step=0.1):
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

**They're identical!** The only reason they both work is that each class has an `evaluate()` method.

If we wanted to change how plots look (different colors, titles, etc.), we'd have to change it in **both** places.

### Problem 2: Integration is Blocked

We can take derivatives:

```python exec
id: polynomials-1-constants-lines-page-3-7
line = Linear(m=2, b=3)
print(f"Function: {line}")
print(f"Derivative: {line.derivative()}")  # Works! Returns Constant

const = Constant(5)
print(f"\nFunction: {const}")
print(f"Derivative: {const.derivative()}")  # Works! Returns Constant(0)
```

But what about **integrals**?

The integral of `mx + b` is:
```
∫(mx + b)dx = (m/2)x² + bx + C
```

This is a **quadratic function**! But we don't have a `Quadratic` class yet, so we can't write an `integrate()` method.

Similarly, the integral of constant `c` is:
```
∫c dx = cx + C
```

This is a **linear function**. We could actually implement `Constant.integrate()` since we have `Linear`:

```python exec
id: polynomials-1-constants-lines-page-3-8
# Let's add integrate() to Constant
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

**Let's test it:**

```python exec
id: polynomials-1-constants-lines-page-3-9
const = Constant(5)
print(f"Function: {const}")

integral = const.integrate(C=0)
print(f"Integral: {integral}")
# Should be 5x + 0

# Verify by taking derivative
check = integral.derivative()
print(f"Derivative of integral: {check}")
# Should get back Constant(5)!
```

But we still can't integrate `Linear` functions until we have `Quadratic`!

### Problem 3: The Pattern is Clear but Unsustainable

Let's think about derivatives:

```
Linear(m, b) → Constant(m) → Constant(0) → Constant(0) → ...
```

And integrals (if we had all the classes):

```
Constant(c) → Linear(c, 0) → Quadratic(...) → Cubic(...) → ...
```

**Going down** (derivatives) works fine - we eventually reach zero.

**Going up** (integrals) needs infinite classes - Quadratic, Cubic, Quartic, Quintic, Sextic, ...

Do we really want to create a new class for every polynomial degree?

---

## Reflections and Looking Ahead

### What We've Accomplished

We've built two classes that:
- Store mathematical function data (`c` for Constant, `m` and `b` for Linear)
- Provide methods to work with them (evaluate, plot, derivative, find_root)
- Can be used in similar ways (same method names)
- Return instances of each other (derivatives connect them)

### What We've Discovered

1. **Common structure**: Both classes have very similar methods
2. **Polymorphism**: We can treat different classes similarly
3. **Classes returning classes**: Methods can create new objects
4. **Code duplication**: Some methods are identical
5. **Blocked operations**: We can't integrate because we need more classes
6. **Edge cases**: `Linear(m=0, b)` is really a `Constant`

### Questions to Think About

1. **Can we reduce code duplication?** The `plot()` method is identical in both classes.

2. **How do we handle integration?** We need `Quadratic`, `Cubic`, ... forever?

3. **Are separate classes the best approach?** Or is there a more general way to represent any polynomial?

4. **What about the edge cases?** Should `Linear(m=0, b=7)` just create a `Constant(7)`?

---

## Exercises

### Your turn 1: Exploring Derivatives

```python exec
id: polynomials-1-constants-lines-page-3-10
# Create f(x) = 3x + 7
# Find f'(x), f''(x), f'''(x)
# What pattern do you notice?

# YOUR CODE HERE
```

### Your turn 2: Finding Roots Graphically

```python exec
id: polynomials-1-constants-lines-page-3-11
# Create several linear functions
# Use find_root() to find where they cross the x-axis
# Plot each one to verify visually

# YOUR CODE HERE
```

### Your turn 3: The step Parameter

```python exec
id: polynomials-1-constants-lines-page-3-12
# Create a linear function
# Plot it with step = 5, step = 1, step = 0.1, step = 0.01
# What's the minimum step needed to make it look smooth?
# How does this relate to the slope?

# YOUR CODE HERE
```

### Your turn 4: Working with Collections

```python exec
id: polynomials-1-constants-lines-page-3-13
# Create a list with 5 different functions (mix of Constant and Linear)
# For each function:
#   - Print it
#   - Evaluate it at x = 3
#   - Find its derivative
#   - Find its root (if it has one)

# YOUR CODE HERE
```

### Your turn 5: Integration

```python exec
id: polynomials-1-constants-lines-page-3-14
# Create const = Constant(4)
# Find its integral (should be Linear)
# Take the derivative of the integral
# Do you get back the original function?

# Try with different constants and different values of C

# YOUR CODE HERE
```

### Your turn 6: Composition

```python exec
id: polynomials-1-constants-lines-page-3-15
# Create f = Linear(m=2, b=1)  # f(x) = 2x + 1
# Create g = Constant(5)        # g(x) = 5

# Compute f(g(x)) - what do you get?
# Compute g(f(x)) - what do you get?
# Are they the same?

# YOUR CODE HERE
```

---

## Next Time

In **Tutorial 2**, we'll add the `Quadratic` class to represent parabolas. We'll discover:

- How derivatives work for quadratics (they return Linear!)
- Special properties of quadratics (vertex, discriminant)
- More about where derivatives equal zero
- Why the pattern of separate classes becomes unsustainable

The problems we noticed today will become even more pressing, pushing us toward a better solution.

---

**End of Tutorial 1**

## Looking back

Before leaving this page, a sentence on each. What you write stays on this device.

```reflect
- Something you expected before running a cell that turned out differently
- The one idea from this page you could explain to someone else now
- A question this page raised that it did not answer
```
