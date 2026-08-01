# MIT 3.3: Defining and Graphing Trigonometric Functions

> **Learning outcome:** MIT 5N18396, Section 3 (Functions & Calculus) — 3.3 (define and graph simple trigonometric functions). This is an explicit, direct match: amplitude, period, phase shift and vertical shift are exactly the transformation vocabulary the LO calls for.
> **Pulled in from:** `mathematics` repo, `markdown/worksheet_05c_graphs_sine_cosine.md`
> **Teaching method:** Pen-and-paper exercises, with real-world science tie-ins (sound, radio, tides, circadian rhythms)
> **Pairs with:** [`MIT-4.5-4.7_Radians-and-the-Unit-Circle.md`](./MIT-4.5-4.7_Radians-and-the-Unit-Circle.md) (definitions) and [`MIT-4.4_4.9_Right-Triangle-Trigonometry.md`](./MIT-4.4_4.9_Right-Triangle-Trigonometry.md)

---

**AIML Foundations Mathematics — Worksheet 5C: Graphs of Sine and Cosine**

> **What This Worksheet Is About**
>
> Sine and cosine don't just solve triangles — they describe anything that oscillates, cycles, or waves. Sound, light, electricity, ocean tides, seasonal temperatures, and even the vibration of atoms all follow sinusoidal patterns.
>
> Understanding how to read and manipulate these graphs is essential for signal processing, communications, and the Fourier analysis that underlies much of modern technology.

---

## Part A: The Basic Sine and Cosine Curves (16 problems)

### The Parent Functions

$$y = \sin(x) \quad \text{and} \quad y = \cos(x)$$

**Key Properties:**
- **Period:** $2\pi$ (one complete cycle)
- **Amplitude:** 1 (distance from center to peak)
- **Range:** $[-1, 1]$
- **Domain:** All real numbers

**The only difference:** Cosine is sine shifted left by $\frac{\pi}{2}$:
$$\cos(x) = \sin\left(x + \frac{\pi}{2}\right)$$

---

**1.** Complete the table for $y = \sin(x)$:

| $x$ | $0$ | $\frac{\pi}{6}$ | $\frac{\pi}{4}$ | $\frac{\pi}{3}$ | $\frac{\pi}{2}$ | $\pi$ | $\frac{3\pi}{2}$ | $2\pi$ |
|-----|-----|-----------------|-----------------|-----------------|-----------------|-------|------------------|--------|
| $\sin(x)$ | | | | | | | | |

**2.** Complete the table for $y = \cos(x)$:

| $x$ | $0$ | $\frac{\pi}{6}$ | $\frac{\pi}{4}$ | $\frac{\pi}{3}$ | $\frac{\pi}{2}$ | $\pi$ | $\frac{3\pi}{2}$ | $2\pi$ |
|-----|-----|-----------------|-----------------|-----------------|-----------------|-------|------------------|--------|
| $\cos(x)$ | | | | | | | | |

**3.** Sketch both functions on the same axes from $x = 0$ to $x = 2\pi$.

**4.** At what x-values does $\sin(x) = \cos(x)$ in the interval $[0, 2\pi]$?

**5.** At what x-values does $\sin(x) = 0$ in the interval $[0, 2\pi]$?

**6.** At what x-values does $\cos(x) = 0$ in the interval $[0, 2\pi]$?

**7.** At what x-value does $\sin(x)$ reach its maximum in $[0, 2\pi]$? Its minimum?

**8.** At what x-value does $\cos(x)$ reach its maximum in $[0, 2\pi]$? Its minimum?

---

### Symmetry

**9.** $\sin(-x) = $ \_\_\_\_\_\_\_\_\_\_ (Sine is an **odd** function)

**10.** $\cos(-x) = $ \_\_\_\_\_\_\_\_\_\_ (Cosine is an **even** function)

**11.** Verify: $\sin(-\frac{\pi}{4}) = -\sin(\frac{\pi}{4})$

**12.** Verify: $\cos(-\frac{\pi}{3}) = \cos(\frac{\pi}{3})$

---

**🎵 Science Connection: Sound Waves**

**13.** A pure musical tone is a sine wave. The note "A" above middle C has a frequency of 440 Hz (cycles per second).
- (a) What is the period of this sound wave in seconds?
- (b) How many complete cycles occur in 1 second?

**14.** The equation for this sound wave (simplified) is:
$$y(t) = A\sin(2\pi \cdot 440 \cdot t)$$
where $t$ is time in seconds and $A$ is amplitude.

At $t = 0$, what is $y(0)$?

**15.** At $t = \frac{1}{880}$ seconds, what is $y(t)$?

**16.** At what time does the first peak occur?

---

## Part B: Amplitude — Vertical Stretch (14 problems)

### The General Form

$$y = A\sin(x) \quad \text{or} \quad y = A\cos(x)$$

**Amplitude** $= |A|$ (the distance from the midline to the peak)

- If $A > 1$: vertical stretch (taller waves)
- If $0 < A < 1$: vertical compression (shorter waves)
- If $A < 0$: reflection across the x-axis

---

**Identify the amplitude and sketch one period:**

**17.** $y = 3\sin(x)$

**18.** $y = 0.5\cos(x)$

**19.** $y = -2\sin(x)$

**20.** $y = -\cos(x)$

---

**Write the equation of a sine function with:**

**21.** Amplitude 4, no other transformations.

**22.** Amplitude $\frac{1}{3}$, reflected across the x-axis.

---

**🔊 Science Connection: Sound Intensity**

**23.** A quiet whisper might have amplitude 0.01 (in arbitrary units), while a loud shout might have amplitude 1.0.

If quiet sound is $y = 0.01\sin(x)$ and loud sound is $y = 1.0\sin(x)$:
- (a) How many times larger is the amplitude of the shout?
- (b) Sound intensity is proportional to amplitude squared. How many times more intense is the shout?

**24.** Noise-canceling headphones work by generating a sound wave that is the **negative** of the incoming noise.

If noise is $y = A\sin(x)$, what wave cancels it?

---

**🔬 Science Connection: Light Waves**

**25.** Light is an electromagnetic wave. The electric field oscillates as a sine wave.

If blue light has a smaller amplitude than red light (same intensity), which has:
- (a) More energy per photon? (Hint: This depends on frequency, not amplitude)
- (b) More photons for the same total energy?

**26.** In interference experiments, two waves can:
- Add constructively (peaks align): $\sin(x) + \sin(x) = 2\sin(x)$
- Add destructively (peaks align with troughs): $\sin(x) + \sin(x + \pi) = 0$

Verify the destructive case: $\sin(x) + \sin(x + \pi) = \sin(x) + (-\sin(x)) = 0$ ✓

---

**📻 Science Connection: Radio Waves**

**27.** AM radio (Amplitude Modulation) encodes information by varying the amplitude of a carrier wave.

The carrier might be $y = \sin(1000000 \cdot 2\pi t)$ (1 MHz).

When you speak, the amplitude changes: $y = A(t)\sin(1000000 \cdot 2\pi t)$

If $A(t)$ varies between 0.5 and 1.5, what are the minimum and maximum peak heights of the signal?

---

## Part C: Period — Horizontal Stretch/Compression (18 problems)

### The General Form

$$y = \sin(Bx) \quad \text{or} \quad y = \cos(Bx)$$

**Period** $= \frac{2\pi}{|B|}$

- If $B > 1$: horizontal compression (faster oscillation, shorter period)
- If $0 < B < 1$: horizontal stretch (slower oscillation, longer period)

**Frequency** $= \frac{|B|}{2\pi} = \frac{1}{\text{Period}}$ (cycles per unit)

---

**Find the period:**

**28.** $y = \sin(2x)$

**29.** $y = \cos(3x)$

**30.** $y = \sin\left(\frac{x}{2}\right)$

**31.** $y = \cos(4\pi x)$

**32.** $y = \sin\left(\frac{\pi x}{3}\right)$

---

**Find B if the period is:**

**33.** Period $= \pi$

**34.** Period $= 4\pi$

**35.** Period $= 1$ (useful for time in seconds!)

**36.** Period $= \frac{1}{60}$ (one cycle per minute)

---

**🎵 Science Connection: Musical Frequencies**

**37.** Middle C has frequency 261.6 Hz.
- (a) What is the period in seconds?
- (b) Write the equation for this sound wave: $y = \sin(Bt)$ where the period is in seconds.

**38.** An octave higher means double the frequency. What is the frequency of C one octave above middle C?

**39.** The note E above middle C has frequency 329.6 Hz.
- (a) Write the equation.
- (b) If you play both C and E together, what mathematical operation combines them?

---

**📡 Science Connection: Radio Frequencies**

**40.** FM radio station 98.5 FM broadcasts at 98.5 MHz (megahertz = million Hz).
- (a) What is the period of this electromagnetic wave?
- (b) How does this compare to AM radio at 1 MHz?

**41.** Wi-Fi operates at either 2.4 GHz or 5 GHz (gigahertz = billion Hz).
- (a) What is the period of a 2.4 GHz wave?
- (b) What is the period of a 5 GHz wave?
- (c) Which has more cycles per second?

---

**🔬 Science Connection: X-rays and Visible Light**

**42.** Visible light has frequencies around $5 \times 10^{14}$ Hz (500 THz).
- (a) What is the period?
- (b) Light travels at $c = 3 \times 10^8$ m/s. Wavelength $\lambda = c \cdot T$ where $T$ is period. Find the wavelength.

**43.** X-rays have frequencies around $10^{18}$ Hz.
- (a) What is the period?
- (b) What is the wavelength?
- (c) Why can X-rays "see" smaller features than visible light?

---

**🔬 Science Connection: EUV Lithography**

**44.** Extreme ultraviolet (EUV) light used in chip manufacturing has wavelength 13.5 nm.
- (a) Convert to meters.
- (b) Using $\lambda = c \cdot T$, find the period.
- (c) Find the frequency.

**45.** The light in EUV lithography can be modeled as $E(t) = E_0\sin(2\pi f t)$. With $f$ from problem 44:
- (a) What is $B$ in $E(t) = E_0\sin(Bt)$?
- (b) This is an incredibly large number! What does this tell you about how fast the electric field oscillates?

---

## Part D: Phase Shift — Horizontal Translation (14 problems)

### The General Form

$$y = \sin(x - C) \quad \text{or} \quad y = \cos(x - C)$$

**Phase shift** $= C$ (shifts right if $C > 0$, left if $C < 0$)

Note: In $y = \sin(Bx - C)$, the phase shift is $\frac{C}{B}$, not $C$!

---

**Identify the phase shift:**

**46.** $y = \sin\left(x - \frac{\pi}{4}\right)$

**47.** $y = \cos\left(x + \frac{\pi}{3}\right)$

**48.** $y = \sin(2x - \pi)$ — *Careful! Factor out B first.*

**49.** $y = \cos\left(3x + \frac{\pi}{2}\right)$

---

**Write the equation:**

**50.** Sine function shifted right by $\frac{\pi}{6}$.

**51.** Cosine function shifted left by $\frac{\pi}{4}$.

**52.** Sine function with period $\pi$ and phase shift $\frac{\pi}{4}$ to the right.

---

**🔌 Science Connection: AC Electricity**

**53.** In three-phase electrical power, three sine waves are used, each shifted by 120° (or $\frac{2\pi}{3}$ radians):

$$V_1 = V_0\sin(\omega t)$$
$$V_2 = V_0\sin\left(\omega t - \frac{2\pi}{3}\right)$$
$$V_3 = V_0\sin\left(\omega t - \frac{4\pi}{3}\right)$$

At $t = 0$, calculate $V_1$, $V_2$, and $V_3$ in terms of $V_0$.

**54.** Show that $V_1 + V_2 + V_3 = 0$ at $t = 0$.

*This is always true! The three phases always sum to zero, which is important for power transmission.*

---

**📻 Science Connection: Signal Phase**

**55.** GPS works by comparing the phase of signals from multiple satellites. If two satellites send identical sine waves but one signal travels farther:

Satellite A: $y_A = \sin(\omega t)$
Satellite B: $y_B = \sin(\omega t - \phi)$

If the phase difference $\phi = \frac{\pi}{2}$ and the wave has frequency 1.575 GHz, how much extra time did signal B take?

*Hint: Phase difference $\phi$ corresponds to time difference $\Delta t = \frac{\phi}{\omega} = \frac{\phi}{2\pi f}$*

**56.** At the speed of light ($3 \times 10^8$ m/s), what extra distance did signal B travel?

---

**🔬 Science Connection: Interference in Thin Films**

**57.** When light reflects off a thin film (like oil on water), the two reflections (top and bottom of film) can interfere.

If the film thickness causes a phase shift of $\phi = \pi$, what happens when the two waves combine?

**58.** At what phase shift do you get constructive interference (bright colors)?

---

## Part E: Vertical Shift — Moving the Midline (10 problems)

### The General Form

$$y = \sin(x) + D \quad \text{or} \quad y = \cos(x) + D$$

**Vertical shift** $= D$ (midline moves to $y = D$)

**Range:** $[D - A, D + A]$ where $A$ is amplitude

---

**Identify amplitude, period, phase shift, and vertical shift:**

**59.** $y = 2\sin(x) + 3$

**60.** $y = -3\cos(2x) - 1$

**61.** $y = 4\sin\left(x - \frac{\pi}{2}\right) + 5$

**62.** $y = \frac{1}{2}\cos(4x + \pi) - 2$

---

**🌡️ Science Connection: Temperature Cycles**

**63.** Dublin's average daily temperature varies roughly sinusoidally through the year:
- Average: 10°C
- Varies by about ±5°C from the average
- Coldest around January 15, warmest around July 15

Let $t$ be days after January 1.

- (a) What is the amplitude?
- (b) What is the vertical shift (midline)?
- (c) What is the period?
- (d) Write an equation using cosine: $T(t) = A\cos(B(t - C)) + D$

*Hint: Use cosine with the coldest point as the "start" of the cycle.*

**64.** Using your equation:
- (a) What temperature does it predict for March 15 ($t = 73$)?
- (b) For June 1 ($t = 151$)?

---

**🌊 Science Connection: Tides**

**65.** Ocean tides follow roughly sinusoidal patterns (actually more complex due to Sun and Moon interactions).

A simplified model: High tide at midnight (12:00 AM) with height 3.2 m, low tide at 6:15 AM with height 0.8 m.

- (a) What is the amplitude?
- (b) What is the midline (average tide level)?
- (c) What is the period?
- (d) Write the equation using cosine.

---

**🔬 Science Connection: Circadian Rhythms**

**66.** Your body temperature varies throughout the day:
- Lowest around 4:00 AM: 36.2°C
- Highest around 4:00 PM: 37.4°C

- (a) What is the amplitude and midline?
- (b) Write an equation where $t$ is hours after midnight.
- (c) What is your predicted body temperature at 8:00 AM?

---

## Part F: The Complete General Form (10 problems)

### Putting It All Together

$$y = A\sin(B(x - C)) + D \quad \text{or} \quad y = A\cos(B(x - C)) + D$$

| Parameter | Effect |
|-----------|--------|
| $\|A\|$ | Amplitude (vertical stretch) |
| $A < 0$ | Reflection across midline |
| $\frac{2\pi}{\|B\|}$ | Period (horizontal stretch) |
| $C$ | Phase shift (horizontal translation) |
| $D$ | Vertical shift (midline) |

---

**For each function, identify all parameters and sketch:**

**67.** $y = 3\sin(2x - \pi) + 1$

**68.** $y = -2\cos\left(\frac{x}{2} + \frac{\pi}{4}\right) - 3$

---

**Write the equation given:**

**69.** Amplitude 5, period $4\pi$, phase shift $\frac{\pi}{2}$ right, midline $y = -2$, using sine.

**70.** Amplitude 2, period 1 (useful for signals!), no phase shift, midline $y = 3$, using cosine.

---

**🎵 Science Connection: Musical Synthesis**

**71.** A synthesizer creates complex sounds by adding sine waves. A simple "flute-like" tone might be:

$$y(t) = 1.0\sin(2\pi \cdot 440t) + 0.3\sin(2\pi \cdot 880t) + 0.1\sin(2\pi \cdot 1320t)$$

- (a) What are the three frequencies present?
- (b) What are the three amplitudes?
- (c) The first frequency is the "fundamental." What is the relationship between the other frequencies and the fundamental?

**72.** A square wave can be approximated by:

$$y(t) = \sin(t) + \frac{1}{3}\sin(3t) + \frac{1}{5}\sin(5t) + \frac{1}{7}\sin(7t) + \cdots$$

- (a) What pattern do you see in the frequencies?
- (b) What pattern do you see in the amplitudes?
- (c) This is a **Fourier series**! It shows any periodic wave can be built from sine waves.

---

**🔬 Science Connection: Quantum Mechanics Preview**

**73.** In quantum mechanics, a particle in a box has wave functions that are sine waves:

$$\psi_n(x) = A\sin\left(\frac{n\pi x}{L}\right)$$

where $L$ is the box length and $n = 1, 2, 3, ...$

- (a) What is the "period" of $\psi_1(x)$?
- (b) What is the "period" of $\psi_2(x)$?
- (c) How many half-wavelengths fit in the box for $\psi_n(x)$?

---

**📡 Science Connection: Sampling and Aliasing**

**74.** When digitizing a signal, you must sample at least twice per period (Nyquist theorem).

A signal has frequency 1000 Hz.
- (a) What is the minimum sampling rate needed?
- (b) If you sample at 800 Hz (too slow), the signal "aliases" to a lower frequency. The aliased frequency is $|f - f_s|$ where $f_s$ is the sample rate. What frequency would you hear?

**75.** CDs sample audio at 44,100 Hz.
- (a) What is the highest frequency that can be accurately recorded?
- (b) Why is this sufficient for human hearing (which goes up to about 20,000 Hz)?

**76.** A scientist digitizes a signal at 100 samples per second. She observes a frequency of 30 Hz in the data. Could the original signal actually have been 70 Hz? Explain.

---

## Answer Key

### Part A: Basic Curves
1. 0, $\frac{1}{2}$, $\frac{\sqrt{2}}{2}$, $\frac{\sqrt{3}}{2}$, 1, 0, -1, 0
2. 1, $\frac{\sqrt{3}}{2}$, $\frac{\sqrt{2}}{2}$, $\frac{1}{2}$, 0, -1, 0, 1
4. $x = \frac{\pi}{4}, \frac{5\pi}{4}$
5. $x = 0, \pi, 2\pi$
6. $x = \frac{\pi}{2}, \frac{3\pi}{2}$
7. Max at $\frac{\pi}{2}$, min at $\frac{3\pi}{2}$
8. Max at $0, 2\pi$, min at $\pi$
9. $-\sin(x)$
10. $\cos(x)$
13. (a) $\frac{1}{440}$ s ≈ 2.27 ms (b) 440
14. 0
15. 1
16. $t = \frac{1}{1760}$ s

### Part B: Amplitude
17. Amplitude = 3
18. Amplitude = 0.5
19. Amplitude = 2, reflected
20. Amplitude = 1, reflected
21. $y = 4\sin(x)$
22. $y = -\frac{1}{3}\sin(x)$
23. (a) 100 times (b) 10,000 times
24. $y = -A\sin(x)$
27. Min: 0.5, Max: 1.5

### Part C: Period
28. $\pi$
29. $\frac{2\pi}{3}$
30. $4\pi$
31. $\frac{1}{2}$
32. 6
33. $B = 2$
34. $B = \frac{1}{2}$
35. $B = 2\pi$
36. $B = 120\pi$
37. (a) 0.00382 s (b) $y = \sin(1643.5t)$
38. 523.2 Hz
40. (a) $1.02 \times 10^{-8}$ s (b) 98.5× shorter period
41. (a) $4.17 \times 10^{-10}$ s (b) $2 \times 10^{-10}$ s (c) 5 GHz
42. (a) $2 \times 10^{-15}$ s (b) 600 nm
43. (a) $10^{-18}$ s (b) 0.3 nm (c) Wavelength comparable to atomic spacing
44. (a) $1.35 \times 10^{-8}$ m (b) $4.5 \times 10^{-17}$ s (c) $2.22 \times 10^{16}$ Hz
45. (a) $1.40 \times 10^{17}$ rad/s

### Part D: Phase Shift
46. $\frac{\pi}{4}$ right
47. $\frac{\pi}{3}$ left
48. $\frac{\pi}{2}$ right
49. $\frac{\pi}{6}$ left
50. $y = \sin(x - \frac{\pi}{6})$
51. $y = \cos(x + \frac{\pi}{4})$
52. $y = \sin(2(x - \frac{\pi}{4}))$
53. $V_1 = 0$, $V_2 = -\frac{\sqrt{3}}{2}V_0$, $V_3 = \frac{\sqrt{3}}{2}V_0$
55. $\Delta t \approx 1.59 \times 10^{-10}$ s
56. ≈ 4.77 cm

### Part E: Vertical Shift
59. A=2, P=$2\pi$, C=0, D=3
60. A=3, P=$\pi$, C=0, D=-1
61. A=4, P=$2\pi$, C=$\frac{\pi}{2}$, D=5
62. A=$\frac{1}{2}$, P=$\frac{\pi}{2}$, C=$-\frac{\pi}{4}$, D=-2
63. (a) 5°C (b) 10°C (c) 365 days (d) $T(t) = -5\cos(\frac{2\pi}{365}(t-14)) + 10$
65. (a) 1.2 m (b) 2.0 m (c) 12.5 hours (d) $h(t) = 1.2\cos(\frac{2\pi}{12.5}t) + 2.0$
66. (a) A=0.6°C, D=36.8°C (c) 36.68°C

### Part F: Complete Form
67. A=3, P=$\pi$, C=$\frac{\pi}{2}$, D=1
68. A=2, P=$4\pi$, C=$-\frac{\pi}{2}$, D=-3
69. $y = 5\sin(\frac{1}{2}(x - \frac{\pi}{2})) - 2$
70. $y = 2\cos(2\pi x) + 3$
71. (a) 440 Hz, 880 Hz, 1320 Hz (b) 1.0, 0.3, 0.1 (c) Harmonics (2× and 3× fundamental)
72. (a) Odd integers (b) $\frac{1}{n}$ for odd $n$
73. (a) $2L$ (b) $L$ (c) $n$
74. (a) 2000 Hz (b) 200 Hz
75. (a) 22,050 Hz (b) Exceeds human hearing range
76. Yes! 70 Hz aliases to $|70-100| = 30$ Hz

---

*End of worksheet.*
