---
title: "Hidden in Plain Sight: Part 1 (1 of 3)"
slug: part-1-greyscale-encoding-page-1
course: ai-and-ml-foundations
course_title: "AI and ML Foundations"
series: 6-projects-hidden-in-plain-sight
series_title: "Projects / Hidden in Plain Sight"
version: 2026.09.06.1
---

# Hidden in Plain Sight: Part 1
## Greyscale Image Encoding

## Welcome!

Have you ever wondered how computers store and display text? Or how digital images are really just grids of numbers? In this tutorial, you'll discover how to hide messages in images by converting letters into grayscale pixels.

By the end of this tutorial, you'll be able to:
- Convert text into numbers using character encoding
- Understand how 2D arrays organize image data
- Create grayscale images from text messages
- Decode images back into readable text

### What You'll Learn

1. **Character Encoding**: How computers represent letters as numbers
2. **2D Arrays**: How images organize pixel data in rows and columns
3. **Grayscale Values**: How numbers become shades of gray
4. **Encoding**: Transforming text into images
5. **Decoding**: Recovering text from images

### Why This Matters

The concepts you'll learn here are fundamental to:
- Digital image processing
- Data representation and transformation
- Understanding how computers store information
- Foundations of steganography (hiding information)

### Prerequisites

- Basic Python knowledge (variables, loops, functions, lists)
- No image processing experience needed
- We'll use only **numpy** and **matplotlib** throughout

Let's begin!

```python exec
id: part-1-greyscale-encoding-page-1-1
# Import our minimal library set
import numpy as np
import matplotlib.pyplot as plt

# Configure matplotlib for clear visualizations
plt.rcParams['figure.figsize'] = (10, 6)
plt.rcParams['font.size'] = 11

print("Libraries loaded successfully!")
print("Ready to explore encoding.")
```

---

## Section 1: Characters as Numbers

### The Fundamental Question

Computers don't understand letters directly. They only work with numbers. So how does a computer store the letter 'A' or the word 'HELLO'?

The answer: **Character encoding systems** that map each character to a unique number.

### ASCII and Unicode

**ASCII** (American Standard Code for Information Interchange) was one of the first widely-used character encoding systems, created in the 1960s. It assigns numbers 0-127 to common characters:

- Numbers: '0' = 48, '1' = 49, ..., '9' = 57
- Uppercase: 'A' = 65, 'B' = 66, ..., 'Z' = 90
- Lowercase: 'a' = 97, 'b' = 98, ..., 'z' = 122
- Symbols: '!' = 33, '?' = 63, ' ' = 32 (space)

**Unicode** is a more comprehensive system that includes ASCII plus thousands of additional characters from languages worldwide, emoji, and symbols.

**Learn more:**
- [ASCII Table](https://www.asciitable.com/)
- [Unicode Consortium](https://home.unicode.org/)
- [Character Encoding Basics](https://www.joelonsoftware.com/2003/10/08/the-absolute-minimum-every-software-developer-absolutely-positively-must-know-about-unicode-and-character-sets-no-excuses/)

### Converting Characters to Numbers

Python provides the `ord()` function to get a character's numeric code:

```python exec
id: part-1-greyscale-encoding-page-1-2
# Get the numeric value of a character
print("Character codes:")
print(f"'A' = {ord('A')}")
print(f"'B' = {ord('B')}")
print(f"'a' = {ord('a')}")
print(f"' ' (space) = {ord(' ')}")
print(f"'!' = {ord('!')}")

# Notice the pattern
print("\nPattern in letters:")
for letter in ['A', 'B', 'C', 'D', 'E']:
    print(f"{letter} = {ord(letter)}")
```

**Observation:** Notice that consecutive letters have consecutive numbers! This pattern makes sense - the encoding system was designed to be logical and systematic.

### Converting Numbers Back to Characters

The reverse operation uses `chr()`:

```python exec
id: part-1-greyscale-encoding-page-1-3
# Convert numbers back to characters
print("Number to character:")
print(f"65 = '{chr(65)}'")
print(f"72 = '{chr(72)}'")
print(f"33 = '{chr(33)}'")

# Can you guess what this spells?
mystery_numbers = [72, 69, 76, 76, 79]
mystery_word = ''.join([chr(n) for n in mystery_numbers])
print(f"\nMystery word: {mystery_word}")
```

### Your Turn: Exercise 1

**Task:** Convert your name to numbers and back again.

1. Use `ord()` to get the number for each letter
2. Store the numbers in a list
3. Use `chr()` to convert back to letters
4. Join them to recreate your name

```python exec
id: part-1-greyscale-encoding-page-1-4
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
# Your code here
# Example:
name = "YOUR_NAME_HERE"

# Step 1: Convert to numbers
numbers = [ord(char) for char in name]
print(f"Name: {name}")
print(f"Numbers: {numbers}")

# Step 2: Convert back to letters
recovered = ''.join([chr(n) for n in numbers])
print(f"Recovered: {recovered}")
print(f"Match: {name == recovered}")
```

---

## Section 2: From Numbers to Grayscale

### What is Grayscale?

In digital images, grayscale means using shades of gray (from black to white) to represent each pixel. Instead of color, each pixel has just one number representing its brightness.

**Standard range:** 0 to 255
- 0 = pure black
- 255 = pure white  
- Values in between = shades of gray

**Why 0-255?** Computers store each pixel using 8 bits (one byte). With 8 bits, you can represent 2^8 = 256 different values (0 through 255).

### Mapping Characters to Grayscale

ASCII values range from 0-127, but we need values in the range 0-255 for best visibility. Let's create a simple mapping:

```python exec
id: part-1-greyscale-encoding-page-1-5
def char_to_grayscale(character):
    """
    Convert a character to a grayscale value (0-255).

    Strategy: Multiply ASCII value by 2 to spread across full range.
    This ensures different characters get noticeably different shades.

    Parameters:
    -----------
    character : str
        Single character to convert

    Returns:
    --------
    int : Grayscale value (0-255)
    """
    ascii_val = ord(character)
    grayscale = ascii_val * 2  # Scale up to use more of 0-255 range

    # Ensure we don't exceed 255
    if grayscale > 255:
        grayscale = 255

    return grayscale

# Test it
print("Character to grayscale:")
for char in ['A', 'M', 'Z', 'a', 'm', 'z', ' ']:
    gray = char_to_grayscale(char)
    print(f"'{char}' (ASCII {ord(char)}) → grayscale {gray}")
```

**Observation:**
- Lowercase letters appear lighter (higher values) than uppercase
- Space character appears very dark (low value)
- The multiply-by-2 scaling helps spread values across the full range

### Visualizing Grayscale Values

Let's see what these values look like visually:

```python exec
id: part-1-greyscale-encoding-page-1-6
# Create a simple grayscale bar
test_text = "HELLO world!"
gray_values = [char_to_grayscale(char) for char in test_text]

# Reshape into a row for display
gray_row = np.array(gray_values).reshape(1, -1)

# Display
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 4))

# Show the grayscale bar
ax1.imshow(gray_row, cmap='gray', vmin=0, vmax=255, aspect='auto')
ax1.set_title(f'Grayscale Representation of "{test_text}"')
ax1.set_xticks(range(len(test_text)))
ax1.set_xticklabels(list(test_text))
ax1.set_yticks([])

# Show the values as a bar chart
ax2.bar(range(len(gray_values)), gray_values, color='gray')
ax2.set_xlabel('Character Position')
ax2.set_ylabel('Grayscale Value')
ax2.set_title('Numeric Values')
ax2.set_xticks(range(len(test_text)))
ax2.set_xticklabels(list(test_text))
ax2.set_ylim([0, 255])
ax2.grid(axis='y', alpha=0.3)

plt.tight_layout()
plt.show()

print("\nGrayscale values:")
for char, gray in zip(test_text, gray_values):
    print(f"'{char}' → {gray}")
```

**What do you notice?**
- Each character creates a unique shade of gray
- Uppercase and lowercase versions of the same letter look different
- The space character is quite dark
- We can see patterns emerging even in this simple visualization

## Looking back

Before leaving this page, a sentence on each. What you write stays on this device.

```reflect
- Something you expected before running a cell that turned out differently
- The one idea from this page you could explain to someone else now
- Something you would change or try next, if there were time
- A question this page raised for you that it did not answer. Bring it to the next session; these questions are where the next session starts.
```
