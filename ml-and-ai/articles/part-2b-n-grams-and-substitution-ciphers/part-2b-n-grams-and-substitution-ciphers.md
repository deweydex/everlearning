---
title: "Hidden in Plain Sight: Part 2b"
slug: part-2b-n-grams-and-substitution-ciphers
course: ai-and-ml-foundations
course_title: "AI and ML Foundations"
series: 6-projects-hidden-in-plain-sight
series_title: "Projects / Hidden in Plain Sight"
version: 2026.09.06.1
---

# Hidden in Plain Sight: Part 2b
## N-Gram Analysis and Pattern Recognition

## Welcome to Part 2b!

In Part 2a, you learned to break Caesar ciphers using frequency analysis. But Caesar ciphers are weak - only 26 possible keys.

What about **random substitution ciphers** where each letter can be replaced by any other letter? That's 26! (403 septillion) possible keys! Brute force is impossible.

Yet these ciphers CAN be broken using n-gram analysis. Let's learn how!

### What You'll Learn

1. **N-Grams**: Sequences of consecutive letters
2. **Sliding Window Extraction**: How to extract overlapping n-grams (with visual intuition!)
3. **Pattern Persistence**: Why patterns survive substitution
4. **Bigram and Trigram Analysis**: Using letter combinations
5. **Breaking Random Substitution**: Practical cryptanalysis

### Historical Context

During times of oppression, people have used coded messages to share information safely. In the American South during slavery, quilts with specific patterns conveyed messages. During various authoritarian regimes, writers and journalists developed codes to share truth despite censorship.

Understanding how patterns persist through encoding helps us appreciate both the ingenuity of those seeking to communicate freely and the mathematical foundations that make privacy possible.


### Prerequisites

- Parts 1 and 2a completed
- Understanding of frequency analysis and chi-squared
- Patience with complex algorithms

```python exec
id: part-2b-n-grams-and-substitution-ciphers-1
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter

plt.rcParams['figure.figsize'] = (12, 6)
plt.rcParams['font.size'] = 11

print('Libraries loaded!')
print('Ready for n-gram analysis.')
```

---

## Section 1: Understanding N-Grams

### What is an N-Gram?

An **n-gram** is a sequence of N consecutive items from a larger sequence.

- N=1: "unigram" (single letters)
- N=2: "bigram" or "digram" (pairs)
- N=3: "trigram" (triples)
- N=4: "quadgram" (groups of four)

**Examples from "HELLO":**
- Unigrams: H, E, L, L, O
- Bigrams: HE, EL, LL, LO
- Trigrams: HEL, ELL, LLO

**Notice:** We got 3 trigrams from a 5-letter word. Why 3, not 2?

---

## Section 1.5: Visualizing N-Gram Extraction Step-by-Step

*This section is crucial! Understanding the sliding window is key to everything that follows.*

### The Sliding Window Metaphor

Imagine text on paper:
```
H E L L O   W O R L D
```

You have a window showing exactly 3 letters at a time. You slide it along:

**Position 0:** Window at start
```
[H E L] L O   W O R L D
```
You see: "HEL"

**Position 1:** Slide right by ONE letter
```
H [E L L] O   W O R L D
```
You see: "ELL"

**Position 2:** Slide again
```
H E [L L O]   W O R L D
```
You see: "LLO"

This is a **sliding window** - moves ONE position at a time, not three!

### Why Overlapping?

**Non-overlapping (chunking):**
```
"HELLO" → ["HEL", "LO"]
```
Lost information: "ELL" and "LLO" never seen!

**Overlapping (sliding window):**
```
"HELLO" → ["HEL", "ELL", "LLO"]
```
Captures ALL 3-letter sequences!

### Visual ASCII Demonstration

```python exec
id: part-2b-n-grams-and-substitution-ciphers-2
def show_trigram_extraction(text):
    """Visual demonstration of trigram extraction"""
    n = 3
    print(f'Text: "{text}"')
    print(f'Length: {len(text)} characters')
    print(f'Expected trigrams: {len(text) - n + 1}')
    print('\n' + '='*60)
    
    trigrams = []
    for i in range(len(text) - n + 1):
        # Visual indicator
        indicator = ' ' * i + '^' * n
        
        print(f'\nPosition {i}:')
        print(f'  {text}')
        print(f'  {indicator}')
        
        trigram = text[i:i+n]
        trigrams.append(trigram)
        print(f'  Trigram: "{trigram}"')
    
    print('\n' + '='*60)
    print(f'Total extracted: {len(trigrams)} trigrams')
    print(f'Trigrams: {trigrams}')
    return trigrams

# Demonstrate
result = show_trigram_extraction("HELLO")
```

### The Formula

For text of length L, you get:

**(L - N + 1)** n-grams of size N

Example: "HELLO" has length 5
- Trigrams: 5 - 3 + 1 = 3 

### Why the +1?

```
Text: "AB" (length 2)
Bigrams: 2 - 2 = 0 Wrong!
Actually: 2 - 2 + 1 = 1 ("AB")

Text: "ABC" (length 3)
Bigrams: 3 - 2 = 1 Wrong!
Actually: 3 - 2 + 1 = 2 ("AB", "BC")
```

The +1 accounts for the last valid position.

```python exec
id: part-2b-n-grams-and-substitution-ciphers-3
def extract_ngrams(text, n):
    """
    Extract all n-grams from text using sliding window.
    
    Parameters:
    -----------
    text : str
        Text to analyze
    n : int
        Size of n-grams
    
    Returns:
    --------
    list : All n-grams
    """
    # Keep only letters, uppercase
    letters = ''.join(c.upper() for c in text if c.isalpha())
    
    # Extract using sliding window
    ngrams = [letters[i:i+n] for i in range(len(letters) - n + 1)]
    
    return ngrams

# Test with different n values
test_text = "THE QUICK BROWN FOX"

for n in [1, 2, 3, 4]:
    ngrams = extract_ngrams(test_text, n)
    name = ['', 'unigrams', 'bigrams', 'trigrams', 'quadgrams'][n]
    print(f'\n{name.capitalize()} (n={n}): {len(ngrams)} extracted')
    print(f'First 5: {ngrams[:5]}')
```

---

## Section 2: N-Gram Frequencies in English

### Most Common Bigrams

In English, the most common 2-letter combinations are:
- TH: ~3.56%
- HE: ~3.07%
- IN: ~2.43%
- ER: ~2.05%
- AN: ~1.99%

### Most Common Trigrams

- THE: ~3.51%
- AND: ~1.59%
- ING: ~1.16%
- HER: ~0.87%
- HAT: ~0.73%

**These patterns are consistent across English text!**

```python exec
id: part-2b-n-grams-and-substitution-ciphers-4
# Common trigrams in English
COMMON_TRIGRAMS = {
    'THE': 3.51, 'AND': 1.59, 'ING': 1.16, 'HER': 0.87, 'HAT': 0.73,
    'HIS': 0.65, 'THA': 0.64, 'ERE': 0.63, 'FOR': 0.61, 'ENT': 0.61
}

def analyze_trigrams(text):
    """Calculate trigram frequencies"""
    trigrams = extract_ngrams(text, 3)
    total = len(trigrams)
    
    if total == 0:
        return {}
    
    counts = Counter(trigrams)
    frequencies = {tri: (count / total) * 100 for tri, count in counts.items()}
    
    return frequencies

# Analyze sample text
sample = """The theory of evolution through natural selection was developed by Charles Darwin. 
The theory explains how species adapt over time through inherited variations."""

freq = analyze_trigrams(sample)
print('Most common trigrams in sample:')
for tri, pct in sorted(freq.items(), key=lambda x: x[1], reverse=True)[:10]:
    print(f'{tri}: {pct:.2f}%')
```

---

## Section 3: Breaking Random Substitution Ciphers

### The Challenge

Random substitution: each letter → different letter
- Key space: 26! = 403,291,461,126,605,635,584,000,000
- Brute force: IMPOSSIBLE

But **patterns persist**!

If plaintext has "THE" frequently, ciphertext will have some trigram frequently (the encrypted version of THE).

### Strategy

1. Find most common trigrams in ciphertext
2. Guess they correspond to common English trigrams
3. Make partial substitutions
4. Refine based on patterns
5. Iterate until plaintext emerges

This is **heuristic cryptanalysis** - educated guessing!

```python exec
id: part-2b-n-grams-and-substitution-ciphers-5
def create_random_substitution():
    """Create random substitution cipher key"""
    import random
    letters = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    shuffled = letters.copy()
    random.shuffle(shuffled)
    return dict(zip(letters, shuffled))

def apply_substitution(text, key):
    """Apply substitution cipher"""
    result = []
    for char in text:
        if char.isalpha():
            is_upper = char.isupper()
            char_upper = char.upper()
            subst = key.get(char_upper, char_upper)
            result.append(subst if is_upper else subst.lower())
        else:
            result.append(char)
    return ''.join(result)

# Create and test
key = create_random_substitution()
plaintext = "THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG"
ciphertext = apply_substitution(plaintext, key)

print(f'Plaintext:  {plaintext}')
print(f'Ciphertext: {ciphertext}')
print('\nKey (first 10 letters):')
for letter in 'ABCDEFGHIJ':
    print(f'{letter} → {key[letter]}')
```

---

## Summary and Key Takeaways

### What You've Learned

1. **N-Grams**
 - Sequences of N consecutive letters
 - Extracted using sliding window (ONE position at a time)
 - Formula: (L - N + 1) n-grams from text of length L

2. **Sliding Window** (Critical Understanding!)
 - Overlapping extraction captures ALL patterns
 - Non-overlapping (chunking) loses information
 - Visual metaphor: window sliding along text

3. **Pattern Persistence**
 - N-gram patterns survive substitution ciphers
 - Common combinations remain common after encryption
 - Enables statistical attack on "unbreakable" ciphers

4. **Bigram and Trigram Analysis**
 - TH, HE, IN most common bigrams
 - THE, AND, ING most common trigrams
 - Consistent across English text

5. **Breaking Random Substitution**
 - Impossible by brute force
 - Possible using pattern matching
 - Requires longer text for reliability
 - Often produces partial solutions

### Skills Gained

 N-gram extraction with sliding window
 Understanding pattern persistence
 Trigram frequency analysis
 Heuristic cryptanalysis
 Dealing with partial solutions
 Patient, iterative problem solving

### Looking Ahead: Part 3

We've been working with grayscale (1 value per pixel). What if we use **color**?

In **Part 3: RGB Three-Channel Encoding**, we'll:
- Use the RGB color model (3 channels)
- Encode more efficiently
- Create beautiful colorful images
- Connect trigrams to RGB channels!

---

## Exercises

### Your turn 1: Manual Extraction

Extract all bigrams from "PYTHON" by hand. How many should you get? Verify with code.

### Your turn 2: Most Common N-Grams

Write a function to find the top 10 most common n-grams in any text for any n.

### Try this: Pattern Finder

Given a ciphertext encrypted with random substitution, identify which encrypted trigram most likely represents "THE". Use frequency analysis to make an educated guess.

---


You've completed Part 2b! You now understand:
- How to extract n-grams using sliding window (with deep visual intuition!)
- Why patterns persist through substitution
- How to analyze bigrams and trigrams
- How to approach breaking hard ciphers

**The sliding window concept you learned is used in:**
- Natural language processing
- DNA sequence analysis
- Time series analysis
- Pattern matching algorithms

**Next:** Part 3 - RGB Three-Channel Encoding

Ready for color? Let's go!

## Looking back

Before leaving this page, a sentence on each. What you write stays on this device.

```reflect
- Something you expected before running a cell that turned out differently
- The one idea from this page you could explain to someone else now
- Something you would change or try next, if there were time
- A question this page raised for you that it did not answer. Bring it to the next session; these questions are where the next session starts.
```
