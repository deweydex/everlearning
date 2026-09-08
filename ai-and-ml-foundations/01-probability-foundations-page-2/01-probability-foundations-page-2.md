---
title: "01-probability-foundations-page-2 (2 of 2)"
slug: 01-probability-foundations-page-2
course: ai-and-ml-foundations
course_title: "AI and ML Foundations"
series: 3-probability-and-statistics
series_title: "Probability and Statistics"
version: 2026.09.06.1
---

Before starting this page, run the cell below. It repeats the imports and definitions from the earlier pages that this page uses.

```python exec
id: 01-probability-foundations-page-2-setup
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter

import numpy as np
import matplotlib.pyplot as plt
from collections import Counter

np.random.seed(42)

def flip_coin():
    """Simulate a single coin flip."""
    return np.random.choice(['H', 'T'])

# Flip 10 times
flips = [flip_coin() for _ in range(10)]
print("10 coin flips:", flips)
print(f"Heads: {flips.count('H')}, Tails: {flips.count('T')}")

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

---

## Part 4: Independence vs. Dependence

### Quick Check 4.1: Test Your Intuition

Which pairs of events are independent?
1. Flipping a coin twice: first flip and second flip
2. Drawing two cards from a deck WITHOUT replacement
3. Pixel brightness and pixel x-coordinate in a gradient image
4. Weather today and weather tomorrow
5. Current word and next word in a sentence

Write your predictions:

```python exec
id: 01-probability-foundations-page-2-1
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
# Your predictions and reasoning:
```

### Independence Definition

Events A and B are **independent** if:
$$P(A \cap B) = P(A) \times P(B)$$

Interpretation: Knowing A occurred doesn't change the probability of B.

### Example 4.1: Testing Coin Flip Independence

```python exec
id: 01-probability-foundations-page-2-2
# From our earlier simulation
first_heads = sum(1 for flip in double_flips if flip[0] == 'H')
second_heads = sum(1 for flip in double_flips if flip[1] == 'H')
both_heads = sum(1 for flip in double_flips if flip == 'HH')

prob_first_h = first_heads / len(double_flips)
prob_second_h = second_heads / len(double_flips)
prob_both_h = both_heads / len(double_flips)

expected_if_independent = prob_first_h * prob_second_h

print(f"P(First H) = {prob_first_h:.4f}")
print(f"P(Second H) = {prob_second_h:.4f}")
print(f"P(Both H) = {prob_both_h:.4f}")
print(f"\nIf independent: {expected_if_independent:.4f}")
print(f"Actual: {prob_both_h:.4f}")
print(f"\nDifference: {abs(expected_if_independent - prob_both_h):.6f}")
print("Coin flips ARE independent!")
```

### Try this 4.1: Test Image Independence

Using the top-bottom gradient image from earlier:
1. Calculate P(Dark) and P(Top)
2. Calculate P(Dark AND Top)
3. Calculate P(Dark) × P(Top)
4. Are they equal? What does this mean?
5. Why would these events NOT be independent?

```python exec
id: 01-probability-foundations-page-2-3
# YOUR CODE HERE
```

### Example 4.2: Words Are NOT Independent!

```python exec
id: 01-probability-foundations-page-2-4
# Simple text
text = "the doctor prescribed medicine the doctor prescribed rest the patient needed medicine the patient needed rest"
words = text.split()

# Calculate word probabilities
word_freq = Counter(words)
total_words = len(words)

print("Word probabilities:")
for word, count in word_freq.most_common():
    prob = count / total_words
    print(f"  P('{word}') = {prob:.3f}")

# Look at bigrams
bigrams = [(words[i], words[i+1]) for i in range(len(words)-1)]
bigram_freq = Counter(bigrams)

print("\nCommon bigrams:")
for bigram, count in bigram_freq.most_common(5):
    prob = count / len(bigrams)
    print(f"  P('{bigram[0]} {bigram[1]}') = {prob:.3f}")

# Test independence for "doctor" and "prescribed"
prob_doctor = word_freq['doctor'] / total_words
prob_prescribed = word_freq['prescribed'] / total_words
prob_doctor_prescribed = bigram_freq[('doctor', 'prescribed')] / len(bigrams)

expected = prob_doctor * prob_prescribed
print(f"\nTesting independence:")
print(f"P('doctor') × P('prescribed') = {expected:.4f}")
print(f"P('doctor prescribed') = {prob_doctor_prescribed:.4f}")
print(f"\nThese are NOT equal - words are DEPENDENT!")
print("This is why language models work!")
```

### Try this 4.2: Find Dependencies in Text

Create a longer text (at least 50 words) on any topic.
1. Calculate individual word probabilities
2. Calculate bigram probabilities
3. Find 3 pairs of consecutive words
4. Test each pair for independence
5. Which pairs show the strongest dependence?
6. Why do you think these specific pairs are dependent?

```python exec
id: 01-probability-foundations-page-2-5
# YOUR CODE HERE
```

---

## Part 5: Conditional Probability

### The Most Important Concept in AI

**Conditional probability** answers: "What's P(A) given that B occurred?"

Notation: P(A|B) (read: "probability of A given B")

Formula:
$$P(A|B) = \frac{P(A \cap B)}{P(B)}$$

### Quick Check 5.1: Intuition Test

Before seeing any formulas:
- You draw a card from a deck. It's red. What's P(it's a heart)?
- A pixel is in the top half of an image. What's P(it's dark) in our gradient image?
- The previous word is "doctor". What's P(next word is "prescribed")?

Write your intuitive answers:

```python exec
id: 01-probability-foundations-page-2-6
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
# Your intuitive answers:
```

### Example 5.1: The Medical Testing Paradox

This is the scenario from the beginning! A test for a rare disease:
- Disease affects 1% of population
- Test is 95% accurate (true positive rate)
- Test has 5% false positive rate

**Question**: If you test positive, what's P(you have the disease)?

```python exec
id: 01-probability-foundations-page-2-7
# Simulate population
population_size = 10000

# 1% have disease
has_disease = np.random.random(population_size) < 0.01

# Administer tests
test_results = np.zeros(population_size, dtype=bool)

# For diseased: 95% test positive
diseased_indices = np.where(has_disease)[0]
for idx in diseased_indices:
    test_results[idx] = np.random.random() < 0.95

# For healthy: 5% test positive (false positive)
healthy_indices = np.where(~has_disease)[0]
for idx in healthy_indices:
    test_results[idx] = np.random.random() < 0.05

# Analysis
true_positives = np.sum(has_disease & test_results)
false_positives = np.sum(~has_disease & test_results)
total_positive = np.sum(test_results)

print(f"Population: {population_size:,}")
print(f"Actually diseased: {np.sum(has_disease)}")
print(f"\nTest Results:")
print(f"  Total positive tests: {total_positive}")
print(f"  True positives: {true_positives}")
print(f"  False positives: {false_positives}")

# The key calculation
prob_disease_given_positive = true_positives / total_positive
print(f"\nP(Disease | Positive Test) = {prob_disease_given_positive:.4f}")
print(f"\nSurprise! Only {prob_disease_given_positive*100:.1f}% of positive tests are true!")
print("\nWhy? The disease is so rare that even a good test")
print("produces more false positives than true positives.")
```

### Try this 5.1: Visualize the Medical Test

Create a visualization to understand this paradox:
1. Make a 2×2 contingency table:
   - Rows: Has Disease (Yes/No)
   - Cols: Test Result (Positive/Negative)
2. Fill in the counts from the simulation
3. Highlight the true positive and false positive cells
4. Calculate and display P(Disease|Positive) visually
5. What happens if the disease affects 10% instead of 1%?

```python exec
id: 01-probability-foundations-page-2-8
# YOUR CODE HERE
# Hint: Can use plt.table() or create a custom visualization
```

### Example 5.2: Conditional Probability in Images

```python exec
id: 01-probability-foundations-page-2-9
# Using our gradient image
# Calculate P(Dark | Top half)
prob_dark_given_top = prob_dark_and_top / prob_top
print(f"P(Dark | Top half) = {prob_dark_given_top:.4f}")
print(f"P(Dark) overall = {prob_dark:.4f}")
print(f"\nDarkness is MORE likely given top half!")

# Calculate P(Dark | Bottom half)
is_bottom = ~is_top_half
prob_bottom = np.mean(is_bottom)
prob_dark_and_bottom = np.mean(is_dark & is_bottom)
prob_dark_given_bottom = prob_dark_and_bottom / prob_bottom

print(f"\nP(Dark | Bottom half) = {prob_dark_given_bottom:.4f}")
print(f"Darkness is LESS likely given bottom half!")
```

### Try this 5.2: Conditional Image Analysis

Create a 100×100 image with a specific pattern:
- Top-left quadrant: very dark (0-30)
- Top-right quadrant: dark (30-80)
- Bottom-left quadrant: bright (170-220)
- Bottom-right quadrant: very bright (220-255)

Calculate and compare:
1. P(Very dark | Top half)
2. P(Very dark | Left half)
3. P(Very dark | Top-left quadrant)
4. P(Very dark) overall
5. Create a visualization showing all four quadrants
6. Which condition gives the highest probability of very dark?

```python exec
id: 01-probability-foundations-page-2-10
# YOUR CODE HERE
```

### Example 5.3: Next Word Prediction with Context

```python exec
id: 01-probability-foundations-page-2-11
# Calculate P(prescribed | previous word is "doctor")
doctor_first_count = sum(count for (first, second), count in bigram_freq.items()
                         if first == 'doctor')
doctor_prescribed_count = bigram_freq[('doctor', 'prescribed')]

prob_prescribed_given_doctor = doctor_prescribed_count / doctor_first_count

print(f"P('prescribed' | 'doctor') = {prob_prescribed_given_doctor:.4f}")
print(f"P('prescribed') overall = {prob_prescribed:.4f}")
print(f"\nKnowing previous word is 'doctor' INCREASES probability!")
print("This is the foundation of language models.")
```

### Try this 5.3: Build a Better Predictor

Create a more complex text (at least 100 words) and build a bigram predictor:
1. For 5 different words, calculate P(next word | previous word)
2. Compare to P(next word) without context
3. Which previous words provide the most information?
4. Create a function that predicts the next word given a previous word
5. Test your predictor: given "the", what does it predict?
6. How accurate is it?

```python exec
id: 01-probability-foundations-page-2-12
# YOUR CODE HERE
```

---

## Part 6: Putting It All Together

### Try this 6.1: Email Spam Detection

You're building a spam filter with this data:
- 20% of emails are spam
- Word "free" appears in 60% of spam
- Word "free" appears in 5% of legitimate emails

Questions:
1. Calculate P("free" appears) overall
2. Calculate P(Spam | "free" appears)
3. If an email contains "free", how likely is it spam?
4. Simulate 10,000 emails to verify
5. Visualize the breakdown
6. How does this change if 50% of emails are spam?

**A question before moving on.** This program makes a judgement about a person. Who chose the threshold, and what happens to the person just on the wrong side of it? What does the program not know about them? What would you want said to them? Write a sentence or two; there is no right answer, and the question is the point.

```python exec
id: 01-probability-foundations-page-2-13
# YOUR CODE HERE
# Hint: Use law of total probability for P("free")
```

### Try this 6.2: Multi-Word Spam Detection

Extend the spam filter to use TWO words:
- P(Spam) = 0.20
- P("free" | Spam) = 0.60
- P("free" | Legit) = 0.05
- P("click" | Spam) = 0.50
- P("click" | Legit) = 0.10

Assume words appear independently given spam/legit.

Calculate:
1. P(Spam | "free" AND "click")
2. Compare to P(Spam | "free" only)
3. Does the second word provide more information?
4. Simulate to verify
5. What about emails with neither word?

**A question before moving on.** This program makes a judgement about a person. Who chose the threshold, and what happens to the person just on the wrong side of it? What does the program not know about them? What would you want said to them? Write a sentence or two; there is no right answer, and the question is the point.

```python exec
id: 01-probability-foundations-page-2-14
# YOUR CODE HERE
```

### Try this 6.3: Image Quality Assessment

Create a system to detect "low quality" images:
1. Generate 1000 images (50×50 each)
   - 30% are "low quality": mean brightness 30-70, high noise
   - 70% are "high quality": mean brightness 100-200, low noise
2. Define a test: brightness < 80 suggests low quality
3. Calculate:
   - P(Test says low quality | Actually low quality)
   - P(Test says low quality | Actually high quality)
   - P(Actually low quality | Test says low quality)
4. Visualize samples from each category
5. How good is your test?

```python exec
id: 01-probability-foundations-page-2-15
# YOUR CODE HERE
```

---

## Final Project: Multi-Modal Probability Analysis

### Project Description

Combine everything you've learned to build a comprehensive probability analyzer that works with images, text, and health data.

### Requirements

**Part A: Data Generation**
1. Generate 500 patient records, each with:
   - Medical scan image (100×100 pixels)
   - Doctor's note (text, 20-30 words)
   - Test result (positive/negative)
2. Create realistic dependencies:
   - Positive tests correlate with darker image regions
   - Certain words correlate with positive tests
   - Image brightness correlates with specific words

**Part B: Probability Analysis**
1. Calculate basic probabilities for each modality
2. Test independence between modalities
3. Calculate conditional probabilities:
   - P(Positive | Dark image)
   - P(Positive | Specific word appears)
   - P(Positive | Dark image AND specific word)

**Part C: Visualization**
1. Create comprehensive visualizations showing:
   - Distribution of each feature
   - Contingency tables
   - Conditional probability comparisons
2. Display sample images with their labels and text

**Part D: Analysis Report**
Write a summary addressing:
1. Which features are most predictive?
2. Which pairs show strongest dependence?
3. How does conditional probability improve prediction?
4. What are the limitations of your analysis?

### Bonus Challenges
- Implement a simple classifier using probability
- Compare performance with/without conditioning
- Analyze how sample size affects probability estimates
- Handle missing data (some patients missing images or text)

```python exec
id: 01-probability-foundations-page-2-16
# YOUR PROJECT CODE HERE
```

---

## Summary and Reflection

### What You've Learned

**Core Concepts:**
1. Sample spaces and events
2. Probability scales (0 to 1)
3. Compound events (AND, OR, NOT)
4. Independence and dependence
5. Conditional probability

**Key Formulas:**
- Basic probability: P(E) = favorable / total
- Addition rule: P(A∪B) = P(A) + P(B) - P(A∩B)
- Independence: P(A∩B) = P(A) × P(B)
- Conditional: P(A|B) = P(A∩B) / P(B)

**Applications:**
- Image analysis: pixel distributions, regions, features
- NLP: word prediction, bigrams, context
- Health: medical testing, diagnosis, risk assessment

### Reflection Questions

**Understanding:**
1. Why is conditional probability more useful than unconditional probability?
2. When are events independent in practice?
3. How does the medical testing paradox challenge your intuition?

**Application:**
1. Where else in AI would conditional probability be crucial?
2. How might you use these concepts in your own projects?
3. What patterns of dependence exist in your domain of interest?

**Critical Thinking:**
1. What are limitations of probability models?
2. How much data do you need for reliable probability estimates?
3. When might simulation be better than calculation?

### Looking Ahead

In Notebook 2, we'll learn:
- Counting principles for calculating probabilities
- Permutations and combinations
- Applications to complex probability problems
- Connection to machine learning sample spaces

### Final Thought

Probability isn't just mathematics - it's a way of thinking about uncertainty. Every time an AI makes a prediction, it's calculating conditional probabilities. Every time you see a confidence score, someone estimated a probability. You now understand the foundations of how machines reason about uncertainty.

The medical testing paradox shows why: Even with accurate tests, rare events require careful probabilistic reasoning. The same principle applies everywhere in AI: context matters, prior probabilities matter, and our intuition can mislead us.

Keep asking: What's the sample space? Are events independent? What information am I conditioning on?

## Looking back

Before leaving this page, a sentence on each. What you write stays on this device.

```reflect
- Something you expected before running a cell that turned out differently
- The one idea from this page you could explain to someone else now
- Something you would change or try next, if there were time
- A question this page raised for you that it did not answer. Bring it to the next session; these questions are where the next session starts.
```
