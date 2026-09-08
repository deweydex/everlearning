---
title: "part-1-greyscale-encoding-page-3 (3 of 3)"
slug: part-1-greyscale-encoding-page-3
course: ai-and-ml-foundations
course_title: "AI and ML Foundations"
series: 6-projects-hidden-in-plain-sight
series_title: "Projects / Hidden in Plain Sight"
version: 2026.09.06.1
---

Before starting this page, run the cell below. It repeats the imports and definitions from the earlier pages that this page uses.

```python exec
id: part-1-greyscale-encoding-page-3-setup
import numpy as np
import matplotlib.pyplot as plt
```

---

## Summary and Key Takeaways

### What You've Learned

1. **Character Encoding**
 - Computers represent characters as numbers using ASCII/Unicode
 - `ord()` converts character → number
 - `chr()` converts number → character

2. **2D Arrays** (Critical Understanding!)
 - Images are 2D arrays with rows and columns
 - Access elements with `array[row][column]`
 - Converting 1D text to 2D image requires reshaping

3. **Grayscale Encoding**
 - Grayscale values range from 0 (black) to 255 (white)
 - Each character maps to a unique shade
 - Scaling helps use the full range of values

4. **Encoding Process**
 - Text → ASCII values → Grayscale values → 2D array → Image
 - Padding handles size mismatches
 - matplotlib displays the result

5. **Decoding Process**
 - Image → Flatten to 1D → Reverse scaling → ASCII values → Text
 - Reversible transformation (no information lost)

6. **Patterns and Limitations**
 - Repeated letters create visible patterns
 - Not cryptographically secure
 - Image size determines message capacity

### Skills Gained

 Working with character encodings
 Understanding and creating 2D arrays
 Converting between different data representations
 Using numpy for array operations
 Using matplotlib for visualization
 Implementing encoding/decoding algorithms
 Debugging transformation errors

### Looking Ahead: Part 2

In **Part 2a**, we'll explore:
- Why those visible patterns matter
- Letter frequency analysis in natural language
- How to detect and break simple ciphers
- Statistical thinking for pattern recognition

The patterns we saw in our encoded images are the foundation for cryptanalysis!

---

## Exercises and Challenges

### Your turn 1: Different Scaling Factors

We multiplied ASCII values by 2. What if we used different scaling?

Modify the `char_to_grayscale()` function to try:
- Multiplying by 1 (no scaling)
- Multiplying by 3
- Using the formula: `(ascii_val - 32) * (255 / 95)` to spread printable characters across full range

How does each affect the image appearance?

```python exec
id: part-1-greyscale-encoding-page-3-1
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
# Your code here
```

### Your turn 2: Image Dimensions

Encode the same message with three different dimensions:
1. Very wide (width=20, height=2)
2. Square (width=10, height=10)
3. Tall (width=2, height=20)

Compare the visual appearance. Which is easier to "read" visually?

```python exec
id: part-1-greyscale-encoding-page-3-2
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
# Your code here
```

### Your turn 3: Pattern Creation

Can you create text that produces:
1. A striped pattern (alternating light and dark)
2. A gradient (gradually getting lighter or darker)
3. A checkerboard pattern

Hint: Use letters with different ASCII values to create contrast.

```python exec
id: part-1-greyscale-encoding-page-3-3
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
# Your code here
```

### Try this: Error Detection

If one pixel value in the image gets corrupted (changed), can you detect it during decoding?

Create a function that:
1. Encodes a message
2. Randomly changes one pixel value
3. Decodes and compares to original
4. Reports which character was affected

```python exec
id: part-1-greyscale-encoding-page-3-4
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
# Your code here
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

## Additional Resources

### Character Encoding
- [ASCII Table and History](https://www.asciitable.com/)
- [Unicode Basics](https://unicode.org/standard/tutorial-info.html)
- [Character Encoding Guide](https://www.joelonsoftware.com/2003/10/08/the-absolute-minimum-every-software-developer-absolutely-positively-must-know-about-unicode-and-character-sets-no-excuses/)

### Image Processing
- [Digital Image Basics](https://en.wikipedia.org/wiki/Digital_image)
- [Grayscale Images Explained](https://en.wikipedia.org/wiki/Grayscale)
- [Matplotlib Image Tutorial](https://matplotlib.org/stable/tutorials/introductory/images.html)

### Python and NumPy
- [NumPy Array Basics](https://numpy.org/doc/stable/user/absolute_beginners.html)
- [NumPy Reshaping Arrays](https://numpy.org/doc/stable/reference/generated/numpy.reshape.html)
- [Python ord() and chr()](https://docs.python.org/3/library/functions.html)

### Related Topics
- [Steganography Introduction](https://en.wikipedia.org/wiki/Steganography)
- [Data Representation](https://en.wikipedia.org/wiki/Data_(computing))
- [Information Theory Basics](https://en.wikipedia.org/wiki/Information_theory)

---


You've completed Part 1 of the Hidden in Plain Sight tutorial series. You now understand how to:
- Convert text to numbers and back
- Work with 2D arrays for image data
- Encode text as grayscale images
- Decode images back to text

These foundational concepts will be essential as we move forward to explore frequency analysis, pattern recognition, and more sophisticated encoding schemes.

**Next:** Part 2a - Frequency Analysis and Caesar Ciphers

Ready to continue? Let's explore why those patterns we saw matter!
