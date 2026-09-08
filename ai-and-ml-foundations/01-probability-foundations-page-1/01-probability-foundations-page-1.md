---
title: "Notebook 1: Probability Foundations (1 of 2)"
slug: 01-probability-foundations-page-1
course: ai-and-ml-foundations
course_title: "AI and ML Foundations"
series: 3-probability-and-statistics
series_title: "Probability and Statistics"
version: 2026.09.06.1
---

# Notebook 1: Probability Foundations

## Part 0: Why Probability Matters for AI

Before diving into formulas, consider these real scenarios:

**Scenario 1: Image Recognition**
Your phone looks at a photo and says "85% confident this is a cat." What does 85% actually mean? How did it calculate that number?

**Scenario 2: Text Prediction**
You type "I'm going to the..." and your keyboard suggests "store", "gym", "doctor". How does it know which word is most likely?

**Scenario 3: Medical Diagnosis**
A patient tests positive for a rare disease. The test is 95% accurate. Does that mean there's a 95% chance they have the disease?

**Spoiler**: The answer to Scenario 3 is often "no" - sometimes much less than 95%! We'll discover why.

### What You'll Learn

This notebook builds probability from the ground up:
1. **Experiments and sample spaces**: Defining what's possible
2. **Probability scales**: Numbers between 0 and 1
3. **Compound events**: Combining probabilities with AND, OR, NOT
4. **Independence**: When events don't affect each other
5. **Conditional probability**: Updating beliefs with new information

You'll work with images, text, and health data throughout. By the end, you'll solve the medical testing paradox from Scenario 3.

---

## Part 1: Experiments and Sample Spaces

### Quick Check 1.1: What Makes Something Random?

Before reading further, think:
- Is flipping a coin random?
- Is tomorrow's temperature random?
- Is the next word you'll type random?
- What makes something "random" vs. "deterministic"?

Write your thoughts:

```python exec
id: 01-probability-foundations-page-1-1
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
# Your thoughts here as a comment:
#
```

### Random Experiments

A **random experiment** is any process where:
1. We can list all possible outcomes
2. We cannot predict with certainty which outcome will occur
3. We can repeat the experiment under the same conditions

The set of all possible outcomes is the **sample space** (Ω).

```python exec
id: 01-probability-foundations-page-1-2
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter

np.random.seed(42)
```

### Example 1.1: Coin Flips

```python exec
id: 01-probability-foundations-page-1-3
def flip_coin():
    """Simulate a single coin flip."""
    return np.random.choice(['H', 'T'])

# Flip 10 times
flips = [flip_coin() for _ in range(10)]
print("10 coin flips:", flips)
print(f"Heads: {flips.count('H')}, Tails: {flips.count('T')}")
```

```python exec
id: 01-probability-foundations-page-1-4
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
# Your code here
```

```python exec
id: 01-probability-foundations-page-1-5
def random_bitflip():
    """Simulate a single coin flip."""
    return np.random.choice([0, 1])

flips8 = [int(random_bitflip()) for _ in range(8)]
print(flips8)
#0
#1
#10 = 2 * 1 + 0 *1
#11 = 2 * 1 + 1 * 1 = 3
#100 = 2 * 4 + 0 * 2 + 0 * 1

#11111111 = 255
#100000000 = 256
my_binary_num = bin(16)
#print(my_binary_num)
print(bin(255))
```

### Try this 1.1: Predict Then Test

Before running the code:
1. Predict: If you flip 100 coins, roughly how many heads will you get?
2. Write your prediction below
3. Now simulate 100 flips and compare
4. Try 1000 flips. What do you notice?
5. What happens as you increase the number of flips?

```python exec
id: 01-probability-foundations-page-1-6
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
# Your prediction:
"I predict 50 heads approximately"

flips = [flip_coin() for _ in range(100)]
print("100 coin flips:", flips)
print(f"Heads: {flips.count('H')}, Tails: {flips.count('T')}")
```

### Example 1.2: Pixel Values in Images

In a grayscale image, each pixel has a value from 0 (black) to 255 (white).

Sample space: Ω = {0, 1, 2, ..., 255}

```python exec
id: 01-probability-foundations-page-1-7
# Create an image with three brightness regions
dark_pixels = np.random.randint(0, 51, size=100)      # 0-50
medium_pixels = np.random.randint(100, 151, size=100) # 100-150
bright_pixels = np.random.randint(200, 256, size=100) # 200-255

image_pixels = np.concatenate([dark_pixels, medium_pixels, bright_pixels])

# Visualize
plt.figure(figsize=(10, 4))
plt.hist(image_pixels, bins=30, edgecolor='black', alpha=0.7)
plt.xlabel('Pixel Value')
plt.ylabel('Frequency')
plt.title('Distribution of Pixel Values')
plt.grid(True, alpha=0.3)
plt.show()

print(f"Total pixels: {len(image_pixels)}")
print(f"Dark (0-50): {len(dark_pixels)}")
print(f"Medium (100-150): {len(medium_pixels)}")
print(f"Bright (200-255): {len(bright_pixels)}")
```

### Try this 1.2: Analyze the Image

Looking at the histogram above:
1. What can you infer about the image? (Dark, bright, mixed?)
2. Sample 20 random pixels from the image
3. Count how many fall in each region (dark/medium/bright)
4. Does your sample match the overall distribution?
5. Try sampling again. Do you get the same result?

```python exec
id: 01-probability-foundations-page-1-8
# YOUR CODE HERE
```

### Example 1.3: Next Word Prediction (NLP)

Consider: "The doctor prescribed..."

What word comes next? The sample space includes all English words, but they're not equally likely!

```python exec
id: 01-probability-foundations-page-1-9
# Simplified next-word model
# (In reality, trained on millions of texts)
possible_words = [
    'medicine', 'medicine', 'medicine', 'medicine', 'medicine',
    'antibiotics', 'antibiotics', 'antibiotics',
    'rest', 'rest',
    'exercise',
    'treatment'
]

# Sample 20 predictions
predictions = [np.random.choice(possible_words) for _ in range(20)]
print("20 predictions:", predictions)

# Count frequencies
word_counts = Counter(predictions)
print("\nFrequencies:")
for word, count in word_counts.most_common():
    print(f"  {word}: {count}")
```

### Try this 1.3: Build a Word Predictor

Create your own next-word model:
1. After "The patient feels..." create a list of possible next words
2. Make some words more frequent than others (realistic frequencies)
3. Sample 50 predictions
4. Plot a bar chart of word frequencies
5. Which word is most common? Is this what you'd expect?

```python exec
id: 01-probability-foundations-page-1-10
# YOUR CODE HERE
# Hint: Use Counter and plt.bar()
```

---

## Part 2: Probability - Measuring Likelihood

### Quick Check 2.1: Understanding Probability

Before we define probability formally, answer:
- What does "50% chance of rain" mean to you?
- If a coin has 50% chance of heads, does that mean exactly 5 heads in 10 flips?
- Can probability be negative? Can it be larger than 1?

Write your thoughts:

```python exec
id: 01-probability-foundations-page-1-11
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
# Your thoughts:
```

### The Probability Scale

Probability is a number between 0 and 1:
- **P(E) = 0**: Event E is impossible
- **P(E) = 1**: Event E is certain
- **P(E) = 0.5**: Event E happens half the time

### Calculating Probability

For equally likely outcomes:
$$P(E) = \frac{\text{Number of favorable outcomes}}{\text{Total number of outcomes}}$$

For experiments we can repeat:
$$P(E) \approx \frac{\text{Number of times E occurs}}{\text{Total number of trials}}$$

```python exec
id: 01-probability-foundations-page-1-12
def estimate_probability(experiment_fn, event_check_fn, num_trials=10000):
    """Estimate probability through simulation."""
    successes = 0
    for _ in range(num_trials):
        outcome = experiment_fn()
        if event_check_fn(outcome):
            successes += 1
    return successes / num_trials

# Example: P(Heads)
prob_heads = estimate_probability(
    experiment_fn=flip_coin,
    event_check_fn=lambda x: x == 'H',
    num_trials=10000
)

print(f"Estimated P(Heads) = {prob_heads:.4f}")
print(f"Theoretical P(Heads) = 0.5000")
```

### Try this 2.1: Estimate Pixel Probabilities

Using the image_pixels array from earlier:
1. Calculate P(pixel is dark), where dark means value < 75
2. Calculate P(pixel is bright), where bright means value > 175
3. Calculate P(pixel is medium), where medium means 75 ≤ value ≤ 175
4. Verify that these three probabilities sum to 1.0
5. Why must they sum to 1.0?

```python exec
id: 01-probability-foundations-page-1-13
# YOUR CODE HERE
```

### Try this 2.2: Word Prediction Probabilities

Using your word list from Challenge 1.3:
1. Calculate P(each word)
2. Create a visualization (bar chart) of these probabilities
3. Verify all probabilities sum to 1.0
4. Which word is most probable? Least probable?
5. How would these probabilities change if you trained on different texts?

```python exec
id: 01-probability-foundations-page-1-14
# YOUR CODE HERE
```

### Quick Check 2.2: Probability Rules

Given:
- P(rain tomorrow) = 0.3
- P(no rain tomorrow) = ???

What must P(no rain) equal? Why?

```python exec
id: 01-probability-foundations-page-1-15
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
# Your answer and reasoning:
```

---

## Part 3: Compound Events

### Combining Events

We can combine events using logical operations:
- **AND** (∩): Both events occur
- **OR** (∪): At least one event occurs
- **NOT** (¬): Event does not occur

### Example 3.1: Two Coin Flips

```python exec
id: 01-probability-foundations-page-1-16
def flip_two_coins():
    """Flip two coins, return as string."""
    return flip_coin() + flip_coin()

# Simulate 10000 double flips
double_flips = [flip_two_coins() for _ in range(10000)]

# Count outcomes
outcome_counts = Counter(double_flips)
print("Outcome frequencies:")
for outcome in ['HH', 'HT', 'TH', 'TT']:
    count = outcome_counts[outcome]
    prob = count / 10000
    print(f"  {outcome}: {count} ({prob:.4f})")
```

### Try this 3.1: Predict Then Calculate

Before running any code, predict:
1. P(both flips are heads) = ???
2. P(at least one head) = ???
3. P(exactly one head) = ???
4. P(first flip is heads) = ???

Write your predictions, then verify with simulation.

```python exec
id: 01-probability-foundations-page-1-17
# Predictions:
#

# YOUR VERIFICATION CODE HERE
```

### The Addition Rule

For any two events A and B:
$$P(A \cup B) = P(A) + P(B) - P(A \cap B)$$

Why subtract P(A ∩ B)? Because otherwise we count it twice!

### Example 3.2: Image Features

Create an image where the top half is darker than the bottom half.

```python exec
id: 01-probability-foundations-page-1-18
# Create 100x100 image
top_half = np.random.randint(0, 80, size=(50, 100))     # darker
bottom_half = np.random.randint(100, 256, size=(50, 100)) # brighter
full_image = np.vstack([top_half, bottom_half])

# Flatten and analyze
all_pixels = full_image.flatten()
pixel_positions = [(i // 100, i % 100) for i in range(len(all_pixels))]

# Define events
is_dark = all_pixels < 50
is_top_half = np.array([pos[0] < 50 for pos in pixel_positions])

# Calculate probabilities
prob_dark = np.mean(is_dark)
prob_top = np.mean(is_top_half)
prob_dark_and_top = np.mean(is_dark & is_top_half)
prob_dark_or_top = np.mean(is_dark | is_top_half)

print(f"P(Dark) = {prob_dark:.4f}")
print(f"P(Top half) = {prob_top:.4f}")
print(f"P(Dark AND Top) = {prob_dark_and_top:.4f}")
print(f"P(Dark OR Top) = {prob_dark_or_top:.4f}")

# Verify addition rule
calculated = prob_dark + prob_top - prob_dark_and_top
print(f"\nAddition rule check: {calculated:.4f} vs {prob_dark_or_top:.4f}")

# Visualize
plt.figure(figsize=(6, 6))
plt.imshow(full_image, cmap='gray', vmin=0, vmax=255)
plt.title('Image: Darker on Top')
plt.colorbar(label='Pixel Value')
plt.show()
```

### Try this 3.2: Create and Analyze Your Own Image

Create a 100x100 image with TWO distinct regions:
1. Left half: mostly dark (0-50)
2. Right half: mostly bright (200-255)

Then calculate:
1. P(pixel is dark)
2. P(pixel is on left)
3. P(dark AND left)
4. P(dark OR left)
5. Verify the addition rule
6. Visualize your image

```python exec
id: 01-probability-foundations-page-1-19
# YOUR CODE HERE
```

### Try this 3.3: Text Analysis - Bigrams

Given this text:
```
"the patient was diagnosed the doctor prescribed medicine the patient recovered"
```

1. Split into words
2. Calculate P(word is "the")
3. Calculate P(word is "patient")
4. Calculate P(word is "the" OR "patient")
5. Can "the" and "patient" occur simultaneously? Why or why not?
6. Does this affect the addition rule?

```python exec
id: 01-probability-foundations-page-1-20
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
