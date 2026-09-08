---
title: "Tutorial 1: Linear and Constant Functions - Our First Classes (2 of 3)"
slug: polynomials-1-constants-lines-page-2
course: programming-and-design-principles
series: oop-polynomials
series_title: "Object-Oriented Programming: A Worked Project"
version: 2026.09.07.1
---

*Page 2 of 3.*

*Before starting this page, run the cell below. It repeats the setup from the earlier pages that this page uses.*

```python exec
id: polynomials-1-constants-lines-page-2-setup
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
```

---

## Part B: The Linear Function

### What is a linear function?

A **linear function** has the form:

```
f(x) = mx + b
```

Where:
- `m` is the **slope** (how steep the line is)
- `b` is the **y-intercept** (where the line crosses the y-axis)

For example:
- `f(x) = 2x + 3` has slope 2 and y-intercept 3
- `f(x) = -x + 1` has slope -1 and y-intercept 1
- `f(x) = 3x` has slope 3 and y-intercept 0

When we graph a linear function, we get a **straight line** (not horizontal unless `m = 0`).

---

### Building the Linear Class - Basic Structure

```python exec
id: polynomials-1-constants-lines-page-2-1
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
```

**Let's test it:**

```python exec
id: polynomials-1-constants-lines-page-2-2
line1 = Linear(m=2, b=3)    # f(x) = 2x + 3
line2 = Linear(m=-1, b=0)   # f(x) = -x
line3 = Linear(m=0, b=5)    # f(x) = 5 (wait, this is a constant!)

print(f"line1: slope={line1.m}, y-intercept={line1.b}")
print(f"line2: slope={line2.m}, y-intercept={line2.b}")
print(f"line3: slope={line3.m}, y-intercept={line3.b}")
```

---

### YOUR TURN: Implement evaluate()

Based on what we did for `Constant`, implement the `evaluate()` method for `Linear`.

**Hints:**
- For a linear function `f(x) = mx + b`, what is `f(x)` at a given `x`?
- You have access to `self.m` and `self.b`

```python exec
id: polynomials-1-constants-lines-page-2-3
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
```

**Test your implementation:**

```python exec
id: polynomials-1-constants-lines-page-2-4
line = Linear(m=2, b=3)
print(f"f(0) = {line.evaluate(0)}")   # Should be 3
print(f"f(1) = {line.evaluate(1)}")   # Should be 5
print(f"f(5) = {line.evaluate(5)}")   # Should be 13
print(f"f(-1) = {line.evaluate(-1)}") # Should be 1
```

<details>
<summary>Click to see solution</summary>

```python
def evaluate(self, x: float) -> float:
 """Evaluate the linear function at x."""
 return self.m * x + self.b
```

</details>

**Solution:**

```python exec
id: polynomials-1-constants-lines-page-2-5
class Linear:
    def __init__(self, m: float, b: float):
        self.m = m
        self.b = b
    
    def evaluate(self, x: float) -> float:
        """Evaluate the linear function at x."""
        return self.m * x + self.b
```

---

### YOUR TURN: Implement __str__()

Implement the `__str__()` method to return a readable representation like `"2x + 3"` or `"-x + 1"`.

```python exec
id: polynomials-1-constants-lines-page-2-6
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
```

**Test your implementation:**

```python exec
id: polynomials-1-constants-lines-page-2-7
line1 = Linear(m=2, b=3)
print(f"line1: {line1}")  # Should print something like "2x + 3"

line2 = Linear(m=-1, b=1)
print(f"line2: {line2}")  # Should print something like "-1x + 1"

line3 = Linear(m=3, b=0)
print(f"line3: {line3}")  # Should print something like "3x + 0"
```

**Solution:**

```python exec
id: polynomials-1-constants-lines-page-2-8
class Linear:
    def __init__(self, m: float, b: float):
        self.m = m
        self.b = b
    
    def evaluate(self, x: float) -> float:
        return self.m * x + self.b
    
    def __str__(self) -> str:
        """Return a readable string representation."""
        return f"{self.m}x + {self.b}"
```

Note: We could make this fancier (e.g., showing "-x" instead of "-1x", or "3x" instead of "3x + 0"), but this simple version works fine!

---

### YOUR TURN: Implement plot()

Following the **exact same pattern** as `Constant.plot()`, implement the `plot()` method for `Linear`.

**Hints:**
- The structure should be identical to `Constant.plot()`
- The only difference is that you'll call `self.evaluate()` which now does something different

```python exec
id: polynomials-1-constants-lines-page-2-9
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
```

**Test your implementation:**

```python exec
id: polynomials-1-constants-lines-page-2-10
line1 = Linear(m=2, b=3)
line1.plot()
```

```python exec
id: polynomials-1-constants-lines-page-2-11
line2 = Linear(m=-1, b=5)
line2.plot()
```

```python exec
id: polynomials-1-constants-lines-page-2-12
line3 = Linear(m=0, b=2)
line3.plot()  # What do you notice about this one?
```

**Solution:**

```python exec
id: polynomials-1-constants-lines-page-2-13
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
```

---

### Exploring step with Linear functions

Now that we have lines instead of constants, the `step` parameter matters more:

```python exec
id: polynomials-1-constants-lines-page-2-14
line = Linear(m=2, b=1)

print("With step = 2:")
line.plot(x_min=-5, x_max=5, step=2)
```

```python exec
id: polynomials-1-constants-lines-page-2-15
print("With step = 0.5:")
line.plot(x_min=-5, x_max=5, step=0.5)
```

```python exec
id: polynomials-1-constants-lines-page-2-16
print("With step = 0.1:")
line.plot(x_min=-5, x_max=5, step=0.1)
```

**Questions to think about:**
1. Can you see the individual points when `step = 2`?
2. Do they still look like straight lines?
3. For a linear function, how many points do we *actually* need to draw a line?
4. Why might we still want many points?

---

### Adding the derivative() method

The derivative of a linear function `f(x) = mx + b` is:

```
f'(x) = m
```

The slope `m` is the rate of change - it's **constant**! No matter where you are on the line, it's rising (or falling) at the same rate.

Notice: The derivative is a `Constant` object!

```python exec
id: polynomials-1-constants-lines-page-2-17
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
```

**Let's test it:**

```python exec
id: polynomials-1-constants-lines-page-2-18
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
```

---

### Adding the find_root() method

A **root** is where `f(x) = 0`. For `f(x) = mx + b`:

```
mx + b = 0
mx = -b
x = -b/m
```

But wait - what if `m = 0`? Then we don't really have a linear function, we have a constant function!
- If `m = 0` and `b = 0`: every x is a root
- If `m = 0` and `b ≠ 0`: no roots

```python exec
id: polynomials-1-constants-lines-page-2-19
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
```

**Let's test it:**

```python exec
id: polynomials-1-constants-lines-page-2-20
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
```

**Verification by plotting:**

```python exec
id: polynomials-1-constants-lines-page-2-21
line = Linear(m=2, b=-6)
print(f"Root at x = {line.find_root()}")
line.plot()
# Look at where the line crosses the x-axis!
```

## Looking back

Before leaving this page, a sentence on each. What you write stays on this device.

```reflect
- Something you expected before running a cell that turned out differently
- The one idea from this page you could explain to someone else now
- A question this page raised that it did not answer
```
