---
title: "Part 2: Exploring the Dot Product and Vector Relationships"
slug: 02-dot-product-and-projections
course: ai-and-ml-foundations
course_title: "AI and ML Foundations"
series: 1-linear-algebra
series_title: "Linear Algebra"
version: 2026.09.06.1
---

# Part 2: Exploring the Dot Product and Vector Relationships

Welcome back! In our first notebook, we discovered how to represent vectors as lists and visualize them as arrows. We learned to add vectors and scale them.

Today, we're going to explore a fascinating operation called the **dot product**. It might seem mysterious at first, but through experimentation, we'll uncover what it tells us about the relationship between vectors.

## Setting Up

First, let's import our tools and bring back the functions we created last time:

```python exec
id: 02-dot-product-and-projections-1
import matplotlib.pyplot as plt
import math  # We'll need this for some calculations

# Let's redefine our helper functions from last time
def draw_vector(vector, color='blue', label=None):
    """Draw a vector as an arrow from the origin."""
    x, y = vector[0], vector[1]
    plt.arrow(0, 0, x, y, head_width=0.3, head_length=0.3, 
              fc=color, ec=color, linewidth=2)
    if label:
        plt.text(x*0.5, y*0.5, label, fontsize=12)

def setup_plot(x_range=10, y_range=10):
    """Set up a coordinate system for drawing vectors."""
    plt.figure(figsize=(8, 8))
    plt.axhline(y=0, color='k', linewidth=0.5)
    plt.axvline(x=0, color='k', linewidth=0.5)
    plt.xlim(-x_range, x_range)
    plt.ylim(-y_range, y_range)
    plt.grid(True, alpha=0.3)
    plt.gca().set_aspect('equal')
    plt.xlabel('x', fontsize=12)
    plt.ylabel('y', fontsize=12)

def add_vectors(v1, v2):
    """Add two vectors component-wise."""
    return [v1[0] + v2[0], v1[1] + v2[1]]

def scale_vector(scalar, vector):
    """Multiply a vector by a scalar."""
    return [scalar * vector[0], scalar * vector[1]]
```

## The Dot Product: A New Kind of Multiplication

When we multiply a vector by a number (scalar multiplication), we get another vector. But there's another way to "multiply" vectors that gives us a single number instead. It's called the **dot product** or **inner product**.

Here's how it works: we multiply corresponding components and then add them all up.

```python exec
id: 02-dot-product-and-projections-2
def dot_product(v1, v2):
    """
    Calculate the dot product of two vectors.
    
    The dot product is: v1[0]*v2[0] + v1[1]*v2[1]
    
    Parameters:
    - v1: first vector [x1, y1]
    - v2: second vector [x2, y2]
    
    Returns:
    - a single number (not a vector!)
    """
    return v1[0] * v2[0] + v1[1] * v2[1]
```

Let's try it out:

```python exec
id: 02-dot-product-and-projections-3
a = [3, 4]
b = [2, 1]

result = dot_product(a, b)
print(f"a = {a}")
print(f"b = {b}")
print(f"a · b = {result}")
print(f"\nBreaking it down: ({a[0]} × {b[0]}) + ({a[1]} × {b[1]}) = {a[0]*b[0]} + {a[1]*b[1]} = {result}")
```

## What Does This Number Mean?

The dot product gives us a single number, but what does it tell us? Let's investigate by computing dot products for vectors in different configurations.

### Experiment 1: Vectors Pointing in Similar Directions

```python exec
id: 02-dot-product-and-projections-4
# Two vectors pointing in roughly the same direction
v1 = [3, 2]
v2 = [4, 3]

setup_plot(5, 5)
draw_vector(v1, color='blue', label='v1')
draw_vector(v2, color='red', label='v2')
plt.title(f'Dot product: {dot_product(v1, v2)}')
plt.show()
```

### Experiment 2: Vectors Pointing in Perpendicular Directions

```python exec
id: 02-dot-product-and-projections-5
# Two perpendicular vectors
v1 = [3, 0]  # pointing right
v2 = [0, 3]  # pointing up

setup_plot(5, 5)
draw_vector(v1, color='blue', label='v1')
draw_vector(v2, color='red', label='v2')
plt.title(f'Dot product: {dot_product(v1, v2)}')
plt.show()

# Let's try another pair of perpendicular vectors
v3 = [2, 3]
v4 = [-3, 2]  # This is perpendicular to v3!

setup_plot(5, 5)
draw_vector(v3, color='blue', label='v3')
draw_vector(v4, color='red', label='v4')
plt.title(f'Dot product: {dot_product(v3, v4)}')
plt.show()
```

### Experiment 3: Vectors Pointing in Opposite Directions

```python exec
id: 02-dot-product-and-projections-6
# Two vectors pointing in opposite directions
v1 = [3, 2]
v2 = [-3, -2]

setup_plot(5, 5)
draw_vector(v1, color='blue', label='v1')
draw_vector(v2, color='red', label='v2')
plt.title(f'Dot product: {dot_product(v1, v2)}')
plt.show()
```

## What Patterns Are Emerging?

Look at the dot products we calculated:
- When vectors point in similar directions, what sign is the dot product?
- When vectors are perpendicular, what is the dot product?
- When vectors point in opposite directions, what sign is the dot product?

**Your investigation:** Try creating your own pairs of vectors and calculating their dot products. Can you find patterns between the angle between vectors and the value of their dot product?

```python exec
id: 02-dot-product-and-projections-7
# Try your own examples here:
```

## A Useful Function: Vector Length

Before we go further, let's create a function to calculate how long a vector is. We can use the Pythagorean theorem: if a vector is [x, y], its length is √(x² + y²).

```python exec
id: 02-dot-product-and-projections-8
def vector_length(v):
    """
    Calculate the length (magnitude) of a vector.
    
    Length = √(x² + y²)
    
    Parameters:
    - v: a vector [x, y]
    
    Returns:
    - the length as a number
    """
    return math.sqrt(v[0]**2 + v[1]**2)

# Test it out
v = [3, 4]
print(f"Vector {v} has length {vector_length(v)}")
print(f"Check: 3² + 4² = {3**2 + 4**2}, and √25 = {math.sqrt(25)}")
```

## A Beautiful Connection

Here's something remarkable: we can use the dot product to find the length of a vector!

What happens if we take the dot product of a vector with itself?

```python exec
id: 02-dot-product-and-projections-9
v = [3, 4]

dot_with_self = dot_product(v, v)
length = vector_length(v)
length_squared = length ** 2

print(f"Vector: {v}")
print(f"v · v = {dot_with_self}")
print(f"Length of v = {length}")
print(f"Length squared = {length_squared}")
print(f"\nNotice: v · v = length²!")
```

**Why does this work?** Let's think about it:
- v · v = v[0]×v[0] + v[1]×v[1] = v[0]² + v[1]²
- Length = √(v[0]² + v[1]²)
- So v · v = (Length)²

Try this with different vectors to verify it works!

```python exec
id: 02-dot-product-and-projections-10
# Test with your own vectors:
```

## Finding Perpendicular Vectors

We discovered that when two vectors are perpendicular, their dot product is zero. Can we use this to create a function that finds a perpendicular vector?

Here's a neat trick: if we have a vector [x, y], then [-y, x] is perpendicular to it!

```python exec
id: 02-dot-product-and-projections-11
def perpendicular_vector(v):
    """
    Find a vector perpendicular to the given vector.
    
    If v = [x, y], then [-y, x] is perpendicular to v.
    
    Parameters:
    - v: a vector [x, y]
    
    Returns:
    - a perpendicular vector [-y, x]
    """
    return [-v[1], v[0]]

# Test it
v = [3, 2]
perp = perpendicular_vector(v)

print(f"Original vector: {v}")
print(f"Perpendicular vector: {perp}")
print(f"Their dot product: {dot_product(v, perp)}")
print(f"(Should be 0 if they're truly perpendicular!)")

# Visualize
setup_plot(5, 5)
draw_vector(v, color='blue', label='v')
draw_vector(perp, color='red', label='perpendicular to v')
plt.title('Perpendicular Vectors')
plt.show()
```

### Your Exploration

**Investigate:** 
- Does this always work? Try different vectors.
- What happens if you apply the perpendicular function twice? (That is, find the perpendicular of the perpendicular)
- Can you think of why [-y, x] is perpendicular to [x, y]? (Hint: calculate their dot product algebraically)

```python exec
id: 02-dot-product-and-projections-12
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
# Your investigations:
```

## Unit Vectors: Vectors of Length 1

Sometimes it's useful to have a vector that points in a particular direction but has exactly length 1. We call these **unit vectors**.

How do we create one? We divide each component by the vector's length!

```python exec
id: 02-dot-product-and-projections-13
def normalize_vector(v):
    """
    Create a unit vector (length 1) pointing in the same direction as v.
    
    We do this by dividing each component by the vector's length.
    
    Parameters:
    - v: a vector [x, y]
    
    Returns:
    - a unit vector pointing in the same direction
    """
    length = vector_length(v)
    
    # We need to avoid dividing by zero!
    if length == 0:
        return [0, 0]
    
    # Divide each component by the length
    return [v[0]/length, v[1]/length]

# Test it
v = [3, 4]
unit_v = normalize_vector(v)

print(f"Original vector: {v}")
print(f"Length: {vector_length(v)}")
print(f"\nUnit vector: {unit_v}")
print(f"Length of unit vector: {vector_length(unit_v)}")
```

```python exec
id: 02-dot-product-and-projections-14
# Visualize several vectors and their unit vectors
vectors = [[3, 4], [2, 1], [-2, 3], [1, -2]]

setup_plot(5, 5)

for v in vectors:
    unit = normalize_vector(v)
    draw_vector(v, color='lightblue')
    draw_vector(unit, color='darkblue', label=f'unit')

plt.title('Vectors (light blue) and Their Unit Vectors (dark blue)')
plt.show()
```

## An Interesting Challenge

Now that we have several tools, let's try something creative.

**Challenge:** Can you create a function that takes a vector and returns another vector that:
1. Is perpendicular to the original
2. Has length 1
3. Points "to the left" of the original vector (when you're looking along the vector's direction)

Hint: You can use the functions we've already written!

```python exec
id: 02-dot-product-and-projections-15
def perpendicular_unit_vector(v):
    """
    Create a unit vector perpendicular to v.
    
    Your solution here!
    """
    # Hint: Combine perpendicular_vector() and normalize_vector()
    pass  # Replace this with your solution

# Test it when you're ready
# v = [3, 4]
# perp_unit = perpendicular_unit_vector(v)
# print(f"Original: {v}")
# print(f"Perpendicular unit: {perp_unit}")
# print(f"Dot product (should be 0): {dot_product(v, perp_unit)}")
# print(f"Length (should be 1): {vector_length(perp_unit)}")
```

## Projection: How Much of One Vector Points in Another's Direction?

Here's a fascinating question: if we have two vectors, how much of one vector points in the direction of the other?

Imagine shining a light perpendicular to vector **b**. The shadow that vector **a** casts onto **b** is called the **projection** of **a** onto **b**.

We can calculate this using the dot product!

```python exec
id: 02-dot-product-and-projections-16
def project_onto(a, b):
    """
    Project vector a onto vector b.
    
    This gives us the component of a that points in b's direction.
    
    Formula: proj_b(a) = ((a · b) / (b · b)) * b
    
    Parameters:
    - a: the vector to project
    - b: the vector to project onto
    
    Returns:
    - the projection vector
    """
    # Calculate how much a points in b's direction
    dot_ab = dot_product(a, b)
    dot_bb = dot_product(b, b)
    
    # Avoid division by zero
    if dot_bb == 0:
        return [0, 0]
    
    # Scale b by the appropriate amount
    scalar = dot_ab / dot_bb
    return scale_vector(scalar, b)
```

```python exec
id: 02-dot-product-and-projections-17
# Let's visualize projection
def draw_projection(a, b):
    """Helper function to visualize projections."""
    proj = project_onto(a, b)
    
    setup_plot(6, 6)
    draw_vector(a, color='blue', label='a')
    draw_vector(b, color='red', label='b')
    draw_vector(proj, color='green', label='projection')
    
    # Draw a dashed line from a to its projection
    plt.plot([a[0], proj[0]], [a[1], proj[1]], 'k--', alpha=0.5, linewidth=1)
    
    plt.title('Projection of a onto b')
    plt.show()

# Example 1: Vectors at an angle
a = [3, 2]
b = [4, 1]
draw_projection(a, b)

# Example 2: What if the vectors are perpendicular?
a = [3, 0]
b = [0, 4]
draw_projection(a, b)

# Example 3: What if they point in the same direction?
a = [2, 1]
b = [4, 2]
draw_projection(a, b)
```

## Explore Projections

**Investigation time:**
- What happens to the projection when vectors are perpendicular?
- What happens when they point in the same direction?
- What happens when they point in opposite directions?
- Try projecting a long vector onto a short vector, then vice versa. What do you notice?

```python exec
id: 02-dot-product-and-projections-18
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
# Your explorations:
```

## A Creative Challenge: Breaking Vectors into Components

Here's a powerful idea: any vector can be written as the sum of two perpendicular components.

If we have vector **a** and we want to break it into:
- A part parallel to **b**
- A part perpendicular to **b**

We can use projection! The parallel part is the projection, and we can find the perpendicular part by subtraction.

```python exec
id: 02-dot-product-and-projections-19
def subtract_vectors(v1, v2):
    """
    Subtract v2 from v1.
    
    Parameters:
    - v1: first vector
    - v2: vector to subtract
    
    Returns:
    - v1 - v2
    """
    return [v1[0] - v2[0], v1[1] - v2[1]]

# Now let's decompose a vector
a = [5, 3]
b = [4, 1]

# The part of a parallel to b
parallel = project_onto(a, b)

# The part of a perpendicular to b
perpendicular = subtract_vectors(a, parallel)

print(f"Original vector a: {a}")
print(f"Parallel component: {parallel}")
print(f"Perpendicular component: {perpendicular}")
print(f"\nCheck: parallel + perpendicular = {add_vectors(parallel, perpendicular)}")
print(f"Does this equal a? {add_vectors(parallel, perpendicular) == a}")

# Visualize
setup_plot(6, 6)
draw_vector(a, color='blue', label='a')
draw_vector(b, color='red', label='b')
draw_vector(parallel, color='green', label='parallel')
draw_vector(perpendicular, color='purple', label='perpendicular')
plt.title('Decomposing a vector into parallel and perpendicular parts')
plt.show()
```

## A Thought Experiment

**Ponder this:** We've now built several operations:
- Addition and subtraction of vectors
- Scaling vectors
- Dot product
- Projection

Think about how these operations relate to each other. Can you express one operation in terms of others?

For example:
- We used the dot product to create projection
- We used projection and subtraction to decompose vectors

Try creating your own combinations and see what interesting new operations you can invent!

```python exec
id: 02-dot-product-and-projections-20
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
# Your creative combinations:
```

## Wrapping Up Part 2

Today we've discovered:

1. The **dot product** - a way to multiply vectors that gives us a number
2. The dot product tells us about the angle between vectors:
   - Positive: similar directions
   - Zero: perpendicular
   - Negative: opposite directions
3. We can use the dot product to:
   - Find the length of a vector (v · v = length²)
   - Create unit vectors (length 1)
   - Project one vector onto another
   - Decompose vectors into components

Our growing library of functions:
- `dot_product(v1, v2)`
- `vector_length(v)`
- `normalize_vector(v)`
- `perpendicular_vector(v)`
- `project_onto(a, b)`
- `subtract_vectors(v1, v2)`

In the next notebook, we'll extend these ideas to **matrices** - which are like vectors of vectors! We'll discover how matrix operations are built on everything we've learned so far.

## Looking back

Before leaving this page, a sentence on each. What you write stays on this device.

```reflect
- Something you expected before running a cell that turned out differently
- The one idea from this page you could explain to someone else now
- Something you would change or try next, if there were time
- A question this page raised for you that it did not answer. Bring it to the next session; these questions are where the next session starts.
```
