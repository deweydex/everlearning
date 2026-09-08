---
title: "Tutorial 12: Object-Oriented Programming Fundamentals"
slug: tutorial-12-object-oriented-programming
course: programming-and-design-principles
course_title: "Programming and Design Principles"
series: tutorials
series_title: "Tutorials"
version: 2026.09.06.1
---

# Tutorial 12: Object-Oriented Programming Fundamentals

## References and Resources

**Primary References:**
- Lutz, M. (2013). *Learning Python* (5th ed.). O'Reilly Media.
- Ramalho, L. (2022). *Fluent Python* (2nd ed.). O'Reilly Media.
- Python Software Foundation. (2024). *Python Tutorial: Classes*. https://docs.python.org/3/tutorial/classes.html

**Further Resources:**
- Martin, R. C. (2008). *Clean Code: A Handbook of Agile Software Craftsmanship*. Prentice Hall.
- Gamma, E., et al. (1994). *Design Patterns: Elements of Reusable Object-Oriented Software*. Addison-Wesley.
- Real Python OOP Guide: https://realpython.com/python3-object-oriented-programming/
- PEP 8 Style Guide: https://peps.python.org/pep-0008/

---

   - Defining Classes
   - Creating Objects (Instances)
   - Attributes and Methods
3. [Encapsulation and Data Hiding](#encapsulation)
4. [Class Methods and Static Methods](#class-methods)
5. [Inheritance](#inheritance)
   - Basic Inheritance
   - Method Overriding
   - Multiple Inheritance
6. [Polymorphism](#polymorphism)
7. [Real-World Application: Machine Learning Model Classes](#application)
8. [Practice Exercises](#exercises)
9. [Summary and Key Takeaways](#summary)

---

## Introduction to Object-Oriented Programming

Object-Oriented Programming (OOP) is a paradigm that organizes code around **objects**—bundles of data and functions that operate on that data. This approach offers several advantages:

- **Modularity**: Code is organized into self-contained units
- **Reusability**: Classes can be reused across projects
- **Maintainability**: Changes are localized, reducing bugs
- **Abstraction**: Complex systems can be represented simply

### Key OOP Concepts

1. **Class**: A blueprint or template for creating objects
2. **Object (Instance)**: A specific realization of a class
3. **Attribute**: Data stored in an object
4. **Method**: Function that operates on object data
5. **Encapsulation**: Bundling data with methods that operate on it
6. **Inheritance**: Creating new classes from existing ones
7. **Polymorphism**: Using a unified interface for different types

Let's explore these concepts through practical examples in machine learning and statistics.

## Classes and Objects

### Defining a Basic Class

Let's start by creating a class to represent a statistical dataset:

```python exec
id: tutorial-12-object-oriented-programming-1
import numpy as np
from typing import Optional, Tuple


class Dataset:
    """
    A class to represent and analyze a numerical dataset.
    
    This class encapsulates data along with methods for computing
    statistical properties, demonstrating the core OOP principle
    of bundling data with behavior.
    
    Attributes:
        name: A descriptive name for the dataset
        data: NumPy array containing the numerical values
    """
    
    def __init__(self, name: str, data: np.ndarray) -> None:
        """
        Initialize a Dataset object.
        
        The __init__ method is called automatically when creating
        a new instance. It sets up the object's initial state.
        
        Args:
            name: A descriptive name for the dataset
            data: NumPy array of numerical values
        """
        self.name = name
        self.data = np.array(data)  # Ensure it's a NumPy array
    
    def calculate_mean(self) -> float:
        """
        Calculate the arithmetic mean of the dataset.
        
        Returns:
            The mean value
        """
        return np.mean(self.data)
    
    def calculate_std(self) -> float:
        """
        Calculate the standard deviation of the dataset.
        
        Returns:
            The standard deviation
        """
        return np.std(self.data)
    
    def calculate_median(self) -> float:
        """
        Calculate the median of the dataset.
        
        Returns:
            The median value
        """
        return np.median(self.data)
    
    def summarize(self) -> None:
        """
        Print a statistical summary of the dataset.
        """
        print(f"Dataset: {self.name}")
        print(f"  Size: {len(self.data)} observations")
        print(f"  Mean: {self.calculate_mean():.4f}")
        print(f"  Median: {self.calculate_median():.4f}")
        print(f"  Std Dev: {self.calculate_std():.4f}")
        print(f"  Range: [{np.min(self.data):.2f}, {np.max(self.data):.2f}]")


# Creating objects (instances) of the Dataset class
exam_scores = Dataset(
    name="Final Exam Scores",
    data=np.array([85, 92, 78, 95, 88, 76, 90, 82, 89, 91])
)

project_grades = Dataset(
    name="Project Grades",
    data=np.array([88, 94, 81, 97, 90, 79, 92, 85, 91, 93])
)

# Using the objects
print("Analyzing two separate datasets:\n")
exam_scores.summarize()
print()
project_grades.summarize()

print("\nKey Concept: Each object maintains its own state (data)")
print("while sharing the same methods (behavior).")
```

### Instance Attributes vs. Class Attributes

Let's explore the difference between instance and class attributes:

```python exec
id: tutorial-12-object-oriented-programming-2
class NeuralNetworkLayer:
    """
    Represents a layer in a neural network.
    
    Demonstrates the difference between instance attributes
    (unique to each layer) and class attributes (shared by all layers).
    
    Class Attributes:
        total_layers: Count of all layers created
        supported_activations: List of available activation functions
    
    Instance Attributes:
        layer_id: Unique identifier for this layer
        num_neurons: Number of neurons in this layer
        activation: Activation function for this layer
    """
    
    # Class attributes (shared by all instances)
    total_layers = 0
    supported_activations = ['relu', 'sigmoid', 'tanh', 'softmax']
    
    def __init__(self, num_neurons: int, activation: str = 'relu') -> None:
        """
        Initialize a neural network layer.
        
        Args:
            num_neurons: Number of neurons in this layer
            activation: Activation function name
        
        Raises:
            ValueError: If activation function is not supported
        """
        if activation not in NeuralNetworkLayer.supported_activations:
            raise ValueError(
                f"Activation '{activation}' not supported. "
                f"Choose from {NeuralNetworkLayer.supported_activations}"
            )
        
        # Instance attributes (unique to each object)
        NeuralNetworkLayer.total_layers += 1
        self.layer_id = NeuralNetworkLayer.total_layers
        self.num_neurons = num_neurons
        self.activation = activation
    
    def describe(self) -> None:
        """
        Print a description of this layer.
        """
        print(f"Layer {self.layer_id}:")
        print(f"  Neurons: {self.num_neurons}")
        print(f"  Activation: {self.activation}")


# Create multiple layers
print("Building a neural network architecture:\n")

input_layer = NeuralNetworkLayer(num_neurons=784, activation='relu')
hidden_layer1 = NeuralNetworkLayer(num_neurons=128, activation='relu')
hidden_layer2 = NeuralNetworkLayer(num_neurons=64, activation='relu')
output_layer = NeuralNetworkLayer(num_neurons=10, activation='softmax')

# Each layer has unique attributes
input_layer.describe()
print()
hidden_layer1.describe()
print()
output_layer.describe()

# But they share class attributes
print(f"\nTotal layers created: {NeuralNetworkLayer.total_layers}")
print(f"Supported activations: {NeuralNetworkLayer.supported_activations}")
```

## Encapsulation and Data Hiding

Encapsulation involves bundling data with methods and controlling access to internal state. Let's implement a class with private attributes:

```python exec
id: tutorial-12-object-oriented-programming-3
class TrainingHistory:
    """
    Tracks training metrics with controlled access.
    
    This class demonstrates encapsulation by:
    1. Keeping internal data private (using underscore convention)
    2. Providing public methods for controlled access
    3. Validating data before modification
    
    Private Attributes:
        _train_losses: List of training loss values
        _val_losses: List of validation loss values
        _epochs: List of epoch numbers
    """
    
    def __init__(self) -> None:
        """
        Initialize an empty training history.
        
        The underscore prefix indicates these attributes should be
        treated as private (Python convention, not enforced).
        """
        self._train_losses = []
        self._val_losses = []
        self._epochs = []
    
    def record_epoch(self, epoch: int, train_loss: float, val_loss: float) -> None:
        """
        Record metrics for a training epoch.
        
        This method provides controlled access to internal data,
        ensuring data integrity through validation.
        
        Args:
            epoch: Epoch number (must be sequential)
            train_loss: Training loss value
            val_loss: Validation loss value
        
        Raises:
            ValueError: If epoch number is not sequential
        """
        # Validation: ensure sequential epochs
        expected_epoch = len(self._epochs) + 1
        if epoch != expected_epoch:
            raise ValueError(
                f"Expected epoch {expected_epoch}, got {epoch}. "
                "Epochs must be recorded sequentially."
            )
        
        # Record data
        self._epochs.append(epoch)
        self._train_losses.append(train_loss)
        self._val_losses.append(val_loss)
    
    def get_best_epoch(self) -> Optional[Tuple[int, float]]:
        """
        Find the epoch with lowest validation loss.
        
        Returns:
            Tuple of (epoch_number, validation_loss) or None if no data
        """
        if not self._val_losses:
            return None
        
        best_index = np.argmin(self._val_losses)
        return (self._epochs[best_index], self._val_losses[best_index])
    
    def check_overfitting(self, threshold: float = 0.1) -> bool:
        """
        Check if model is overfitting.
        
        Overfitting is detected when validation loss exceeds
        training loss by more than the threshold.
        
        Args:
            threshold: Maximum acceptable difference
        
        Returns:
            True if overfitting is detected
        """
        if len(self._epochs) < 2:
            return False
        
        recent_train = self._train_losses[-1]
        recent_val = self._val_losses[-1]
        
        return (recent_val - recent_train) > threshold
    
    def get_summary(self) -> dict[str, float]:
        """
        Get summary statistics.
        
        Returns:
            Dictionary with summary metrics
        """
        if not self._epochs:
            return {}
        
        return {
            'total_epochs': len(self._epochs),
            'final_train_loss': self._train_losses[-1],
            'final_val_loss': self._val_losses[-1],
            'best_val_loss': min(self._val_losses),
            'overfitting_detected': self.check_overfitting()
        }


# Demonstrate encapsulation
print("Training a model and tracking progress:\n")

history = TrainingHistory()

# Simulate training
np.random.seed(42)
for epoch in range(1, 11):
    # Simulate decreasing loss with some noise
    train_loss = 1.0 * np.exp(-0.2 * epoch) + np.random.normal(0, 0.02)
    val_loss = 1.0 * np.exp(-0.15 * epoch) + np.random.normal(0, 0.03)
    
    history.record_epoch(epoch, train_loss, val_loss)
    
    if epoch % 3 == 0:
        print(f"Epoch {epoch}: Train={train_loss:.4f}, Val={val_loss:.4f}")

# Access data through methods (not direct attribute access)
print("\nTraining Summary:")
summary = history.get_summary()
for key, value in summary.items():
    print(f"  {key}: {value}")

best_epoch, best_loss = history.get_best_epoch()
print(f"\nBest model at epoch {best_epoch} with loss {best_loss:.4f}")

print("\nNote: Direct access to _train_losses is possible but discouraged.")
print("Encapsulation helps maintain data integrity.")
```

## Class Methods and Static Methods

Python provides decorators for different types of methods:

```python exec
id: tutorial-12-object-oriented-programming-4
class DataPreprocessor:
    """
    Utility class for data preprocessing.
    
    Demonstrates three types of methods:
    1. Instance methods: Operate on instance data
    2. Class methods: Operate on class-level data
    3. Static methods: Utility functions (no access to instance or class)
    """
    
    # Class attribute
    default_scaling_method = 'standardization'
    
    def __init__(self, data: np.ndarray) -> None:
        """
        Initialize preprocessor with data.
        
        Args:
            data: Input data array
        """
        self.data = data
        self.scaled_data = None
    
    # Regular instance method
    def standardize(self) -> np.ndarray:
        """
        Standardize the instance's data (mean=0, std=1).
        
        Returns:
            Standardized data
        """
        mean = np.mean(self.data)
        std = np.std(self.data)
        self.scaled_data = (self.data - mean) / std
        return self.scaled_data
    
    # Class method (uses @classmethod decorator)
    @classmethod
    def from_list(cls, data_list: list[float]) -> 'DataPreprocessor':
        """
        Alternative constructor from a Python list.
        
        Class methods are often used as alternative constructors.
        They receive the class (cls) as first argument, not an instance.
        
        Args:
            data_list: Python list of numerical values
        
        Returns:
            New DataPreprocessor instance
        """
        data_array = np.array(data_list)
        return cls(data_array)
    
    @classmethod
    def set_default_scaling(cls, method: str) -> None:
        """
        Set the default scaling method for all instances.
        
        Args:
            method: Scaling method name
        """
        cls.default_scaling_method = method
        print(f"Default scaling method set to: {method}")
    
    # Static method (uses @staticmethod decorator)
    @staticmethod
    def calculate_outliers(data: np.ndarray, num_std: float = 3.0) -> np.ndarray:
        """
        Identify outliers using the standard deviation method.
        
        Static methods don't access instance or class data.
        They're utility functions that logically belong to the class.
        
        Args:
            data: Input data array
            num_std: Number of standard deviations for threshold
        
        Returns:
            Boolean array indicating outliers
        """
        mean = np.mean(data)
        std = np.std(data)
        threshold = num_std * std
        
        is_outlier = np.abs(data - mean) > threshold
        return is_outlier
    
    @staticmethod
    def validate_data(data: np.ndarray) -> bool:
        """
        Check if data is valid for preprocessing.
        
        Args:
            data: Input data array
        
        Returns:
            True if data is valid
        """
        if data.size == 0:
            return False
        if np.any(np.isnan(data)):
            return False
        if np.any(np.isinf(data)):
            return False
        return True


# Demonstrate different method types
print("Method Types Demonstration:\n")

# Using instance method
data = np.array([10, 20, 30, 40, 50, 100])  # 100 is an outlier
preprocessor = DataPreprocessor(data)
standardized = preprocessor.standardize()
print("Instance method (standardize):")
print(f"  Original: {data}")
print(f"  Standardized: {standardized}")
print()

# Using class method (alternative constructor)
data_list = [15, 25, 35, 45, 55]
preprocessor2 = DataPreprocessor.from_list(data_list)
print("Class method (alternative constructor):")
print(f"  Created from list: {data_list}")
print()

# Using static method (no instance needed)
outliers = DataPreprocessor.calculate_outliers(data)
print("Static method (outlier detection):")
print(f"  Data: {data}")
print(f"  Outliers: {data[outliers]}")
print()

# Validation using static method
valid_data = np.array([1, 2, 3])
invalid_data = np.array([1, np.nan, 3])
print("Static method (validation):")
print(f"  Valid data: {DataPreprocessor.validate_data(valid_data)}")
print(f"  Invalid data: {DataPreprocessor.validate_data(invalid_data)}")
```

## Inheritance

### Basic Inheritance

Inheritance allows us to create new classes based on existing ones, promoting code reuse:

```python exec
id: tutorial-12-object-oriented-programming-5
class BaseModel:
    """
    Base class for machine learning models.
    
    This abstract base class defines the common interface
    that all ML models should implement.
    
    Attributes:
        model_name: Name identifying this model
        is_trained: Whether the model has been trained
    """
    
    def __init__(self, model_name: str) -> None:
        """
        Initialize the base model.
        
        Args:
            model_name: Name for this model instance
        """
        self.model_name = model_name
        self.is_trained = False
    
    def fit(self, features: np.ndarray, targets: np.ndarray) -> None:
        """
        Train the model on data.
        
        This is a template method that subclasses should override.
        
        Args:
            features: Training features
            targets: Training targets
        """
        raise NotImplementedError("Subclasses must implement fit()")
    
    def predict(self, features: np.ndarray) -> np.ndarray:
        """
        Make predictions on new data.
        
        This is a template method that subclasses should override.
        
        Args:
            features: Input features
        
        Returns:
            Predictions
        """
        raise NotImplementedError("Subclasses must implement predict()")
    
    def get_info(self) -> str:
        """
        Get model information.
        
        This method is inherited by all subclasses.
        
        Returns:
            Model information string
        """
        status = "trained" if self.is_trained else "untrained"
        return f"{self.model_name} ({status})"


class SimpleLinearRegression(BaseModel):
    """
    Simple linear regression model (one feature).
    
    Inherits from BaseModel and implements the required methods.
    
    Attributes:
        slope: Learned slope parameter
        intercept: Learned intercept parameter
    """
    
    def __init__(self) -> None:
        """
        Initialize simple linear regression model.
        """
        super().__init__("Simple Linear Regression")  # Call parent constructor
        self.slope = None
        self.intercept = None
    
    def fit(self, features: np.ndarray, targets: np.ndarray) -> None:
        """
        Fit the model using ordinary least squares.
        
        Args:
            features: Training features (1D array)
            targets: Training targets
        """
        # Calculate slope and intercept
        feature_mean = np.mean(features)
        target_mean = np.mean(targets)
        
        numerator = np.sum((features - feature_mean) * (targets - target_mean))
        denominator = np.sum((features - feature_mean) ** 2)
        
        self.slope = numerator / denominator
        self.intercept = target_mean - self.slope * feature_mean
        
        self.is_trained = True
    
    def predict(self, features: np.ndarray) -> np.ndarray:
        """
        Make predictions using the linear model.
        
        Args:
            features: Input features
        
        Returns:
            Predictions
        """
        if not self.is_trained:
            raise RuntimeError("Model must be trained before prediction")
        
        return self.slope * features + self.intercept


class RidgeRegression(BaseModel):
    """
    Ridge regression with L2 regularization.
    
    Another subclass of BaseModel with different implementation.
    
    Attributes:
        alpha: Regularization strength
        coefficients: Learned coefficients
    """
    
    def __init__(self, alpha: float = 1.0) -> None:
        """
        Initialize ridge regression model.
        
        Args:
            alpha: Regularization strength
        """
        super().__init__("Ridge Regression")
        self.alpha = alpha
        self.coefficients = None
    
    def fit(self, features: np.ndarray, targets: np.ndarray) -> None:
        """
        Fit ridge regression using normal equations.
        
        Args:
            features: Training features (can be multidimensional)
            targets: Training targets
        """
        # Add intercept column
        features_with_intercept = np.column_stack([
            np.ones(len(features)), 
            features
        ])
        
        # Ridge regression: (X^T X + αI)^(-1) X^T y
        num_features = features_with_intercept.shape[1]
        identity = np.eye(num_features)
        identity[0, 0] = 0  # Don't regularize intercept
        
        xtx = features_with_intercept.T @ features_with_intercept
        xty = features_with_intercept.T @ targets
        
        self.coefficients = np.linalg.solve(
            xtx + self.alpha * identity, 
            xty
        )
        
        self.is_trained = True
    
    def predict(self, features: np.ndarray) -> np.ndarray:
        """
        Make predictions using ridge regression.
        
        Args:
            features: Input features
        
        Returns:
            Predictions
        """
        if not self.is_trained:
            raise RuntimeError("Model must be trained before prediction")
        
        features_with_intercept = np.column_stack([
            np.ones(len(features)), 
            features
        ])
        
        return features_with_intercept @ self.coefficients


# Demonstrate inheritance
print("Inheritance Demonstration:\n")

# Generate synthetic data
np.random.seed(42)
x_train = np.random.uniform(0, 10, 50)
y_train = 2 * x_train + 5 + np.random.normal(0, 2, 50)

# Create and train models
models = [
    SimpleLinearRegression(),
    RidgeRegression(alpha=0.1)
]

for model in models:
    print(f"Training {model.get_info()}...")
    
    if isinstance(model, SimpleLinearRegression):
        model.fit(x_train, y_train)
        print(f"  Slope: {model.slope:.4f}")
        print(f"  Intercept: {model.intercept:.4f}")
    else:
        model.fit(x_train.reshape(-1, 1), y_train)
        print(f"  Coefficients: {model.coefficients}")
    
    print(f"  Status: {model.get_info()}")
    print()

print("Note: Both models inherit from BaseModel and share common interface.")
```

## Polymorphism

Polymorphism allows different classes to be used through the same interface:

```python exec
id: tutorial-12-object-oriented-programming-6
def evaluate_model(model: BaseModel, test_features: np.ndarray, test_targets: np.ndarray) -> float:
    """
    Evaluate any model that inherits from BaseModel.
    
    This function demonstrates polymorphism: it works with any
    object that has the predict() method, regardless of the
    specific model type.
    
    Args:
        model: Any model inheriting from BaseModel
        test_features: Test features
        test_targets: True test targets
    
    Returns:
        R² score
    """
    print(f"Evaluating {model.get_info()}...")
    
    predictions = model.predict(test_features)
    
    # Calculate R² score
    ss_total = np.sum((test_targets - np.mean(test_targets)) ** 2)
    ss_residual = np.sum((test_targets - predictions) ** 2)
    r_squared = 1 - (ss_residual / ss_total)
    
    print(f"  R² score: {r_squared:.4f}")
    return r_squared


# Generate test data
np.random.seed(42)
x_test = np.random.uniform(0, 10, 20)
y_test = 2 * x_test + 5 + np.random.normal(0, 2, 20)

print("Polymorphism in Action:\n")
print("Testing different models with the same evaluation function:\n")

# The same function works with different model types
simple_model = models[0]  # SimpleLinearRegression
ridge_model = models[1]   # RidgeRegression

evaluate_model(simple_model, x_test, y_test)
print()
evaluate_model(ridge_model, x_test.reshape(-1, 1), y_test)

print("\nKey Concept: The evaluate_model function doesn't need to know")
print("the specific model type - it just calls the predict() method!")
```

## Real-World Application: Machine Learning Pipeline

Let's build a complete ML pipeline using OOP principles:

```python exec
id: tutorial-12-object-oriented-programming-7
class DataSplitter:
    """
    Handles train-test splitting with reproducibility.
    """
    
    def __init__(self, test_size: float = 0.2, random_state: int = 42) -> None:
        """
        Initialize the splitter.
        
        Args:
            test_size: Proportion of data for testing
            random_state: Random seed for reproducibility
        """
        self.test_size = test_size
        self.random_state = random_state
    
    def split(self, features: np.ndarray, targets: np.ndarray) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
        """
        Split data into train and test sets.
        
        Args:
            features: Feature matrix
            targets: Target vector
        
        Returns:
            Tuple of (X_train, X_test, y_train, y_test)
        """
        np.random.seed(self.random_state)
        
        num_samples = len(features)
        indices = np.random.permutation(num_samples)
        
        test_samples = int(num_samples * self.test_size)
        test_indices = indices[:test_samples]
        train_indices = indices[test_samples:]
        
        return (
            features[train_indices],
            features[test_indices],
            targets[train_indices],
            targets[test_indices]
        )


class ModelEvaluator:
    """
    Evaluates model performance with multiple metrics.
    """
    
    @staticmethod
    def calculate_metrics(true_values: np.ndarray, predictions: np.ndarray) -> dict[str, float]:
        """
        Calculate multiple evaluation metrics.
        
        Args:
            true_values: True target values
            predictions: Model predictions
        
        Returns:
            Dictionary of metrics
        """
        residuals = true_values - predictions
        
        # Mean Squared Error
        mse = np.mean(residuals ** 2)
        
        # Root Mean Squared Error
        rmse = np.sqrt(mse)
        
        # Mean Absolute Error
        mae = np.mean(np.abs(residuals))
        
        # R² Score
        ss_total = np.sum((true_values - np.mean(true_values)) ** 2)
        ss_residual = np.sum(residuals ** 2)
        r_squared = 1 - (ss_residual / ss_total)
        
        return {
            'MSE': mse,
            'RMSE': rmse,
            'MAE': mae,
            'R²': r_squared
        }


class MLPipeline:
    """
    Complete machine learning pipeline.
    
    Orchestrates data splitting, model training, and evaluation.
    """
    
    def __init__(self, model: BaseModel, test_size: float = 0.2) -> None:
        """
        Initialize the pipeline.
        
        Args:
            model: Model to train and evaluate
            test_size: Proportion of data for testing
        """
        self.model = model
        self.splitter = DataSplitter(test_size=test_size)
        self.evaluator = ModelEvaluator()
        self.metrics = None
    
    def run(self, features: np.ndarray, targets: np.ndarray) -> dict[str, float]:
        """
        Run the complete pipeline.
        
        Args:
            features: Feature matrix
            targets: Target vector
        
        Returns:
            Dictionary of evaluation metrics
        """
        print(f"Running pipeline with {self.model.get_info()}\n")
        
        # Step 1: Split data
        print("Step 1: Splitting data...")
        x_train, x_test, y_train, y_test = self.splitter.split(features, targets)
        print(f"  Training samples: {len(x_train)}")
        print(f"  Testing samples: {len(x_test)}")
        print()
        
        # Step 2: Train model
        print("Step 2: Training model...")
        self.model.fit(x_train, y_train)
        print(f"  Status: {self.model.get_info()}")
        print()
        
        # Step 3: Make predictions
        print("Step 3: Making predictions...")
        predictions = self.model.predict(x_test)
        print(f"  Generated {len(predictions)} predictions")
        print()
        
        # Step 4: Evaluate
        print("Step 4: Evaluating performance...")
        self.metrics = self.evaluator.calculate_metrics(y_test, predictions)
        
        for metric_name, metric_value in self.metrics.items():
            print(f"  {metric_name}: {metric_value:.4f}")
        
        return self.metrics


# Demonstrate the complete pipeline
print("Complete ML Pipeline Demonstration\n")
print("=" * 50)
print()

# Generate synthetic dataset
np.random.seed(42)
num_samples = 200
x_data = np.random.uniform(0, 10, num_samples)
y_data = 3 * x_data + 7 + np.random.normal(0, 3, num_samples)

# Create and run pipeline
model = SimpleLinearRegression()
pipeline = MLPipeline(model=model, test_size=0.2)
results = pipeline.run(x_data, y_data)

print()
print("=" * 50)
print("\nPipeline complete! All components worked together using OOP principles.")
```

## Practice Exercises

### Your turn 1: Create a Scaler Class

Implement a StandardScaler class for data normalization:

```python exec
id: tutorial-12-object-oriented-programming-8
class StandardScaler:
    """
    Standardize features by removing mean and scaling to unit variance.
    
    TODO: Implement this class with:
    - __init__: Initialize with empty mean and std attributes
    - fit: Calculate and store mean and std from training data
    - transform: Apply standardization using stored parameters
    - fit_transform: Convenience method combining fit and transform
    
    Attributes:
        mean_: Mean of training data (set by fit)
        std_: Standard deviation of training data (set by fit)
    """
    
    def __init__(self) -> None:
        # TODO: Initialize attributes
        pass
    
    def fit(self, data: np.ndarray) -> 'StandardScaler':
        # TODO: Calculate and store mean and std
        pass
    
    def transform(self, data: np.ndarray) -> np.ndarray:
        # TODO: Apply standardization
        pass
    
    def fit_transform(self, data: np.ndarray) -> np.ndarray:
        # TODO: Fit and transform in one step
        pass


# Test your implementation
test_data = np.array([1, 2, 3, 4, 5])
scaler = StandardScaler()
scaled_data = scaler.fit_transform(test_data)

print(f"Original: {test_data}")
print(f"Scaled: {scaled_data}")
print(f"Mean: {np.mean(scaled_data):.6f} (should be ≈0)")
print(f"Std: {np.std(scaled_data):.6f} (should be ≈1)")
```

### Your turn 2: Implement K-Nearest Neighbors

Create a KNN classifier inheriting from BaseModel:

```python exec
id: tutorial-12-object-oriented-programming-9
class KNNClassifier(BaseModel):
    """
    K-Nearest Neighbors classifier.
    
    TODO: Implement this class with:
    - __init__: Set k (number of neighbors)
    - fit: Store training data
    - predict: Find k nearest neighbors and return majority class
    - _calculate_distances: Helper method to compute Euclidean distances
    
    Attributes:
        k: Number of neighbors to consider
        X_train: Stored training features
        y_train: Stored training labels
    """
    
    def __init__(self, k: int = 3) -> None:
        # TODO: Initialize
        pass
    
    def fit(self, features: np.ndarray, targets: np.ndarray) -> None:
        # TODO: Store training data
        pass
    
    def _calculate_distances(self, test_point: np.ndarray) -> np.ndarray:
        # TODO: Calculate Euclidean distances to all training points
        pass
    
    def predict(self, features: np.ndarray) -> np.ndarray:
        # TODO: Implement KNN prediction
        # Hint: Use _calculate_distances, np.argsort, and np.bincount
        pass


# Test data (simple 2D classification)
X_train = np.array([[1, 2], [2, 3], [3, 1], [6, 5], [7, 7], [8, 6]])
y_train = np.array([0, 0, 0, 1, 1, 1])  # Two classes

knn = KNNClassifier(k=3)
knn.fit(X_train, y_train)

# Test predictions
X_test = np.array([[2, 2], [7, 6]])
predictions = knn.predict(X_test)
print(f"Predictions: {predictions}")
print("Expected: [0 1] (first point near class 0, second near class 1)")
```

## Summary and Key Takeaways

### Core OOP Concepts

1. **Classes and Objects**
   - Classes are blueprints, objects are instances
   - `__init__` method initializes objects
   - `self` refers to the instance

2. **Encapsulation**
   - Bundle data with methods that operate on it
   - Use underscore prefix for "private" attributes
   - Provide public methods for controlled access

3. **Method Types**
   - Instance methods: Operate on instance data (use `self`)
   - Class methods: Operate on class data (use `@classmethod`, receive `cls`)
   - Static methods: Utility functions (use `@staticmethod`, no special first arg)

4. **Inheritance**
   - Create new classes based on existing ones
   - Use `super()` to call parent class methods
   - Override methods to customize behavior

5. **Polymorphism**
   - Different classes can be used through same interface
   - Write code that works with any object implementing required methods
   - Promotes flexibility and extensibility

### Benefits in Machine Learning

OOP is essential for modern ML frameworks:

- **Scikit-learn**: All models follow the `fit/predict` interface
- **PyTorch/TensorFlow**: Neural networks as class hierarchies
- **Modular pipelines**: Compose preprocessing, training, evaluation
- **Experimentation**: Easy to swap models and compare

### Best Practices

1. **Single Responsibility**: Each class should have one clear purpose
2. **Descriptive Names**: Use clear, meaningful class and method names
3. **Type Hints**: Document expected types for all parameters
4. **Docstrings**: Explain what classes and methods do
5. **Composition over Inheritance**: Prefer building complex objects from simpler ones
6. **Follow PEP 8**: Consistent style makes code more readable

---

## Conclusion

You've now completed this tutorial series covering:

1. **Tutorial A**: Mathematical foundations with `math` and `random` libraries
2. **Tutorial B**: Numerical computing with NumPy
3. **Tutorial C**: Data visualization with Matplotlib
4. **Tutorial D**: Object-oriented programming fundamentals

These skills form the foundation for advanced machine learning work. As you continue your journey:

- Practice building complete projects that integrate all these concepts
- Study open-source ML libraries to see OOP in action
- Focus on writing clean, maintainable, well-documented code
- Remember: Good software engineering practices are as important as algorithmic knowledge

**Next Steps**: Apply these concepts to real projects, explore scikit-learn's source code to see professional OOP design, and consider learning about design patterns for even more sophisticated software architecture.

## Looking back

Before leaving this page, a sentence on each. What you write stays on this device.

```reflect
- Something you expected before running a cell that turned out differently
- The one idea from this page you could explain to someone else now
- Something you would change or try next, if there were time
- A question this page raised for you that it did not answer. Bring it to the next session; these questions are where the next session starts.
```
