---
title: "04-continuous-distributions-page-2 (2 of 2)"
slug: 04-continuous-distributions-page-2
course: ai-and-ml-foundations
course_title: "AI and ML Foundations"
series: 3-probability-and-statistics
series_title: "Probability and Statistics"
version: 2026.09.06.1
---

Before starting this page, run the cell below. It repeats the imports and definitions from the earlier pages that this page uses.

```python exec
id: 04-continuous-distributions-page-2-setup
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import warnings

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import warnings
warnings.filterwarnings('ignore')

np.random.seed(42)

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

---

## Part 4: Z-Scores and Standardization

The **z-score** tells you how many standard deviations a value is from the mean.

$$z = \frac{x - \mu}{\sigma}$$

**Standard Normal Distribution**: N(0, 1)
- Mean = 0
- Standard deviation = 1

Any normal distribution can be converted to standard normal using z-scores.

```python exec
id: 04-continuous-distributions-page-2-1
# Example: Convert heights to z-scores
heights = np.random.normal(170, 10, size=1000)

# Calculate z-scores
mu = np.mean(heights)
sigma = np.std(heights)
z_scores = (heights - mu) / sigma

# Plot both distributions
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

# Original distribution
ax1.hist(heights, bins=30, density=True, alpha=0.7, edgecolor='black')
x = np.linspace(heights.min(), heights.max(), 1000)
ax1.plot(x, stats.norm.pdf(x, mu, sigma), 'r-', linewidth=2)
ax1.set_xlabel('Height (cm)', fontsize=12)
ax1.set_ylabel('Density', fontsize=12)
ax1.set_title(f'Original: N({mu:.1f}, {sigma:.1f}²)', fontsize=12, weight='bold')
ax1.grid(True, alpha=0.3)

# Standardized distribution
ax2.hist(z_scores, bins=30, density=True, alpha=0.7, edgecolor='black')
z = np.linspace(z_scores.min(), z_scores.max(), 1000)
ax2.plot(z, stats.norm.pdf(z, 0, 1), 'r-', linewidth=2)
ax2.set_xlabel('Z-score', fontsize=12)
ax2.set_ylabel('Density', fontsize=12)
ax2.set_title('Standardized: N(0, 1)', fontsize=12, weight='bold')
ax2.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

print(f"Original: mean={mu:.2f}, std={sigma:.2f}")
print(f"Z-scores: mean={np.mean(z_scores):.6f}, std={np.std(z_scores):.6f}")
```

### Try this 4.1: Interpret Z-Scores

A person's height is 185 cm. The population mean is 170 cm with standard deviation 10 cm.

1. Calculate their z-score
2. What percentile are they in? (Use `stats.norm.cdf`)
3. What percentage of people are taller?
4. If someone has z-score of -1.5, what is their height?
5. Verify your calculations with code

```python exec
id: 04-continuous-distributions-page-2-2
# YOUR CODE HERE
```

### Example 4.1: Normalizing Image Data

In deep learning, we often normalize images before training.

```python exec
id: 04-continuous-distributions-page-2-3
# Create a sample image
image = np.random.normal(128, 30, size=(100, 100))
image = np.clip(image, 0, 255)

# Normalize
mean_pixel = np.mean(image)
std_pixel = np.std(image)
normalized_image = (image - mean_pixel) / std_pixel

# Plot
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

im1 = ax1.imshow(image, cmap='gray')
ax1.set_title(f'Original\nmean={mean_pixel:.1f}, std={std_pixel:.1f}', fontsize=12, weight='bold')
ax1.axis('off')
plt.colorbar(im1, ax=ax1)

im2 = ax2.imshow(normalized_image, cmap='gray')
ax2.set_title(f'Normalized\nmean={np.mean(normalized_image):.2f}, std={np.std(normalized_image):.2f}', 
              fontsize=12, weight='bold')
ax2.axis('off')
plt.colorbar(im2, ax=ax2)

plt.tight_layout()
plt.show()

print("Normalization makes pixel values have mean 0 and std 1")
print("This helps neural networks train more stably")
```

### Try this 4.2: Batch Normalization

You have 10 images with different brightness levels.

1. Create 10 random 50×50 images with different means (e.g., 50, 80, 110, ...)
2. Normalize each image individually
3. Display all 10 original and normalized images in a grid
4. Calculate statistics for each normalized image
5. Why does each normalized image have mean≈0 and std≈1?

```python exec
id: 04-continuous-distributions-page-2-4
# YOUR CODE HERE
```

---

## Part 5: The Central Limit Theorem

**The Central Limit Theorem (CLT)** is one of the most important results in statistics:

> If you take the **mean** of many random samples from ANY distribution, those means will be approximately normally distributed.

This explains why normal distributions appear everywhere!

### Demonstration: Uniform to Normal

```python exec
id: 04-continuous-distributions-page-2-5
# Start with uniform distribution
def demonstrate_clt(sample_sizes=[1, 5, 10, 30]):
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    axes = axes.flatten()
    
    num_experiments = 10000
    
    for i, n in enumerate(sample_sizes):
        # For each experiment, take n samples and compute their mean
        means = []
        for _ in range(num_experiments):
            samples = np.random.uniform(0, 1, size=n)
            means.append(np.mean(samples))
        
        # Plot histogram
        axes[i].hist(means, bins=50, density=True, alpha=0.7, edgecolor='black')
        
        # Overlay normal distribution
        mu_theoretical = 0.5  # mean of uniform(0,1)
        sigma_theoretical = np.sqrt(1/12) / np.sqrt(n)  # std of sample mean
        x = np.linspace(0, 1, 1000)
        pdf = stats.norm.pdf(x, mu_theoretical, sigma_theoretical)
        axes[i].plot(x, pdf, 'r-', linewidth=2, label='Normal approximation')
        
        axes[i].set_xlabel('Sample Mean', fontsize=11)
        axes[i].set_ylabel('Density', fontsize=11)
        axes[i].set_title(f'Sample size n={n}', fontsize=12, weight='bold')
        axes[i].legend()
        axes[i].grid(True, alpha=0.3)
    
    plt.suptitle('Central Limit Theorem: Distribution of Sample Means', 
                 fontsize=14, weight='bold', y=1.00)
    plt.tight_layout()
    plt.show()

demonstrate_clt()

print("Notice: As sample size increases, the distribution becomes more normal!")
```

### Try this 5.1: CLT with Different Distributions

Test the CLT with a heavily skewed distribution (exponential).

1. Generate samples from exponential distribution (use `np.random.exponential`)
2. For sample sizes n = 1, 5, 20, 50:
   - Take 10000 samples of size n
   - Calculate the mean of each sample
   - Plot histogram of these means
3. Observe how quickly it becomes normal
4. Does CLT work even for non-symmetric distributions?

```python exec
id: 04-continuous-distributions-page-2-6
# YOUR CODE HERE
```

### Example 5.1: Average Pixel Brightness

Even if individual pixels aren't normally distributed, the average brightness of a region tends to be normal!

```python exec
id: 04-continuous-distributions-page-2-7
# Create images with bimodal pixel distribution (dark and bright, nothing in between)
def create_bimodal_image():
    image = np.random.choice([50, 200], size=(100, 100))
    return image

# Sample one image
sample_image = create_bimodal_image()

# Calculate mean brightness for 10000 images
mean_brightnesses = []
for _ in range(10000):
    img = create_bimodal_image()
    mean_brightnesses.append(np.mean(img))

# Plot
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

# Individual pixel distribution
ax1.hist(sample_image.flatten(), bins=50, edgecolor='black', alpha=0.7)
ax1.set_xlabel('Pixel Value', fontsize=12)
ax1.set_ylabel('Frequency', fontsize=12)
ax1.set_title('Individual Pixel Distribution (Bimodal)', fontsize=12, weight='bold')
ax1.grid(True, alpha=0.3)

# Distribution of means
ax2.hist(mean_brightnesses, bins=50, density=True, edgecolor='black', alpha=0.7)
x = np.linspace(min(mean_brightnesses), max(mean_brightnesses), 1000)
mu_empirical = np.mean(mean_brightnesses)
sigma_empirical = np.std(mean_brightnesses)
ax2.plot(x, stats.norm.pdf(x, mu_empirical, sigma_empirical), 'r-', linewidth=2)
ax2.set_xlabel('Mean Brightness', fontsize=12)
ax2.set_ylabel('Density', fontsize=12)
ax2.set_title('Distribution of Mean Brightness (Normal!)', fontsize=12, weight='bold')
ax2.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

print("CLT in action: Non-normal pixels → Normal means!")
```

### Try this 5.2: Word Frequency Averaging

Word frequencies in individual documents aren't normal, but average frequencies across many documents might be.

1. Simulate 1000 documents where the word "health" appears following a Poisson(3) distribution
2. For batch sizes of 1, 5, 10, 30 documents:
   - Calculate the mean frequency across batches
   - Plot histogram of these means
3. Does CLT apply to count data?

```python exec
id: 04-continuous-distributions-page-2-8
# YOUR CODE HERE
```

---

## Part 6: Exponential Distribution

The **exponential distribution** models the time between events in a Poisson process.

**Notation**: X ~ Exponential(λ)
- λ (lambda) = rate parameter

**PDF**:
$$f(x) = \lambda e^{-\lambda x} \text{ for } x \geq 0$$

**Mean**: 1/λ

**Variance**: 1/λ²

### Example 6.1: Time Between Patient Arrivals

```python exec
id: 04-continuous-distributions-page-2-9
# Patients arrive at rate λ = 2 per hour (mean time = 0.5 hours = 30 min)
lambda_rate = 2.0

# Generate wait times
wait_times = np.random.exponential(1/lambda_rate, size=1000)

# Plot
plt.figure(figsize=(10, 6))
plt.hist(wait_times, bins=50, density=True, alpha=0.7, edgecolor='black')

# Overlay theoretical PDF
x = np.linspace(0, wait_times.max(), 1000)
pdf = lambda_rate * np.exp(-lambda_rate * x)
plt.plot(x, pdf, 'r-', linewidth=2, label=f'Exponential(λ={lambda_rate})')

plt.xlabel('Time Between Arrivals (hours)', fontsize=12)
plt.ylabel('Density', fontsize=12)
plt.title('Patient Arrival Times', fontsize=14, weight='bold')
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

print(f"Mean wait time: {1/lambda_rate:.2f} hours")
print(f"Sample mean: {np.mean(wait_times):.2f} hours")
```

### Try this 6.1: Email Arrival Times

You receive emails at an average rate of 5 per hour.

1. Model the time between emails using exponential distribution
2. Simulate 1000 inter-arrival times
3. What's the probability the next email arrives within 10 minutes? (Use `stats.expon.cdf`)
4. What's the probability you wait more than 30 minutes?
5. Verify with simulation

```python exec
id: 04-continuous-distributions-page-2-10
# YOUR CODE HERE
```

### Example 6.2: Image Processing Task Duration

Processing time for images often follows exponential distribution.

```python exec
id: 04-continuous-distributions-page-2-11
# Average processing time: 2 seconds
mean_time = 2.0
lambda_rate = 1 / mean_time

# Simulate processing 1000 images
processing_times = np.random.exponential(mean_time, size=1000)

# Statistics
print(f"Mean processing time: {np.mean(processing_times):.2f} seconds")
print(f"Median processing time: {np.median(processing_times):.2f} seconds")
print(f"Max processing time: {np.max(processing_times):.2f} seconds")
print(f"\nPercentage completed within 1 second: {np.mean(processing_times < 1)*100:.1f}%")
print(f"Percentage taking more than 5 seconds: {np.mean(processing_times > 5)*100:.1f}%")

# Plot
plt.figure(figsize=(10, 6))
plt.hist(processing_times, bins=50, density=True, alpha=0.7, edgecolor='black')
x = np.linspace(0, processing_times.max(), 1000)
pdf = lambda_rate * np.exp(-lambda_rate * x)
plt.plot(x, pdf, 'r-', linewidth=2)
plt.xlabel('Processing Time (seconds)', fontsize=12)
plt.ylabel('Density', fontsize=12)
plt.title('Image Processing Time Distribution', fontsize=14, weight='bold')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
```

### Try this 6.2: Memoryless Property

The exponential distribution is memoryless: P(X > s + t | X > s) = P(X > t)

Translation: If you've already waited 10 minutes, the probability of waiting 5 more minutes is the same as the original probability of waiting 5 minutes.

1. Verify this property with simulation
2. Generate 10000 wait times from Exponential(1)
3. Filter for times > 2 (already waited 2 units)
4. Among those, calculate P(wait > 3) = P(total wait > 5 | already waited 2)
5. Compare to P(wait > 1) from the original distribution
6. Are they equal?

```python exec
id: 04-continuous-distributions-page-2-12
# YOUR CODE HERE
```

---

## Part 7: Applications to Real Data

### Example 7.1: Analyzing Medical Measurements

```python exec
id: 04-continuous-distributions-page-2-13
# Simulate patient data
np.random.seed(42)
n_patients = 500

# Generate realistic medical data
systolic_bp = np.random.normal(120, 15, n_patients)  # mmHg
diastolic_bp = np.random.normal(80, 10, n_patients)  # mmHg
heart_rate = np.random.normal(72, 12, n_patients)  # bpm
temperature = np.random.normal(37.0, 0.5, n_patients)  # Celsius

# Plot distributions
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
measurements = [
    (systolic_bp, 'Systolic Blood Pressure (mmHg)', axes[0, 0]),
    (diastolic_bp, 'Diastolic Blood Pressure (mmHg)', axes[0, 1]),
    (heart_rate, 'Heart Rate (bpm)', axes[1, 0]),
    (temperature, 'Body Temperature (°C)', axes[1, 1])
]

for data, label, ax in measurements:
    ax.hist(data, bins=30, density=True, alpha=0.7, edgecolor='black')
    
    # Overlay normal distribution
    mu, sigma = np.mean(data), np.std(data)
    x = np.linspace(data.min(), data.max(), 1000)
    ax.plot(x, stats.norm.pdf(x, mu, sigma), 'r-', linewidth=2)
    
    ax.set_xlabel(label, fontsize=11)
    ax.set_ylabel('Density', fontsize=11)
    ax.set_title(f'μ={mu:.1f}, σ={sigma:.1f}', fontsize=11, weight='bold')
    ax.grid(True, alpha=0.3)

plt.suptitle('Distribution of Medical Measurements', fontsize=14, weight='bold')
plt.tight_layout()
plt.show()
```

### Try this 7.1: Identify Outliers

Using the medical data above:

1. For each measurement, calculate z-scores for all patients
2. Identify patients with |z| > 3 (extreme values)
3. Count how many "outliers" there are in each measurement
4. Is this consistent with the 99.7% rule?
5. Visualize outliers on the histograms (mark them in red)

```python exec
id: 04-continuous-distributions-page-2-14
# YOUR CODE HERE
```

### Example 7.2: Sentiment Score Distribution

Sentiment analysis outputs often follow normal distribution.

```python exec
id: 04-continuous-distributions-page-2-15
# Simulate sentiment scores for product reviews
# Positive product: mean=0.3, std=0.4
positive_product = np.random.normal(0.3, 0.4, 1000)
positive_product = np.clip(positive_product, -1, 1)  # Sentiment scores in [-1, 1]

# Negative product: mean=-0.2, std=0.3  
negative_product = np.random.normal(-0.2, 0.3, 1000)
negative_product = np.clip(negative_product, -1, 1)

# Plot
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

# Positive product
ax1.hist(positive_product, bins=40, density=True, alpha=0.7, edgecolor='black', color='green')
x = np.linspace(-1, 1, 1000)
ax1.plot(x, stats.norm.pdf(x, np.mean(positive_product), np.std(positive_product)), 
         'r-', linewidth=2)
ax1.set_xlabel('Sentiment Score', fontsize=12)
ax1.set_ylabel('Density', fontsize=12)
ax1.set_title('Positive Product Reviews', fontsize=12, weight='bold')
ax1.axvline(x=0, color='black', linestyle='--', alpha=0.5)
ax1.grid(True, alpha=0.3)

# Negative product
ax2.hist(negative_product, bins=40, density=True, alpha=0.7, edgecolor='black', color='red')
ax2.plot(x, stats.norm.pdf(x, np.mean(negative_product), np.std(negative_product)), 
         'b-', linewidth=2)
ax2.set_xlabel('Sentiment Score', fontsize=12)
ax2.set_ylabel('Density', fontsize=12)
ax2.set_title('Negative Product Reviews', fontsize=12, weight='bold')
ax2.axvline(x=0, color='black', linestyle='--', alpha=0.5)
ax2.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

print(f"Positive product: {np.mean(positive_product > 0)*100:.1f}% positive reviews")
print(f"Negative product: {np.mean(negative_product > 0)*100:.1f}% positive reviews")
```

### Try this 7.2: Detect Sentiment Shift

A company releases a product update. You have sentiment scores before and after.

1. Generate 500 "before" scores: N(0.1, 0.3)
2. Generate 500 "after" scores: N(0.4, 0.3)
3. Plot both distributions overlaid
4. Calculate the percentage of reviews that improved (after > before)
5. Use z-scores to determine if the change is statistically significant
6. Visualize the overlap between distributions

```python exec
id: 04-continuous-distributions-page-2-16
# YOUR CODE HERE
```

---

## Part 8: Advanced Application - Image Quality Metrics

### Example 8.1: Structural Similarity Index (SSIM)

```python exec
id: 04-continuous-distributions-page-2-17
def simple_ssim(img1, img2):
    """Simplified SSIM calculation."""
    mu1, mu2 = np.mean(img1), np.mean(img2)
    sigma1, sigma2 = np.std(img1), np.std(img2)
    sigma12 = np.mean((img1 - mu1) * (img2 - mu2))
    
    c1, c2 = 0.01**2, 0.03**2
    ssim = ((2*mu1*mu2 + c1) * (2*sigma12 + c2)) / \
           ((mu1**2 + mu2**2 + c1) * (sigma1**2 + sigma2**2 + c2))
    return ssim

# Create reference image
reference = create_checkerboard(100, 10)

# Create degraded versions
gaussian_noise = reference + np.random.normal(0, 20, reference.shape)
blurred = np.copy(reference)
for i in range(1, 99):
    for j in range(1, 99):
        blurred[i, j] = np.mean(reference[i-1:i+2, j-1:j+2])

# Calculate SSIM
ssim_noisy = simple_ssim(reference, gaussian_noise)
ssim_blurred = simple_ssim(reference, blurred)

# Visualize
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

axes[0].imshow(reference, cmap='gray', vmin=0, vmax=255)
axes[0].set_title('Reference Image', fontsize=12, weight='bold')
axes[0].axis('off')

axes[1].imshow(gaussian_noise, cmap='gray', vmin=0, vmax=255)
axes[1].set_title(f'Noisy (SSIM={ssim_noisy:.3f})', fontsize=12, weight='bold')
axes[1].axis('off')

axes[2].imshow(blurred, cmap='gray', vmin=0, vmax=255)
axes[2].set_title(f'Blurred (SSIM={ssim_blurred:.3f})', fontsize=12, weight='bold')
axes[2].axis('off')

plt.tight_layout()
plt.show()

print("SSIM ranges from -1 to 1, where 1 = identical images")
print("Gaussian statistics are central to image quality metrics")
```

### Try this 8.1: Comprehensive Image Analysis

Create a complete image quality analysis pipeline:

1. Start with a clean image (create or load)
2. Add three types of degradation:
   - Gaussian noise (σ = 10, 20, 30)
   - Uniform noise  
   - Salt-and-pepper noise
3. For each degraded image:
   - Calculate mean squared error (MSE)
   - Calculate peak signal-to-noise ratio (PSNR)
   - Analyze pixel value distribution
4. Create a comprehensive visualization grid
5. Discuss: Which noise type is most problematic?

```python exec
id: 04-continuous-distributions-page-2-18
# YOUR CODE HERE
# Hint: MSE = mean((img1 - img2)**2)
# Hint: PSNR = 10 * log10(MAX_PIXEL²/MSE)
```

---

## Final Project: Multi-Modal Analysis

### Project Description

Combine everything you've learned to analyze a multi-modal dataset that includes:
- Text sentiment scores
- Image quality metrics
- Medical measurements

### Your Task

1. **Data Generation**:
   - Generate 1000 samples with:
     - Sentiment score: Normal(-0.5 to 0.5)
     - Image quality: Uniform(0 to 1)
     - Health metric: Normal with realistic parameters

2. **Exploratory Analysis**:
   - Plot distribution of each variable
   - Fit appropriate probability distributions
   - Calculate summary statistics
   - Identify outliers using z-scores

3. **Normalization**:
   - Standardize all variables to z-scores
   - Verify mean≈0, std≈1 for each

4. **Hypothesis Testing**:
   - Divide samples into two groups (above/below median sentiment)
   - Compare health metrics between groups
   - Use CLT to analyze sample means

5. **Visualization**:
   - Create a comprehensive dashboard
   - Include all distributions, correlations, outliers
   - Annotate key findings

6. **Interpretation**:
   - Write a paragraph summarizing findings
   - Discuss which distributions fit the data
   - Explain any anomalies or patterns

### Bonus Challenges

- Implement a simple anomaly detection system using z-scores
- Simulate the effect of sample size on conclusion certainty
- Create an interactive visualization (if you know plotting libraries)
- Apply CLT to demonstrate normality of aggregated metrics

```python exec
id: 04-continuous-distributions-page-2-19
# YOUR PROJECT CODE HERE
```

---

## Summary and Reflection

### Key Concepts Mastered

**Continuous Distributions:**
- Uniform: Equal probability across an interval
- Normal/Gaussian: The bell curve, most important in statistics
- Exponential: Time between rare events

**Critical Ideas:**
- PDF vs. PMF: Density vs. Mass
- Z-scores: Standardizing measurements
- Central Limit Theorem: Why everything becomes normal
- The 68-95-99.7 rule

**Applications:**
- Image processing: Noise models, quality metrics, normalization
- NLP: Word embeddings, sentiment analysis, attention weights
- Health: Physiological measurements, risk assessment

### Distribution Comparison Table

| Distribution | Parameters | Mean | Variance | Use Case |
|--------------|------------|------|----------|----------|
| Uniform(a,b) | a, b | (a+b)/2 | (b-a)²/12 | Random initialization |
| Normal(μ,σ²) | μ, σ² | μ | σ² | Measurement error, averages |
| Exponential(λ) | λ | 1/λ | 1/λ² | Wait times, event intervals |

### Reflection Questions

1. **Why is the normal distribution so ubiquitous in nature and machine learning?**
   - Think about the Central Limit Theorem
   - Consider measurement error
   - Reflect on biological variation

2. **How do standardization and normalization improve machine learning?**
   - Why do neural networks train better with normalized inputs?
   - What does it mean for different features to have similar scales?

3. **When would you choose uniform vs. normal initialization?**
   - Consider the properties of each
   - Think about gradient flow
   - Reflect on symmetry

4. **How does the CLT change your understanding of averaging?**
   - Why can we average "weird" distributions?
   - What does this mean for batch processing?
   - How does sample size affect reliability?

5. **What role do probability distributions play in uncertainty quantification?**
   - How do confidence intervals work?
   - Why do we report means with error bars?
   - What does it mean to be "95% confident"?

### Looking Forward

You now have the probability foundations needed for:
- **Machine Learning**: Understanding loss functions, gradient descent, initialization
- **Statistics**: Hypothesis testing, confidence intervals, regression
- **Deep Learning**: Batch normalization, dropout, weight initialization
- **Data Science**: Exploratory analysis, outlier detection, feature engineering

### Next Steps

In the remaining notebooks, we'll explore:
- **Notebook 5**: Descriptive statistics and real data analysis
- **Notebook 6**: Bayesian methods and applications
- **Final Project**: Bringing it all together with real-world datasets

### Final Thought

Probability is not just about calculating numbers. It's a framework for thinking about uncertainty, making predictions, and quantifying our confidence. These distributions aren't mathematical abstractions—they're patterns that describe real phenomena in images, language, and health data. As you continue, keep asking: "What distribution might describe this?" and "How certain am I?"

## Looking back

Before leaving this page, a sentence on each. What you write stays on this device.

```reflect
- Something you expected before running a cell that turned out differently
- The one idea from this page you could explain to someone else now
- Something you would change or try next, if there were time
- A question this page raised for you that it did not answer. Bring it to the next session; these questions are where the next session starts.
```
