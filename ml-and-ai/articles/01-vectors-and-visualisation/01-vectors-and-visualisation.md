---
title: "Part 1: Discovering Vectors Through Lists and Pictures"
slug: 01-vectors-and-visualisation
course: ai-and-ml-foundations
course_title: "AI and ML Foundations"
series: 1-linear-algebra
series_title: "Linear Algebra"
version: 2026.09.06.1
---

# Part 1: Discovering Vectors Through Lists and Pictures

Welcome! In this series of notebooks, we're going to embark on a journey together. We'll start with simple ideas in Python and gradually build up our own library of tools for working with vectors and matrices. Along the way, we'll discover some beautiful mathematical patterns and see them come to life through visualizations.

 We'll take it step by step, and by the end, you'll have created something powerful from scratch.

## What We'll Explore Today

Today's adventure will take us through:
- Understanding what lists are in Python and how we can use them
- Discovering vectors (which turn out to be closely related to lists!)
- Learning to visualize vectors as arrows
- Exploring what happens when we combine vectors

Let's begin!

## Setting Up Our Tools

First, we need to import some tools that will help us draw pictures. Think of this as getting out our sketchbook and pencils before we start drawing.

The `matplotlib` library is what we'll use to create visualizations.

```python exec
id: 01-vectors-and-visualisation-1
# This imports the plotting library we'll use to visualize vectors
import matplotlib.pyplot as plt

# This line makes our plots appear right in the notebook

```

## Lists: Our Starting Point

In Python, a **list** is a way to store multiple values together. We create a list by putting values inside square brackets `[]`, separated by commas.

Let's start with something simple:

```python exec
id: 01-vectors-and-visualisation-2
# Here's a list with two numbers
my_first_list = [3, 4]

# We can print it to see what's inside
print(my_first_list)
```

We can access individual items in a list using their position (called an **index**). Python counts starting from 0, so the first item is at index 0, the second at index 1, and so on.

```python exec
id: 01-vectors-and-visualisation-3
# Get the first number (index 0)
first_number = my_first_list[0]
print("First number:", first_number)

# Get the second number (index 1)
second_number = my_first_list[1]
print("Second number:", second_number)
```

### Exploration Time

Let's play with lists for a moment. Try creating a few different lists and see what happens:

```python exec
id: 01-vectors-and-visualisation-4
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
# Try creating your own lists here. What happens if you:
# - Make a list with three numbers?
# - Use negative numbers?
# - Use decimal numbers (like 2.5)?

# Your experiments here:
```

## From Lists to Vectors

Now here's where things get interesting. A **vector** is essentially a list of numbers that we think about in a special way. Instead of just being numbers in a row, we can imagine a vector as an arrow pointing from the origin (0, 0) to a point in space.

For example, the list `[3, 4]` can be thought of as a vector that points 3 units in the x-direction and 4 units in the y-direction.

Let's create a function to visualize vectors. A **function** in Python is like a recipe – we define it once, and then we can use it many times.

```python exec
id: 01-vectors-and-visualisation-5
def draw_vector(vector, color='blue', label=None):
    """
    Draw a vector as an arrow from the origin to the point (vector[0], vector[1]).

    Parameters:
    - vector: a list with two numbers [x, y]
    - color: what color to draw the arrow (default is blue)
    - label: optional text to label the vector
    """
    # Get the x and y components from our vector
    x = vector[0]
    y = vector[1]

    # Draw an arrow from (0,0) to (x,y)
    # The arrow function takes: start_x, start_y, change_in_x, change_in_y
    plt.arrow(0, 0, x, y,
              head_width=0.3, head_length=0.3,
              fc=color, ec=color, linewidth=2)

    # If we provided a label, add it near the tip of the vector
    if label:
        plt.text(x*0.5, y*0.5, label, fontsize=12)

def setup_plot(x_range=10, y_range=10):
    """
    Set up a nice coordinate system for drawing vectors.

    Parameters:
    - x_range: how far to show on the x-axis (positive and negative)
    - y_range: how far to show on the y-axis (positive and negative)
    """
    plt.figure(figsize=(8, 8))

    # Draw axes
    plt.axhline(y=0, color='k', linewidth=0.5)
    plt.axvline(x=0, color='k', linewidth=0.5)

    # Set the range of the plot
    plt.xlim(-x_range, x_range)
    plt.ylim(-y_range, y_range)

    # Add grid to make it easier to read coordinates
    plt.grid(True, alpha=0.3)

    # Make sure the aspect ratio is equal (squares look like squares)
    plt.gca().set_aspect('equal')

    # Label our axes
    plt.xlabel('x', fontsize=12)
    plt.ylabel('y', fontsize=12)
```

Now let's use these functions to draw our first vector!

```python exec
id: 01-vectors-and-visualisation-6
# Create a vector
v = [3, 4]

# Set up our coordinate system
setup_plot()

# Draw the vector
draw_vector(v, color='blue', label='v')

# Display the plot
plt.title('Our First Vector!')
plt.show()

print(f"We drew a vector with components: x = {v[0]}, y = {v[1]}")
```

## Reflection Point

Take a moment to think about what you're seeing. The arrow starts at the origin (0, 0) and points to the location (3, 4).

**Question to ponder:** If we think of the tip of the arrow as a destination, what does the arrow itself tell us? What if we started from a different point – would the arrow look the same?

(There are no wrong answers here – just think about what makes sense to you!)

## Playing with Different Vectors

Let's draw several vectors and see what patterns we notice:

```python exec
id: 01-vectors-and-visualisation-7
# Let's create a few different vectors
v1 = [2, 3]
v2 = [-1, 2]
v3 = [3, -2]

# Set up our plot
setup_plot(5, 5)

# Draw all three vectors in different colors
draw_vector(v1, color='blue', label='v1')
draw_vector(v2, color='red', label='v2')
draw_vector(v3, color='green', label='v3')

plt.title('Three Different Vectors')
plt.show()
```

### Exploration: What Happens When...

Let's investigate what happens when we change different parts of a vector. Try modifying the vectors below and observe the results:

```python exec
id: 01-vectors-and-visualisation-8
# What happens when both components are the same?
equal_components = [3, 3]

setup_plot(5, 5)
draw_vector(equal_components, color='purple', label='equal')
plt.title('Vector with Equal Components')
plt.show()

# What happens when one component is zero?
zero_y = [4, 0]
zero_x = [0, 4]

setup_plot(5, 5)
draw_vector(zero_y, color='orange', label='horizontal')
draw_vector(zero_x, color='cyan', label='vertical')
plt.title('Vectors with Zero Components')
plt.show()
```

### Your Turn

Create some vectors of your own and visualize them. What happens when you:
- Make both components negative?
- Use very large numbers?
- Make one component much larger than the other?

```python exec
id: 01-vectors-and-visualisation-9
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
# Your experiments here:
```

## Adding Vectors: A First Glimpse

Now let's try something interesting. What if we want to combine two vectors? Let's start by just adding the numbers component by component and see what happens.

First, let's write a function to add two vectors:

```python exec
id: 01-vectors-and-visualisation-10
def add_vectors(v1, v2):
    """
    Add two vectors by adding their corresponding components.

    Parameters:
    - v1: first vector [x1, y1]
    - v2: second vector [x2, y2]

    Returns:
    - a new vector [x1+x2, y1+y2]
    """
    # Add the x-components together
    new_x = v1[0] + v2[0]

    # Add the y-components together
    new_y = v1[1] + v2[1]

    # Return a new vector with these components
    return [new_x, new_y]
```

Now let's see what this looks like visually:

```python exec
id: 01-vectors-and-visualisation-11
# Define two vectors
a = [2, 1]
b = [1, 3]

# Add them together
c = add_vectors(a, b)

print(f"a = {a}")
print(f"b = {b}")
print(f"a + b = {c}")

# Visualize all three
setup_plot(5, 5)
draw_vector(a, color='blue', label='a')
draw_vector(b, color='red', label='b')
draw_vector(c, color='purple', label='a+b')
plt.title('Adding Two Vectors')
plt.show()
```

## Something Interesting to Notice

Look at where the purple vector (a+b) ends up! Let's draw this in a different way to see a beautiful pattern:

```python exec
id: 01-vectors-and-visualisation-12
def draw_vector_from_point(start, vector, color='blue', label=None, linestyle='-'):
    """
    Draw a vector starting from a specific point instead of the origin.

    Parameters:
    - start: the starting point [x, y]
    - vector: the vector to draw [dx, dy]
    - color: color of the arrow
    - label: optional label
    - linestyle: style of line ('-' for solid, '--' for dashed)
    """
    x_start = start[0]
    y_start = start[1]
    dx = vector[0]
    dy = vector[1]

    plt.arrow(x_start, y_start, dx, dy,
              head_width=0.2, head_length=0.2,
              fc=color, ec=color, linewidth=2,
              linestyle=linestyle)

    if label:
        plt.text(x_start + dx*0.5, y_start + dy*0.5, label, fontsize=12)

# Redraw with a "tip-to-tail" visualization
setup_plot(5, 5)

# Draw vector a from the origin
draw_vector(a, color='blue', label='a')

# Draw vector b starting from the tip of vector a
draw_vector_from_point(a, b, color='red', label='b')

# Draw the sum
draw_vector(c, color='purple', label='a+b')

# Draw a dashed parallelogram to show the relationship
draw_vector_from_point(b, a, color='gray', linestyle='--')

plt.title('The Parallelogram Pattern')
plt.show()
```

## A Question to Explore

Notice how we can think of vector addition in two ways:
1. Starting at the origin, draw **a**, then from its tip draw **b**, and you end up at **a+b**
2. The vectors **a**, **b**, and **a+b** form a parallelogram

**Try this:** Create your own pairs of vectors and add them. Do you always get a parallelogram? What happens when the vectors point in opposite directions? What about when one vector is very small?

```python exec
id: 01-vectors-and-visualisation-13
# Experiment here - try different vector combinations:
```

## Multiplying a Vector by a Number

What if we take a vector and multiply each component by the same number? Let's explore this:

```python exec
id: 01-vectors-and-visualisation-14
def scale_vector(scalar, vector):
    """
    Multiply a vector by a number (called a scalar).

    Parameters:
    - scalar: the number to multiply by
    - vector: the vector [x, y]

    Returns:
    - a new vector [scalar*x, scalar*y]
    """
    new_x = scalar * vector[0]
    new_y = scalar * vector[1]
    return [new_x, new_y]
```

```python exec
id: 01-vectors-and-visualisation-15
# Let's take a vector and multiply it by different numbers
v = [2, 1]

v_times_2 = scale_vector(2, v)
v_times_half = scale_vector(0.5, v)
v_times_neg = scale_vector(-1, v)

setup_plot(5, 5)
draw_vector(v, color='blue', label='v')
draw_vector(v_times_2, color='green', label='2v')
draw_vector(v_times_half, color='orange', label='0.5v')
draw_vector(v_times_neg, color='red', label='-v')

plt.title('Scaling a Vector')
plt.show()
```

## What Patterns Do You Notice?

**Explore:** What happens when you multiply a vector by:
- A number greater than 1?
- A number between 0 and 1?
- Zero?
- A negative number?

Try creating your own examples below:

```python exec
id: 01-vectors-and-visualisation-16
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
# Your explorations:
```

## Wrapping Up Part 1

Let's reflect on what we've discovered today:

1. We learned that **vectors** can be represented as **lists** of numbers in Python
2. We can visualize vectors as arrows pointing from the origin to a point
3. We created functions to help us work with vectors:
   - `draw_vector()` to visualize them
   - `add_vectors()` to combine them
   - `scale_vector()` to make them longer or shorter
4. We discovered some interesting patterns:
   - Adding vectors creates a parallelogram
   - Scaling a vector changes its length but not its direction (unless we multiply by a negative number!)

In the next notebook, we'll explore more vector operations and discover how vectors can help us understand geometric transformations.

## Before We Continue

Take a moment to experiment more with the functions we created. Try:
- Adding three or more vectors together (hint: you can use `add_vectors()` multiple times)
- Combining scaling and addition: what does `2*a + 3*b` look like?
- Creating vectors that, when added together, give you a specific target vector

```python exec
id: 01-vectors-and-visualisation-17
# Final playground - experiment here!
```

## Looking back

Before leaving this page, a sentence on each. What you write stays on this device.

```reflect
- Something you expected before running a cell that turned out differently
- The one idea from this page you could explain to someone else now
- Something you would change or try next, if there were time
- A question this page raised for you that it did not answer. Bring it to the next session; these questions are where the next session starts.
```
