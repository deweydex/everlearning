---
title: "Tutorial 2: Quadratic Functions - Patterns Strengthen (3 of 3)"
slug: polynomials-2-quadratics-page-3
course: programming-and-design-principles
series: oop-polynomials
series_title: "Object-Oriented Programming: A Worked Project"
version: 2026.09.07.1
---

*Page 3 of 3.*

*Before starting this page, run the cell below. It repeats the setup from the earlier pages that this page uses.*

```python exec
id: polynomials-2-quadratics-page-3-setup
# From an earlier page of this tutorial: needed again here.
import numpy as np
import matplotlib.pyplot as plt

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

# From an earlier page of this tutorial: needed again here.
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
        if self.m == 0:
            if self.b == 0:
                return "All x values are roots (function is always zero)"
            else:
                return "No roots (function never equals zero)"
        else:
            return -self.b / self.m

# From an earlier page of this tutorial: needed again here.
# Test Constant
c = Constant(3)
print(f"Constant: {c}")
print(f"Derivative: {c.derivative()}")

# Test Linear  
line = Linear(m=2, b=-4)
print(f"\nLinear: {line}")
print(f"Derivative: {line.derivative()}")
print(f"Root: {line.find_root()}")

# From an earlier page of this tutorial: needed again here.
class Quadratic:
    """
    A class representing a quadratic function f(x) = ax² + bx + c.
    
    Attributes:
    -----------
    a : float
        Coefficient of x²
    b : float
        Coefficient of x
    c : float
        Constant term
    """
    
    def __init__(self, a: float, b: float, c: float):
        """
        Create a quadratic function f(x) = ax² + bx + c
        
        Parameters:
        -----------
        a : float
            Coefficient of x²
        b : float
            Coefficient of x
        c : float
            Constant term
        """
        self.a = a
        self.b = b
        self.c = c

# From an earlier page of this tutorial: needed again here.
# Test basic creation
q1 = Quadratic(a=1, b=-4, c=3)
q2 = Quadratic(a=-2, b=0, c=5)
q3 = Quadratic(a=1, b=0, c=0)

print(f"q1: a={q1.a}, b={q1.b}, c={q1.c}")
print(f"q2: a={q2.a}, b={q2.b}, c={q2.c}")
print(f"q3: a={q3.a}, b={q3.b}, c={q3.c}")

# From an earlier page of this tutorial: needed again here.
class Quadratic:
    def __init__(self, a: float, b: float, c: float):
        self.a = a
        self.b = b
        self.c = c
    
    def evaluate(self, x: float) -> float:
        """
        Evaluate the quadratic function at x.
        
        Parameters:
        -----------
        x : float
            The input value
            
        Returns:
        --------
        float
            The value ax² + bx + c
        """
        # YOUR CODE HERE
        pass

# From an earlier page of this tutorial: needed again here.
# Test your implementation
quad = Quadratic(a=1, b=-4, c=3)
print(f"f(0) = {quad.evaluate(0)}")   # Should be 3
print(f"f(1) = {quad.evaluate(1)}")   # Should be 0  (1 - 4 + 3 = 0)
print(f"f(2) = {quad.evaluate(2)}")   # Should be -1 (4 - 8 + 3 = -1)
print(f"f(3) = {quad.evaluate(3)}")   # Should be 0  (9 - 12 + 3 = 0)

# From an earlier page of this tutorial: needed again here.
class Quadratic:
    def __init__(self, a: float, b: float, c: float):
        self.a = a
        self.b = b
        self.c = c
    
    def evaluate(self, x: float) -> float:
        """Evaluate the quadratic function at x."""
        return self.a * x**2 + self.b * x + self.c

# From an earlier page of this tutorial: needed again here.
class Quadratic:
    def __init__(self, a: float, b: float, c: float):
        self.a = a
        self.b = b
        self.c = c
    
    def evaluate(self, x: float) -> float:
        return self.a * x**2 + self.b * x + self.c
    
    def __str__(self) -> str:
        """
        Return a readable string representation of the function.
        
        Returns:
        --------
        str
            String representation like "x² - 4x + 3"
        """
        # YOUR CODE HERE
        pass

# From an earlier page of this tutorial: needed again here.
# Test your implementation
q1 = Quadratic(a=1, b=-4, c=3)
print(f"q1: {q1}")

q2 = Quadratic(a=-2, b=0, c=5)
print(f"q2: {q2}")

q3 = Quadratic(a=1, b=0, c=0)
print(f"q3: {q3}")

# From an earlier page of this tutorial: needed again here.
class Quadratic:
    def __init__(self, a: float, b: float, c: float):
        self.a = a
        self.b = b
        self.c = c
    
    def evaluate(self, x: float) -> float:
        return self.a * x**2 + self.b * x + self.c
    
    def __str__(self) -> str:
        """Return a readable string representation."""
        return f"{self.a}x² + {self.b}x + {self.c}"

# From an earlier page of this tutorial: needed again here.
class Quadratic:
    def __init__(self, a: float, b: float, c: float):
        self.a = a
        self.b = b
        self.c = c
    
    def evaluate(self, x: float) -> float:
        return self.a * x**2 + self.b * x + self.c
    
    def __str__(self) -> str:
        return f"{self.a}x² + {self.b}x + {self.c}"
    
    def plot(self, x_min: float = -10, x_max: float = 10, step: float = 0.1):
        """
        Plot the quadratic function.
        
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
quad = Quadratic(a=1, b=-4, c=3)
quad.plot()

# From an earlier page of this tutorial: needed again here.
class Quadratic:
    def __init__(self, a: float, b: float, c: float):
        self.a = a
        self.b = b
        self.c = c
    
    def evaluate(self, x: float) -> float:
        return self.a * x**2 + self.b * x + self.c
    
    def __str__(self) -> str:
        return f"{self.a}x² + {self.b}x + {self.c}"
    
    def plot(self, x_min: float = -10, x_max: float = 10, step: float = 0.1):
        """Plot the quadratic function."""
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
# Parabola opening upward (a > 0)
q1 = Quadratic(a=1, b=0, c=-4)
print(f"Opening upward: {q1}")
q1.plot(x_min=-5, x_max=5)

# From an earlier page of this tutorial: needed again here.
# Parabola opening downward (a < 0)
q2 = Quadratic(a=-1, b=0, c=4)
print(f"Opening downward: {q2}")
q2.plot(x_min=-5, x_max=5)

# From an earlier page of this tutorial: needed again here.
# Parabola shifted to the side
q3 = Quadratic(a=1, b=-4, c=3)
print(f"Shifted parabola: {q3}")
q3.plot(x_min=-1, x_max=5)

# From an earlier page of this tutorial: needed again here.
quad = Quadratic(a=1, b=0, c=-4)

print("With step = 2 (very coarse):")
quad.plot(x_min=-5, x_max=5, step=2)

# From an earlier page of this tutorial: needed again here.
print("With step = 0.5:")
quad.plot(x_min=-5, x_max=5, step=0.5)

# From an earlier page of this tutorial: needed again here.
print("With step = 0.1 (default):")
quad.plot(x_min=-5, x_max=5, step=0.1)

# From an earlier page of this tutorial: needed again here.
class Quadratic:
    def __init__(self, a: float, b: float, c: float):
        self.a = a
        self.b = b
        self.c = c
    
    def evaluate(self, x: float) -> float:
        return self.a * x**2 + self.b * x + self.c
    
    def __str__(self) -> str:
        return f"{self.a}x² + {self.b}x + {self.c}"
    
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
        Return the derivative of this quadratic function.
        
        The derivative of ax² + bx + c is 2ax + b (a linear function).
        
        Returns:
        --------
        Linear
            A new Linear object representing 2ax + b
        """
        return Linear(m=2*self.a, b=self.b)

# From an earlier page of this tutorial: needed again here.
quad = Quadratic(a=1, b=-4, c=3)
print(f"Original function: {quad}")
print(f"Type: {type(quad).__name__}")

# First derivative
first_deriv = quad.derivative()
print(f"\nFirst derivative: {first_deriv}")
print(f"Type: {type(first_deriv).__name__}")

# Second derivative
second_deriv = first_deriv.derivative()
print(f"\nSecond derivative: {second_deriv}")
print(f"Type: {type(second_deriv).__name__}")

# Third derivative
third_deriv = second_deriv.derivative()
print(f"\nThird derivative: {third_deriv}")
print(f"Type: {type(third_deriv).__name__}")

# Fourth derivative
fourth_deriv = third_deriv.derivative()
print(f"\nFourth derivative: {fourth_deriv}")
print(f"Type: {type(fourth_deriv).__name__}")

# From an earlier page of this tutorial: needed again here.
class Quadratic:
    def __init__(self, a: float, b: float, c: float):
        self.a = a
        self.b = b
        self.c = c
    
    def evaluate(self, x: float) -> float:
        return self.a * x**2 + self.b * x + self.c
    
    def __str__(self) -> str:
        return f"{self.a}x² + {self.b}x + {self.c}"
    
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
        return Linear(m=2*self.a, b=self.b)
    
    def vertex(self):
        """
        Find the vertex (turning point) of the parabola.
        
        The vertex occurs where the derivative equals zero.
        
        Returns:
        --------
        tuple
            (x, y) coordinates of the vertex
        """
        # Get the derivative
        deriv = self.derivative()
        
        # Find where derivative = 0
        x_vertex = deriv.find_root()
        
        # Evaluate the original function at this x
        y_vertex = self.evaluate(x_vertex)
        
        return (x_vertex, y_vertex)

# From an earlier page of this tutorial: needed again here.
quad = Quadratic(a=1, b=-4, c=3)
print(f"Quadratic: {quad}")

# Method 1: Use vertex formula
vertex_x, vertex_y = quad.vertex()
print(f"\nVertex (using vertex method): ({vertex_x}, {vertex_y})")

# Method 2: Find where derivative = 0
deriv = quad.derivative()
print(f"\nDerivative: {deriv}")
deriv_root = deriv.find_root()
print(f"Where derivative = 0: x = {deriv_root}")

# They should match!
print(f"\nDo they match? {vertex_x == deriv_root}")

# What's the slope at the vertex?
slope_at_vertex = deriv.evaluate(vertex_x)
print(f"Slope at vertex: {slope_at_vertex}")

# From an earlier page of this tutorial: needed again here.
def plot_with_derivative(quad, x_min=-5, x_max=5):
    """
    Plot a quadratic and its derivative on the same axes.
    """
    x_values = np.arange(x_min, x_max, 0.1)
    
    # Evaluate the quadratic
    y_quad = [quad.evaluate(x) for x in x_values]
    
    # Evaluate the derivative
    deriv = quad.derivative()
    y_deriv = [deriv.evaluate(x) for x in x_values]
    
    # Plot both
    plt.plot(x_values, y_quad, label=f'f(x) = {quad}', linewidth=2)
    plt.plot(x_values, y_deriv, label=f"f'(x) = {deriv}", linestyle='--', linewidth=2)
    
    # Mark the vertex
    vertex_x, vertex_y = quad.vertex()
    plt.plot(vertex_x, vertex_y, 'ro', markersize=10, label=f'Vertex ({vertex_x:.2f}, {vertex_y:.2f})')
    
    plt.axhline(y=0, color='k', linestyle='-', linewidth=0.5)
    plt.axvline(x=0, color='k', linestyle='-', linewidth=0.5)
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Function and its Derivative')
    plt.show()

# From an earlier page of this tutorial: needed again here.
quad = Quadratic(a=1, b=-4, c=3)
plot_with_derivative(quad)

# From an earlier page of this tutorial: needed again here.
# Upward-opening parabola
q1 = Quadratic(a=2, b=0, c=-8)
plot_with_derivative(q1)

# From an earlier page of this tutorial: needed again here.
# Downward-opening parabola
q2 = Quadratic(a=-1, b=4, c=1)
plot_with_derivative(q2)

# From an earlier page of this tutorial: needed again here.
class Quadratic:
    def __init__(self, a: float, b: float, c: float):
        self.a = a
        self.b = b
        self.c = c
    
    def evaluate(self, x: float) -> float:
        return self.a * x**2 + self.b * x + self.c
    
    def __str__(self) -> str:
        return f"{self.a}x² + {self.b}x + {self.c}"
    
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
        return Linear(m=2*self.a, b=self.b)
    
    def vertex(self):
        deriv = self.derivative()
        x_vertex = deriv.find_root()
        y_vertex = self.evaluate(x_vertex)
        return (x_vertex, y_vertex)
    
    def discriminant(self) -> float:
        """
        Calculate the discriminant b² - 4ac.
        
        The discriminant tells us about the roots:
        - Positive: two real roots
        - Zero: one real root (vertex touches x-axis)
        - Negative: no real roots
        
        Returns:
        --------
        float
            The value of b² - 4ac
        """
        return self.b**2 - 4*self.a*self.c
    
    def find_roots(self):
        """
        Find the x-intercepts using the quadratic formula.
        
        Returns:
        --------
        list
            List of roots (may be empty, contain one root, or two roots)
        """
        disc = self.discriminant()
        
        if disc < 0:
            # No real roots
            return []
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

# From an earlier page of this tutorial: needed again here.
# Case 1: Two roots (discriminant > 0)
q1 = Quadratic(a=1, b=0, c=-4)  # x² - 4
print(f"Function: {q1}")
print(f"Discriminant: {q1.discriminant()}")
print(f"Roots: {q1.find_roots()}")
q1.plot(x_min=-5, x_max=5)

# From an earlier page of this tutorial: needed again here.
# Case 2: One root (discriminant = 0)
q2 = Quadratic(a=1, b=-2, c=1)  # x² - 2x + 1 = (x-1)²
print(f"Function: {q2}")
print(f"Discriminant: {q2.discriminant()}")
print(f"Roots: {q2.find_roots()}")
q2.plot(x_min=-1, x_max=3)

# From an earlier page of this tutorial: needed again here.
# Case 3: No real roots (discriminant < 0)
q3 = Quadratic(a=1, b=0, c=4)  # x² + 4
print(f"Function: {q3}")
print(f"Discriminant: {q3.discriminant()}")
print(f"Roots: {q3.find_roots()}")
q3.plot(x_min=-5, x_max=5)

# From an earlier page of this tutorial: needed again here.
quad = Quadratic(a=1, b=-4, c=3)  # This factors as (x-1)(x-3)
print(f"Function: {quad}")

roots = quad.find_roots()
print(f"Roots: {roots}")

# Average of the two roots
avg_roots = (roots[0] + roots[1]) / 2
print(f"Average of roots: {avg_roots}")

# Vertex x-coordinate
vertex_x, vertex_y = quad.vertex()
print(f"Vertex x-coordinate: {vertex_x}")

print(f"\nAre they equal? {avg_roots == vertex_x}")

# From an earlier page of this tutorial: needed again here.
# This is frustrating!
print("In Constant:")
print("    def plot(self, x_min=-10, x_max=10, step=0.1):")
print("        x_values = np.arange(x_min, x_max + step, step)")
print("        y_values = [self.evaluate(x) for x in x_values]")
print("        # ... plotting code ...")
print()
print("In Linear:")
print("    def plot(self, x_min=-10, x_max=10, step=0.1):")
print("        x_values = np.arange(x_min, x_max + step, step)")
print("        y_values = [self.evaluate(x) for x in x_values]")
print("        # ... SAME plotting code ...")
print()
print("In Quadratic:")
print("    def plot(self, x_min=-10, x_max=10, step=0.1):")
print("        x_values = np.arange(x_min, x_max + step, step)")
print("        y_values = [self.evaluate(x) for x in x_values]")
print("        # ... SAME plotting code AGAIN ...")

# From an earlier page of this tutorial: needed again here.
const = Constant(5)
print(f"Function: {const}")

integral = const.integrate(C=0)
print(f"Integral: {integral}")

# Verify
check = integral.derivative()
print(f"Derivative of integral: {check}")

# From an earlier page of this tutorial: needed again here.
line = Linear(m=2, b=3)
print(f"Linear function: {line}")
print("Can we integrate it?")

# The integral SHOULD be: (2/2)x² + 3x = x² + 3x
# But we can't create that without a Quadratic class!
# We could write:
#   def integrate(self, C=0):
#       return Quadratic(a=self.m/2, b=self.b, c=C)

print("\nFor Quadratic:")
quad = Quadratic(a=1, b=-3, c=2)
print(f"Quadratic function: {quad}")
print("Can we integrate it?")

# The integral SHOULD be: (1/3)x³ - (3/2)x² + 2x + C
# But we don't have a Cubic class!
print("NO! We'd need a Cubic class.")

# From an earlier page of this tutorial: needed again here.
print("Derivatives (going DOWN in degree):")
print("Quartic → Cubic → Quadratic → Linear → Constant → Constant(0)")
print("This works fine - we eventually reach zero.")
print()
print("Integrals (going UP in degree):")
print("Constant → Linear → Quadratic → Cubic → Quartic → Quintic → ...")
print("This needs INFINITE classes!")
print()
print("Classes we'd need to create:")
print("- Cubic (degree 3)")
print("- Quartic (degree 4)")
print("- Quintic (degree 5)")
print("- Sextic (degree 6)")
print("- Septic (degree 7)")
print("- Octic (degree 8)")
print("- ... forever!")

# From an earlier page of this tutorial: needed again here.
print("If we had Cubic(a, b, c, d) representing ax³ + bx² + cx + d:")
print()
print("Its derivative would be: 3ax² + 2bx + c (a Quadratic!)")
print("That derivative's derivative: 6ax + 2b (a Linear!)")
print("That derivative's derivative: 6a (a Constant!)")
print("That derivative's derivative: 0 (Constant(0))")
print()
print("So a cubic has UP TO 2 turning points!")
print("(Where the quadratic derivative equals zero)")

# From an earlier page of this tutorial: needed again here.
functions = [
    Constant(3),
    Linear(m=2, b=-4),
    Quadratic(a=1, b=-4, c=3)
]

for f in functions:
    print(f"Function: {f}")
    print(f"  Type: {type(f).__name__}")
    print(f"  At x=2: {f.evaluate(2)}")
    print(f"  Derivative: {f.derivative()}")
    print(f"  Derivative type: {type(f.derivative()).__name__}")
    print()

# From an earlier page of this tutorial: needed again here.
# Start with a quadratic
f = Quadratic(a=1, b=-6, c=8)
print(f"f(x) = {f}")

# Take successive derivatives
f1 = f.derivative()
print(f"f'(x) = {f1} [{type(f1).__name__}]")

f2 = f1.derivative()
print(f"f''(x) = {f2} [{type(f2).__name__}]")

f3 = f2.derivative()
print(f"f'''(x) = {f3} [{type(f3).__name__}]")

f4 = f3.derivative()
print(f"f''''(x) = {f4} [{type(f4).__name__}]")
```

## Reflection: What We've Learned

### What Works Well:

1. **Derivative chain is beautiful**: `Quadratic → Linear → Constant → Constant(0)`
2. **Classes return proper types**: Each derivative returns the correct class
3. **Mathematical connections are clear**: Vertex ↔ derivative root, discriminant ↔ number of roots
4. **Polymorphism emerges**: Same method names let us treat different classes uniformly

### What's Broken:

1. **Code duplication**: `plot()` is identical in all three classes
2. **Integration blocked**: Can't integrate `Quadratic` without `Cubic` class
3. **Infinite classes needed**: Would need a class for every polynomial degree
4. **Lost generality**: Can only work with degrees 0, 1, 2

### The Central Question:

**Is there a way to represent ANY polynomial with ONE class?**

What if instead of:
```python
Constant(c) # stores c
Linear(m, b) # stores m, b
Quadratic(a, b, c) # stores a, b, c
Cubic(a, b, c, d) # stores a, b, c, d
# ... forever
```

We used:
```python
Polynomial([c]) # represents c
Polynomial([b, m]) # represents b + mx 
Polynomial([c, b, a]) # represents c + bx + ax²
Polynomial([d, c, b, a]) # represents d + cx + bx² + ax³
# ... any degree!
```

**Next time**, we'll explore this idea!

## Exercises

### Your turn 1: Exploring Vertices

```python exec
id: polynomials-2-quadratics-page-3-1
# Create three quadratics:
# - One opening upward with vertex above x-axis
# - One opening downward with vertex below x-axis  
# - One with vertex exactly on the x-axis

# For each one:
# - Print the function
# - Print the vertex
# - Print the discriminant
# - Print the roots
# - Plot it

# YOUR CODE HERE
```

### Your turn 2: Derivative Chain

```python exec
id: polynomials-2-quadratics-page-3-2
# Create q = Quadratic(a=2, b=-8, c=6)
# Take successive derivatives until you reach Constant(0)
# At each step, print the function and evaluate it at x=3

# YOUR CODE HERE
```

### Your turn 3: Root Verification

```python exec
id: polynomials-2-quadratics-page-3-3
# Create a quadratic with two roots
# Use find_roots() to get them
# Evaluate the function at each root to verify they give 0
# Find the vertex and verify it's halfway between the roots

# YOUR CODE HERE
```

### Your turn 4: Factored Form

```python exec
id: polynomials-2-quadratics-page-3-4
# If a quadratic has roots r1 and r2, it can be written as:
# f(x) = a(x - r1)(x - r2)

# Given roots at x=1 and x=3, and knowing the parabola opens upward (a=1),
# expand (x-1)(x-3) by hand to get ax² + bx + c form
# Create the Quadratic object with those coefficients
# Verify that find_roots() gives you back [1, 3]

# YOUR CODE HERE
```

### Your turn 5: Comparing Derivatives

```python exec
id: polynomials-2-quadratics-page-3-5
# Create several quadratics with different values of a
# For each one:
# - Find its derivative
# - What's the relationship between the coefficient 'a' and the derivative's slope?
# - Plot each quadratic with its derivative

# YOUR CODE HERE
```

## Looking Ahead

In **Tutorial 3**, we'll create a general `Polynomial` class that can represent any degree polynomial using a list of coefficients. We'll discover:

- How to represent polynomials with coefficient lists
- Derivatives and integrals that work for ANY degree
- What we gain (generality, no code duplication)
- What we lose (easy exact formulas, special methods like `vertex()`)

The problems we've noticed will finally have a solution... but it will come with trade-offs!

---

**End of Tutorial 2**

## Looking back

Before leaving this page, a sentence on each. What you write stays on this device.

```reflect
- Something you expected before running a cell that turned out differently
- The one idea from this page you could explain to someone else now
- A question this page raised that it did not answer
```
