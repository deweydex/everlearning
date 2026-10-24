---
title: "Week 7-8: Text Generation with Markov Chains"
slug: week-07-08-text-generation
course: ai-and-ml-foundations
course_title: "AI and ML Foundations"
series: 6-projects-from-0-to-markov
series_title: "Projects / From 0 to Markov"
version: 2026.09.06.1
---

# Week 7-8: Text Generation with Markov Chains

## Making Machines Write

This is it. The moment we've been building toward.

You're about to teach a computer to write. Not perfectly, not intelligently (yet), but surprisingly well.

By applying Markov chains to text, you'll create generators that can:
- Write fake Shakespeare
- Generate plausible tweets
- Create nonsense that *sounds* right
- Mimic any writing style you feed it

The key insight: **text is just a sequence of symbols**. And we're experts at modeling sequences now!

Let's start simple and build up to something impressive.

---

```python exec
id: week-07-08-text-generation-1
import numpy as np
import matplotlib.pyplot as plt
from collections import defaultdict, Counter
import random
import string

np.random.seed(42)
random.seed(42)
```

## Part 1: Character-Level Generation

Let's start with the simplest approach: treating each **character** as a state.

If we train on "hello world", our chain learns:
- After 'h', we often see 'e'
- After 'l', we might see 'l' or 'o'
- After 'o', we might see ' ' or 'r'

### Building a Character-Level Chain

```python exec
id: week-07-08-text-generation-2
class CharacterMarkovChain:
    """
    Markov chain for character-level text generation.
    """
    
    def __init__(self, order=1):
        """
        order: how many previous characters to consider
        order=1: current character depends on 1 previous
        order=2: current character depends on 2 previous
        """
        self.order = order
        self.transitions = defaultdict(lambda: defaultdict(int))
        self.transition_probs = {}
    
    def fit(self, text):
        """Learn from text."""
        for i in range(len(text) - self.order):
            # Context: the previous 'order' characters
            context = text[i:i+self.order]
            # Next character
            next_char = text[i+self.order]
            
            self.transitions[context][next_char] += 1
        
        # Convert to probabilities
        for context, next_chars in self.transitions.items():
            total = sum(next_chars.values())
            self.transition_probs[context] = {
                char: count/total 
                for char, count in next_chars.items()
            }
        
        return self
    
    def generate(self, start_text, length=100):
        """
        Generate text starting with start_text.
        """
        if len(start_text) < self.order:
            raise ValueError(f"start_text must be at least {self.order} characters")
        
        result = start_text
        
        for _ in range(length):
            # Get the context (last 'order' characters)
            context = result[-self.order:]
            
            # If we've never seen this context, pick a random one
            if context not in self.transition_probs:
                context = random.choice(list(self.transition_probs.keys()))
            
            # Get possible next characters
            probs = self.transition_probs[context]
            chars = list(probs.keys())
            probabilities = list(probs.values())
            
            # Choose next character
            next_char = np.random.choice(chars, p=probabilities)
            result += next_char
        
        return result
    
    def analyze(self):
        """Show some statistics about the learned model."""
        print(f"Order: {self.order}")
        print(f"Unique contexts: {len(self.transition_probs)}")
        print(f"\nMost common contexts:")
        
        # Count total appearances of each context
        context_counts = {
            context: sum(chars.values()) 
            for context, chars in self.transitions.items()
        }
        
        top_contexts = sorted(context_counts.items(), 
                            key=lambda x: x[1], reverse=True)[:5]
        
        for context, count in top_contexts:
            print(f"  '{context}': {count} times")
            # Show what follows
            next_chars = self.transition_probs[context]
            top_next = sorted(next_chars.items(), 
                            key=lambda x: x[1], reverse=True)[:3]
            for char, prob in top_next:
                print(f"    → '{char}': {prob:.2%}")
```

### Test with Simple Text

```python exec
id: week-07-08-text-generation-3
# Start with something simple
simple_text = "hello world, hello there, hello everyone, hi there, hi world"

# First-order model
char_mc1 = CharacterMarkovChain(order=1)
char_mc1.fit(simple_text)

print("First-Order Character Model:")
print("=" * 60)
char_mc1.analyze()

print("\nGenerated text:")
print("=" * 60)
for i in range(3):
    generated = char_mc1.generate("h", length=40)
    print(f"{i+1}. {generated}")
```

### Try Higher Order

```python exec
id: week-07-08-text-generation-4
# Second-order model (considers last 2 characters)
char_mc2 = CharacterMarkovChain(order=2)
char_mc2.fit(simple_text)

print("\nSecond-Order Character Model:")
print("=" * 60)
char_mc2.analyze()

print("\nGenerated text:")
print("=" * 60)
for i in range(3):
    generated = char_mc2.generate("he", length=40)
    print(f"{i+1}. {generated}")
```

**Notice:** Higher order = more realistic! But also more repetitive with small training data.

---

## Part 2: Training on Real Text

Let's use actual literary text. We'll start with some famous opening lines:

```python exec
id: week-07-08-text-generation-5
# Famous book openings
training_text = """
It was the best of times, it was the worst of times, it was the age of wisdom, 
it was the age of foolishness, it was the epoch of belief, it was the epoch of 
incredulity, it was the season of Light, it was the season of Darkness, it was 
the spring of hope, it was the winter of despair.

Call me Ishmael. Some years ago, never mind how long precisely, having little 
or no money in my purse, and nothing particular to interest me on shore, I 
thought I would sail about a little and see the watery part of the world.

It is a truth universally acknowledged, that a single man in possession of a 
good fortune, must be in want of a wife. However little known the feelings or 
views of such a man may be on his first entering a neighbourhood, this truth 
is so well fixed in the minds of the surrounding families, that he is 
considered the rightful property of some one or other of their daughters.
"""

print(f"Training text length: {len(training_text)} characters")
print(f"Unique characters: {len(set(training_text))}")
```

### Train and Generate

```python exec
id: week-07-08-text-generation-6
# Try different orders
for order in [1, 2, 3, 4]:
    print(f"\n{'='*70}")
    print(f"ORDER {order}:")
    print(f"{'='*70}\n")
    
    model = CharacterMarkovChain(order=order)
    model.fit(training_text)
    
    # Generate starting with "It "
    start = "It " if order <= 2 else "It w"
    generated = model.generate(start, length=200)
    print(generated)
    print()
```

### Observations

**Order 1**: Gibberish, but with correct letter frequencies  
**Order 2**: Some word-like structures appear  
**Order 3**: Real words start appearing!  
**Order 4**: Almost too good - starts copying training text

There's a **sweet spot** around order 2-3 for character-level generation.

---

## Part 3: Word-Level Generation

Character-level is fun, but word-level is where things get interesting!

Instead of learning "h" → "e", we learn "the" → "quick"

```python exec
id: week-07-08-text-generation-7
class WordMarkovChain:
    """
    Markov chain for word-level text generation.
    """
    
    def __init__(self, order=1):
        self.order = order
        self.transitions = defaultdict(lambda: defaultdict(int))
        self.transition_probs = {}
        self.start_words = []  # Track sentence starts
    
    def tokenize(self, text):
        """Split text into words (simple tokenization)."""
        # Keep punctuation attached to words for now
        words = text.split()
        return words
    
    def fit(self, text):
        """Learn from text."""
        words = self.tokenize(text)
        
        # Track possible sentence starts (words after periods)
        self.start_words = [words[0]]  # First word is always a start
        for i in range(len(words) - 1):
            if any(p in words[i] for p in '.!?'):
                if i + 1 < len(words):
                    self.start_words.append(words[i+1])
        
        # Learn transitions
        for i in range(len(words) - self.order):
            context = tuple(words[i:i+self.order])
            next_word = words[i+self.order]
            self.transitions[context][next_word] += 1
        
        # Convert to probabilities
        for context, next_words in self.transitions.items():
            total = sum(next_words.values())
            self.transition_probs[context] = {
                word: count/total 
                for word, count in next_words.items()
            }
        
        return self
    
    def generate(self, length=50, start_word=None):
        """
        Generate text with specified number of words.
        """
        if not self.transition_probs:
            raise ValueError("Model not trained yet!")
        
        # Choose starting context
        if start_word:
            # Find contexts that start with this word
            matching = [c for c in self.transition_probs.keys() 
                       if c[0].lower().startswith(start_word.lower())]
            if matching:
                context = random.choice(matching)
            else:
                context = random.choice(list(self.transition_probs.keys()))
        else:
            # Start with a sentence starter
            first_word = random.choice(self.start_words)
            # Find contexts starting with this word
            matching = [c for c in self.transition_probs.keys() if c[0] == first_word]
            context = random.choice(matching) if matching else random.choice(list(self.transition_probs.keys()))
        
        result = list(context)
        
        for _ in range(length - len(context)):
            # Get current context
            current_context = tuple(result[-self.order:])
            
            # If we've never seen this context, try a random one
            if current_context not in self.transition_probs:
                # Try to find a context with matching end
                matching = [c for c in self.transition_probs.keys() 
                           if c[-1] == current_context[-1]]
                if matching:
                    current_context = random.choice(matching)
                else:
                    current_context = random.choice(list(self.transition_probs.keys()))
            
            # Choose next word
            probs = self.transition_probs[current_context]
            words = list(probs.keys())
            probabilities = list(probs.values())
            
            next_word = np.random.choice(words, p=probabilities)
            result.append(next_word)
        
        return ' '.join(result)
    
    def analyze(self, top_n=5):
        """Show statistics about learned model."""
        print(f"Order: {self.order}")
        print(f"Unique contexts: {len(self.transition_probs)}")
        print(f"Possible sentence starts: {len(set(self.start_words))}")
        
        print(f"\nMost common contexts:")
        context_counts = {
            context: sum(words.values()) 
            for context, words in self.transitions.items()
        }
        
        top_contexts = sorted(context_counts.items(), 
                            key=lambda x: x[1], reverse=True)[:top_n]
        
        for context, count in top_contexts:
            print(f"\n  {' '.join(context)}: {count} times")
            next_words = self.transition_probs[context]
            top_next = sorted(next_words.items(), 
                            key=lambda x: x[1], reverse=True)[:3]
            for word, prob in top_next:
                print(f"    → {word}: {prob:.1%}")
```

### Train on Our Literary Text

```python exec
id: week-07-08-text-generation-8
# First-order word model
word_mc1 = WordMarkovChain(order=1)
word_mc1.fit(training_text)

print("First-Order Word Model:")
print("=" * 60)
word_mc1.analyze()

print("\n" + "=" * 60)
print("GENERATED TEXT (Order 1):")
print("=" * 60)
for i in range(3):
    text = word_mc1.generate(length=30)
    print(f"\n{i+1}. {text}")
```

```python exec
id: week-07-08-text-generation-9
# Second-order word model
word_mc2 = WordMarkovChain(order=2)
word_mc2.fit(training_text)

print("\nSecond-Order Word Model:")
print("=" * 60)
word_mc2.analyze()

print("\n" + "=" * 60)
print("GENERATED TEXT (Order 2):")
print("=" * 60)
for i in range(3):
    text = word_mc2.generate(length=30)
    print(f"\n{i+1}. {text}")
```

**Much better!** The second-order model produces surprisingly coherent text.

---

## Part 4: Training on Larger Corpora

The more training data, the better! Let's create a bigger training set:

```python exec
id: week-07-08-text-generation-10
# Extended literary corpus
large_corpus = """
It was the best of times, it was the worst of times, it was the age of wisdom, 
it was the age of foolishness. The sun was shining on the sea, shining with all 
his might. He tried with all his might to make the billows smooth and bright.

In the beginning was the Word, and the Word was with God, and the Word was God.
All things were made through him, and without him was not any thing made that was made.

To be, or not to be, that is the question. Whether tis nobler in the mind to suffer 
the slings and arrows of outrageous fortune, or to take arms against a sea of troubles.

It is a truth universally acknowledged that a single man in possession of a good fortune 
must be in want of a wife. However little known the feelings or views of such a man may be, 
this truth is so well fixed in the minds of the surrounding families.

Call me Ishmael. Some years ago, never mind how long precisely, having little or no money 
in my purse, and nothing particular to interest me on shore, I thought I would sail about 
a little and see the watery part of the world.

Once upon a time, in a land far, far away, there lived a young princess. She was beautiful 
and kind, loved by all who knew her. One day, she ventured into the deep, dark forest.

The man in black fled across the desert, and the gunslinger followed. The desert was the 
apotheosis of all deserts, huge, standing to the sky for what might have been parsecs in 
all directions.
"""

print(f"Corpus size: {len(large_corpus)} characters")
print(f"Word count: {len(large_corpus.split())}")
```

```python exec
id: week-07-08-text-generation-11
# Train multiple models
models = {}
for order in [1, 2, 3]:
    model = WordMarkovChain(order=order)
    model.fit(large_corpus)
    models[order] = model

# Generate comparison
for order, model in models.items():
    print(f"\n{'='*70}")
    print(f"ORDER {order} GENERATION:")
    print(f"{'='*70}\n")
    
    for i in range(2):
        text = model.generate(length=40)
        print(f"{text}\n")
```

---

## Part 5: Interactive Text Generator

Let's build an interactive tool where you can provide a prompt!

```python exec
id: week-07-08-text-generation-12
def interactive_generator(model, prompts):
    """
    Generate text from multiple prompts.
    """
    print("INTERACTIVE TEXT GENERATION")
    print("=" * 70)
    print(f"Model order: {model.order}")
    print(f"Training contexts: {len(model.transition_probs)}")
    print()
    
    for prompt in prompts:
        print(f"\nPrompt: '{prompt}'")
        print("-" * 70)
        
        try:
            generated = model.generate(length=30, start_word=prompt)
            print(generated)
        except Exception as e:
            print(f"Error: {e}")
            print("Trying without prompt...")
            generated = model.generate(length=30)
            print(generated)

# Test with different prompts
prompts = ["The", "It", "In", "Once", "Call"]
interactive_generator(models[2], prompts)
```

---

## Part 6: Analyzing Quality

How do we measure if generated text is "good"?

### Perplexity

**Perplexity** measures how "surprised" the model is by new text. Lower = better.

Formula: perplexity = 2^(-average log probability)

```python exec
id: week-07-08-text-generation-13
def calculate_perplexity(model, test_text):
    """
    Calculate perplexity of model on test text.
    Lower perplexity = better model.
    """
    words = model.tokenize(test_text)
    
    log_prob_sum = 0
    count = 0
    
    for i in range(len(words) - model.order):
        context = tuple(words[i:i+model.order])
        next_word = words[i+model.order]
        
        if context in model.transition_probs:
            if next_word in model.transition_probs[context]:
                prob = model.transition_probs[context][next_word]
                log_prob_sum += np.log2(prob)
                count += 1
    
    if count == 0:
        return float('inf')
    
    avg_log_prob = log_prob_sum / count
    perplexity = 2 ** (-avg_log_prob)
    
    return perplexity

# Test on held-out text
test_text = "It was a dark and stormy night when the man arrived at the old house."

print("Perplexity comparison:")
print("=" * 50)
for order, model in models.items():
    perp = calculate_perplexity(model, test_text)
    print(f"Order {order}: {perp:.2f}")

print("\n(Lower perplexity = better predictions)")
```

---

## Part 7: Style Transfer - Mimicking Authors

Different authors have different styles. Can we learn them?

```python exec
id: week-07-08-text-generation-14
# Different "authors" with distinct styles
formal_text = """
It is a truth universally acknowledged that a single man in possession of a good 
fortune must be in want of a wife. The circumstances of his life, however varied, 
are of considerable importance to the understanding of his character. One must 
consider the particulars with great attention and care.
"""

casual_text = """
So yeah, the guy was pretty rich and everyone figured he'd want to get married. 
His life was kinda all over the place but that's what made him interesting. You 
gotta look at the details if you really want to understand what he was all about.
"""

poetic_text = """
The moon hung low in the velvet sky, casting silver shadows across the sleeping 
earth. Stars whispered secrets to the night wind, which carried them gently to 
the dreaming souls below. Time itself seemed to pause, holding its breath in 
reverence of the quiet beauty.
"""

# Train separate models
formal_model = WordMarkovChain(order=2).fit(formal_text)
casual_model = WordMarkovChain(order=2).fit(casual_text)
poetic_model = WordMarkovChain(order=2).fit(poetic_text)

print("STYLE COMPARISON:\n")

print("FORMAL STYLE:")
print("-" * 70)
print(formal_model.generate(30))

print("\n\nCASUAL STYLE:")
print("-" * 70)
print(casual_model.generate(30))

print("\n\nPOETIC STYLE:")
print("-" * 70)
print(poetic_model.generate(30))
```

---

## Week 7-8 Summary

You've built text generators from scratch!

### What You've Created
- Character-level text generation
- Word-level text generation 
- Multi-order Markov models
- Style-specific generators
- Quality metrics (perplexity)

### Key Insights
- **Text is sequential data** - perfect for Markov chains
- **Order matters**: Higher order = more context = better coherence
- **But**: Higher order needs MORE training data
- **Sweet spot**: Usually order 2-3 for word-level
- **Style emerges**: Different training data → different generated style

### Limitations
- No long-term memory (forgets what it said 10 words ago)
- No semantic understanding (doesn't "know" what words mean)
- Can produce nonsense or inappropriate combinations
- Limited by training data size and quality

### Modern AI
What you've built is the ancestor of modern AI text generators!

- GPT models use **transformers** (not Markov chains)
- But the core idea is similar: predict next token from context
- Modern models have MUCH larger context windows
- And billions of parameters learned from internet-scale data

---

## Looking Ahead: Week 9-10

Final project time! You'll apply everything to build:
- A weather forecasting system with Markov chains
- A complete text generation app
- Other creative applications
- Statistical analysis and evaluation

Let's bring it all together!

---

## Try this Problems

### Try this 1: Twitter Bot
Collect 50+ tweet-like messages. Train a model and generate new "tweets" of exactly 280 characters.

```python exec
id: week-07-08-text-generation-15
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
# Your Twitter bot here
```

### Try this 2: Bi-directional Generation
Modify the WordMarkovChain to generate text both forward AND backward from a seed word. (Hint: Learn both forward and backward transitions)

```python exec
id: week-07-08-text-generation-16
# Bi-directional model
```

### Try this 3: Sentence Structure
Analyze generated text for sentence length distribution. Compare to training text. Are they similar?

```python exec
id: week-07-08-text-generation-17
# Statistical analysis
```

### Try this 4: Punctuation Model
Create a separate model that ONLY predicts when to use punctuation. Combine it with a word model for better-formatted output.

```python exec
id: week-07-08-text-generation-18
# Punctuation prediction
```

### Try this 5: Rhyme Generator
Train on poetry. Generate text that attempts to rhyme by tracking word endings and encouraging rhyming patterns.

```python exec
id: week-07-08-text-generation-19
# Rhyme-aware generator
```

## Looking back

Before leaving this page, a sentence on each. What you write stays on this device.

```reflect
- Something you expected before running a cell that turned out differently
- The one idea from this page you could explain to someone else now
- Something you would change or try next, if there were time
- A question this page raised for you that it did not answer. Bring it to the next session; these questions are where the next session starts.
```
