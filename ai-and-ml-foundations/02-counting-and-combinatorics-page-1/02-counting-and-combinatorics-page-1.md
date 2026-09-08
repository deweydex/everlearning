---
title: "Notebook 2: Counting & Combinatorics (1 of 2)"
slug: 02-counting-and-combinatorics-page-1
course: ai-and-ml-foundations
course_title: "AI and ML Foundations"
series: 3-probability-and-statistics
series_title: "Probability and Statistics"
version: 2026.09.06.1
---

# Notebook 2: Counting & Combinatorics

## Part 0: Why Counting Matters

Before calculating probabilities, we need to count possibilities. But some numbers are too large to count directly.

**Consider these questions:**

**Question 1**: How many different 5-word sentences can you make from a 10,000-word vocabulary?

**Question 2**: How many unique 3×3 pixel patterns exist in a grayscale image (256 values per pixel)?

**Question 3**: How many ways can a doctor order 3 treatments from 10 available options?

**Question 4**: How many 8-character passwords are possible?

### Quick Check 0.1: Estimation Challenge

Before learning any formulas, estimate answers to these questions. Write your guesses and reasoning:

```python exec
id: 02-counting-and-combinatorics-page-1-1
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
# Your estimates:
# Question 1:
# Question 2:
# Question 3:
# Question 4:
# Reasoning:
```

### What You'll Learn

This notebook teaches systematic counting:
1. **Multiplication and addition principles**: Combining choices
2. **Factorials**: Rapid growth
3. **Permutations**: Order matters (arrangements)
4. **Combinations**: Order doesn't matter (selections)
5. **Applications**: Probability calculations with large sample spaces

---

## Part 1: The Fundamental Counting Principles

```python exec
id: 02-counting-and-combinatorics-page-1-2
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
import math
from itertools import permutations, combinations, product

np.random.seed(42)
```

### The Multiplication Principle

**Rule**: If event 1 can occur in m ways AND event 2 can occur in n ways, then both events together can occur in **m × n** ways.

### Example 1.1: Building Sentences

```python exec
id: 02-counting-and-combinatorics-page-1-3
# Sentence structure: Subject + Verb + Object
subjects = ["the patient", "the doctor", "the nurse"]
verbs = ["examined", "treated", "diagnosed", "helped"]
objects = ["the wound", "the illness", "the condition"]

# Count
num_subjects = len(subjects)
num_verbs = len(verbs)
num_objects = len(objects)

total_sentences = num_subjects * num_verbs * num_objects
print(f"Total sentences: {num_subjects} × {num_verbs} × {num_objects} = {total_sentences}")

# Generate first 10
all_sentences = []
for subj in subjects:
    for verb in verbs:
        for obj in objects:
            all_sentences.append(f"{subj} {verb} {obj}")

print(f"\nFirst 10 sentences:")
for i, sent in enumerate(all_sentences[:10], 1):
    print(f"{i}. {sent}")
print(f"\n... and {len(all_sentences)-10} more")
```

### Try this 1.1: Predict Then Calculate

You want to create sentences with:
- 5 subjects
- 8 verbs  
- 6 objects
- 4 modifiers ("quickly", "carefully", "slowly", "urgently")

Structure: Subject + Verb + Object + Modifier

1. Predict: How many sentences are possible?
2. Calculate using the multiplication principle
3. Generate 20 random sentences
4. What if you add 3 more verbs? How does the count change?

```python exec
id: 02-counting-and-combinatorics-page-1-4
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
# Your prediction:

# YOUR CODE HERE
```

### Example 1.2: Binary Pixel Patterns

```python exec
id: 02-counting-and-combinatorics-page-1-5
# Binary image: each pixel is 0 or 1
# 3×3 pattern has 9 pixels
num_pixels = 9
choices_per_pixel = 2
total_patterns = choices_per_pixel ** num_pixels

print(f"Binary 3×3 patterns: {choices_per_pixel}^{num_pixels} = {total_patterns}")

# Visualize 10 random patterns
fig, axes = plt.subplots(2, 5, figsize=(12, 5))
axes = axes.flatten()

for i, ax in enumerate(axes):
    pattern = np.random.randint(0, 2, size=(3, 3))
    ax.imshow(pattern, cmap='gray', vmin=0, vmax=1)
    ax.set_title(f"Pattern {i+1}")
    ax.axis('off')

plt.suptitle(f"10 Random Patterns (out of {total_patterns} possible)", fontsize=14, weight='bold')
plt.tight_layout()
plt.show()
```

### Try this 1.2: Explore Pattern Spaces

Calculate the number of patterns for:
1. 4×4 binary images
2. 3×3 grayscale images (4 possible values: 0, 85, 170, 255)
3. 5×5 binary images
4. 2×2 grayscale images (256 possible values)

Then:
5. Which has more possible patterns: 10×10 binary or 3×3 full grayscale?
6. Create a bar chart comparing these counts (use log scale!)
7. Why does this matter for image recognition?

```python exec
id: 02-counting-and-combinatorics-page-1-6
# YOUR CODE HERE
```

### Quick Check 1.1: Password Strength

Before calculating:
- Password A: 4 lowercase letters
- Password B: 4 mixedcase letters
- Password C: 8 lowercase letters
- Password D: 8 mixedcase letters
- Password E: 12 lowercase letters
- Password F: 12 mixedcase letters
Which is stronger? By roughly how much? What might a graph look like?

```python exec
id: 02-counting-and-combinatorics-page-1-7
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
# Your prediction:
```

### Example 1.3: Password Strength Analysis

```python exec
id: 02-counting-and-combinatorics-page-1-8
password_length = 8
choices_per_char = 26 + 26 + 10 + 10  # lower + upper + digits + special

total_passwords = choices_per_char ** password_length

print(f"8-character passwords: {choices_per_char}^{password_length}")
print(f"= {total_passwords:.2e}")
print(f"= {total_passwords:,}")

# Time to crack at 1 billion attempts/second
attempts_per_second = 1_000_000_000
seconds_to_crack = total_passwords / attempts_per_second
years_to_crack = seconds_to_crack / (60 * 60 * 24 * 365)

print(f"\nAt 1 billion attempts/second: {years_to_crack:.0f} years to try all")
```

### Try this 1.3: Password Policy Analysis

Compare these password policies:
1. **Policy A**: 6 characters, any from 72 possible
2. **Policy B**: 18 characters, lowercase only (26 possible)
3. **Policy C**: 10 characters, uppercase + lowercase (52 possible)

For each:
1. Calculate total possible passwords
2. Calculate time to crack (at 1 billion/sec)
3. Create a visualization comparing their strength
4. Which policy is strongest?
5. What surprised you?

```python exec
id: 02-counting-and-combinatorics-page-1-9
# YOUR CODE HERE
```

### The Addition Principle

**Rule**: If event A can occur in m ways OR event B can occur in n ways, and A and B cannot both occur, then "A or B" can occur in **m + n** ways.

### Try this 1.4: Medical Test Selection

A patient needs ONE test. Options:
- 5 blood tests
- 3 imaging scans
- 2 genetic tests

1. How many total options?
2. If blood tests are unavailable, how many options remain?
3. Create lists of actual test names
4. Display all options to the patient
5. What if patient needs TWO tests (one from each category)?

```python exec
id: 02-counting-and-combinatorics-page-1-10
# YOUR CODE HERE
```

---

## Part 2: Factorials and Permutations

### Quick Check 2.1: Intuition Test

How many ways can you arrange these letters: A, B, C?

Try to list them all before looking ahead:

```python exec
id: 02-counting-and-combinatorics-page-1-11
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
# Your list:
```

### Factorials

The **factorial** of n (written n!) is:
$$n! = n \times (n-1) \times (n-2) \times ... \times 2 \times 1$$

Special case: 0! = 1

Factorials grow **extremely fast**!

```python exec
id: 02-counting-and-combinatorics-page-1-12
def factorial(n):
    """Calculate n! recursively."""
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# Display factorials
print("Factorials:")
for n in range(11):
    print(f"{n}! = {factorial(n):,}")

print(f"\n20! = {math.factorial(20):,}")
print("\nFactorials grow faster than exponentials!")
```

### Try this 2.1: Visualize Factorial Growth

1. Calculate factorials from 1 to 15
2. Plot them on both linear and log scale
3. On the same plot, add 2^n and n^2
4. Compare the growth rates
5. At what point does factorial overtake exponential?
6. Why does this matter for algorithm analysis?

```python exec
id: 02-counting-and-combinatorics-page-1-13
# YOUR CODE HERE
```

### Permutations: Order Matters

**Question**: How many ways can you arrange n distinct objects?

**Answer**: n!

### Example 2.1: Word Arrangements

```python exec
id: 02-counting-and-combinatorics-page-1-14
word = "CAT"
letters = list(word)

# Generate all permutations
all_perms = list(permutations(letters))

print(f"Letters: {letters}")
print(f"Number of arrangements: {len(letters)}! = {factorial(len(letters))}")
print(f"\nAll arrangements:")
for i, perm in enumerate(all_perms, 1):
    print(f"{i}. {''.join(perm)}")
```

### Try this 2.2: Anagram Detection

Given the word "LISTEN":
1. How many possible arrangements exist?
2. Generate all arrangements (this will be a lot!)
3. How many of these are real English words?
4. Find "SILENT" in the list (it's an anagram!)
5. Create a function to check if two words are anagrams
6. Test with: "dormitory" and "dirty room"

```python exec
id: 02-counting-and-combinatorics-page-1-15
# YOUR CODE HERE
# Hint: Use sorted(word) to test anagrams
```

### Example 2.2: Treatment Sequences

```python exec
id: 02-counting-and-combinatorics-page-1-16
treatments = ["Surgery", "Radiation", "Chemotherapy", "Physical Therapy"]

num_sequences = factorial(len(treatments))
print(f"Number of treatment sequences: {len(treatments)}! = {num_sequences}")

# Generate all
all_sequences = list(permutations(treatments))

print(f"\nFirst 10 sequences:")
for i, seq in enumerate(all_sequences[:10], 1):
    print(f"{i}. {' → '.join(seq)}")
print(f"\n... and {len(all_sequences)-10} more")
```

### Try this 2.3: Optimize Treatment Order

Some treatment orders are better than others. Create a scoring system:
1. Generate all 24 possible sequences
2. Assign effectiveness scores:
   - Surgery before Radiation: +10 points
   - Chemotherapy before Physical Therapy: +5 points
   - Physical Therapy last: +8 points
3. Calculate score for each sequence
4. Find the best sequence
5. Find the worst sequence
6. Visualize score distribution

```python exec
id: 02-counting-and-combinatorics-page-1-17
# YOUR CODE HERE
```

### Partial Permutations: P(n, r)

**Question**: How many ways to arrange r objects from n objects?

**Answer**:
$$P(n, r) = \frac{n!}{(n-r)!}$$

```python exec
id: 02-counting-and-combinatorics-page-1-18
def permutation(n, r):
    """Calculate P(n,r)."""
    return factorial(n) // factorial(n - r)

# Example: Top 3 from 10 images
n_images = 10
top_k = 3
num_rankings = permutation(n_images, top_k)

print(f"P({n_images}, {top_k}) = {num_rankings}")
print(f"Different ways to rank top 3 from 10 images")
```

### Try this 2.4: Search Engine Rankings

A search engine has 50 possible results for a query.
It must display the top 10 in order.

1. How many different top-10 rankings are possible?
2. Compare to the total number of ways to select 10 from 50 (ignoring order)
3. What's the ratio?
4. If you had to test all rankings, how long would it take?
   (Assume 0.1 seconds per test)
5. Why is search engine optimization so challenging?

```python exec
id: 02-counting-and-combinatorics-page-1-19
# YOUR CODE HERE
```

## Looking back

Before leaving this page, a sentence on each. What you write stays on this device.

```reflect
- Something you expected before running a cell that turned out differently
- The one idea from this page you could explain to someone else now
- Something you would change or try next, if there were time
- A question this page raised for you that it did not answer. Bring it to the next session; these questions are where the next session starts.
```
