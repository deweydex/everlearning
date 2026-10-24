---
title: "Tutorial 0: Getting Started - Programming with Polynomials"
slug: polynomials-0-introduction
course: programming-and-design-principles
series: oop-polynomials
series_title: "Object-Oriented Programming: A Worked Project"
version: 2026.09.07.1
---

# Tutorial 0: Getting Started - Programming with Polynomials

## Welcome!

Over the next five tutorials, we're going to explore **polynomial functions** through the lens of **object-oriented programming**. This isn't just about learning Python syntax - it's about discovering how programming concepts emerge naturally from mathematical problems.

### What Are We Building?

We'll create classes to represent and work with polynomial functions:
- Constants: `f(x) = 5`
- Linear functions: `f(x) = 2x + 3`
- Quadratics: `f(x) = x² - 4x + 3`
- And polynomials of any degree!

### Why Polynomials?

Polynomials are everywhere in mathematics and computing:
- **Physics**: Trajectories, motion, energy
- **Economics**: Cost functions, revenue models
- **Machine Learning**: Polynomial features, activation functions, curve fitting
- **Computer Graphics**: Bezier curves, animation paths
- **Signal Processing**: Approximating complex signals


- How to design classes
- When to use specific vs. general solutions
- Trade-offs in software design
- How inheritance can solve design problems

### Our Journey

We'll follow a **discovery-based approach**. Instead of being told "here's how to do OOP," we'll:
1. Build simple solutions
2. Notice problems and limitations
3. Discover better approaches
4. Understand trade-offs
5. Arrive at elegant solutions

This mirrors how real software development works - we iterate, we learn from what doesn't work, and we refine our designs.

---

## Tutorial Overview

### Tutorial 1: Linear and Constant Functions - Our First Classes

**What we'll build:**
- A `Constant` class for functions like `f(x) = 5`
- A `Linear` class for functions like `f(x) = 2x + 3`

**What we'll learn:**
- What a class is and why we need them
- How to bundle data and behavior together
- Basic methods: `evaluate()`, `plot()`, `derivative()`, `find_root()`
- How different classes can have the same method names (polymorphism preview)

**Problems we'll notice:**
- Code repetition (same `plot()` method in both classes)
- Integration is blocked (would need more classes)
- Pattern suggests we'd need infinite classes

**Key insight:** "These classes share a lot of structure. What if we keep adding more?"

---

### Tutorial 2: Quadratic Functions - Patterns Strengthen

**What we'll build:**
- A `Quadratic` class for parabolas: `f(x) = ax² + bx + c`
- Special methods: `vertex()`, `discriminant()`, `find_roots()`

**What we'll learn:**
- How derivatives connect classes (Quadratic → Linear → Constant)
- Where derivative equals zero (critical points, turning points)
- The relationship between roots and the vertex
- How the discriminant tells us about roots

**Problems intensify:**
- Code duplication is worse (three identical `plot()` methods)
- Still can't integrate (would need Cubic, Quartic, ...)
- Pattern is beautiful but clearly unsustainable

**Key insight:** "Do we really want to create a new class for every polynomial degree?"

---

### Tutorial 3: The Polynomial Class - General Representation

**What we'll build:**
- ONE `Polynomial` class that can represent any degree
- Coefficient list representation: `[c₀, c₁, c₂, ...]` means `c₀ + c₁x + c₂x² + ...`

**What we'll learn:**
- How to use lists to represent mathematical objects
- Power rule for derivatives (works for any degree!)
- Reverse power rule for integrals (works for any degree!)
- The beauty of general solutions

**Victory moments:**
- Derivatives work for everything!
- Integrals work for everything!
- Only ONE class instead of infinite
- No code duplication

**New trade-offs:**
- Lost exact root formulas (no more quadratic formula)
- Lost special methods (no more `vertex()`, `discriminant()`)
- Less intuitive interface (`[3, -4, 1]` vs `Quadratic(a=1, b=-4, c=3)`)

**Key insight:** "We solved some problems but created new ones. Can we have both generality AND specificity?"

---

### Tutorial 4: Polynomial Arithmetic - Combining Polynomials

**What we'll build:**
- Addition (`+`): Combine like terms
- Subtraction (`-`): Subtract coefficients
- Multiplication (`*`): Each term multiplies each term
- Equality testing (`==`)
- Building polynomials from roots

**What we'll learn:**
- Operator overloading (`__add__`, `__sub__`, `__mul__`, `__eq__`)
- How to handle lists of different lengths
- Verifying algebraic identities programmatically
- The power of general representations

**What we'll explore:**
- Binomial expansion and Pascal's triangle
- Factored vs. expanded forms
- Algebraic identities: `(a+b)² = a² + 2ab + b²`
- Building polynomials from known roots

**The tension remains:** "This is powerful, but we still lost those nice specific methods..."

---

### Tutorial 5: Inheritance - Best of Both Worlds (Parts 1 & 2)

**Part 1: Understanding Inheritance**

**What we'll build:**
- `Linear` class that inherits from `Polynomial`
- `Quadratic` class that inherits from `Polynomial`

**What we'll learn:**
- What inheritance is and why we need it
- `super().__init__()` to call parent initialization
- Inheriting methods automatically
- Overriding methods when needed
- Adding specialized methods

**The beautiful result:**
```python
quad = Quadratic(a=1, b=-4, c=3)
quad.vertex() # Specialized method - only for Quadratic
quad.discriminant() # Specialized method - only for Quadratic
quad.derivative() # Inherited from Polynomial - works!
quad.integrate() # Inherited from Polynomial - works!
quad + other # Inherited arithmetic - works!
```

**Part 2: Polymorphism and Design Principles**

**What we'll explore:**
- How different classes can be used interchangeably
- When to inherit vs. when to write from scratch
- The Liskov Substitution Principle (in plain language)
- Design patterns that emerge from our work

**The final insight:**
```python
functions = [
 Constant(5),
 Linear(m=2, b=3),
 Quadratic(a=1, b=-4, c=3),
 Polynomial([1, 0, -1, 0, 1])
]

# They ALL work the same way!
for f in functions:
 print(f.derivative())
 f.plot()
```

---

## The Big Picture: What We're Really Learning

### Programming Concepts

1. **Classes and Objects**
 - Bundling data and behavior
 - Encapsulation
 - Methods vs. functions

2. **Inheritance**
 - Reusing code through parent classes
 - Extending functionality
 - Method overriding

3. **Polymorphism**
 - Same interface, different implementations
 - Duck typing
 - Treating different objects uniformly

4. **Operator Overloading**
 - Making objects behave like built-in types
 - `+`, `-`, `*`, `==` for custom classes

5. **Design Patterns**
 - Building from simple to complex
 - Recognizing when to generalize
 - Trade-offs between specificity and generality

### Mathematical Concepts

1. **Calculus**
 - Derivatives (rate of change)
 - Integrals (accumulation)
 - Power rule and reverse power rule
 - Critical points and optimization

2. **Algebra**
 - Polynomial operations
 - Factoring and expanding
 - Roots and zeros
 - Algebraic identities

3. **Numerical Methods**
 - Newton's method for root finding
 - When exact formulas aren't available
 - Approximation and iteration

### Computational Thinking

1. **Abstraction**
 - Finding common patterns
 - Generalizing specific cases
 - Knowing when to abstract

2. **Decomposition**
 - Breaking problems into pieces
 - Building complex from simple

3. **Algorithm Design**
 - Iterative methods
 - Recursive thinking (polynomial multiplication)

4. **Testing and Verification**
 - Checking mathematical properties
 - Verifying identities
 - Edge cases and error handling

---

## How to Approach These Tutorials

### Active Learning

These tutorials are designed for **active engagement**:

1. **Try before looking at solutions**
 - Each "YOUR TURN" section has a solution, but try implementing it first
 - Struggling is part of learning - embrace it!

2. **Experiment**
 - Change values, try edge cases
 - Break things on purpose to see what happens
 - Ask "what if...?" questions

3. **Connect ideas**
 - Notice patterns across tutorials
 - See how problems from one tutorial motivate solutions in the next
 - Think about why we make certain design decisions

4. **Do the exercises**
 - They're not optional extras - they deepen understanding
 - Many exercises preview concepts from future tutorials

### Building Intuition

**Mathematics through code:**
- When you plot a function, you're seeing the math come alive
- When you verify an identity, you're building algebraic intuition
- When derivatives and integrals actually work, calculus becomes concrete

**Programming through math:**
- Mathematical structures suggest code structures
- Mathematical operations guide our method design
- Mathematical relationships reveal programming patterns

### The Discovery Process

This isn't a linear path. We'll:
- Build something that works
- Notice it's not quite right
- Try to fix it
- Discover we need a different approach
- Build something better
- Understand the trade-offs

This is **realistic software development**. We rarely get it right the first time, and that's okay!

---

## Prerequisites and Setup

### What You Need to Know

**Python basics:**
- Variables and types
- Lists and loops
- Functions (defining and calling)
- Basic conditionals (`if/else`)

**Mathematics:**
- Basic algebra (what is `2x + 3`?)
- What a function is (input → output)
- Graphing on x-y axes

**Nice to have (but we'll explain as we go):**
- Derivatives and integrals (we'll review the basics)
- Quadratic formula
- Roots of polynomials

### Libraries We'll Use

We only need two libraries, and we'll use them simply:

```python exec
id: polynomials-0-introduction-1
import numpy as np          # For creating number ranges
import matplotlib.pyplot as plt  # For plotting
```

That's it! Let's test that they work:

```python exec
id: polynomials-0-introduction-2
# Create some x values
x_values = np.arange(-5, 5, 0.1)

# Create some y values
y_values = [x**2 for x in x_values]

# Plot them
plt.plot(x_values, y_values)
plt.xlabel('x')
plt.ylabel('y')
plt.title('A simple parabola: y = x²')
plt.grid(True, alpha=0.3)
plt.show()

print("✓ Setup complete! Ready to start.")
```

---

## A Note on Difficulty

These tutorials will **challenge you**. That's intentional and healthy!

**When you feel stuck:**
1. Read the hints carefully
2. Try a simpler version first
3. Look at previous examples
4. Check the solution, understand it, then try again from scratch
5. Remember: everyone struggles with new concepts

**When it feels too easy:**
1. Try to implement before reading ahead
2. Do the exercises
3. Extend the ideas (can you add new methods?)
4. Think about edge cases and limitations

**The goal isn't to finish quickly** - it's to understand deeply.

---

## Beyond These Tutorials

After completing these five tutorials, you'll have:

1. **A solid foundation in OOP**
 - Classes, inheritance, polymorphism
 - Design patterns and trade-offs
 - When to use which approach

2. **Mathematical computing skills**
 - Implementing mathematical concepts in code
 - Numerical methods
 - Visualization

3. **A framework for learning**
 - How to approach new programming concepts
 - How to design and refine code
 - How to balance competing concerns

### Possible Extensions

Want to keep going? You could:
- Add more numerical methods (bisection, secant method)
- Implement polynomial division
- Create rational functions (ratios of polynomials)
- Explore curve fitting (least squares)
- Build spline interpolation
- Connect to machine learning (polynomial regression)

---

## Let's Begin!

Ready to start? Head to **Tutorial 1: Linear and Constant Functions**.

Remember:
- Be patient with yourself
- Experiment freely
- Notice patterns
- Ask "why?" questions
- Enjoy the discovery process!

Let's build something interesting together.

---

**Next: Tutorial 1 - Linear and Constant Functions**

## Looking back

Before leaving this page, a sentence on each. What you write stays on this device.

```reflect
- Something you expected before running a cell that turned out differently
- The one idea from this page you could explain to someone else now
- A question this page raised that it did not answer
```
