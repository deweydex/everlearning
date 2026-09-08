---
title: "DON'T RUN THIS! (2 of 3)"
slug: week-00-python-foundations-page-2
course: ai-and-ml-foundations
course_title: "AI and ML Foundations"
series: 6-projects-from-0-to-markov
series_title: "Projects / From 0 to Markov"
version: 2026.09.06.1
---

Before starting this page, run the cell below. It repeats the imports and definitions from the earlier pages that this page uses.

```python exec
id: week-00-python-foundations-page-2-setup
score = 0
print(f"Starting score: {score}")

score = score + 10
print(f"After bonus: {score}")

score = score + 5
print(f"After another bonus: {score}")

# Shortcut: score += 5 does the same as score = score + 5

for i in range(5):
    print("I will learn Python!")

print("Done! That was easy.")

scores = [78, 85, 92, 88, 76, 95, 89]

# Calculate average
total = 0
for score in scores:
    total = total + score

average = total / len(scores)
print(f"Average score: {average:.1f}")

# Find highest
highest = scores[0]
for score in scores:
    if score > highest:
        highest = score

print(f"Highest score: {highest}")
```

## Part 5: Functions - Creating Your Own Tools

### The DRY Principle: Don't Repeat Yourself

Imagine calculating rectangle areas over and over:

```python exec
id: week-00-python-foundations-page-2-1
# The tedious way
length1, width1 = 5, 3
area1 = length1 * width1
print(f"Rectangle 1: {area1}")

length2, width2 = 8, 4
area2 = length2 * width2
print(f"Rectangle 2: {area2}")

# This gets old fast!
```

### Solution: Create a Function!

```python exec
id: week-00-python-foundations-page-2-2
def rectangle_area(length: float, width: float) -> float:
    """Calculate the area of a rectangle."""
    area = length * width
    return area

# Now use it!
print(f"Rectangle 1: {rectangle_area(5, 3)}")
print(f"Rectangle 2: {rectangle_area(8, 4)}")
print(f"Rectangle 3: {rectangle_area(12, 7)}")

# Much cleaner!
```

### Anatomy of a Function

```python
def function_name(parameter1: type, parameter2: type)-> return_type:
    """
    Docstring: explains what the function does
    """
    # Do calculations
    result = parameter1 + parameter2
    
    # Return the answer
    return result
```

Key parts:
- `def`: keyword that starts a function
- `function_name`: what you call it (use descriptive names!)
- `parameters`: inputs (can have 0, 1, 2, or more)
- `return`: what comes back out

### Building Useful Functions

```python exec
id: week-00-python-foundations-page-2-3
def greet(name:str)-> str:
    """Say hello to someone."""
    return f"Hello, {name}! Welcome to Python!"

def is_even(number:int)-> int:
    """Check if a number is even."""
    return number % 2 == 0

def celsius_to_fahrenheit(celsius:float)-> float:
    """Convert Celsius to Fahrenheit."""
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# Test them!
print(greet("Alice"))
print("Is 7 even?", is_even(7))
print(f"Is 12 even? {is_even(12)}")
print(f"20°C is {celsius_to_fahrenheit(20):.1f}°F")
```

### Functions Can Return Multiple Values

```python exec
id: week-00-python-foundations-page-2-4
def analyze_number(num:int):
    """Return multiple properties of a number."""
    is_positive = num > 0
    is_even = num % 2 == 0
    square = num ** 2

    return is_positive, is_even, square

# Unpack the results
positive, even, sq = analyze_number(7)
print(f"7 is positive: {positive}")
print(f"7 is even: {even}")
print(f"7 squared: {sq}")
```

### Functions + Loops = Power!

```python exec
id: week-00-python-foundations-page-2-5
def sum_of_numbers(n):
    """
    Sum of 1 + 2 + ... + n
    Example: sum_of_numbers(5) = 15
    """
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

def count_vowels(text):
    """Count vowels in a string."""
    vowels = "aeiouAEIOU"
    count = 0

    for letter in text:
        if letter in vowels:
            count += 1

    return count

def find_factors(number):
    """Find all factors of a number."""
    factors = []

    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)

    return factors

# Test them
print(f"Sum 1 to 100: {sum_of_numbers(100)}")
print(f"Vowels in 'Hello World': {count_vowels('Hello World')}")
print(f"Factors of 24: {find_factors(24)}")
```

**Your turn:** Write a function called `is_prime(n)` that returns True if n is prime, False otherwise.

Hint: A prime number has exactly 2 factors (1 and itself)

```python exec
id: week-00-python-foundations-page-2-6
hint: Look at the variables already defined above this cell, and finish the line the same way the pattern before it was finished.
know: is_prime(7) prints True, and is_prime(12) prints False
def is_prime(n):
    """Check if n is a prime number."""
    # Your code here!
    pass

# Test it
# print(is_prime(7))   # Should be True
# print(is_prime(12))  # Should be False
```

<details class="dl-answer"><summary>answer</summary>

```python
def is_prime(n):
    """Check if n is a prime number."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Test it
print(is_prime(7))   # Should be True
print(is_prime(12))  # Should be False
```

</details>

---

## Part 6: Mini-Project - Text Analyzer

Let's combine everything we've learned into something useful!

We'll build a function that analyzes text and returns statistics about it.

```python exec
id: week-00-python-foundations-page-2-7
def analyze_text(text):
    """
    Analyze a piece of text and return statistics.

    Returns a dictionary with character count, word count,
    sentence count, and vowel count.
    """
    # Character count
    char_count = len(text)

    # Word count
    words = text.split()
    word_count = len(words)

    # Sentence count (approximate)
    sentences = text.count('.') + text.count('!') + text.count('?')

    # Vowel count
    vowels = "aeiouAEIOU"
    vowel_count = 0
    for char in text:
        if char in vowels:
            vowel_count += 1

    # Return all statistics as a dictionary
    return {
        'characters': char_count,
        'words': word_count,
        'sentences': sentences,
        'vowels': vowel_count
    }

# Test it
sample_text = """
Python is a powerful programming language.
It is easy to learn and fun to use!
You can build amazing things with it.
"""

stats = analyze_text(sample_text)

print("Text Analysis:")
print(f"Characters: {stats['characters']}")
print(f"Words: {stats['words']}")
print(f"Sentences: {stats['sentences']}")
print(f"Vowels: {stats['vowels']}")

# Calculate average word length
avg_word_length = stats['characters'] / stats['words']
print(f"Average word length: {avg_word_length:.1f} characters")
```

**Extension Challenge:** Modify the function to also count:
1. Consonants
2. Uppercase letters
3. Numbers in the text
4. The longest word

```python exec
id: week-00-python-foundations-page-2-8
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
# Your extended version here!
```

---

## Part 7: While Loops - A Different Kind of Repetition

Sometimes you don't know *how many times* to loop - you just want to loop *until something happens*.

That's where `while` loops shine.

```python exec
id: week-00-python-foundations-page-2-9
# Countdown with while
count = 5
while count > 0:
    print(count)
    count = count - 1
print("Blast off!")
```

**Warning:** While loops can run forever if you're not careful!

```python
# DON'T RUN THIS!
while True:
    print("Forever...")
```

If you accidentally create an infinite loop, click the stop button (■) in Jupyter.

### Interactive Example: Guessing Game

This won't work perfectly in Jupyter, but it demonstrates the concept:

```python exec
id: week-00-python-foundations-page-2-10
def guessing_game():
    """Simple number guessing game."""
    import random
    secret = random.randint(1, 10)
    attempts = 0

    print("I'm thinking of a number between 1 and 10...")

    # We'll simulate instead of using input
    # In a real program, you'd use: guess = int(input("Your guess: "))

    for attempt in range(1, 6):  # Give 5 attempts
        guess = random.randint(1, 10)  # Simulate random guessing
        print(f"Attempt {attempt}: Guess {guess}", end=" - ")

        if guess < secret:
            print("Too low!")
        elif guess > secret:
            print("Too high!")
        else:
            print(f"Correct! The number was {secret}")
            return

    print(f"\nOut of attempts! The number was {secret}")

guessing_game()
```

---

## Part 8: Final Project - The Dice Simulator

Let's build something that connects to what's coming next week: probability!

We'll simulate rolling dice thousands of times and see what patterns emerge.

```python exec
id: week-00-python-foundations-page-2-11
import random

def roll_die():
    """Roll a single 6-sided die."""
    return random.randint(1, 6)

def roll_multiple_dice(num_dice):
    """Roll multiple dice and return results."""
    rolls = []
    for i in range(num_dice):
        rolls.append(roll_die())
    return rolls

# Test basic rolling
print("Single roll:", roll_die())
print("Three dice:", roll_multiple_dice(3))
```

### Now Let's Simulate Many Rolls

This is where it gets interesting!

```python exec
id: week-00-python-foundations-page-2-12
def simulate_rolls(num_rolls):
    """
    Simulate many dice rolls and count outcomes.
    This connects to Week 1 probability!
    """
    # Count each outcome
    counts = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}

    for _ in range(num_rolls):
        roll = roll_die()
        counts[roll] += 1

    return counts

# Simulate 1000 rolls
results = simulate_rolls(1000)

print("\nResults from 1000 rolls:")
for face, count in results.items():
    percentage = (count / 1000) * 100
    bar = "█" * int(percentage / 2)  # Visual bar
    print(f"{face}: {bar} {count} ({percentage:.1f}%)")
```

**Question to ponder:** What do you notice about the percentages? What happens if you run it again? What about with 10,000 rolls?

This is your first glimpse of probability in action!

### Extension: Two Dice Sums

Here's a classic probability question: When you roll two dice and add them, which sum is most common?

```python exec
id: week-00-python-foundations-page-2-13
def two_dice_sum_simulator(num_rolls):
    """
    Roll two dice and track the sum.
    What sums are most common? Why?
    """
    sum_counts = {}

    for _ in range(num_rolls):
        die1 = roll_die()
        die2 = roll_die()
        total = die1 + die2

        if total not in sum_counts:
            sum_counts[total] = 0
        sum_counts[total] += 1

    return sum_counts

# Try it
sums = two_dice_sum_simulator(10000)

print("\nTwo-dice sum frequencies:")
for sum_value in sorted(sums.keys()):
    count = sums[sum_value]
    percentage = (count / 10000) * 100
    bar = "█" * int(percentage * 2)
    print(f"{sum_value:2d}: {bar} ({percentage:.1f}%)")
```

**Big question:** Why is 7 the most common sum?

Think about it before looking at the answer below.

<details>
<summary>Click here for the answer</summary>

There are more ways to make 7 than any other number:
- 1+6, 2+5, 3+4, 4+3, 5+2, 6+1 = 6 ways

Compare to 2:
- 1+1 = only 1 way

Or 12:
- 6+6 = only 1 way

This is the foundation of probability theory!
</details>

---

## Capstone Challenge: The Coin Flip Problem

Here's a famous probability puzzle that combines everything we've learned:

**Question:** On average, how many coin flips does it take to see three heads in a row?

```python exec
id: week-00-python-foundations-page-2-14
def flip_coin():
    """Return 'H' or 'T' for heads or tails."""
    return random.choice(['H', 'T'])

def flip_until_pattern(pattern):
    """
    Flip coins until we see a specific pattern.
    Example: pattern = "HHH" (three heads in a row)
    Return: number of flips needed, and all flips
    """
    flips = []
    flip_count = 0

    while True:
        flip = flip_coin()
        flips.append(flip)
        flip_count += 1

        # Check if we have the pattern
        if len(flips) >= len(pattern):
            recent = ''.join(flips[-len(pattern):])
            if recent == pattern:
                return flip_count, flips

# Test it
flips_needed, all_flips = flip_until_pattern("HHH")
print(f"Flips needed for HHH: {flips_needed}")
print(f"Sequence: {''.join(all_flips)}")
```

### Now Let's Run It Many Times

```python exec
id: week-00-python-foundations-page-2-15
def experiment_with_pattern(pattern, num_trials=100):
    """Run the experiment many times and find the average."""
    results = []

    for trial in range(num_trials):
        flips_needed, _ = flip_until_pattern(pattern)
        results.append(flips_needed)

    average = sum(results) / len(results)
    minimum = min(results)
    maximum = max(results)

    print(f"\nPattern: {pattern}")
    print(f"Average flips: {average:.1f}")
    print(f"Minimum: {minimum}")
    print(f"Maximum: {maximum}")

    return average

# Try different patterns
experiment_with_pattern("HHH", 100)
experiment_with_pattern("HTH", 100)
```

**Mind-bending question:** Do HHH and HTH take the same amount of time on average?

Try it and see! This is actually a famous result called "Penney's Game" in probability theory.

---

## Looking back

Before leaving this page, a sentence on each. What you write stays on this device.

```reflect
- Something you expected before running a cell that turned out differently
- The one idea from this page you could explain to someone else now
- Something you would change or try next, if there were time
- A question this page raised for you that it did not answer. Bring it to the next session; these questions are where the next session starts.
```
