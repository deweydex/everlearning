---
title: "Calculus at Sea: Integrals and Accumulation"
slug: 02-integrals-at-sea
course: ai-and-ml-foundations
course_title: "AI and ML Foundations"
series: 2-calculus
series_title: "Calculus"
version: 2026.09.06.1
---

# Calculus at Sea: Integrals and Accumulation
## From a Speed Log to the Distance Travelled


**The Navigator's Second Question:**

In *Derivatives and Optimization* we asked how fast the ship was moving at each moment. The log now holds those speeds, one reading every hour. The captain asks the opposite question: given all those speeds, how far did we travel? A derivative takes a position and gives a rate. An *integral* takes a rate and gives back the total. This notebook is about the second direction.

```python exec
id: 02-integrals-at-sea-1
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

# The ship's speed in knots, one reading each hour for twelve hours
hours = np.arange(0, 13)
speeds = np.array([4.0, 5.5, 6.8, 7.4, 7.0, 6.1, 5.2, 4.9, 5.6, 6.9, 7.8, 7.5, 6.2])

fig, ax = plt.subplots(figsize=(9, 4))
ax.plot(hours, speeds, "o-", label="speed (knots)")
ax.set_xlabel("hour"); ax.set_ylabel("knots"); ax.set_title("The speed log")
ax.grid(alpha=0.3); ax.legend()
```

## Part 1: Distance Is Speed Times Time, Added Up

### The Simplest Estimate

If the ship held a steady 4 knots for the first hour, it covered 4 nautical miles in that hour. If it then held 5.5 knots for the second hour, that is 5.5 more. Adding the twelve hourly readings, one per hour, gives an estimate of the whole voyage. Let's compute it, and draw what we are adding.

```python exec
id: 02-integrals-at-sea-2
hour_length = 1.0
distance_estimate = sum(speeds[:-1] * hour_length)   # use each hour's opening speed
print(f"Estimated distance: {distance_estimate:.1f} nautical miles")

fig, ax = plt.subplots(figsize=(9, 4))
ax.bar(hours[:-1], speeds[:-1], width=1.0, align="edge", alpha=0.4, label="one hour at the opening speed")
ax.plot(hours, speeds, "o-", color="black", label="speed log")
ax.set_xlabel("hour"); ax.set_ylabel("knots"); ax.set_title("Each bar is a distance: speed x one hour")
ax.legend(); ax.grid(alpha=0.3)
```

Every bar has a width of one hour and a height of one speed, so its area is a distance. The total distance is the total area of the bars. That sentence is the whole idea of an integral: **the area under a rate curve is the accumulated total**.

The estimate is rough, because the ship did not hold each hour's opening speed for the whole hour. The next part makes the pieces smaller.

### Your turn 1.1

The estimate above used each hour's *opening* speed. Recompute it using each hour's *closing* speed (`speeds[1:]`), and then the *average* of the two. Which of the three do you trust most, and why?

```python exec
id: 02-integrals-at-sea-3
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
# Your code here
```

## Part 2: Numerical Integration: Smaller Pieces, Better Answers

### A Smooth Speed

To see how an approximation improves, we need the true speed at every instant, not just on the hour. Suppose the speed followed the smooth curve below (in knots, with time in hours). We will estimate the area under it with rectangles of shrinking width and watch the estimates settle.

```python exec
id: 02-integrals-at-sea-4
def speed(t):
    '''A smooth model of the ship's speed at time t (hours).'''
    return 6 + 2 * np.sin(t / 2) - 0.1 * t

def left_rectangles(f, a, b, n):
    '''Area under f from a to b using n rectangles, each at the left-hand height.'''
    width = (b - a) / n
    lefts = a + width * np.arange(n)
    return np.sum(f(lefts) * width)

for n in (4, 12, 48, 192, 768):
    print(f"{n:4d} rectangles -> {left_rectangles(speed, 0, 12, n):.4f} nautical miles")
```

As the rectangles get narrower the estimates stop changing in the early digits. The number they settle on is the *definite integral* of the speed from hour 0 to hour 12, written

$$\int_0^{12} \text{speed}(t)\, dt .$$

The tall S is a stretched letter S for "sum", the $dt$ is the width of a piece, and the limits 0 and 12 are where the adding starts and stops. Reading it as "add up speed times a small bit of time, from 0 to 12" is exactly right.

### Visualizing the Approximation

```python exec
id: 02-integrals-at-sea-5
t = np.linspace(0, 12, 400)
fig, axes = plt.subplots(1, 3, figsize=(14, 4), sharey=True)
for ax, n in zip(axes, (4, 12, 48)):
    width = 12 / n
    lefts = width * np.arange(n)
    ax.bar(lefts, speed(lefts), width=width, align="edge", alpha=0.4)
    ax.plot(t, speed(t), color="black")
    ax.set_title(f"{n} rectangles: {left_rectangles(speed, 0, 12, n):.3f}")
    ax.set_xlabel("hour")
axes[0].set_ylabel("knots")
```

### Your turn 2.1: Two Better Rules

Left-hand rectangles undershoot where the curve rises and overshoot where it falls. Two small changes fix most of that. The *midpoint rule* measures each rectangle at its centre. The *trapezoid rule* joins the left and right heights with a straight line, so each piece is a trapezoid with area $\tfrac{1}{2}(f_{\text{left}} + f_{\text{right}}) \cdot \text{width}$.

Implement both, and compare all three rules at `n = 12`. Which gets closest to the 768-rectangle answer from above?

```python exec
id: 02-integrals-at-sea-6
know: at `n = 12`, the midpoint rule gives 64.961 and the trapezoid rule 64.956; the left-rectangle rule gave 65.835. The exact value, from Part 3, is 64.959.
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
def midpoint_rule(f, a, b, n):
    # Your code here
    pass

def trapezoid_rule(f, a, b, n):
    # Your code here
    pass
```

## Part 3: Symbolic Integrals: Let SymPy Do the Algebra

### Exact Answers

Just as SymPy can differentiate a formula exactly, it can integrate one. The function is `sp.integrate`. Given a formula alone it returns the *antiderivative*, a formula whose derivative is the one you started with. Given limits, it returns the definite integral as a number.

```python exec
id: 02-integrals-at-sea-7
t_sym = sp.symbols("t")
speed_sym = 6 + 2 * sp.sin(t_sym / 2) - sp.Rational(1, 10) * t_sym

antiderivative = sp.integrate(speed_sym, t_sym)
exact = sp.integrate(speed_sym, (t_sym, 0, 12))

print("speed(t)          =", speed_sym)
print("antiderivative    =", antiderivative)
print("exact distance    =", exact, "=", float(exact))
print("768 rectangles    =", round(left_rectangles(speed, 0, 12, 768), 4))
```

The numerical estimate and the exact answer differ by about a hundredth of a mile, and the exact one has no `n` to choose. That is the trade the previous notebook described in the other direction: numerical methods work on any function, including a table of measurements, while symbolic methods need a formula and repay it with an exact answer.

### Common Integration Rules Demonstrated

The power rule for derivatives brought a power down by one. Integration puts it back up by one, and divides by the new power.

```python exec
id: 02-integrals-at-sea-8
x = sp.symbols("x")
for expression in (x**2, x**3, sp.sqrt(x), sp.exp(x), sp.sin(x), 1 / x):
    print(f"integral of {str(expression):8} = {sp.integrate(expression, x)}")
```

### Your turn 3.1

Find the antiderivative of $3x^2 - 4x + 5$ by hand using the rule above, then check it with SymPy. Then differentiate your answer with `sp.diff` and confirm you get the original back. What happened to the constant 5, and what would have happened to a constant added to your antiderivative?

```python exec
id: 02-integrals-at-sea-9
know: SymPy gives `x**3 - 2*x**2 + 5*x`, and differentiating it returns `3*x**2 - 4*x + 5`. The constant 5 came back; a constant added to your antiderivative would vanish on differentiating, which is why an antiderivative is only ever known up to a constant.
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
# Your code here
```

## Part 4: The Fundamental Theorem: Integration Undoes Differentiation

### One Idea, Two Directions

The exercise you just did is the most important fact in calculus, and it deserves a plain statement. If you integrate a rate you get a total, and if you differentiate that total you get the rate back. The two operations undo each other, in the way that adding and subtracting do. Let's see it numerically, with no symbols at all.

```python exec
id: 02-integrals-at-sea-10
# Accumulate distance hour by hour with fine rectangles, then differentiate the running total
fine_t = np.linspace(0, 12, 1201)
width = fine_t[1] - fine_t[0]
running_distance = np.cumsum(speed(fine_t) * width)          # the integral, as a running total
recovered_speed = np.gradient(running_distance, width)        # the derivative of that total

fig, axes = plt.subplots(1, 2, figsize=(12, 4))
axes[0].plot(fine_t, running_distance); axes[0].set_title("running total: distance so far")
axes[0].set_xlabel("hour"); axes[0].set_ylabel("nautical miles")
axes[1].plot(fine_t, speed(fine_t), label="speed(t)")
axes[1].plot(fine_t, recovered_speed, "--", label="derivative of the running total")
axes[1].set_title("differentiating the total gives the rate back")
axes[1].set_xlabel("hour"); axes[1].set_ylabel("knots"); axes[1].legend()
print(f"largest gap between the two curves: {np.max(np.abs(speed(fine_t) - recovered_speed)):.4f} knots")
```

The dashed line sits on top of the original speed. `np.cumsum` built the integral piece by piece, `np.gradient` took the derivative, and the two cancelled. On paper the same statement is

$$\frac{d}{dt}\int_0^t \text{speed}(u)\, du = \text{speed}(t),$$

and it is why the symbolic method in Part 3 works at all: to integrate a function, find something whose derivative it is.

### Your turn 4.1

The reverse direction: differentiate `running_distance` was one way round. Now start from the derivative. Take `speed(fine_t)`, integrate it with `np.cumsum` as above, and check that the value at hour 12 matches the exact distance from Part 3. Then explain in one sentence why the running total starts at zero.

```python exec
id: 02-integrals-at-sea-11
know: the running total at hour 12 is within a few hundredths of 64.959.
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
# Your code here
```

## Part 5: Probability Is an Area

### Where This Meets Part 3 of the Course

In *Continuous Distributions* a probability was the area under a density curve between two values. That is an integral, and now you can compute one. The *uniform* distribution on 0 to 10 has a flat density of $\tfrac{1}{10}$, so the whole area is 1, as every probability distribution's must be. The probability of landing between 2 and 5 is the area of that strip.

```python exec
id: 02-integrals-at-sea-12
u = sp.symbols("u")
density = sp.Rational(1, 10)

whole_area = sp.integrate(density, (u, 0, 10))
between_2_and_5 = sp.integrate(density, (u, 2, 5))
expected_value = sp.integrate(u * density, (u, 0, 10))

print("total area under the density  =", whole_area)
print("P(2 <= U <= 5)                =", between_2_and_5)
print("expected value  E[U]          =", expected_value)
```

The last line is new. The *expected value* of a continuous quantity is $\int x\, f(x)\, dx$: each value, weighted by how likely it is, added up. For the uniform distribution it lands in the middle, which is what intuition says. In Part 3 you met expected value as a sum over a discrete distribution; this is the same idea with the sum replaced by an integral.

### The Bell Curve, Numerically

The normal distribution's density has no elementary antiderivative, so the symbolic route gives up and the numerical one is what everybody uses. Let's confirm the rule that about 68 percent of a normal distribution lies within one standard deviation of its mean.

```python exec
id: 02-integrals-at-sea-13
def normal_density(z):
    return np.exp(-z**2 / 2) / np.sqrt(2 * np.pi)

within_one = left_rectangles(normal_density, -1, 1, 2000)
within_two = left_rectangles(normal_density, -2, 2, 2000)
print(f"P(-1 <= Z <= 1) = {within_one:.4f}")
print(f"P(-2 <= Z <= 2) = {within_two:.4f}")

z = np.linspace(-4, 4, 400)
fig, ax = plt.subplots(figsize=(8, 4))
ax.plot(z, normal_density(z), color="black")
mask = (z >= -1) & (z <= 1)
ax.fill_between(z[mask], normal_density(z[mask]), alpha=0.4, label=f"area = {within_one:.3f}")
ax.set_title("A probability is an area under the density"); ax.legend()
```

### Your turn 5.1

A model reports that a measurement error follows the normal density above. Using `left_rectangles`, find the probability that the error is larger than 1.5 in either direction (that is, the area outside $-1.5$ to $1.5$). Remember that the whole area is 1.

```python exec
id: 02-integrals-at-sea-14
know: about 0.134, or a little over 13 percent.
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
# Your code here
```

## Part 6: Where Integrals Appear in Machine Learning

You will not often write `sp.integrate` in a machine learning program, and you will constantly use what it means. A *mean loss* over a dataset is a sum of small pieces divided by how many there are, which is an integral over the data with the width factored out. A model's *expected* error is an integral of the loss against the distribution of inputs, and the training set is the rectangle approximation to it. A *probability* that a network reports is an area under some density it has learned. Every time you average, you are integrating with a coarse `n`, and the lesson of Part 2 applies: more pieces, better estimate.

### Your turn 6.1

Take the squared-error loss $L(w) = (w - 3)^2$ from *Learning a Line*. Its average over all values of $w$ between 0 and 6 is $\tfrac{1}{6}\int_0^6 (w-3)^2\, dw$. Compute it symbolically and numerically, and compare it with the loss at the best $w$. What does the difference tell you about how far a random starting guess usually is from the bottom of the bowl?

```python exec
id: 02-integrals-at-sea-15
know: the average loss is exactly 3, and the loss at the best $w$ is 0. A random start is, on average, three units of loss above the bottom of the bowl.
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
# Your code here
```

---
## Summary and Next Steps

**What You've Mastered:**
- An integral as accumulation, and the area under a rate curve as a total
- Rectangle, midpoint and trapezoid rules, and how they converge
- Exact integrals and antiderivatives with SymPy
- The fundamental theorem: integration and differentiation undo each other
- Probability and expected value as integrals

**Key Connections:**
- **Physics**: speed integrates to distance; acceleration integrates to speed
- **Probability**: a density integrates to a probability; $x\,f(x)$ integrates to an expected value
- **Machine learning**: every average is a coarse integral; expected loss is the integral training approximates

**When to Use Each Method:**

| Method | Use When | Pros | Cons |
|--------|----------|------|------|
| **Numerical** | You have data, or a density with no formula | Works on anything | Approximate; choose `n` |
| **Symbolic** | You have a formula SymPy can handle | Exact | Many functions have no closed form |

**Next**: *Learning a Line* uses the derivative side of this pair to walk downhill on a loss. When you meet the mean squared error there, you will be looking at Part 6 of this notebook.

## What we set out to do

These were the aims of this notebook. Now that you have worked through it, they are a check on what happened rather than a promise about it.

- Understand an integral as accumulation: adding up many small pieces
- Approximate an integral numerically with rectangles and trapezoids, and watch the approximation settle
- Compute integrals exactly with SymPy
- See that integration undoes differentiation, and why that matters
- Read a probability as an area under a curve, which is how Part 3's continuous distributions work

## Looking back

Before leaving this page, a sentence on each. What you write stays on this device.

```reflect
- Something you expected before running a cell that turned out differently
- The one idea from this page you could explain to someone else now
- Something you would change or try next, if there were time
- A question this page raised for you that it did not answer. Bring it to the next session; these questions are where the next session starts.
```
