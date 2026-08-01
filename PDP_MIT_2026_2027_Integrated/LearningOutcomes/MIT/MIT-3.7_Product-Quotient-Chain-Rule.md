# MIT 3.7: Product, Quotient & Chain Rule Differentiation

> **Learning outcome:** MIT 5N18396, Section 3 (Functions & Calculus) — 3.7 (use the sum, product and quotient formulas for differentiation and the chain rule to differentiate simple functions that are a composition of several functions). This is the single most direct source-content match found anywhere in the four repos for an explicit MIT sub-outcome.
> **Pulled in from:** `mathematics` repo, `markdown/worksheet_04c_advanced_rules.md`
> **Teaching method:** Pen-and-paper exercises (answer key included below)
> **Pairs with:** [`MIT-3.6_Derivatives-Integrals-and-Inverse-Operations.md`](./MIT-3.6_Derivatives-Integrals-and-Inverse-Operations.md) and [`MIT-3.6_What-Derivatives-and-Integrals-Tell-Us.md`](./MIT-3.6_What-Derivatives-and-Integrals-Tell-Us.md)

---

**AIML Foundations Mathematics — Worksheet 4C: Advanced Rules — Derivatives and Their Integral Inverses**

> **What This Worksheet Is About**
>
> Each derivative rule has an integral counterpart:
> - **Product Rule** ↔ **Integration by Parts**
> - **Chain Rule** ↔ **Substitution (u-sub)**
>
> These are inverse operations!

---

## Part A: The Product Rule (12 problems)

$$\frac{d}{dx}[u \cdot v] = u' \cdot v + u \cdot v'$$

**Find the derivative:**

**1.** $f(x) = x^2(x + 1)$

**2.** $g(t) = t^3(t - 4)$

**3.** $h(p) = (p + 2)(p - 5)$

**4.** $y = (2x + 1)(3x - 2)$

**5.** $f(m) = m^2(m^2 + 3m - 1)$

**6.** $g(r) = (r^2 - 1)(r^2 + 1)$

**7.** Verify problem 3 by expanding first.

**8.** Verify problem 6 by simplifying first: $(r^2-1)(r^2+1) = ?$

---

**With Chain Rule:**

**9.** $h(x) = x^2(x + 1)^3$

**10.** $y = (t + 1)^2(t - 1)^3$

**11.** $f(k) = k(2k + 1)^4$

**12.** $g(n) = (n^2 + 1)^2(n - 1)$

---

## Part B: Integration by Parts — Reversing Product Rule (10 problems)

$$\int u \, dv = uv - \int v \, du$$

**Connection:** If $\frac{d}{dx}[f \cdot g] = f'g + fg'$, then $\int (f'g + fg') dx = fg + C$

---

**13.** The derivative of $x^2(x+1)$ is $3x^2 + 2x$.

Therefore: $\int (3x^2 + 2x) dx = $ \_\_\_\_\_\_\_\_\_\_

**14.** The derivative of $(x-1)(x+3)$ is $2x + 2$.

Therefore: $\int (2x + 2) dx = $ \_\_\_\_\_\_\_\_\_\_

**15.** Find $\frac{d}{dx}[(2x+1)(x-2)]$. Then verify $\int [\text{your answer}] dx$ gives back $(2x+1)(x-2) + C$.

**16.** Start with $f(x) = x(x+1)^2$. Differentiate, then integrate your answer.

---

**Direct Integration (for comparison):**

**17.** $\int (3x^2 + 2x) dx = $

**18.** $\int (2x + 2) dx = $

**19.** Compare: Are problems 13 & 17 the same? Are 14 & 18 the same (up to constants)?

**20.** Explain why integration is "harder" than differentiation:

- Differentiation: clear rules always work
- Integration: may require \_\_\_\_\_\_\_\_\_\_ or may not have closed form

---

## Part C: The Quotient Rule (10 problems)

$$\frac{d}{dx}\left[\frac{u}{v}\right] = \frac{u'v - uv'}{v^2}$$

**Find the derivative:**

**23.** $f(x) = \frac{x}{x + 2}$

**24.** $g(t) = \frac{t^2}{t - 1}$

**25.** $h(p) = \frac{p + 1}{p - 1}$

**26.** $y = \frac{x^2 + 1}{x}$

**27.** $f(m) = \frac{1}{m^2 + 1}$

**28.** $g(r) = \frac{r^3}{r^2 + 1}$

---

**Quotient Rule vs. Rewriting:**

**29.** Find $\frac{d}{dx}\left[\frac{1}{x^3}\right]$ two ways:
- (a) Quotient rule
- (b) Rewrite as $x^{-3}$

**30.** Find $\frac{d}{dx}\left[\frac{x^4 + 2x^2}{x^2}\right]$ by simplifying first.

**31.** Simplify first, then differentiate: $\frac{x^2 - 1}{x + 1}$

**32.** When MUST you use quotient rule? (When denominator has \_\_\_\_\_\_\_\_ that don't cancel)

---

## Part D: The Chain Rule (16 problems)

$$\frac{d}{dx}[f(g(x))] = f'(g(x)) \cdot g'(x)$$

**"Derivative of outside × derivative of inside"**

---

**Find the derivative:**

**33.** $f(x) = (x + 3)^4$

**34.** $g(t) = (2t - 1)^5$

**35.** $h(p) = (p^2 + 1)^3$

**36.** $y = (3x^2 - x)^4$

**37.** $f(m) = (m^3 + m)^2$

**38.** $g(r) = (1 - r^2)^6$

---

**Negative and Fractional Powers:**

**39.** $h(x) = (x + 1)^{-1}$

**40.** $y = (t^2 + 4)^{-2}$

**41.** $f(k) = \sqrt{k + 5}$

**42.** $g(n) = \sqrt{n^2 + 1}$

---

**Verify by Expanding:**

**43.** $(x + 2)^3$: Use chain rule, then expand and differentiate. Same answer?

**44.** $(2x - 1)^2$: Both methods.

---

**Combining Rules:**

**45.** $f(x) = x^2(x + 1)^3$ (product + chain)

**46.** $g(t) = \frac{t}{(t + 1)^2}$ (quotient + chain)

**47.** $h(x) = \sqrt{x(x + 4)}$ (chain with product inside)

**48.** $y = \left(\frac{x}{x+1}\right)^3$ (chain on quotient)

---

## Part E: Substitution — Reversing the Chain Rule (16 problems)

$$\int f(g(x)) \cdot g'(x) \, dx = F(g(x)) + C$$

**Let $u = g(x)$, then $du = g'(x) dx$**

---

**Perfect Cases:**

**49.** $\int 3x^2(x^3 + 1)^4 \, dx$

Let $u = x^3 + 1$, $du = 3x^2 dx$

$= \int u^4 du = $

**50.** $\int 2t(t^2 - 3)^5 \, dt$

**51.** $\int 4p^3(p^4 + 2)^{-2} \, dp$

**52.** $\int \frac{6x^2}{\sqrt{x^3 + 1}} \, dx$

**53.** $\int (2m + 1)(m^2 + m)^3 \, dm$

---

**Adjusting Constants:**

**54.** $\int x(x^2 + 1)^3 \, dx$

We need $2x dx$ but have $x dx$. So: $x dx = \frac{1}{2}(2x dx) = \frac{1}{2}du$

$= \frac{1}{2}\int u^3 du = $

**55.** $\int t(t^2 + 5)^4 \, dt$

**56.** $\int \frac{x}{\sqrt{x^2 + 4}} \, dx$

**57.** $\int p^2(p^3 - 1)^2 \, dp$

---

**Verify by Differentiating:**

**58.** Check problem 49: Differentiate $\frac{(x^3+1)^5}{5}$ using chain rule.

**59.** Check problem 54: Differentiate $\frac{(x^2+1)^4}{8}$.

---

**Connection to Chain Rule:**

**60.** Chain rule: $\frac{d}{dx}[(x^2+1)^5] = 10x(x^2+1)^4$

Therefore: $\int 10x(x^2+1)^4 dx = $ \_\_\_\_\_\_\_\_\_\_

**61.** Chain rule: $\frac{d}{dx}[(t^3-2)^4] = 12t^2(t^3-2)^3$

Therefore: $\int 12t^2(t^3-2)^3 dt = $ \_\_\_\_\_\_\_\_\_\_

**62.** Explain: Substitution is "chain rule backwards."

---

**More Practice:**

**63.** $\int (3x - 2)^4 \, dx$

**64.** $\int (5t + 1)^{-3} \, dt$

---

## Part F: Combining Everything (10 problems)

**Differentiate:**

**65.** $\frac{x^2}{(x+1)^3}$

**66.** $x(x^2 + 1)^{1/2}$

**67.** $\frac{(x-1)^2}{(x+1)^2}$

---

**Integrate:**

**68.** $\int \frac{2x}{(x^2 + 1)^3} dx$

**69.** $\int \frac{x}{\sqrt{x^2 + 9}} dx$

**70.** $\int (x+1)(x^2 + 2x)^4 dx$

*Hint: $\frac{d}{dx}(x^2 + 2x) = 2x + 2 = 2(x + 1)$*

---

**Round-Trips:**

**71.** Start with $(x^2 + 1)^3$. Differentiate, then integrate back.

**72.** Start with $x(x + 1)^2$. Differentiate, then integrate back.

**73.** Start with $\frac{x}{x+1}$. Differentiate, then integrate back.

**74.** Why does "differentiate then integrate" give $f(x) + C$, but "integrate then differentiate" gives exactly $f(x)$?

---

## Answer Key

### Part A
1. $3x^2 + 2x$
2. $4t^3 - 12t^2$
3. $2p - 3$
4. $12x - 1$
5. $5m^4 + 12m^3 - 3m^2$
6. $4r^3$
9. $2x(x+1)^3 + x^2 \cdot 3(x+1)^2 = x(x+1)^2(5x + 2)$
10. $2(t+1)(t-1)^3 + (t+1)^2 \cdot 3(t-1)^2 = (t+1)(t-1)^2(5t - 1)$
11. $(2k+1)^4 + k \cdot 4(2k+1)^3 \cdot 2 = (2k+1)^3(10k + 1)$
12. $2(n^2+1) \cdot 2n \cdot (n-1) + (n^2+1)^2 = (n^2+1)(5n^2 - 4n + 1)$

### Part B
13. $x^3 + x^2 + C$ (or $x^2(x+1) + C$)
14. $x^2 + 2x + C$ (or $(x-1)(x+3) + C = x^2 + 2x - 3 + C$)
15. Derivative: $4x - 3$; integral gives $(2x+1)(x-2) + C$
17. $x^3 + x^2 + C$
18. $x^2 + 2x + C$
19. Yes (differ by constant)

### Part C
23. $\frac{2}{(x+2)^2}$
24. $\frac{t^2 - 2t}{(t-1)^2}$
25. $\frac{-2}{(p-1)^2}$
26. $1 - \frac{1}{x^2}$
27. $\frac{-2m}{(m^2+1)^2}$
28. $\frac{r^4 + 3r^2}{(r^2+1)^2}$
29. Both: $-3x^{-4}$
30. Simplify to $x^2 + 2$; derivative: $2x$
31. Simplify to $x - 1$; derivative: $1$

### Part D
33. $4(x + 3)^3$
34. $10(2t - 1)^4$
35. $6p(p^2 + 1)^2$
36. $4(6x - 1)(3x^2 - x)^3$
37. $2(3m^2 + 1)(m^3 + m)$
38. $-12r(1 - r^2)^5$
39. $-(x + 1)^{-2}$
40. $-4t(t^2 + 4)^{-3}$
41. $\frac{1}{2}(k + 5)^{-1/2} = \frac{1}{2\sqrt{k+5}}$
42. $\frac{n}{\sqrt{n^2+1}}$
45. $2x(x+1)^3 + 3x^2(x+1)^2 = x(x+1)^2(5x+2)$
46. $\frac{(t+1)^2 - 2t(t+1)}{(t+1)^4} = \frac{1-t}{(t+1)^3}$
47. $\frac{2x + 4}{2\sqrt{x(x+4)}} = \frac{x+2}{\sqrt{x(x+4)}}$
48. $\frac{3x^2}{(x+1)^4}$

### Part E
49. $\frac{(x^3+1)^5}{5} + C$
50. $\frac{(t^2-3)^6}{6} + C$
51. $\frac{-1}{p^4+2} + C$
52. $2\sqrt{x^3+1} + C$
53. $\frac{(m^2+m)^4}{4} + C$
54. $\frac{(x^2+1)^4}{8} + C$
55. $\frac{(t^2+5)^5}{10} + C$
56. $\sqrt{x^2+4} + C$
57. $\frac{(p^3-1)^3}{9} + C$
60. $(x^2+1)^5 + C$
61. $(t^3-2)^4 + C$
63. $\frac{(3x-2)^5}{15} + C$
64. $\frac{-1}{10(5t+1)^2} + C$

### Part F
65. $\frac{2x(x+1)^3 - x^2 \cdot 3(x+1)^2}{(x+1)^6} = \frac{x(2-x)}{(x+1)^4}$
66. $(x^2+1)^{1/2} + \frac{x^2}{\sqrt{x^2+1}} = \frac{2x^2+1}{\sqrt{x^2+1}}$
68. $\frac{-1}{2(x^2+1)^2} + C$
69. $\sqrt{x^2+9} + C$
70. $\frac{(x^2+2x)^5}{10} + C$
71. Derivative: $6x(x^2+1)^2$; Integral: $(x^2+1)^3 + C$ ✓
74. Differentiation loses information (the constant), integration adds it back arbitrarily.

---

*End of worksheet.*
