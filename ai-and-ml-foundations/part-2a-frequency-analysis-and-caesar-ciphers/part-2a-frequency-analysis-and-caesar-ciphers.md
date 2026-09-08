---
title: "Hidden in Plain Sight: Part 2a"
slug: part-2a-frequency-analysis-and-caesar-ciphers
course: ai-and-ml-foundations
course_title: "AI and ML Foundations"
series: 6-projects-hidden-in-plain-sight
series_title: "Projects / Hidden in Plain Sight"
version: 2026.09.06.1
---

# Hidden in Plain Sight: Part 2a
## Frequency Analysis and Caesar Ciphers

## Welcome Back!

In Part 1, you encoded text as grayscale images and discovered that repeated letters create repeated patterns.

This observation is powerful. In this tutorial, we'll explore why patterns matter and how they reveal information in encrypted text.

### What You'll Learn

1. **Letter Frequencies**: Why some letters appear more often
2. **Statistical Analysis**: Measuring and visualizing patterns  
3. **Chi-Squared Testing**: Comparing patterns mathematically (with intuition!)
4. **Caesar Ciphers**: Simple but important historical encryption
5. **Cryptanalysis**: Breaking ciphers using frequency analysis

### Historical Context

Throughout history, people have protected private communications. From personal letters to journalistic sources, from resistance movements to diplomatic correspondence, information privacy has been essential for human rights.

In the 9th century, Arab philosopher and mathematician **Al-Kindi** discovered that encrypted messages carry statistical fingerprints. His frequency analysis work represents one of humanity's earliest applications of statistics to practical problems. Al-Kindi contributed to philosophy, mathematics, medicine, and many fields - cryptography was part of his broader interest in understanding patterns in language and nature.

### Prerequisites

- Part 1 completed (character encoding, 2D arrays, image creation)
- Basic Python (loops, lists, functions, dictionaries)
- Comfort with percentages and basic statistics
- numpy and matplotlib (same as Part 1)

```python exec
id: part-2a-frequency-analysis-and-caesar-ciphers-1
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter

plt.rcParams['figure.figsize'] = (12, 6)
plt.rcParams['font.size'] = 11

print('Libraries loaded!')
print('Ready for frequency analysis.')
```

---

## Section 1: Discovering Letter Frequencies

### The Question

Do all letters appear equally often in English text?

Before reading further, think about this. Look at this sentence. Do some letters seem more common?

### A Simple Experiment

```python exec
id: part-2a-frequency-analysis-and-caesar-ciphers-2
# Famous opening line
sample = "It was the best of times it was the worst of times"

# Clean: remove spaces, uppercase
clean = sample.upper().replace(' ', '')

print(f'Original: {sample}')
print(f'Cleaned: {clean}')
print(f'Total letters: {len(clean)}')

# Count letters
counts = Counter(clean)
print('\nLetter counts:')
for letter in sorted(counts):
    print(f'{letter}: {counts[letter]}')
```

**Observation:** Even in short text, some letters appear much more often!

### Expected Frequencies in English

Linguists analyzing millions of words found remarkably consistent patterns:

**Most common:**
- E: ~12.7%
- T: ~9.1%
- A: ~8.2%
- O: ~7.5%
- I: ~7.0%

**Least common:**
- Q: ~0.10%
- Z: ~0.07%

**Mnemonic:** "ETAOIN SHRDLU" - the 12 most common letters, famously used on Linotype machines!

**Why this pattern?**
- Common words use these letters ("the", "and", "of")
- English has more words with these letters
- Historical language evolution

---

## Section 2: Caesar Ciphers

### What is a Caesar Cipher?

A shift cipher - one of the simplest encryption methods. Shifts each letter by a fixed number of positions.

**Historical Note:**

Named after Julius Caesar who used it, but shift ciphers have been used throughout history by anyone needing basic privacy - lovers protecting letters, individuals maintaining private journals, resistance movements sharing information safely.

Simple doesn't mean secure, but understanding these historical methods helps us appreciate cryptography's role in protecting human rights and privacy.

### How It Works

**Example: Shift by 3**

```
Original: A B C D E F G H I J K L M N O P Q R S T U V W X Y Z  
Shifted:  D E F G H I J K L M N O P Q R S T U V W X Y Z A B C
```

"HELLO" becomes "KHOOR"

### Mathematics

Using A=0, B=1, ..., Z=25:

```
Encryption: E(x) = (x + shift) mod 26
Decryption: D(x) = (x - shift) mod 26
```

The `mod 26` wraps around from Z back to A.

**Modulo is like a clock:**
- 13:00 + 2 hours = 15:00 (normal)
- 23:00 + 2 hours = 01:00 (wraps at 24)

For alphabet (26 letters):
- Z (25) + 1 = A (0)

```python exec
id: part-2a-frequency-analysis-and-caesar-ciphers-3
def caesar_cipher(text, shift):
    """
    Encrypt/decrypt text using Caesar cipher.
    
    Parameters:
    -----------
    text : str
        Text to process
    shift : int
        Number of positions to shift (negative for decryption)
    
    Returns:
    --------
    str : Shifted text
    """
    result = []
    for char in text:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.upper()
            char_num = ord(char) - ord('A')
            shifted_num = (char_num + shift) % 26
            shifted_char = chr(shifted_num + ord('A'))
            if not is_upper:
                shifted_char = shifted_char.lower()
            result.append(shifted_char)
        else:
            result.append(char)
    return ''.join(result)

# Test
original = "Hello, World!"
encrypted = caesar_cipher(original, 3)
decrypted = caesar_cipher(encrypted, -3)

print(f'Original:  {original}')
print(f'Encrypted: {encrypted}')
print(f'Decrypted: {decrypted}')
print(f'Match: {original == decrypted}')
```

---

## Section 3: Building Intuition for Chi-Squared Testing

*This section is crucial! Take your time here.*

### The Problem

We need to answer: **"How well does this text's letter frequency match English?"**

We need a single number: "good match" or "terrible match."

Chi-squared (χ²) gives us exactly that!

### Starting with Surprise

Imagine a bag with 10 letter tiles. Based on English, expect:
- E: 5 tiles (50%)
- T: 3 tiles (30%)
- A: 2 tiles (20%)

Draw all 10 tiles. Three scenarios:

**Scenario 1:** Get E=5, T=3, A=2
**Surprise level:** ZERO (perfect match!)

**Scenario 2:** Get E=4, T=3, A=3
**Surprise level:** LOW (close match)

**Scenario 3:** Get E=0, T=0, A=10
**Surprise level:** VERY HIGH (terrible match!)

### Chi-Squared = Number for Surprise

- Scenario 1: χ² ≈ 0
- Scenario 2: χ² ≈ small number
- Scenario 3: χ² ≈ large number

**Lower χ² = better match**

```python exec
id: part-2a-frequency-analysis-and-caesar-ciphers-4
# Demonstrate the concept
expected = {'E': 5, 'T': 3, 'A': 2}
observed = {'E': 4, 'T': 3, 'A': 3}

print('Simple differences:')
total_diff = 0
for letter in expected:
    diff = observed[letter] - expected[letter]
    total_diff += diff
    print(f'{letter}: observed={observed[letter]}, expected={expected[letter]}, diff={diff}')

print(f'\nSum of differences: {total_diff}')
print('Problem: Positive and negative cancel out!')

print('\nSquared differences:')
total_squared = 0
for letter in expected:
    diff = observed[letter] - expected[letter]
    squared = diff ** 2
    total_squared += squared
    print(f'{letter}: difference={diff}, squared={squared}')

print(f'\nSum of squared: {total_squared}')
print('Better! Now we see the mismatch.')
```

### Why Square?

**To prevent cancellation and emphasize large differences.**

### Why Divide by Expected?

**Proportionality problem:**

Situation A: Expected 100, got 105 → 5% difference
Situation B: Expected 2, got 7 → 250% difference!

Same absolute difference (5), but B is much more surprising!

**Solution:** Divide by expected value to normalize for rarity.

```python exec
id: part-2a-frequency-analysis-and-caesar-ciphers-5
# Proportionality demonstration
situations = [
    ('A', 100, 105),
    ('B', 2, 7)
]

print('Comparing surprises:\n')
for name, expected, observed in situations:
    diff = observed - expected
    percent_diff = (diff / expected) * 100
    contribution = (diff ** 2) / expected
    
    print(f'Situation {name}:')
    print(f'  Expected {expected}, got {observed}')
    print(f'  Absolute difference: {diff}')
    print(f'  Percentage difference: {percent_diff:.1f}%')
    print(f'  Chi-squared contribution: {contribution:.2f}')
    print()

print('Situation B has higher chi-squared contribution,')
print('correctly reflecting it is more surprising!')
```

### Complete Formula

```
χ² = Σ [(Observed - Expected)² / Expected]
```

**In plain English:**
1. For each letter:
   - Find difference (observed - expected)
   - Square it (prevent cancellation)
   - Divide by expected (normalize for rarity)
2. Add up all values
3. Result is your chi-squared

**Lower = better match**

```python exec
id: part-2a-frequency-analysis-and-caesar-ciphers-6
# Standard English frequencies
ENGLISH_FREQ = {
    'E': 12.70, 'T': 9.06, 'A': 8.17, 'O': 7.51, 'I': 6.97,
    'N': 6.75, 'S': 6.33, 'H': 6.09, 'R': 5.99, 'D': 4.25,
    'L': 4.03, 'C': 2.78, 'U': 2.76, 'M': 2.41, 'W': 2.36,
    'F': 2.23, 'G': 2.02, 'Y': 1.97, 'P': 1.93, 'B': 1.29,
    'V': 0.98, 'K': 0.77, 'J': 0.15, 'X': 0.15, 'Q': 0.10, 'Z': 0.07
}

def calculate_frequency(text):
    """Calculate letter frequency percentages"""
    letters = [c.upper() for c in text if c.isalpha()]
    total = len(letters)
    if total == 0:
        return {}
    counts = Counter(letters)
    return {letter: (count / total) * 100 for letter, count in counts.items()}

def calculate_chi_squared(text_freq, expected_freq=ENGLISH_FREQ):
    """
    Calculate chi-squared comparing text to expected.
    Lower = better match.
    """
    chi_sq = 0.0
    for letter in expected_freq:
        observed = text_freq.get(letter, 0)
        expected = expected_freq[letter]
        if expected > 0:
            chi_sq += ((observed - expected) ** 2) / expected
    return chi_sq

# Test
test_text = "The quick brown fox jumps over the lazy dog"
freq = calculate_frequency(test_text)
chi_sq = calculate_chi_squared(freq)
print(f'Text: {test_text}')
print(f'Chi-squared: {chi_sq:.2f}')
print('\n(For English text, typically < 100)')
```

---

## Section 4: Breaking Caesar Ciphers

### The Strategy

**Key insight:** Only 26 possible shifts! Try them all!

**Brute force approach:**
1. Try all 26 shifts
2. For each, calculate letter frequencies
3. Calculate chi-squared vs English
4. Shift with **lowest** chi-squared is probably correct

### Pseudocode

```
FUNCTION break_caesar(encrypted_text):
    best_shift = 0
    best_chi_squared = infinity
    best_decryption = ""
    
    FOR shift FROM 0 TO 25:
        decrypted = caesar_cipher(encrypted_text, -shift)
        freq = calculate_frequency(decrypted)
        chi_sq = calculate_chi_squared(freq)
        
        IF chi_sq < best_chi_squared:
            best_chi_squared = chi_sq
            best_shift = shift
            best_decryption = decrypted
    
    RETURN best_decryption, best_shift, best_chi_squared
```

```python exec
id: part-2a-frequency-analysis-and-caesar-ciphers-7
def break_caesar(encrypted_text, show_all=False):
    """
    Break Caesar cipher by trying all shifts.
    
    Returns: (decrypted_text, shift, chi_squared)
    """
    best_shift = 0
    best_chi_sq = float('inf')
    best_decryption = ""
    results = []
    
    for shift in range(26):
        decrypted = caesar_cipher(encrypted_text, -shift)
        freq = calculate_frequency(decrypted)
        chi_sq = calculate_chi_squared(freq)
        results.append((shift, chi_sq, decrypted))
        
        if chi_sq < best_chi_sq:
            best_chi_sq = chi_sq
            best_shift = shift
            best_decryption = decrypted
    
    if show_all:
        print('Chi-squared for all shifts:')
        print('-' * 70)
        for shift, chi_sq, dec in sorted(results, key=lambda x: x[1]):
            preview = dec[:40].replace('\n', ' ')
            marker = ' *** BEST' if shift == best_shift else ''
            print(f'Shift {shift:2d}: χ²={chi_sq:6.2f} | {preview}{marker}')
        print('-' * 70)
    
    return best_decryption, best_shift, best_chi_sq

# Test
secret = "Wkh txlfn eurzq ira mxpsv ryhu wkh odcb grj."
print(f'Encrypted: {secret}')
print('\nBreaking cipher...\n')

decrypted, shift, chi_sq = break_caesar(secret, show_all=True)

print(f'\n*** RESULT ***')
print(f'Best shift: {shift}')
print(f'Chi-squared: {chi_sq:.2f}')
print(f'Decrypted: {decrypted}')
```

## Looking back

Before leaving this page, a sentence on each. What you write stays on this device.

```reflect
- Something you expected before running a cell that turned out differently
- The one idea from this page you could explain to someone else now
- Something you would change or try next, if there were time
- A question this page raised for you that it did not answer. Bring it to the next session; these questions are where the next session starts.
```

---

## Summary and Key Takeaways

### What You've Learned

1. **Letter Frequency Patterns**
 - Natural languages have predictable statistical patterns
 - E, T, A, O, I most common in English
 - Patterns consistent across large texts

2. **Caesar Ciphers**
 - Simple shift encryption
 - Used historically for basic privacy
 - Preserve frequency patterns (fatal weakness!)

3. **Chi-Squared Testing**
 - Measures how well observed matches expected
 - Lower values = better match
 - Enables automatic language detection
 - **Now you understand WHY it works, not just how!**

4. **Cryptanalysis**
 - Breaking ciphers by analyzing patterns
 - Brute force works when keyspace is small
 - Statistical methods reveal structure

5. **Limitations**
 - Simple substitution ciphers are NOT secure
 - Pattern preservation is fundamental weakness
 - Modern encryption must hide statistical patterns

### Skills Gained

 Statistical text analysis
 Frequency calculation and visualization
 Chi-squared testing (with deep intuition!)
 Implementing Caesar ciphers
 Automated cryptanalysis
 Critical thinking about encryption

### Looking Ahead: Part 2b

Caesar ciphers: only 26 possibilities. Easy to break!

But what about **random substitution** where each letter can be any other letter?

That's 26! = 403,291,461,126,605,635,584,000,000 possible keys!

Brute force won't work. In **Part 2b**, we'll learn:
- N-gram analysis (letter combinations)
- Why patterns persist in random substitution
- More sophisticated frequency analysis
- Breaking much harder ciphers

---

## Exercises

### Your turn 1: Different Languages

Letter frequencies differ between languages. Research frequencies for another language (Spanish, French, German) and create a frequency dictionary. Modify the cipher-breaking code to work for that language.

### Your turn 2: Text Length

Experiment to determine minimum text length for reliable cipher-breaking. Try different lengths (10, 50, 100, 200, 500 characters) and measure success rate.

### Try this: ROT13

ROT13 is shift=13. Special property: applying twice returns original (13+13=26=0 mod 26). Create a function that detects ROT13 and provides one-click decode.

---

## Additional Resources

### Frequency Analysis
- [Letter Frequency by Language](https://en.wikipedia.org/wiki/Letter_frequency)
- [Practical Cryptography](http://practicalcryptography.com/cryptanalysis/)
- [Chi-Squared Test Explained](https://www.statisticshowto.com/chi-square/)

### Historical Context 
- [Al-Kindi and Frequency Analysis](https://www.historyofinformation.com/detail.php?entryid=2441)
- [History of Cryptography](https://en.wikipedia.org/wiki/History_of_cryptography)
- [The Code Book by Simon Singh](https://simonsingh.net/books/the-code-book/)

### Interactive Tools
- [CyberChef](https://gchq.github.io/CyberChef/)
- [Cryptii](https://cryptii.com/)
- [Frequency Analysis Tool](https://www.dcode.fr/frequency-analysis)

---


You've completed Part 2a! You now understand:
- Why patterns in text matter
- How frequency analysis works
- **How and WHY chi-squared testing works** (with deep intuition!)
- How to break Caesar ciphers automatically

The chi-squared concept you learned is used throughout statistics and data science - you've gained a valuable tool!

**Next:** Part 2b - N-Gram Analysis and Breaking Random Substitution

Ready to tackle harder ciphers? Let's go!
