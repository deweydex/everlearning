---
title: "Binomial Coefficient: Recursive vs Memoized"
slug: binomial-coefficient-recursive-vs-memoised
course: ai-and-ml-foundations
course_title: "AI and ML Foundations"
series: 3-probability-and-statistics-enrichment
series_title: "Probability and Statistics / Enrichment"
version: 2026.09.06.1
---

# Binomial Coefficient: Recursive vs Memoized

This notebook compares the performance of two approaches to calculating binomial coefficients:
1. Naive recursive approach (exponential time)
2. Memoized approach (polynomial time)

We'll count the number of function calls required by each algorithm and visualize the difference.

```python exec
id: binomial-coefficient-recursive-vs-memoised-1
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from IPython.display import display

# For cleaner plots
plt.style.use('ggplot')
```

## Implementation of Both Algorithms

First, let's implement both algorithms with step counting.

```python exec
id: binomial-coefficient-recursive-vs-memoised-2
def binomial_coefficient_recursive(n, k, steps=None, call_index=0) -> int:
    """
    Calculate binomial coefficient C(n,k) using naive recursion.

    Args:
        n, k: Parameters for C(n,k)
        steps: List to track function calls (recursive and memoized)
        call_index: Index in steps list for this algorithm (0 for recursive)

    Returns:
        The binomial coefficient C(n,k)
    """
    if steps is None:
        steps = [0, 0]

    # Count this function call
    steps[call_index] += 1

    # Base cases
    if k == 0 or k == n:
        return 1

    # Recursive case: C(n,k) = C(n-1,k-1) + C(n-1,k)
    left = binomial_coefficient_recursive(n-1, k-1, steps, call_index)
    right = binomial_coefficient_recursive(n-1, k, steps, call_index)

    return left + right
```

```python exec
id: binomial-coefficient-recursive-vs-memoised-3
def binomial_coefficient_memoized(n, k, steps=None, call_index=1, memo=None):
    """
    Calculate binomial coefficient C(n,k) using memoization.

    Args:
        n, k: Parameters for C(n,k)
        steps: List to track function calls (recursive and memoized)
        call_index: Index in steps list for this algorithm (1 for memoized)
        memo: Dictionary for memoization

    Returns:
        The binomial coefficient C(n,k)
    """
    if steps is None:
        steps = [0, 0]
    if memo is None:
        memo = {}

    # Count this function call
    steps[call_index] += 1

    # Check if we've already computed this value
    if (n, k) in memo:
        return memo[(n, k)]

    # Base cases
    if k == 0 or k == n:
        memo[(n, k)] = 1
        return 1

    # Recursive case with memoization
    left = binomial_coefficient_memoized(n-1, k-1, steps, call_index, memo)
    right = binomial_coefficient_memoized(n-1, k, steps, call_index, memo)
    memo[(n, k)] = left + right

    return memo[(n, k)]
```

```python exec
id: binomial-coefficient-recursive-vs-memoised-4
def binomial_coefficient_iterative(n, k, steps = None, call_index = 2):
    """
    Calculate binomial coefficient C(n,k) using iterative approach.

    Args:
        n, k: Parameters for C(n,k)

    Returns:
        The binomial coefficient C(n,k)
    """
    if k < 0 or k > n:
        return 0
    if k == 0 or k == n:
        return 1
    if k > n // 2:
        k = n - k

    c = 1

    c = 1
    for k in range(1,n+1):# because we start with our 1, and include our max n
        c = c * (n+1- k) / (k* (n-k+1))
    return c
```

```python exec
id: binomial-coefficient-recursive-vs-memoised-5
binomial_coefficient_iterative(5,2)
```

## Collecting Performance Data

Let's collect data for various values of n (with k = n/2, which is typically the worst case).

```python exec
id: binomial-coefficient-recursive-vs-memoised-6
def collect_comparison_data(max_n=15):
    """
    Collect performance data for both algorithms for various input sizes.

    Args:
        max_n: Maximum value of n to test

    Returns:
        DataFrame with performance data
    """
    data = []

    for n in range(1, max_n + 1):
        k = n // 2  # Use n/2 as k (worst case)

        # Steps counters
        steps = [0, 0]  # [recursive_steps, memoized_steps]

        # Run both algorithms
        result_recursive = binomial_coefficient_recursive(n, k, steps, 0)
        result_memoized = binomial_coefficient_memoized(n, k, steps, 1)

        # Save results
        data.append({
            'n': n,
            'k': k,
            'result': result_recursive,  # Same for both algorithms
            'recursive_steps': steps[0],
            'memoized_steps': steps[1],
            'speedup_factor': steps[0] / steps[1] if steps[1] > 0 else float('inf')
        })

    return pd.DataFrame(data)
```

```python exec
id: binomial-coefficient-recursive-vs-memoised-7
# Generate the comparison data
comparison_df = collect_comparison_data(25)
display(comparison_df)
```

## Visualizing the Results

Let's create visualizations to better understand the performance difference.

```python exec
id: binomial-coefficient-recursive-vs-memoised-8
def plot_step_comparison(df):
    """
    Create a line plot comparing function calls for both algorithms.
    """
    plt.figure(figsize=(10, 10))

    # Plot both algorithms
    plt.plot(df['n'], df['recursive_steps'], 'o-', color='#E24A33', linewidth=2, markersize=8, label='Recursive (O(2^n))')
    plt.plot(df['n'], df['memoized_steps'], 'o-', color='#348ABD', linewidth=2, markersize=8, label='Memoized (O(n×k))')

    # Add labels and title
    plt.xlabel('Input Size (n)', fontsize=12)
    plt.ylabel('Function Calls', fontsize=12)
    plt.title('Binomial Coefficient: Recursive vs Memoized', fontsize=14)
    plt.grid(True, alpha=0.3)
    plt.legend(fontsize=12)

    # Use log scale for y-axis due to exponential growth
    plt.yscale('log')

    plt.tight_layout()
    plt.show()

def plot_speedup_factor(df):
    """
    Create a bar chart showing the speedup factor (recursive steps / memoized steps).
    """
    plt.figure(figsize=(10, 10))

    # Plot speedup factor
    plt.bar(df['n'], df['speedup_factor'], color='#30A2DA', alpha=0.7)

    # Add labels and title
    plt.xlabel('Input Size (n)', fontsize=12)
    plt.ylabel('Speedup Factor (log scale)', fontsize=12)
    plt.title('Memoization Speedup Factor for Binomial Coefficient', fontsize=14)
    plt.grid(True, alpha=0.3, axis='y')

    # Use log scale for y-axis due to exponential growth
    plt.yscale('log')

    # Add data labels
    for i, val in enumerate(df['speedup_factor']):
        if val < 1000:  # Only show labels for smaller values to avoid clutter
            plt.text(df['n'][i], val * 1.1, f'{val:.1f}x', ha='center', va='bottom', fontsize=9)

    plt.tight_layout()
    plt.show()
```

```python exec
id: binomial-coefficient-recursive-vs-memoised-9
# Plot the comparison results
plot_step_comparison(comparison_df)
plot_speedup_factor(comparison_df)
```

## Linear vs. Log Scale Comparison

Let's also visualize this with a linear scale to emphasize the dramatic difference.

```python exec
id: binomial-coefficient-recursive-vs-memoised-10
def plot_linear_comparison(df):
    """
    Create a line plot with linear scale for direct comparison.
    """
    plt.figure(figsize=(12, 6))

    # Plot both algorithms
    plt.plot(df['n'], df['recursive_steps'], 'o-', color='#E24A33', linewidth=2, markersize=8, label='Recursive (O(2^n))')
    plt.plot(df['n'], df['memoized_steps'], 'o-', color='#348ABD', linewidth=2, markersize=8, label='Memoized (O(n×k))')

    # Add labels and title
    plt.xlabel('Input Size (n)', fontsize=12)
    plt.ylabel('Function Calls', fontsize=12)
    plt.title('Binomial Coefficient: Recursive vs Memoized (Linear Scale)', fontsize=14)
    plt.grid(True, alpha=0.3)
    plt.legend(fontsize=12)

    # Highlight the exponential growth
    plt.annotate('Exponential Growth',
                 xy=(df['n'].iloc[-3], df['recursive_steps'].iloc[-3]),
                 xytext=(df['n'].iloc[-6], df['recursive_steps'].iloc[-6] * 0.7),
                 arrowprops=dict(facecolor='black', shrink=0.05, width=1.5, headwidth=8),
                 fontsize=12)

    # Highlight the polynomial growth
    plt.annotate('Polynomial Growth',
                 xy=(df['n'].iloc[-2], df['memoized_steps'].iloc[-2]),
                 xytext=(df['n'].iloc[-6], df['memoized_steps'].iloc[-6] * 1.5),
                 arrowprops=dict(facecolor='black', shrink=0.05, width=1.5, headwidth=8),
                 fontsize=12)

    plt.tight_layout()
    plt.show()
```

```python exec
id: binomial-coefficient-recursive-vs-memoised-11
# Plot with linear scale
plot_linear_comparison(comparison_df)
```

## Theoretical Growth Rate Comparison

Let's visualize the theoretical growth rates for both algorithms.

```python exec
id: binomial-coefficient-recursive-vs-memoised-12
def plot_theoretical_growth(max_n=20):
    """
    Plot theoretical growth rates for both algorithms.
    """
    n_values = np.arange(1, max_n + 1)

    # Calculate theoretical complexities
    exponential_growth = 2**n_values  # O(2^n)
    quadratic_growth = n_values * (n_values / 2)  # O(n*k) where k=n/2

    # Scale to make them comparable
    scale_factor = exponential_growth[10] / quadratic_growth[10]  # Scale at n=10
    scaled_quadratic = quadratic_growth * scale_factor

    plt.figure(figsize=(12, 6))

    # Plot theoretical growth rates
    plt.plot(n_values, exponential_growth, '--', color='#E24A33', linewidth=2, label='O(2^n)')
    plt.plot(n_values, scaled_quadratic, '--', color='#348ABD', linewidth=2, label='O(n²)')

    # Add labels and title
    plt.xlabel('Input Size (n)', fontsize=12)
    plt.ylabel('Number of Operations (scaled)', fontsize=12)
    plt.title('Theoretical Growth Rates Comparison', fontsize=14)
    plt.grid(True, alpha=0.3)
    plt.legend(fontsize=12)

    # Use log scale for y-axis
    plt.yscale('log')

    plt.tight_layout()
    plt.show()
```

```python exec
id: binomial-coefficient-recursive-vs-memoised-13
# Plot theoretical growth rates
plot_theoretical_growth()
```

## Conclusion

This comparison clearly demonstrates how memoization transforms an exponential algorithm into a polynomial one:

1. The naive recursive approach has time complexity O(2^n) due to recalculating the same subproblems repeatedly
2. The memoized approach has time complexity O(n×k), or O(n²) in the worst case where k=n/2
3. For larger inputs (n > 15), the difference becomes astronomical

This pattern applies to many recursive algorithms with overlapping subproblems, such as Fibonacci numbers, Longest Common Subsequence, and more.

```python exec
id: binomial-coefficient-recursive-vs-memoised-14
def fastfib(n):
    # we want to remember the fibonnaci numbers we learned before
    fib_list = []
    fib_1 = 1
    fib_2 = 1
    fib_list.append(fib_1)
    fib_list.append(fib_2)
    for i in range(1, n):
        fib_list.append(fib_list[i-1] + fib_list[i])
        print(fib_list)
        # fib_i = fib_{i - 1} + fib_{i - 2}
    return fib_list[-1]

print(fastfib(10))

slow_fib = lambda n: 1 if n <= 2 else slow_fib(n - 1) + slow_fib(n - 2)
print(slow_fib(11))
```

## Looking back

Before leaving this page, a sentence on each. What you write stays on this device.

```reflect
- Something you expected before running a cell that turned out differently
- The one idea from this page you could explain to someone else now
- Something you would change or try next, if there were time
- A question this page raised for you that it did not answer. Bring it to the next session; these questions are where the next session starts.
```
