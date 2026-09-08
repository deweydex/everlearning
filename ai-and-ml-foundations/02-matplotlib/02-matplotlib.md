---
title: "Data Visualization with Matplotlib"
slug: 02-matplotlib
course: ai-and-ml-foundations
course_title: "AI and ML Foundations"
series: 0-python-and-numpy-refresher
series_title: "Python and NumPy Refresher"
version: 2026.09.06.1
---

# Data Visualization with Matplotlib

## References and Resources

**Primary References:**
- Hunter, J. D. (2007). Matplotlib: A 2D graphics environment. *Computing in Science & Engineering*, 9(3), 90-95. https://doi.org/10.1109/MCSE.2007.55
- Matplotlib Development Team. (2024). *Matplotlib Documentation*. https://matplotlib.org/stable/
- VanderPlas, J. (2016). *Python Data Science Handbook*. O'Reilly Media. (Free: https://jakevdp.github.io/PythonDataScienceHandbook/)

**Further Resources:**
- Wilke, C. O. (2019). *Fundamentals of Data Visualization*. O'Reilly Media. (Free: https://clauswilke.com/dataviz/)
- Matplotlib Gallery: https://matplotlib.org/stable/gallery/index.html
- Tufte, E. R. (2001). *The Visual Display of Quantitative Information* (2nd ed.). Graphics Press.

---

---

## Introduction to Scientific Visualization

Visualization is not merely about making plots—it's about understanding data, discovering patterns, and communicating insights effectively. In machine learning and statistics, visualization serves multiple crucial purposes:

- **Exploratory analysis**: Understanding data distributions and relationships
- **Model diagnostics**: Identifying problems with model assumptions
- **Result communication**: Presenting findings to stakeholders
- **Theory validation**: Checking mathematical derivations visually

Matplotlib provides the foundation for scientific visualization in Python. Let's begin:

```python exec
id: 02-matplotlib-1
import numpy as np
import matplotlib.pyplot as plt
from typing import Tuple, List

# Set style for better-looking plots
plt.style.use('seaborn-v0_8-darkgrid')

print(f"Matplotlib version: {plt.matplotlib.__version__}")
print(f"NumPy version: {np.__version__}")
```

## Basic Plotting Techniques

### Line Plots for Continuous Data

Line plots effectively show how variables change over continuous domains. Let's visualize how different activation functions behave:

```python exec
id: 02-matplotlib-2
def relu_activation(input_values: np.ndarray) -> np.ndarray:
    """
    Rectified Linear Unit (ReLU) activation function.
    
    Args:
        input_values: Input array
    
    Returns:
        max(0, x) for each element
    """
    return np.maximum(0, input_values)


def sigmoid_activation(input_values: np.ndarray) -> np.ndarray:
    """
    Sigmoid activation function.
    
    Args:
        input_values: Input array
    
    Returns:
        1 / (1 + e^(-x)) for each element
    """
    return 1 / (1 + np.exp(-input_values))


def tanh_activation(input_values: np.ndarray) -> np.ndarray:
    """
    Hyperbolic tangent activation function.
    
    Args:
        input_values: Input array
    
    Returns:
        tanh(x) for each element
    """
    return np.tanh(input_values)


# Generate input range
x_values = np.linspace(-5, 5, 200)

# Calculate activation outputs
relu_output = relu_activation(x_values)
sigmoid_output = sigmoid_activation(x_values)
tanh_output = tanh_activation(x_values)

# Create figure
plt.figure(figsize=(12, 6))

# Plot each activation function
plt.plot(x_values, relu_output, label='ReLU', linewidth=2)
plt.plot(x_values, sigmoid_output, label='Sigmoid', linewidth=2)
plt.plot(x_values, tanh_output, label='Tanh', linewidth=2)

# Add reference lines
plt.axhline(y=0, color='k', linestyle='--', alpha=0.3, linewidth=1)
plt.axvline(x=0, color='k', linestyle='--', alpha=0.3, linewidth=1)

# Customize plot
plt.xlabel('Input Value', fontsize=12)
plt.ylabel('Output Value', fontsize=12)
plt.title('Comparison of Activation Functions in Neural Networks', fontsize=14, fontweight='bold')
plt.legend(fontsize=11, loc='best')
plt.grid(True, alpha=0.3)

# Add annotation
plt.text(2.5, 0.85, 'Sigmoid saturates\nat extremes', 
         bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

plt.tight_layout()
plt.show()

print("Observations:")
print("- ReLU: Simple, non-saturating for positive values")
print("- Sigmoid: Smooth, bounded (0,1), saturates at extremes")
print("- Tanh: Smooth, bounded (-1,1), zero-centered")
```

### Scatter Plots for Relationships

Scatter plots reveal relationships between variables. Let's explore correlation patterns:

```python exec
id: 02-matplotlib-3
def generate_correlated_data(num_samples: int, correlation: float) -> Tuple[np.ndarray, np.ndarray]:
    """
    Generate two correlated variables.
    
    Args:
        num_samples: Number of data points
        correlation: Desired correlation coefficient (-1 to 1)
    
    Returns:
        Tuple of (x, y) arrays
    """
    # Generate independent standard normal variable
    x_variable = np.random.randn(num_samples)
    
    # Generate correlated variable using Cholesky decomposition concept
    noise = np.random.randn(num_samples)
    y_variable = correlation * x_variable + np.sqrt(1 - correlation**2) * noise
    
    return x_variable, y_variable


# Set random seed
np.random.seed(42)

# Create figure with subplots
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
fig.suptitle('Effect of Correlation on Scatter Patterns', fontsize=14, fontweight='bold')

correlations = [0.95, 0.5, 0.0, -0.8]
titles = ['Strong Positive (r=0.95)', 'Moderate Positive (r=0.5)', 
          'No Correlation (r=0.0)', 'Strong Negative (r=-0.8)']

for ax, corr, title in zip(axes.flat, correlations, titles):
    x_data, y_data = generate_correlated_data(100, corr)
    
    # Create scatter plot
    ax.scatter(x_data, y_data, alpha=0.6, edgecolors='k', linewidth=0.5)
    
    # Fit and plot regression line
    coefficients = np.polyfit(x_data, y_data, 1)
    regression_line = np.polyval(coefficients, x_data)
    ax.plot(x_data, regression_line, 'r--', linewidth=2, label='Regression line')
    
    # Customize subplot
    ax.set_xlabel('Feature X', fontsize=10)
    ax.set_ylabel('Feature Y', fontsize=10)
    ax.set_title(title, fontsize=11)
    ax.legend(fontsize=9)
    ax.grid(True, alpha=0.3)
    
    # Add correlation coefficient text
    actual_corr = np.corrcoef(x_data, y_data)[0, 1]
    ax.text(0.05, 0.95, f'r = {actual_corr:.3f}', 
            transform=ax.transAxes, verticalalignment='top',
            bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

plt.tight_layout()
plt.show()
```

## Statistical Visualizations

### Histograms and Probability Distributions

Histograms help us understand the distribution of data, which is essential for choosing appropriate statistical methods:

```python exec
id: 02-matplotlib-4
def plot_distribution_comparison() -> None:
    """
    Compare different probability distributions visually.
    """
    np.random.seed(42)
    num_samples = 10000
    
    # Generate data from different distributions
    normal_data = np.random.normal(loc=0, scale=1, size=num_samples)
    uniform_data = np.random.uniform(low=-3, high=3, size=num_samples)
    exponential_data = np.random.exponential(scale=1, size=num_samples)
    
    # Create figure
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    fig.suptitle('Distribution Shapes: Visual Identification Guide', fontsize=14, fontweight='bold')
    
    # Plot 1: Normal distribution
    axes[0].hist(normal_data, bins=50, density=True, alpha=0.7, 
                 color='skyblue', edgecolor='black')
    axes[0].set_title('Normal (Gaussian) Distribution', fontsize=12)
    axes[0].set_xlabel('Value', fontsize=10)
    axes[0].set_ylabel('Probability Density', fontsize=10)
    axes[0].axvline(x=np.mean(normal_data), color='r', linestyle='--', 
                    linewidth=2, label=f'Mean = {np.mean(normal_data):.2f}')
    axes[0].legend()
    axes[0].grid(True, alpha=0.3)
    
    # Plot 2: Uniform distribution
    axes[1].hist(uniform_data, bins=50, density=True, alpha=0.7, 
                 color='lightgreen', edgecolor='black')
    axes[1].set_title('Uniform Distribution', fontsize=12)
    axes[1].set_xlabel('Value', fontsize=10)
    axes[1].set_ylabel('Probability Density', fontsize=10)
    axes[1].axvline(x=np.mean(uniform_data), color='r', linestyle='--', 
                    linewidth=2, label=f'Mean = {np.mean(uniform_data):.2f}')
    axes[1].legend()
    axes[1].grid(True, alpha=0.3)
    
    # Plot 3: Exponential distribution
    axes[2].hist(exponential_data, bins=50, density=True, alpha=0.7, 
                 color='lightsalmon', edgecolor='black')
    axes[2].set_title('Exponential Distribution', fontsize=12)
    axes[2].set_xlabel('Value', fontsize=10)
    axes[2].set_ylabel('Probability Density', fontsize=10)
    axes[2].axvline(x=np.mean(exponential_data), color='r', linestyle='--', 
                    linewidth=2, label=f'Mean = {np.mean(exponential_data):.2f}')
    axes[2].legend()
    axes[2].grid(True, alpha=0.3)
    axes[2].set_xlim(0, 6)  # Limit x-axis for better visualization
    
    plt.tight_layout()
    plt.show()
    
    print("Applications in Machine Learning:")
    print("- Normal: Error distributions, Gaussian Naive Bayes")
    print("- Uniform: Random initialization, dropout masks")
    print("- Exponential: Time between events, survival analysis")


plot_distribution_comparison()
```

### Box Plots for Comparing Groups

Box plots effectively summarize distributions and facilitate group comparisons:

```python exec
id: 02-matplotlib-5
def compare_model_performance() -> None:
    """
    Visualize performance of different models using box plots.
    """
    np.random.seed(42)
    
    # Simulate cross-validation scores for different models
    model_scores = {
        'Linear\nRegression': np.random.normal(0.75, 0.05, 30),
        'Ridge\nRegression': np.random.normal(0.78, 0.04, 30),
        'Lasso\nRegression': np.random.normal(0.76, 0.045, 30),
        'Random\nForest': np.random.normal(0.82, 0.03, 30),
        'Gradient\nBoosting': np.random.normal(0.84, 0.035, 30)
    }
    
    # Create figure
    fig, ax = plt.subplots(figsize=(12, 6))
    
    # Create box plot
    positions = np.arange(len(model_scores))
    box_plot = ax.boxplot(model_scores.values(), 
                          labels=model_scores.keys(),
                          positions=positions,
                          widths=0.6,
                          patch_artist=True,
                          showmeans=True,
                          meanline=True)
    
    # Customize box colors
    colors = ['lightblue', 'lightgreen', 'lightyellow', 'lightcoral', 'plum']
    for patch, color in zip(box_plot['boxes'], colors):
        patch.set_facecolor(color)
        patch.set_alpha(0.7)
    
    # Customize plot
    ax.set_xlabel('Model Type', fontsize=12, fontweight='bold')
    ax.set_ylabel('R² Score', fontsize=12, fontweight='bold')
    ax.set_title('Model Performance Comparison (30-Fold Cross-Validation)', 
                 fontsize=14, fontweight='bold')
    ax.grid(True, axis='y', alpha=0.3)
    ax.set_ylim(0.6, 0.95)
    
    # Add reference line for acceptable performance
    ax.axhline(y=0.80, color='red', linestyle='--', linewidth=2, 
               alpha=0.5, label='Acceptable threshold')
    
    ax.legend(fontsize=10)
    
    plt.tight_layout()
    plt.show()
    
    # Print statistics
    print("Model Performance Summary:")
    print(f"{'Model':<20} {'Median':<10} {'IQR':<10}")
    print("-" * 40)
    for model_name, scores in model_scores.items():
        median_score = np.median(scores)
        iqr_score = np.percentile(scores, 75) - np.percentile(scores, 25)
        print(f"{model_name.replace(chr(10), ' '):<20} {median_score:<10.4f} {iqr_score:<10.4f}")


compare_model_performance()
```

## Mathematical Functions and Analysis

### Plotting Loss Functions

Understanding loss function behavior is crucial for optimization. Let's visualize different loss functions:

```python exec
id: 02-matplotlib-6
def mean_squared_error(predictions: np.ndarray, targets: float) -> np.ndarray:
    """
    Calculate Mean Squared Error loss.
    
    Args:
        predictions: Model predictions
        targets: True target value
    
    Returns:
        MSE loss values
    """
    return (predictions - targets) ** 2


def mean_absolute_error(predictions: np.ndarray, targets: float) -> np.ndarray:
    """
    Calculate Mean Absolute Error loss.
    
    Args:
        predictions: Model predictions
        targets: True target value
    
    Returns:
        MAE loss values
    """
    return np.abs(predictions - targets)


def huber_loss(predictions: np.ndarray, targets: float, delta: float = 1.0) -> np.ndarray:
    """
    Calculate Huber loss (robust to outliers).
    
    Args:
        predictions: Model predictions
        targets: True target value
        delta: Threshold for switching between MSE and MAE
    
    Returns:
        Huber loss values
    """
    error = np.abs(predictions - targets)
    quadratic_part = np.minimum(error, delta)
    linear_part = error - quadratic_part
    return 0.5 * quadratic_part ** 2 + delta * linear_part


# Generate prediction range
true_value = 0.0
predictions = np.linspace(-3, 3, 300)

# Calculate losses
mse_values = mean_squared_error(predictions, true_value)
mae_values = mean_absolute_error(predictions, true_value)
huber_values = huber_loss(predictions, true_value, delta=1.0)

# Create plot
plt.figure(figsize=(12, 6))

plt.plot(predictions, mse_values, label='MSE (Mean Squared Error)', linewidth=2)
plt.plot(predictions, mae_values, label='MAE (Mean Absolute Error)', linewidth=2)
plt.plot(predictions, huber_values, label='Huber Loss (δ=1)', linewidth=2)

# Add reference lines
plt.axvline(x=true_value, color='k', linestyle='--', alpha=0.3, linewidth=1)
plt.axhline(y=0, color='k', linestyle='--', alpha=0.3, linewidth=1)

# Customize plot
plt.xlabel('Prediction Error (predicted - true)', fontsize=12)
plt.ylabel('Loss Value', fontsize=12)
plt.title('Comparison of Regression Loss Functions', fontsize=14, fontweight='bold')
plt.legend(fontsize=11, loc='upper center')
plt.grid(True, alpha=0.3)
plt.ylim(0, 6)

# Add annotations
plt.text(1.5, 4.5, 'MSE penalizes\nlarge errors heavily', 
         bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
plt.text(-2.5, 2, 'MAE is linear,\nless sensitive to outliers', 
         bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.5))

plt.tight_layout()
plt.show()

print("Loss Function Properties:")
print("- MSE: Differentiable everywhere, sensitive to outliers")
print("- MAE: Robust to outliers, not differentiable at zero")
print("- Huber: Combines benefits of both, used in robust regression")
```

### Contour Plots for Optimization Landscapes

Contour plots help visualize optimization landscapes in two dimensions:

```python exec
id: 02-matplotlib-7
def visualize_optimization_landscape() -> None:
    """
    Visualize a 2D optimization landscape with contours.
    
    This represents a simplified view of how gradient descent
    navigates the parameter space.
    """
    # Define a simple quadratic function (convex optimization)
    def objective_function(theta1: np.ndarray, theta2: np.ndarray) -> np.ndarray:
        """Quadratic bowl function: f(θ₁, θ₂) = θ₁² + 2θ₂²"""
        return theta1**2 + 2 * theta2**2
    
    # Create mesh grid
    theta1_range = np.linspace(-3, 3, 100)
    theta2_range = np.linspace(-3, 3, 100)
    theta1_mesh, theta2_mesh = np.meshgrid(theta1_range, theta2_range)
    
    # Calculate function values
    function_values = objective_function(theta1_mesh, theta2_mesh)
    
    # Simulate gradient descent path
    learning_rate = 0.1
    num_iterations = 30
    path_theta1 = [2.5]
    path_theta2 = [2.0]
    
    for _ in range(num_iterations):
        # Calculate gradients
        grad_theta1 = 2 * path_theta1[-1]
        grad_theta2 = 4 * path_theta2[-1]
        
        # Update parameters
        new_theta1 = path_theta1[-1] - learning_rate * grad_theta1
        new_theta2 = path_theta2[-1] - learning_rate * grad_theta2
        
        path_theta1.append(new_theta1)
        path_theta2.append(new_theta2)
    
    # Create plot
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
    fig.suptitle('Optimization Landscape Visualization', fontsize=14, fontweight='bold')
    
    # Subplot 1: Contour plot with gradient descent path
    contour = ax1.contour(theta1_mesh, theta2_mesh, function_values, 
                          levels=20, cmap='viridis', alpha=0.6)
    ax1.clabel(contour, inline=True, fontsize=8)
    ax1.plot(path_theta1, path_theta2, 'r.-', linewidth=2, 
             markersize=8, label='Gradient Descent Path')
    ax1.plot(0, 0, 'r*', markersize=20, label='Global Minimum')
    ax1.set_xlabel('Parameter θ₁', fontsize=11)
    ax1.set_ylabel('Parameter θ₂', fontsize=11)
    ax1.set_title('Contour Plot with Optimization Path', fontsize=12)
    ax1.legend(fontsize=10)
    ax1.grid(True, alpha=0.3)
    
    # Subplot 2: Loss over iterations
    loss_values = [objective_function(t1, t2) for t1, t2 in zip(path_theta1, path_theta2)]
    ax2.plot(loss_values, 'b.-', linewidth=2, markersize=8)
    ax2.set_xlabel('Iteration', fontsize=11)
    ax2.set_ylabel('Loss Value', fontsize=11)
    ax2.set_title('Convergence: Loss vs. Iteration', fontsize=12)
    ax2.grid(True, alpha=0.3)
    ax2.set_yscale('log')  # Log scale to see convergence better
    
    plt.tight_layout()
    plt.show()
    
    print(f"Starting point: θ₁={path_theta1[0]:.2f}, θ₂={path_theta2[0]:.2f}")
    print(f"Final point: θ₁={path_theta1[-1]:.6f}, θ₂={path_theta2[-1]:.6f}")
    print(f"Initial loss: {loss_values[0]:.4f}")
    print(f"Final loss: {loss_values[-1]:.8f}")


visualize_optimization_landscape()
```

## Real-World Application: Model Diagnostics

Let's create a comprehensive diagnostic dashboard for evaluating regression models:

```python exec
id: 02-matplotlib-8
def create_regression_diagnostics(true_values: np.ndarray, predictions: np.ndarray) -> None:
    """
    Create comprehensive diagnostic plots for regression analysis.
    
    Args:
        true_values: True target values
        predictions: Model predictions
    """
    residuals = true_values - predictions
    
    # Create figure with multiple subplots
    fig = plt.figure(figsize=(15, 10))
    gs = fig.add_gridspec(2, 2, hspace=0.3, wspace=0.3)
    
    # Plot 1: Predicted vs. Actual
    ax1 = fig.add_subplot(gs[0, 0])
    ax1.scatter(true_values, predictions, alpha=0.6, edgecolors='k', linewidth=0.5)
    
    # Add perfect prediction line
    min_val = min(true_values.min(), predictions.min())
    max_val = max(true_values.max(), predictions.max())
    ax1.plot([min_val, max_val], [min_val, max_val], 'r--', 
             linewidth=2, label='Perfect Prediction')
    
    ax1.set_xlabel('True Values', fontsize=11)
    ax1.set_ylabel('Predicted Values', fontsize=11)
    ax1.set_title('Predicted vs. Actual Values', fontsize=12, fontweight='bold')
    ax1.legend(fontsize=10)
    ax1.grid(True, alpha=0.3)
    
    # Plot 2: Residual Plot
    ax2 = fig.add_subplot(gs[0, 1])
    ax2.scatter(predictions, residuals, alpha=0.6, edgecolors='k', linewidth=0.5)
    ax2.axhline(y=0, color='r', linestyle='--', linewidth=2)
    ax2.set_xlabel('Predicted Values', fontsize=11)
    ax2.set_ylabel('Residuals', fontsize=11)
    ax2.set_title('Residual Plot', fontsize=12, fontweight='bold')
    ax2.grid(True, alpha=0.3)
    
    # Plot 3: Residual Histogram
    ax3 = fig.add_subplot(gs[1, 0])
    ax3.hist(residuals, bins=30, density=True, alpha=0.7, 
             color='skyblue', edgecolor='black')
    
    # Overlay normal distribution
    residual_mean = np.mean(residuals)
    residual_std = np.std(residuals)
    x_range = np.linspace(residuals.min(), residuals.max(), 100)
    normal_curve = (1 / (residual_std * np.sqrt(2 * np.pi))) * \
                   np.exp(-0.5 * ((x_range - residual_mean) / residual_std) ** 2)
    ax3.plot(x_range, normal_curve, 'r-', linewidth=2, label='Normal Distribution')
    
    ax3.set_xlabel('Residuals', fontsize=11)
    ax3.set_ylabel('Density', fontsize=11)
    ax3.set_title('Distribution of Residuals', fontsize=12, fontweight='bold')
    ax3.legend(fontsize=10)
    ax3.grid(True, alpha=0.3)
    
    # Plot 4: Q-Q Plot
    ax4 = fig.add_subplot(gs[1, 1])
    
    # Sort residuals and calculate theoretical quantiles
    sorted_residuals = np.sort(residuals)
    theoretical_quantiles = np.linspace(-3, 3, len(sorted_residuals))
    standardized_residuals = (sorted_residuals - np.mean(residuals)) / np.std(residuals)
    
    ax4.scatter(theoretical_quantiles, standardized_residuals, 
                alpha=0.6, edgecolors='k', linewidth=0.5)
    ax4.plot([-3, 3], [-3, 3], 'r--', linewidth=2, label='Normal Distribution')
    ax4.set_xlabel('Theoretical Quantiles', fontsize=11)
    ax4.set_ylabel('Standardized Residuals', fontsize=11)
    ax4.set_title('Q-Q Plot (Normality Check)', fontsize=12, fontweight='bold')
    ax4.legend(fontsize=10)
    ax4.grid(True, alpha=0.3)
    
    # Overall title
    fig.suptitle('Regression Model Diagnostic Dashboard', 
                 fontsize=14, fontweight='bold', y=0.98)
    
    plt.show()
    
    # Print diagnostic statistics
    r_squared = 1 - (np.sum(residuals**2) / np.sum((true_values - np.mean(true_values))**2))
    rmse = np.sqrt(np.mean(residuals**2))
    mae = np.mean(np.abs(residuals))
    
    print("Diagnostic Statistics:")
    print(f"  R² Score: {r_squared:.4f}")
    print(f"  RMSE: {rmse:.4f}")
    print(f"  MAE: {mae:.4f}")
    print(f"  Mean Residual: {np.mean(residuals):.6f} (should be ≈ 0)")
    print(f"  Std Residual: {np.std(residuals):.4f}")


# Generate sample data
np.random.seed(42)
num_samples = 200

# True values
true_vals = np.random.uniform(0, 100, num_samples)

# Predictions with some error
preds = true_vals + np.random.normal(0, 10, num_samples)

# Create diagnostic plots
create_regression_diagnostics(true_vals, preds)
```

## Practice Exercises

### Your turn 1: Plotting Learning Curves

Create a learning curve plot showing training and validation performance:

```python exec
id: 02-matplotlib-9
def plot_learning_curves(train_scores: np.ndarray, val_scores: np.ndarray) -> None:
    """
    Plot learning curves for model evaluation.
    
    Args:
        train_scores: Training scores over epochs
        val_scores: Validation scores over epochs
    
    TODO: Implement this function to create a learning curve plot with:
    - Two lines (training and validation)
    - Shaded regions showing variance if data is 2D
    - Appropriate labels and title
    - Grid for readability
    - Legend
    """
    # TODO: Implement learning curve visualization
    pass


# Test data
np.random.seed(42)
epochs = np.arange(1, 51)
train_acc = 0.5 + 0.5 * (1 - np.exp(-epochs / 10)) + np.random.normal(0, 0.02, 50)
val_acc = 0.5 + 0.45 * (1 - np.exp(-epochs / 10)) + np.random.normal(0, 0.03, 50)

plot_learning_curves(train_acc, val_acc)
```

### Your turn 2: Feature Importance Visualization

Create a horizontal bar chart showing feature importance:

```python exec
id: 02-matplotlib-10
def plot_feature_importance(feature_names: List[str], importances: np.ndarray) -> None:
    """
    Create a horizontal bar chart of feature importances.
    
    Args:
        feature_names: Names of features
        importances: Importance scores for each feature
    
    TODO: Create a horizontal bar chart that:
    - Sorts features by importance (descending)
    - Uses appropriate colors
    - Has clear labels
    - Shows values on bars
    """
    # TODO: Implement feature importance visualization
    pass


# Test data
features = ['Feature A', 'Feature B', 'Feature C', 'Feature D', 'Feature E']
importance_scores = np.array([0.25, 0.15, 0.30, 0.20, 0.10])

plot_feature_importance(features, importance_scores)
```

## Summary and Key Takeaways

### Core Visualization Principles

1. **Purpose-Driven Design**
   - Choose plot types that match your analytical goals
   - Simplify visual elements to highlight key insights
   - Consider your audience's technical background

2. **Plot Types for Different Tasks**
   - Line plots: Continuous relationships, time series
   - Scatter plots: Correlations, clustering
   - Histograms: Distributions, frequency analysis
   - Box plots: Group comparisons, outlier detection
   - Contour plots: Optimization landscapes, 2D functions

3. **Effective Customization**
   - Always label axes with units
   - Use color meaningfully, not decoratively
   - Add reference lines for context
   - Include legends when comparing multiple series
   - Maintain consistent styling across related plots

### Machine Learning Applications

Visualization is essential throughout the ML pipeline:

- **Data exploration**: Understanding distributions, detecting anomalies
- **Feature engineering**: Identifying relationships, transformations
- **Model selection**: Comparing algorithms, hyperparameters
- **Diagnostics**: Residual analysis, bias-variance tradeoff
- **Results**: Confusion matrices, ROC curves, performance metrics

### Best Practices

1. **Start simple, add complexity only when needed**
2. **Use subplots for multi-faceted comparisons**
3. **Always provide context** (reference lines, annotations)
4. **Save figures in appropriate formats** (vector for publications, raster for web)
5. **Make plots self-explanatory** (descriptive titles, clear labels)

---

## Next Steps

In the next tutorial, **Tutorial D: Object-Oriented Programming Fundamentals**, we'll explore:

- Classes and objects in Python
- Encapsulation and data hiding
- Methods and attributes
- Inheritance and polymorphism
- Building reusable, maintainable code structures

Understanding OOP is crucial for working with modern ML frameworks (scikit-learn, TensorFlow, PyTorch), which are all built using object-oriented design patterns. Let's see how we can structure our code more effectively using these principles.

## Looking back

Before leaving this page, a sentence on each. What you write stays on this device.

```reflect
- Something you expected before running a cell that turned out differently
- The one idea from this page you could explain to someone else now
- Something you would change or try next, if there were time
- A question this page raised for you that it did not answer. Bring it to the next session; these questions are where the next session starts.
```
