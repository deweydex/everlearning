---
title: "Numerical Computing with NumPy"
slug: 01-numpy
course: ai-and-ml-foundations
course_title: "AI and ML Foundations"
series: 0-python-and-numpy-refresher
series_title: "Python and NumPy Refresher"
version: 2026.09.06.1
---

# Numerical Computing with NumPy

## References and Resources

**Primary References:**
- Harris, C. R., et al. (2020). Array programming with NumPy. *Nature*, 585(7825), 357-362. https://doi.org/10.1038/s41586-020-2649-2
- NumPy Developers. (2024). *NumPy User Guide*. https://numpy.org/doc/stable/user/
- VanderPlas, J. (2016). *Python Data Science Handbook*. O'Reilly Media. (Free: https://jakevdp.github.io/PythonDataScienceHandbook/)

**Further Resources:**
- Strang, G. (2016). *Introduction to Linear Algebra* (5th ed.). Wellesley-Cambridge Press.
- McKinney, W. (2022). *Python for Data Analysis* (3rd ed.). O'Reilly Media.
- NumPy Documentation on Broadcasting: https://numpy.org/doc/stable/user/basics.broadcasting.html

---

   - Creating Arrays
   - Array Properties and Attributes
   - Array Indexing and Slicing
3. [Vectorized Operations](#vectorization)
   - Element-wise Operations
   - Broadcasting
   - Universal Functions (ufuncs)
4. [Statistical Operations](#statistics)
   - Descriptive Statistics
   - Correlation and Covariance
5. [Linear Algebra for Machine Learning](#linear-algebra)
   - Matrix Operations
   - Solving Linear Systems
   - Eigenvalues and Eigenvectors
6. [Real-World Application: Linear Regression from Scratch](#application)
7. [Practice Exercises](#exercises)
8. [Summary and Key Takeaways](#summary)

---

## Introduction to NumPy

NumPy (Numerical Python) is the fundamental package for scientific computing in Python. It provides:

- **Efficient multidimensional array objects** (ndarray)
- **Vectorized operations** that avoid slow Python loops
- **Mathematical functions** optimized for arrays
- **Linear algebra capabilities** essential for machine learning

Why is NumPy crucial for data science and machine learning?

1. **Performance**: NumPy operations are implemented in C, making them 10-100x faster than Python loops
2. **Memory efficiency**: Arrays use contiguous memory blocks
3. **Expressiveness**: Vectorized syntax is concise and readable
4. **Foundation**: Most scientific libraries (pandas, scikit-learn, TensorFlow) build on NumPy

Let's begin by importing NumPy with the conventional alias:

```python exec
id: 01-numpy-1
import numpy as np
from typing import Tuple

# Display NumPy version
print(f"NumPy version: {np.__version__}")
```

## Arrays: The Foundation of Numerical Computing

### Creating Arrays

NumPy arrays can be created in several ways. Let's explore the most common methods and when to use each:

```python exec
id: 01-numpy-2
def demonstrate_array_creation() -> None:
    """
    Demonstrate various methods for creating NumPy arrays.
    
    Each method serves different purposes in numerical computing
    and machine learning workflows.
    """
    print("Array Creation Methods:")
    print("=" * 50)
    print()
    
    # Method 1: From Python lists (for known data)
    data_points = np.array([2.5, 3.7, 4.1, 5.9, 6.2])
    print("1. From list:")
    print(f"   {data_points}")
    print()
    
    # Method 2: Zeros (for initialization)
    weights = np.zeros(5)
    print("2. Zeros (weight initialization):")
    print(f"   {weights}")
    print()
    
    # Method 3: Ones (for bias terms or masks)
    bias_vector = np.ones(3)
    print("3. Ones (bias vector):")
    print(f"   {bias_vector}")
    print()
    
    # Method 4: Arange (sequential values)
    time_steps = np.arange(0, 10, 2)  # start, stop, step
    print("4. Arange (time steps):")
    print(f"   {time_steps}")
    print()
    
    # Method 5: Linspace (evenly spaced values)
    x_values = np.linspace(0, 1, 5)  # start, stop, num_points
    print("5. Linspace (evenly spaced):")
    print(f"   {x_values}")
    print()
    
    # Method 6: Random values (for stochastic methods)
    np.random.seed(42)  # For reproducibility
    random_data = np.random.randn(5)  # Standard normal distribution
    print("6. Random (normal distribution):")
    print(f"   {random_data}")
    print()
    
    # Method 7: 2D arrays (matrices)
    design_matrix = np.array([
        [1.0, 2.0, 3.0],
        [4.0, 5.0, 6.0],
        [7.0, 8.0, 9.0]
    ])
    print("7. 2D array (design matrix):")
    print(design_matrix)
    print()


demonstrate_array_creation()
```

### Array Properties and Attributes

Understanding array properties is essential for debugging and designing efficient algorithms. Let's examine the key attributes:

```python exec
id: 01-numpy-3
def analyze_array_properties(array: np.ndarray) -> None:
    """
    Display important properties of a NumPy array.
    
    Args:
        array: NumPy array to analyze
    """
    print("Array Properties:")
    print(f"  Shape: {array.shape}  (dimensions)")
    print(f"  Dimensions: {array.ndim}  (number of axes)")
    print(f"  Size: {array.size}  (total elements)")
    print(f"  Data type: {array.dtype}  (element type)")
    print(f"  Item size: {array.itemsize} bytes  (per element)")
    print(f"  Total bytes: {array.nbytes} bytes")
    print()


# Create sample arrays for analysis
vector_1d = np.array([1, 2, 3, 4, 5])
matrix_2d = np.array([[1, 2, 3], [4, 5, 6]])
tensor_3d = np.ones((2, 3, 4))  # 2 matrices of shape (3, 4)

print("1D Array (Vector):")
analyze_array_properties(vector_1d)

print("2D Array (Matrix):")
analyze_array_properties(matrix_2d)

print("3D Array (Tensor):")
analyze_array_properties(tensor_3d)

print("Application: In deep learning, 3D tensors might represent:")
print("  - (samples, height, width) for grayscale images")
print("  - (samples, time_steps, features) for time series")
```

### Array Indexing and Slicing

Efficient data access is crucial for machine learning workflows. Let's explore NumPy's powerful indexing capabilities:

```python exec
id: 01-numpy-4
def demonstrate_indexing() -> None:
    """
    Demonstrate various indexing and slicing techniques.
    
    These operations are fundamental for data manipulation
    in machine learning pipelines.
    """
    # Create a sample dataset (exam scores across 5 students, 3 subjects)
    scores = np.array([
        [85, 90, 78],  # Student 1: Math, Science, English
        [92, 88, 95],  # Student 2
        [78, 85, 82],  # Student 3
        [95, 92, 89],  # Student 4
        [88, 86, 91]   # Student 5
    ])
    
    print("Original Data (Students × Subjects):")
    print(scores)
    print()
    
    # Basic indexing
    print("1. Single element (Student 2, Science):")
    print(f"   {scores[1, 1]}")
    print()
    
    # Row slicing
    print("2. First three students (all subjects):")
    print(scores[:3, :])
    print()
    
    # Column slicing
    print("3. All students, Math scores only:")
    print(scores[:, 0])
    print()
    
    # Boolean indexing (powerful for filtering)
    print("4. Students with Math score > 85:")
    high_math_scores = scores[scores[:, 0] > 85]
    print(high_math_scores)
    print()
    
    # Fancy indexing (using arrays of indices)
    print("5. Specific students (1st, 3rd, 5th):")
    selected_students = scores[[0, 2, 4], :]
    print(selected_students)
    print()


demonstrate_indexing()
```

## Vectorized Operations

### Element-wise Operations and Performance

Vectorization eliminates explicit loops, resulting in cleaner, faster code. Let's compare approaches:

```python exec
id: 01-numpy-5
import time

def compare_loop_vs_vectorized(array_size: int = 1000000) -> None:
    """
    Compare performance of Python loops vs. NumPy vectorization.
    
    Args:
        array_size: Number of elements to process
    """
    # Create large arrays
    array_a = np.random.rand(array_size)
    array_b = np.random.rand(array_size)
    
    print(f"Computing element-wise product of {array_size:,} elements:")
    print()
    
    # Method 1: Python loop (slow)
    start_time = time.time()
    result_loop = []
    for i in range(len(array_a)):
        result_loop.append(array_a[i] * array_b[i])
    loop_time = time.time() - start_time
    
    # Method 2: NumPy vectorization (fast)
    start_time = time.time()
    result_vectorized = array_a * array_b
    vectorized_time = time.time() - start_time
    
    # Results
    print(f"Python loop time: {loop_time:.4f} seconds")
    print(f"NumPy vectorized time: {vectorized_time:.4f} seconds")
    print(f"Speedup: {loop_time / vectorized_time:.1f}x faster")
    print()
    print("Conclusion: Vectorization is essential for large-scale computations.")


compare_loop_vs_vectorized()
```

### Broadcasting: Elegant Array Operations

Broadcasting allows NumPy to perform operations on arrays of different shapes. Let's see how this simplifies common operations:

```python exec
id: 01-numpy-6
def demonstrate_broadcasting() -> None:
    """
    Demonstrate NumPy broadcasting for efficient computations.
    
    Broadcasting eliminates the need for explicit loops when
    working with arrays of different shapes.
    """
    print("Broadcasting Examples:")
    print("=" * 50)
    print()
    
    # Example 1: Standardization (common preprocessing)
    # Each feature should have mean=0, std=1
    data_matrix = np.array([
        [100, 200, 50],   # Sample 1: height(cm), weight(kg), age
        [150, 180, 45],   # Sample 2
        [180, 220, 55],   # Sample 3
        [120, 190, 48]    # Sample 4
    ])
    
    print("1. Feature Standardization:")
    print("Original data:")
    print(data_matrix)
    print()
    
    # Calculate mean and std for each feature (column)
    feature_means = data_matrix.mean(axis=0)  # Shape: (3,)
    feature_stds = data_matrix.std(axis=0)    # Shape: (3,)
    
    # Broadcasting: (4, 3) - (3,) → (4, 3)
    standardized_data = (data_matrix - feature_means) / feature_stds
    
    print("Feature means:", feature_means)
    print("Feature stds:", feature_stds)
    print("Standardized data:")
    print(standardized_data)
    print(f"Verification - new means: {standardized_data.mean(axis=0)}")
    print(f"Verification - new stds: {standardized_data.std(axis=0)}")
    print()
    
    # Example 2: Adding bias term
    print("2. Adding Bias Term:")
    weights = np.array([0.5, 0.3, 0.2])
    bias = 1.0
    
    # Broadcasting: (4, 3) @ (3,) + scalar
    predictions = standardized_data @ weights + bias
    print(f"Predictions shape: {predictions.shape}")
    print(f"Predictions: {predictions}")
    print()


demonstrate_broadcasting()
```

### Universal Functions (ufuncs)

NumPy's universal functions provide fast element-wise operations. Let's apply them to a real problem:

```python exec
id: 01-numpy-7
def softmax_function(logits: np.ndarray) -> np.ndarray:
    """
    Compute the softmax function for multi-class classification.
    
    Softmax converts logits (raw scores) into probabilities that sum to 1.
    It's used in the output layer of neural networks for classification.
    
    Args:
        logits: Array of raw prediction scores
    
    Returns:
        Array of probabilities summing to 1
    
    Formula: softmax(x_i) = exp(x_i) / Σ exp(x_j)
    
    Note: We subtract max(logits) for numerical stability
    """
    # Subtract max for numerical stability
    exp_logits = np.exp(logits - np.max(logits))
    return exp_logits / np.sum(exp_logits)


def demonstrate_ufuncs() -> None:
    """
    Demonstrate universal functions with a classification example.
    """
    # Simulated raw scores from a 3-class classifier
    raw_scores = np.array([2.5, 1.0, 0.5])  # Scores for classes A, B, C
    
    print("Multi-class Classification with Softmax:")
    print(f"Raw scores: {raw_scores}")
    print()
    
    # Apply softmax
    probabilities = softmax_function(raw_scores)
    
    print("Class probabilities after softmax:")
    classes = ['Class A', 'Class B', 'Class C']
    for class_name, prob in zip(classes, probabilities):
        print(f"  {class_name}: {prob:.4f} ({prob*100:.2f}%)")
    
    print(f"\nSum of probabilities: {np.sum(probabilities):.6f}")
    print(f"Predicted class: {classes[np.argmax(probabilities)]}")
    print()
    
    # Other useful ufuncs
    data = np.array([-2.5, -1.0, 0.0, 1.0, 2.5])
    print("Other Universal Functions:")
    print(f"Original: {data}")
    print(f"Absolute: {np.abs(data)}")
    print(f"Square: {np.square(data)}")
    print(f"Square root (positive): {np.sqrt(np.abs(data))}")
    print(f"Sign: {np.sign(data)}")


demonstrate_ufuncs()
```

## Statistical Operations

### Descriptive Statistics

NumPy provides efficient functions for computing statistical summaries. Let's analyze a dataset:

```python exec
id: 01-numpy-8
def comprehensive_statistical_analysis(data: np.ndarray) -> None:
    """
    Perform comprehensive statistical analysis on a dataset.
    
    Args:
        data: NumPy array containing numerical data
    """
    print("Statistical Analysis:")
    print("=" * 50)
    print()
    
    # Central tendency
    print("Measures of Central Tendency:")
    print(f"  Mean: {np.mean(data):.4f}")
    print(f"  Median: {np.median(data):.4f}")
    print()
    
    # Dispersion
    print("Measures of Dispersion:")
    print(f"  Standard deviation: {np.std(data):.4f}")
    print(f"  Variance: {np.var(data):.4f}")
    print(f"  Range: {np.ptp(data):.4f}  (peak-to-peak)")
    print()
    
    # Quartiles
    print("Quartiles:")
    q1 = np.percentile(data, 25)
    q2 = np.percentile(data, 50)  # median
    q3 = np.percentile(data, 75)
    iqr = q3 - q1
    print(f"  Q1 (25th percentile): {q1:.4f}")
    print(f"  Q2 (50th percentile): {q2:.4f}")
    print(f"  Q3 (75th percentile): {q3:.4f}")
    print(f"  IQR (Interquartile range): {iqr:.4f}")
    print()
    
    # Extremes
    print("Extremes:")
    print(f"  Minimum: {np.min(data):.4f}")
    print(f"  Maximum: {np.max(data):.4f}")
    print(f"  Argmin (index): {np.argmin(data)}")
    print(f"  Argmax (index): {np.argmax(data)}")
    print()


# Generate sample data: test scores with some noise
np.random.seed(42)
test_scores = np.random.normal(loc=75, scale=12, size=100)

print(f"Analyzing {len(test_scores)} test scores:")
print()
comprehensive_statistical_analysis(test_scores)
```

### Correlation and Covariance

Understanding relationships between variables is crucial for feature selection and model interpretation:

```python exec
id: 01-numpy-9
def analyze_correlations() -> None:
    """
    Demonstrate correlation and covariance analysis.
    
    These metrics help identify relationships between features,
    which is essential for:
    - Feature selection
    - Multicollinearity detection
    - Understanding data structure
    """
    # Generate correlated features
    np.random.seed(42)
    num_samples = 100
    
    # Feature 1: Study hours (independent)
    study_hours = np.random.uniform(1, 10, num_samples)
    
    # Feature 2: Test score (correlated with study hours)
    # Score = 50 + 4*hours + noise
    test_score = 50 + 4 * study_hours + np.random.normal(0, 5, num_samples)
    
    # Feature 3: Age (independent, not correlated)
    age = np.random.uniform(18, 25, num_samples)
    
    # Combine features into a matrix
    feature_matrix = np.column_stack([study_hours, test_score, age])
    
    print("Correlation and Covariance Analysis:")
    print("=" * 50)
    print()
    
    # Correlation matrix
    correlation_matrix = np.corrcoef(feature_matrix.T)
    print("Correlation Matrix:")
    print("Features: [Study Hours, Test Score, Age]")
    print(correlation_matrix)
    print()
    
    # Interpretation
    print("Interpretation:")
    print(f"  Study Hours ↔ Test Score: r = {correlation_matrix[0, 1]:.3f}")
    print(f"    Strong positive correlation (as expected)")
    print(f"  Study Hours ↔ Age: r = {correlation_matrix[0, 2]:.3f}")
    print(f"    Weak correlation (independent variables)")
    print(f"  Test Score ↔ Age: r = {correlation_matrix[1, 2]:.3f}")
    print(f"    Weak correlation (independent variables)")
    print()
    
    # Covariance matrix
    covariance_matrix = np.cov(feature_matrix.T)
    print("Covariance Matrix:")
    print(covariance_matrix)
    print()
    print("Note: Covariance depends on scale, correlation is standardized.")


analyze_correlations()
```

## Linear Algebra for Machine Learning

### Matrix Operations

Linear algebra is the mathematical foundation of machine learning. Let's explore essential operations:

```python exec
id: 01-numpy-10
def demonstrate_matrix_operations() -> None:
    """
    Demonstrate fundamental matrix operations for machine learning.
    """
    print("Essential Matrix Operations:")
    print("=" * 50)
    print()
    
    # Define matrices
    matrix_a = np.array([
        [1, 2],
        [3, 4]
    ])
    
    matrix_b = np.array([
        [5, 6],
        [7, 8]
    ])
    
    vector_x = np.array([1, 2])
    
    print("Matrix A:")
    print(matrix_a)
    print()
    
    print("Matrix B:")
    print(matrix_b)
    print()
    
    # Matrix multiplication (dot product)
    print("1. Matrix Multiplication (A @ B):")
    product = matrix_a @ matrix_b  # or np.matmul(A, B)
    print(product)
    print("Application: Neural network forward pass")
    print()
    
    # Matrix-vector multiplication
    print("2. Matrix-Vector Multiplication (A @ x):")
    result = matrix_a @ vector_x
    print(result)
    print("Application: Linear transformation, predictions")
    print()
    
    # Transpose
    print("3. Transpose (A.T):")
    transposed = matrix_a.T
    print(transposed)
    print("Application: Gradient computation, feature engineering")
    print()
    
    # Trace
    print("4. Trace (sum of diagonal):")
    trace = np.trace(matrix_a)
    print(f"tr(A) = {trace}")
    print("Application: Optimization algorithms")
    print()
    
    # Determinant
    print("5. Determinant:")
    det = np.linalg.det(matrix_a)
    print(f"det(A) = {det:.4f}")
    print("Application: Checks if matrix is invertible")
    print()
    
    # Matrix inverse
    if det != 0:
        print("6. Matrix Inverse (A^(-1)):")
        inverse = np.linalg.inv(matrix_a)
        print(inverse)
        print("Verification (A @ A^(-1) should be identity):")
        print(matrix_a @ inverse)
        print("Application: Solving linear systems, normal equations")
        print()


demonstrate_matrix_operations()
```

### Solving Linear Systems

Many machine learning problems reduce to solving systems of linear equations. Let's see how:

```python exec
id: 01-numpy-11
def solve_linear_system_example() -> None:
    """
    Demonstrate solving systems of linear equations.
    
    Problem: Find weights that minimize error in a linear model.
    This is the foundation of linear regression.
    """
    print("Solving Linear System: Ax = b")
    print("=" * 50)
    print()
    
    # System of equations:
    # 2x + 3y = 8
    # 1x + 4y = 9
    
    coefficient_matrix = np.array([
        [2, 3],
        [1, 4]
    ])
    
    constants = np.array([8, 9])
    
    print("System of equations:")
    print("  2x + 3y = 8")
    print("  1x + 4y = 9")
    print()
    
    # Solution using np.linalg.solve (efficient)
    solution = np.linalg.solve(coefficient_matrix, constants)
    
    print(f"Solution: x = {solution[0]:.4f}, y = {solution[1]:.4f}")
    print()
    
    # Verification
    verification = coefficient_matrix @ solution
    print("Verification (A @ x should equal b):")
    print(f"  Computed: {verification}")
    print(f"  Expected: {constants}")
    print(f"  Error: {np.linalg.norm(verification - constants):.10f}")
    print()
    
    print("Application: This is exactly what happens in the")
    print("normal equations for linear regression!")


solve_linear_system_example()
```

### Eigenvalues and Eigenvectors

Eigendecomposition is fundamental to Principal Component Analysis (PCA) and many other ML algorithms:

```python exec
id: 01-numpy-12
def demonstrate_eigendecomposition() -> None:
    """
    Demonstrate eigenvalue decomposition and its applications.
    
    Eigenvalues and eigenvectors reveal fundamental properties
    of linear transformations and are used in:
    - PCA (dimensionality reduction)
    - Spectral clustering
    - Graph algorithms
    """
    print("Eigenvalue Decomposition:")
    print("=" * 50)
    print()
    
    # Create a covariance-like matrix (symmetric, positive semi-definite)
    covariance_matrix = np.array([
        [4.0, 2.0],
        [2.0, 3.0]
    ])
    
    print("Covariance Matrix:")
    print(covariance_matrix)
    print()
    
    # Compute eigenvalues and eigenvectors
    eigenvalues, eigenvectors = np.linalg.eig(covariance_matrix)
    
    print("Eigenvalues:")
    for index, eigenvalue in enumerate(eigenvalues):
        print(f"  λ{index + 1} = {eigenvalue:.4f}")
    print()
    
    print("Eigenvectors (as columns):")
    print(eigenvectors)
    print()
    
    # Interpretation for PCA
    print("Interpretation for PCA:")
    total_variance = np.sum(eigenvalues)
    
    for index, eigenvalue in enumerate(eigenvalues):
        explained_variance = (eigenvalue / total_variance) * 100
        print(f"  PC{index + 1}: {explained_variance:.2f}% of variance")
    
    print()
    print("The first principal component (largest eigenvalue)")
    print("captures the direction of maximum variance.")
    
    # Verification: A @ v = λ @ v
    print()
    print("Verification (A @ v should equal λ * v):")
    first_eigenvector = eigenvectors[:, 0]
    first_eigenvalue = eigenvalues[0]
    
    left_side = covariance_matrix @ first_eigenvector
    right_side = first_eigenvalue * first_eigenvector
    
    print(f"  A @ v = {left_side}")
    print(f"  λ * v = {right_side}")
    print(f"  Error: {np.linalg.norm(left_side - right_side):.10f}")


demonstrate_eigendecomposition()
```

## Real-World Application: Linear Regression from Scratch

Let's implement linear regression using NumPy, demonstrating how all the concepts come together:

```python exec
id: 01-numpy-13
class LinearRegressionNumPy:
    """
    Linear regression implementation using NumPy.
    
    This implementation uses the normal equation approach:
    θ = (X^T X)^(-1) X^T y
    
    Attributes:
        coefficients: Learned regression coefficients
        intercept: Learned intercept term
    """
    
    def __init__(self) -> None:
        self.coefficients: np.ndarray = None
        intercept: float = None
    
    def fit(self, features: np.ndarray, targets: np.ndarray) -> None:
        """
        Fit the linear regression model using normal equations.
        
        Args:
            features: Design matrix of shape (n_samples, n_features)
            targets: Target values of shape (n_samples,)
        """
        # Add column of ones for intercept term
        num_samples = features.shape[0]
        features_with_intercept = np.column_stack([
            np.ones(num_samples), 
            features
        ])
        
        # Normal equation: θ = (X^T X)^(-1) X^T y
        xtx = features_with_intercept.T @ features_with_intercept
        xty = features_with_intercept.T @ targets
        theta = np.linalg.solve(xtx, xty)
        
        # Store parameters
        self.intercept = theta[0]
        self.coefficients = theta[1:]
    
    def predict(self, features: np.ndarray) -> np.ndarray:
        """
        Make predictions using the fitted model.
        
        Args:
            features: Input features of shape (n_samples, n_features)
        
        Returns:
            Predicted values of shape (n_samples,)
        """
        return self.intercept + features @ self.coefficients
    
    def score(self, features: np.ndarray, targets: np.ndarray) -> float:
        """
        Calculate R² score (coefficient of determination).
        
        Args:
            features: Input features
            targets: True target values
        
        Returns:
            R² score (1.0 = perfect fit, 0.0 = baseline)
        """
        predictions = self.predict(features)
        
        # Total sum of squares
        ss_total = np.sum((targets - np.mean(targets)) ** 2)
        
        # Residual sum of squares
        ss_residual = np.sum((targets - predictions) ** 2)
        
        # R² = 1 - (SS_res / SS_tot)
        r_squared = 1 - (ss_residual / ss_total)
        
        return r_squared


def demonstrate_linear_regression() -> None:
    """
    Demonstrate linear regression on synthetic data.
    """
    print("Linear Regression from Scratch:")
    print("=" * 50)
    print()
    
    # Generate synthetic data
    np.random.seed(42)
    num_samples = 100
    
    # Feature: hours studied
    study_hours = np.random.uniform(1, 10, num_samples)
    
    # Target: test score = 50 + 5*hours + noise
    true_intercept = 50
    true_coefficient = 5
    noise = np.random.normal(0, 5, num_samples)
    test_scores = true_intercept + true_coefficient * study_hours + noise
    
    # Reshape for model
    features_2d = study_hours.reshape(-1, 1)
    
    print(f"Generated {num_samples} samples")
    print(f"True relationship: score = {true_intercept} + {true_coefficient} * hours + noise")
    print()
    
    # Fit model
    model = LinearRegressionNumPy()
    model.fit(features_2d, test_scores)
    
    print("Learned parameters:")
    print(f"  Intercept: {model.intercept:.4f} (true: {true_intercept})")
    print(f"  Coefficient: {model.coefficients[0]:.4f} (true: {true_coefficient})")
    print()
    
    # Evaluate
    r_squared = model.score(features_2d, test_scores)
    print(f"Model performance:")
    print(f"  R² score: {r_squared:.4f}")
    print()
    
    # Make predictions
    test_hours = np.array([[3], [5], [7]])
    predictions = model.predict(test_hours)
    
    print("Sample predictions:")
    for hours, score in zip(test_hours.flatten(), predictions):
        print(f"  {hours} hours → {score:.2f} points")


demonstrate_linear_regression()
```

## Practice Exercises

### Your turn 1: Polynomial Features

Implement a function to create polynomial features for non-linear regression:

```python exec
id: 01-numpy-14
def create_polynomial_features(input_array: np.ndarray, degree: int) -> np.ndarray:
    """
    Create polynomial features up to specified degree.
    
    For input x, creates features: [1, x, x², x³, ..., x^degree]
    
    Args:
        input_array: Input features of shape (n_samples,) or (n_samples, 1)
        degree: Maximum polynomial degree
    
    Returns:
        Polynomial features of shape (n_samples, degree + 1)
    
    Hint: Use np.power() and np.column_stack()
    """
    # TODO: Implement polynomial feature creation
    pass


# Test your implementation
test_input = np.array([1, 2, 3, 4, 5])
poly_features = create_polynomial_features(test_input, degree=3)

print("Polynomial Features (degree=3):")
print("Input:", test_input)
print("Features shape:", poly_features.shape)
print("Features:")
print(poly_features)
```

### Your turn 2: Distance Metrics

Implement Euclidean and Manhattan distance calculations:

```python exec
id: 01-numpy-15
def euclidean_distance(point1: np.ndarray, point2: np.ndarray) -> float:
    """
    Calculate Euclidean distance between two points.
    
    Formula: √(Σ(xi - yi)²)
    
    Args:
        point1: First point
        point2: Second point
    
    Returns:
        Euclidean distance
    
    Hint: Use np.sqrt() and np.sum()
    """
    # TODO: Implement Euclidean distance
    pass


def manhattan_distance(point1: np.ndarray, point2: np.ndarray) -> float:
    """
    Calculate Manhattan (L1) distance between two points.
    
    Formula: Σ|xi - yi|
    
    Args:
        point1: First point
        point2: Second point
    
    Returns:
        Manhattan distance
    
    Hint: Use np.abs() and np.sum()
    """
    # TODO: Implement Manhattan distance
    pass


# Test your implementation
point_a = np.array([1, 2, 3])
point_b = np.array([4, 6, 8])

print("Distance Calculations:")
print(f"Point A: {point_a}")
print(f"Point B: {point_b}")
print(f"Euclidean distance: {euclidean_distance(point_a, point_b):.4f}")
print(f"Manhattan distance: {manhattan_distance(point_a, point_b):.4f}")
```

### Your turn 3: Batch Normalization

Implement batch normalization, a key technique in deep learning:

```python exec
id: 01-numpy-16
def batch_normalize(data: np.ndarray, epsilon: float = 1e-8) -> np.ndarray:
    """
    Apply batch normalization to data.
    
    Formula: (x - μ) / √(σ² + ε)
    where μ is mean, σ² is variance, ε prevents division by zero
    
    Args:
        data: Input data of shape (n_samples, n_features)
        epsilon: Small constant for numerical stability
    
    Returns:
        Normalized data with mean≈0, std≈1 for each feature
    
    Hint: Normalize each feature (column) independently
    """
    # TODO: Implement batch normalization
    # 1. Calculate mean and std for each feature
    # 2. Normalize: (data - mean) / (std + epsilon)
    pass


# Test your implementation
np.random.seed(42)
test_data = np.random.randn(100, 3) * 10 + 50  # Random data with mean≈50

normalized_data = batch_normalize(test_data)

print("Batch Normalization:")
print("Original data statistics:")
print(f"  Mean per feature: {test_data.mean(axis=0)}")
print(f"  Std per feature: {test_data.std(axis=0)}")
print()
print("Normalized data statistics:")
print(f"  Mean per feature: {normalized_data.mean(axis=0)}")
print(f"  Std per feature: {normalized_data.std(axis=0)}")
```

## Summary and Key Takeaways

### Core NumPy Concepts

1. **Arrays (ndarray)**
   - Efficient multidimensional containers
   - Fixed type, contiguous memory
   - Foundation for all numerical computing

2. **Vectorization**
   - Eliminates explicit loops
   - 10-100x faster than Python loops
   - More readable and maintainable code

3. **Broadcasting**
   - Implicit expansion of arrays
   - Enables operations on different shapes
   - Essential for efficient batch operations

4. **Statistical Operations**
   - Built-in descriptive statistics
   - Correlation and covariance analysis
   - Foundation for exploratory data analysis

5. **Linear Algebra**
   - Matrix operations for transformations
   - Solving systems of equations
   - Eigendecomposition for PCA

### Machine Learning Applications

NumPy operations appear throughout machine learning:

- **Data preprocessing**: Normalization, standardization
- **Model implementation**: Linear regression, neural networks
- **Optimization**: Gradient descent, matrix factorization
- **Evaluation**: Distance metrics, similarity measures
- **Dimensionality reduction**: PCA, matrix decomposition

### Best Practices

1. **Always vectorize**: Avoid explicit Python loops
2. **Use appropriate dtypes**: Match precision to problem requirements
3. **Leverage broadcasting**: Simplify operations on different shapes
4. **Profile for performance**: Use NumPy's optimized functions
5. **Understand memory layout**: Contiguous arrays are faster

---

## Next Steps

In the next tutorial, **Tutorial C: Data Visualization with Matplotlib**, we'll explore:

- Creating publication-quality plots
- Visualizing statistical distributions
- Plotting mathematical functions
- Customizing plot aesthetics
- Multi-panel figures for comparisons

Visualization is essential for understanding data, diagnosing models, and communicating results. Matplotlib builds naturally on NumPy arrays, making it the perfect next step in our journey.

## Looking back

Before leaving this page, a sentence on each. What you write stays on this device.

```reflect
- Something you expected before running a cell that turned out differently
- The one idea from this page you could explain to someone else now
- Something you would change or try next, if there were time
- A question this page raised for you that it did not answer. Bring it to the next session; these questions are where the next session starts.
```
