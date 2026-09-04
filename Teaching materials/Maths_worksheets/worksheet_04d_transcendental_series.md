# Worksheet 4D: Transcendental Functions via Series
**AIML Foundations Mathematics**  
**Dublin and Dún Laoghaire ETB**  
**Instructor: Josh Aaron**

---

> **What This Worksheet Is About**
>
> So far, we've worked with polynomials. But what about functions like $e^x$, $\sin(x)$, $\cos(x)$, and $\ln(x)$?
>
> Here's the beautiful secret: **These functions can be written as infinite polynomials (series)!**
>
> Once we write them as polynomials, we can differentiate and integrate term by term using the power rule. This lets us *discover* their derivatives rather than just memorizing them.

---

## Part A: The Exponential Function $e^x$ (18 problems)

### The Series Definition

The number $e \approx 2.71828...$ is defined as:

$$e = 1 + 1 + \frac{1}{2!} + \frac{1}{3!} + \frac{1}{4!} + \cdots$$

And the exponential function $e^x$ is:

$$\boxed{e^x = 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \frac{x^4}{4!} + \cdots = \sum_{n=0}^{\infty} \frac{x^n}{n!}}$$

**Reminder:** $n! = n \times (n-1) \times \cdots \times 2 \times 1$, and $0! = 1$ by convention.

---

**Understanding the Series:**

**1.** Calculate the first five terms of the series for $e^1 = e$:

$1 + 1 + \frac{1}{2} + \frac{1}{6} + \frac{1}{24} = $ \_\_\_\_\_\_\_\_\_\_

**2.** Compare your answer to $e \approx 2.71828$. How close?

**3.** Write out the first 6 terms of the series for $e^x$:

$e^x = 1 + x + $ \_\_\_\_\_\_\_\_\_\_ $ + $ \_\_\_\_\_\_\_\_\_\_ $ + $ \_\_\_\_\_\_\_\_\_\_ $ + $ \_\_\_\_\_\_\_\_\_\_ $ + \cdots$

**4.** Use the first 4 terms to approximate $e^{0.5}$:

$e^{0.5} \approx 1 + 0.5 + \frac{0.25}{2} + \frac{0.125}{6} = $ \_\_\_\_\_\_\_\_\_\_

Actual value: $e^{0.5} \approx 1.6487$. How close?

---

### Differentiating $e^x$ Term by Term

**5.** Differentiate each term of the series $e^x = 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \frac{x^4}{4!} + \cdots$

| Term | Derivative |
|------|------------|
| $1$ | |
| $x$ | |
| $\frac{x^2}{2!} = \frac{x^2}{2}$ | |
| $\frac{x^3}{3!} = \frac{x^3}{6}$ | |
| $\frac{x^4}{4!} = \frac{x^4}{24}$ | |
| $\frac{x^5}{5!} = \frac{x^5}{120}$ | |

**6.** Write out the derivative series you get:

$\frac{d}{dx}e^x = 0 + 1 + $ \_\_\_\_\_\_ $ + $ \_\_\_\_\_\_ $ + $ \_\_\_\_\_\_ $ + \cdots$

**7.** Compare to the original series. What do you notice?

**8.** Complete: $\frac{d}{dx}e^x = $ \_\_\_\_\_\_\_\_\_\_

**This is remarkable!** The exponential function is its own derivative!

---

### Integrating $e^x$ Term by Term

**9.** Integrate each term of $e^x = 1 + x + \frac{x^2}{2} + \frac{x^3}{6} + \frac{x^4}{24} + \cdots$

| Term | Integral |
|------|----------|
| $1$ | |
| $x$ | |
| $\frac{x^2}{2}$ | |
| $\frac{x^3}{6}$ | |
| $\frac{x^4}{24}$ | |

**10.** Write out the integrated series:

$\int e^x \, dx = x + \frac{x^2}{2} + $ \_\_\_\_\_\_ $ + $ \_\_\_\_\_\_ $ + $ \_\_\_\_\_\_ $ + C$

**11.** Factor out from each term to show this equals $e^x + C$:

Hint: $x = \frac{x^1}{1!}$, $\frac{x^2}{2} = \frac{x^2}{2!}$, etc.

**12.** Complete: $\int e^x \, dx = $ \_\_\_\_\_\_\_\_\_\_ $ + C$

---

### The Derivative and Integral are Inverses

**13.** Start with $f(x) = e^x$. Differentiate, then integrate:

$f'(x) = $ \_\_\_\_\_\_\_\_\_\_

$\int f'(x) \, dx = $ \_\_\_\_\_\_\_\_\_\_

**14.** Start with $g(x) = e^x$. Integrate, then differentiate:

$\int g(x) \, dx = $ \_\_\_\_\_\_\_\_\_\_

$\frac{d}{dx}\left[\int g(x) \, dx\right] = $ \_\_\_\_\_\_\_\_\_\_

---

### Chain Rule and Substitution with $e^x$

**15.** Using the chain rule: $\frac{d}{dx}e^{2x} = e^{2x} \cdot 2 = 2e^{2x}$

Find: $\frac{d}{dx}e^{3x} = $ \_\_\_\_\_\_\_\_\_\_

**16.** Find: $\frac{d}{dx}e^{-x} = $ \_\_\_\_\_\_\_\_\_\_

**17.** Using substitution: $\int e^{2x} \, dx$

Let $u = 2x$, so $du = 2dx$, meaning $dx = \frac{1}{2}du$

$\int e^{2x} \, dx = \int e^u \cdot \frac{1}{2} du = \frac{1}{2}e^u + C = $ \_\_\_\_\_\_\_\_\_\_ $ + C$

**18.** Find: $\int e^{5x} \, dx = $ \_\_\_\_\_\_\_\_\_\_ $ + C$

---

## Part B: Sine and Cosine via Series (24 problems)

### The Series Definitions

$$\boxed{\sin(x) = x - \frac{x^3}{3!} + \frac{x^5}{5!} - \frac{x^7}{7!} + \cdots = \sum_{n=0}^{\infty} \frac{(-1)^n x^{2n+1}}{(2n+1)!}}$$

$$\boxed{\cos(x) = 1 - \frac{x^2}{2!} + \frac{x^4}{4!} - \frac{x^6}{6!} + \cdots = \sum_{n=0}^{\infty} \frac{(-1)^n x^{2n}}{(2n)!}}$$

**Note:** $x$ is in **radians**, not degrees!

---

**Understanding the Patterns:**

**19.** The sine series has only \_\_\_\_\_\_\_\_\_\_ powers of $x$ (odd/even).

**20.** The cosine series has only \_\_\_\_\_\_\_\_\_\_ powers of $x$ (odd/even).

**21.** Both series alternate signs: $+ \, - \, + \, - \, \cdots$

**22.** Use the first 3 terms to approximate $\sin(0.5)$:

$\sin(0.5) \approx 0.5 - \frac{(0.5)^3}{6} + \frac{(0.5)^5}{120} = $ \_\_\_\_\_\_\_\_\_\_

Actual: $\sin(0.5) \approx 0.4794$. How close?

**23.** Use the first 3 terms to approximate $\cos(0.5)$:

$\cos(0.5) \approx 1 - \frac{(0.5)^2}{2} + \frac{(0.5)^4}{24} = $ \_\_\_\_\_\_\_\_\_\_

Actual: $\cos(0.5) \approx 0.8776$. How close?

---

### Discovering the Derivative of Sine

**24.** Differentiate each term of $\sin(x) = x - \frac{x^3}{6} + \frac{x^5}{120} - \frac{x^7}{5040} + \cdots$

| Term | Derivative |
|------|------------|
| $x$ | |
| $-\frac{x^3}{6}$ | |
| $\frac{x^5}{120}$ | |
| $-\frac{x^7}{5040}$ | |

**25.** Write the derivative series:

$\frac{d}{dx}\sin(x) = 1 - $ \_\_\_\_\_\_ $ + $ \_\_\_\_\_\_ $ - $ \_\_\_\_\_\_ $ + \cdots$

**26.** Compare to the cosine series. What is $\frac{d}{dx}\sin(x)$?

$$\boxed{\frac{d}{dx}\sin(x) = \cos(x)}$$

---

### Discovering the Derivative of Cosine

**27.** Differentiate each term of $\cos(x) = 1 - \frac{x^2}{2} + \frac{x^4}{24} - \frac{x^6}{720} + \cdots$

| Term | Derivative |
|------|------------|
| $1$ | |
| $-\frac{x^2}{2}$ | |
| $\frac{x^4}{24}$ | |
| $-\frac{x^6}{720}$ | |

**28.** Write the derivative series:

$\frac{d}{dx}\cos(x) = 0 - x + $ \_\_\_\_\_\_ $ - $ \_\_\_\_\_\_ $ + \cdots$

**29.** Factor out $-1$ and compare to the sine series:

$\frac{d}{dx}\cos(x) = -\left(x - \frac{x^3}{6} + \frac{x^5}{120} - \cdots\right) = $ \_\_\_\_\_\_\_\_\_\_

$$\boxed{\frac{d}{dx}\cos(x) = -\sin(x)}$$

---

### The Beautiful Cycle

**30.** Fill in the differentiation cycle:

$\sin(x) \xrightarrow{\frac{d}{dx}}$ \_\_\_\_\_\_ $\xrightarrow{\frac{d}{dx}}$ \_\_\_\_\_\_ $\xrightarrow{\frac{d}{dx}}$ \_\_\_\_\_\_ $\xrightarrow{\frac{d}{dx}}$ \_\_\_\_\_\_

**31.** How many derivatives does it take to get back to $\sin(x)$?

**32.** What is $\frac{d^4}{dx^4}\sin(x)$? (The fourth derivative)

**33.** What is $\frac{d^{100}}{dx^{100}}\cos(x)$?

*Hint: $100 = 4 \times 25$, so we go around the cycle 25 times.*

---

### Integrating Sine and Cosine

**34.** Since $\frac{d}{dx}\sin(x) = \cos(x)$, what is $\int \cos(x) \, dx$?

**35.** Since $\frac{d}{dx}\cos(x) = -\sin(x)$, what is $\int \sin(x) \, dx$?

*Careful with the sign!*

**36.** Verify by differentiating: $\frac{d}{dx}(-\cos(x)) = $ \_\_\_\_\_\_\_\_\_\_

**37.** Fill in the integration cycle:

$\sin(x) \xrightarrow{\int}$ \_\_\_\_\_\_ $\xrightarrow{\int}$ \_\_\_\_\_\_ $\xrightarrow{\int}$ \_\_\_\_\_\_ $\xrightarrow{\int}$ \_\_\_\_\_\_

*(Don't forget the $+C$ in practice, but ignore it for the cycle)*

---

### Chain Rule and Substitution with Trig

**38.** Find: $\frac{d}{dx}\sin(2x) = $ \_\_\_\_\_\_\_\_\_\_

**39.** Find: $\frac{d}{dx}\cos(3x) = $ \_\_\_\_\_\_\_\_\_\_

**40.** Find: $\frac{d}{dx}\sin(x^2) = $ \_\_\_\_\_\_\_\_\_\_

**41.** Find: $\int \cos(4x) \, dx = $ \_\_\_\_\_\_\_\_\_\_ $ + C$

**42.** Find: $\int \sin(2x) \, dx = $ \_\_\_\_\_\_\_\_\_\_ $ + C$

---

## Part C: The Natural Logarithm $\ln(x)$ (16 problems)

### A Different Approach

Unlike $e^x$, $\sin$, and $\cos$, the series for $\ln(x)$ doesn't converge for all $x$. But we can use a related series:

$$\ln(1 + x) = x - \frac{x^2}{2} + \frac{x^3}{3} - \frac{x^4}{4} + \cdots \quad \text{for } -1 < x \leq 1$$

---

**43.** Use the first 4 terms to approximate $\ln(1.5) = \ln(1 + 0.5)$:

$\ln(1.5) \approx 0.5 - \frac{0.25}{2} + \frac{0.125}{3} - \frac{0.0625}{4} = $ \_\_\_\_\_\_\_\_\_\_

Actual: $\ln(1.5) \approx 0.4055$. How close?

**44.** Use the first 4 terms to approximate $\ln(2) = \ln(1 + 1)$:

$\ln(2) \approx 1 - \frac{1}{2} + \frac{1}{3} - \frac{1}{4} = $ \_\_\_\_\_\_\_\_\_\_

Actual: $\ln(2) \approx 0.6931$. (The series converges slowly here!)

---

### The Derivative of $\ln(x)$

**45.** Differentiate each term of $\ln(1+x) = x - \frac{x^2}{2} + \frac{x^3}{3} - \frac{x^4}{4} + \cdots$

| Term | Derivative |
|------|------------|
| $x$ | |
| $-\frac{x^2}{2}$ | |
| $\frac{x^3}{3}$ | |
| $-\frac{x^4}{4}$ | |

**46.** Write the derivative series:

$\frac{d}{dx}\ln(1+x) = 1 - x + $ \_\_\_\_\_\_ $ - $ \_\_\_\_\_\_ $ + \cdots$

**47.** This is a geometric series! Recall: $1 - x + x^2 - x^3 + \cdots = \frac{1}{1+x}$

So: $\frac{d}{dx}\ln(1+x) = $ \_\_\_\_\_\_\_\_\_\_

**48.** Using the chain rule: If $u = 1 + x$, then $\frac{d}{dx}\ln(u) = \frac{1}{u} \cdot \frac{du}{dx} = \frac{1}{1+x} \cdot 1$

For general $\ln(x)$: $\frac{d}{dx}\ln(x) = $ \_\_\_\_\_\_\_\_\_\_

$$\boxed{\frac{d}{dx}\ln(x) = \frac{1}{x}}$$

---

### The Integral of $\frac{1}{x}$

**49.** We now know: $\int \frac{1}{x} \, dx = \ln|x| + C$

Why the absolute value? Because $\ln(x)$ is only defined for $x > 0$, but $\frac{1}{x}$ exists for $x \neq 0$.

**50.** Verify: $\frac{d}{dx}\ln|x| = \frac{1}{x}$ for both $x > 0$ and $x < 0$.

---

### Chain Rule and Substitution with $\ln$

**51.** Find: $\frac{d}{dx}\ln(2x) = $ \_\_\_\_\_\_\_\_\_\_

**52.** Find: $\frac{d}{dx}\ln(x^2) = $ \_\_\_\_\_\_\_\_\_\_

*Two ways: chain rule, or use $\ln(x^2) = 2\ln(x)$ first*

**53.** Find: $\frac{d}{dx}\ln(x^2 + 1) = $ \_\_\_\_\_\_\_\_\_\_

**54.** Find: $\int \frac{2x}{x^2 + 1} \, dx = $ \_\_\_\_\_\_\_\_\_\_ $ + C$

*Hint: Let $u = x^2 + 1$*

**55.** Find: $\int \frac{3x^2}{x^3 + 5} \, dx = $ \_\_\_\_\_\_\_\_\_\_ $ + C$

**56.** Find: $\int \frac{1}{2x + 3} \, dx = $ \_\_\_\_\_\_\_\_\_\_ $ + C$

---

### The $\ln$ and $e^x$ Connection

**57.** Since $e^x$ and $\ln(x)$ are inverse functions:

$\ln(e^x) = $ \_\_\_\_\_\_\_\_\_\_ and $e^{\ln(x)} = $ \_\_\_\_\_\_\_\_\_\_

**58.** Differentiate $\ln(e^x)$ using the chain rule and verify it equals 1.

---

## Part D: Putting It All Together (18 problems)

### Summary Table

| Function | Derivative | Integral |
|----------|------------|----------|
| $e^x$ | $e^x$ | $e^x + C$ |
| $\sin(x)$ | $\cos(x)$ | $-\cos(x) + C$ |
| $\cos(x)$ | $-\sin(x)$ | $\sin(x) + C$ |
| $\ln(x)$ | $\frac{1}{x}$ | $x\ln(x) - x + C$ |
| $\frac{1}{x}$ | $-\frac{1}{x^2}$ | $\ln|x| + C$ |

---

### Mixed Practice — Derivatives

**59.** $\frac{d}{dx}(e^x + \sin(x))$

**60.** $\frac{d}{dx}(x^2 + \cos(x))$

**61.** $\frac{d}{dx}(e^x \cdot x)$ — *Product rule!*

**62.** $\frac{d}{dx}(x \cdot \sin(x))$

**63.** $\frac{d}{dx}\left(\frac{e^x}{x}\right)$ — *Quotient rule!*

**64.** $\frac{d}{dx}(e^{\sin(x)})$ — *Chain rule!*

**65.** $\frac{d}{dx}(\sin(e^x))$

**66.** $\frac{d}{dx}(\ln(\cos(x)))$

---

### Mixed Practice — Integrals

**67.** $\int (e^x + x^2) \, dx$

**68.** $\int (3\cos(x) - 2\sin(x)) \, dx$

**69.** $\int \frac{e^x + 1}{e^x} \, dx$ — *Simplify first!*

**70.** $\int x \cdot e^x \, dx$ — *Integration by parts!*

Let $u = x$, $dv = e^x dx$. Then $du = dx$, $v = e^x$.

$= xe^x - \int e^x \, dx = $ \_\_\_\_\_\_\_\_\_\_

**71.** $\int x \cdot \cos(x) \, dx$ — *Integration by parts!*

**72.** $\int e^x \cdot \sin(x) \, dx$ — *This requires parts twice!* (Challenge)

---

### Euler's Formula — The Grand Unification

**73.** Recall: $e^{ix} = \cos(x) + i\sin(x)$ where $i = \sqrt{-1}$

Using the series for $e^x$ with $x$ replaced by $ix$:

$e^{ix} = 1 + (ix) + \frac{(ix)^2}{2!} + \frac{(ix)^3}{3!} + \frac{(ix)^4}{4!} + \cdots$

Calculate the first few powers of $i$:
- $i^1 = i$
- $i^2 = -1$
- $i^3 = -i$
- $i^4 = 1$
- $i^5 = $ \_\_\_\_\_

**74.** Separate the real and imaginary parts of $e^{ix}$:

Real part: $1 - \frac{x^2}{2!} + \frac{x^4}{4!} - \cdots = $ \_\_\_\_\_\_\_\_\_\_

Imaginary part: $x - \frac{x^3}{3!} + \frac{x^5}{5!} - \cdots = $ \_\_\_\_\_\_\_\_\_\_

**75.** This proves: $e^{ix} = \cos(x) + i\sin(x)$

At $x = \pi$: $e^{i\pi} = \cos(\pi) + i\sin(\pi) = -1 + 0 = -1$

So: $e^{i\pi} + 1 = 0$

This is called **Euler's identity** — often called the most beautiful equation in mathematics!

**76.** Explain in your own words why $e$, $i$, $\pi$, $1$, and $0$ appearing in one equation is remarkable.

---

## Answer Key

### Part A: Exponential Function
1. $\approx 2.708$
2. Very close (within 0.01)
3. $e^x = 1 + x + \frac{x^2}{2} + \frac{x^3}{6} + \frac{x^4}{24} + \frac{x^5}{120} + \cdots$
4. $\approx 1.6458$
5. Derivatives: $0, 1, x, \frac{x^2}{2}, \frac{x^3}{6}, \frac{x^4}{24}$
6. $1 + x + \frac{x^2}{2} + \frac{x^3}{6} + \frac{x^4}{24} + \cdots$
7. It's the same series!
8. $e^x$
9. Integrals: $x, \frac{x^2}{2}, \frac{x^3}{6}, \frac{x^4}{24}, \frac{x^5}{120}$
10. $x + \frac{x^2}{2} + \frac{x^3}{6} + \frac{x^4}{24} + \frac{x^5}{120} + C$
11. Each term is $\frac{x^n}{n!}$
12. $e^x$
13. $e^x$; $e^x + C$
14. $e^x + C$; $e^x$
15. $3e^{3x}$
16. $-e^{-x}$
17. $\frac{1}{2}e^{2x}$
18. $\frac{1}{5}e^{5x}$

### Part B: Sine and Cosine
19. odd
20. even
22. $\approx 0.4792$
23. $\approx 0.8776$
24. Derivatives: $1, -\frac{x^2}{2}, \frac{x^4}{24}, -\frac{x^6}{720}$
25. $1 - \frac{x^2}{2} + \frac{x^4}{24} - \frac{x^6}{720} + \cdots$
26. $\cos(x)$
27. Derivatives: $0, -x, \frac{x^3}{6}, -\frac{x^5}{120}$
28. $-x + \frac{x^3}{6} - \frac{x^5}{120} + \cdots$
29. $-\sin(x)$
30. $\cos(x) \to -\sin(x) \to -\cos(x) \to \sin(x)$
31. 4
32. $\sin(x)$
33. $\cos(x)$
34. $\sin(x) + C$
35. $-\cos(x) + C$
36. $\sin(x)$
37. $-\cos(x) \to -\sin(x) \to \cos(x) \to \sin(x)$
38. $2\cos(2x)$
39. $-3\sin(3x)$
40. $2x\cos(x^2)$
41. $\frac{1}{4}\sin(4x)$
42. $-\frac{1}{2}\cos(2x)$

### Part C: Natural Logarithm
43. $\approx 0.4010$
44. $\approx 0.5833$
45. Derivatives: $1, -x, x^2, -x^3$
46. $1 - x + x^2 - x^3 + \cdots$
47. $\frac{1}{1+x}$
48. $\frac{1}{x}$
51. $\frac{1}{x}$
52. $\frac{2}{x}$
53. $\frac{2x}{x^2 + 1}$
54. $\ln(x^2 + 1)$
55. $\ln(x^3 + 5)$
56. $\frac{1}{2}\ln|2x + 3|$
57. $x$; $x$

### Part D: Mixed Practice
59. $e^x + \cos(x)$
60. $2x - \sin(x)$
61. $e^x \cdot x + e^x = e^x(x + 1)$
62. $\sin(x) + x\cos(x)$
63. $\frac{e^x(x - 1)}{x^2}$
64. $\cos(x) \cdot e^{\sin(x)}$
65. $e^x \cdot \cos(e^x)$
66. $\frac{-\sin(x)}{\cos(x)} = -\tan(x)$
67. $e^x + \frac{x^3}{3} + C$
68. $3\sin(x) + 2\cos(x) + C$
69. $1 + e^{-x}$; $x - e^{-x} + C$
70. $xe^x - e^x + C = e^x(x - 1) + C$
71. $x\sin(x) + \cos(x) + C$
72. $\frac{e^x}{2}(\sin(x) - \cos(x)) + C$
73. $i^5 = i$
74. $\cos(x)$; $\sin(x)$

---

*End of Worksheet 4D*
