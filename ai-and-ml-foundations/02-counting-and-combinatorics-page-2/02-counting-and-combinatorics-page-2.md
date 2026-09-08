---
title: "02-counting-and-combinatorics-page-2 (2 of 2)"
slug: 02-counting-and-combinatorics-page-2
course: ai-and-ml-foundations
course_title: "AI and ML Foundations"
series: 3-probability-and-statistics
series_title: "Probability and Statistics"
version: 2026.09.06.1
---

Before starting this page, run the cell below. It repeats the imports and definitions from the earlier pages that this page uses.

```python exec
id: 02-counting-and-combinatorics-page-2-setup
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
import math
from itertools import permutations, combinations, product

import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
import math
from itertools import permutations, combinations, product

np.random.seed(42)

# Sentence structure: Subject + Verb + Object
subjects = ["the patient", "the doctor", "the nurse"]
verbs = ["examined", "treated", "diagnosed", "helped"]
objects = ["the wound", "the illness", "the condition"]

# Count
num_subjects = len(subjects)
num_verbs = len(verbs)
num_objects = len(objects)

total_sentences = num_subjects * num_verbs * num_objects
print(f"Total sentences: {num_subjects} × {num_verbs} × {num_objects} = {total_sentences}")

# Generate first 10
all_sentences = []
for subj in subjects:
    for verb in verbs:
        for obj in objects:
            all_sentences.append(f"{subj} {verb} {obj}")

print(f"\nFirst 10 sentences:")
for i, sent in enumerate(all_sentences[:10], 1):
    print(f"{i}. {sent}")
print(f"\n... and {len(all_sentences)-10} more")

def factorial(n):
    """Calculate n! recursively."""
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# Display factorials
print("Factorials:")
for n in range(11):
    print(f"{n}! = {factorial(n):,}")

print(f"\n20! = {math.factorial(20):,}")
print("\nFactorials grow faster than exponentials!")

word = "CAT"
letters = list(word)

# Generate all permutations
all_perms = list(permutations(letters))

print(f"Letters: {letters}")
print(f"Number of arrangements: {len(letters)}! = {factorial(len(letters))}")
print(f"\nAll arrangements:")
for i, perm in enumerate(all_perms, 1):
    print(f"{i}. {''.join(perm)}")
```

---

## Part 3: Combinations

### Quick Check 3.1: Permutation vs. Combination

You're choosing 2 toppings from {Pepperoni, Mushroom, Olives}.

For PERMUTATIONS: "Pepperoni then Mushroom" ≠ "Mushroom then Pepperoni"
For COMBINATIONS: Both are just "Pepperoni and Mushroom"

Which applies to pizza toppings? Why?

```python exec
id: 02-counting-and-combinatorics-page-2-1
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
# Your reasoning:
```

### Combinations: Order Doesn't Matter

**Question**: How many ways to choose r objects from n objects?

**Answer**:
$$C(n, r) = \binom{n}{r} = \frac{n!}{r!(n-r)!}$$

Read as: "n choose r"

### Why divide by r!?

Because each selection can be arranged in r! ways, and we don't care about order!

```python exec
id: 02-counting-and-combinatorics-page-2-2
def combination(n, r):
    """Calculate C(n,r)."""
    return factorial(n) // (factorial(r) * factorial(n - r))

# Verify with simple example
letters = ['A', 'B', 'C']
r = 2

all_combos = list(combinations(letters, r))
calculated = combination(len(letters), r)

print(f"Choose {r} from {letters}:")
for combo in all_combos:
    print(f"  {combo}")

print(f"\nCalculated: C({len(letters)}, {r}) = {calculated}")
print(f"Counted: {len(all_combos)}")
```

### Try this 3.1: Medical Test Selection

```python exec
id: 02-counting-and-combinatorics-page-2-3
available_tests = [
    "Blood Glucose", "Cholesterol", "Liver Function", "Kidney Function",
    "Thyroid", "Vitamin D", "Iron", "Calcium"
]

tests_to_order = 3
num_combinations = combination(len(available_tests), tests_to_order)

print(f"C({len(available_tests)}, {tests_to_order}) = {num_combinations}")

# Show first 10
all_combos = list(combinations(available_tests, tests_to_order))
print(f"\nFirst 10 combinations:")
for i, combo in enumerate(all_combos[:10], 1):
    print(f"{i}. {', '.join(combo)}")
print(f"\n... and {len(all_combos)-10} more")
```

### Try this 3.2: Extend the Medical Analysis

Using the same 8 tests:
1. Calculate combinations for selecting 1, 2, 3, 4, 5 tests
2. Plot these as a bar chart
3. Which selection size has the most combinations?
4. Calculate C(8,4) and compare to C(8,4) manually
5. Notice any symmetry? Why does C(n,r) = C(n,n-r)?
6. What's the sum of all possible combinations from selecting 0 to 8 tests?

```python exec
id: 02-counting-and-combinatorics-page-2-4
# YOUR CODE HERE
```

### Example 3.1: Feature Selection in ML

```python exec
id: 02-counting-and-combinatorics-page-2-5
total_features = 20
features_to_select = 5

num_models = combination(total_features, features_to_select)

print(f"C({total_features}, {features_to_select}) = {num_models:,}")

# Time estimate
minutes_per_model = 2
total_hours = (num_models * minutes_per_model) / 60
total_days = total_hours / 24

print(f"\nAt {minutes_per_model} minutes per model:")
print(f"Total time: {total_hours:.1f} hours = {total_days:.1f} days")
print(f"\nThis is why smart feature selection matters!")
```

### Try this 3.3: Feature Selection Strategies

You have 30 features and want to find the best subset.

Compare three strategies:
1. **Exhaustive**: Try all subsets of size 1 to 10
2. **Greedy**: Start with 0, add best feature one at a time (30 + 29 + ... + 21)
3. **Random**: Sample 1000 random subsets

For each:
1. Calculate number of models to train
2. Estimate time (1 minute per model)
3. Create a comparison table
4. Which is most practical?
5. What's the trade-off?

```python exec
id: 02-counting-and-combinatorics-page-2-6
# YOUR CODE HERE
```

### Pascal's Triangle

Binomial coefficients form a beautiful pattern!

```python exec
id: 02-counting-and-combinatorics-page-2-7
def generate_pascals_triangle(num_rows):
    triangle = []
    for n in range(num_rows):
        row = [combination(n, r) for r in range(n + 1)]
        triangle.append(row)
    return triangle

triangle = generate_pascals_triangle(10)

print("Pascal's Triangle:")
for n, row in enumerate(triangle):
    spacing = ' ' * (10 - n) * 2
    row_str = '  '.join(f"{val:3d}" for val in row)
    print(f"{spacing}{row_str}")

print(f"\nRow 5: {triangle[5]}")
print("These are C(5,0), C(5,1), C(5,2), C(5,3), C(5,4), C(5,5)")
```

### Try this 3.4: Explore Pascal's Triangle

1. Generate Pascal's triangle up to row 15
2. Calculate the sum of each row
3. What pattern do you notice in the row sums?
4. Find the maximum value in each row - where is it?
5. Color code a visualization: even vs odd numbers
6. Research: What's the connection to binomial expansion?

```python exec
id: 02-counting-and-combinatorics-page-2-8
# YOUR CODE HERE
```

---

## Part 4: Applications to Probability

### Recall

$$P(E) = \frac{\text{favorable outcomes}}{\text{total outcomes}}$$

Counting helps us calculate both numerator and denominator!

### Example 4.1: Poker Hands

```python exec
id: 02-counting-and-combinatorics-page-2-9
# Total 5-card hands from 52 cards
total_hands = combination(52, 5)
print(f"Total 5-card hands: C(52, 5) = {total_hands:,}")

# Hands with exactly 3 aces
# Choose 3 aces from 4: C(4, 3)
# Choose 2 non-aces from 48: C(48, 2)
ways_3_aces = combination(4, 3)
ways_2_non_aces = combination(48, 2)
hands_with_3_aces = ways_3_aces * ways_2_non_aces

print(f"\nHands with exactly 3 aces:")
print(f"  C(4,3) × C(48,2) = {ways_3_aces} × {ways_2_non_aces} = {hands_with_3_aces:,}")

# Probability
prob = hands_with_3_aces / total_hands
print(f"\nP(exactly 3 aces) = {prob:.6f}")
print(f"About 1 in {int(1/prob):,}")
```

### Try this 4.1: More Poker Probabilities

Calculate the probability of:
1. Exactly 2 aces
2. At least 1 ace
3. All 5 cards the same suit (flush)
4. No face cards (J, Q, K)
5. Exactly 3 cards of one rank (three of a kind)

For each:
- Show the counting calculation
- Calculate the probability
- Express as "1 in X"
- Verify with simulation (deal 100,000 random hands)

```python exec
id: 02-counting-and-combinatorics-page-2-10
# YOUR CODE HERE
```

### Example 4.2: Birthday Paradox

In a room of 23 people, what's P(at least 2 share a birthday)?

```python exec
id: 02-counting-and-combinatorics-page-2-11
def prob_all_different_birthdays(n_people):
    """P(all n people have different birthdays)."""
    if n_people > 365:
        return 0.0

    prob = 1.0
    for i in range(n_people):
        prob *= (365 - i) / 365
    return prob

def prob_at_least_two_same(n_people):
    return 1 - prob_all_different_birthdays(n_people)

n = 23
prob = prob_at_least_two_same(n)
print(f"With {n} people:")
print(f"P(at least 2 share birthday) = {prob:.4f}")
print(f"\nOver 50% chance!")
```

### Try this 4.2: Birthday Paradox Analysis

1. Calculate probability for group sizes 1 to 100
2. Plot probability vs. group size
3. Find the group size where probability first exceeds:
   - 25%
   - 50%
   - 75%
   - 99%
4. Simulate with 10,000 trials to verify
5. What if there are only 30 possible birthdays instead of 365?
6. Create an interactive visualization

```python exec
id: 02-counting-and-combinatorics-page-2-12
# YOUR CODE HERE
```

---

## Part 5: Applications to NLP

### Example 5.1: N-gram Explosion

```python exec
id: 02-counting-and-combinatorics-page-2-13
def ngram_space(vocab_size, n):
    return vocab_size ** n

vocab_sizes = {
    'Small': 1000,
    'Medium': 10000,
    'Large': 50000
}

n_values = [1, 2, 3, 4, 5]

print("N-gram space sizes:\n")
for name, vocab in vocab_sizes.items():
    print(f"{name} vocabulary ({vocab:,} words):")
    for n in n_values:
        size = ngram_space(vocab, n)
        print(f"  {n}-grams: {size:.2e}")
    print()
```

### Try this 5.1: Text Generation Complexity

You're building a text generator with:
- Vocabulary: 5000 words
- Model: Predicts next word given previous 2 words (trigrams)

Questions:
1. How many possible trigrams exist?
2. If you store each as a 64-bit integer, how much memory?
3. If you only see 100 million trigrams in training, what fraction of all possible trigrams is that?
4. How does this change with 4-grams? 5-grams?
5. Why do modern language models use neural networks instead of counting?
6. Calculate the same for a 50,000-word vocabulary

```python exec
id: 02-counting-and-combinatorics-page-2-14
# YOUR CODE HERE
```

### Try this 5.2: Vocabulary Size vs Model Complexity

Compare different vocabulary sizes:
1. Calculate 5-gram spaces for vocabularies of 1K, 5K, 10K, 50K
2. Plot on log scale
3. Calculate percentage of space that could be seen with 1B training examples
4. Why do large language models need massive datasets?
5. Research: How do subword tokenizers (BPE, WordPiece) help?

```python exec
id: 02-counting-and-combinatorics-page-2-15
# YOUR CODE HERE
```

---

## Final Project: Combinatorial Analysis System

### Project Goals

Build a comprehensive system that analyzes combinatorial complexity across multiple domains.

### Requirements

**Part A: Image Pattern Analysis**
1. Calculate pattern spaces for various image sizes and bit depths
2. Estimate storage requirements
3. Determine feasible sizes for exhaustive search
4. Visualize the explosion of possibilities

**Part B: NLP Complexity**
1. Analyze n-gram spaces for different vocabulary sizes
2. Calculate sampling rates from corpora
3. Compare different tokenization strategies
4. Estimate memory requirements

**Part C: Medical Decision Trees**
1. Model diagnostic pathways with branching decisions
2. Calculate total possible diagnostic paths
3. Optimize decision tree depth vs coverage
4. Analyze combinatorial explosion in medicine

**Part D: Password Security**
1. Compare password policies quantitatively
2. Calculate crack times under various attacks
3. Recommend optimal policies
4. Visualize security vs usability trade-offs

**Part E: Synthesis**
1. Create unified dashboard comparing all analyses
2. Identify common patterns in combinatorial growth
3. Discuss implications for AI/ML
4. Propose strategies for managing complexity

### Bonus Challenges
- Implement dynamic programming for some calculations
- Compare recursive vs iterative implementations
- Analyze time complexity of your counting functions
- Create interactive visualizations

```python exec
id: 02-counting-and-combinatorics-page-2-16
# YOUR PROJECT CODE HERE
```

---

## Summary and Reflection

### Key Concepts

**Counting Principles:**
- Multiplication: Independent choices multiply
- Addition: Mutually exclusive choices add
- Factorials: n! grows extremely fast

**Arrangements:**
- Permutations: Order matters, P(n,r) = n!/(n-r)!
- Combinations: Order doesn't matter, C(n,r) = n!/[r!(n-r)!]

**Applications:**
- Probability calculations (poker, birthday paradox)
- NLP (n-gram spaces, vocabulary)
- Images (pattern spaces, compression)
- Security (password strength)
- ML (feature selection, model search)

### Reflection Questions

**Conceptual:**
1. Why does order matter in some situations but not others?
2. How does combinatorial explosion limit brute-force approaches?
3. What strategies exist for managing huge search spaces?

**Practical:**
1. When should you enumerate all possibilities vs. sample?
2. How do you decide between permutations and combinations?
3. What role does counting play in algorithm design?

**Connections:**
1. How do these concepts connect to probability?
2. Where do you see combinatorics in machine learning?
3. What real-world problems face combinatorial complexity?

### Looking Ahead

In Notebook 3:
- Discrete probability distributions
- Bernoulli, Binomial, Geometric, Poisson
- Expected value and variance
- Monte Carlo simulation

### Final Thought

Combinatorics reveals a fundamental challenge in AI: the space of possibilities grows faster than our ability to explore it. Understanding this growth is crucial for designing efficient algorithms, estimating computational costs, and knowing when approximation is necessary.

The birthday paradox shows how our intuition fails with combinatorics. The n-gram explosion shows why neural networks beat counting. The password analysis shows how mathematics informs security.

Master counting, and you'll understand why some AI problems are easy and others are impossibly hard.

## Looking back

Before leaving this page, a sentence on each. What you write stays on this device.

```reflect
- Something you expected before running a cell that turned out differently
- The one idea from this page you could explain to someone else now
- Something you would change or try next, if there were time
- A question this page raised for you that it did not answer. Bring it to the next session; these questions are where the next session starts.
```
