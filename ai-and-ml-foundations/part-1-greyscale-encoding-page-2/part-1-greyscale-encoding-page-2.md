---
title: "part-1-greyscale-encoding-page-2 (2 of 3)"
slug: part-1-greyscale-encoding-page-2
course: ai-and-ml-foundations
course_title: "AI and ML Foundations"
series: 6-projects-hidden-in-plain-sight
series_title: "Projects / Hidden in Plain Sight"
version: 2026.09.06.1
---

Before starting this page, run the cell below. It repeats the imports and definitions from the earlier pages that this page uses.

```python exec
id: part-1-greyscale-encoding-page-2-setup
import numpy as np
import matplotlib.pyplot as plt

# Import our minimal library set
import numpy as np
import matplotlib.pyplot as plt

# Configure matplotlib for clear visualizations
plt.rcParams['figure.figsize'] = (10, 6)
plt.rcParams['font.size'] = 11

print("Libraries loaded successfully!")
print("Ready to explore encoding.")

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

---

## Section 2.5: Understanding 2D Arrays and Image Structure

*This is a crucial section! If you've never worked with 2D arrays before, take your time here. Understanding this concept is essential for everything that follows.*

### What is a 2D Array?

Before we can create images from text, we need to understand how images are organized in computer memory. Images aren't just lists of pixel values - they're arranged in a grid with rows and columns.

Think about things you encounter daily that have two dimensions:

**A Chess Board:**
- 8 rows × 8 columns = 64 squares
- Each square has a position: "Row 4, Column E"
- You need two pieces of information to locate any square

**A Spreadsheet:**
- Rows numbered: 1, 2, 3, ...
- Columns labeled: A, B, C, ...
- Each cell has an address like "B5"

**Theater Seating:**
- Row letters: A, B, C, ...
- Seat numbers: 1, 2, 3, ...
- Your ticket might say "Row C, Seat 7"

All these systems use **two pieces of information** to locate something: a row and a column.

### From 1D Lists to 2D Arrays

You're already familiar with 1D lists (one-dimensional):

```python exec
id: part-1-greyscale-encoding-page-2-1
# A simple 1D list
letters_1d = ['A', 'B', 'C', 'D', 'E', 'F']

# To access an element, use ONE index:
print("1D list access:")
print(f"letters_1d[0] = {letters_1d[0]}")  # 'A'
print(f"letters_1d[3] = {letters_1d[3]}")  # 'D'

# This is like having items in a line:
print("\n1D visualization:")
print(" ".join(letters_1d))
print(" ".join([str(i) for i in range(len(letters_1d))]))
```

But images aren't lines - they're rectangles! We need rows AND columns:

```python exec
id: part-1-greyscale-encoding-page-2-2
# A 2D array (list of lists)
letters_2d = [
    ['A', 'B', 'C'],  # Row 0
    ['D', 'E', 'F']   # Row 1
]

# To access an element, use TWO indices:
print("2D array access:")
print(f"letters_2d[0][0] = {letters_2d[0][0]}")  # 'A' - Row 0, Column 0
print(f"letters_2d[0][1] = {letters_2d[0][1]}")  # 'B' - Row 0, Column 1
print(f"letters_2d[1][0] = {letters_2d[1][0]}")  # 'D' - Row 1, Column 0
print(f"letters_2d[1][2] = {letters_2d[1][2]}")  # 'F' - Row 1, Column 2

# Visualize the 2D structure
print("\n2D visualization:")
print("      Col0  Col1  Col2")
print("Row 0:  A     B     C")
print("Row 1:  D     E     F")
```

### Visual Diagram

Here's how to think about 2D array indexing:

```
        Column 0    Column 1    Column 2
      ┌──────────┬──────────┬──────────┐
Row 0 │    A     │    B     │    C     │
      ├──────────┼──────────┼──────────┤
Row 1 │    D     │    E     │    F     │
      └──────────┴──────────┴──────────┘

To access 'B': array[0][1]  (Row 0, Column 1)
To access 'E': array[1][1]  (Row 1, Column 1)
To access 'F': array[1][2]  (Row 1, Column 2)
```

**Important:** In Python (and most programming languages), we count from 0, not 1!
- First row is Row 0
- First column is Column 0

### Your turn: Reading 2D Arrays

```python exec
id: part-1-greyscale-encoding-page-2-3
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
# Here's a 3×3 grid of numbers
numbers = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

# Questions (try to answer before running):
print("What is at each position?")
print(f"[0][0] = {numbers[0][0]}  (should be 10)")
print(f"[1][1] = {numbers[1][1]}  (should be 50)")
print(f"[2][2] = {numbers[2][2]}  (should be 90)")
print(f"[1][2] = {numbers[1][2]}  (should be 60)")
print(f"[2][1] = {numbers[2][1]}  (should be 80)")

# Your turn: What would you type to access the number 30?
# Answer: numbers[0][2]
```

### From 1D Text to 2D Image Array

This is the key transformation we need! Here's the problem:

**Input:** A 1D list of values (our text converted to numbers)
```python
values = [72, 69, 76, 76, 79]  # "HELLO"
```

**Output:** A 2D array we can display as an image

Let's walk through this step by step:

```python exec
id: part-1-greyscale-encoding-page-2-4
# Step 1: Start with our text
text = "HELLO"
print(f"Text: {text}")
print(f"Length: {len(text)} characters")

# Step 2: Convert to numbers
values = [ord(char) for char in text]
print(f"\nValues: {values}")

# Step 3: Decide on image dimensions
# Let's make a 2×3 image (2 rows, 3 columns)
rows = 2
cols = 3
total_pixels = rows * cols
print(f"\nImage dimensions: {rows} rows × {cols} columns = {total_pixels} pixels")

# Step 4: Do we have enough values?
print(f"Values we have: {len(values)}")
print(f"Pixels we need: {total_pixels}")

if len(values) < total_pixels:
    print(f"We're short {total_pixels - len(values)} value(s)! Need padding.")
    # Add padding (using space = 32)
    while len(values) < total_pixels:
        values.append(32)  # space character
    print(f"After padding: {values}")
```

```python exec
id: part-1-greyscale-encoding-page-2-5
# Step 5: Reshape into 2D array
# Method 1: Manual (to understand the process)
array_2d = []
for row_num in range(rows):
    start_idx = row_num * cols  # Starting position for this row
    end_idx = start_idx + cols  # Ending position
    row_values = values[start_idx:end_idx]
    array_2d.append(row_values)
    print(f"Row {row_num}: indices [{start_idx}:{end_idx}] = {row_values}")

print(f"\n2D array (list of lists):")
for i, row in enumerate(array_2d):
    print(f"Row {i}: {row}")

# Step 6: Convert to numpy array for image display
array_2d_numpy = np.array(array_2d)
print(f"\nNumPy array shape: {array_2d_numpy.shape}")
print(f"NumPy array:\n{array_2d_numpy}")
```

Let's visualize what we just created:

```python exec
id: part-1-greyscale-encoding-page-2-6
# Show the transformation visually
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))

# Original 1D values
ax1.bar(range(len(values)), values)
ax1.set_title('1D: List of Values')
ax1.set_xlabel('Position')
ax1.set_ylabel('Value')
ax1.set_xticks(range(len(values)))
ax1.set_xticklabels([chr(v) for v in values])

# 2D array as image
im = ax2.imshow(array_2d_numpy, cmap='gray', vmin=0, vmax=255)
ax2.set_title('2D: Image Array')
ax2.set_xlabel('Column')
ax2.set_ylabel('Row')

# Add text labels showing the values
for i in range(rows):
    for j in range(cols):
        val = array_2d_numpy[i, j]
        char = chr(val) if 32 <= val <= 126 else '?'
        ax2.text(j, i, f'{char}\n{val}',
                ha='center', va='center',
                color='red' if val > 128 else 'yellow',
                fontsize=10, fontweight='bold')

plt.colorbar(im, ax=ax2, label='Pixel Value')
plt.tight_layout()
plt.show()
```

### Why Images Need 2D Arrays

Every digital image is fundamentally a 2D array of pixel values:

- **Width** = number of columns = how many pixels across
- **Height** = number of rows = how many pixels tall  
- **Total pixels** = width × height

For example, a 1920×1080 image has:
- 1080 rows
- 1920 columns
- Total: 1920 × 1080 = 2,073,600 pixels!

Each pixel in a grayscale image stores one number (0-255) representing its brightness.

### Common Confusions Addressed

#### Confusion 1: Row vs. Column Order

**Remember:** `array[row][column]`

**Mnemonic:** "RC" for "Row-Column" - alphabetically ordered!

```python exec
id: part-1-greyscale-encoding-page-2-7
# Example
grid = [[1, 2, 3], [4, 5, 6]]

print("To access 5 (second row, second column):")
print(f"grid[1][1] = {grid[1][1]} ✓ Correct!")
# NOT grid[2][2] or grid[1][2]
```

#### Confusion 2: Counting from 0

**Remember:** If you have N rows, valid indices are 0 to N-1

```python exec
id: part-1-greyscale-encoding-page-2-8
grid = [[1,2], [3,4], [5,6]]  # 3 rows, 2 columns

print("Valid row indices: 0, 1, 2")
print("Valid column indices: 0, 1")

# This would cause an error:
# grid[3][0]  # Row 3 doesn't exist! Only 0, 1, 2
```

### Practice: Create Your Own 2D Array

```python exec
id: part-1-greyscale-encoding-page-2-9
# Challenge: Create a 3×3 array with the letters in your name
# (If your name is shorter than 9 letters, add padding)

your_name = "YOURNAME"  # Replace with your name

# Convert to ASCII values
name_values = [ord(c) for c in your_name]

# Pad to 9 values if needed
while len(name_values) < 9:
    name_values.append(32)  # Add spaces

# Truncate if too long
name_values = name_values[:9]

# Reshape to 3×3
name_array = np.array(name_values).reshape(3, 3)

print("Your name as a 3×3 array:")
print(name_array)

# Display as image
plt.imshow(name_array, cmap='gray', vmin=0, vmax=255)
plt.title(f"Your name: {your_name}")
plt.colorbar(label='ASCII Value')
plt.show()
```

### Summary: 2D Arrays

**Key Points:**
1. 2D arrays organize data in rows and columns (like a grid)
2. Access elements using: `array[row][column]`
3. Images are 2D arrays of pixel values
4. Converting 1D to 2D:
   - Decide dimensions (rows × cols)
   - Add padding if needed
   - Split into rows of the right length
5. Always count from 0!

Now that you understand 2D arrays, we're ready to create images from text!

---

## Section 3: Creating Images from Text

Now we'll put everything together to create actual images from text messages.

### The Complete Encoding Process

**Pseudocode:**
```
FUNCTION text_to_image(text, width, height):
    
    # Step 1: Convert text to grayscale values
    values = empty list
    FOR each character in text:
        ascii_value = get ASCII value of character
        gray_value = ascii_value * 2  # Scale to 0-255 range
        IF gray_value > 255:
            gray_value = 255
        ADD gray_value to values
    
    # Step 2: Calculate how many pixels we need
    needed_pixels = width * height
    
    # Step 3: Add padding if necessary
    WHILE length of values < needed_pixels:
        ADD padding_value to values
    
    # Step 4: Truncate if too long
    IF length of values > needed_pixels:
        KEEP only first needed_pixels values
    
    # Step 5: Reshape into 2D array
    image_array = reshape values into height rows and width columns
    
    RETURN image_array
```

### Implementation

```python exec
id: part-1-greyscale-encoding-page-2-10
def text_to_image(text, width, height, padding_char=' '):
    """
    Convert text into a grayscale image array.

    Parameters:
    -----------
    text : str
        The text message to encode
    width : int
        Number of columns in the output image
    height : int
        Number of rows in the output image
    padding_char : str
        Character to use for padding (default: space)

    Returns:
    --------
    numpy.ndarray : 2D array of grayscale values
    """
    # Step 1: Convert text to grayscale values
    values = []
    for char in text:
        ascii_val = ord(char)
        gray_val = min(ascii_val * 2, 255)  # Scale and cap at 255
        values.append(gray_val)

    # Step 2: Calculate needed pixels
    needed = width * height

    # Step 3: Add padding if needed
    if len(values) < needed:
        padding_value = ord(padding_char) * 2
        values.extend([padding_value] * (needed - len(values)))

    # Step 4: Truncate if too long
    elif len(values) > needed:
        values = values[:needed]

    # Step 5: Reshape into 2D array
    image_array = np.array(values).reshape(height, width)

    return image_array

# Test it!
message = "Hello, World!"
img = text_to_image(message, width=5, height=3)

print(f"Message: {message}")
print(f"Image shape: {img.shape}")
print(f"Image array:\n{img}")
```

### Displaying the Image

```python exec
id: part-1-greyscale-encoding-page-2-11
def display_encoded_image(image_array, title="Encoded Message"):
    """
    Display a grayscale image with appropriate settings.
    """
    plt.figure(figsize=(10, 6))
    plt.imshow(image_array, cmap='gray', vmin=0, vmax=255, interpolation='nearest')
    plt.title(title, fontsize=14)
    plt.colorbar(label='Pixel Value (0=black, 255=white)')
    plt.xlabel('Column')
    plt.ylabel('Row')
    plt.tight_layout()
    plt.show()

# Display our encoded message
display_encoded_image(img, f"Encoded: {message}")
```

### Try Different Messages

```python exec
id: part-1-greyscale-encoding-page-2-12
# Compare different texts
messages = [
    "HELLO",
    "hello",
    "12345",
    "     "  # Five spaces
]

fig, axes = plt.subplots(2, 2, figsize=(12, 10))
axes = axes.flatten()

for idx, msg in enumerate(messages):
    img = text_to_image(msg, width=5, height=1)

    axes[idx].imshow(img, cmap='gray', vmin=0, vmax=255, aspect='auto')
    axes[idx].set_title(f"Text: '{msg}'")
    axes[idx].set_xticks(range(5))
    axes[idx].set_xticklabels(list(msg))
    axes[idx].set_yticks([])

plt.tight_layout()
plt.show()

print("Observations:")
print("- Uppercase and lowercase create different patterns")
print("- Numbers create a different pattern than letters")
print("- Spaces appear very dark")
```

---

## Section 4: Decoding Images Back to Text

Now for the reverse process: given an image, can we recover the original text?

### The Decoding Process

**Pseudocode:**
```
FUNCTION image_to_text(image_array):
    
    # Step 1: Flatten 2D array into 1D list
    values = flatten image_array into 1D
    
    # Step 2: Convert grayscale values back to ASCII
    characters = empty list
    FOR each gray_value in values:
        ascii_value = gray_value / 2  # Reverse the scaling
        ascii_value = round to nearest integer
        
        # Convert to character
        IF ascii_value is in valid range (0-127):
            character = convert ascii_value to character
            ADD character to characters
    
    # Step 3: Join into string
    text = join all characters
    
    RETURN text
```

```python exec
id: part-1-greyscale-encoding-page-2-13
def image_to_text(image_array):
    """
    Decode a grayscale image array back into text.

    Parameters:
    -----------
    image_array : numpy.ndarray
        2D array of grayscale values

    Returns:
    --------
    str : The decoded text message
    """
    # Step 1: Flatten to 1D
    values = image_array.flatten()

    # Step 2: Convert back to characters
    characters = []
    for gray_val in values:
        # Reverse the scaling (we multiplied by 2, so divide by 2)
        ascii_val = int(round(gray_val / 2))

        # Only convert if in valid ASCII range
        if 0 <= ascii_val <= 127:
            char = chr(ascii_val)
            characters.append(char)
        else:
            characters.append('?')  # Unknown character

    # Step 3: Join into string
    text = ''.join(characters)

    return text

# Test encoding and decoding
original = "Hello, World!"
print(f"Original text: {original}")

# Encode
encoded = text_to_image(original, width=5, height=3)
print(f"\nEncoded to {encoded.shape} image")

# Decode
decoded = image_to_text(encoded)
print(f"\nDecoded text: {decoded}")

# Check if they match
# Note: decoded might have padding, so we check if original is in decoded
match = original in decoded
print(f"\nSuccessful decode: {match}")
```

### Complete Encode-Decode Demo

```python exec
id: part-1-greyscale-encoding-page-2-14
def demo_encoding(message, width, height):
    """
    Complete demonstration of encoding and decoding.
    """
    print("="*60)
    print("ENCODING DEMONSTRATION")
    print("="*60)

    # Original message
    print(f"\n1. Original Message:")
    print(f"   '{message}'")
    print(f"   Length: {len(message)} characters")

    # Encode
    print(f"\n2. Encoding to {width}×{height} image...")
    encoded_image = text_to_image(message, width, height)
    print(f"   Image shape: {encoded_image.shape}")
    print(f"   Pixel values range: {encoded_image.min()} to {encoded_image.max()}")

    # Display
    print(f"\n3. Displaying image...")
    display_encoded_image(encoded_image, f"Encoded: {message}")

    # Decode
    print(f"\n4. Decoding image back to text...")
    decoded_message = image_to_text(encoded_image)
    print(f"   Decoded: '{decoded_message}'")

    # Verify
    print(f"\n5. Verification:")
    if message in decoded_message:
        print(f"   ✓ Success! Original message recovered.")
        if len(decoded_message) > len(message):
            print(f"   (Note: {len(decoded_message) - len(message)} padding characters added)")
    else:
        print(f"   ✗ Error: Messages don't match")
        print(f"   Original:  '{message}'")
        print(f"   Decoded:   '{decoded_message}'")

    print("\n" + "="*60)
    return encoded_image, decoded_message

# Try it!
my_message = "SECRET MESSAGE"
img, decoded = demo_encoding(my_message, width=5, height=3)
```

### Your turn: Encode Your Own Message

```python exec
id: part-1-greyscale-encoding-page-2-15
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
# Your turn! Create and encode a message
# Try different dimensions and see how it affects the image

your_message = "Write your message here!"
image_width = 8
image_height = 4

# Encode and decode
my_img, my_decoded = demo_encoding(your_message, image_width, image_height)

# Challenges:
# 1. What happens if you make the image very wide (width=20, height=1)?
# 2. What happens if you make it square (width=10, height=10)?
# 3. Can you encode a longer message? How big does the image need to be?
```

---

## Section 5: Exploring Patterns and Limitations

### Pattern Recognition

One interesting property: repeated letters create repeated patterns!

```python exec
id: part-1-greyscale-encoding-page-2-16
# Compare messages with and without repetition
messages = [
    "ABCDEFGH",
    "AAAABBBB",
    "ABABABAB"
]

fig, axes = plt.subplots(len(messages), 1, figsize=(12, 8))

for idx, msg in enumerate(messages):
    img = text_to_image(msg, width=8, height=1)

    axes[idx].imshow(img, cmap='gray', vmin=0, vmax=255, aspect='auto')
    axes[idx].set_title(f"Text: '{msg}'")
    axes[idx].set_xticks(range(8))
    axes[idx].set_xticklabels(list(msg))
    axes[idx].set_yticks([])

plt.tight_layout()
plt.show()

print("Pattern Observations:")
print("- All different letters: Varied grayscale")
print("- Repeated letters: Blocks of same shade")
print("- Alternating letters: Striped pattern")
```

### Limitations and Considerations

**Information Leakage:**
- Same letters always produce the same shade
- Repeated patterns are visible
- This is NOT secure encryption!

**Image Size Constraints:**
- Longer messages need larger images
- Very small images can only hold a few characters
- Padding affects image size

```python exec
id: part-1-greyscale-encoding-page-2-17
# Calculate required image size for a message
def calculate_required_size(message_length, aspect_ratio=1.5):
    """
    Calculate good dimensions for encoding a message.

    aspect_ratio: width/height (1.5 means 3:2 ratio)
    """
    # We need at least message_length pixels
    # Let's aim for width = aspect_ratio * height
    # So: width * height >= message_length
    # And: width = aspect_ratio * height
    # Therefore: aspect_ratio * height^2 >= message_length

    height = int(np.ceil(np.sqrt(message_length / aspect_ratio)))
    width = int(np.ceil(aspect_ratio * height))

    return width, height

# Test with different message lengths
test_lengths = [10, 50, 100, 500]

print("Recommended image dimensions:")
print(f"{'Message Length':<20} {'Width x Height':<20} {'Total Pixels'}")
print("-" * 60)

for length in test_lengths:
    w, h = calculate_required_size(length)
    total = w * h
    print(f"{length:<20} {f'{w} x {h}':<20} {total}")
```

## Looking back

Before leaving this page, a sentence on each. What you write stays on this device.

```reflect
- Something you expected before running a cell that turned out differently
- The one idea from this page you could explain to someone else now
- Something you would change or try next, if there were time
- A question this page raised for you that it did not answer. Bring it to the next session; these questions are where the next session starts.
```
