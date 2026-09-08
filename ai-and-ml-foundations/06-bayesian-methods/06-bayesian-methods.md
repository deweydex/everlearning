---
title: "Notebook 6: Bayesian Methods & Applications"
slug: 06-bayesian-methods
course: ai-and-ml-foundations
course_title: "AI and ML Foundations"
series: 3-probability-and-statistics
series_title: "Probability and Statistics"
version: 2026.09.06.1
---

# Notebook 6: Bayesian Methods & Applications

## Part 0: Thinking Like a Bayesian

In Notebook 1, you learned conditional probability: P(A|B). Now we flip the question: Given we observed B, what's the probability of A?

### Quick Check 0.1: The Medical Testing Puzzle (Revisited)

Recall from Notebook 1:
- Disease prevalence: 1%
- Test accuracy: 95%
- False positive rate: 5%

You test positive. Before we calculate anything:
- Is it more likely you have the disease or don't?
- Estimate P(Disease | Positive Test)
- What information did you use to make this estimate?

Write your intuition:

```python exec
id: 06-bayesian-methods-1
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
# Your reasoning:
```

### What is Bayesian Thinking?

**Bayesian inference** is about updating beliefs with evidence:
1. Start with **prior** belief (before seeing data)
2. Observe new **evidence**
3. Calculate **posterior** belief (after seeing data)

This is how you actually reason:
- "Based on what I knew before..."
- "...and what I just observed..."
- "...I now believe..."

### What You'll Learn

This notebook covers:
1. **Bayes' Theorem**: The mathematical foundation
2. **Bayesian updating**: Changing beliefs with evidence
3. **Prior, likelihood, posterior**: The three key components
4. **Medical diagnosis**: Interpreting test results correctly
5. **Spam filtering**: Naive Bayes classifier
6. **Image classification**: Bayesian decision rules
7. **A/B testing**: Making decisions under uncertainty

---

## Part 1: Bayes' Theorem

**A question before moving on.** This program makes a judgement about a person. Who chose the threshold, and what happens to the person just on the wrong side of it? What does the program not know about them? What would you want said to them? Write a sentence or two; there is no right answer, and the question is the point.

```python exec
id: 06-bayesian-methods-2
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
from scipy import stats

np.random.seed(42)
```

### The Formula

$$P(A|B) = \frac{P(B|A) \cdot P(A)}{P(B)}$$

In words:
$$\text{Posterior} = \frac{\text{Likelihood} \times \text{Prior}}{\text{Evidence}}$$

Components:
- **P(A)**: Prior - what we believe before observing B
- **P(B|A)**: Likelihood - probability of observing B given A is true
- **P(B)**: Evidence - total probability of observing B
- **P(A|B)**: Posterior - updated belief after observing B

### Example 1.1: Medical Testing (Complete Solution)

```python exec
id: 06-bayesian-methods-3
# Given information
p_disease = 0.01  # Prior: 1% of people have disease
p_positive_given_disease = 0.95  # Likelihood: test is 95% accurate
p_positive_given_healthy = 0.05  # False positive rate: 5%

# Calculate P(Positive) using law of total probability
p_positive = (p_positive_given_disease * p_disease + 
              p_positive_given_healthy * (1 - p_disease))

# Bayes' theorem
p_disease_given_positive = (p_positive_given_disease * p_disease) / p_positive

print("Given:")
print(f"  P(Disease) = {p_disease:.2%}")
print(f"  P(Positive | Disease) = {p_positive_given_disease:.2%}")
print(f"  P(Positive | Healthy) = {p_positive_given_healthy:.2%}")
print(f"\nCalculated:")
print(f"  P(Positive) = {p_positive:.4f}")
print(f"\nResult:")
print(f"  P(Disease | Positive) = {p_disease_given_positive:.4f}")
print(f"\nInterpretation: Only {p_disease_given_positive:.1%} chance of disease!")
print("Even with a positive test, you likely don't have the disease.")
print("\nWhy? The disease is rare, so false positives outnumber true positives.")
```

### Visualizing Bayes' Theorem

```python exec
id: 06-bayesian-methods-4
# Simulate population
population = 10000
diseased = int(population * p_disease)
healthy = population - diseased

# Test results
true_positives = int(diseased * p_positive_given_disease)
false_positives = int(healthy * p_positive_given_healthy)
false_negatives = diseased - true_positives
true_negatives = healthy - false_positives

# Create visualization
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# Pie chart of test results
labels = ['True\nPositive', 'False\nPositive', 'False\nNegative', 'True\nNegative']
sizes = [true_positives, false_positives, false_negatives, true_negatives]
colors = ['darkgreen', 'orange', 'red', 'lightgreen']
explode = (0.1, 0.1, 0, 0)

ax1.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.0f',
        startangle=90, textprops={'fontsize': 11})
ax1.set_title(f'Population of {population:,}', fontsize=14, weight='bold')

# Bar chart showing the key calculation
total_positive = true_positives + false_positives
categories = ['True\nPositive', 'False\nPositive']
values = [true_positives, false_positives]

bars = ax2.bar(categories, values, color=['darkgreen', 'orange'], edgecolor='black')
ax2.set_ylabel('Count', fontsize=12)
ax2.set_title(f'Among {total_positive} Positive Tests', fontsize=14, weight='bold')
ax2.grid(True, alpha=0.3, axis='y')

# Add value labels
for bar in bars:
    height = bar.get_height()
    ax2.text(bar.get_x() + bar.get_width()/2., height,
            f'{int(height)}\n({int(height)/total_positive:.1%})',
            ha='center', va='bottom', fontsize=11, weight='bold')

plt.tight_layout()
plt.show()

print(f"\nOut of {total_positive} positive tests:")
print(f"  True positives: {true_positives} ({true_positives/total_positive:.1%})")
print(f"  False positives: {false_positives} ({false_positives/total_positive:.1%})")
```

### Try this 1.1: Vary Disease Prevalence

Keep test accuracy constant (95% true positive, 5% false positive).

Calculate P(Disease | Positive) for prevalence:
1. 0.1% (very rare)
2. 1% (rare)
3. 5% (uncommon)
4. 10% (common)
5. 50% (very common)

Then:
- Plot prevalence vs posterior probability
- At what prevalence does P(Disease|Positive) exceed 50%?
- Create visualizations for each scenario
- What's the key insight?

```python exec
id: 06-bayesian-methods-5
# YOUR CODE HERE
```

### Try this 1.2: Vary Test Accuracy

Keep prevalence constant at 1%.

Compare different tests:
1. Poor test: 70% sensitive, 20% false positive
2. Good test: 90% sensitive, 10% false positive  
3. Better test: 95% sensitive, 5% false positive
4. Excellent test: 99% sensitive, 1% false positive

For each:
- Calculate P(Disease | Positive)
- Calculate P(Disease | Negative)
- Which matters more: sensitivity or specificity?
- Create comparison table

```python exec
id: 06-bayesian-methods-6
# YOUR CODE HERE
```

---

## Part 2: Bayesian Updating

### Quick Check 2.1: Multiple Tests

After one positive test, P(Disease) = 16%.
You take a second test (same accuracy). It's also positive.

Before calculating:
- Should your belief in having the disease increase?
- By a lot or a little?
- Estimate the new probability

Write your prediction:

```python exec
id: 06-bayesian-methods-7
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
# Your prediction:
```

### Sequential Updating

Key insight: **Today's posterior becomes tomorrow's prior**

After test 1:
- Prior = 1%
- Posterior = 16%

For test 2:
- Prior = 16% (yesterday's posterior!)
- Calculate new posterior

```python exec
id: 06-bayesian-methods-8
def bayesian_update(prior, likelihood_given_true, likelihood_given_false):
    """Update probability using Bayes' theorem."""
    # P(Evidence) = P(Evidence|True)*P(True) + P(Evidence|False)*P(False)
    p_evidence = likelihood_given_true * prior + likelihood_given_false * (1 - prior)
    
    # Bayes' theorem
    posterior = (likelihood_given_true * prior) / p_evidence
    return posterior

# Sequential testing
prior = 0.01
p_pos_if_disease = 0.95
p_pos_if_healthy = 0.05

print("Sequential Testing:")
print(f"Before any tests: P(Disease) = {prior:.4f}")

# Test 1: Positive
posterior_1 = bayesian_update(prior, p_pos_if_disease, p_pos_if_healthy)
print(f"After test 1 (positive): P(Disease) = {posterior_1:.4f}")

# Test 2: Positive (use posterior from test 1 as new prior)
posterior_2 = bayesian_update(posterior_1, p_pos_if_disease, p_pos_if_healthy)
print(f"After test 2 (positive): P(Disease) = {posterior_2:.4f}")

# Test 3: Positive
posterior_3 = bayesian_update(posterior_2, p_pos_if_disease, p_pos_if_healthy)
print(f"After test 3 (positive): P(Disease) = {posterior_3:.4f}")

print(f"\nWith 3 positive tests, probability jumped from 1% to {posterior_3:.1%}!")
```

### Visualizing Sequential Updates

```python exec
id: 06-bayesian-methods-9
# Simulate 10 tests
num_tests = 10
probabilities = [prior]
current_prob = prior

for test in range(num_tests):
    current_prob = bayesian_update(current_prob, p_pos_if_disease, p_pos_if_healthy)
    probabilities.append(current_prob)

# Plot
plt.figure(figsize=(12, 6))
plt.plot(range(num_tests + 1), probabilities, 'bo-', linewidth=2, markersize=8)
plt.axhline(y=0.5, color='r', linestyle='--', label='50% threshold')
plt.xlabel('Number of Positive Tests', fontsize=12)
plt.ylabel('P(Disease | All Tests Positive)', fontsize=12)
plt.title('Bayesian Updating with Sequential Tests', fontsize=14, weight='bold')
plt.grid(True, alpha=0.3)
plt.legend()
plt.ylim(0, 1)
plt.show()

print(f"After {num_tests} positive tests: {probabilities[-1]:.4f}")
print(f"\nEach test provides evidence, updating our belief!")
```

### Try this 2.1: Mixed Test Results

Start with 1% prevalence. Conduct 5 tests with these results:
1. Positive
2. Positive
3. Negative
4. Positive
5. Negative

Tasks:
- Update probability after each test
- Plot the trajectory
- After test 3 (first negative), how much did belief decrease?
- Final probability after all 5 tests?
- Is this evidence for or against disease?

```python exec
id: 06-bayesian-methods-10
# YOUR CODE HERE
```

### Try this 2.2: Competing Hypotheses

Three diseases have similar symptoms:
- Disease A: 5% prevalence
- Disease B: 3% prevalence
- Disease C: 2% prevalence
- Healthy: 90%

Symptom probabilities:
- P(Symptom | A) = 0.8
- P(Symptom | B) = 0.6
- P(Symptom | C) = 0.4
- P(Symptom | Healthy) = 0.1

Patient has the symptom. Calculate:
1. P(A | Symptom)
2. P(B | Symptom)
3. P(C | Symptom)
4. P(Healthy | Symptom)
5. Which is most likely?
6. Visualize posterior probabilities

```python exec
id: 06-bayesian-methods-11
# YOUR CODE HERE
```

---

## Part 3: Naive Bayes Classifier

### Quick Check 3.1: Spam Detection Intuition

An email contains: "FREE", "WINNER", "CLICK"

Before any calculations:
- Is this more likely spam or legitimate?
- What if it also contains "meeting" and "project"?
- How would you combine evidence from multiple words?

Write your approach:

**A question before moving on.** This program makes a judgement about a person. Who chose the threshold, and what happens to the person just on the wrong side of it? What does the program not know about them? What would you want said to them? Write a sentence or two; there is no right answer, and the question is the point.

```python exec
id: 06-bayesian-methods-12
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
# Your reasoning:
```

### Naive Bayes for Text Classification

**Assumption**: Words are independent (hence "naive")

$$P(\text{Spam} | w_1, w_2, ..., w_n) \propto P(\text{Spam}) \prod_{i=1}^{n} P(w_i | \text{Spam})$$

We compare:
- P(Spam) × P(w1|Spam) × P(w2|Spam) × ...
- P(Legit) × P(w1|Legit) × P(w2|Legit) × ...

Choose whichever is larger!

**A question before moving on.** This program makes a judgement about a person. Who chose the threshold, and what happens to the person just on the wrong side of it? What does the program not know about them? What would you want said to them? Write a sentence or two; there is no right answer, and the question is the point.

### Example 3.1: Simple Spam Filter

**A question before moving on.** This program makes a judgement about a person. Who chose the threshold, and what happens to the person just on the wrong side of it? What does the program not know about them? What would you want said to them? Write a sentence or two; there is no right answer, and the question is the point.

```python exec
id: 06-bayesian-methods-13
# Training data: word probabilities
p_spam = 0.3  # Prior: 30% of emails are spam

# Likelihood: P(word | category)
word_probs = {
    'free': {'spam': 0.7, 'legit': 0.05},
    'winner': {'spam': 0.6, 'legit': 0.02},
    'meeting': {'spam': 0.1, 'legit': 0.4},
    'project': {'spam': 0.05, 'legit': 0.3},
    'click': {'spam': 0.5, 'legit': 0.1}
}

def classify_email(words, word_probs, p_spam):
    """Classify email using Naive Bayes."""
    p_legit = 1 - p_spam
    
    # Start with priors
    spam_score = p_spam
    legit_score = p_legit
    
    # Multiply by likelihoods
    for word in words:
        if word in word_probs:
            spam_score *= word_probs[word]['spam']
            legit_score *= word_probs[word]['legit']
    
    # Normalize
    total = spam_score + legit_score
    p_spam_given_words = spam_score / total
    
    return p_spam_given_words, spam_score, legit_score

# Test emails
email1 = ['free', 'winner', 'click']
email2 = ['meeting', 'project']
email3 = ['free', 'meeting']

for i, email in enumerate([email1, email2, email3], 1):
    prob, spam_score, legit_score = classify_email(email, word_probs, p_spam)
    classification = "SPAM" if prob > 0.5 else "LEGIT"
    
    print(f"\nEmail {i}: {email}")
    print(f"  Spam score: {spam_score:.6f}")
    print(f"  Legit score: {legit_score:.6f}")
    print(f"  P(Spam | Words) = {prob:.4f}")
    print(f"  Classification: {classification}")
```

### Try this 3.1: Build a Better Spam Filter

Extend the spam filter:
1. Add 10 more words with probabilities
2. Create 10 test emails (5 spam, 5 legit)
3. Classify each email
4. Calculate accuracy
5. Identify which words are most discriminative
6. Handle words not in training data (smoothing)

**A question before moving on.** This program makes a judgement about a person. Who chose the threshold, and what happens to the person just on the wrong side of it? What does the program not know about them? What would you want said to them? Write a sentence or two; there is no right answer, and the question is the point.

```python exec
id: 06-bayesian-methods-14
# YOUR CODE HERE
```

### Try this 3.2: Sentiment Analysis

Build a sentiment classifier (Positive vs Negative):

Training:

- Negative words: "terrible", "hate", "worst", "awful", "poor"
- Neutral words: "the", "is", "and", "to"

Tasks:
1. Assign probabilities P(word | Positive) and P(word | Negative)
2. Set priors (assume 50-50 positive/negative)
3. Classify 10 test reviews
4. Calculate confidence scores
5. Visualize word importance
6. Test edge cases (mixed sentiment)

```python exec
id: 06-bayesian-methods-15
# YOUR CODE HERE
```

---

## Part 4: Image Classification with Bayes

### Example 4.1: Pixel-Based Classification

```python exec
id: 06-bayesian-methods-16
# Generate training data
# Class A: dark images (mean = 50)
# Class B: bright images (mean = 200)

def generate_image(mean, std, size=(10, 10)):
    img = np.random.normal(mean, std, size)
    return np.clip(img, 0, 255)

# Training set
train_a = [generate_image(50, 15) for _ in range(100)]
train_b = [generate_image(200, 15) for _ in range(100)]

# Calculate statistics
mean_a = np.mean([np.mean(img) for img in train_a])
std_a = np.mean([np.std(img) for img in train_a])
mean_b = np.mean([np.mean(img) for img in train_b])
std_b = np.mean([np.std(img) for img in train_b])

print(f"Class A: mean={mean_a:.1f}, std={std_a:.1f}")
print(f"Class B: mean={mean_b:.1f}, std={std_b:.1f}")

# Classification function
def classify_image(img, mean_a, std_a, mean_b, std_b, prior_a=0.5):
    """Classify image using Naive Bayes with Gaussian likelihood."""
    img_mean = np.mean(img)
    
    # Likelihood using Gaussian
    likelihood_a = stats.norm.pdf(img_mean, mean_a, std_a)
    likelihood_b = stats.norm.pdf(img_mean, mean_b, std_b)
    
    # Posterior (unnormalized)
    posterior_a = prior_a * likelihood_a
    posterior_b = (1 - prior_a) * likelihood_b
    
    # Normalize
    total = posterior_a + posterior_b
    prob_a = posterior_a / total
    
    return prob_a

# Test
test_imgs = [
    generate_image(50, 15),
    generate_image(125, 15),
    generate_image(200, 15)
]

fig, axes = plt.subplots(1, 3, figsize=(15, 4))

for i, img in enumerate(test_imgs):
    prob = classify_image(img, mean_a, std_a, mean_b, std_b)
    classification = "Class A (Dark)" if prob > 0.5 else "Class B (Bright)"
    
    axes[i].imshow(img, cmap='gray', vmin=0, vmax=255)
    axes[i].set_title(f'{classification}\nP(A|img)={prob:.3f}', fontsize=11, weight='bold')
    axes[i].axis('off')

plt.tight_layout()
plt.show()
```

### Try this 4.1: Multi-Class Image Classification

Create a 3-class classifier:
- Dark images: mean 50
- Medium images: mean 128
- Bright images: mean 200

Tasks:
1. Generate 100 training images per class
2. Calculate class statistics
3. Implement 3-way classifier
4. Test on 50 new images
5. Calculate accuracy
6. Create confusion matrix
7. Visualize decision boundaries

```python exec
id: 06-bayesian-methods-17
# YOUR CODE HERE
```

### Try this 4.2: Texture Classification

Classify images by texture:
- Smooth: low standard deviation
- Noisy: high standard deviation

Use both mean AND standard deviation as features:
1. Generate training data with different textures
2. Model P(mean, std | class) as 2D Gaussian
3. Implement Bayesian classifier
4. Test classification
5. Visualize feature space and decision boundary
6. Compare to using only mean

```python exec
id: 06-bayesian-methods-18
# YOUR CODE HERE
```

---

## Part 5: A/B Testing and Decision Making

### Quick Check 5.1: Which Design is Better?

You test two website designs:
- Design A: 15/100 conversions
- Design B: 18/100 conversions

Before any analysis:
- Is B definitely better?
- Could this be random chance?
- How confident should you be?

Write your thoughts:

```python exec
id: 06-bayesian-methods-19
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
# Your reasoning:
```

### Bayesian A/B Testing

Instead of asking "Is there a difference?", ask:
"What's the probability that B is better than A?"

```python exec
id: 06-bayesian-methods-20
# Observed data
n_a, conversions_a = 100, 15
n_b, conversions_b = 100, 18

# Sample from posterior distributions (Beta distributions)
# Beta(α, β) is conjugate prior for Binomial
samples_a = np.random.beta(conversions_a + 1, n_a - conversions_a + 1, 10000)
samples_b = np.random.beta(conversions_b + 1, n_b - conversions_b + 1, 10000)

# Probability that B > A
prob_b_better = np.mean(samples_b > samples_a)

# Visualize
plt.figure(figsize=(12, 6))
plt.hist(samples_a, bins=50, alpha=0.5, label='Design A', density=True, edgecolor='black')
plt.hist(samples_b, bins=50, alpha=0.5, label='Design B', density=True, edgecolor='black')
plt.axvline(np.mean(samples_a), color='blue', linestyle='--', linewidth=2)
plt.axvline(np.mean(samples_b), color='orange', linestyle='--', linewidth=2)
plt.xlabel('Conversion Rate', fontsize=12)
plt.ylabel('Density', fontsize=12)
plt.title(f'Posterior Distributions\nP(B > A) = {prob_b_better:.3f}', fontsize=14, weight='bold')
plt.legend(fontsize=11)
plt.grid(True, alpha=0.3)
plt.show()

print(f"Design A: {conversions_a}/{n_a} = {conversions_a/n_a:.1%}")
print(f"Design B: {conversions_b}/{n_b} = {conversions_b/n_b:.1%}")
print(f"\nProbability B is better: {prob_b_better:.1%}")

if prob_b_better > 0.95:
    print("Strong evidence for B!")
elif prob_b_better > 0.8:
    print("Moderate evidence for B.")
else:
    print("Not enough evidence to decide.")
```

### Try this 5.1: Sequential A/B Testing

Monitor an A/B test over time:
1. Start with 10 users each
2. Add 10 more users every "day" for 10 days
3. Update posterior after each day
4. Plot P(B > A) over time
5. At what day could you make a decision?
6. How does sample size affect confidence?

```python exec
id: 06-bayesian-methods-21
# YOUR CODE HERE
```

### Try this 5.2: Multi-Variant Testing

Test three designs:
- Design A: 15/100
- Design B: 18/100
- Design C: 22/100

Calculate:
1. P(A is best)
2. P(B is best)
3. P(C is best)
4. Expected loss for choosing each
5. Visualize all posteriors
6. Make a recommendation

```python exec
id: 06-bayesian-methods-22
# YOUR CODE HERE
```

---

## Final Project: Intelligent Medical Diagnostic System

### Project Description

Build a comprehensive Bayesian diagnostic system that:
- Updates beliefs with multiple tests
- Classifies medical images
- Analyzes patient text descriptions
- Makes treatment recommendations

### System Components

**Part A: Disease Prior Estimation**
1. Model 5 diseases with different prevalences
2. Account for age, gender, risk factors
3. Calculate initial priors for each patient

**Part B: Multi-Test Integration**
1. Implement 3 different tests (varying accuracy)
2. Update beliefs sequentially
3. Track confidence over time
4. Determine when to stop testing

**Part C: Image-Based Diagnosis**
1. Generate 500 medical scan images (5 classes)
2. Extract features (mean, std, texture)
3. Build Naive Bayes classifier
4. Integrate with test results

**Part D: Symptom Description Analysis**
1. Create vocabulary of symptoms
2. Assign P(symptom | disease) for each
3. Classify patient descriptions
4. Combine with image and test data

**Part E: Decision Making**
1. Calculate expected cost of each treatment
2. Factor in test costs vs. benefit of information
3. Recommend optimal action
4. Quantify uncertainty

**Part F: Visualization Dashboard**
1. Show prior → posterior evolution
2. Display confidence for each disease
3. Visualize feature importance
4. Create interpretable reports

**Part G: Validation**
1. Test on 100 synthetic patients
2. Calculate diagnostic accuracy
3. Analyze failure cases
4. Compare to baseline methods

### Bonus Challenges
- Implement Thompson sampling for adaptive testing
- Add hierarchical Bayesian model for population
- Include treatment response prediction
- Build interactive web interface
- Compare Bayesian vs frequentist approaches

```python exec
id: 06-bayesian-methods-23
# YOUR PROJECT CODE HERE
```

---

## Summary and Reflection

### Key Concepts

**Bayes' Theorem:**
$$P(A|B) = \frac{P(B|A) \cdot P(A)}{P(B)}$$

Components:
- **Prior**: Initial belief
- **Likelihood**: How well data fits hypothesis
- **Posterior**: Updated belief after seeing data
- **Evidence**: Normalization factor

**Key Insights:**
1. Rare events require strong evidence
2. Today's posterior = tomorrow's prior
3. Evidence accumulates multiplicatively
4. Independence assumptions simplify calculation
5. Bayesian methods quantify uncertainty

**Applications:**
- Medical diagnosis (sequential testing)
- Spam filtering (Naive Bayes)
- Image classification (likelihood models)
- A/B testing (decision making)

### Reflection Questions

**Conceptual:**
1. Why does base rate matter so much?
2. When is the "naive" assumption reasonable?
3. How do priors influence conclusions?

**Practical:**
1. When should you gather more evidence?
2. How do you choose priors without data?
3. What makes evidence "strong"?

**Philosophical:**
1. Is probability objective or subjective?
2. How do beliefs change with evidence?
3. Can we ever be 100% certain?

### Connection to AI/ML

Bayesian thinking underlies:
- Naive Bayes classifiers (spam, sentiment)
- Bayesian networks (causal reasoning)
- Gaussian processes (regression)
- Bayesian optimization (hyperparameter tuning)
- Probabilistic programming (uncertainty quantification)

### Final Thought

Bayesian reasoning is how we actually think. When you see dark clouds and grab an umbrella, you're updating P(Rain|Dark Clouds). When you hear your phone buzz and guess it's a text from a friend, you're combining P(Friend) with P(Buzz|Friend Text).

The medical testing paradox shows why intuition fails with rare events. The spam filter shows why context matters. A/B testing shows why we need probabilistic thinking for decisions.

You started this series learning probability foundations. You now understand how to:
- Model uncertainty
- Count possibilities
- Recognize patterns in distributions
- Describe data with statistics
- Update beliefs with evidence

These aren't just mathematical tools. They're ways of thinking clearly about an uncertain world. Use them wisely.

**A question before moving on.** This program makes a judgement about a person. Who chose the threshold, and what happens to the person just on the wrong side of it? What does the program not know about them? What would you want said to them? Write a sentence or two; there is no right answer, and the question is the point.

## Looking back

Before leaving this page, a sentence on each. What you write stays on this device.

```reflect
- Something you expected before running a cell that turned out differently
- The one idea from this page you could explain to someone else now
- Something you would change or try next, if there were time
- A question this page raised for you that it did not answer. Bring it to the next session; these questions are where the next session starts.
```
