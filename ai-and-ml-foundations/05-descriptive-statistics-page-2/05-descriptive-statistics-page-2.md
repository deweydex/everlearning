---
title: "05-descriptive-statistics-page-2 (2 of 2)"
slug: 05-descriptive-statistics-page-2
course: ai-and-ml-foundations
course_title: "AI and ML Foundations"
series: 3-probability-and-statistics
series_title: "Probability and Statistics"
version: 2026.09.06.1
---

Before starting this page, run the cell below. It repeats the imports and definitions from the earlier pages that this page uses.

```python exec
id: 05-descriptive-statistics-page-2-setup
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
from scipy import stats
import pandas as pd

import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
from scipy import stats
import pandas as pd

np.random.seed(42)

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

---

## Part 3: Visualization

### Box Plots (Box-and-Whisker)

Shows: Q1, Q2 (median), Q3, whiskers, outliers

```python exec
id: 05-descriptive-statistics-page-2-1
# Compare three groups
group_a = np.random.normal(70, 5, 100)
group_b = np.random.normal(75, 10, 100)
group_c = np.random.normal(65, 15, 100)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

# Box plot
ax1.boxplot([group_a, group_b, group_c], labels=['Group A', 'Group B', 'Group C'])
ax1.set_ylabel('Score', fontsize=12)
ax1.set_title('Box Plot Comparison', fontsize=14, weight='bold')
ax1.grid(True, alpha=0.3, axis='y')

# Histograms
ax2.hist(group_a, bins=20, alpha=0.5, label='Group A', edgecolor='black')
ax2.hist(group_b, bins=20, alpha=0.5, label='Group B', edgecolor='black')
ax2.hist(group_c, bins=20, alpha=0.5, label='Group C', edgecolor='black')
ax2.set_xlabel('Score', fontsize=12)
ax2.set_ylabel('Frequency', fontsize=12)
ax2.set_title('Histogram Comparison', fontsize=14, weight='bold')
ax2.legend()
ax2.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

print("Box plots show:")
print("- Center (median)")
print("- Spread (IQR)")
print("- Outliers")
print("- Shape (skewness)")
```

### Try this 3.1: Medical Data Visualization

Generate patient data for three conditions:
- Healthy: systolic BP ~ N(120, 10)
- Pre-hypertension: ~ N(135, 12)
- Hypertension: ~ N(155, 15)

Create:
1. Side-by-side box plots
2. Overlapping histograms
3. Violin plots (if familiar)
4. Summary statistics table
5. Identify overlap regions
6. Discuss: How distinct are the groups?

```python exec
id: 05-descriptive-statistics-page-2-2
# YOUR CODE HERE
```

### Try this 3.2: Image Region Statistics

Create a 200×200 image with four quadrants:
- Top-left: mean=50, std=10
- Top-right: mean=100, std=20
- Bottom-left: mean=150, std=15
- Bottom-right: mean=200, std=25

1. Visualize the full image
2. Create box plots comparing all quadrants
3. Calculate and display statistics for each
4. Which quadrant is most variable?
5. Add 50 random outlier pixels
6. How do box plots change?

```python exec
id: 05-descriptive-statistics-page-2-3
# YOUR CODE HERE
```

---

## Part 4: Relationships Between Variables

### Quick Check 4.1: Predicting Relationships

Which pairs would you expect to be related?
- Height and weight
- Study hours and exam score
- Age and reaction time
- Shoe size and IQ
- Temperature and ice cream sales

For each, predict: positive, negative, or no relationship?

```python exec
id: 05-descriptive-statistics-page-2-4
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
# Your predictions:
```

### Scatter Plots

Visualize relationships between two variables.

```python exec
id: 05-descriptive-statistics-page-2-5
# Generate related data
study_hours = np.random.uniform(0, 10, 100)
exam_scores = 50 + 4 * study_hours + np.random.normal(0, 5, 100)
exam_scores = np.clip(exam_scores, 0, 100)

plt.figure(figsize=(10, 6))
plt.scatter(study_hours, exam_scores, alpha=0.6, s=50)
plt.xlabel('Study Hours', fontsize=12)
plt.ylabel('Exam Score', fontsize=12)
plt.title('Study Hours vs Exam Score', fontsize=14, weight='bold')
plt.grid(True, alpha=0.3)
plt.show()

print("Positive relationship: more study → higher scores")
```

### Covariance

Measures how two variables vary together:

$$\text{cov}(X, Y) = \frac{1}{n-1} \sum_{i=1}^{n} (x_i - \bar{x})(y_i - \bar{y})$$

- Positive: variables increase together
- Negative: one increases, other decreases
- Zero: no linear relationship

```python exec
id: 05-descriptive-statistics-page-2-6
cov = np.cov(study_hours, exam_scores)[0, 1]
print(f"Covariance: {cov:.2f}")
print("\nProblem: Units depend on scale of variables!")
```

### Correlation (Pearson's r)

Standardized covariance:

$$r = \frac{\text{cov}(X,Y)}{s_X s_Y}$$

Range: -1 to +1
- r = +1: perfect positive linear relationship
- r = 0: no linear relationship
- r = -1: perfect negative linear relationship

```python exec
id: 05-descriptive-statistics-page-2-7
correlation = np.corrcoef(study_hours, exam_scores)[0, 1]
print(f"Correlation: {correlation:.3f}")
print(f"\nThis is a {'strong' if abs(correlation) > 0.7 else 'moderate' if abs(correlation) > 0.4 else 'weak'} positive relationship")
```

### Try this 4.1: Explore Correlation Patterns

Generate datasets with specific correlations:
1. r = 0.9 (strong positive)
2. r = 0.5 (moderate positive)
3. r = 0.0 (no relationship)
4. r = -0.5 (moderate negative)
5. r = -0.9 (strong negative)

For each:
- Create scatter plot
- Calculate actual correlation
- Add a best-fit line
- Create a grid of all 5 plots
- What visual patterns do you notice?

```python exec
id: 05-descriptive-statistics-page-2-8
# YOUR CODE HERE
# Hint: y = r*x + sqrt(1-r²)*noise generates correlation r
```

### Example 4.1: Image Patch Similarity

```python exec
id: 05-descriptive-statistics-page-2-9
# Create reference pattern
reference = np.random.rand(10, 10)

# Create similar patterns
noise_levels = [0.1, 0.5, 1.0]
fig, axes = plt.subplots(1, 4, figsize=(16, 4))

axes[0].imshow(reference, cmap='gray')
axes[0].set_title('Reference', fontsize=11, weight='bold')
axes[0].axis('off')

for i, noise_level in enumerate(noise_levels):
    noisy = reference + np.random.normal(0, noise_level, reference.shape)
    
    # Calculate correlation between flattened versions
    corr = np.corrcoef(reference.flatten(), noisy.flatten())[0, 1]
    
    axes[i+1].imshow(noisy, cmap='gray')
    axes[i+1].set_title(f'Noise={noise_level}\nCorr={corr:.3f}', fontsize=11, weight='bold')
    axes[i+1].axis('off')

plt.tight_layout()
plt.show()

print("Lower correlation = less similar patches")
print("Correlation measures image similarity!")
```

### Try this 4.2: Image Texture Analysis

Create three texture types:
1. Horizontal stripes
2. Vertical stripes
3. Checkerboard

For each pair:
- Calculate pixel-wise correlation
- Create a correlation matrix (3×3)
- Visualize as a heatmap
- Which textures are most different?
- Add Gaussian noise and recalculate
- How does noise affect texture correlation?

```python exec
id: 05-descriptive-statistics-page-2-10
# YOUR CODE HERE
```

### Try this 4.3: Word Frequency Correlation

Analyze two texts:
1. Count frequency of common words ("the", "and", "of", etc.) in each
2. Calculate correlation of word frequencies
3. Create scatter plot: frequency in text 1 vs text 2
4. Which words appear similarly frequent?
5. Which words differ most?
6. Compare correlations across different text types

```python exec
id: 05-descriptive-statistics-page-2-11
# YOUR CODE HERE
```

### Important: Correlation ≠ Causation!

Examples of spurious correlations:
- Ice cream sales and drowning deaths (both caused by warm weather)
- Number of firefighters and fire damage (both caused by fire size)
- Shoe size and reading ability in children (both caused by age)

Always ask: Is there a third variable causing both?

---

## Part 5: Introduction to Regression

### Linear Regression

Find the best-fit line: y = mx + b

Minimize squared errors (least squares)

```python exec
id: 05-descriptive-statistics-page-2-12
from scipy import stats as sp_stats

# Calculate regression line
slope, intercept, r_value, p_value, std_err = sp_stats.linregress(study_hours, exam_scores)

# Predictions
predicted_scores = slope * study_hours + intercept

# Visualize
plt.figure(figsize=(10, 6))
plt.scatter(study_hours, exam_scores, alpha=0.6, s=50, label='Actual')
plt.plot(study_hours, predicted_scores, 'r-', linewidth=2, label='Best Fit Line')
plt.xlabel('Study Hours', fontsize=12)
plt.ylabel('Exam Score', fontsize=12)
plt.title(f'Linear Regression: y = {slope:.2f}x + {intercept:.2f}\nR² = {r_value**2:.3f}', 
          fontsize=14, weight='bold')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()

print(f"Slope: {slope:.2f} (each hour → {slope:.2f} point increase)")
print(f"Intercept: {intercept:.2f} (expected score with 0 hours)")
print(f"R²: {r_value**2:.3f} ({r_value**2*100:.1f}% of variance explained)")
```

### Try this 5.1: Make Predictions

Using the regression model above:
1. Predict score for 5 hours of study
2. Predict score for 10 hours
3. Calculate residuals (actual - predicted) for all points
4. Plot residuals vs study hours
5. Are residuals randomly distributed?
6. What does the residual pattern tell you?

```python exec
id: 05-descriptive-statistics-page-2-13
# YOUR CODE HERE
```

### Try this 5.2: Image Compression via Regression

Use regression to compress an image:
1. Create a gradient image (smooth 0-255 transition)
2. For each row, fit a line to pixel values
3. Store only slope and intercept (2 numbers per row)
4. Reconstruct image from these parameters
5. Calculate compression ratio
6. Measure reconstruction error (MSE)
7. Compare to original image

```python exec
id: 05-descriptive-statistics-page-2-14
# YOUR CODE HERE
```

### Try this 5.3: Multiple Variable Regression

Predict exam score from multiple factors:
- Study hours (0-10)
- Sleep hours (4-10)
- Previous exam score (40-90)

1. Generate synthetic data with realistic relationships
2. Fit multiple regression model (use sklearn if available)
3. Determine which factor most important
4. Calculate prediction accuracy
5. Visualize predictions vs actual
6. Create partial dependence plots

```python exec
id: 05-descriptive-statistics-page-2-15
# YOUR CODE HERE
```

---

## Final Project: Comprehensive Data Analysis

### Project Description

Conduct a complete statistical analysis of multi-modal data.

### Dataset: Health Monitoring System

Generate synthetic data for 500 patients:
- Age (20-80)
- BMI (18-40)
- Systolic BP (100-180)
- Diastolic BP (60-110)
- Heart rate (50-100)
- Exercise hours/week (0-10)
- Medical image quality score (0-100)
- Risk score (0-100, derived from above)

### Requirements

**Part A: Descriptive Statistics**
1. Calculate mean, median, std dev for each variable
2. Identify outliers using multiple methods
3. Create distribution visualizations
4. Generate summary statistics table

**Part B: Univariate Analysis**
1. Plot histograms for all variables
2. Create box plots comparing age groups
3. Identify skewness in distributions
4. Test normality assumptions

**Part C: Bivariate Analysis**
1. Calculate correlation matrix
2. Create correlation heatmap
3. Generate scatter plots for key pairs
4. Identify strongest relationships

**Part D: Regression Analysis**
1. Predict risk score from other variables
2. Build multiple regression model
3. Evaluate model performance (R²)
4. Identify most important predictors

**Part E: Image Analysis**
1. Generate 500 medical scan images (varying quality)
2. Extract image statistics (mean, std, SNR)
3. Correlate image quality with health metrics
4. Classify images as good/poor quality

**Part F: Visualization Dashboard**
1. Create comprehensive 4×3 subplot grid
2. Show key relationships and distributions
3. Highlight important findings
4. Use consistent color scheme

**Part G: Report**
Write a summary addressing:
1. Key findings from descriptive statistics
2. Which variables most strongly predict risk?
3. Are there distinct patient groups?
4. Recommendations for health monitoring
5. Limitations of the analysis

### Bonus Challenges
- Implement PCA for dimensionality reduction
- Cluster patients into risk groups
- Build a simple classification model
- Create interactive visualizations
- Compare different regression techniques

```python exec
id: 05-descriptive-statistics-page-2-16
# YOUR PROJECT CODE HERE
```

---

## Summary and Reflection

### Key Concepts

**Measures of Center:**
- Mean: Average, sensitive to outliers
- Median: Middle value, robust to outliers
- Mode: Most common value

**Measures of Spread:**
- Range: Max - Min
- Variance: Average squared deviation
- Standard deviation: Square root of variance
- IQR: Q3 - Q1, robust measure

**Relationships:**
- Correlation: Measures linear association (-1 to +1)
- Regression: Predicts one variable from another
- R²: Proportion of variance explained

### Reflection Questions

**Conceptual:**
1. When should you use mean vs median?
2. Why is standard deviation more useful than variance?
3. How do outliers affect different statistics?

**Practical:**
1. How do you choose appropriate visualizations?
2. What makes a correlation "strong" vs "weak"?
3. When is correlation misleading?

**Critical Thinking:**
1. Can statistics lie? How?
2. What's lost when summarizing data?
3. How do you balance simplicity and completeness?

### Looking Ahead

In Notebook 6:
- Bayesian methods and updating beliefs
- Prior, likelihood, posterior
- Real-world applications
- Decision making under uncertainty

### Final Thought

Descriptive statistics transform data into understanding. Every mean tells a story of center, every standard deviation speaks of variability, every correlation hints at relationships. But remember: statistics describe, they don't explain. Behind every number is a question: Why?

The best data analysts don't just calculate - they explore, visualize, question, and communicate. They know when means mislead, when correlations confuse, and when visualizations reveal truths that numbers hide.

You now have the tools. Use them wisely, skeptically, and creatively.

## Looking back

Before leaving this page, a sentence on each. What you write stays on this device.

```reflect
- Something you expected before running a cell that turned out differently
- The one idea from this page you could explain to someone else now
- Something you would change or try next, if there were time
- A question this page raised for you that it did not answer. Bring it to the next session; these questions are where the next session starts.
```
