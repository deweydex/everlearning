# Worksheet 5D: Trigonometric Identities and Equations
**AIML Foundations Mathematics**  
**Dublin and Dún Laoghaire ETB**  
**Instructor: Josh Aaron**

---

> **What This Worksheet Is About**
>
> Trigonometric identities are equations that are true for all values of the variable. They're not problems to solve — they're tools that let us simplify expressions, prove relationships, and solve equations.
>
> These identities appear constantly in physics, engineering, and signal processing. Mastering them gives you powerful algebraic tools.

---

## Part A: Fundamental Identities (18 problems)

### The Pythagorean Identity

From the unit circle, we know:
$$\boxed{\sin^2\theta + \cos^2\theta = 1}$$

**Derived forms:**
- $\sin^2\theta = 1 - \cos^2\theta$
- $\cos^2\theta = 1 - \sin^2\theta$

---

**Simplify using the Pythagorean identity:**

**1.** $\sin^2(x) + \cos^2(x)$

**2.** $1 - \sin^2(x)$

**3.** $1 - \cos^2(x)$

**4.** $\frac{\sin^2(x)}{1 - \cos^2(x)}$

**5.** $\frac{1 - \sin^2(x)}{\cos(x)}$

**6.** $(\sin(x) + \cos(x))^2$

*Hint: Expand, then use the identity.*

---

### Quotient and Reciprocal Identities

$$\tan\theta = \frac{\sin\theta}{\cos\theta} \qquad \cot\theta = \frac{\cos\theta}{\sin\theta} = \frac{1}{\tan\theta}$$

$$\sec\theta = \frac{1}{\cos\theta} \qquad \csc\theta = \frac{1}{\sin\theta}$$

---

**Simplify:**

**7.** $\frac{\sin(x)}{\cos(x)}$

**8.** $\sin(x) \cdot \sec(x)$

**9.** $\cos(x) \cdot \csc(x)$

**10.** $\tan(x) \cdot \cos(x)$

**11.** $\frac{\sec(x)}{\csc(x)}$

**12.** $\sin^2(x) + \sin^2(x)\tan^2(x)$

*Hint: Factor out $\sin^2(x)$.*

---

### More Pythagorean Identities

Dividing $\sin^2\theta + \cos^2\theta = 1$ by $\cos^2\theta$:
$$\boxed{\tan^2\theta + 1 = \sec^2\theta}$$

Dividing by $\sin^2\theta$:
$$\boxed{1 + \cot^2\theta = \csc^2\theta}$$

---

**Simplify:**

**13.** $\sec^2(x) - 1$

**14.** $\csc^2(x) - 1$

**15.** $\sec^2(x) - \tan^2(x)$

**16.** $\frac{\tan^2(x)}{\sec^2(x) - 1}$

**17.** $\tan^2(x) + \cot^2(x) + 2$

*Hint: Rewrite using $\sec^2 - 1$ and $\csc^2 - 1$.*

**18.** $\frac{1 - \cos^2(x)}{\sin(x)}$

---

## Part B: Sum and Difference Formulas (20 problems)

### The Formulas

$$\boxed{\sin(A \pm B) = \sin A \cos B \pm \cos A \sin B}$$

$$\boxed{\cos(A \pm B) = \cos A \cos B \mp \sin A \sin B}$$

$$\boxed{\tan(A \pm B) = \frac{\tan A \pm \tan B}{1 \mp \tan A \tan B}}$$

**Memory aid:** 
- Sine: "sine-cosine, cosine-sine" with SAME sign as the original
- Cosine: "cosine-cosine, sine-sine" with OPPOSITE sign

---

**Find exact values using sum/difference formulas:**

**19.** $\sin(75°) = \sin(45° + 30°)$

**20.** $\cos(75°)$

**21.** $\sin(15°) = \sin(45° - 30°)$

**22.** $\cos(15°)$

**23.** $\tan(75°)$

**24.** $\sin(105°)$ — *Write as 60° + 45°*

**25.** $\cos(105°)$

---

**Verify identities:**

**26.** Show that $\sin(x + \frac{\pi}{2}) = \cos(x)$

**27.** Show that $\cos(x - \frac{\pi}{2}) = \sin(x)$

**28.** Show that $\sin(\pi - x) = \sin(x)$

**29.** Show that $\cos(\pi - x) = -\cos(x)$

---

**🔬 Science Connection: Phase in Wave Addition**

**30.** When two waves of the same frequency but different phases combine:

$$y_1 = A\sin(\omega t) \quad \text{and} \quad y_2 = A\sin(\omega t + \phi)$$

Using the sum formula on $y_2$:

$y_2 = A[\sin(\omega t)\cos\phi + \cos(\omega t)\sin\phi]$

$y_1 + y_2 = A\sin(\omega t) + A\sin(\omega t)\cos\phi + A\cos(\omega t)\sin\phi$

$= A(1 + \cos\phi)\sin(\omega t) + A\sin\phi\cos(\omega t)$

If $\phi = \frac{\pi}{2}$, simplify this expression.

**31.** If $\phi = \pi$ (waves completely out of phase), what is $y_1 + y_2$?

---

**🔬 Science Connection: Rotation Matrices**

**32.** In computer graphics and robotics, rotation by angle $\theta$ uses the matrix:

$$R = \begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix}$$

To rotate first by $\alpha$, then by $\beta$, you multiply matrices. The result should be rotation by $\alpha + \beta$. This is equivalent to showing:

$\cos(\alpha)\cos(\beta) - \sin(\alpha)\sin(\beta) = \cos(\alpha + \beta)$

Verify this matches the sum formula for cosine!

**33.** Rotating a point $(1, 0)$ by 30°, then by 60°, should give the same result as rotating by 90°.
- (a) What is $\cos(90°)$ and $\sin(90°)$?
- (b) Verify that $\cos(30°)\cos(60°) - \sin(30°)\sin(60°) = \cos(90°)$

---

**🔭 Astronomy: Orbital Mechanics**

**34.** The position of a planet in an elliptical orbit involves angles that add and subtract. 

If a satellite's angular position is the sum of two angles: $\theta_{total} = \theta_1 + \theta_2$

where $\theta_1 = 45°$ and $\theta_2 = 60°$, find $\cos(\theta_{total})$ and $\sin(\theta_{total})$ exactly.

---

## Part C: Double Angle and Half Angle Formulas (18 problems)

### Double Angle Formulas

Setting $A = B$ in the sum formulas:

$$\boxed{\sin(2\theta) = 2\sin\theta\cos\theta}$$

$$\boxed{\cos(2\theta) = \cos^2\theta - \sin^2\theta = 2\cos^2\theta - 1 = 1 - 2\sin^2\theta}$$

$$\boxed{\tan(2\theta) = \frac{2\tan\theta}{1 - \tan^2\theta}}$$

---

**Simplify:**

**35.** $2\sin(30°)\cos(30°)$

**36.** $\cos^2(45°) - \sin^2(45°)$

**37.** $2\cos^2(30°) - 1$

**38.** $1 - 2\sin^2(60°)$

---

**Find exact values:**

**39.** If $\sin\theta = \frac{3}{5}$ and $\theta$ is in Quadrant I, find:
- (a) $\cos\theta$
- (b) $\sin(2\theta)$
- (c) $\cos(2\theta)$

**40.** If $\cos\theta = \frac{5}{13}$ and $\theta$ is in Quadrant I, find $\sin(2\theta)$ and $\cos(2\theta)$.

---

### Half Angle Formulas

$$\sin\left(\frac{\theta}{2}\right) = \pm\sqrt{\frac{1 - \cos\theta}{2}}$$

$$\cos\left(\frac{\theta}{2}\right) = \pm\sqrt{\frac{1 + \cos\theta}{2}}$$

(Sign depends on which quadrant $\frac{\theta}{2}$ is in)

---

**Find exact values:**

**41.** $\sin(22.5°)$ — *Use $\theta = 45°$*

**42.** $\cos(22.5°)$

**43.** $\sin(15°)$ — *Use $\theta = 30°$* — Compare to your answer from Problem 21!

**44.** $\cos(15°)$

---

**🔬 Science Connection: Power Reduction**

In electronics, it's often necessary to convert between powers of trig functions and multiple angles.

**45.** The power reduction formulas come from solving the double-angle formulas:

$$\sin^2\theta = \frac{1 - \cos(2\theta)}{2} \qquad \cos^2\theta = \frac{1 + \cos(2\theta)}{2}$$

Verify by expanding $\cos(2\theta) = 1 - 2\sin^2\theta$ and solving for $\sin^2\theta$.

**46.** In AC circuits, power is proportional to $\sin^2(\omega t)$ or $\cos^2(\omega t)$.

Using the power reduction formula, show that:
$\sin^2(\omega t) = \frac{1}{2} - \frac{1}{2}\cos(2\omega t)$

What does this tell you about the frequency of power oscillation compared to voltage oscillation?

---

**🔬 Science Connection: Interference Patterns**

**47.** When two identical beams of light interfere, the intensity is proportional to:

$$I \propto \cos^2\left(\frac{\phi}{2}\right)$$

where $\phi$ is the phase difference.

Using the half-angle relationship, rewrite this as:
$I \propto \frac{1 + \cos\phi}{2}$

**48.** In Young's double-slit experiment, the phase difference is $\phi = \frac{2\pi d \sin\theta}{\lambda}$ where $d$ is slit separation, $\theta$ is angle from center, and $\lambda$ is wavelength.

At what values of $\phi$ do you get:
- (a) Maximum intensity (bright fringes)?
- (b) Minimum intensity (dark fringes)?

---

**🔬 Science Connection: Lithography Interference**

**49.** Interference lithography creates patterns by interfering two laser beams. The pattern has period:

$$p = \frac{\lambda}{2\sin\theta}$$

where $\theta$ is the half-angle between the beams.

Using $\lambda = 193$ nm and $\theta = 30°$, what pattern period can be achieved?

**50.** To create 10 nm features, you need $p = 20$ nm. If $\lambda = 13.5$ nm (EUV), what angle $\theta$ is needed?

---

## Part D: Solving Trigonometric Equations (20 problems)

### Strategy

1. Isolate the trig function if possible
2. Use identities to simplify
3. Find all solutions in the required interval
4. Remember: trig functions are periodic!

---

**Solve for $x$ in $[0, 2\pi)$:**

**51.** $\sin(x) = \frac{1}{2}$

**52.** $\cos(x) = -\frac{\sqrt{2}}{2}$

**53.** $\tan(x) = 1$

**54.** $\sin(x) = -\frac{\sqrt{3}}{2}$

**55.** $2\cos(x) - 1 = 0$

**56.** $2\sin(x) + \sqrt{3} = 0$

---

**Solve (may require factoring or identities):**

**57.** $2\sin^2(x) - 1 = 0$

**58.** $\cos^2(x) - \cos(x) = 0$

**59.** $2\sin^2(x) - \sin(x) - 1 = 0$

**60.** $\tan^2(x) - 3 = 0$

**61.** $\sin(2x) = \frac{\sqrt{3}}{2}$ in $[0, 2\pi)$

*Hint: Let $u = 2x$, solve for $u$ in $[0, 4\pi)$, then find $x$.*

**62.** $\cos(2x) = -\frac{1}{2}$ in $[0, 2\pi)$

---

**Use identities to solve:**

**63.** $\sin^2(x) - \cos^2(x) = 0$

*Hint: This is $-\cos(2x) = 0$*

**64.** $\sin(x)\cos(x) = \frac{1}{4}$

*Hint: Use $\sin(2x) = 2\sin(x)\cos(x)$*

**65.** $1 - \sin^2(x) = \frac{1}{2}$

---

**🔬 Science Connection: Resonance**

**66.** A system oscillates at frequency $\omega$. Resonance occurs when the driving frequency matches the natural frequency, i.e., when:

$\sin(\omega_d t) = \sin(\omega_n t)$

If $\omega_d = 2\pi$ rad/s and $\omega_n = 2\pi$ rad/s, at what times $t$ in $[0, 1)$ seconds do the phases align (equal to each other)?

---

**🔬 Science Connection: Standing Waves**

**67.** A standing wave on a string is described by:

$y(x,t) = 2A\sin(kx)\cos(\omega t)$

The nodes (points that don't move) occur where $\sin(kx) = 0$.

If $k = \frac{\pi}{0.5} = 2\pi$ m$^{-1}$, find all nodes in the interval $x \in [0, 2]$ meters.

---

**🔬 Science Connection: Diffraction Minima**

**68.** In single-slit diffraction, dark fringes occur when:

$\sin\theta = \frac{m\lambda}{a}$

where $a$ is slit width, $\lambda$ is wavelength, and $m = \pm 1, \pm 2, ...$

For $a = 1000$ nm and $\lambda = 500$ nm, find all angles $\theta$ where dark fringes occur (within the physical range where $|\sin\theta| \leq 1$).

---

**General Solutions:**

**69.** Give the general solution (all solutions) for $\sin(x) = \frac{1}{2}$.

**70.** Give the general solution for $\cos(x) = 0$.

---

## Answer Key

### Part A: Fundamental Identities
1. 1
2. $\cos^2(x)$
3. $\sin^2(x)$
4. 1
5. $\cos(x)$
6. $1 + 2\sin(x)\cos(x) = 1 + \sin(2x)$
7. $\tan(x)$
8. $\tan(x)$
9. $\cot(x)$
10. $\sin(x)$
11. $\tan(x)$
12. $\tan^2(x)$
13. $\tan^2(x)$
14. $\cot^2(x)$
15. 1
16. 1
17. $\sec^2(x) + \csc^2(x)$
18. $\sin(x)$

### Part B: Sum and Difference
19. $\frac{\sqrt{6} + \sqrt{2}}{4}$
20. $\frac{\sqrt{6} - \sqrt{2}}{4}$
21. $\frac{\sqrt{6} - \sqrt{2}}{4}$
22. $\frac{\sqrt{6} + \sqrt{2}}{4}$
23. $2 + \sqrt{3}$
24. $\frac{\sqrt{6} + \sqrt{2}}{4}$
25. $\frac{\sqrt{2} - \sqrt{6}}{4}$
30. $A\sin(\omega t) + A\cos(\omega t)$
31. 0
33. (a) 0, 1 (b) $\frac{\sqrt{3}}{2} \cdot \frac{1}{2} - \frac{1}{2} \cdot \frac{\sqrt{3}}{2} = 0$ ✓
34. $\cos(105°) = \frac{\sqrt{2} - \sqrt{6}}{4}$, $\sin(105°) = \frac{\sqrt{6} + \sqrt{2}}{4}$

### Part C: Double and Half Angle
35. $\frac{\sqrt{3}}{2}$
36. 0
37. $\frac{1}{2}$
38. $-\frac{1}{2}$
39. (a) $\frac{4}{5}$ (b) $\frac{24}{25}$ (c) $\frac{7}{25}$
40. $\sin(2\theta) = \frac{120}{169}$, $\cos(2\theta) = -\frac{119}{169}$
41. $\frac{\sqrt{2-\sqrt{2}}}{2}$
42. $\frac{\sqrt{2+\sqrt{2}}}{2}$
43. $\frac{\sqrt{2-\sqrt{3}}}{2}$
44. $\frac{\sqrt{2+\sqrt{3}}}{2}$
46. Power oscillates at twice the frequency of voltage
48. (a) $\phi = 0, 2\pi, 4\pi, ...$ (b) $\phi = \pi, 3\pi, 5\pi, ...$
49. 193 nm
50. $\theta \approx 19.7°$

### Part D: Solving Equations
51. $x = \frac{\pi}{6}, \frac{5\pi}{6}$
52. $x = \frac{3\pi}{4}, \frac{5\pi}{4}$
53. $x = \frac{\pi}{4}, \frac{5\pi}{4}$
54. $x = \frac{4\pi}{3}, \frac{5\pi}{3}$
55. $x = \frac{\pi}{3}, \frac{5\pi}{3}$
56. $x = \frac{4\pi}{3}, \frac{5\pi}{3}$
57. $x = \frac{\pi}{4}, \frac{3\pi}{4}, \frac{5\pi}{4}, \frac{7\pi}{4}$
58. $x = 0, \frac{\pi}{2}, \frac{3\pi}{2}$ (Note: $\cos(x) = 0$ or $\cos(x) = 1$)
59. $x = \frac{\pi}{2}, \frac{7\pi}{6}, \frac{11\pi}{6}$
60. $x = \frac{\pi}{3}, \frac{2\pi}{3}, \frac{4\pi}{3}, \frac{5\pi}{3}$
61. $x = \frac{\pi}{6}, \frac{\pi}{3}, \frac{7\pi}{6}, \frac{4\pi}{3}$
62. $x = \frac{\pi}{3}, \frac{2\pi}{3}, \frac{4\pi}{3}, \frac{5\pi}{3}$
63. $x = \frac{\pi}{4}, \frac{3\pi}{4}, \frac{5\pi}{4}, \frac{7\pi}{4}$
64. $x = \frac{\pi}{12}, \frac{5\pi}{12}, \frac{13\pi}{12}, \frac{17\pi}{12}$
65. $x = \frac{\pi}{4}, \frac{3\pi}{4}, \frac{5\pi}{4}, \frac{7\pi}{4}$
66. All $t$ in $[0, 1)$ (they're always equal since frequencies match)
67. $x = 0, 0.5, 1.0, 1.5, 2.0$ meters
68. $\theta = 30°, 90°$ (for $m = 1, 2$; also negative angles)
69. $x = \frac{\pi}{6} + 2\pi n$ or $x = \frac{5\pi}{6} + 2\pi n$, where $n$ is any integer
70. $x = \frac{\pi}{2} + \pi n$, where $n$ is any integer

---

*End of Worksheet 5D*
