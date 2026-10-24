---
title: "Notebook 4: Continuous Distributions (1 of 2)"
slug: 04-continuous-distributions-page-1
course: ai-and-ml-foundations
course_title: "AI and ML Foundations"
series: 3-probability-and-statistics
series_title: "Probability and Statistics"
version: 2026.09.06.1
---

# Notebook 4: Continuous Distributions

## From Discrete to Continuous

In the previous notebook, we worked with **discrete** distributions: outcomes you could count (0, 1, 2, 3, ...).

But many real-world measurements are **continuous**: they can take any value in a range.

### Examples of Continuous Data

**Images:**
- Pixel brightness: 0.0 to 255.0 (not just integers!)
- Color intensity: 0.0 to 1.0
- Image similarity scores: any value between 0 and 1

**Natural Language:**
- Word embedding coordinates: any real number
- Sentiment scores: -1.0 to +1.0
- Attention weights: 0.0 to 1.0

**Health Measurements:**
- Height, weight, temperature
- Blood pressure, heart rate
- Time between events

For continuous data, we can't ask "What's the probability of exactly 172.83491... cm?" because there are infinitely many possible values. Instead, we ask: **"What's the probability of being in a range?"**

This notebook explores:
1. **Probability Density Functions (PDFs)**: The continuous equivalent of PMFs
2. **Uniform Distribution**: All values equally likely
3. **Normal (Gaussian) Distribution**: The most important distribution in statistics
4. **Central Limit Theorem**: Why normal distributions appear everywhere
5. **Exponential Distribution**: Time between events
6. **Applications**: Image analysis, NLP embeddings, measurement data

---

## Part 1: Understanding Continuous Probability

### Try this 1.1: Think Before You Code

Before we write any code, think about this:

You measure the height of 1000 people. Two people are both 172 cm tall, but one is 172.41 cm and the other is 172.89 cm. If your measuring device only shows whole centimeters, they both appear as "172 cm".

**Question**: What happens as your measuring device becomes more precise? How does this relate to probability?

```python exec
id: 04-continuous-distributions-page-1-1
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import warnings
warnings.filterwarnings('ignore')

np.random.seed(42)
```

### From Discrete to Continuous: A Simulation

```python exec
id: 04-continuous-distributions-page-1-2
# Generate 10000 random heights (normally distributed around 170 cm)
true_heights = np.random.normal(170, 10, size=10000)

# Simulate measuring with different precision levels
precision_levels = [1, 0.1, 0.01, 0.001]  # cm

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
axes = axes.flatten()

for i, precision in enumerate(precision_levels):
    # Round to given precision
    measured_heights = np.round(true_heights / precision) * precision
    
    # Plot histogram
    axes[i].hist(measured_heights, bins=50, edgecolor='black', alpha=0.7)
    axes[i].set_xlabel('Height (cm)', fontsize=11)
    axes[i].set_ylabel('Frequency', fontsize=11)
    axes[i].set_title(f'Precision: {precision} cm', fontsize=12, weight='bold')
    axes[i].grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

print("Notice: As precision increases, the histogram becomes smoother.")
print("In the limit, it approaches a smooth curve: the probability density function.")
```

### Try this 1.2: Explore Precision

Modify the code above to:
1. Change the number of samples from 10000 to 1000 and then to 100000
2. Observe how the histograms change
3. What happens with more data?

**Write your observations below:**

```python exec
id: 04-continuous-distributions-page-1-3
# YOUR EXPLORATION HERE
```

### Probability Density Functions (PDFs)

For continuous distributions, we use a **probability density function** f(x).

Key properties:
- f(x) ≥ 0 for all x
- The area under the entire curve = 1
- P(a ≤ X ≤ b) = area under curve from a to b

**Important**: f(x) is NOT a probability! It's a density. The probability is the area under the curve.

---

## Part 2: Uniform Distribution

The **uniform distribution** assigns equal probability to all values in an interval [a, b].

**Notation**: X ~ Uniform(a, b)

**PDF**:
$$f(x) = \begin{cases} 
\frac{1}{b-a} & \text{if } a \leq x \leq b \\
0 & \text{otherwise}
\end{cases}$$

**Mean**: (a + b) / 2

**Variance**: (b - a)² / 12

### Example 2.1: Random Image Initialization

In deep learning, we often initialize weights uniformly between -0.1 and 0.1.

```python exec
id: 04-continuous-distributions-page-1-4
# Generate uniform samples
a, b = -0.1, 0.1
samples = np.random.uniform(a, b, size=10000)

# Plot
plt.figure(figsize=(10, 6))
plt.hist(samples, bins=50, density=True, alpha=0.7, edgecolor='black', label='Sample histogram')

# Overlay theoretical PDF
x = np.linspace(a - 0.05, b + 0.05, 1000)
pdf = np.where((x >= a) & (x <= b), 1/(b-a), 0)
plt.plot(x, pdf, 'r-', linewidth=2, label='Theoretical PDF')

plt.xlabel('Value', fontsize=12)
plt.ylabel('Density', fontsize=12)
plt.title('Uniform Distribution: Weight Initialization', fontsize=14, weight='bold')
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

# Calculate statistics
print(f"Theoretical mean: {(a+b)/2:.4f}")
print(f"Sample mean: {np.mean(samples):.4f}")
print(f"\nTheoretical variance: {(b-a)**2/12:.6f}")
print(f"Sample variance: {np.var(samples):.6f}")
```

### Try this 2.1: Pixel Brightness

You're generating a random image where each pixel brightness is uniformly distributed between 0 and 255.

1. Generate a 50×50 image with uniform random pixels
2. Display the image
3. Calculate the mean brightness
4. Create a histogram of pixel values
5. What would you expect the mean to be? Does your result match?

```python exec
id: 04-continuous-distributions-page-1-5
# YOUR CODE HERE
# Hint: np.random.uniform(low, high, size=(rows, cols))
# Hint: plt.imshow(image, cmap='gray', vmin=0, vmax=255)
```

### Try this 2.2: Random Attention Weights

In transformer models, attention weights are initially random before training.

1. Generate 1000 attention weights uniformly between 0 and 1
2. Normalize them so they sum to 1 (divide each by the sum)
3. Plot a histogram of the normalized weights
4. Are they still uniformly distributed? Why or why not?

```python exec
id: 04-continuous-distributions-page-1-6
# YOUR CODE HERE
```

---

## Part 3: Normal (Gaussian) Distribution

The **normal distribution** is the most important distribution in statistics and machine learning.

**Notation**: X ~ Normal(μ, σ²) or X ~ N(μ, σ²)
- μ (mu) = mean
- σ² (sigma squared) = variance
- σ = standard deviation

**PDF**:
$$f(x) = \frac{1}{\sigma\sqrt{2\pi}} e^{-\frac{(x-\mu)^2}{2\sigma^2}}$$

### Why is it called "Normal"?

It appears so frequently in nature and measurement that it became the "norm"!

```python exec
id: 04-continuous-distributions-page-1-7
# Visualize the normal distribution
mu, sigma = 0, 1
x = np.linspace(-4, 4, 1000)
pdf = stats.norm.pdf(x, mu, sigma)

plt.figure(figsize=(10, 6))
plt.plot(x, pdf, 'b-', linewidth=2)
plt.fill_between(x, pdf, alpha=0.3)
plt.xlabel('Value', fontsize=12)
plt.ylabel('Density', fontsize=12)
plt.title('Standard Normal Distribution: N(0, 1)', fontsize=14, weight='bold')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

print("The bell curve: symmetric, centered at mean, most data within 3 standard deviations")
```

### Try this 3.1: Explore Parameters

Create a visualization showing how μ and σ affect the normal distribution.

1. Plot three normal distributions with μ = -2, 0, 2 and σ = 1 (same plot)
2. Plot three normal distributions with μ = 0 and σ = 0.5, 1, 2 (same plot)
3. What does μ control? What does σ control?

```python exec
id: 04-continuous-distributions-page-1-8
# YOUR CODE HERE
# Hint: Use a loop and different colors for each curve
```

### The 68-95-99.7 Rule (Empirical Rule)

For a normal distribution:
- 68% of data falls within 1 standard deviation of the mean
- 95% within 2 standard deviations
- 99.7% within 3 standard deviations

```python exec
id: 04-continuous-distributions-page-1-9
# Visualize the empirical rule
mu, sigma = 100, 15
x = np.linspace(mu - 4*sigma, mu + 4*sigma, 1000)
pdf = stats.norm.pdf(x, mu, sigma)

fig, ax = plt.subplots(figsize=(12, 7))
ax.plot(x, pdf, 'k-', linewidth=2)

# Shade regions
# 1 std dev (68%)
x1 = x[(x >= mu - sigma) & (x <= mu + sigma)]
y1 = stats.norm.pdf(x1, mu, sigma)
ax.fill_between(x1, y1, alpha=0.3, color='blue', label='68% (±1σ)')

# 2 std dev (95%)
x2 = x[(x >= mu - 2*sigma) & (x <= mu + 2*sigma) & ((x < mu - sigma) | (x > mu + sigma))]
y2 = stats.norm.pdf(x2, mu, sigma)
ax.fill_between(x2, y2, alpha=0.3, color='green', label='95% (±2σ)')

# 3 std dev (99.7%)
x3 = x[(x >= mu - 3*sigma) & (x <= mu + 3*sigma) & ((x < mu - 2*sigma) | (x > mu + 2*sigma))]
y3 = stats.norm.pdf(x3, mu, sigma)
ax.fill_between(x3, y3, alpha=0.3, color='red', label='99.7% (±3σ)')

ax.set_xlabel('Value', fontsize=12)
ax.set_ylabel('Density', fontsize=12)
ax.set_title(f'The 68-95-99.7 Rule: N({mu}, {sigma}²)', fontsize=14, weight='bold')
ax.legend(fontsize=11)
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
```

### Try this 3.2: Apply the Rule

IQ scores are normally distributed with mean 100 and standard deviation 15.

1. What percentage of people have IQ between 85 and 115?
2. What percentage have IQ above 130?
3. Use `stats.norm.cdf()` to verify your answers
4. Generate 10000 IQ samples and plot a histogram
5. Verify the 68-95-99.7 rule with your samples

```python exec
id: 04-continuous-distributions-page-1-10
# YOUR CODE HERE
# Hint: stats.norm.cdf(x, mu, sigma) gives P(X ≤ x)
```

### Example 3.1: Image Noise

Gaussian noise in images follows a normal distribution.

```python exec
id: 04-continuous-distributions-page-1-11
# Create a clean checkerboard image
def create_checkerboard(size=100, square_size=10):
    board = np.zeros((size, size))
    for i in range(0, size, square_size):
        for j in range(0, size, square_size):
            if (i // square_size + j // square_size) % 2 == 0:
                board[i:i+square_size, j:j+square_size] = 200
    return board

clean_image = create_checkerboard()

# Add Gaussian noise
noise_levels = [5, 15, 30]
fig, axes = plt.subplots(1, 4, figsize=(16, 4))

axes[0].imshow(clean_image, cmap='gray', vmin=0, vmax=255)
axes[0].set_title('Clean Image', fontsize=12, weight='bold')
axes[0].axis('off')

for i, sigma in enumerate(noise_levels):
    noise = np.random.normal(0, sigma, clean_image.shape)
    noisy_image = np.clip(clean_image + noise, 0, 255)
    
    axes[i+1].imshow(noisy_image, cmap='gray', vmin=0, vmax=255)
    axes[i+1].set_title(f'Gaussian Noise (σ={sigma})', fontsize=12, weight='bold')
    axes[i+1].axis('off')

plt.tight_layout()
plt.show()
```

### Try this 3.3: Analyze Noise

Using the noisy images above:

1. Extract the noise from one of the noisy images (subtract the clean image)
2. Plot a histogram of the noise values
3. Calculate the mean and standard deviation of the noise
4. Overlay a normal distribution with those parameters on your histogram
5. Does it match? Should it?

```python exec
id: 04-continuous-distributions-page-1-12
# YOUR CODE HERE
```

### Example 3.2: Word Embeddings

In NLP, word embeddings are often initialized with small random values from a normal distribution.

```python exec
id: 04-continuous-distributions-page-1-13
# Initialize embeddings for a small vocabulary
vocab_size = 1000
embedding_dim = 50

# Initialize with N(0, 0.01)
embeddings = np.random.normal(0, 0.01, size=(vocab_size, embedding_dim))

# Flatten to analyze distribution
all_values = embeddings.flatten()

# Plot
plt.figure(figsize=(10, 6))
plt.hist(all_values, bins=50, density=True, alpha=0.7, edgecolor='black')

# Overlay theoretical distribution
x = np.linspace(all_values.min(), all_values.max(), 1000)
pdf = stats.norm.pdf(x, 0, 0.01)
plt.plot(x, pdf, 'r-', linewidth=2, label='Theoretical N(0, 0.01)')

plt.xlabel('Embedding Value', fontsize=12)
plt.ylabel('Density', fontsize=12)
plt.title('Word Embedding Initialization Distribution', fontsize=14, weight='bold')
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

print(f"Total embedding parameters: {vocab_size * embedding_dim:,}")
print(f"Sample mean: {np.mean(all_values):.6f}")
print(f"Sample std: {np.std(all_values):.6f}")
```

### Try this 3.4: Embedding Statistics

1. Create embeddings with different initialization schemes:
   - N(0, 0.01)
   - N(0, 0.1)
   - Uniform(-0.1, 0.1)
2. For each, calculate the L2 norm (Euclidean length) of each word vector
3. Plot histograms of these norms
4. Which initialization leads to most similar-length vectors?
5. Why might this matter for training?

```python exec
id: 04-continuous-distributions-page-1-14
# YOUR CODE HERE
# Hint: np.linalg.norm(vector) calculates L2 norm
```

## Looking back

Before leaving this page, a sentence on each. What you write stays on this device.

```reflect
- Something you expected before running a cell that turned out differently
- The one idea from this page you could explain to someone else now
- Something you would change or try next, if there were time
- A question this page raised for you that it did not answer. Bring it to the next session; these questions are where the next session starts.
```
