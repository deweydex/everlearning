---
title: "Notebook 3: Discrete Probability Distributions (1 of 2)"
slug: 03-discrete-distributions-page-1
course: ai-and-ml-foundations
course_title: "AI and ML Foundations"
series: 3-probability-and-statistics
series_title: "Probability and Statistics"
version: 2026.09.06.1
---

# Notebook 3: Discrete Probability Distributions

## Part 0: From Counting to Patterns

In Notebooks 1-2, we calculated probabilities for specific events. But many real-world scenarios follow **repeatable patterns** - probability structures that appear across different contexts.

### Quick Check 0.1: Recognize the Pattern

Before learning about distributions, consider these scenarios:

**Scenario A**: Flip a coin 10 times. Count the heads.
**Scenario B**: Test 10 patients for a disease (10% prevalence). Count positive cases.
**Scenario C**: Sample 10 pixels from an image (20% are bright). Count bright pixels.

What do these three scenarios have in common? Write your thoughts:

```python exec
id: 03-discrete-distributions-page-1-1
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
# Your observations:
```

### Why Study Distributions?

These patterns are called **probability distributions**. Instead of deriving probabilities from scratch each time, we recognize the pattern and use a mathematical model.

### What You'll Learn

This notebook covers four key discrete distributions:
1. **Bernoulli**: Single yes/no trial
2. **Binomial**: n independent yes/no trials
3. **Geometric**: Waiting for first success
4. **Poisson**: Counting rare events
5. **Expected Value & Variance**: Measuring center and spread
6. **Monte Carlo Simulation**: Computational probability

---

## Part 1: Random Variables

```python exec
id: 03-discrete-distributions-page-1-2
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
from scipy import stats
import math

np.random.seed(42)

def plot_pmf(x_values, probabilities, title, xlabel="Value", ylabel="Probability"):
    """Plot probability mass function."""
    plt.figure(figsize=(10, 6))
    plt.bar(x_values, probabilities, edgecolor='black', alpha=0.7)
    plt.xlabel(xlabel, fontsize=12)
    plt.ylabel(ylabel, fontsize=12)
    plt.title(title, fontsize=14, weight='bold')
    plt.grid(True, alpha=0.3, axis='y')
    plt.tight_layout()
    plt.show()
```

### What is a Random Variable?

A **random variable** is a numerical value determined by chance.

Examples:
- X = number of heads in 10 coin flips (values: 0, 1, 2, ..., 10)
- Y = number of bright pixels in a sample (values: 0, 1, 2, ...)
- Z = number of times word "the" appears in a paragraph

The **probability mass function (PMF)** gives P(X = k) for each possible value k.

### Try this 1.1: Create Your Own Random Variable

Define a random variable for:
1. Number of emails received in an hour
2. Number of typos in a page
3. Number of dark pixels in a 3×3 image region

For each:
- What are the possible values?
- Simulate 20 observations
- Plot a histogram

```python exec
id: 03-discrete-distributions-page-1-3
# YOUR CODE HERE
```

---

## Part 2: Bernoulli Distribution

### Quick Check 2.1: One Trial

A coin flip has two outcomes. How would you represent this numerically?
- Heads = ???
- Tails = ???

Why might 1 and 0 be good choices?

```python exec
id: 03-discrete-distributions-page-1-4
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
# Your reasoning:
```

### The Bernoulli Distribution

Models a single trial with two outcomes:
- Success (1) with probability p
- Failure (0) with probability 1-p

**Notation**: X ~ Bernoulli(p)

**PMF**:
- P(X = 1) = p
- P(X = 0) = 1 - p

**Expected Value**: E[X] = p

**Variance**: Var(X) = p(1-p)

### Example 2.1: Disease Prevalence

```python exec
id: 03-discrete-distributions-page-1-5
p_disease = 0.1

# Visualize
x_values = [0, 1]
probabilities = [1 - p_disease, p_disease]

plot_pmf(x_values, probabilities,
         title="Bernoulli Distribution: Disease (p=0.1)",
         xlabel="Has Disease (0=No, 1=Yes)")

print(f"Expected value: {p_disease}")
print(f"Variance: {p_disease * (1-p_disease):.4f}")
```

### Try this 2.1: Simulate and Verify

1. Simulate 1000 Bernoulli trials with p=0.1
2. Calculate sample mean and compare to theoretical mean
3. Calculate sample variance and compare to theoretical variance
4. Plot histogram of results
5. What happens as you increase sample size?

```python exec
id: 03-discrete-distributions-page-1-6
# YOUR CODE HERE
```

### Example 2.2: Word Occurrence

```python exec
id: 03-discrete-distributions-page-1-7
# Word "diagnosis" appears in 15% of medical sentences
p_word = 0.15

# Simulate 1000 sentences
num_sentences = 1000
contains_word = np.random.random(num_sentences) < p_word

num_with_word = np.sum(contains_word)
observed_prob = num_with_word / num_sentences

print(f"Simulated {num_sentences} sentences")
print(f"Sentences with 'diagnosis': {num_with_word}")
print(f"Observed probability: {observed_prob:.4f}")
print(f"Expected probability: {p_word:.4f}")
```

### Try this 2.2: Text Analysis with Bernoulli

Analyze word presence in sentences:
1. Create a list of 10 different words with their probabilities
2. Simulate 500 sentences, each checking for word presence
3. For each word, calculate observed vs expected frequency
4. Which words appear most/least often?
5. Create a visualization comparing all words
6. Calculate total variance across all words

```python exec
id: 03-discrete-distributions-page-1-8
# YOUR CODE HERE
```

### Try this 2.3: Pixel Classification

In an image, 30% of pixels are "edges" (high gradient).

1. Model edge detection as Bernoulli(0.3)
2. Simulate classifying 10000 pixels
3. Calculate expected edges vs actual
4. What if the classifier is imperfect (95% accuracy)?
5. How does this affect the variance?

```python exec
id: 03-discrete-distributions-page-1-9
# YOUR CODE HERE
```

---

## Part 3: Binomial Distribution

### Quick Check 3.1: Predict the Distribution

Before seeing any code:
- Flip 10 fair coins
- What's the most likely number of heads?
- Is 0 heads or 5 heads more likely?
- Sketch what you think the distribution looks like

```python exec
id: 03-discrete-distributions-page-1-10
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
# Your predictions:
```

### The Binomial Distribution

Models: number of successes in n independent Bernoulli trials

**Notation**: X ~ Binomial(n, p)

**PMF**:
$$P(X = k) = \binom{n}{k} p^k (1-p)^{n-k}$$

**Expected Value**: E[X] = np

**Variance**: Var(X) = np(1-p)

### Example 3.1: Coin Flips

```python exec
id: 03-discrete-distributions-page-1-11
n_flips = 10
p_heads = 0.5

k_values = np.arange(0, n_flips + 1)
pmf_values = [stats.binom.pmf(k, n_flips, p_heads) for k in k_values]

plot_pmf(k_values, pmf_values,
         title=f"Binomial Distribution: Coin Flips (n={n_flips}, p={p_heads})",
         xlabel="Number of Heads")

expected = n_flips * p_heads
variance = n_flips * p_heads * (1 - p_heads)

print(f"Expected heads: {expected}")
print(f"Standard deviation: {np.sqrt(variance):.2f}")
print(f"Most likely outcome: {k_values[np.argmax(pmf_values)]} heads")
```

### Try this 3.1: Explore Parameters

How do n and p affect the distribution?

Create visualizations showing:
1. Fixed p=0.5, varying n: 5, 10, 20, 50
2. Fixed n=20, varying p: 0.1, 0.3, 0.5, 0.7, 0.9
3. What patterns do you notice?
4. When is the distribution symmetric?
5. How does variance change with n? with p?

```python exec
id: 03-discrete-distributions-page-1-12
# YOUR CODE HERE
```

### Example 3.2: Medical Testing at Scale

```python exec
id: 03-discrete-distributions-page-1-13
n_patients = 100
p_disease = 0.20

k_values = np.arange(0, n_patients + 1)
pmf_values = [stats.binom.pmf(k, n_patients, p_disease) for k in k_values]

# Plot reasonable range
plot_range = (5, 35)
k_plot = k_values[plot_range[0]:plot_range[1]]
pmf_plot = pmf_values[plot_range[0]:plot_range[1]]

plot_pmf(k_plot, pmf_plot,
         title=f"Binomial: Diseased Patients (n={n_patients}, p={p_disease})",
         xlabel="Number with Disease")

expected = n_patients * p_disease
std_dev = np.sqrt(n_patients * p_disease * (1 - p_disease))

print(f"Expected: {expected}")
print(f"Std dev: {std_dev:.2f}")
print(f"Likely range: {expected - std_dev:.1f} to {expected + std_dev:.1f}")

# Specific probabilities
prob_exactly_20 = stats.binom.pmf(20, n_patients, p_disease)
prob_at_least_25 = 1 - stats.binom.cdf(24, n_patients, p_disease)
prob_less_than_15 = stats.binom.cdf(14, n_patients, p_disease)

print(f"\nP(exactly 20) = {prob_exactly_20:.4f}")
print(f"P(at least 25) = {prob_at_least_25:.4f}")
print(f"P(less than 15) = {prob_less_than_15:.4f}")
```

### Try this 3.2: Medical Screening Analysis

A hospital screens 200 patients for three different conditions:
- Condition A: 5% prevalence
- Condition B: 15% prevalence
- Condition C: 25% prevalence

For each condition:
1. Plot the distribution of positive cases
2. Calculate probability of 0 positive cases
3. Calculate 95% confidence interval (2 std devs)
4. Simulate 1000 screening days
5. Compare simulation to theory
6. Which condition shows most variability? Why?

```python exec
id: 03-discrete-distributions-page-1-14
# YOUR CODE HERE
```

### Example 3.3: Character Frequencies in Text

```python exec
id: 03-discrete-distributions-page-1-15
# Letter 'e' appears with p=0.127 in English
n_chars = 100
p_letter_e = 0.127

# Simulate 10000 samples
num_samples = 10000
counts_of_e = []

for _ in range(num_samples):
    sample = np.random.random(n_chars) < p_letter_e
    counts_of_e.append(np.sum(sample))

# Theoretical distribution
k_values = np.arange(0, 30)
theoretical_pmf = [stats.binom.pmf(k, n_chars, p_letter_e) for k in k_values]

# Plot
plt.figure(figsize=(10, 6))
plt.hist(counts_of_e, bins=range(0, 30), density=True, alpha=0.7, edgecolor='black')
plt.plot(k_values, theoretical_pmf, 'ro-', linewidth=2, markersize=8, label='Theoretical')
plt.xlabel("Count of 'e'", fontsize=12)
plt.ylabel("Probability", fontsize=12)
plt.title("Letter 'e' in 100-character samples", fontsize=14, weight='bold')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()

simulated_mean = np.mean(counts_of_e)
theoretical_mean = n_chars * p_letter_e
print(f"Simulated mean: {simulated_mean:.2f}")
print(f"Theoretical mean: {theoretical_mean:.2f}")
```

### Try this 3.3: Multi-Character Analysis

English letter frequencies:
- 'e': 12.7%, 't': 9.1%, 'a': 8.2%, 'o': 7.5%, 'i': 7.0%

For 200-character samples:
1. Model each letter with Binomial
2. Simulate 1000 samples
3. Plot distributions for all 5 letters (subplots)
4. Calculate correlation between letter counts
5. Which pair shows strongest correlation?
6. Does this make linguistic sense?

```python exec
id: 03-discrete-distributions-page-1-16
# YOUR CODE HERE
```

### Try this 3.4: Image Patch Analysis

In 10×10 pixel patches:
- 40% of patches contain edges
- You sample 50 random patches

1. Model as Binomial(50, 0.4)
2. What's P(exactly 20 patches have edges)?
3. What's P(at least 25 have edges)?
4. Calculate the most likely outcome
5. Simulate 10000 trials
6. Visualize simulation vs theory

```python exec
id: 03-discrete-distributions-page-1-17
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
