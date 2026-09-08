---
title: "Calculus at Sea: Derivatives and Optimization"
slug: 01-derivatives-at-sea
course: ai-and-ml-foundations
course_title: "AI and ML Foundations"
series: 2-calculus
series_title: "Calculus"
version: 2026.09.06.1
---

# Calculus at Sea: Derivatives and Optimization
## From Rates of Change to Finding Treasure


**The Pirate's Toolkit:**
As a navigator, you need to understand how things change:
- How fast is the ship moving?
- When is the tide rising fastest?
- Where is the treasure hill's peak?
- What angle maximizes cannon range?

All of these involve **derivatives** - the mathematical tool for understanding change.

```python exec
id: 01-derivatives-at-sea-1
# Import required libraries
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import patches
import sympy as sp
from sympy import symbols, diff, sin, cos, exp, log, sqrt

# Set up nice plotting defaults
plt.rcParams['figure.figsize'] = (10, 6)
plt.rcParams['font.size'] = 11
```

---
## Part 1: What is a Derivative?
### The Intuitive Idea: Velocity

Imagine a ship sailing. Its **position** changes over time. The **derivative** tells us the **velocity** - how fast the position is changing.

**Mathematical Definition:**
The derivative of f(x) at point x is:

$$f'(x) = \lim_{h \to 0} \frac{f(x+h) - f(x)}{h}$$

This is the **slope of the tangent line** at point x.

```python exec
id: 01-derivatives-at-sea-2
def visualize_derivative_concept():
    """
    Visualize the derivative as the slope of the tangent line.
    """
    # Define a function: ship's position over time
    def ship_position(time):
        return 0.5 * time**2 + 2 * time + 1

    # Time points
    time_values = np.linspace(0, 5, 100)
    position_values = ship_position(time_values)

    # Point where we want the derivative
    time_point = 2.0
    position_point = ship_position(time_point)

    # Calculate derivative (slope) at this point
    # For f(t) = 0.5t² + 2t + 1, f'(t) = t + 2
    derivative_value = time_point + 2

    # Create tangent line
    tangent_time = np.linspace(time_point - 1, time_point + 1, 50)
    tangent_position = position_point + derivative_value * (tangent_time - time_point)

    # Plot
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

    # Left plot: Function and tangent line
    ax1.plot(time_values, position_values, 'b-', linewidth=2, label='Ship position')
    ax1.plot(tangent_time, tangent_position, 'r--', linewidth=2, label=f'Tangent (slope={derivative_value})')
    ax1.plot(time_point, position_point, 'ro', markersize=10, label=f'Point at t={time_point}')
    ax1.set_xlabel('Time (hours)')
    ax1.set_ylabel('Position (nautical miles)')
    ax1.set_title('Ship Position Over Time')
    ax1.legend()
    ax1.grid(True, alpha=0.3)

    # Right plot: Show secant lines approaching tangent
    ax2.plot(time_values, position_values, 'b-', linewidth=2, label='Ship position')
    ax2.plot(time_point, position_point, 'ro', markersize=10)

    # Draw several secant lines with decreasing h
    h_values = [1.5, 1.0, 0.5, 0.2]
    colors = ['orange', 'yellow', 'lime', 'red']

    for h_value, color in zip(h_values, colors):
        time_plus_h = time_point + h_value
        position_plus_h = ship_position(time_plus_h)

        # Secant line
        secant_slope = (position_plus_h - position_point) / h_value
        secant_time = np.array([time_point, time_plus_h])
        secant_position = np.array([position_point, position_plus_h])

        ax2.plot(secant_time, secant_position, color=color, linewidth=2,
                label=f'h={h_value}, slope≈{secant_slope:.2f}', alpha=0.7)

    ax2.set_xlabel('Time (hours)')
    ax2.set_ylabel('Position (nautical miles)')
    ax2.set_title('Secant Lines Approaching Tangent (h → 0)')
    ax2.legend(loc='upper left', fontsize=9)
    ax2.grid(True, alpha=0.3)
    ax2.set_xlim(1, 4)
    ax2.set_ylim(4, 12)

    plt.tight_layout()
    plt.show()

    print(f"At time t = {time_point} hours:")
    print(f"  Position = {position_point:.2f} nautical miles")
    print(f"  Velocity (derivative) = {derivative_value:.2f} nautical miles per hour")
    print(f"\nThe derivative tells us the ship's instantaneous velocity!")

visualize_derivative_concept()
```

### Interactive Exploration: Change the Function

Let's explore how derivatives work for different functions.

```python exec
id: 01-derivatives-at-sea-3
def plot_function_and_derivative(function, derivative_function, x_range, title):
    """
    Plot a function and its derivative side by side.
    """
    x_values = np.linspace(x_range[0], x_range[1], 200)
    y_values = function(x_values)
    derivative_values = derivative_function(x_values)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

    # Original function
    ax1.plot(x_values, y_values, 'b-', linewidth=2)
    ax1.axhline(y=0, color='k', linewidth=0.5)
    ax1.axvline(x=0, color='k', linewidth=0.5)
    ax1.set_xlabel('x')
    ax1.set_ylabel('f(x)')
    ax1.set_title(f'Function: {title}')
    ax1.grid(True, alpha=0.3)

    # Derivative
    ax2.plot(x_values, derivative_values, 'r-', linewidth=2)
    ax2.axhline(y=0, color='k', linewidth=0.5)
    ax2.axvline(x=0, color='k', linewidth=0.5)
    ax2.set_xlabel('x')
    ax2.set_ylabel("f'(x)")
    ax2.set_title("Derivative: Rate of Change")
    ax2.grid(True, alpha=0.3)

    # Mark interesting points
    # Where derivative is zero (local max/min)
    zero_crossings = np.where(np.diff(np.sign(derivative_values)))[0]
    for idx in zero_crossings:
        ax1.plot(x_values[idx], y_values[idx], 'go', markersize=10,
                label='Critical point' if idx == zero_crossings[0] else '')
        ax2.plot(x_values[idx], 0, 'go', markersize=10)

    if len(zero_crossings) > 0:
        ax1.legend()

    plt.tight_layout()
    plt.show()

# Example 1: Quadratic (parabola)
print("Example 1: Treasure Hill")
print("Height h(x) = -x² + 4x + 5")
print("Derivative h'(x) = -2x + 4")
print()

def hill_height(x):
    return -x**2 + 4*x + 5

def hill_slope(x):
    return -2*x + 4

plot_function_and_derivative(hill_height, hill_slope, [-1, 5], 'h(x) = -x² + 4x + 5')

print("Notice: Where the derivative equals zero, the hill reaches its peak!")
print("This happens at x = 2, where h'(2) = 0")
```

```python exec
id: 01-derivatives-at-sea-4
# Example 2: Cubic function
print("Example 2: Ocean Wave")
print("Wave w(x) = x³ - 6x² + 9x + 2")
print("Derivative w'(x) = 3x² - 12x + 9")
print()

def wave_height(x):
    return x**3 - 6*x**2 + 9*x + 2

def wave_slope(x):
    return 3*x**2 - 12*x + 9

plot_function_and_derivative(wave_height, wave_slope, [0, 4], 'w(x) = x³ - 6x² + 9x + 2')

print("Notice: This wave has both a crest (local max) and a trough (local min)!")
print("Both occur where the derivative equals zero.")
```

```python exec
id: 01-derivatives-at-sea-5
# Example 3: Trigonometric (tide)
print("Example 3: Tide Height")
print("Tide T(t) = 3sin(t) + 1")
print("Derivative T'(t) = 3cos(t)")
print()

def tide_height(time):
    return 3 * np.sin(time) + 1

def tide_rate(time):
    return 3 * np.cos(time)

plot_function_and_derivative(tide_height, tide_rate, [0, 2*np.pi], 'T(t) = 3sin(t) + 1')

print("Notice: When tide is at its highest/lowest, the rate of change is zero!")
print("When tide is at mean level, it's changing fastest (max derivative).")
```

### Your turn 1.1: Understanding Derivatives Visually

```python exec
id: 01-derivatives-at-sea-6
# For each graph, answer these questions:
# 1. Where is f'(x) positive? (function increasing)
# 2. Where is f'(x) negative? (function decreasing)
# 3. Where is f'(x) = 0? (flat spots - maxima/minima)
# 4. Where is f'(x) largest in magnitude? (steepest slope)

# Create your own function and its derivative:
def my_function(x):
    # Try: x**4 - 4*x**3 + 2
    pass

def my_derivative(x):
    # What's the derivative of your function?
    pass

# Plot them:
# plot_function_and_derivative(my_function, my_derivative, [-2, 4], 'Your function')
```

---
## Part 2: Numerical Derivatives (Approximation)
### Computing Derivatives Without Calculus

When we don't know the formula for the derivative, we can **approximate** it using the definition:

$$f'(x) \approx \frac{f(x+h) - f(x)}{h}$$

for a small value of h. This is called the **forward difference** method.

There are three main methods:
1. **Forward difference**: $f'(x) \approx \frac{f(x+h) - f(x)}{h}$
2. **Backward difference**: $f'(x) \approx \frac{f(x) - f(x-h)}{h}$
3. **Central difference**: $f'(x) \approx \frac{f(x+h) - f(x-h)}{2h}$ (most accurate!)

```python exec
id: 01-derivatives-at-sea-7
def forward_difference(function, x_value, step_size):
    """
    Compute derivative using forward difference method.

    Args:
        function: The function to differentiate
        x_value: Point at which to find derivative
        step_size: Small h value

    Returns:
        Approximate derivative at x_value
    """
    return (function(x_value + step_size) - function(x_value)) / step_size

def backward_difference(function, x_value, step_size):
    """
    Compute derivative using backward difference method.
    """
    return (function(x_value) - function(x_value - step_size)) / step_size

def central_difference(function, x_value, step_size):
    """
    Compute derivative using central difference method (most accurate).
    """
    return (function(x_value + step_size) - function(x_value - step_size)) / (2 * step_size)

# Test with a function we know the exact derivative
def test_function(x):
    return x**3

# Exact derivative: 3x²
def exact_derivative(x):
    return 3 * x**2

test_point = 2.0
exact_value = exact_derivative(test_point)

print(f"Function: f(x) = x³")
print(f"Point: x = {test_point}")
print(f"Exact derivative: f'({test_point}) = {exact_value}")
print()

# Try different step sizes
step_sizes = [0.1, 0.01, 0.001, 0.0001]

print("Numerical Approximations:")
print(f"{'h':<10} {'Forward':<12} {'Backward':<12} {'Central':<12}")
print(f"{'':10} {'Diff':<12} {'Diff':<12} {'Diff':<12}")
print("-" * 50)

for step_size in step_sizes:
    forward = forward_difference(test_function, test_point, step_size)
    backward = backward_difference(test_function, test_point, step_size)
    central = central_difference(test_function, test_point, step_size)

    print(f"{step_size:<10.4f} {forward:<12.6f} {backward:<12.6f} {central:<12.6f}")

print(f"\nExact: {exact_value}")
print("\nNotice: Central difference is most accurate!")
print("Also notice: Smaller h generally gives better approximation (but not too small!)")
```

### Visualizing the Approximation Methods

```python exec
id: 01-derivatives-at-sea-8
def visualize_difference_methods():
    """
    Show how different finite difference methods approximate the derivative.
    """
    def function(x):
        return 0.3 * x**2 + 1

    x_point = 2.0
    step_size = 0.8

    # Function values
    x_values = np.linspace(0, 4, 100)
    y_values = function(x_values)

    fig, axes = plt.subplots(1, 3, figsize=(15, 5))

    methods = [
        ('Forward', x_point, x_point + step_size),
        ('Backward', x_point - step_size, x_point),
        ('Central', x_point - step_size, x_point + step_size)
    ]

    for ax, (name, x1, x2) in zip(axes, methods):
        # Plot function
        ax.plot(x_values, y_values, 'b-', linewidth=2, label='f(x)')

        # Plot points used
        if name == 'Central':
            ax.plot([x1, x2], [function(x1), function(x2)], 'ro', markersize=8)
            ax.plot(x_point, function(x_point), 'go', markersize=10, label='Target point')
        else:
            ax.plot([x1, x2], [function(x1), function(x2)], 'ro', markersize=8, label='Points used')

        # Draw secant line
        slope = (function(x2) - function(x1)) / (x2 - x1)
        secant_x = np.linspace(x1 - 0.5, x2 + 0.5, 50)
        secant_y = function(x1) + slope * (secant_x - x1)
        ax.plot(secant_x, secant_y, 'r--', linewidth=2, label=f'Slope={slope:.2f}')

        ax.set_xlabel('x')
        ax.set_ylabel('f(x)')
        ax.set_title(f'{name} Difference')
        ax.legend()
        ax.grid(True, alpha=0.3)
        ax.set_xlim(0, 4)
        ax.set_ylim(0, 6)

    plt.tight_layout()
    plt.show()

visualize_difference_methods()

print("Key Observations:")
print("- Forward: Uses points to the right")
print("- Backward: Uses points to the left")
print("- Central: Uses points on both sides (more balanced, more accurate!)")
```

### Your turn 2.1: Implement Numerical Derivatives

```python exec
id: 01-derivatives-at-sea-9
# Challenge: Compute the derivative of sin(x) at x = π/4 numerically
# The exact answer is cos(π/4) = √2/2 ≈ 0.7071

import math

def sine_function(x):
    return math.sin(x)

target_x = math.pi / 4
exact_derivative = math.cos(target_x)

# 1. Use central difference with h=0.001 to approximate the derivative

# 2. Calculate the percentage error

# 3. Try h = 0.1, 0.01, 0.001, 0.0001 and plot error vs h

# 4. What happens if h is too small (try h=1e-10)? Why?
```

### Computing Derivatives for Data

```python exec
id: 01-derivatives-at-sea-10
def numerical_derivative_array(x_values, y_values, method='central'):
    """
    Compute numerical derivative for discrete data points.

    Args:
        x_values: Array of x coordinates
        y_values: Array of y coordinates
        method: 'forward', 'backward', or 'central'

    Returns:
        Array of derivative values
    """
    derivative = np.zeros_like(y_values)

    if method == 'forward':
        for i in range(len(y_values) - 1):
            derivative[i] = (y_values[i+1] - y_values[i]) / (x_values[i+1] - x_values[i])
        derivative[-1] = derivative[-2]  # Repeat last value

    elif method == 'backward':
        derivative[0] = (y_values[1] - y_values[0]) / (x_values[1] - x_values[0])
        for i in range(1, len(y_values)):
            derivative[i] = (y_values[i] - y_values[i-1]) / (x_values[i] - x_values[i-1])

    elif method == 'central':
        # First point: forward difference
        derivative[0] = (y_values[1] - y_values[0]) / (x_values[1] - x_values[0])

        # Middle points: central difference
        for i in range(1, len(y_values) - 1):
            derivative[i] = (y_values[i+1] - y_values[i-1]) / (x_values[i+1] - x_values[i-1])

        # Last point: backward difference
        derivative[-1] = (y_values[-1] - y_values[-2]) / (x_values[-1] - x_values[-2])

    return derivative

# Example: Tide measurements over 24 hours
time_hours = np.array([0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24])
tide_height_meters = np.array([2.1, 3.5, 4.2, 3.8, 2.5, 1.3, 0.8, 1.2, 2.3, 3.6, 4.3, 3.9, 2.4])

# Compute rate of change
tide_rate = numerical_derivative_array(time_hours, tide_height_meters, method='central')

# Plot
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8))

ax1.plot(time_hours, tide_height_meters, 'b-o', linewidth=2, markersize=6)
ax1.set_xlabel('Time (hours)')
ax1.set_ylabel('Tide Height (meters)')
ax1.set_title('Measured Tide Heights')
ax1.grid(True, alpha=0.3)

ax2.plot(time_hours, tide_rate, 'r-o', linewidth=2, markersize=6)
ax2.axhline(y=0, color='k', linewidth=0.5, linestyle='--')
ax2.set_xlabel('Time (hours)')
ax2.set_ylabel('Rate of Change (meters/hour)')
ax2.set_title('Tide Rising/Falling Rate (Numerical Derivative)')
ax2.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

print("Interpretation:")
print("- Positive derivative: Tide is rising")
print("- Negative derivative: Tide is falling")
print("- Zero derivative: Tide at high or low point")
print(f"\nFastest rise at t={time_hours[np.argmax(tide_rate)]} hours: {np.max(tide_rate):.2f} m/hr")
print(f"Fastest fall at t={time_hours[np.argmin(tide_rate)]} hours: {np.min(tide_rate):.2f} m/hr")
```

### Your turn 2.2: Analyzing Ship Velocity

```python exec
id: 01-derivatives-at-sea-11
# A ship's position is recorded every hour
time_data = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8])
position_data = np.array([0, 5, 18, 33, 48, 60, 68, 72, 73])  # nautical miles

# 1. Compute the ship's velocity (derivative of position) using central difference

# 2. Plot position and velocity on separate graphs

# 3. When was the ship moving fastest?

# 4. When was the ship decelerating?

# 5. Compute the acceleration (derivative of velocity = second derivative of position)
```

---
## Part 3: Symbolic Derivatives (Exact)
### Let the Computer Do the Calculus!

**SymPy** is a Python library for symbolic mathematics. It can compute exact derivatives algebraically.

```python exec
id: 01-derivatives-at-sea-12
# Define a symbolic variable
x = symbols('x')

# Define a symbolic function
function_expression = x**3 + 2*x**2 - 5*x + 7

print("Function:")
print(f"f(x) = {function_expression}")
print()

# Compute the derivative symbolically
derivative_expression = diff(function_expression, x)

print("Derivative (computed by SymPy):")
print(f"f'(x) = {derivative_expression}")
print()

# Second derivative
second_derivative = diff(derivative_expression, x)
print("Second derivative:")
print(f"f''(x) = {second_derivative}")
```

### Common Derivative Rules Demonstrated

```python exec
id: 01-derivatives-at-sea-13
x = symbols('x')

print("Derivative Rules Demonstrated:")
print("=" * 60)

# Power rule
f1 = x**5
print(f"\nPower Rule: d/dx({f1}) = {diff(f1, x)}")

# Constant multiple
f2 = 7*x**3
print(f"Constant Multiple: d/dx({f2}) = {diff(f2, x)}")

# Sum rule
f3 = x**2 + 3*x + 5
print(f"Sum Rule: d/dx({f3}) = {diff(f3, x)}")

# Product rule
f4 = x**2 * sin(x)
print(f"Product Rule: d/dx({f4}) = {diff(f4, x)}")

# Quotient rule
f5 = x**2 / (x + 1)
print(f"Quotient Rule: d/dx({f5}) = {diff(f5, x)}")

# Chain rule
f6 = sin(x**2)
print(f"Chain Rule: d/dx({f6}) = {diff(f6, x)}")

# Exponential
f7 = exp(x)
print(f"Exponential: d/dx({f7}) = {diff(f7, x)}")

# Logarithm
f8 = log(x)
print(f"Logarithm: d/dx({f8}) = {diff(f8, x)}")

# Trigonometric
f9 = sin(x)
print(f"Sine: d/dx({f9}) = {diff(f9, x)}")

f10 = cos(x)
print(f"Cosine: d/dx({f10}) = {diff(f10, x)}")
```

### Evaluating Symbolic Derivatives at Specific Points

```python exec
id: 01-derivatives-at-sea-14
x = symbols('x')

# Define a function
treasure_function = x**3 - 6*x**2 + 9*x + 5

print("Treasure Hill Function:")
print(f"h(x) = {treasure_function}")
print()

# Get derivative
slope_function = diff(treasure_function, x)
print("Slope Function (derivative):")
print(f"h'(x) = {slope_function}")
print()

# Evaluate at specific points
points_of_interest = [0, 1, 2, 3, 4]

print("Evaluation at specific points:")
print(f"{'x':<5} {'h(x)':<10} {'h\'(x)':<10} {'Interpretation'}")
print("-" * 50)

for point in points_of_interest:
    height = treasure_function.subs(x, point)
    slope = slope_function.subs(x, point)

    if slope > 0:
        interpretation = "Going uphill"
    elif slope < 0:
        interpretation = "Going downhill"
    else:
        interpretation = "Flat (peak or valley!)"

    print(f"{point:<5} {float(height):<10.2f} {float(slope):<10.2f} {interpretation}")
```

### Your turn 3.1: Symbolic Differentiation Practice

```python exec
id: 01-derivatives-at-sea-15
x = symbols('x')

# Compute derivatives of these functions symbolically:

# 1. f(x) = x⁴ - 8x² + 16

# 2. g(x) = (x² + 1)(x³ - 2x)

# 3. h(x) = sin(x) * cos(x)
#    Hint: This simplifies to sin(2x)/2

# 4. k(x) = e^(x²)

# 5. m(x) = ln(x² + 1)

# For each:
# a) Find the derivative
# b) Find where the derivative equals zero (critical points)
# c) Evaluate the derivative at x = 1
```

### Comparing Numerical vs Symbolic

```python exec
id: 01-derivatives-at-sea-16
def compare_numerical_symbolic():
    """
    Compare numerical and symbolic derivative methods.
    """
    # Symbolic
    x = symbols('x')
    symbolic_function = exp(sin(x))
    symbolic_derivative = diff(symbolic_function, x)

    print("Function: f(x) = e^(sin(x))")
    print(f"Symbolic derivative: f'(x) = {symbolic_derivative}")
    print()

    # Convert to numerical function
    from sympy import lambdify
    numerical_function = lambdify(x, symbolic_function, 'numpy')
    exact_derivative_func = lambdify(x, symbolic_derivative, 'numpy')

    # Test points
    test_points = np.linspace(0, 2*np.pi, 10)

    print("Comparison at various points:")
    print(f"{'x':<10} {'Symbolic':<15} {'Numerical':<15} {'Error':<15}")
    print("-" * 60)

    step_size = 0.0001
    for point in test_points:
        exact = exact_derivative_func(point)
        approx = central_difference(numerical_function, point, step_size)
        error = abs(exact - approx)

        print(f"{point:<10.4f} {exact:<15.8f} {approx:<15.8f} {error:<15.2e}")

    print("\nConclusion: Symbolic is exact, numerical is approximate but very close!")

compare_numerical_symbolic()
```

---
## Part 4: Optimization - Finding Extrema
### Using Derivatives to Find Maximum and Minimum Values

**Key Idea**: At a local maximum or minimum, the derivative equals zero!

**Process**:
1. Find f'(x)
2. Solve f'(x) = 0 to find critical points
3. Use second derivative test or check values to determine if max or min

**Second Derivative Test**:
- If f''(x) > 0: local minimum (concave up)
- If f''(x) < 0: local maximum (concave down)
- If f''(x) = 0: inconclusive

```python exec
id: 01-derivatives-at-sea-17
def find_and_classify_critical_points(function_expr):
    """
    Find critical points and classify them as max, min, or saddle.
    """
    x = symbols('x')

    print(f"Function: f(x) = {function_expr}")
    print()

    # First derivative
    first_deriv = diff(function_expr, x)
    print(f"First derivative: f'(x) = {first_deriv}")

    # Find critical points (where f'(x) = 0)
    from sympy import solve
    critical_points = solve(first_deriv, x)
    print(f"\nCritical points (f'(x) = 0): {critical_points}")

    # Second derivative
    second_deriv = diff(first_deriv, x)
    print(f"\nSecond derivative: f''(x) = {second_deriv}")
    print()

    # Classify each critical point
    print("Classification:")
    print("-" * 60)

    for point in critical_points:
        if point.is_real:
            second_deriv_value = second_deriv.subs(x, point)
            function_value = function_expr.subs(x, point)

            print(f"\nAt x = {float(point):.4f}:")
            print(f"  f(x) = {float(function_value):.4f}")
            print(f"  f''(x) = {float(second_deriv_value):.4f}")

            if second_deriv_value > 0:
                print(f"  → LOCAL MINIMUM (concave up)")
            elif second_deriv_value < 0:
                print(f"  → LOCAL MAXIMUM (concave down)")
            else:
                print(f"  → INCONCLUSIVE (test fails)")

# Example 1: Simple parabola
x = symbols('x')
parabola = x**2 - 4*x + 7
find_and_classify_critical_points(parabola)
print("\n" + "="*60 + "\n")

# Example 2: Cubic with both max and min
cubic = x**3 - 6*x**2 + 9*x + 1
find_and_classify_critical_points(cubic)
```

### Visualizing Optimization

```python exec
id: 01-derivatives-at-sea-18
def visualize_optimization(function_expr, x_range, title):
    """
    Visualize a function and its critical points.
    """
    x = symbols('x')

    # Convert to numerical function
    from sympy import lambdify
    numerical_func = lambdify(x, function_expr, 'numpy')

    # Find critical points
    from sympy import solve
    first_deriv = diff(function_expr, x)
    second_deriv = diff(first_deriv, x)
    critical_points = [float(pt) for pt in solve(first_deriv, x) if pt.is_real]

    # Plot
    x_vals = np.linspace(x_range[0], x_range[1], 500)
    y_vals = numerical_func(x_vals)

    plt.figure(figsize=(12, 6))
    plt.plot(x_vals, y_vals, 'b-', linewidth=2, label='f(x)')

    # Mark critical points
    for cp in critical_points:
        if x_range[0] <= cp <= x_range[1]:
            cp_value = numerical_func(cp)
            second_val = float(second_deriv.subs(x, cp))

            if second_val > 0:
                color = 'green'
                marker = 'v'
                label = f'Min at x={cp:.2f}'
            elif second_val < 0:
                color = 'red'
                marker = '^'
                label = f'Max at x={cp:.2f}'
            else:
                color = 'yellow'
                marker = 'o'
                label = f'Inflection at x={cp:.2f}'

            plt.plot(cp, cp_value, marker, color=color, markersize=15,
                    label=label, markeredgecolor='black', markeredgewidth=2)

    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title(title)
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.show()

# Treasure hill example
x = symbols('x')
hill = -x**2 + 6*x - 5
visualize_optimization(hill, [0, 6], 'Treasure Hill: f(x) = -x² + 6x - 5')

# Wavy ocean example
wave = x**4 - 8*x**2 + 10
visualize_optimization(wave, [-3, 3], 'Ocean Waves: f(x) = x⁴ - 8x² + 10')
```

### Real Application: Maximizing Profit

```python exec
id: 01-derivatives-at-sea-19
print("Pirate Ship Profit Optimization")
print("=" * 60)
print()
print("A pirate captain sells x crates of rum per voyage.")
print("Revenue: R(x) = 50x - 0.5x² doubloons")
print("Cost: C(x) = 100 + 10x doubloons")
print("Profit: P(x) = R(x) - C(x) = -0.5x² + 40x - 100")
print()

x = symbols('x')
profit = -0.5*x**2 + 40*x - 100

# Find maximum profit
profit_deriv = diff(profit, x)
print(f"Profit function: P(x) = {profit}")
print(f"Derivative: P'(x) = {profit_deriv}")
print()

from sympy import solve
optimal_quantity = solve(profit_deriv, x)[0]
max_profit = profit.subs(x, optimal_quantity)

print(f"Optimal quantity: {optimal_quantity} crates")
print(f"Maximum profit: {max_profit} doubloons")
print()

# Visualize
visualize_optimization(profit, [0, 80], 'Profit Optimization')

print("\nConclusion: Sell 40 crates per voyage for maximum profit of 700 doubloons!")
```

### Your turn 4.1: Optimization Problems

```python exec
id: 01-derivatives-at-sea-20
# Problem 1: Cannon Range
# The range of a cannon is R(θ) = v² sin(2θ) / g
# Where v = initial velocity, θ = angle, g = gravity
# For v = 50 m/s and g = 10 m/s², find the angle that maximizes range
# Hint: The optimal angle should be 45°

# Problem 2: Treasure Chest Dimensions
# A chest has fixed volume 1000 cubic units
# Surface area SA(x) = 2x² + 4000/x where x is side length
# Find dimensions that minimize material (surface area)

# Problem 3: Ship Speed vs Fuel Cost
# Cost per hour: C(v) = 100 + 2v² where v = speed in knots
# For a 120 nautical mile journey, find speed that minimizes total cost
# Hint: Total cost = C(v) × time = C(v) × (120/v)

# Problem 4: Lighthouse Beam
# Intensity I(x) = 1000/(x² + 4) where x is distance from lighthouse
# Where is intensity changing most rapidly? (Find where |I'(x)| is maximum)
```

---
## Part 5: Higher-Order Derivatives and Applications
### Second Derivatives: Concavity and Acceleration

```python exec
id: 01-derivatives-at-sea-21
def visualize_concavity():
    """
    Show relationship between function, first derivative, and second derivative.
    """
    x = symbols('x')
    func = x**4 - 4*x**3

    first = diff(func, x)
    second = diff(first, x)

    from sympy import lambdify
    f = lambdify(x, func, 'numpy')
    fp = lambdify(x, first, 'numpy')
    fpp = lambdify(x, second, 'numpy')

    x_vals = np.linspace(-1, 4, 400)

    fig, axes = plt.subplots(3, 1, figsize=(12, 10))

    # Function
    axes[0].plot(x_vals, f(x_vals), 'b-', linewidth=2)
    axes[0].axhline(y=0, color='k', linewidth=0.5)
    axes[0].axvline(x=0, color='k', linewidth=0.5)
    axes[0].set_ylabel('f(x)')
    axes[0].set_title(f'Function: f(x) = {func}')
    axes[0].grid(True, alpha=0.3)

    # First derivative
    axes[1].plot(x_vals, fp(x_vals), 'r-', linewidth=2)
    axes[1].axhline(y=0, color='k', linewidth=0.5)
    axes[1].axvline(x=0, color='k', linewidth=0.5)
    axes[1].set_ylabel("f'(x)")
    axes[1].set_title(f"First Derivative: f'(x) = {first}")
    axes[1].grid(True, alpha=0.3)
    axes[1].fill_between(x_vals, 0, fp(x_vals), where=(fp(x_vals)>0),
                         alpha=0.3, color='green', label='f increasing')
    axes[1].fill_between(x_vals, 0, fp(x_vals), where=(fp(x_vals)<0),
                         alpha=0.3, color='red', label='f decreasing')
    axes[1].legend()

    # Second derivative
    axes[2].plot(x_vals, fpp(x_vals), 'purple', linewidth=2)
    axes[2].axhline(y=0, color='k', linewidth=0.5)
    axes[2].axvline(x=0, color='k', linewidth=0.5)
    axes[2].set_xlabel('x')
    axes[2].set_ylabel("f''(x)")
    axes[2].set_title(f"Second Derivative: f''(x) = {second}")
    axes[2].grid(True, alpha=0.3)
    axes[2].fill_between(x_vals, 0, fpp(x_vals), where=(fpp(x_vals)>0),
                         alpha=0.3, color='blue', label='concave up')
    axes[2].fill_between(x_vals, 0, fpp(x_vals), where=(fpp(x_vals)<0),
                         alpha=0.3, color='orange', label='concave down')
    axes[2].legend()

    plt.tight_layout()
    plt.show()

    print("Key Observations:")
    print("- Where f'(x) = 0, f(x) has a critical point")
    print("- Where f'(x) > 0, f(x) is increasing")
    print("- Where f'(x) < 0, f(x) is decreasing")
    print("- Where f''(x) > 0, f(x) is concave up (cup shape)")
    print("- Where f''(x) < 0, f(x) is concave down (cap shape)")
    print("- Where f''(x) = 0, there may be an inflection point")

visualize_concavity()
```

### Physical Interpretation: Position, Velocity, Acceleration

```python exec
id: 01-derivatives-at-sea-22
print("Ship Motion Analysis")
print("=" * 60)
print()

t = symbols('t')
position = t**3 - 6*t**2 + 9*t

velocity = diff(position, t)
acceleration = diff(velocity, t)

print(f"Position: s(t) = {position} nautical miles")
print(f"Velocity: v(t) = s'(t) = {velocity} nm/hr")
print(f"Acceleration: a(t) = v'(t) = s''(t) = {acceleration} nm/hr²")
print()

from sympy import lambdify
s = lambdify(t, position, 'numpy')
v = lambdify(t, velocity, 'numpy')
a = lambdify(t, acceleration, 'numpy')

time_vals = np.linspace(0, 5, 200)

fig, axes = plt.subplots(3, 1, figsize=(12, 10))

axes[0].plot(time_vals, s(time_vals), 'b-', linewidth=2)
axes[0].set_ylabel('Position (nm)')
axes[0].set_title('Position vs Time')
axes[0].grid(True, alpha=0.3)

axes[1].plot(time_vals, v(time_vals), 'r-', linewidth=2)
axes[1].axhline(y=0, color='k', linewidth=0.5, linestyle='--')
axes[1].set_ylabel('Velocity (nm/hr)')
axes[1].set_title('Velocity vs Time (1st derivative)')
axes[1].grid(True, alpha=0.3)

axes[2].plot(time_vals, a(time_vals), 'purple', linewidth=2)
axes[2].axhline(y=0, color='k', linewidth=0.5, linestyle='--')
axes[2].set_xlabel('Time (hours)')
axes[2].set_ylabel('Acceleration (nm/hr²)')
axes[2].set_title('Acceleration vs Time (2nd derivative)')
axes[2].grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

# Find when ship is at rest
from sympy import solve
rest_times = solve(velocity, t)
print(f"\nShip at rest (v=0) at t = {rest_times}")

# Find when acceleration is zero
zero_accel = solve(acceleration, t)
print(f"Zero acceleration at t = {zero_accel}")
```

---
## Part 6: Gradient Descent Preview
### Using Derivatives for Optimization Algorithms

Gradient descent is a fundamental algorithm in machine learning. It uses derivatives to find minima iteratively.

```python exec
id: 01-derivatives-at-sea-23
def gradient_descent_1d(function, derivative, initial_x, learning_rate=0.1,
                        num_iterations=50, tolerance=1e-6):
    """
    Implement gradient descent to find minimum of a 1D function.

    Args:
        function: Function to minimize
        derivative: Derivative of the function
        initial_x: Starting point
        learning_rate: Step size
        num_iterations: Maximum iterations
        tolerance: Stop if change is smaller than this

    Returns:
        History of x values, History of function values
    """
    x_current = initial_x
    x_history = [x_current]
    f_history = [function(x_current)]

    for iteration in range(num_iterations):
        # Compute gradient (derivative)
        gradient = derivative(x_current)

        # Update x by moving in opposite direction of gradient
        x_new = x_current - learning_rate * gradient

        # Check convergence
        if abs(x_new - x_current) < tolerance:
            print(f"Converged after {iteration + 1} iterations")
            break

        x_current = x_new
        x_history.append(x_current)
        f_history.append(function(x_current))

    return np.array(x_history), np.array(f_history)

# Example: Minimize f(x) = x² - 4x + 7
def quadratic(x):
    return x**2 - 4*x + 7

def quadratic_derivative(x):
    return 2*x - 4

# Run gradient descent from x=10
x_hist, f_hist = gradient_descent_1d(quadratic, quadratic_derivative,
                                     initial_x=10, learning_rate=0.3)

# Visualize
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

# Left plot: Function and path
x_plot = np.linspace(-1, 11, 200)
y_plot = quadratic(x_plot)

ax1.plot(x_plot, y_plot, 'b-', linewidth=2, label='f(x) = x² - 4x + 7')
ax1.plot(x_hist, f_hist, 'ro-', markersize=6, linewidth=1.5, label='Gradient descent path')
ax1.plot(x_hist[0], f_hist[0], 'gs', markersize=12, label='Start')
ax1.plot(x_hist[-1], f_hist[-1], 'r*', markersize=15, label='End (minimum)')
ax1.set_xlabel('x')
ax1.set_ylabel('f(x)')
ax1.set_title('Gradient Descent: Finding Minimum')
ax1.legend()
ax1.grid(True, alpha=0.3)

# Right plot: Convergence
ax2.plot(f_hist, 'r-o', linewidth=2, markersize=5)
ax2.set_xlabel('Iteration')
ax2.set_ylabel('f(x)')
ax2.set_title('Convergence: Function Value vs Iteration')
ax2.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

print(f"\nStarting point: x = {x_hist[0]:.4f}, f(x) = {f_hist[0]:.4f}")
print(f"Ending point: x = {x_hist[-1]:.4f}, f(x) = {f_hist[-1]:.4f}")
print(f"Analytical minimum: x = 2, f(x) = 3")
print(f"\nGradient descent found the minimum in {len(x_hist)} steps!")
```

### Your turn 6.1: Implement Gradient Descent

```python exec
id: 01-derivatives-at-sea-24
# Challenge: Use gradient descent to minimize f(x) = x⁴ - 4x² + 2x

# 1. Define the function and its derivative

# 2. Run gradient descent from x = -2 with learning_rate = 0.1

# 3. Visualize the path on the function plot

# 4. Try different learning rates (0.01, 0.1, 0.5, 1.0)
#    What happens if the learning rate is too large?

# 5. This function has multiple local minima.
#    Try different starting points. Do you always reach the same minimum?
```

---
## Summary and Next Steps

**What You've Mastered:**
- Derivatives as rates of change
- Numerical differentiation (forward, backward, central)
- Symbolic differentiation with SymPy
- Finding maxima and minima
- Second derivatives and concavity
- Gradient descent basics

**Key Connections:**
- **Physics**: position → velocity → acceleration
- **Economics**: cost → marginal cost, revenue → marginal revenue
- **Optimization**: finding best solutions
- **Machine Learning**: gradient descent, backpropagation

**When to Use Each Method:**

| Method | Use When | Pros | Cons |
|--------|----------|------|------|
| **Numerical** | Only have data points | Works for any function | Approximate, sensitive to noise |
| **Symbolic** | Have formula | Exact answer | Need explicit formula |
| **Graphical** | Need intuition | Visual understanding | Not precise |

**Next Topics:**
- Integration (area under curves)
- Partial derivatives (functions of multiple variables)
- Optimization in higher dimensions
- Differential equations
- Taylor series approximations

**Applications in Computing:**
- Neural network training (backpropagation uses derivatives!)
- Computer graphics (curves and surfaces)
- Game physics (motion and collisions)
- Image processing (edge detection)
- Robotics (control systems)

You now have the calculus foundation for advanced computational methods!

## What we set out to do

These were the aims of this notebook. Now that you have worked through it, they are a check on what happened rather than a promise about it.

- Understand derivatives as rates of change
- Visualize derivatives using graphs
- Compute derivatives numerically (approximation)
- Compute derivatives symbolically (exact)
- Apply derivatives to optimization problems
- Connect calculus to real-world scenarios

## Looking back

Before leaving this page, a sentence on each. What you write stays on this device.

```reflect
- Something you expected before running a cell that turned out differently
- The one idea from this page you could explain to someone else now
- Something you would change or try next, if there were time
- A question this page raised for you that it did not answer. Bring it to the next session; these questions are where the next session starts.
```
