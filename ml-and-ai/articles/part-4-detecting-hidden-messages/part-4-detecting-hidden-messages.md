---
title: "Hidden in Plain Sight: Part 4"
slug: part-4-detecting-hidden-messages
course: ai-and-ml-foundations
course_title: "AI and ML Foundations"
series: 6-projects-hidden-in-plain-sight
series_title: "Projects / Hidden in Plain Sight"
version: 2026.09.06.1
---

# Hidden in Plain Sight: Part 4
## Detecting Hidden Messages

## Welcome to Part 4!In Parts 1-3, you created **visible** encodings - anyone could see there's a message in the image.Now we explore **steganography** - hiding messages so they're invisible! And more importantly: how to DETECT hidden messages.This is brand new content applying everything you've learned to modern digital forensics and media literacy.

### What You'll Learn1. **Steganography vs Cryptography**: Hiding vs scrambling2. **LSB Encoding**: Hiding data in the least significant bit3. **Statistical Detection**: Finding hidden messages4. **Chi-Squared Application**: Using your Part 2a knowledge!5. **Real-World Applications**: Digital forensics, watermarking, authentication

### Why This MattersIn our digital age:- **Journalists** verify image authenticity- **Forensic analysts** detect hidden information- **Content creators** protect intellectual property with watermarks- **Citizens** need media literacy to spot manipulated imagesUnderstanding steganography detection helps you become a critical consumer of digital media.

### Historical and Modern Context

Steganography has peaceful applications:- **Copyright protection**: Invisible watermarks prove ownership- **Authentication**: Verify image hasn't been tampered with- **Privacy**: Journalists protecting sensitive sources- **Anti-counterfeiting**: Hidden marks in currency and documentsToday, with AI-generated images and deepfakes spreading, the ability to detect hidden information or manipulation is more important than ever.### Prerequisites- Parts 1-3 completed (especially chi-squared from Part 2a!)- Understanding of binary representation helpful- Critical thinking about digital media

```python exec
id: part-4-detecting-hidden-messages-1
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
plt.rcParams['figure.figsize'] = (12, 6)
plt.rcParams['font.size'] = 11
print('Libraries loaded!')
print('Ready to detect hidden messages.')
```

---

## Section 1: Steganography vs Cryptography

### Two Different Approaches

**Cryptography:**
- Makes message UNREADABLE
- Everyone knows message exists
- Example: Caesar cipher - "HELLO" → "KHOOR"
- Obvious something is hidden

**Steganography:**
- Makes message INVISIBLE
- Nobody knows message exists
- Example: Message hidden in image pixels
- Looks like normal image

**Best security:** Combine both!
- Encrypt message (cryptography)
- Hide encrypted message (steganography)
- Even if found, still unreadable

### Historical Examples

**Ancient:**
- Invisible inks (lemon juice, milk)
- Messages tattooed on shaved heads, hair regrown
- Wax tablets with hidden layers

**Modern:**
- Digital watermarks in images
- Data hidden in audio files
- Messages in video frames
- Metadata in documents

---
## Section 2: LSB Steganography

### What is LSB?

**LSB** = **L**east **S**ignificant **B**it

Every pixel value is stored in binary. For a grayscale value:

```
Value 156 in binary: 10011100
                     ^^^^^^^^                     
                     |||||||└─ LSB (least significant)
                     ||||||└── 2nd bit
                     ...continues ...
                     └──────── MSB (most significant)
```

**Key insight:** Changing the LSB barely affects the value!

```
156 = 10011100  (even number)
157 = 10011101  (odd number, LSB changed)
```

Visual difference? Almost invisible!
(156 and 157 are nearly identical shades)
### Hiding Data in LSBs

**Strategy:**
1. Take your secret message bits
2. Replace LSBs of image pixels with message bits
3. Image looks almost identical
4. But now contains hidden message!

**Capacity:**
One bit per pixel
- 100×100 grayscale image = 10,000 pixels = 10,000 bits ~ 1,250 bytes
- Can hide about 1KB of text!

```python exec
id: part-4-detecting-hidden-messages-2
def text_to_bits(text):
    """Convert text to binary string"""
    bits = ''
    for char in text:
        # Get ASCII value, convert to 8-bit binary
        bits += format(ord(char), '08b')
    return bits

def bits_to_text(bits):
    """Convert binary string back to text"""
    chars = []
    for i in range(0, len(bits), 8):
        byte = bits[i:i+8]
        if len(byte) == 8:
            chars.append(chr(int(byte, 2)))
    return ''.join(chars)

# Demonstrate the conversion functions
message = "SECRET"
bits = text_to_bits(message)
print(f'Message: {message}')
print(f'As bits: {bits}')
print(f'Length: {len(bits)} bits')
print(f'\nRecovered: {bits_to_text(bits)}')
```

```python exec
id: part-4-detecting-hidden-messages-3
def hide_message_lsb(image, message):
    """
    Hide message in image using LSB steganography.

    Parameters:
    -----------
    image : numpy.ndarray
        Original image (grayscale).
    message : str
        Message to hide.

    Returns:
    --------
    numpy.ndarray : Image with the hidden message.
    """
    # Convert the message string into a binary string of 0s and 1s
    bits = text_to_bits(message)

    # Calculate the maximum number of bits that can be hidden in the image
    max_bits = image.shape[0] * image.shape[1]

    # Check if the message is too long to fit in the image
    if len(bits) > max_bits:
        raise ValueError(f'Message too long! Need {len(bits)} bits, but image has {max_bits} pixels to hide in.')

    # Create a copy of the original image to avoid modifying it directly
    stego_image = image.copy()

    # Flatten the image array to easily iterate through pixels
    flat = stego_image.flatten()

    # Iterate through the message bits and replace the LSB of each pixel
    for i, bit in enumerate(bits):
        # Clear the current LSB (making it 0) and then set it to the message bit
        # (flat[i] & ~1) clears the LSB
        # | int(bit) sets the LSB to the value of the message bit
        flat[i] = (flat[i] & ~1) | int(bit)

    # Reshape the flattened array back to the original image dimensions
    return flat.reshape(image.shape)

# --- Test the LSB hiding function --- #

# Create a sample grayscale image with random pixel values
original = np.random.randint(100, 200, (20, 20), dtype=np.uint8)
secret_msg = "HI"

# Hide the message in the original image
stego = hide_message_lsb(original, secret_msg)

# --- Display the results --- #

# Set up a figure with three subplots for comparison
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(15, 5))

# Display the original image
ax1.imshow(original, cmap='gray', vmin=0, vmax=255)
ax1.set_title('Original Image')
ax1.axis('off')

# Display the image with the hidden message
ax2.imshow(stego, cmap='gray', vmin=0, vmax=255)
ax2.set_title('With Hidden Message')
ax2.axis('off')

# Calculate and display the difference between the original and stego image
# The difference is amplified (multiplied by 255) for better visibility
diff = np.abs(original.astype(int) - stego.astype(int)) * 255
ax3.imshow(diff, cmap='hot', vmin=0, vmax=255)
ax3.set_title('Difference (amplified)')
ax3.axis('off')

plt.tight_layout()
plt.show()

# Print information about the hidden message and the maximum pixel difference
print(f'Hidden message: "{secret_msg}"')
print(f'Max difference: {np.max(np.abs(original - stego))}')
print('Almost invisible!')
```

---
## Section 3: Detecting Hidden Messages

### The ChallengeHow can we tell if an image contains a hidden message?**Key observation:

** Natural images have specific statistical properties. Hiding data disrupts these properties.

### LSB AnalysisIn natural images:

- LSBs appear random- Roughly equal 0s and 1s
- No obvious patternsWith hidden message:
- LSBs follow message structure
- May not be evenly distributed
- Detectable with statistics!
### Chi-Squared Test Returns!
Remember chi-squared from Part 2a? We use it here too!

**For natural images:**
- Expect ~50% zeros in LSBs
- Expect ~50% ones in LSBs

**With hidden data:**- Distribution may skew- Chi-squared will be higher!

```python exec
id: part-4-detecting-hidden-messages-4
def detect_lsb_steganography(image):
    """
    Detect possible LSB steganography using statistical test.

    Returns:
    --------
    tuple : (verdict, chi_squared_value)
    """
    # Extract LSBs
    lsbs = image.flatten() & 1

    # Count 0s and 1s
    zeros = np.sum(lsbs == 0)
    ones = np.sum(lsbs == 1)
    total = len(lsbs)

    # Natural images: expect 50/50 split
    expected = total / 2

    # Chi-squared test
    chi_sq = ((zeros - expected)**2 / expected +
               (ones - expected)**2 / expected)

    # Interpretation (threshold at 95% confidence for 1 degree of freedom)
    # The critical value for a chi-squared distribution with 1 degree of freedom
    # at a 95% confidence level is approximately 3.84.
    threshold = 3.84

    if chi_sq < threshold:
        verdict = "No hidden message detected"
    else:
        verdict = "Possible hidden message!"

    return verdict, chi_sq

# Test the detection function on our sample images
print('Original image:')
verdict1, chi1 = detect_lsb_steganography(original)
print(f'  {verdict1}')
print(f'  Chi-squared: {chi1:.2f}')

print('\nImage with hidden message:')
verdict2, chi2 = detect_lsb_steganography(stego)
print(f'  {verdict2}')
print(f'  Chi-squared: {chi2:.2f}')

print('\nNotice how chi-squared increases when message is hidden!')
```

---

## Section 4: Real-World Applications

### Digital Forensics

**Use cases:**
- Detecting hidden communications
- Finding embedded data in evidence
- Verifying image authenticity
- Identifying tampering

### Media Authentication

**Applications:**
- Journalists verifying image sources
- Detecting manipulated photos
- Identifying AI-generated content
- Copyright enforcement

### Watermarking

**Benefits:**
- Prove ownership of digital content
- Track unauthorized copying
- Invisible copyright notices
- Authentication without visible marks

### Ethical Considerations

**Important questions:**
- When is hiding data legitimate?
- Privacy vs security concerns
- Responsible disclosure
- Legal implications

**Best practices:**
- Use for legitimate purposes only
- Respect privacy and consent
- Follow applicable laws
- Consider ethical implications

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
1. **Steganography** - Hiding vs scrambling information - LSB method for hiding data - Capacity and limitations - Historical and modern applications
2. **Detection Methods** - Statistical analysis of LSBs - Chi-squared test (applied from Part 2a!) - Natural image properties - Identifying anomalies
3. **Real-World Skills** - Digital forensics basics - Media authentication - Critical evaluation of images - Understanding watermarking
4. **Ethical Framework** - Legitimate uses of steganography - Privacy considerations - Responsible technology use - Legal and ethical boundaries

### Skills Gained Implementing LSB steganography Statistical detection of hidden data Applying chi-squared in new context Critical thinking about digital media Understanding forensics basics Media literacy skills

### Series Complete!

You've completed all 4 parts of Hidden in Plain Sight! You now understand:

**Part 1:** Character encoding, 2D arrays, grayscale images

**Part 2a:** Frequency analysis, chi-squared testing, breaking Caesar ciphers

**Part 2b:** N-grams, sliding windows, pattern persistence

**Part 3:** RGB encoding, three-channel arrays, efficiency

**Part 4:** Steganography, detection, digital forensicsYou've gained skills in:
- **Programming:** Functions, arrays, data structures
- **Mathematics:** Statistics, chi-squared, probability
- **Critical Thinking:** Pattern recognition, problem solving
- **Media Literacy:** Evaluating digital content

### What's Next?

**Continue learning:**
- Explore modern encryption (AES, RSA)
- Study machine learning for image analysis
- Investigate blockchain and cryptographic hashing
- Learn about quantum cryptography

**Apply your skills:**
- Create your own encoding schemes
- Build detection tools
- Contribute to open source projects
- Share knowledge with others---

## Final Exercises

### Your turn 1: Complete System

Build a complete steganography system with:
- Message hiding
- Message extraction
- Detection capability
- User interface

### Your turn 2: Comparison Study

Compare LSB steganography with other methods. Research and implement one alternative technique.

### Try this: Robust Detection

Create a detection system that works on various image types and sizes. Test against different hiding methods.---

## Additional Resources

### Steganography
- [Introduction to Steganography](https://en.wikipedia.org/wiki/Steganography)
- [Digital Watermarking](https://en.wikipedia.org/wiki/Digital_watermarking)
- [Steganalysis](https://en.wikipedia.org/wiki/Steganalysis)

### Digital Forensics
- [Computer Forensics Basics](https://en.wikipedia.org/wiki/Digital_forensics)
- [Image Forensics](https://en.wikipedia.org/wiki/Image_forensics)

### Media Literacy
- [Evaluating Digital Content](https://www.commonsense.org/education/digital-citizenship)
- [Detecting Deepfakes](https://www.media.mit.edu/projects/detect-fakes/overview/)---


You've completed the entire Hidden in Plain Sight tutorial series!

You've journeyed from basic character encoding to sophisticated steganography detection. Along the way, you've:
- Built practical tools
- Developed critical thinking
- Learned statistical methods
- Gained media literacy skills
- Understood ethical implications**These skills will serve you well** in computer science, data analysis, digital citizenship, and beyond.

Thank you for your dedication and curiosity. Keep exploring, keep learning, and use your knowledge responsibly!

**End of Series**
