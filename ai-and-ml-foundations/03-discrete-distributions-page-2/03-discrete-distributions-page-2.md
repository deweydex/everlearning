---
title: "03-discrete-distributions-page-2 (2 of 2)"
slug: 03-discrete-distributions-page-2
course: ai-and-ml-foundations
course_title: "AI and ML Foundations"
series: 3-probability-and-statistics
series_title: "Probability and Statistics"
version: 2026.09.06.1
---

Before starting this page, run the cell below. It repeats the imports and definitions from the earlier pages that this page uses.

```python exec
id: 03-discrete-distributions-page-2-setup
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
from scipy import stats
import math

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

p_disease = 0.1

# Visualize
x_values = [0, 1]
probabilities = [1 - p_disease, p_disease]

plot_pmf(x_values, probabilities,
         title="Bernoulli Distribution: Disease (p=0.1)",
         xlabel="Has Disease (0=No, 1=Yes)")

print(f"Expected value: {p_disease}")
print(f"Variance: {p_disease * (1-p_disease):.4f}")

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

---

## Part 4: Geometric Distribution

### Quick Check 4.1: Waiting Times

You're looking for the word "rare" in text. It appears in 2% of sentences.

Before any calculations:
- About how many sentences until you find it?
- Is finding it on the 1st sentence more likely than the 50th?
- Sketch what the distribution might look like

```python exec
id: 03-discrete-distributions-page-2-1
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
# Your predictions:
```

### The Geometric Distribution

Models: number of trials until first success

**Notation**: X ~ Geometric(p)

**PMF**:
$$P(X = k) = (1-p)^{k-1} p$$

Interpretation: (k-1) failures, then 1 success

**Expected Value**: E[X] = 1/p

**Variance**: Var(X) = (1-p)/p²

### Example 4.1: Finding a Rare Word

```python exec
id: 03-discrete-distributions-page-2-2
p_rare = 0.02

k_values = np.arange(1, 101)
pmf_values = [stats.geom.pmf(k, p_rare) for k in k_values]

plt.figure(figsize=(12, 6))
plt.bar(k_values[:100], pmf_values[:100], edgecolor='black', alpha=0.7)
plt.xlabel("Sentence Number", fontsize=12)
plt.ylabel("Probability", fontsize=12)
plt.title(f"Geometric Distribution: Finding rare word (p={p_rare})", fontsize=14, weight='bold')
plt.grid(True, alpha=0.3, axis='y')
plt.show()

expected = 1 / p_rare
variance = (1 - p_rare) / (p_rare ** 2)

print(f"Expected waiting time: {expected:.1f} sentences")
print(f"Standard deviation: {np.sqrt(variance):.1f}")

# Probabilities
prob_within_10 = stats.geom.cdf(10, p_rare)
prob_more_than_50 = 1 - stats.geom.cdf(50, p_rare)

print(f"\nP(find within 10 sentences) = {prob_within_10:.4f}")
print(f"P(need more than 50) = {prob_more_than_50:.4f}")
```

### Try this 4.1: Simulate Waiting Times

1. Simulate finding the rare word 10000 times
2. Record the waiting time for each trial
3. Plot histogram vs theoretical distribution
4. Calculate empirical mean vs theoretical
5. What's the longest wait you observed?
6. What's the median waiting time?

```python exec
id: 03-discrete-distributions-page-2-3
# YOUR CODE HERE
```

### Example 4.2: Medical Diagnosis Search

```python exec
id: 03-discrete-distributions-page-2-4
# Rare disease: 0.5% prevalence
p_rare_disease = 0.005

# Simulate
num_simulations = 10000
waiting_times = []

for _ in range(num_simulations):
    trials = 0
    while True:
        trials += 1
        if np.random.random() < p_rare_disease:
            break
        if trials > 1000:
            break
    waiting_times.append(trials)

plt.figure(figsize=(12, 6))
plt.hist(waiting_times, bins=50, density=True, alpha=0.7, edgecolor='black')
plt.axvline(x=1/p_rare_disease, color='r', linestyle='--', linewidth=2, 
            label=f'Expected = {1/p_rare_disease:.0f}')
plt.xlabel("Patients Screened", fontsize=12)
plt.ylabel("Density", fontsize=12)
plt.title(f"Waiting for Rare Disease (p={p_rare_disease})", fontsize=14, weight='bold')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()

print(f"Expected: {1/p_rare_disease:.1f} patients")
print(f"Simulated mean: {np.mean(waiting_times):.1f}")
print(f"Simulated median: {np.median(waiting_times):.1f}")
print(f"\nNote: Mean > Median (right-skewed distribution)")
```

### Try this 4.2: Compare Multiple Scenarios

Analyze waiting times for:
- Event A: p = 0.01 (1%)
- Event B: p = 0.05 (5%)
- Event C: p = 0.10 (10%)

For each:
1. Plot the geometric distribution
2. Calculate expected waiting time
3. Simulate 5000 trials
4. Compare mean vs median
5. Calculate probability of waiting > 2×expected
6. Create a comparison visualization

```python exec
id: 03-discrete-distributions-page-2-5
# YOUR CODE HERE
```

### Try this 4.3: Memoryless Property

The geometric distribution is memoryless:
P(X > s+t | X > s) = P(X > t)

Verify this property:
1. Generate 10000 waiting times from Geometric(0.1)
2. Filter for times > 5 (already waited 5 trials)
3. Among those, calculate P(need 3 more trials)
4. Compare to original P(need 3 trials)
5. Are they equal?
6. Why does this make sense?

```python exec
id: 03-discrete-distributions-page-2-6
# YOUR CODE HERE
```

---

## Part 5: Poisson Distribution

### Quick Check 5.1: Pattern Recognition

Which scenarios might follow similar patterns?
- Typos per page in a book
- Patients arriving per hour at ER
- Emails received per day
- Pixels with errors in an image
- Traffic accidents per week

What do they have in common?

```python exec
id: 03-discrete-distributions-page-2-7
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
# Your observations:
```

### The Poisson Distribution

Models: number of rare events in a fixed interval

**Notation**: X ~ Poisson(λ)

**PMF**:
$$P(X = k) = \frac{e^{-\lambda} \lambda^k}{k!}$$

**Expected Value**: E[X] = λ

**Variance**: Var(X) = λ

**Key Property**: Mean = Variance!

### Example 5.1: Typos in Documents

```python exec
id: 03-discrete-distributions-page-2-8
lambda_typos = 2.0

k_values = np.arange(0, 11)
pmf_values = [stats.poisson.pmf(k, lambda_typos) for k in k_values]

plot_pmf(k_values, pmf_values,
         title=f"Poisson Distribution: Typos per page (λ={lambda_typos})",
         xlabel="Number of Typos")

prob_exactly_3 = stats.poisson.pmf(3, lambda_typos)
prob_at_most_1 = stats.poisson.cdf(1, lambda_typos)
prob_more_than_4 = 1 - stats.poisson.cdf(4, lambda_typos)

print(f"P(exactly 3 typos) = {prob_exactly_3:.4f}")
print(f"P(at most 1 typo) = {prob_at_most_1:.4f}")
print(f"P(more than 4 typos) = {prob_more_than_4:.4f}")
```

### Try this 5.1: Document Quality Control

A publishing house has three quality tiers:
- Excellent: λ = 0.5 typos/page
- Good: λ = 2.0 typos/page
- Poor: λ = 5.0 typos/page

For each tier:
1. Plot the distribution
2. Calculate P(0 typos)
3. Calculate P(more than 3 typos)
4. Simulate 1000 pages
5. What's the maximum typos you'd expect?
6. Create a comparison visualization

```python exec
id: 03-discrete-distributions-page-2-9
# YOUR CODE HERE
```

### Example 5.2: Emergency Room Arrivals

```python exec
id: 03-discrete-distributions-page-2-10
lambda_patients = 5.0

k_values = np.arange(0, 16)
pmf_values = [stats.poisson.pmf(k, lambda_patients) for k in k_values]

plot_pmf(k_values, pmf_values,
         title=f"Poisson: ER Patients per hour (λ={lambda_patients})",
         xlabel="Number of Patients")

print(f"Expected: {lambda_patients}")
print(f"Std dev: {np.sqrt(lambda_patients):.2f}")

prob_exactly_5 = stats.poisson.pmf(5, lambda_patients)
prob_between_3_and_7 = sum(stats.poisson.pmf(k, lambda_patients) for k in range(3, 8))
prob_more_than_10 = 1 - stats.poisson.cdf(10, lambda_patients)

print(f"\nP(exactly 5) = {prob_exactly_5:.4f}")
print(f"P(between 3 and 7) = {prob_between_3_and_7:.4f}")
print(f"P(more than 10) = {prob_more_than_10:.4f}")
```

### Try this 5.2: Staffing Analysis

The ER must have enough staff for the patient load.

1. Calculate P(need k doctors) for k = 1 to 15
2. If each doctor handles 2 patients/hour, how many needed?
3. What staffing level covers 95% of scenarios?
4. What about 99%?
5. Simulate 1000 hours of arrivals
6. Calculate understaffing frequency for different levels

```python exec
id: 03-discrete-distributions-page-2-11
# YOUR CODE HERE
```

### Try this 5.3: Image Noise Analysis

Pixel errors follow Poisson(λ=0.3 per 100 pixels).

For a 1000×1000 image:
1. Calculate expected total errors
2. Calculate variance
3. Simulate 100 images
4. Plot distribution of error counts
5. What's P(more than 350 errors)?
6. If error rate increases to λ=0.5, how does this change?

```python exec
id: 03-discrete-distributions-page-2-12
# YOUR CODE HERE
```

---

## Part 6: Monte Carlo Simulation

### What is Monte Carlo?

Use random sampling to approximate complex probability calculations.

Basic process:
1. Generate many random samples
2. Count favorable outcomes
3. Estimate probability: favorable/total

### Example 6.1: Estimating π

```python exec
id: 03-discrete-distributions-page-2-13
def estimate_pi(num_samples):
    """Estimate π using Monte Carlo."""
    x = np.random.random(num_samples)
    y = np.random.random(num_samples)
    inside = (x**2 + y**2) <= 1
    return 4 * np.sum(inside) / num_samples, x, y, inside

pi_est, x, y, inside = estimate_pi(10000)

plt.figure(figsize=(8, 8))
plt.scatter(x[inside], y[inside], c='red', s=1, alpha=0.5)
plt.scatter(x[~inside], y[~inside], c='blue', s=1, alpha=0.5)
plt.xlabel('x', fontsize=12)
plt.ylabel('y', fontsize=12)
plt.title(f'Monte Carlo π\nEstimate: {pi_est:.4f}, Actual: {np.pi:.4f}', 
          fontsize=14, weight='bold')
plt.axis('equal')
plt.grid(True, alpha=0.3)
plt.show()

print(f"Error: {abs(pi_est - np.pi):.6f}")
```

### Try this 6.1: Convergence Analysis

Study how estimate improves with sample size:
1. Run Monte Carlo with N = 10, 100, 1000, 10000, 100000
2. Plot estimate vs N
3. Plot error vs N (log scale)
4. How fast does error decrease?
5. Repeat 10 times for each N to measure variability
6. Plot error bars showing variance

```python exec
id: 03-discrete-distributions-page-2-14
# YOUR CODE HERE
```

### Try this 6.2: Medical Risk Assessment

A patient has multiple risk factors:
- Smoker: increases risk by 2×
- Age > 50: increases by 1.5×
- Family history: increases by 1.3×
- Base risk: 5%

Use Monte Carlo to:
1. Simulate 10000 patients with all three risk factors
2. Calculate disease rate
3. Compare to patients with no risk factors
4. Test each risk factor individually
5. Create visualization of all scenarios
6. Which factor has biggest impact?

```python exec
id: 03-discrete-distributions-page-2-15
# YOUR CODE HERE
```

### Try this 6.3: Complex Image Noise

Combine multiple noise sources:
- Gaussian noise: N(0, σ=15)
- Poisson noise: λ=10
- Salt-and-pepper: 5% of pixels

1. Create clean 100×100 checkerboard
2. Add all three noise types
3. Simulate 100 noisy versions
4. Calculate average signal-to-noise ratio
5. Visualize noise distribution
6. Which noise type dominates?

```python exec
id: 03-discrete-distributions-page-2-16
# YOUR CODE HERE
```

---

## Final Project: Multi-Distribution Analysis

### Project Description

Analyze a complex system using multiple probability distributions.

### Scenario: Medical Clinic Operations

Model a clinic with:
- Patient arrivals: Poisson(λ=5 per hour)
- Disease prevalence: Binomial(n=patients, p=0.15)
- Wait for first critical case: Geometric(p=0.05)
- Individual diagnosis: Bernoulli(p=varies by patient)

### Requirements

**Part A: Individual Distributions**
1. Model each process separately
2. Calculate theoretical statistics
3. Generate visualizations
4. Verify with simulation

**Part B: System Simulation**
1. Simulate 100 hours of clinic operation
2. Track all metrics:
   - Total patients
   - Diseased patients
   - Time to critical case
   - Resource utilization

**Part C: Analysis**
1. Compare simulated vs theoretical
2. Identify bottlenecks
3. Calculate probability of overcrowding
4. Optimize staffing levels

**Part D: Visualization Dashboard**
1. Create comprehensive visualization
2. Show all distributions
3. Highlight key statistics
4. Compare scenarios

**Part E: Report**
1. Summarize findings
2. Make recommendations
3. Discuss limitations
4. Propose improvements

### Bonus Challenges
- Add time-varying arrival rates
- Model patient urgency levels
- Implement priority queue
- Optimize for multiple objectives

```python exec
id: 03-discrete-distributions-page-2-17
# YOUR PROJECT CODE HERE
```

---

## Summary and Reflection

### Key Distributions

| Distribution | Use Case | Parameters | Mean | Variance |
|--------------|----------|------------|------|----------|
| Bernoulli | Single trial | p | p | p(1-p) |
| Binomial | n trials | n, p | np | np(1-p) |
| Geometric | Wait for success | p | 1/p | (1-p)/p² |
| Poisson | Rare events | λ | λ | λ |

### Reflection Questions

**Pattern Recognition:**
1. How do you identify which distribution fits a scenario?
2. What assumptions does each distribution make?
3. When might these assumptions be violated?

**Applications:**
1. Where else have you seen these patterns?
2. How do distributions simplify probability calculations?
3. What's the connection between distributions and real data?

**Simulation:**
1. When is simulation better than calculation?
2. How do you verify simulation accuracy?
3. What's the trade-off between precision and computation?

### Looking Ahead

In Notebook 4:
- Continuous distributions (Normal, Exponential, Uniform)
- Central Limit Theorem
- Z-scores and standardization
- Real-world measurement data

### Final Thought

Discrete distributions are the building blocks of probability theory. They transform infinite possible scenarios into tractable mathematical models. Master these four distributions, and you'll recognize patterns everywhere - from text analysis to image processing to medical diagnosis.

The key insight: repetition creates patterns. Whether it's coin flips, pixel values, or patient arrivals, when we repeat similar random processes, predictable distributions emerge. This is why statistics works - and why AI can learn from data.

## Looking back

Before leaving this page, a sentence on each. What you write stays on this device.

```reflect
- Something you expected before running a cell that turned out differently
- The one idea from this page you could explain to someone else now
- Something you would change or try next, if there were time
- A question this page raised for you that it did not answer. Bring it to the next session; these questions are where the next session starts.
```
