# MIT 3.6: Derivatives as Rates of Change (Power Rule, Antiderivatives)

> **Learning outcome:** MIT 5N18396, Section 3 (Functions & Calculus) — 3.6 (understand how a derivative arises as a limit from looking for tangent lines or rates of change). This worksheet goes further than the LO strictly requires (it also introduces integration as the inverse operation), which is useful context but not itself examined.
> **Teaching method:** Pen-and-paper exercises (answer key included below)
> **Pairs with:** [`MIT-3.6_What-Derivatives-and-Integrals-Tell-Us.md`](./MIT-3.6_What-Derivatives-and-Integrals-Tell-Us.md) (interpretation) and [`MIT-3.7_Product-Quotient-Chain-Rule.md`](./MIT-3.7_Product-Quotient-Chain-Rule.md) (the remaining differentiation rules)

---

**AIML Foundations Mathematics — Worksheet 4A: Derivatives and Integrals — Inverse Operations**

> **What This Worksheet Is About**
>
> Derivatives and integrals are **inverses** of each other, just like multiplication and division, or squaring and square roots.
>
> - **Derivative:** Given a function, find its rate of change
> - **Integral:** Given a rate of change, find the original function
>
> But there's a twist: When we "undo" a derivative, we don't get back exactly one function — we get a whole **family** of functions!

---

## Part A: The Power Rule — Both Directions (20 problems)

### Differentiation: Bring down the power, reduce by 1

$$\frac{d}{dx}x^n = n \cdot x^{n-1}$$

### Integration: Increase the power by 1, divide by new power

$$\int x^n \, dx = \frac{x^{n+1}}{n+1} + C \quad \text{(for } n \neq -1\text{)}$$

**Notice they're inverses!**
- Derivative: exponent comes **down** and **decreases**
- Integral: exponent goes **up** and we **divide** by it

---

**Find both the derivative and the integral of each function:**

**1.** $f(x) = x^4$

- $f'(x) = $ \_\_\_\_\_\_\_\_\_\_
- $\int x^4 \, dx = $ \_\_\_\_\_\_\_\_\_\_

**2.** $g(t) = t^5$

- $g'(t) = $ \_\_\_\_\_\_\_\_\_\_
- $\int t^5 \, dt = $ \_\_\_\_\_\_\_\_\_\_

**3.** $h(p) = p^3$

- $h'(p) = $ \_\_\_\_\_\_\_\_\_\_
- $\int p^3 \, dp = $ \_\_\_\_\_\_\_\_\_\_

**4.** $y = x^7$

**5.** $f(m) = m^2$

**6.** $g(r) = r^{10}$

**7.** $h(k) = k^1 = k$

**8.** $y = x^{100}$

---

**Negative and Fractional Exponents:**

**9.** $f(x) = x^{-2}$

- $f'(x) = $ \_\_\_\_\_\_\_\_\_\_
- $\int x^{-2} \, dx = $ \_\_\_\_\_\_\_\_\_\_

**10.** $g(t) = t^{-3}$

**11.** $h(x) = x^{1/2} = \sqrt{x}$

- $h'(x) = $ \_\_\_\_\_\_\_\_\_\_
- $\int x^{1/2} \, dx = $ \_\_\_\_\_\_\_\_\_\_

**12.** $y = x^{1/3}$

**13.** $f(p) = p^{-1/2}$

**14.** $g(n) = n^{3/2}$

---

**The Special Case: What happens when $n = -1$?**

**15.** Try to compute $\int x^{-1} \, dx$ using the formula $\frac{x^{n+1}}{n+1}$.

What goes wrong?

**16.** The integral of $x^{-1} = \frac{1}{x}$ is actually $\ln|x| + C$.

---

**Checking Your Work — Derivatives and Integrals Undo Each Other:**

**17.** If $\int x^3 \, dx = \frac{x^4}{4} + C$, verify by differentiating: $\frac{d}{dx}\left(\frac{x^4}{4} + C\right) = $ \_\_\_\_\_

**18.** If $\frac{d}{dx}(x^5) = 5x^4$, verify by integrating: $\int 5x^4 \, dx = $ \_\_\_\_\_

**19.** Differentiate, then integrate: Start with $f(x) = x^6$
- $f'(x) = $ \_\_\_\_\_
- $\int f'(x) \, dx = $ \_\_\_\_\_
- Do you get back $x^6$? (Plus what?)

**20.** Integrate, then differentiate: Start with $g(x) = x^4$
- $\int g(x) \, dx = $ \_\_\_\_\_
- $\frac{d}{dx}\left[\int g(x) \, dx\right] = $ \_\_\_\_\_
- Do you get back $x^4$?

---

## Part B: Why "+C"? — The Family of Antiderivatives (14 problems)

Consider these three functions:
- $f(x) = x^2$
- $g(x) = x^2 + 5$
- $h(x) = x^2 - 17$

**21.** Find the derivative of each:
- $f'(x) = $ \_\_\_\_\_
- $g'(x) = $ \_\_\_\_\_
- $h'(x) = $ \_\_\_\_\_

**22.** What do you notice? Why does this happen?

**23.** The functions $x^2$, $x^2 + 5$, and $x^2 - 17$ are all different, but they have the \_\_\_\_\_\_\_\_\_\_ derivative.

**24.** Graphically: Sketch $y = x^2$, $y = x^2 + 3$, and $y = x^2 - 2$ on the same axes.

- How are these parabolas related?
- At any given x-value, do they have the same slope?

---

**The Key Insight:**

> When we integrate $2x$, we get $x^2 + C$ where $C$ is **any constant**.
>
> This represents a whole **family** of functions — infinitely many parabolas, all with the same shape but shifted up or down.

---

**25.** Write three different functions whose derivative is $3x^2$.

**26.** Write three different functions whose derivative is $5t^4$.

**27.** Write the general antiderivative (with +C) of $4p^3$.

**28.** If $F'(x) = 6x^5$, what is $F(x)$?

---

**Finding a Specific Function — Initial Conditions:**

If we know $F'(x) = 2x$ AND $F(0) = 7$, we can find the specific function:

$F(x) = x^2 + C$

$F(0) = 0^2 + C = 7$, so $C = 7$

Therefore $F(x) = x^2 + 7$

---

**29.** Find $F(x)$ if $F'(x) = 3x^2$ and $F(0) = 5$.

**30.** Find $G(t)$ if $G'(t) = 4t^3$ and $G(1) = 10$.

**31.** Find $H(p)$ if $H'(p) = 2p + 1$ and $H(2) = 0$.

**32.** A ball's velocity is $v(t) = 20 - 10t$ m/s. Its position is $s(t) = \int v(t) \, dt$.

- (a) Find $s(t)$ with the constant $C$.
- (b) If the ball starts at height $s(0) = 5$ meters, find $C$.
- (c) Write the complete position function.

**33.** An object's acceleration is $a(t) = 6$ m/s². Starting from rest ($v(0) = 0$):

- (a) Find velocity: $v(t) = \int a(t) \, dt$
- (b) If position $s(0) = 10$, find $s(t) = \int v(t) \, dt$.

**34.** Explain in your own words why integration has "+C" but differentiation doesn't.

---

## Part C: Constants and Sums — Both Directions (16 problems)

### Derivative Rules:
- $\frac{d}{dx}(c) = 0$ (constant rule)
- $\frac{d}{dx}[cf(x)] = c \cdot f'(x)$ (constant multiple)
- $\frac{d}{dx}[f(x) + g(x)] = f'(x) + g'(x)$ (sum rule)

### Integral Rules (the reverses):
- $\int 0 \, dx = C$ (integrating zero gives a constant)
- $\int c \cdot f(x) \, dx = c \cdot \int f(x) \, dx$ (constant multiple)
- $\int [f(x) + g(x)] \, dx = \int f(x) \, dx + \int g(x) \, dx$ (sum rule)

**Also:** $\int c \, dx = cx + C$ (integrating a constant)

---

**Find both the derivative and the integral:**

**35.** $f(x) = 5x^3$

- $f'(x) = $ \_\_\_\_\_\_\_\_\_\_
- $\int 5x^3 \, dx = $ \_\_\_\_\_\_\_\_\_\_

**36.** $g(t) = -2t^4$

**37.** $h(p) = \frac{1}{2}p^6$

**38.** $y = 7$ (a constant function)

- $\frac{dy}{dx} = $ \_\_\_\_\_\_\_\_\_\_
- $\int 7 \, dx = $ \_\_\_\_\_\_\_\_\_\_

**39.** $f(m) = -3$

---

**Sums and Differences:**

**40.** $f(x) = x^3 + x^2$

- $f'(x) = $ \_\_\_\_\_\_\_\_\_\_
- $\int (x^3 + x^2) \, dx = $ \_\_\_\_\_\_\_\_\_\_

**41.** $g(t) = t^4 - t^2$

**42.** $h(r) = 3r^2 + 2r - 5$

**43.** $y = 4x^3 - 6x^2 + 2x - 1$

**44.** $f(k) = k^5 - 3k^3 + 2k$

**45.** $g(n) = 2n^4 + n^3 - 5n^2 + 4n - 7$

---

**Verify by reversing:**

**46.** Check problem 40: Differentiate your integral. Do you get back $x^3 + x^2$?

**47.** Check problem 43: Integrate your derivative. Do you get back $4x^3 - 6x^2 + 2x - 1$ (plus C)?

---

**Rewriting Before Integrating:**

**48.** Find $\int \frac{3}{x^2} \, dx$

*Hint: Rewrite as $3x^{-2}$ first*

**49.** Find $\int \frac{5}{\sqrt{t}} \, dt$

**50.** Find $\int \left(x + \frac{1}{x^2}\right) dx$

---

## Part D: Polynomials — Complete Practice (16 problems)

**Find the derivative:**

**51.** $f(x) = 2x^5 - 3x^4 + x^3 - 7x + 2$

**52.** $g(t) = \frac{t^4}{4} - \frac{t^3}{3} + \frac{t^2}{2}$

**53.** $h(p) = (p + 2)(p - 3)$ *(expand first)*

**54.** $y = (x - 1)^2$

---

**Find the integral:**

**55.** $\int (3x^2 - 4x + 5) \, dx$

**56.** $\int (t^4 - 2t^3 + t - 3) \, dt$

**57.** $\int (6m^5 - 4m^3 + 2m) \, dm$

**58.** $\int (u^2 + 1)^2 \, du$ *(expand first!)*

---

**Mixed — Derivative or Integral as Specified:**

**59.** $\frac{d}{dx}(x^4 - 3x^2 + 2)$

**60.** $\int (4r^3 - 6r) \, dr$

**61.** $\frac{d}{dt}(t^6 + 2t^4 - t)$

**62.** $\int (5k^4 - 3k^2 + 1) \, dk$

---

**Round-Trip Problems:**

**63.** Start with $f(x) = x^5$.
- (a) Differentiate: $f'(x) = $
- (b) Integrate your answer: $\int f'(x) \, dx = $
- (c) Is this $f(x)$? Explain.

**64.** Start with $g(t) = t^3 - 4t$.
- (a) Integrate: $\int g(t) \, dt = $
- (b) Differentiate your answer.
- (c) Is this $g(t)$? Explain.

**65.** Why does integrating then differentiating give you back exactly what you started with, but differentiating then integrating gives you the original plus a constant?

**66.** Complete this analogy:

Squaring and square roots are inverses: $(\sqrt{x})^2 = x$ and $\sqrt{x^2} = |x|$ (almost x, but not quite for negatives)

Similarly: $\frac{d}{dx}\left[\int f(x) \, dx\right] = $ \_\_\_\_\_ and $\int \frac{d}{dx}[f(x)] \, dx = $ \_\_\_\_\_

---

## Part E: Building Intuition — What's Really Happening (10 problems)

**67.** The derivative of position is velocity. The integral of velocity is \_\_\_\_\_\_\_\_\_\_.

**68.** The derivative of velocity is acceleration. The integral of acceleration is \_\_\_\_\_\_\_\_\_\_.

**69.** If you know an object's acceleration at all times, can you determine its exact position? What additional information do you need?

**70.** Match the physical quantities:

| Function | Derivative | Integral |
|----------|------------|----------|
| Position | | |
| Velocity | | |
| Acceleration | | |

---

**71.** A car's velocity is $v(t) = 3t^2$ m/s.

- (a) What is the acceleration $a(t) = v'(t)$?
- (b) What is the position $s(t) = \int v(t) \, dt$?
- (c) If $s(0) = 0$, what is the specific position function?
- (d) How far has the car traveled from $t = 0$ to $t = 2$?

**72.** An object's position is $s(t) = t^3 - 6t^2 + 9t$.

- (a) Find velocity $v(t) = s'(t)$.
- (b) Find acceleration $a(t) = v'(t)$.
- (c) When is velocity zero?
- (d) When is acceleration zero?

---

**73.** Revenue $R(q)$ depends on quantity sold $q$.

- **Marginal revenue** is $R'(q)$ — the extra revenue from one more unit.
- If you know marginal revenue, $\int R'(q) \, dq$ gives you \_\_\_\_\_\_\_\_\_\_.

**74.** Cost $C(q)$ depends on quantity produced.

- **Marginal cost** is $C'(q)$.
- If marginal cost is $MC(q) = 6q + 10$, find the cost function $C(q)$.
- If fixed costs are $C(0) = 500$, find the specific cost function.

---

**75.** Population growth rate is $P'(t) = 1000 + 50t$ people per year.

- (a) Find $P(t)$, the population function.
- (b) If the population at $t = 0$ is 50,000, find the specific function.
- (c) What is the population after 10 years?

**76.** Water flows into a tank at rate $r(t) = 100 - 2t$ liters per minute.

- (a) The amount of water $W(t) = \int r(t) \, dt$. Find it.
- (b) If the tank starts empty, $W(0) = 0$. Find the specific function.
- (c) How much water is in the tank after 10 minutes?
- (d) When does the tank stop filling (when $r(t) = 0$)?

---

## Part F: The Fundamental Theorem Preview (6 problems)

The **Fundamental Theorem of Calculus** connects derivatives and integrals precisely:

$$\int_a^b f(x) \, dx = F(b) - F(a)$$

where $F'(x) = f(x)$.

This says: To find the integral from $a$ to $b$, find ANY antiderivative $F$, then compute $F(b) - F(a)$.

(The $+C$ cancels out!)

---

**Evaluate these definite integrals:**

**77.** $\int_0^2 x^2 \, dx$

- Antiderivative: $F(x) = \frac{x^3}{3}$
- $F(2) - F(0) = \frac{8}{3} - 0 = $ \_\_\_\_\_

**78.** $\int_1^3 2x \, dx$

**79.** $\int_0^4 (3t^2 - 2t) \, dt$

**80.** $\int_{-1}^{1} x^3 \, dx$

*Hint: What symmetry do you notice?*

**81.** $\int_1^4 \sqrt{x} \, dx$

**82.** $\int_0^3 (x^2 + 1) \, dx$

---

## Answer Key

### Part A
1. $f'(x) = 4x^3$; $\int x^4 dx = \frac{x^5}{5} + C$
2. $g'(t) = 5t^4$; $\int t^5 dt = \frac{t^6}{6} + C$
3. $h'(p) = 3p^2$; $\int p^3 dp = \frac{p^4}{4} + C$
4. $7x^6$; $\frac{x^8}{8} + C$
5. $2m$; $\frac{m^3}{3} + C$
6. $10r^9$; $\frac{r^{11}}{11} + C$
7. $1$; $\frac{k^2}{2} + C$
8. $100x^{99}$; $\frac{x^{101}}{101} + C$
9. $-2x^{-3}$; $\frac{x^{-1}}{-1} + C = -\frac{1}{x} + C$
10. $-3t^{-4}$; $\frac{t^{-2}}{-2} + C = -\frac{1}{2t^2} + C$
11. $\frac{1}{2}x^{-1/2}$; $\frac{x^{3/2}}{3/2} + C = \frac{2}{3}x^{3/2} + C$
12. $\frac{1}{3}x^{-2/3}$; $\frac{x^{4/3}}{4/3} + C = \frac{3}{4}x^{4/3} + C$
13. $-\frac{1}{2}p^{-3/2}$; $\frac{p^{1/2}}{1/2} + C = 2\sqrt{p} + C$
14. $\frac{3}{2}n^{1/2}$; $\frac{n^{5/2}}{5/2} + C = \frac{2}{5}n^{5/2} + C$
15. Division by zero ($n + 1 = 0$)
17. $x^3$
18. $x^5 + C$
19. $6x^5$; $x^6 + C$; Yes, plus C
20. $\frac{x^5}{5} + C$; $x^4$; Yes exactly

### Part B
21. All equal $2x$
22. Constants disappear when differentiating
23. same
25. $x^3$, $x^3 + 1$, $x^3 - 100$ (any three)
26. $t^5$, $t^5 + 7$, $t^5 - \pi$ (any three)
27. $p^4 + C$
28. $x^6 + C$
29. $F(x) = x^3 + 5$
30. $G(t) = t^4 + 6$
31. $H(p) = p^2 + p - 6$
32. (a) $20t - 5t^2 + C$ (b) $C = 5$ (c) $s(t) = 20t - 5t^2 + 5$
33. (a) $v(t) = 6t$ (b) $s(t) = 3t^2 + 10$

### Part C
35. $15x^2$; $\frac{5x^4}{4} + C$
36. $-8t^3$; $-\frac{2t^5}{5} + C$
37. $3p^5$; $\frac{p^7}{14} + C$
38. $0$; $7x + C$
39. $0$; $-3x + C$
40. $3x^2 + 2x$; $\frac{x^4}{4} + \frac{x^3}{3} + C$
41. $4t^3 - 2t$; $\frac{t^5}{5} - \frac{t^3}{3} + C$
42. $6r + 2$; $r^3 + r^2 - 5r + C$
43. $12x^2 - 12x + 2$; $x^4 - 2x^3 + x^2 - x + C$
44. $5k^4 - 9k^2 + 2$; $\frac{k^6}{6} - \frac{3k^4}{4} + k^2 + C$
45. $8n^3 + 3n^2 - 10n + 4$; $\frac{2n^5}{5} + \frac{n^4}{4} - \frac{5n^3}{3} + 2n^2 - 7n + C$
48. $-3x^{-1} + C = -\frac{3}{x} + C$
49. $10\sqrt{t} + C$
50. $\frac{x^2}{2} - \frac{1}{x} + C$

### Part D
51. $10x^4 - 12x^3 + 3x^2 - 7$
52. $t^3 - t^2 + t$
53. $h(p) = p^2 - p - 6$, $h'(p) = 2p - 1$
54. $y = x^2 - 2x + 1$, $y' = 2x - 2$
55. $x^3 - 2x^2 + 5x + C$
56. $\frac{t^5}{5} - \frac{t^4}{2} + \frac{t^2}{2} - 3t + C$
57. $m^6 - m^4 + m^2 + C$
58. $(u^2+1)^2 = u^4 + 2u^2 + 1$; $\frac{u^5}{5} + \frac{2u^3}{3} + u + C$
59. $4x^3 - 6x$
60. $r^4 - 3r^2 + C$
61. $6t^5 + 8t^3 - 1$
62. $k^5 - k^3 + k + C$
63. (a) $5x^4$ (b) $x^5 + C$ (c) Original plus constant
64. (a) $\frac{t^4}{4} - 2t^2 + C$ (b) $t^3 - 4t$ (c) Exactly $g(t)$
66. $f(x)$; $f(x) + C$

### Part E
67. position
68. velocity
71. (a) $6t$ (b) $t^3 + C$ (c) $t^3$ (d) $8$ m
72. (a) $3t^2 - 12t + 9$ (b) $6t - 12$ (c) $t = 1, 3$ (d) $t = 2$
74. $C(q) = 3q^2 + 10q + 500$
75. (b) $P(t) = 1000t + 25t^2 + 50000$ (c) $62,500$
76. (b) $W(t) = 100t - t^2$ (c) $900$ L (d) $t = 50$ min

### Part F
77. $\frac{8}{3}$
78. $8$
79. $48$
80. $0$ (odd function, symmetric interval)
81. $\frac{14}{3}$
82. $12$

---

*End of worksheet.*
