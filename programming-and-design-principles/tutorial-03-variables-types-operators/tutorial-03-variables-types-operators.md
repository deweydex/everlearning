---
title: "Tutorial 3: Variables, Data Types & Operators"
slug: tutorial-03-variables-types-operators
course: programming-and-design-principles
course_title: "Programming and Design Principles"
series: tutorials
series_title: "Tutorials"
version: 2026.09.06.1
---

# Tutorial 3: Variables, Data Types & Operators

**Module**: Programming & Design Principles 5N2927  
**Level**: QQI Level 5  
**Theme**: Data Handling for Machine Learning

---

---

## Introduction

Welcome to Tutorial 3! Now that we understand algorithms and problem-solving, let's explore how to work with different types of data in Python. Understanding data types and operators is essential for processing the diverse data you'll encounter in machine learning.

### What You'll Learn

By the end of this tutorial, you'll be able to:
- Create and use variables with proper naming conventions
- Understand and work with different Python data types
- Convert between data types safely
- Apply arithmetic, comparison, and logical operators
- Understand operator precedence rules
- Perform feature engineering operations for ML

## Variables and Naming Conventions

Variables are fundamental to programming - they're containers that store data we want to work with.

### What Are Variables?

A **variable** is a named location in memory that stores a value. Think of it as a labeled box where you can put data and retrieve it later using the label.

### Variable Naming Best Practices

Following these conventions makes your code professional and readable:

**Rules (Python Requirements)**:
- Must start with letter or underscore
- Can contain letters, numbers, underscores
- Cannot contain spaces or special characters
- Case-sensitive (score ≠ Score ≠ SCORE)
- Cannot use Python keywords (if, for, while, etc.)

**Conventions (Professional Standards)**:
- Use snake_case for variable names: `learning_rate`, `batch_size`
- Use descriptive names: `model_accuracy` not `ma` or `acc`
- Avoid single letters except in very limited contexts
- Use verb_noun for boolean variables: `is_trained`, `has_converged`
- Keep names concise but clear: `num_epochs` not `number_of_training_epochs`

Let's see good versus poor naming:

```python exec
id: tutorial-03-variables-types-operators-1
# Examples of Variable Naming

print("=== Variable Naming: Good vs Poor ===")
print()

# POOR: Unclear, abbreviated, single letters
print("POOR Examples:")
n = 1000  # What does 'n' represent?
lr = 0.01  # Is this learning rate? Linear regression?
x = 0.85  # No context whatsoever
print(f"n={n}, lr={lr}, x={x}")
print("^ Hard to understand what these represent!")
print()

# GOOD: Clear, descriptive, follows conventions  
print("GOOD Examples:")
num_training_examples = 1000
learning_rate = 0.01
model_accuracy = 0.85
print(f"Training examples: {num_training_examples}")
print(f"Learning rate: {learning_rate}")
print(f"Model accuracy: {model_accuracy}")
print("^ Immediately clear what each variable represents!")
print()

# EXCELLENT: Descriptive with type hints for functions
def calculate_f1_score(precision: float, recall: float) -> float:
    """
    Calculate F1 score from precision and recall.
    
    Args:
        precision: Precision metric (0-1)
        recall: Recall metric (0-1)
        
    Returns:
        F1 score (harmonic mean of precision and recall)
    """
    if precision + recall == 0:
        return 0.0
    return 2 * (precision * recall) / (precision + recall)

precision_score = 0.85
recall_score = 0.90
f1_score = calculate_f1_score(precision_score, recall_score)
print(f"Precision: {precision_score}")
print(f"Recall: {recall_score}")
print(f"F1 Score: {f1_score:.4f}")
```

### Think About It

**Question**: Why do you think using descriptive variable names like `learning_rate` is considered more important in machine learning code than in some other types of programming?

**Hint**: Think about who reads ML code (data scientists, researchers) and how complex ML concepts can be.

Write your thoughts:

*Your reflection:*

(Double-click to edit)

---

## Data Types in Python

Python has several built-in data types. Understanding them is crucial for processing different kinds of information.

### Numeric Types

**int** (Integer): Whole numbers, positive or negative

```python exec
id: tutorial-03-variables-types-operators-2
# Integer examples in ML context
num_epochs = 100
batch_size = 32
num_layers = 5

print("=== Integer Examples ===")
print(f"Training epochs: {num_epochs}")
print(f"Batch size: {batch_size}")
print(f"Network layers: {num_layers}")
print(f"Type: {type(num_epochs)}")
```

**float** (Floating-point): Numbers with decimal points

```python exec
id: tutorial-03-variables-types-operators-3
# Float examples in ML context
learning_rate = 0.001
dropout_rate = 0.5
model_accuracy = 0.9234

print("=== Float Examples ===")
print(f"Learning rate: {learning_rate}")
print(f"Dropout rate: {dropout_rate}")
print(f"Model accuracy: {model_accuracy:.4f}")
print(f"Type: {type(learning_rate)}")
```

### String Type

**str** (String): Text data, enclosed in quotes

```python exec
id: tutorial-03-variables-types-operators-4
# String examples in ML context
model_name = "ResNet50"
optimizer_type = "Adam"
activation_function = "relu"

print("=== String Examples ===")
print(f"Model: {model_name}")
print(f"Optimizer: {optimizer_type}")
print(f"Activation: {activation_function}")
print(f"Type: {type(model_name)}")

# String operations
dataset_path = "/data/training_set.csv"
print(f"\nDataset: {dataset_path}")
print(f"Filename: {dataset_path.split('/')[-1]}")
```

### Boolean Type

**bool** (Boolean): True or False values, essential for logic

```python exec
id: tutorial-03-variables-types-operators-5
# Boolean examples in ML context
is_trained = False
has_converged = False
use_gpu = True

print("=== Boolean Examples ===")
print(f"Model trained: {is_trained}")
print(f"Training converged: {has_converged}")
print(f"Using GPU: {use_gpu}")
print(f"Type: {type(is_trained)}")

# Boolean in decision-making
if use_gpu:
    print("\nTraining on GPU for faster computation")
else:
    print("\nTraining on CPU")
```

### Collection Types

**list**: Ordered, mutable collection

```python exec
id: tutorial-03-variables-types-operators-6
# List examples in ML context
training_losses = [0.8, 0.6, 0.4, 0.3, 0.25]
layer_sizes = [784, 128, 64, 10]
class_labels = ["cat", "dog", "bird", "fish"]

print("=== List Examples ===")
print(f"Training losses: {training_losses}")
print(f"Layer sizes: {layer_sizes}")
print(f"Classes: {class_labels}")
print(f"First loss: {training_losses[0]}")
print(f"Last loss: {training_losses[-1]}")

# List operations
print(f"\nEpochs trained: {len(training_losses)}")
print(f"Average loss: {sum(training_losses) / len(training_losses):.3f}")
```

**dict** (Dictionary): Key-value pairs for structured data

```python exec
id: tutorial-03-variables-types-operators-7
# Dictionary examples in ML context
model_config = {
    "learning_rate": 0.001,
    "batch_size": 32,
    "num_epochs": 100,
    "optimizer": "Adam"
}

training_metrics = {
    "accuracy": 0.923,
    "precision": 0.915,
    "recall": 0.931,
    "f1_score": 0.923
}

print("=== Dictionary Examples ===")
print("Model Configuration:")
for key, value in model_config.items():
    print(f"  {key}: {value}")

print("\nTraining Metrics:")
for metric, score in training_metrics.items():
    print(f"  {metric}: {score:.3f}")

# Accessing dictionary values
print(f"\nCurrent learning rate: {model_config['learning_rate']}")
```

---

## Type Conversion and Casting

Often, we need to convert data from one type to another. This is called **type conversion** or **casting**.

```python exec
id: tutorial-03-variables-types-operators-8
# Type conversion for ML applications

print("=== Type Conversion Examples ===")
print()

# Example 1: Converting string input to numbers
print("Example 1: User Input Processing")
epochs_input = "100"  # Imagine this came from user input
epochs_number = int(epochs_input)
print(f"String '{epochs_input}' → Integer {epochs_number}")
print()

# Example 2: Converting for calculations
print("Example 2: Accuracy Calculation")
correct_predictions = 85
total_predictions = 100
accuracy = correct_predictions / total_predictions
print(f"Accuracy: {accuracy:.2%}")
print()

# Example 3: Converting to string for display
print("Example 3: Creating Display Messages")
accuracy_value = 0.9234
accuracy_percent = int(accuracy_value * 100)
message = f"Model achieved {accuracy_percent}% accuracy"
print(message)
```

### Safe Type Conversion

Not all conversions are valid - let's handle errors gracefully:

```python exec
id: tutorial-03-variables-types-operators-9
# Demonstrating safe type conversion

def safe_float_conversion(value: str) -> float:
    """
    Safely convert string to float with error handling.
    
    Args:
        value: String to convert
        
    Returns:
        Float value or 0.0 if conversion fails
    """
    try:
        return float(value)
    except ValueError:
        print(f"Warning: Could not convert '{value}' to float, using 0.0")
        return 0.0

# Testing conversion
print("=== Safe Conversion ===")
valid_input = "0.85"
invalid_input = "not_a_number"

result1 = safe_float_conversion(valid_input)
result2 = safe_float_conversion(invalid_input)

print(f"Valid: '{valid_input}' → {result1}")
print(f"Invalid: '{invalid_input}' → {result2}")
```

---

## Arithmetic Operators

Arithmetic operators perform mathematical calculations - essential for ML computations.

### Basic Operators

| Operator | Operation | Example |
|----------|-----------|---------|  
| + | Addition | 5 + 3 = 8 |
| - | Subtraction | 5 - 3 = 2 |
| * | Multiplication | 5 * 3 = 15 |
| / | Division (float) | 5 / 2 = 2.5 |
| // | Floor division | 5 // 2 = 2 |
| % | Modulus | 5 % 2 = 1 |
| ** | Exponentiation | 5 ** 2 = 25 |

```python exec
id: tutorial-03-variables-types-operators-10
# Arithmetic operators in ML calculations

print("=== ML Arithmetic Examples ===")
print()

# Example 1: Calculating number of batches
print("Example 1: Batch Calculation")
total_samples = 1000
batch_size = 32
num_full_batches = total_samples // batch_size
remaining_samples = total_samples % batch_size

print(f"Total samples: {total_samples}")
print(f"Batch size: {batch_size}")
print(f"Full batches: {num_full_batches}")
print(f"Remaining: {remaining_samples}")
print()

# Example 2: Learning rate decay
print("Example 2: Learning Rate Decay")
initial_learning_rate = 0.1
decay_rate = 0.96
epoch = 10

current_learning_rate = initial_learning_rate * (decay_rate ** epoch)
print(f"Initial LR: {initial_learning_rate}")
print(f"After epoch {epoch}: {current_learning_rate:.6f}")
print()

# Example 3: Training progress
print("Example 3: Training Progress")
current_epoch = 47
total_epochs = 100
progress_percentage = (current_epoch / total_epochs) * 100

print(f"Epoch {current_epoch}/{total_epochs}")
print(f"Progress: {progress_percentage:.1f}%")
```

---

## Comparison Operators

Comparison operators test relationships between values and return Boolean results.

| Operator | Meaning | Example |
|----------|---------|---------|  
| == | Equal to | 5 == 5 → True |
| != | Not equal to | 5 != 3 → True |
| < | Less than | 3 < 5 → True |
| > | Greater than | 5 > 3 → True |
| <= | Less than or equal | 5 <= 5 → True |
| >= | Greater than or equal | 5 >= 3 → True |

```python exec
id: tutorial-03-variables-types-operators-11
# Comparison operators in ML validation

def check_convergence(current_loss: float, 
                     previous_loss: float, 
                     tolerance: float) -> bool:
    """
    Check if training has converged.
    
    Args:
        current_loss: Loss in current epoch
        previous_loss: Loss in previous epoch
        tolerance: Minimum improvement threshold
        
    Returns:
        True if loss improvement is below tolerance
    """
    loss_improvement = previous_loss - current_loss
    return loss_improvement < tolerance

# Example usage
print("=== Convergence Checking ===")
prev_loss = 0.245
curr_loss = 0.243
tol = 0.001

converged = check_convergence(curr_loss, prev_loss, tol)
improvement = prev_loss - curr_loss

print(f"Previous loss: {prev_loss}")
print(f"Current loss: {curr_loss}")
print(f"Improvement: {improvement:.4f}")
print(f"Tolerance: {tol}")
print(f"Has converged: {converged}")
```

---

## Logical Operators

Logical operators combine boolean expressions.

| Operator | Meaning | Example |
|----------|---------|---------|  
| and | Both true | True and False → False |
| or | At least one true | True or False → True |
| not | Opposite | not True → False |

```python exec
id: tutorial-03-variables-types-operators-12
# Logical operators in ML decision making

def should_save_model(current_accuracy: float,
                     best_accuracy: float,
                     min_improvement: float,
                     epoch: int,
                     save_frequency: int) -> bool:
    """
    Determine if model should be saved.
    
    Args:
        current_accuracy: Current epoch accuracy
        best_accuracy: Best accuracy so far
        min_improvement: Minimum improvement to save
        epoch: Current epoch number
        save_frequency: How often to save
        
    Returns:
        True if model should be saved
    """
    improved = (current_accuracy - best_accuracy) >= min_improvement
    is_checkpoint = (epoch % save_frequency) == 0
    
    return improved or is_checkpoint

# Test scenarios
print("=== Model Saving Logic ===")
print()

# Scenario 1: Improved accuracy
result1 = should_save_model(0.925, 0.920, 0.001, 47, 10)
print("Scenario 1: Accuracy improved")
print(f"  Should save: {result1}")
print()

# Scenario 2: Checkpoint epoch
result2 = should_save_model(0.918, 0.920, 0.001, 50, 10)
print("Scenario 2: Checkpoint epoch")
print(f"  Should save: {result2}")
```

---

## Operator Precedence

Python evaluates operators in a specific order:

1. Parentheses `()`
2. Exponentiation `**`
3. Multiplication, Division, Modulus `*`, `/`, `//`, `%`
4. Addition, Subtraction `+`, `-`
5. Comparison `<`, `>`, `<=`, `>=`, `==`, `!=`
6. Logical NOT `not`
7. Logical AND `and`
8. Logical OR `or`

**Best practice**: Use parentheses to make your intentions clear!

```python exec
id: tutorial-03-variables-types-operators-13
# Operator precedence examples

print("=== Operator Precedence ===")
print()

# Without parentheses - relies on precedence
result1 = 2 + 3 * 4
print(f"Without parentheses: 2 + 3 * 4 = {result1}")
print("  (Multiplication first, then addition)")
print()

# With parentheses - explicit ordering
result2 = (2 + 3) * 4
print(f"With parentheses: (2 + 3) * 4 = {result2}")
print("  (Addition first, then multiplication)")
print()

# ML example: Weighted score calculation
feature_1 = 0.8
feature_2 = 0.6
weight_1 = 0.7
weight_2 = 0.3

# GOOD: Clear with parentheses
weighted_score = (feature_1 * weight_1) + (feature_2 * weight_2)
print(f"Weighted score: {weighted_score:.3f}")
```

---

## Feature Engineering for ML

Feature engineering uses operators to transform raw data into features that ML models can learn from effectively.

### Min-Max Normalization

Scale features to range [0, 1]:

```python exec
id: tutorial-03-variables-types-operators-14
# Min-Max Normalization Implementation

def normalize_feature(value: float, 
                     min_value: float, 
                     max_value: float) -> float:
    """
    Normalize value to [0, 1] range using min-max scaling.
    
    Args:
        value: Value to normalize
        min_value: Minimum value in dataset
        max_value: Maximum value in dataset
        
    Returns:
        Normalized value between 0 and 1
    """
    if max_value == min_value:
        return 0.0
    return (value - min_value) / (max_value - min_value)

# Example: Normalizing age feature
print("=== Min-Max Normalization ===")
ages = [22, 35, 45, 28, 52, 19, 67, 41]
min_age = min(ages)
max_age = max(ages)

print(f"Original ages: {ages}")
print(f"Range: {min_age} to {max_age}")
print()

normalized_ages = [normalize_feature(age, min_age, max_age) for age in ages]
print("Normalized ages:")
for original, normalized in zip(ages, normalized_ages):
    print(f"  {original:2d} → {normalized:.3f}")
```

### Z-Score Standardization

Transform features to have mean=0 and standard deviation=1:

```python exec
id: tutorial-03-variables-types-operators-15
# Z-Score Standardization Implementation

def calculate_mean(values: list) -> float:
    """Calculate arithmetic mean of values."""
    return sum(values) / len(values)

def calculate_std_dev(values: list, mean: float) -> float:
    """Calculate standard deviation of values."""
    variance = sum((x - mean) ** 2 for x in values) / len(values)
    return variance ** 0.5

def standardize_feature(value: float, 
                       mean: float, 
                       std_dev: float) -> float:
    """
    Standardize value using z-score.
    
    Args:
        value: Value to standardize
        mean: Mean of dataset
        std_dev: Standard deviation of dataset
        
    Returns:
        Standardized value (z-score)
    """
    if std_dev == 0:
        return 0.0
    return (value - mean) / std_dev

# Example: Standardizing test scores
print("=== Z-Score Standardization ===")
scores = [85, 92, 78, 88, 95, 82, 90, 87]
mean_score = calculate_mean(scores)
std_score = calculate_std_dev(scores, mean_score)

print(f"Original scores: {scores}")
print(f"Mean: {mean_score:.2f}")
print(f"Std Dev: {std_score:.2f}")
print()

standardized_scores = [standardize_feature(score, mean_score, std_score) 
                      for score in scores]
print("Standardized scores (z-scores):")
for original, standardized in zip(scores, standardized_scores):
    print(f"  {original:2d} → {standardized:+.3f}")
```

### Think About It

**Question**: When might you choose min-max normalization over z-score standardization, or vice versa? What factors would influence your decision?

Write your thoughts:

*Your reflection:*

(Double-click to edit)

---

## Practice Exercises

### Your turn: Precision and Recall Calculator

**Background**: In classification, precision and recall are key metrics.
- Precision = True Positives / (True Positives + False Positives)
- Recall = True Positives / (True Positives + False Negatives)

**Task**: Implement functions to calculate these metrics.

```python exec
id: tutorial-03-variables-types-operators-16
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
# Foundation Exercise: Classification Metrics

def calculate_precision(true_positives: int, false_positives: int) -> float:
    """
    Calculate precision metric.
    
    Args:
        true_positives: Number of correct positive predictions
        false_positives: Number of incorrect positive predictions
        
    Returns:
        Precision score (0-1)
    """
    # Your code here
    pass

def calculate_recall(true_positives: int, false_negatives: int) -> float:
    """
    Calculate recall metric.
    
    Args:
        true_positives: Number of correct positive predictions
        false_negatives: Number of missed positive cases
        
    Returns:
        Recall score (0-1)
    """
    # Your code here
    pass

# Test your functions
# true_pos = 85
# false_pos = 15
# false_neg = 10
# 
# precision = calculate_precision(true_pos, false_pos)
# recall = calculate_recall(true_pos, false_neg)
# print(f"Precision: {precision:.3f}")
# print(f"Recall: {recall:.3f}")
```

### Your turn: Training/Validation Split

**Task**: Calculate how to split a dataset into training and validation sets.

```python exec
id: tutorial-03-variables-types-operators-17
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
# Practice Exercise: Dataset Splitting

def calculate_split_sizes(total_samples: int, 
                         train_ratio: float) -> tuple:
    """
    Calculate training and validation set sizes.
    
    Args:
        total_samples: Total number of samples
        train_ratio: Fraction for training (e.g., 0.8)
        
    Returns:
        Tuple of (training_size, validation_size)
    """
    # Your code here
    pass

# Test your function
# train_size, val_size = calculate_split_sizes(1000, 0.8)
# print(f"Total: 1000 samples")
# print(f"Training: {train_size}")
# print(f"Validation: {val_size}")
```

### Try this Exercise: Batch Processing Calculator

**Task**: Calculate iteration details for training with batches.

Given:
- Total samples in dataset
- Batch size
- Number of epochs

Calculate:
- Batches per epoch
- Total iterations
- Samples in last batch

```python exec
id: tutorial-03-variables-types-operators-18
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
# Challenge Exercise: Batch Processing

def calculate_training_details(total_samples: int,
                               batch_size: int,
                               num_epochs: int) -> dict:
    """
    Calculate training iteration details.
    
    Args:
        total_samples: Total samples in dataset
        batch_size: Size of each batch
        num_epochs: Number of training epochs
        
    Returns:
        Dictionary with training details
    """
    # Your code here
    pass

# Test your function
# details = calculate_training_details(10000, 32, 50)
# print("Training Details:")
# for key, value in details.items():
#     print(f"  {key}: {value}")
```

---

## Common Mistakes

### Mistake 1: Integer Division When Float Needed

```python exec
id: tutorial-03-variables-types-operators-19
# Demonstrating division issues

print("=== Division Mistakes ===")
print()

correct = 85
total = 100

# BAD: Integer division
wrong_accuracy = correct // total
print(f"BAD: {correct} // {total} = {wrong_accuracy}")
print("  ^ Gives 0, not the accuracy!")
print()

# GOOD: Float division
right_accuracy = correct / total
print(f"GOOD: {correct} / {total} = {right_accuracy}")
print(f"  ^ Correct accuracy: {right_accuracy:.1%}")
```

### Mistake 2: Not Checking for Division by Zero

```python exec
id: tutorial-03-variables-types-operators-20
# Safe division example

def safe_divide(numerator: float, denominator: float) -> float:
    """
    Safely divide two numbers.
    
    Args:
        numerator: Number to divide
        denominator: Number to divide by
        
    Returns:
        Result or 0.0 if denominator is zero
    """
    if denominator == 0:
        print("Warning: Division by zero")
        return 0.0
    return numerator / denominator

print("=== Safe Division ===")
result1 = safe_divide(10, 2)
result2 = safe_divide(10, 0)
print(f"10 / 2 = {result1}")
print(f"10 / 0 = {result2}")
```

### Mistake 3: Using Single-Letter Variables

```python exec
id: tutorial-03-variables-types-operators-21
# Variable naming comparison

# BAD: Unclear
x = 0.01
n = 100
print(f"x={x}, n={n}")
print("^ What do these represent?")
print()

# GOOD: Clear
learning_rate = 0.01
num_epochs = 100
print(f"Learning rate: {learning_rate}")
print(f"Epochs: {num_epochs}")
print("^ Immediately understandable!")
```

---

## Key Takeaways

### Variables and Naming
- Use descriptive, snake_case names
- Follow PEP 8 conventions
- Avoid single-letter names

### Data Types
- **int**: Whole numbers
- **float**: Decimal numbers
- **str**: Text data
- **bool**: True/False values
- **list**: Ordered collections
- **dict**: Key-value pairs

### Type Conversion
- Use `int()`, `float()`, `str()`
- Handle errors gracefully
- Be aware of precision loss

### Operators
- **Arithmetic**: +, -, *, /, //, %, **
- **Comparison**: ==, !=, <, >, <=, >=
- **Logical**: and, or, not
- Understand precedence

### Feature Engineering
- Min-max normalization: Scale to [0, 1]
- Z-score standardization: Mean=0, std=1
- Transform data for better ML performance

---

## Next Steps


### Self-Assessment Checklist

Before moving on, ensure you can:

- [ ] Create variables with proper naming conventions
- [ ] Identify appropriate data types
- [ ] Convert between types safely
- [ ] Use arithmetic operators
- [ ] Apply comparison operators
- [ ] Combine logic with boolean operators
- [ ] Understand operator precedence
- [ ] Normalize and standardize features
- [ ] Calculate ML metrics
- [ ] Handle edge cases

### Reflection Questions

1. Which data type is most useful for ML work? Why?
2. How does proper type handling prevent bugs?
3. Why is feature scaling important?
4. When would you use min-max vs z-score?

**Your Reflections:**

(Double-click to edit)

1. Most useful data type:

2. Type handling and bugs:

3. Importance of feature scaling:

4. Choosing normalization method:

## What we set out to do

These were the aims of this notebook. Now that you have worked through it, they are a check on what happened rather than a promise about it.

This tutorial addresses:
1. **LO 4**: Understand procedural syntax including variables, data types, operators
2. **LO 7**: Develop documented programs for various problems
3. **LO 11**: Follow coding standards for variable naming

---

## Looking back

Before leaving this page, a sentence on each. What you write stays on this device.

```reflect
- Something you expected before running a cell that turned out differently
- The one idea from this page you could explain to someone else now
- Something you would change or try next, if there were time
- A question this page raised for you that it did not answer. Bring it to the next session; these questions are where the next session starts.
```

### What's Coming in Tutorial 4?

In the next tutorial, **Selection Structures & Decision Making**, you'll explore:

- Boolean logic and truth tables
- If statements for decision making
- If-else structures for binary choices
- Elif chains for multiple options
- Nested conditionals for complex logic
- Building decision trees for classification
- Activation function selection
- Hyperparameter validation

You'll learn how to make your programs intelligent by adding decision-making capabilities!

---

## Additional Resources

**Documentation**:
- Python Built-in Types: https://docs.python.org/3/library/stdtypes.html
- Python Operators: https://docs.python.org/3/library/operator.html

**Feature Engineering**:
- scikit-learn preprocessing: https://scikit-learn.org/stable/modules/preprocessing.html

---

**End of Tutorial 3**
