---
title: "Recursive Divide-and-Conquer Algorithms and Big O Notation"
slug: enrichment-recursive-algorithms
course: programming-and-design-principles
course_title: "Programming and Design Principles"
series: practice
series_title: "Practice"
version: 2026.09.06.1
---

# Recursive Divide-and-Conquer Algorithms and Big O Notation

This notebook explores several classic problems that are solved efficiently using recursive divide-and-conquer approaches. For each algorithm, we'll:

1. Understand the problem
2. Develop a recursive solution
3. Analyze the time complexity using Big O notation
4. Implement and test the solution in Python

## 1. Binary Search

### Problem
Given a sorted array of n elements and a target value, determine if the target exists in the array (and return its index).

### Divide-and-Conquer Approach
1. Compare the target with the middle element of the array
2. If they match, we're done
3. If the target is less than the middle element, recursively search the left half
4. If the target is greater than the middle element, recursively search the right half

### Time Complexity Analysis
In each recursive step, we reduce the problem size by half. This gives us the recurrence relation:

$$T(n) = T(\frac{n}{2}) + O(1)$$

Where $T(n)$ is the time required for an input of size $n$, and $O(1)$ represents the constant time needed for the comparison.

To solve this recurrence relation, we can expand it:

$$\begin{align}
T(n) &= T(\frac{n}{2}) + O(1) \\
&= T(\frac{n}{4}) + O(1) + O(1) \\
&= T(\frac{n}{8}) + O(1) + O(1) + O(1) \\
\end{align}$$

After $\log_2 n$ steps, we reach the base case $T(1) = O(1)$. So the total complexity is:

$$T(n) = O(\log n)$$

This is significantly better than the $O(n)$ complexity of linear search!

```python exec
id: enrichment-recursive-algorithms-1
def binary_search_recursive(arr, target, low, high):
    """Recursive binary search implementation"""
    # Base case: element not found
    if low > high:
        return -1

    # Find the middle element
    mid = (low + high) // 2

    # If the middle element is the target, return its index
    if arr[mid] == target:
        return mid

    # If the target is less than the middle element, search the left half
    elif target < arr[mid]:
        return binary_search_recursive(arr, target, low, mid - 1)

    # If the target is greater than the middle element, search the right half
    else:
        return binary_search_recursive(arr, target, mid + 1, high)

def binary_search(arr, target):
    """Wrapper function for recursive binary search"""
    return binary_search_recursive(arr, target, 0, len(arr) - 1)
```

```python exec
id: enrichment-recursive-algorithms-2
# Test the binary search function
sorted_array = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
print(f"Array: {sorted_array}")
print(f"Searching for 7: index {binary_search(sorted_array, 7)}")
print(f"Searching for 10: index {binary_search(sorted_array, 10)}")
```

### Visualization of the Search Space Reduction

Let's visualize how binary search reduces the search space with each recursive call:

```python exec
id: enrichment-recursive-algorithms-3
import numpy as np
import matplotlib.pyplot as plt

def visualize_binary_search(arr, target):
    plt.figure(figsize=(12, 4))

    low, high = 0, len(arr) - 1
    step = 1

    while low <= high:
        mid = (low + high) // 2

        # Visualize the current state
        plt.subplot(1, 3, min(step, 3))
        plt.bar(range(len(arr)), arr, color='lightblue')

        # Highlight the search range
        plt.bar(range(low, high + 1), arr[low:high + 1], color='lightgreen', alpha=0.5)

        # Highlight the middle element
        plt.bar(mid, arr[mid], color='red')

        plt.title(f"Step {step}: mid={mid}, value={arr[mid]}")
        plt.xlabel("Index")
        plt.ylabel("Value")

        # Update the search range for the next step
        if arr[mid] == target:
            plt.suptitle(f"Found {target} at index {mid}", fontsize=16)
            break
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

        step += 1

    if low > high:
        plt.suptitle(f"{target} not found in array", fontsize=16)

    plt.tight_layout(rect=[0, 0, 1, 0.95])
    plt.show()

# Visualize binary search with our example array
visualize_binary_search(sorted_array, 7)
```

## 2. Merge Sort

### Problem
Sort an array of n elements in ascending order.

### Divide-and-Conquer Approach
1. Divide the unsorted array into two halves
2. Recursively sort each half
3. Merge the two sorted halves into a single sorted array

### Time Complexity Analysis
Let's denote the time complexity for sorting an array of size $n$ as $T(n)$.

1. Dividing the array takes constant time: $O(1)$
2. Recursively sorting two halves takes: $2 \times T(\frac{n}{2})$
3. Merging the sorted halves takes linear time: $O(n)$

This gives us the recurrence relation:

$$T(n) = 2T(\frac{n}{2}) + O(n)$$

We can solve this using the Master Theorem or by expanding the recurrence:

$$\begin{align}
T(n) &= 2T(\frac{n}{2}) + cn \\
&= 2[2T(\frac{n}{4}) + c\frac{n}{2}] + cn \\
&= 4T(\frac{n}{4}) + cn + cn \\
&= 4T(\frac{n}{4}) + 2cn \\
\end{align}$$

After $\log_2 n$ steps, we reach $T(1) = O(1)$. At each level $i$ (from 0 to $\log_2 n - 1$), we have $2^i$ subproblems of size $\frac{n}{2^i}$, with each level contributing $cn$ work.

Total complexity: $T(n) = O(n \log n)$

This is more efficient than simple sorting algorithms like bubble sort or insertion sort, which have $O(n^2)$ complexity.

```python exec
id: enrichment-recursive-algorithms-4
def merge_sort(arr):
    """Recursive merge sort implementation"""
    # Base case: arrays of size 0 or 1 are already sorted
    if len(arr) <= 1:
        return arr

    # Divide step: split the array into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Conquer step: recursively sort both halves
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)

    # Combine step: merge the sorted halves
    return merge(left_sorted, right_sorted)

def merge(left, right):
    """Merge two sorted arrays into a single sorted array"""
    result = []
    i = j = 0

    # Compare elements from both arrays and add the smaller one to the result
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Add any remaining elements
    result.extend(left[i:])
    result.extend(right[j:])

    return result
```

```python exec
id: enrichment-recursive-algorithms-5
# Test the merge sort function
unsorted_array = [38, 27, 43, 3, 9, 82, 10]
print(f"Unsorted array: {unsorted_array}")
sorted_array = merge_sort(unsorted_array)
print(f"Sorted array: {sorted_array}")
```

### Visualizing the Recursive Call Tree

Let's visualize the merge sort process for our example array:

```python exec
id: enrichment-recursive-algorithms-6
import networkx as nx
import matplotlib.pyplot as plt

def visualize_merge_sort_tree(arr):
    G = nx.DiGraph()

    def build_tree(arr, node_id='root'):
        # Base case
        if len(arr) <= 1:
            G.add_node(node_id, label=str(arr))
            return

        G.add_node(node_id, label=str(arr))

        # Divide
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Add child nodes
        left_id = f"{node_id}_L"
        right_id = f"{node_id}_R"

        G.add_edge(node_id, left_id)
        G.add_edge(node_id, right_id)

        # Recursive calls
        build_tree(left_half, left_id)
        build_tree(right_half, right_id)

    build_tree(arr)

    plt.figure(figsize=(14, 10))
    pos = nx.nx_agraph.graphviz_layout(G, prog='dot')

    # Draw nodes
    nx.draw(
        G, pos,
        with_labels=False,
        node_size=2000,
        node_color='lightblue',
        arrows=True,
        arrowsize=15,
        width=2
    )

    # Draw labels
    node_labels = nx.get_node_attributes(G, 'label')
    nx.draw_networkx_labels(G, pos, labels=node_labels, font_size=10)

    plt.title("Merge Sort Recursive Call Tree", fontsize=16)
    plt.axis('off')
    plt.show()

# Visualize the merge sort recursion tree for our example array
visualize_merge_sort_tree([38, 27, 43, 3, 9])
```

## 3. Fast Exponentiation

### Problem
Efficiently calculate $x^n$ for an integer $n \geq 0$.

### Naive Approach
The naive approach would multiply $x$ by itself $n$ times, which takes $O(n)$ time.

### Divide-and-Conquer Approach
We can compute $x^n$ more efficiently by using the following properties:
- If $n$ is even: $x^n = (x^{n/2})^2$
- If $n$ is odd: $x^n = x \cdot (x^{(n-1)/2})^2$

### Time Complexity Analysis
Let $T(n)$ be the number of multiplications needed to compute $x^n$.

For even $n$: $T(n) = T(n/2) + 1$ (one multiplication to square the result)
For odd $n$: $T(n) = T((n-1)/2) + 2$ (one multiplication to square, one to multiply by $x$)

Since $n$ is roughly halved in each recursive call, the maximum depth of recursion is $\log_2 n$. In the worst case (if all $n$ are odd), we perform at most $2\log_2 n$ multiplications.

Therefore, the time complexity is $O(\log n)$, which is exponentially better than the naive $O(n)$ approach.

```python exec
id: enrichment-recursive-algorithms-7
def fast_power(x, n):
    """Recursive fast exponentiation using divide-and-conquer"""
    # Base cases
    if n == 0:
        return 1
    if n == 1:
        return x

    # Recursive case for even power
    if n % 2 == 0:
        half_pow = fast_power(x, n // 2)
        return half_pow * half_pow

    # Recursive case for odd power
    else:
        half_pow = fast_power(x, (n - 1) // 2)
        return x * half_pow * half_pow
```

```python exec
id: enrichment-recursive-algorithms-8
# Test the fast power function
base = 2
exponent = 10
print(f"{base}^{exponent} = {fast_power(base, exponent)}")

base = 3
exponent = 7
print(f"{base}^{exponent} = {fast_power(base, exponent)}")
```

### Tracing the Fast Exponentiation Algorithm

Let's trace the execution of fast_power(2, 10) to understand how it works:

1. fast_power(2, 10)
   - n is even, so we calculate fast_power(2, 5)
   
2. fast_power(2, 5)
   - n is odd, so we calculate fast_power(2, 2)
   
3. fast_power(2, 2)
   - n is even, so we calculate fast_power(2, 1)
   
4. fast_power(2, 1)
   - This is a base case, return 2
   
5. Back to fast_power(2, 2)
   - half_pow = 2
   - Return 2 * 2 = 4
   
6. Back to fast_power(2, 5)
   - half_pow = 4
   - Return 2 * 4 * 4 = 32
   
7. Back to fast_power(2, 10)
   - half_pow = 32
   - Return 32 * 32 = 1024

This required only 4 multiplication operations instead of 9 with the naive approach!

## 4. Recursive Combinations

### Problem
Calculate the binomial coefficient $C(n, k)$, which represents the number of ways to choose $k$ items from a set of $n$ distinct items.

### Mathematical Definition
$$C(n, k) = \frac{n!}{k!(n-k)!}$$

### Recursive Approach
We can use the following recursive definition of the binomial coefficient:

$$C(n, k) = C(n-1, k-1) + C(n-1, k)$$

With base cases:
- $C(n, 0) = 1$ for all $n \geq 0$
- $C(n, n) = 1$ for all $n \geq 0$
- $C(n, k) = 0$ for $k > n$

This recursive definition can be derived from Pascal's Triangle, where each entry is the sum of the two entries above it.

### Time Complexity Analysis
The naive recursive implementation has time complexity $O(2^n)$ because each call branches into two recursive calls, creating an exponential number of overlapping subproblems.

With memoization (storing previously computed results), we can reduce the complexity to $O(n \times k)$ since we compute each value of $C(i, j)$ for $0 \leq i \leq n$ and $0 \leq j \leq k$ exactly once.

```python exec
id: enrichment-recursive-algorithms-9
def naive_combination(n, k):
    """Naive recursive implementation of binomial coefficient"""
    # Base cases
    if k == 0 or k == n:
        return 1
    if k > n:
        return 0

    # Recursive case: C(n, k) = C(n-1, k-1) + C(n-1, k)
    return naive_combination(n-1, k-1) + naive_combination(n-1, k)
```

```python exec
id: enrichment-recursive-algorithms-10
# Memoization to improve efficiency
def memoized_combination(n, k, memo=None):
    """Memoized recursive implementation of binomial coefficient"""
    if memo is None:
        memo = {}

    # Check if we've already computed this value
    if (n, k) in memo:
        return memo[(n, k)]

    # Base cases
    if k == 0 or k == n:
        return 1
    if k > n:
        return 0

    # Recursive case with memoization
    memo[(n, k)] = memoized_combination(n-1, k-1, memo) + memoized_combination(n-1, k, memo)
    return memo[(n, k)]
```

```python exec
id: enrichment-recursive-algorithms-11
# Test the combination functions
n, k = 5, 2
print(f"C({n}, {k}) = {naive_combination(n, k)}")
print(f"C({n}, {k}) = {memoized_combination(n, k)}")

n, k = 10, 4
print(f"C({n}, {k}) = {memoized_combination(n, k)}")
```

### Visualizing Pascal's Triangle

Let's visualize Pascal's Triangle to better understand the recursive relation for combinations:

```python exec
id: enrichment-recursive-algorithms-12
def generate_pascals_triangle(n):
    """Generate Pascal's Triangle up to row n"""
    triangle = []
    for i in range(n + 1):
        row = []
        for j in range(i + 1):
            row.append(memoized_combination(i, j))
        triangle.append(row)
    return triangle

def visualize_pascals_triangle(n):
    """Visualize Pascal's Triangle up to row n"""
    triangle = generate_pascals_triangle(n)

    plt.figure(figsize=(12, 8))
    ax = plt.gca()

    # Remove axes
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.set_xticks([])
    ax.set_yticks([])

    max_row_len = len(triangle[-1])
    for i, row in enumerate(triangle):
        # Center the row
        x_positions = np.linspace(max_row_len - len(row), max_row_len + len(row) - 2, len(row))
        y_position = n - i

        for j, val in enumerate(row):
            circle = plt.Circle((x_positions[j], y_position), 0.45, color='lightblue', alpha=0.8, linewidth=1, edgecolor='blue')
            ax.add_patch(circle)
            ax.text(x_positions[j], y_position, str(val), horizontalalignment='center', verticalalignment='center')

            # Draw lines to parent cells (except for the first row)
            if i > 0:
                # Left parent (if it exists)
                if j > 0:
                    ax.plot([x_positions[j], x_positions[j-1]], [y_position, y_position+1], 'k-', alpha=0.4)
                # Right parent (if it exists)
                if j < len(row) - 1:
                    ax.plot([x_positions[j], x_positions[j]], [y_position, y_position+1], 'k-', alpha=0.4)

    plt.title("Pascal's Triangle: Visual Representation of C(n,k)", fontsize=16)
    plt.axis('equal')
    plt.tight_layout()
    plt.show()

# Visualize Pascal's Triangle up to row 6
visualize_pascals_triangle(6)
```

## Comparing Big O Complexities

Let's visualize the growth rates of different time complexities to understand the efficiency of our algorithms:

```python exec
id: enrichment-recursive-algorithms-13
import numpy as np
import matplotlib.pyplot as plt

def plot_time_complexities():
    n = np.arange(1, 100)

    # Define time complexity functions
    constant = np.ones_like(n)  # O(1)
    logarithmic = np.log2(n)    # O(log n)
    linear = n                 # O(n)
    linearithmic = n * np.log2(n)  # O(n log n)
    quadratic = n ** 2         # O(n²)
    exponential = 2 ** np.minimum(n, 30)  # O(2^n), limited to avoid overflow

    plt.figure(figsize=(12, 8))

    plt.plot(n, constant, label='O(1) - Constant', linewidth=2)
    plt.plot(n, logarithmic, label='O(log n) - Logarithmic (Binary Search, Fast Exponentiation)', linewidth=2)
    plt.plot(n, linear, label='O(n) - Linear', linewidth=2)
    plt.plot(n, linearithmic, label='O(n log n) - Linearithmic (Merge Sort)', linewidth=2)
    plt.plot(n, quadratic, label='O(n²) - Quadratic', linewidth=2)
    plt.plot(n[:30], exponential[:30], label='O(2^n) - Exponential (Naive Recursive Combination)', linewidth=2)

    plt.title('Comparison of Time Complexities', fontsize=16)
    plt.xlabel('Input Size (n)', fontsize=14)
    plt.ylabel('Number of Operations', fontsize=14)
    plt.grid(True)
    plt.legend(fontsize=12)
    plt.show()

    # Log scale plot for better visibility of lower complexity functions
    plt.figure(figsize=(12, 8))

    plt.plot(n, constant, label='O(1) - Constant', linewidth=2)
    plt.plot(n, logarithmic, label='O(log n) - Logarithmic (Binary Search, Fast Exponentiation)', linewidth=2)
    plt.plot(n, linear, label='O(n) - Linear', linewidth=2)
    plt.plot(n, linearithmic, label='O(n log n) - Linearithmic (Merge Sort)', linewidth=2)
    plt.plot(n, quadratic, label='O(n²) - Quadratic', linewidth=2)
    plt.plot(n[:30], exponential[:30], label='O(2^n) - Exponential (Naive Recursive Combination)', linewidth=2)

    plt.title('Comparison of Time Complexities (Log Scale)', fontsize=16)
    plt.xlabel('Input Size (n)', fontsize=14)
    plt.ylabel('Number of Operations (log scale)', fontsize=14)
    plt.yscale('log')
    plt.grid(True)
    plt.legend(fontsize=12)
    plt.show()

# Plot time complexity comparisons
plot_time_complexities()
```

## Conclusion

In this notebook, we've explored several classic problems that are efficiently solved using recursive divide-and-conquer approaches:

1. **Binary Search** - $O(\log n)$ time complexity
2. **Merge Sort** - $O(n \log n)$ time complexity
3. **Fast Exponentiation** - $O(\log n)$ time complexity
4. **Combination Calculation** - $O(2^n)$ naive recursive, $O(n \times k)$ with memoization

Key insights about divide-and-conquer algorithms:

1. They break down problems into smaller subproblems of the same type
2. They solve subproblems recursively
3. They combine the solutions to subproblems to solve the original problem
4. They often lead to efficient algorithms with logarithmic or linearithmic time complexity

Understanding Big O notation helps us analyze and compare the efficiency of different algorithms, especially as the input size grows larger.

## Looking back

Before leaving this page, a sentence on each. What you write stays on this device.

```reflect
- Something you expected before running a cell that turned out differently
- The one idea from this page you could explain to someone else now
- Something you would change or try next, if there were time
- A question this page raised for you that it did not answer. Bring it to the next session; these questions are where the next session starts.
```
