---
title: "Hidden in Plain Sight: Part 3"
slug: part-3-rgb-encoding
course: ai-and-ml-foundations
course_title: "AI and ML Foundations"
series: 6-projects-hidden-in-plain-sight
series_title: "Projects / Hidden in Plain Sight"
version: 2026.09.06.1
---

# Hidden in Plain Sight: Part 3
## RGB Three-Channel Encoding

## Welcome to Part 3!

In Parts 1 and 2, you worked with grayscale images (one value per pixel). Now we'll explore **color images** using the RGB model - three channels of information!

This opens exciting possibilities:
- **3x storage capacity** (three values instead of one)
- Beautiful colorful encodings
- Natural connection to trigrams!

### What You'll Learn

1. **RGB Color Model**: How computers represent color
2. **Three-Channel Arrays**: Working with 3D data structures
3. **Efficient Encoding**: Storing more information per pixel
4. **Trigram-to-RGB Mapping**: Perfect fit for 3-letter sequences!
5. **Creative Applications**: Aesthetic and functional encoding

### Why This Matters

The RGB model is fundamental to:
- Digital images and video
- Computer graphics
- Display technologies
- Understanding color spaces
- Multi-dimensional data representation

### Prerequisites

- Parts 1, 2a, and 2b completed (especially understanding of 2D arrays and trigrams)
- Comfort with 3D thinking
- Same tools: numpy and matplotlib

```python exec
id: part-3-rgb-encoding-1
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['figure.figsize'] = (12, 6)
plt.rcParams['font.size'] = 11

print('Libraries loaded!')
print('Ready for RGB encoding.')
```

---

## Section 1: Understanding the RGB Color Model

### What is RGB?

RGB stands for **Red, Green, Blue** - the three primary colors of light.

**How it works:**
- Each pixel has THREE values instead of one
- Red channel: 0-255 (0=no red, 255=full red)
- Green channel: 0-255
- Blue channel: 0-255

**Mixing colors:**
- (255, 0, 0) = pure red
- (0, 255, 0) = pure green
- (0, 0, 255) = pure blue
- (255, 255, 0) = yellow (red + green)
- (255, 0, 255) = magenta (red + blue)
- (0, 255, 255) = cyan (green + blue)
- (255, 255, 255) = white (all colors)
- (0, 0, 0) = black (no color)

### Why RGB?

Human eyes have three types of color receptors (cones):
- L-cones: sensitive to long wavelengths (red)
- M-cones: sensitive to medium wavelengths (green)
- S-cones: sensitive to short wavelengths (blue)

RGB matches our biology!

```python exec
id: part-3-rgb-encoding-2
# Visualize RGB color mixing
colors = [
    ((255, 0, 0), 'Red'),
    ((0, 255, 0), 'Green'),
    ((0, 0, 255), 'Blue'),
    ((255, 255, 0), 'Yellow'),
    ((255, 0, 255), 'Magenta'),
    ((0, 255, 255), 'Cyan'),
    ((255, 255, 255), 'White'),
    ((128, 128, 128), 'Gray'),
    ((0, 0, 0), 'Black')
]

fig, axes = plt.subplots(3, 3, figsize=(10, 10))
axes = axes.flatten()

for idx, (rgb, name) in enumerate(colors):
    # Create 1x1 image with this color
    color_array = np.array([[rgb]], dtype=np.uint8)
    axes[idx].imshow(color_array)
    axes[idx].set_title(f'{name}\nRGB{rgb}')
    axes[idx].axis('off')

plt.tight_layout()
plt.show()

print('Notice how combining red, green, and blue creates all colors!')
```

---

## Section 2: Three-Channel Arrays

### From 2D to 3D

**Grayscale image:** 2D array
```
shape = (height, width)
example: (10, 15) = 10 rows, 15 columns
```

**RGB image:** 3D array
```
shape = (height, width, 3)
example: (10, 15, 3) = 10 rows, 15 columns, 3 channels
```

The third dimension holds [R, G, B] values.

### Accessing RGB Values

```python exec
id: part-3-rgb-encoding-3
# Create a small RGB image
height, width = 2, 3
rgb_image = np.zeros((height, width, 3), dtype=np.uint8)

# Set some colors
rgb_image[0, 0] = [255, 0, 0]     # Top-left: red
rgb_image[0, 1] = [0, 255, 0]     # Top-middle: green
rgb_image[0, 2] = [0, 0, 255]     # Top-right: blue
rgb_image[1, 0] = [255, 255, 0]   # Bottom-left: yellow
rgb_image[1, 1] = [255, 0, 255]   # Bottom-middle: magenta
rgb_image[1, 2] = [0, 255, 255]   # Bottom-right: cyan

print('RGB image shape:', rgb_image.shape)
print('\nPixel at [0,0] (red):', rgb_image[0, 0])
print('Pixel at [0,1] (green):', rgb_image[0, 1])
print('Pixel at [1,1] (magenta):', rgb_image[1, 1])

# Display
plt.imshow(rgb_image)
plt.title('2×3 RGB Image')
plt.axis('off')
plt.show()
```

---

## Section 3: Encoding Text as RGB

### The Perfect Match: Trigrams!

**Key insight:** One trigram = three letters = THREE values = perfect for RGB!

- Letter 1 → Red channel
- Letter 2 → Green channel
- Letter 3 → Blue channel

**Example:** "THE"
- T (84) → Red = 168
- H (72) → Green = 144
- E (69) → Blue = 138
- Color: (168, 144, 138) = brownish-gray

### Implementation

```python exec
id: part-3-rgb-encoding-4
def text_to_rgb_image(text, width, height):
    """
    Encode text as RGB image using trigrams.
    
    Each pixel encodes 3 letters!
    
    Parameters:
    -----------
    text : str
        Text to encode
    width : int
        Image width in pixels
    height : int
        Image height in pixels
    
    Returns:
    --------
    numpy.ndarray : RGB image array (height, width, 3)
    """
    # Keep only letters, uppercase
    letters = ''.join(c.upper() for c in text if c.isalpha())
    
    # We need 3 letters per pixel
    needed = width * height * 3
    
    # Pad with spaces if needed
    while len(letters) < needed:
        letters += ' '
    
    # Truncate if too long
    letters = letters[:needed]
    
    # Convert to ASCII values, scale to 0-255
    values = [min(ord(c) * 2, 255) for c in letters]
    
    # Reshape to (height, width, 3)
    rgb_array = np.array(values, dtype=np.uint8).reshape(height, width, 3)
    
    return rgb_array

# Test
message = "HELLO WORLD THIS IS A SECRET MESSAGE"
img = text_to_rgb_image(message, width=4, height=3)

print(f'Message: {message}')
print(f'Image shape: {img.shape}')
print(f'Encodes {img.shape[0] * img.shape[1] * 3} letters')

plt.imshow(img)
plt.title(f'RGB Encoding: {message[:20]}...')
plt.axis('off')
plt.show()
```

---

## Section 4: Efficiency Comparison

### Grayscale vs RGB

**Grayscale:**
- 1 letter per pixel
- 10×10 image = 100 letters

**RGB:**
- 3 letters per pixel
- 10×10 image = 300 letters
- **3× more efficient!**

### Information Density

```python exec
id: part-3-rgb-encoding-5
def compare_efficiency(text_length):
    """Compare grayscale vs RGB efficiency"""
    # Grayscale: 1 letter per pixel
    gray_pixels = text_length
    gray_width = int(np.ceil(np.sqrt(gray_pixels)))
    gray_height = int(np.ceil(gray_pixels / gray_width))
    gray_total = gray_width * gray_height
    
    # RGB: 3 letters per pixel
    rgb_pixels = int(np.ceil(text_length / 3))
    rgb_width = int(np.ceil(np.sqrt(rgb_pixels)))
    rgb_height = int(np.ceil(rgb_pixels / rgb_width))
    rgb_total = rgb_width * rgb_height
    
    print(f'Text length: {text_length} letters')
    print(f'\nGrayscale:')
    print(f'  Dimensions: {gray_width}×{gray_height}')
    print(f'  Total pixels: {gray_total}')
    print(f'\nRGB:')
    print(f'  Dimensions: {rgb_width}×{rgb_height}')
    print(f'  Total pixels: {rgb_total}')
    print(f'\nEfficiency gain: {gray_total / rgb_total:.2f}× fewer pixels with RGB')

# Test with different message lengths
for length in [100, 500, 1000]:
    compare_efficiency(length)
    print('\n' + '-'*60 + '\n')
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

1. **RGB Color Model**
 - Three channels: Red, Green, Blue
 - Each channel: 0-255
 - Mixing creates all colors
 - Matches human vision

2. **Three-Channel Arrays**
 - 3D structure: (height, width, 3)
 - Accessing: image[row, col] gives [R, G, B]
 - Natural extension of 2D arrays

3. **Trigram-to-RGB Mapping**
 - Perfect fit: 3 letters = 3 channels
 - Each pixel encodes 3 letters
 - Natural and efficient

4. **Efficiency**
 - RGB: 3× more efficient than grayscale
 - Smaller images for same text
 - More aesthetic possibilities

5. **Creative Applications**
 - Beautiful colorful encodings
 - Artistic data visualization
 - Steganography opportunities

### Skills Gained

 Working with RGB color model
 Creating and manipulating 3D arrays
 Efficient information encoding
 Calculating encoding efficiency
 Understanding color spaces

### Looking Ahead: Part 4

We've encoded visible messages in images. But what about **hidden** messages?

In **Part 4: Detecting Hidden Messages**, we'll learn:
- LSB (Least Significant Bit) steganography
- How to hide messages invisibly
- Statistical methods to detect hidden data
- Digital forensics applications
- Media authenticity verification

---

## Exercises

### Your turn 1: Color Exploration

Create a function that generates all possible colors where each RGB value is a multiple of 64. How many colors is that? Visualize them in a grid.

### Your turn 2: Efficiency Calculator

Write a function that determines the smallest square image (both grayscale and RGB) needed to encode any given text. Compare the pixel counts.

### Try this: Aesthetic Encoding

Create text that produces an aesthetically pleasing RGB image. Can you make a gradient? A pattern? Share your most beautiful encoding!

---

## Additional Resources

### Color Theory
- [RGB Color Model](https://en.wikipedia.org/wiki/RGB_color_model)
- [Color Spaces](https://en.wikipedia.org/wiki/Color_space)
- [Digital Color](https://www.cambridgeincolour.com/tutorials/color-spaces.htm)

### Image Processing
- [Digital Image Basics](https://en.wikipedia.org/wiki/Digital_image)
- [Image File Formats](https://en.wikipedia.org/wiki/Image_file_formats)

---


You've completed Part 3! You now understand:
- The RGB color model and how it works
- Three-dimensional array structures
- Encoding text efficiently using three channels
- The beautiful connection between trigrams and RGB

You've seen how the same concepts (character encoding, arrays, patterns) extend to richer representations!

**Next:** Part 4 - Detecting Hidden Messages

Ready to learn about invisible information? Let's explore steganography!
