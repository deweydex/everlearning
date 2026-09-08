# Worksheet 5A: Angles, Radians, and the Unit Circle
**AIML Foundations Mathematics**  
**Dublin and Dún Laoghaire ETB**  
**Instructor: Josh Aaron**

---

> **What This Worksheet Is About**
>
> Trigonometry began with ancient astronomers trying to measure the heavens. Today it's essential for everything from GPS satellites to semiconductor manufacturing.
>
> We start with two ways to measure angles (degrees and radians) and introduce the unit circle — a tool that will make everything else in trigonometry click into place.

---

## Part A: Degrees and Radians — Two Languages for Angles (20 problems)

### Why Two Systems?

**Degrees** come from ancient Babylon (360° in a circle — probably because 360 has many divisors and roughly matches days in a year).

**Radians** come from mathematics itself: one radian is the angle where the arc length equals the radius.

$$\boxed{2\pi \text{ radians} = 360°}$$

Therefore: $\pi \text{ rad} = 180°$, and $1 \text{ rad} = \frac{180°}{\pi} \approx 57.3°$

---

### Converting Between Systems

**Degrees → Radians:** Multiply by $\frac{\pi}{180}$

**Radians → Degrees:** Multiply by $\frac{180}{\pi}$

---

**Convert to radians (leave answers in terms of $\pi$):**

**1.** $90° = $ \_\_\_\_\_\_\_\_\_\_ rad

**2.** $180° = $ \_\_\_\_\_\_\_\_\_\_ rad

**3.** $45° = $ \_\_\_\_\_\_\_\_\_\_ rad

**4.** $60° = $ \_\_\_\_\_\_\_\_\_\_ rad

**5.** $30° = $ \_\_\_\_\_\_\_\_\_\_ rad

**6.** $120° = $ \_\_\_\_\_\_\_\_\_\_ rad

**7.** $270° = $ \_\_\_\_\_\_\_\_\_\_ rad

**8.** $315° = $ \_\_\_\_\_\_\_\_\_\_ rad

**9.** $150° = $ \_\_\_\_\_\_\_\_\_\_ rad

**10.** $225° = $ \_\_\_\_\_\_\_\_\_\_ rad

---

**Convert to degrees:**

**11.** $\frac{\pi}{6}$ rad $= $ \_\_\_\_\_\_\_\_\_\_°

**12.** $\frac{\pi}{4}$ rad $= $ \_\_\_\_\_\_\_\_\_\_°

**13.** $\frac{\pi}{3}$ rad $= $ \_\_\_\_\_\_\_\_\_\_°

**14.** $\frac{2\pi}{3}$ rad $= $ \_\_\_\_\_\_\_\_\_\_°

**15.** $\frac{5\pi}{6}$ rad $= $ \_\_\_\_\_\_\_\_\_\_°

**16.** $\frac{5\pi}{4}$ rad $= $ \_\_\_\_\_\_\_\_\_\_°

**17.** $\frac{7\pi}{6}$ rad $= $ \_\_\_\_\_\_\_\_\_\_°

**18.** $\frac{11\pi}{6}$ rad $= $ \_\_\_\_\_\_\_\_\_\_°

---

**🔬 Science Connection: Why Radians Matter**

**19.** In calculus, the derivative of $\sin(x)$ is $\cos(x)$ — but **only if $x$ is in radians!**

If we used degrees, we'd get: $\frac{d}{dx}\sin(x°) = \frac{\pi}{180}\cos(x°)$

That ugly factor disappears with radians. This is why all scientific computing uses radians.

**20.** A satellite dish must be aimed within $0.1°$ of the correct angle. Convert this to radians.

---

## Part B: Arc Length and the Radian Definition (12 problems)

### The Key Formula

For a circle of radius $r$ and central angle $\theta$ (in radians):

$$\boxed{s = r\theta}$$

where $s$ is the **arc length**.

This formula is beautifully simple — but only works with radians!

---

**21.** A circle has radius 10 cm. Find the arc length for a central angle of:
- (a) $\frac{\pi}{2}$ rad
- (b) $\pi$ rad
- (c) $2\pi$ rad (verify this gives the circumference!)

**22.** Earth's radius is approximately 6,371 km. 

- (a) If you travel along Earth's surface through an angle of 1 radian (as measured from Earth's center), how far have you traveled?
- (b) Dublin is at latitude 53.3°N. Convert this to radians.
- (c) What is the arc length from the equator to Dublin along a meridian?

---

**🌍 Science Connection: How Eratosthenes Measured Earth**

Around 240 BCE, Eratosthenes noticed that at noon on the summer solstice, the sun was directly overhead in Syene (modern Aswan, Egypt) — it shone straight down a well.

But in Alexandria, 800 km north, the sun cast a shadow at an angle of about 7.2° from vertical.

**23.** 
- (a) Convert 7.2° to radians.
- (b) The arc length between the cities is 800 km. Using $s = r\theta$, solve for $r$ (Earth's radius).
- (c) The actual radius is about 6,371 km. How close was this ancient measurement?

---

**🔭 Astronomy: Angular Size**

When we look at distant objects, we measure their **angular diameter** — how big they appear in the sky.

**24.** The Moon's angular diameter is about 0.52° as seen from Earth.
- (a) Convert to radians.
- (b) The Moon is about 384,400 km away. Using $s = r\theta$ (treating the Moon's diameter as an arc), estimate the Moon's actual diameter.
- (c) The actual diameter is about 3,474 km. How close is your estimate?

**25.** The Sun's angular diameter is also about 0.53° — almost the same as the Moon! This is why solar eclipses are possible. The Sun is about 150 million km away. Estimate the Sun's diameter.

**26.** Jupiter's angular diameter varies from 0.55 arcminutes to 0.83 arcminutes depending on its distance from Earth (1 arcminute = 1/60 of a degree).
- (a) Convert 0.83 arcminutes to radians.
- (b) At closest approach, Jupiter is about 588 million km away. Estimate its diameter.

---

## Part C: The Unit Circle — Your New Best Friend (24 problems)

### What Is It?

The **unit circle** is a circle with radius 1, centered at the origin.

For any angle $\theta$ measured from the positive x-axis:
- The x-coordinate of the point on the circle is $\cos(\theta)$
- The y-coordinate is $\sin(\theta)$

$$\boxed{(\cos\theta, \sin\theta) = \text{coordinates on unit circle at angle } \theta}$$

---

### Special Angles to Memorize

| Angle (°) | Angle (rad) | $\cos\theta$ | $\sin\theta$ |
|-----------|-------------|--------------|--------------|
| 0° | 0 | 1 | 0 |
| 30° | $\frac{\pi}{6}$ | $\frac{\sqrt{3}}{2}$ | $\frac{1}{2}$ |
| 45° | $\frac{\pi}{4}$ | $\frac{\sqrt{2}}{2}$ | $\frac{\sqrt{2}}{2}$ |
| 60° | $\frac{\pi}{3}$ | $\frac{1}{2}$ | $\frac{\sqrt{3}}{2}$ |
| 90° | $\frac{\pi}{2}$ | 0 | 1 |

**Memory trick:** For sine at 0°, 30°, 45°, 60°, 90°: $\frac{\sqrt{0}}{2}, \frac{\sqrt{1}}{2}, \frac{\sqrt{2}}{2}, \frac{\sqrt{3}}{2}, \frac{\sqrt{4}}{2}$

---

**Find the exact values without a calculator:**

**27.** $\cos(0) = $ \_\_\_\_\_ , $\sin(0) = $ \_\_\_\_\_

**28.** $\cos\left(\frac{\pi}{6}\right) = $ \_\_\_\_\_ , $\sin\left(\frac{\pi}{6}\right) = $ \_\_\_\_\_

**29.** $\cos\left(\frac{\pi}{4}\right) = $ \_\_\_\_\_ , $\sin\left(\frac{\pi}{4}\right) = $ \_\_\_\_\_

**30.** $\cos\left(\frac{\pi}{3}\right) = $ \_\_\_\_\_ , $\sin\left(\frac{\pi}{3}\right) = $ \_\_\_\_\_

**31.** $\cos\left(\frac{\pi}{2}\right) = $ \_\_\_\_\_ , $\sin\left(\frac{\pi}{2}\right) = $ \_\_\_\_\_

---

### Extending to All Four Quadrants

**ASTC Rule:** Which functions are positive in each quadrant?
- **A**ll (Quadrant I): Both sin and cos positive
- **S**in (Quadrant II): Only sin positive
- **T**an (Quadrant III): Only tan positive
- **C**os (Quadrant IV): Only cos positive

**Reference Angle:** The acute angle to the x-axis. Use symmetry!

---

**Find the exact values:**

**32.** $\cos\left(\frac{2\pi}{3}\right) = $ \_\_\_\_\_ , $\sin\left(\frac{2\pi}{3}\right) = $ \_\_\_\_\_

*Hint: $\frac{2\pi}{3}$ is in Q2, reference angle is $\frac{\pi}{3}$*

**33.** $\cos\left(\frac{3\pi}{4}\right) = $ \_\_\_\_\_ , $\sin\left(\frac{3\pi}{4}\right) = $ \_\_\_\_\_

**34.** $\cos\left(\frac{5\pi}{6}\right) = $ \_\_\_\_\_ , $\sin\left(\frac{5\pi}{6}\right) = $ \_\_\_\_\_

**35.** $\cos(\pi) = $ \_\_\_\_\_ , $\sin(\pi) = $ \_\_\_\_\_

**36.** $\cos\left(\frac{7\pi}{6}\right) = $ \_\_\_\_\_ , $\sin\left(\frac{7\pi}{6}\right) = $ \_\_\_\_\_

**37.** $\cos\left(\frac{5\pi}{4}\right) = $ \_\_\_\_\_ , $\sin\left(\frac{5\pi}{4}\right) = $ \_\_\_\_\_

**38.** $\cos\left(\frac{4\pi}{3}\right) = $ \_\_\_\_\_ , $\sin\left(\frac{4\pi}{3}\right) = $ \_\_\_\_\_

**39.** $\cos\left(\frac{3\pi}{2}\right) = $ \_\_\_\_\_ , $\sin\left(\frac{3\pi}{2}\right) = $ \_\_\_\_\_

**40.** $\cos\left(\frac{5\pi}{3}\right) = $ \_\_\_\_\_ , $\sin\left(\frac{5\pi}{3}\right) = $ \_\_\_\_\_

**41.** $\cos\left(\frac{7\pi}{4}\right) = $ \_\_\_\_\_ , $\sin\left(\frac{7\pi}{4}\right) = $ \_\_\_\_\_

**42.** $\cos\left(\frac{11\pi}{6}\right) = $ \_\_\_\_\_ , $\sin\left(\frac{11\pi}{6}\right) = $ \_\_\_\_\_

---

### Negative Angles and Angles Beyond $2\pi$

**43.** $\cos(-\frac{\pi}{4}) = $ \_\_\_\_\_ , $\sin(-\frac{\pi}{4}) = $ \_\_\_\_\_

**44.** $\cos(-\frac{\pi}{6}) = $ \_\_\_\_\_ , $\sin(-\frac{\pi}{6}) = $ \_\_\_\_\_

**45.** $\cos\left(\frac{13\pi}{6}\right) = $ \_\_\_\_\_ , $\sin\left(\frac{13\pi}{6}\right) = $ \_\_\_\_\_

*Hint: $\frac{13\pi}{6} = 2\pi + \frac{\pi}{6}$*

**46.** $\cos(3\pi) = $ \_\_\_\_\_ , $\sin(3\pi) = $ \_\_\_\_\_

---

### The Pythagorean Identity

**47.** On the unit circle, a point is at $(\cos\theta, \sin\theta)$. The distance from this point to the origin is the radius, which equals 1.

Using the distance formula: $\sqrt{\cos^2\theta + \sin^2\theta} = 1$

Square both sides: $\cos^2\theta + \sin^2\theta = $ \_\_\_\_\_

**This is the most important identity in trigonometry!**

**48.** Verify the identity for $\theta = \frac{\pi}{4}$:

$\cos^2\left(\frac{\pi}{4}\right) + \sin^2\left(\frac{\pi}{4}\right) = \left(\frac{\sqrt{2}}{2}\right)^2 + \left(\frac{\sqrt{2}}{2}\right)^2 = $ \_\_\_\_\_

**49.** Verify for $\theta = \frac{\pi}{3}$.

**50.** If $\sin\theta = \frac{3}{5}$ and $\theta$ is in Quadrant I, find $\cos\theta$.

---

## Part D: The Tangent Function and More (14 problems)

### Definition

$$\tan\theta = \frac{\sin\theta}{\cos\theta} = \frac{y}{x} = \text{slope of the line from origin to point on circle}$$

---

**Find the exact values:**

**51.** $\tan(0) = $ \_\_\_\_\_

**52.** $\tan\left(\frac{\pi}{6}\right) = $ \_\_\_\_\_

**53.** $\tan\left(\frac{\pi}{4}\right) = $ \_\_\_\_\_

**54.** $\tan\left(\frac{\pi}{3}\right) = $ \_\_\_\_\_

**55.** $\tan\left(\frac{\pi}{2}\right) = $ \_\_\_\_\_ (What happens here?)

**56.** $\tan\left(\frac{2\pi}{3}\right) = $ \_\_\_\_\_

**57.** $\tan\left(\frac{3\pi}{4}\right) = $ \_\_\_\_\_

**58.** $\tan(\pi) = $ \_\_\_\_\_

---

**🔬 Science Connection: Angles of Incidence and Reflection**

**59.** In optics, when light hits a surface, the angle of incidence equals the angle of reflection (measured from the perpendicular "normal" line).

A laser beam hits a mirror at an angle of $\frac{\pi}{6}$ radians from the normal.
- (a) What is the angle of reflection?
- (b) What is the total deflection of the beam (angle between incoming and outgoing rays)?

**60.** In a periscope, light bounces off two mirrors. If each mirror is angled at 45° to the horizontal, through what total angle is the light path bent?

---

**🔬 Microscopy: Numerical Aperture**

The **numerical aperture** (NA) of a microscope objective determines its resolving power:

$$NA = n \cdot \sin(\theta)$$

where $n$ is the refractive index of the medium and $\theta$ is the half-angle of the cone of light entering the objective.

**61.** An air-immersion objective ($n = 1.0$) has a half-angle of 60°.
- (a) Find $\sin(60°)$.
- (b) Calculate the numerical aperture.

**62.** An oil-immersion objective ($n = 1.52$) has a half-angle of 70°.
- (a) Find $\sin(70°)$ using a calculator (≈ 0.940).
- (b) Calculate the numerical aperture.
- (c) Why does using oil allow for higher NA and better resolution?

---

**🔬 Lithography: The Diffraction Limit**

In semiconductor manufacturing, the smallest feature size that can be printed is limited by:

$$\text{Resolution} = k_1 \cdot \frac{\lambda}{NA}$$

where $\lambda$ is the wavelength of light, NA is the numerical aperture, and $k_1$ is a process factor (typically around 0.25-0.4).

**63.** Extreme ultraviolet (EUV) lithography uses $\lambda = 13.5$ nm and has NA ≈ 0.33.
- (a) With $k_1 = 0.3$, what is the theoretical minimum feature size?
- (b) Current chips have 3nm features. Does this seem achievable with these parameters?

**64.** Older lithography used deep ultraviolet (DUV) light at $\lambda = 193$ nm with NA ≈ 1.35 (using immersion).
- (a) With $k_1 = 0.3$, what resolution is achievable?
- (b) Why did the industry need to move to EUV for smaller features?

---

## Answer Key

### Part A: Degrees and Radians
1. $\frac{\pi}{2}$
2. $\pi$
3. $\frac{\pi}{4}$
4. $\frac{\pi}{3}$
5. $\frac{\pi}{6}$
6. $\frac{2\pi}{3}$
7. $\frac{3\pi}{2}$
8. $\frac{7\pi}{4}$
9. $\frac{5\pi}{6}$
10. $\frac{5\pi}{4}$
11. 30°
12. 45°
13. 60°
14. 120°
15. 150°
16. 225°
17. 210°
18. 330°
20. $\approx 0.00175$ rad

### Part B: Arc Length
21. (a) $5\pi$ cm (b) $10\pi$ cm (c) $20\pi$ cm
22. (a) 6,371 km (b) $\approx 0.930$ rad (c) $\approx 5,930$ km
23. (a) $\approx 0.1257$ rad (b) $\approx 6,366$ km (c) Very close!
24. (a) $\approx 0.00908$ rad (b) $\approx 3,490$ km (c) Very close!
25. $\approx 1,390,000$ km (actual ≈ 1,392,000 km)
26. (a) $\approx 0.000242$ rad (b) $\approx 142,000$ km

### Part C: Unit Circle
27. 1, 0
28. $\frac{\sqrt{3}}{2}$, $\frac{1}{2}$
29. $\frac{\sqrt{2}}{2}$, $\frac{\sqrt{2}}{2}$
30. $\frac{1}{2}$, $\frac{\sqrt{3}}{2}$
31. 0, 1
32. $-\frac{1}{2}$, $\frac{\sqrt{3}}{2}$
33. $-\frac{\sqrt{2}}{2}$, $\frac{\sqrt{2}}{2}$
34. $-\frac{\sqrt{3}}{2}$, $\frac{1}{2}$
35. $-1$, $0$
36. $-\frac{\sqrt{3}}{2}$, $-\frac{1}{2}$
37. $-\frac{\sqrt{2}}{2}$, $-\frac{\sqrt{2}}{2}$
38. $-\frac{1}{2}$, $-\frac{\sqrt{3}}{2}$
39. $0$, $-1$
40. $\frac{1}{2}$, $-\frac{\sqrt{3}}{2}$
41. $\frac{\sqrt{2}}{2}$, $-\frac{\sqrt{2}}{2}$
42. $\frac{\sqrt{3}}{2}$, $-\frac{1}{2}$
43. $\frac{\sqrt{2}}{2}$, $-\frac{\sqrt{2}}{2}$
44. $\frac{\sqrt{3}}{2}$, $-\frac{1}{2}$
45. $\frac{\sqrt{3}}{2}$, $\frac{1}{2}$
46. $-1$, $0$
47. 1
48. $\frac{1}{2} + \frac{1}{2} = 1$
49. $\frac{1}{4} + \frac{3}{4} = 1$
50. $\cos\theta = \frac{4}{5}$

### Part D: Tangent and Applications
51. 0
52. $\frac{1}{\sqrt{3}} = \frac{\sqrt{3}}{3}$
53. 1
54. $\sqrt{3}$
55. Undefined (division by zero)
56. $-\sqrt{3}$
57. $-1$
58. 0
59. (a) $\frac{\pi}{6}$ rad (b) $\frac{\pi}{3}$ rad or 60°
60. 90°
61. (a) $\frac{\sqrt{3}}{2} \approx 0.866$ (b) NA = 0.866
62. (a) 0.940 (b) NA ≈ 1.43 (c) Higher refractive index allows larger effective angle
63. (a) $\approx 12.3$ nm (b) Requires multiple patterning techniques
64. (a) $\approx 43$ nm (b) Physics limits further shrinking with longer wavelengths

---

*End of Worksheet 5A*
