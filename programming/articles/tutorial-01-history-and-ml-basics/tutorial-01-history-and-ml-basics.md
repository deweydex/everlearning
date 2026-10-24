---
title: "Tutorial 1: The Evolution of Programming & Machine Learning Basics"
slug: tutorial-01-history-and-ml-basics
course: programming-and-design-principles
course_title: "Programming and Design Principles"
series: tutorials
series_title: "Tutorials"
version: 2026.09.06.1
---

# Tutorial 1: The Evolution of Programming & Machine Learning Basics

## What You'll Learn
- Evolution of programming languages from machine code to modern languages
- Different generations of programming languages
- Programming paradigms (procedural, functional, object-oriented)
- How programming languages differ and why
- Introduction to ML in context of programming history

---

## Part 1: The Dawn of Computing

### Timeline of Programming Languages

#### 1940s: Machine Code - The Beginning
- **Machine Code**: Binary instructions (0s and 1s) that computers understand directly
- Extremely difficult for humans to read and write
- Every computer model had different machine code

**Example of Machine Code:**
```
10110000 01100001 (Move 'a' to register)
```

**Challenge**: Imagine writing an entire program in 0s and 1s! 

#### 1950s: Assembly Language - First Step Up
- **Assembly Language**: Used mnemonics (short words) instead of binary
- **Assembler**: Program that translates assembly to machine code
- Still very low-level and machine-specific

**Example of Assembly:**
```assembly
MOV AX, 5 ; Move 5 into register AX
ADD AX, 3 ; Add 3 to AX
```

Let's simulate how different "generations" of code might look for a simple task:

```python exec
id: tutorial-01-history-and-ml-basics-1
# Simulating different programming "eras" for adding two numbers

print("=== Evolution of Programming ===")
print()

# Machine Code (simulated as binary string)
print("1940s - MACHINE CODE:")
print("10110000 00000101 10000011 11000000 00000011")
print("(Humans can't easily read this!)")
print()

# Assembly (simulated)
print("1950s - ASSEMBLY LANGUAGE:")
print("MOV AX, 5")
print("ADD AX, 3")
print("(Better, but still cryptic)")
print()

# Modern Python
print("2020s - MODERN PYTHON:")
result = 5 + 3
print("result = 5 + 3")
print(f"Result: {result}")
print("(Clear and readable!)")
print()
print("=" * 40)
```

---

### The Rise of High-Level Languages

#### 1950s-1960s: First High-Level Languages

**FORTRAN (1957)** - FORmula TRANslation
- First widely-used high-level language
- Designed for scientific calculations
- Still used in numerical computing today!

**COBOL (1959)** - COmmon Business-Oriented Language
- Designed for business applications
- English-like syntax
- Many banks still use it!

**LISP (1958)** - LISt Processing
- Designed for artificial intelligence research
- **First AI programming language!** 
- Introduced concepts used in ML today

#### 1970s: Structured Programming Revolution

**C (1972)**
- Powerful and efficient
- Foundation for many modern languages
- Operating systems written in C

**Pascal (1970)**
- Emphasized structured programming
- Popular for teaching programming

#### 1980s-1990s: Object-Oriented Era

**C++ (1985)**
- Added object-oriented features to C
- Used for games, system software

**Python (1991)** 
- Designed for readability
- "Simple is better than complex"
- Became dominant in ML/AI!

**Java (1995)**
- "Write once, run anywhere"
- Popular for enterprise applications

#### 2000s-2010s: Modern Era

**JavaScript** - Web development
**Swift** - iOS development 
**Rust** - System programming
**Go** - Cloud services

#### 2010s-Present: the Post-Modern Era

There is more to talk about there, but lets save that for later when we discuss typescript, bun and various frameworks...

Let's visualize this timeline:

```python exec
id: tutorial-01-history-and-ml-basics-2
# Programming Language Timeline

timeline = {
    1940: "Machine Code",
    1950: "Assembly Language",
    1957: "FORTRAN (Scientific)",
    1958: "LISP (AI/ML)",
    1959: "COBOL (Business)",
    1972: "C (System Programming)",
    1985: "C++ (OOP)",
    1991: "Python (ML/AI) 🐍",
    1995: "Java (Enterprise)",
    2010: "Modern AI/ML Era",
    2020: "Rise/Return of Nice Languages"
}

print("=== Programming Language Timeline ===")
print()
for year, language in timeline.items():
    print(f"{year}: {language}")
print()
print("Notice: Over 80 years of evolution!")
```

---

## Part 2: Understanding Programming Languages

### How Do Computers Understand Code?

#### Compilers vs Interpreters

**Compiler**:
- Translates entire program to machine code before running
- Creates an executable file
- Examples: C, C++, Go
- Faster execution, previously slower development (now, it is complicated), relies on lower level model of computing

**Interpreter**:
- Translates and executes code line by line
- No separate executable
- Examples: Python, JavaScript, Ruby  
- Slower execution, but faster development, benefits to readability, relies on higher level thinking

**Python is interpreted**, which makes it great for learning and ML experimentation!

Let's demonstrate how Python executes code sequentially:

```python exec
id: tutorial-01-history-and-ml-basics-3
# Python interprets code line by line, top to bottom

print("Step 1: Starting program")
x = 10
print("Step 2: Created variable x =", x)

x = x + 5
print("Step 3: Updated x to", x)

result = x * 2
print("Step 4: Calculated result =", result)

print("Step 5: Program complete!")

# Each line is interpreted and executed immediately
# This makes Python perfect for interactive ML development!
```

---

### Programming Paradigms

Different **styles** or **approaches** to programming.

#### 1. Procedural Programming
- **Step-by-step instructions**
- Like following a recipe
- Examples: C, Pascal
- **We'll focus on this initially!**

```python exec
id: tutorial-01-history-and-ml-basics-4
# Procedural Programming Example
# Step-by-step procedure to calculate average

print("=== Procedural Approach ===")

# Step 1: Get data
score1 = 85
score2 = 90
score3 = 78

# Step 2: Calculate sum
total = score1 + score2 + score3

# Step 3: Calculate average
average = total / 3

# Step 4: Display result
print("Average score:", average)
```

#### 2. Object-Oriented Programming (OOP)
- Organizes code around **objects**
- Objects have properties and behaviors
- Examples: Java, C++, Python
- **You'll learn this after mastering procedural!**

```python exec
id: tutorial-01-history-and-ml-basics-5
# Preview of Object-Oriented Programming
# Don't worry if this seems complex - you'll learn it later!

print("=== Object-Oriented Preview ===")
print("(You'll learn this properly later)")
print()

# Python strings are objects with methods
message = "hello world"

# Objects have behaviors (methods)
print("Original:", message)
print("Uppercase:", message.upper())
print("Capitalized:", message.capitalize())
print("Title Case:", message.title())
```

#### 3. Functional Programming
- Treats computation as mathematical functions
- Emphasizes immutability
- Examples: Haskell, LISP, (Python supports this too!)

#### 4. Logic Programming
- Based on formal logic
- Used in AI and expert systems
- Example: Prolog

#### 5. Scripting
- Automates tasks
- Often interpreted
- Examples: Python, JavaScript, Bash

**Python is multi-paradigm** - it supports procedural, OOP, and functional styles! This flexibility makes it excellent for ML.

---

## Part 3: What Makes Languages Different?

### Key Distinguishing Characteristics

#### 1. Syntax
The "grammar rules" of a programming language.

Let's compare the same task in different syntaxes:

```python exec
id: tutorial-01-history-and-ml-basics-6
# Python Syntax (what we're learning)
print("=== Different Language Syntax ===")
print()

print("PYTHON (our language):")
print('message = "Hello"')
print('print(message)')
print()

print("C/C++ syntax would be:")
print('char message[] = "Hello";')
print('printf("%s", message);')
print()

print("Java syntax would be:")
print('String message = "Hello";')
print('System.out.println(message);')
print()

print("JavaScript syntax would be:")
print('let message = "Hello";')
print('console.log(message);')
print()

# Notice: Same logic, different syntax!
# Python is considered the most readable
```

#### 2. Data Type Handling

**Statically Typed** (C, Java):
- Must declare variable types
- Example: `int age = 25;`
- Catches errors early

**Dynamically Typed** (Python, JavaScript):
- Types determined at runtime
- Example: `age = 25`
- More flexible, faster to write

Python's dynamic typing makes experimentation easy - perfect for ML!

```python exec
id: tutorial-01-history-and-ml-basics-7
# Python's Dynamic Typing
print("=== Dynamic Typing Demo ===")
print()

# Variable can hold different types
data = 42
print("data as integer:", data, "- Type:", type(data))

data = "Hello"
print("data as string:", data, "- Type:", type(data))

data = 3.14
print("data as float:", data, "- Type:", type(data))

print()
print("Same variable, different types!")
print("This flexibility is powerful for ML experiments")
```

#### 3. Memory Management

**Manual** (C, C++):
- Programmer controls memory
- More control, but more responsibility
- Can cause memory leaks

**Automatic** (Python, Java):
- Garbage collection handles memory
- Easier for programmers
- Python handles this for us!

#### 4. Execution Speed

**Faster**: C, C++, Rust
- Compiled to machine code
- Closer to hardware

**Moderate**: Java, C#
- Compiled to bytecode
- Run on virtual machine

**Slower**: Python, Ruby
- Interpreted
- But: libraries (NumPy, TensorFlow) may use fast C/C++ underneath (Check out Cython)!

---

## Part 4: Machine Learning & Programming History

### The Evolution of AI/ML Programming

#### 1950s-1960s: AI Beginnings
- **LISP** created for AI research
- Expert systems using rules
- Limited by computing power

#### 1980s-1990s: Statistical Methods
- Rise of statistical learning
- **C** and **C++** for performance
- Neural networks research

#### 2000s: Machine Learning Boom
- **Python** emerges as ML language of choice
- Libraries: scikit-learn, NumPy, pandas
- More accessible to non-experts

#### 2010s-Present: Deep Learning Revolution
- TensorFlow, PyTorch (Python-based)
- GPU acceleration
- **Python dominates ML/AI**

### Why Python for Machine Learning?

1. **Readable Syntax**: Easy to learn and understand
2. **Extensive Libraries**: NumPy, pandas, scikit-learn, TensorFlow
3. **Interactive Development**: Jupyter notebooks (like this!)
4. **Large Community**: Lots of resources and help
5. **Rapid Prototyping**: Test ideas quickly
6. **Integration**: Works well with C/C++ for speed

Let's create a simple "expert system" - one of the earliest forms of AI:

```python exec
id: tutorial-01-history-and-ml-basics-8
# Simple Expert System - Weather-Based Advice
# This is like 1960s-style AI programming!

print("=== Expert System Demo ===")
print("Early AI used rule-based systems like this")
print()

# Input data
temperature = 25  # Celsius
is_raining = False
wind_speed = 15  # km/h

# Expert system rules
print("Weather Conditions:")
print(f"Temperature: {temperature}°C")
print(f"Raining: {is_raining}")
print(f"Wind Speed: {wind_speed} km/h")
print()

# Rule-based decision making
print("Expert System Advice:")

# This is how early AI worked - simple rules!
if temperature > 30:
    print("🌞 It's hot! Stay hydrated.")
elif temperature < 10:
    print("🧥 It's cold! Wear a coat.")
else:
    print("😊 Temperature is comfortable!")

if is_raining:
    print("☔ Bring an umbrella!")

if wind_speed > 20:
    print("💨 It's windy! Hold onto your hat!")

print()
print("This rule-based approach is the foundation of AI!")
```

### Modern ML vs Traditional Programming

#### Traditional Programming:
```
Rules + Data → Output
```
We write explicit rules, provide data, get results.

#### Machine Learning:
```
Data + Output → Rules (Model)
```
We provide examples, ML finds the rules!

Let's illustrate this difference:

```python exec
id: tutorial-01-history-and-ml-basics-9
# Traditional Programming Approach
print("=== TRADITIONAL PROGRAMMING ===")
print("We write explicit rules:")
print()

def traditional_spam_detector(email):
    """Rule-based spam detection"""
    # We manually define all rules
    spam_words = ["free", "winner", "urgent", "click now"]

    email_lower = email.lower()

    for word in spam_words:
        if word in email_lower:
            return "SPAM"
    return "NOT SPAM"

# Test it
email1 = "You are a WINNER! Click now for free prize!"
email2 = "Meeting at 3pm tomorrow"

print(f"Email 1: {traditional_spam_detector(email1)}")
print(f"Email 2: {traditional_spam_detector(email2)}")
print()

print("=== MACHINE LEARNING APPROACH ===")
print("(Simplified concept - you'll learn properly later)")
print()
print("ML would:")
print("1. Look at thousands of spam examples")
print("2. Look at thousands of not-spam examples")
print("3. Automatically learn patterns")
print("4. Create rules without us coding them!")
print()
print("Traditional: We write rules")
print("ML: Computer learns rules from examples")
```

---

## Practice Exercises

### Your turn 1: Language Timeline
Fill in the missing information about programming languages, don't forget to cite your souces!

```python exec
id: tutorial-01-history-and-ml-basics-10
# Exercise 1: Complete the language information

languages = {
    "Python": {
        "year": 1991,
        "paradigm": "Multi-paradigm",
        "use_case": "Your answer here",  # What is Python mainly used for?
        "why_ml": "Your answer here"  # Why is it popular for ML?
    },
    "C": {
        "year": 1972,
        "paradigm": "Your answer here",  # What paradigm?
        "use_case": "Your answer here",  # What is C used for?
        "characteristic": "Your answer here"  # Key characteristic?
    },
    "LISP": {
        "year": 1958,
        "paradigm": "Functional",
        "use_case": "Your answer here",  # What was LISP designed for?
        "significance": "Your answer here"  # Why important for AI?
    }
}

# Print your answers
for lang, info in languages.items():
    print(f"{lang}:")
    for key, value in info.items():
        print(f"  {key}: {value}")
    print()
```

### Your turn 2: Comparing Approaches
Create a simple rule-based system for a different domain:

```python exec
id: tutorial-01-history-and-ml-basics-11
# Exercise 2: Student Grade Advisor (Expert System)
# Create a rule-based system that gives study advice based on grades

# Input data
grade_percentage = 65  # Change this to test different scenarios
hours_studied = 5
assignments_completed = 8
total_assignments = 10

print("=== Student Performance Advisor ===")
print(f"Grade: {grade_percentage}%")
print(f"Study Hours: {hours_studied}")
print(f"Assignments: {assignments_completed}/{total_assignments}")
print()
print("Advice:")

# YOUR CODE HERE:
# Add rules that give appropriate advice based on:
# - grade_percentage (e.g., < 50 = failing, 50-65 = pass, 65-79 = merit, 80+ = distinction)
# - hours_studied (e.g., < 3 = study more)
# - assignments_completed (e.g., < 80% completed = catch up needed)

# Example rule to get you started:
if grade_percentage < 50:
    print("⚠️ Grade is failing. Need significant improvement.")

# Add more rules here...

print()
print("(This is how expert systems work!)")
```

### Your turn 3: Understanding Language Characteristics
Match the characteristics to benefits:

```python exec
id: tutorial-01-history-and-ml-basics-12
# Exercise 3: Language Characteristics Quiz
# Fill in the answers (True or False)

questions = {
    "Python is interpreted (not compiled)": None,  # True or False?
    "C is faster than Python for execution": None,  # True or False?
    "Python uses dynamic typing": None,  # True or False?
    "All languages use the same syntax": None,  # True or False?
    "Machine code is easy for humans to read": None,  # True or False?
    "Python is good for rapid prototyping": None,  # True or False?
    "Assembly language uses binary (0s and 1s)": None,  # True or False?
}

# Replace None with True or False for each question
# Then run this cell to see your answers

print("=== Language Characteristics Quiz ===")
for question, answer in questions.items():
    result = "✓" if answer is not None else "❌ (Not answered)"
    print(f"{result} {question}: {answer}")
```

### Your turn 4: Evolution Simulation
Create a simple program showing how we might represent the same calculation in "different eras":

```python exec
id: tutorial-01-history-and-ml-basics-13
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
# Exercise 4: Represent calculating a circle's area in different "styles"
# Formula: Area = π × radius²

import math

radius = 5

print("=== Calculating Circle Area ===")
print(f"Radius: {radius}")
print()

# 1. Basic style (like early programming)
print("BASIC STYLE (1960s):")
pi = 3.14159
area = pi * radius * radius
print("Area:", area)
print()

# 2. Modern Python style
print("MODERN PYTHON STYLE:")
# YOUR CODE HERE: Calculate area using math.pi and ** operator
# Hint: math.pi gives you π, and ** is power operator
area_modern = 0  # Replace with your calculation
print(f"Area: {area_modern}")
print()

# 3. Using a function (procedural programming)
print("PROCEDURAL STYLE (using function):")
# YOUR CODE HERE: Create a function that calculates circle area
def calculate_circle_area(r):
    # Your calculation here
    return 0  # Replace with actual calculation

area_function = calculate_circle_area(radius)
print(f"Area: {area_function}")
print()

print("All produce the same result, but with evolution in style!")
```

---

## Key Concepts Summary

### Evolution of Programming
1. **Machine Code (1940s)**: Binary, hardware-specific
2. **Assembly (1950s)**: Mnemonics, still low-level
3. **High-Level Languages (1950s+)**: More readable, portable
4. **Modern Languages (1990s+)**: Emphasis on productivity and readability

### Language Characteristics
- **Syntax**: The grammar rules
- **Typing**: How variables and types are handled
- **Execution**: Compiled vs interpreted
- **Paradigm**: Programming style/approach
- **Memory Management**: Manual vs automatic

### Common Features Across Languages
1. Variables for storing data  
2. Input/output operations  
3. Mathematical operators  
4. Control structures (branching, looping) (though not always in the same way!)
5. Functions/procedures  
6. Data structures  

### Why Python for ML?
1. **Readable** - Easy to understand
2. **Productive** - Write less code
3. **Interactive** - Great for experimentation
4. **Rich Ecosystem** - Excellent ML libraries
5. **Community** - Large support network

### Programming vs Machine Learning
- **Traditional**: We write explicit rules
- **ML**: Computer learns rules from examples
- **Both**: Use the same programming fundamentals!

---

## Assessment Preparation

This tutorial covers **Theory Exam** topics:
- Learning Outcome 1: Historical development 
- Learning Outcome 3: Differentiating languages 

### Sample Exam Questions

**Question 1**: Explain the evolution from machine code to high-level languages. Why was this evolution necessary?

**Question 2**: Describe three characteristics that differentiate programming languages from each other. Give examples.

**Question 3**: Explain the difference between a compiler and an interpreter. Give an example of a language for each.

**Question 4**: Why is Python considered a good language for machine learning? List at least three reasons.

**Question 5**: Describe the difference between procedural and object-oriented programming paradigms.

---

## Reflection Questions

Take time to think about these:

**Your Reflections:**

1. **Why do you think so many different programming languages exist?**
   
   (Your answer here)

2. **What programming paradigm seems most intuitive to you and why?**
   
   (Your answer here)

3. **How might Python's interpreted nature benefit ML research?**
   
   (Your answer here)

4. **Can you think of a problem that would be better suited to traditional programming vs ML?**
   
   (Your answer here)

---

## Next Steps


- How programming languages evolved
- What makes languages different
- Why Python is excellent for ML
- The connection between programming and AI/ML

### Before Tutorial 2:
- [ ] Complete all exercises
- [ ] Review the timeline and key dates
- [ ] Think about how rule-based systems work
- [ ] Research one language mentioned that interests you

### In Tutorial 2, we'll explore:
- **Algorithms**: Step-by-step problem solving
- **Pseudocode**: Planning before coding  
- **Flowcharts**: Visual representation
- **Building your first real prediction algorithm!**

---

**See you in Tutorial 2!**

```python exec
id: tutorial-01-history-and-ml-basics-14
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
# Your code here
```

## What we set out to do

These were the aims of this notebook. Now that you have worked through it, they are a check on what happened rather than a promise about it.

1. **Demonstrate understanding of historical development** of computer programming (LO 1)
2. **Differentiate between programming languages** by identifying their characteristics (LO 3)
3. Understand the connection between programming evolution and ML development

## Looking back

Before leaving this page, a sentence on each. What you write stays on this device.

```reflect
- Something you expected before running a cell that turned out differently
- The one idea from this page you could explain to someone else now
- Something you would change or try next, if there were time
- A question this page raised for you that it did not answer. Bring it to the next session; these questions are where the next session starts.
```
