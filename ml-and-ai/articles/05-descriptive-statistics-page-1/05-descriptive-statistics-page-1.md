---
title: "Notebook 5: Descriptive Statistics & Real Data Analysis (1 of 2)"
slug: 05-descriptive-statistics-page-1
course: ai-and-ml-foundations
course_title: "AI and ML Foundations"
series: 3-probability-and-statistics
series_title: "Probability and Statistics"
version: 2026.09.06.1
---

# Notebook 5: Descriptive Statistics & Real Data Analysis

## Part 0: From Theory to Practice

You've learned probability distributions and counting principles. Now we turn to real data - messy, incomplete, and full of patterns waiting to be discovered.

### Quick Check 0.1: What Can Numbers Tell Us?

You have test scores: 45, 50, 55, 55, 60, 65, 70, 75, 80, 95

Before calculating anything:
- What's a "typical" score?
- How spread out are the scores?
- Are there any outliers?
- If you had to summarize this class in one sentence, what would you say?

Write your thoughts:

```python exec
id: 05-descriptive-statistics-page-1-1
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
# Your observations:
```

### The Goal of Descriptive Statistics

**Descriptive statistics** summarize and describe data:
- **Center**: Where is the "middle"?
- **Spread**: How variable is the data?
- **Shape**: What does the distribution look like?
- **Relationships**: How do variables relate to each other?

### What You'll Learn

This notebook covers:
1. **Measures of center**: Mean, median, mode
2. **Measures of spread**: Range, variance, standard deviation, IQR
3. **Visualization**: Histograms, box plots, scatter plots
4. **Correlation**: Measuring relationships
5. **Real data**: Working with images, text, health data
6. **Introduction to regression**: Predicting relationships

---

## Part 1: Measures of Center

```python exec
id: 05-descriptive-statistics-page-1-2
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
from scipy import stats
import pandas as pd

np.random.seed(42)
```

### The Mean (Average)

$$\bar{x} = \frac{1}{n} \sum_{i=1}^{n} x_i$$

The mean is sensitive to outliers!

```python exec
id: 05-descriptive-statistics-page-1-3
scores = np.array([45, 50, 55, 55, 60, 65, 70, 75, 80, 95])

mean_score = np.mean(scores)
print(f"Scores: {scores}")
print(f"Mean: {mean_score:.1f}")
```

### The Median (Middle Value)

The median is the middle value when data is sorted.
- If n is odd: middle value
- If n is even: average of two middle values

The median is **robust to outliers**!

```python exec
id: 05-descriptive-statistics-page-1-4
median_score = np.median(scores)
print(f"Median: {median_score:.1f}")
```

### The Mode (Most Common)

The mode is the most frequently occurring value.

```python exec
id: 05-descriptive-statistics-page-1-5
mode_result = stats.mode(scores, keepdims=True)
mode_score = mode_result.mode[0]
print(f"Mode: {mode_score}")
```

### Try this 1.1: Impact of Outliers

Start with: [45, 50, 55, 55, 60, 65, 70, 75, 80, 95]

1. Calculate mean and median
2. Add an extreme outlier: 300
3. Recalculate mean and median
4. Which changed more?
5. Create a visualization showing both datasets
6. When should you use mean vs median?

```python exec
id: 05-descriptive-statistics-page-1-6
# YOUR CODE HERE
```

### Example 1.1: Image Pixel Intensities

```python exec
id: 05-descriptive-statistics-page-1-7
# Create a simple image
image = np.random.normal(128, 30, size=(100, 100))
image = np.clip(image, 0, 255)

# Add some bright outliers (stars, reflections)
num_outliers = 50
outlier_positions = np.random.choice(10000, num_outliers, replace=False)
flat_image = image.flatten()
flat_image[outlier_positions] = 255
image = flat_image.reshape(100, 100)

# Calculate statistics
mean_intensity = np.mean(image)
median_intensity = np.median(image)

# Visualize
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

ax1.imshow(image, cmap='gray', vmin=0, vmax=255)
ax1.set_title(f'Image with Outliers\nMean={mean_intensity:.1f}, Median={median_intensity:.1f}', 
              fontsize=12, weight='bold')
ax1.axis('off')

ax2.hist(image.flatten(), bins=50, edgecolor='black', alpha=0.7)
ax2.axvline(mean_intensity, color='red', linestyle='--', linewidth=2, label='Mean')
ax2.axvline(median_intensity, color='blue', linestyle='--', linewidth=2, label='Median')
ax2.set_xlabel('Pixel Intensity', fontsize=11)
ax2.set_ylabel('Frequency', fontsize=11)
ax2.set_title('Pixel Distribution', fontsize=12, weight='bold')
ax2.legend()
ax2.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

print(f"Mean pulled toward outliers: {mean_intensity:.1f}")
print(f"Median resistant to outliers: {median_intensity:.1f}")
```

### Try this 1.2: Image Statistics

Create three images:
1. Dark image: mean brightness 50
2. Medium image: mean brightness 128
3. Bright image: mean brightness 200

For each:
- Calculate mean, median, mode
- Add 5% salt-and-pepper noise (random black/white pixels)
- Recalculate statistics
- Which statistic changed most?
- Visualize all images and their histograms

```python exec
id: 05-descriptive-statistics-page-1-8
# YOUR CODE HERE
```

### Example 1.2: Word Lengths in Text

```python exec
id: 05-descriptive-statistics-page-1-9
text = """
The patient presented with acute respiratory distress. Initial assessment revealed elevated 
heart rate and decreased oxygen saturation. Immediate intervention was required. The medical 
team administered supplemental oxygen and initiated continuous monitoring protocols.
"""

words = text.split()
word_lengths = [len(word.strip('.,')) for word in words]

mean_length = np.mean(word_lengths)
median_length = np.median(word_lengths)
mode_result = stats.mode(word_lengths, keepdims=True)
mode_length = mode_result.mode[0]

print(f"Total words: {len(words)}")
print(f"Mean word length: {mean_length:.2f}")
print(f"Median word length: {median_length:.1f}")
print(f"Mode word length: {mode_length}")

# Visualize
plt.figure(figsize=(10, 6))
plt.hist(word_lengths, bins=range(1, max(word_lengths)+2), edgecolor='black', alpha=0.7)
plt.axvline(mean_length, color='red', linestyle='--', linewidth=2, label=f'Mean={mean_length:.2f}')
plt.axvline(median_length, color='blue', linestyle='--', linewidth=2, label=f'Median={median_length:.1f}')
plt.axvline(mode_length, color='green', linestyle='--', linewidth=2, label=f'Mode={mode_length}')
plt.xlabel('Word Length', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.title('Distribution of Word Lengths', fontsize=14, weight='bold')
plt.legend()
plt.grid(True, alpha=0.3, axis='y')
plt.show()
```

### Try this 1.3: Compare Text Styles

Analyze word lengths in three text types:
1. Medical text (technical, longer words)
2. News article (general audience)
3. Children's story (simple language)

For each:
- Calculate mean, median, mode word length
- Plot distribution
- Which has longest average words?
- Which has most variability?
- Create a comparison visualization
- What does this tell you about writing style?

```python exec
id: 05-descriptive-statistics-page-1-10
# YOUR CODE HERE
```

---

## Part 2: Measures of Spread

### Quick Check 2.1: Understanding Spread

Two classes both have mean score 70:
- Class A: [68, 69, 70, 71, 72]
- Class B: [40, 60, 70, 80, 100]

Which class is more consistent? How would you measure this?

```python exec
id: 05-descriptive-statistics-page-1-11
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
# Your reasoning:
```

### Range

$$\text{Range} = \max(x) - \min(x)$$

Simple but sensitive to outliers.

### Variance

Average squared deviation from the mean:

$$s^2 = \frac{1}{n-1} \sum_{i=1}^{n} (x_i - \bar{x})^2$$

Why (n-1)? Bessel's correction for sample variance.

### Standard Deviation

$$s = \sqrt{s^2}$$

In the same units as the data!

```python exec
id: 05-descriptive-statistics-page-1-12
class_a = np.array([68, 69, 70, 71, 72])
class_b = np.array([40, 60, 70, 80, 100])

print("Class A:")
print(f"  Mean: {np.mean(class_a):.1f}")
print(f"  Std Dev: {np.std(class_a, ddof=1):.2f}")
print(f"  Range: {np.ptp(class_a)}")

print("\nClass B:")
print(f"  Mean: {np.mean(class_b):.1f}")
print(f"  Std Dev: {np.std(class_b, ddof=1):.2f}")
print(f"  Range: {np.ptp(class_b)}")

print("\nClass B has same mean but much higher variability!")
```

### Try this 2.1: Visualize Spread

Create datasets with:
1. Same mean (100), low spread (std=5)
2. Same mean (100), medium spread (std=15)
3. Same mean (100), high spread (std=30)

For each:
- Generate 1000 samples
- Plot overlapping histograms
- Mark mean and ±1 std dev
- Calculate what % falls within 1 std dev
- Compare to theoretical 68%

```python exec
id: 05-descriptive-statistics-page-1-13
# YOUR CODE HERE
```

### Interquartile Range (IQR)

The middle 50% of the data:

$$\text{IQR} = Q_3 - Q_1$$

Where:
- Q1 (25th percentile): 25% of data below
- Q2 (50th percentile): Median
- Q3 (75th percentile): 75% of data below

IQR is robust to outliers!

```python exec
id: 05-descriptive-statistics-page-1-14
data = np.array([45, 50, 55, 55, 60, 65, 70, 75, 80, 95, 300])  # with outlier

q1 = np.percentile(data, 25)
q2 = np.percentile(data, 50)
q3 = np.percentile(data, 75)
iqr = q3 - q1

print(f"Q1 (25%): {q1}")
print(f"Q2 (50%, Median): {q2}")
print(f"Q3 (75%): {q3}")
print(f"IQR: {iqr}")
print(f"\nStd Dev: {np.std(data, ddof=1):.2f} (affected by outlier)")
print(f"IQR: {iqr} (not affected by outlier)")
```

### Try this 2.2: Outlier Detection

A common rule: outliers are values outside [Q1 - 1.5×IQR, Q3 + 1.5×IQR]

1. Generate 100 values from Normal(50, 10)
2. Add 5 outliers (values > 100)
3. Calculate IQR and outlier boundaries
4. Identify outliers using the rule
5. Visualize with box plot
6. Compare outlier detection using:
   - IQR method
   - 3 standard deviations method

```python exec
id: 05-descriptive-statistics-page-1-15
# YOUR CODE HERE
```

### Example 2.1: Image Noise Analysis

```python exec
id: 05-descriptive-statistics-page-1-16
# Create images with different noise levels
clean_image = np.ones((100, 100)) * 128

noise_levels = [5, 15, 30]
fig, axes = plt.subplots(1, 3, figsize=(15, 4))

for i, sigma in enumerate(noise_levels):
    noisy = clean_image + np.random.normal(0, sigma, clean_image.shape)
    noisy = np.clip(noisy, 0, 255)
    
    std_dev = np.std(noisy)
    
    axes[i].imshow(noisy, cmap='gray', vmin=0, vmax=255)
    axes[i].set_title(f'Noise σ={sigma}\nImage Std={std_dev:.1f}', fontsize=11, weight='bold')
    axes[i].axis('off')

plt.tight_layout()
plt.show()

print("Higher std dev = noisier image")
print("Std dev quantifies image quality!")
```

### Try this 2.3: Signal-to-Noise Ratio

Signal-to-Noise Ratio (SNR) = mean / std dev

1. Create a clean gradient image (0 to 255 smoothly)
2. Add Gaussian noise with σ = 10, 20, 30, 40, 50
3. Calculate SNR for each
4. Plot SNR vs noise level
5. At what noise level does SNR drop below 3?
6. Visualize all noisy images

```python exec
id: 05-descriptive-statistics-page-1-17
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
