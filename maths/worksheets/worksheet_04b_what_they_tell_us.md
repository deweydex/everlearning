# Worksheet 4B: What Derivatives and Integrals Tell Us
**AIML Foundations Mathematics**  
**Dublin and Dún Laoghaire ETB**  
**Instructor: Josh Aaron**

---

> **What This Worksheet Is About**
>
> We've learned *how* to compute derivatives and integrals. Now: *what do they mean*?
>
> - **Derivatives** → rate of change, slope, velocity, increasing/decreasing
> - **Integrals** → accumulation, area, total distance, total quantity
>
> These interpretations are why calculus is so powerful!

---

## Part A: Derivatives — Rate of Change and Slope (16 problems)

| Derivative | Meaning |
|------------|---------|
| $f'(x) > 0$ | Function increasing ↗ |
| $f'(x) < 0$ | Function decreasing ↘ |
| $f'(x) = 0$ | Horizontal tangent (potential max/min) |
| $f''(x) > 0$ | Concave up ∪ |
| $f''(x) < 0$ | Concave down ∩ |

---

**1.** For $f(x) = x^2$, $f'(x) = 2x$.

- (a) Where is $f$ increasing? Decreasing?
- (b) Where is the tangent horizontal?
- (c) What is the slope at $x = 3$?

**2.** For $g(x) = x^3 - 3x$:

- (a) Find $g'(x)$.
- (b) Find critical points (where $g'(x) = 0$).
- (c) Classify as local max or min.

**3.** For $h(t) = t^4 - 8t^2$:

- (a) Find all critical points.
- (b) Use the first or second derivative test to classify each.

**4.** Find the tangent line to $f(x) = x^2$ at $(2, 4)$.

**5.** Find the tangent line to $g(x) = x^3 - x$ at $x = 1$.

**6.** At what point(s) on $y = x^3 - 12x$ is the tangent horizontal?

---

**Physics Applications:**

**7.** Height: $h(t) = 20t - 5t^2$ meters.

- (a) Find velocity $v(t) = h'(t)$.
- (b) When is velocity zero? What's happening then?
- (c) Find acceleration $a(t) = h''(t)$. Interpret it.

**8.** Position: $s(t) = t^3 - 6t^2 + 9t$ meters.

- (a) Find velocity and acceleration.
- (b) When is the object at rest?
- (c) When is acceleration zero?

---

**Second Derivative and Concavity:**

**9.** For $f(x) = x^3$:
- Where is $f''(x) > 0$? (Concave up)
- Where is $f''(x) < 0$? (Concave down)
- Where is the inflection point?

**10.** For $g(x) = x^4 - 6x^2$:
- Find inflection points.
- Describe concavity on each interval.

---

**Optimization:**

**11.** Profit: $P(x) = -x^2 + 80x - 1200$.
- Find the quantity maximizing profit.
- Find maximum profit.

**12.** Area with fixed perimeter: A rectangle has perimeter 100m.
- Express area as $A(w) = w(50 - w) = 50w - w^2$.
- Find dimensions maximizing area.

**13.** A ball's height is $h(t) = -5t^2 + 30t + 10$.
- When does it reach maximum height?
- What is the maximum height?

**14.** Revenue: $R(p) = 500p - 2p^2$.
- Find price maximizing revenue.
- Find maximum revenue.

**15.** Cost: $C(q) = q^3 - 12q^2 + 60q + 100$.
- Find marginal cost $C'(q)$.
- At what quantity is marginal cost minimized?

**16.** Summary: The derivative being zero tells us \_\_\_\_\_\_\_\_\_\_, and the second derivative's sign tells us \_\_\_\_\_\_\_\_\_\_.

---

## Part B: Integrals — Accumulation and Area (16 problems)

| Integral | Meaning |
|----------|---------|
| $\int_a^b f(x) \, dx$ | Signed area under curve |
| $\int v(t) \, dt$ | Displacement |
| $\int r(t) \, dt$ | Total quantity accumulated |

---

**Area Under Curves:**

**17.** Find the area under $f(x) = 3$ from $x = 1$ to $x = 5$.
- Geometrically: rectangle with base \_\_\_ and height \_\_\_
- By integral: $\int_1^5 3 \, dx = $

**18.** Find the area under $f(x) = x$ from $x = 0$ to $x = 4$.
- Geometrically: triangle
- By integral: $\int_0^4 x \, dx = $

**19.** $\int_0^2 x^2 \, dx = $

**20.** $\int_1^3 (2x + 1) \, dx = $

---

**Signed Area:**

**21.** $\int_{-2}^2 x \, dx = $ \_\_\_\_\_ 

Why? (Think about symmetry)

**22.** $\int_{-1}^1 x^3 \, dx = $ \_\_\_\_\_ 

This is an odd function on a symmetric interval.

**23.** $\int_{-2}^2 x^2 \, dx = $ \_\_\_\_\_

This is an even function: $\int_{-a}^a f(x) dx = 2\int_0^a f(x) dx$

**24.** For $f(x) = x - 1$ from $x = 0$ to $x = 2$:
- Sketch the function.
- Where is it positive? Negative?
- Calculate $\int_0^2 (x - 1) dx$. Interpret the result.

---

**Physical Applications:**

**25.** Velocity: $v(t) = 3t^2$ m/s. Find displacement from $t = 0$ to $t = 2$.

**26.** Velocity: $v(t) = t - 2$ m/s from $t = 0$ to $t = 4$.
- (a) When is the object moving forward? Backward?
- (b) Find net displacement: $\int_0^4 (t - 2) dt$
- (c) Find total distance traveled.

**27.** Flow rate: $r(t) = 100 - 4t$ liters/min.
- Find total flow from $t = 0$ to $t = 10$.

**28.** Population growth rate: $P'(t) = 200 + 10t$ people/year.
- Find total growth over 5 years.

---

**Accumulation Functions:**

**29.** Let $A(x) = \int_0^x t^2 \, dt$.
- (a) Compute $A(x)$ explicitly.
- (b) Find $A(1)$, $A(2)$, $A(3)$.
- (c) Find $A'(x)$. What do you notice?

**30.** If $F(x) = \int_1^x (t^3 + 1) dt$, what is $F'(x)$?

(Use the Fundamental Theorem — no need to compute the integral!)

**31.** If $G(x) = \int_0^x \sqrt{t} \, dt$, what is $G'(x)$?

**32.** Explain: "Integrating then differentiating gets you back to where you started."

---

## Part C: The Fundamental Theorem — Tying It Together (12 problems)

**The Fundamental Theorem of Calculus:**

1. $\frac{d}{dx}\left[\int_a^x f(t) \, dt\right] = f(x)$

2. $\int_a^b f(x) \, dx = F(b) - F(a)$ where $F' = f$

---

**Using Part 1:**

**33.** $\frac{d}{dx}\left[\int_0^x t^4 \, dt\right] = $

**34.** $\frac{d}{dx}\left[\int_2^x (3s^2 - s) \, ds\right] = $

**35.** $\frac{d}{dx}\left[\int_1^x \frac{1}{t^2} \, dt\right] = $

---

**Using Part 2:**

**36.** $\int_0^3 2x \, dx = $ (use antiderivative $x^2$)

**37.** $\int_1^4 (x^2 - 1) \, dx = $

**38.** $\int_0^8 x^{1/3} \, dx = $

**39.** $\int_1^e \frac{1}{x} \, dx = $ (antiderivative is $\ln x$; we'll derive this in 4D!)

---

**Round-Trip Verification:**

**40.** Start with $f(x) = x^3$.
- Integrate: $\int f(x) dx = $
- Differentiate your answer.
- Did you get $f(x)$ back?

**41.** Start with $g(x) = 6x^2 - 4x$.
- Differentiate: $g'(x) = $
- Integrate your answer.
- Did you get $g(x)$ back (plus C)?

**42.** Explain the asymmetry: 
- Differentiating then integrating gives $f(x) + C$
- Integrating then differentiating gives exactly $f(x)$

Why the difference?

---

**Connecting Position, Velocity, Acceleration:**

**43.** Complete the chain:

Position $s(t)$ $\xrightarrow{\text{derivative}}$ \_\_\_\_\_\_\_\_ $\xrightarrow{\text{derivative}}$ \_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_ $\xrightarrow{\text{integral}}$ Velocity $\xrightarrow{\text{integral}}$ \_\_\_\_\_\_\_\_

**44.** An object has acceleration $a(t) = 6t$, with $v(0) = 2$ and $s(0) = 1$.
- Find $v(t)$ by integrating $a(t)$ and using the initial condition.
- Find $s(t)$ by integrating $v(t)$ and using the initial condition.

---

## Part D: Area Between Curves (8 problems)

Area between $f(x)$ and $g(x)$ from $a$ to $b$:

$$\text{Area} = \int_a^b |f(x) - g(x)| \, dx$$

If $f(x) \geq g(x)$ on $[a,b]$: Area $= \int_a^b (f(x) - g(x)) \, dx$

---

**45.** Find area between $y = x^2$ and $y = x$ from $x = 0$ to $x = 1$.
- Which is on top?
- Set up and compute the integral.

**46.** Find area between $y = x^2$ and $y = 4$.
- Find intersection points.
- Set up and compute.

**47.** Find area enclosed by $y = x^2$ and $y = 2x$.
- Find intersections.
- Integrate from intersection to intersection.

**48.** Find area between $y = x^3$ and $y = x$ from $x = -1$ to $x = 1$.
- Careful: which is on top changes at $x = 0$!

---

**Applications:**

**49.** Consumer Surplus: Demand is $p = 50 - 2q$, equilibrium price is $p^* = 30$.
- Consumer surplus = $\int_0^{q^*} (50 - 2q - 30) dq$
- Find $q^*$ and calculate surplus.

**50.** The area between a velocity curve and the t-axis represents \_\_\_\_\_\_\_\_\_\_.

**51.** The area between two position curves represents the \_\_\_\_\_\_\_\_\_\_ between them.

**52.** Gini Coefficient: Perfect equality is $y = x$. A Lorenz curve is $y = x^2$.
- Gini = $\frac{\text{Area between curves}}{\text{Area under } y = x}$
- Calculate it.

---

## Part E: Connecting to ML and Optimization (8 problems)

**53.** Loss function: $L(w) = w^2 - 6w + 10$.
- Find $L'(w)$.
- Find the minimum.
- Verify with second derivative.

**54.** Gradient descent update: $w_{new} = w_{old} - \alpha \cdot L'(w_{old})$

For $L(w) = w^2 - 4w + 5$ with $\alpha = 0.1$, starting at $w_0 = 0$:
- Calculate $w_1$, $w_2$, $w_3$.
- What value is $w$ approaching?

**55.** Total loss over dataset $[0, 4]$ with loss function $\ell(x) = (x - 2)^2$:

Total = $\int_0^4 (x-2)^2 dx$. Calculate it.

**56.** Mean loss = $\frac{1}{4}\int_0^4 (x-2)^2 dx$. Calculate it.

**57.** Regularized loss: $L(w) = (w - 5)^2 + 0.5w^2$.
- Expand and simplify.
- Find optimal $w$.
- Compare to unregularized optimum $w = 5$.

**58.** Explain: Why is finding where $L'(w) = 0$ central to training ML models?

**59.** Explain: Why might we care about $\int L(w) dw$ over a region of weight space?

**60.** The Fundamental Theorem connects local information (derivative at a point) to global information (integral over an interval). How does this relate to:
- Local vs. global minima in optimization?
- Gradient (local) vs. total loss (global)?

---

## Answer Key

### Part A
1. (a) Inc: $x > 0$, Dec: $x < 0$ (b) $x = 0$ (c) 6
2. (a) $3x^2 - 3$ (b) $x = \pm 1$ (c) max at $-1$, min at $1$
3. CPs: $0, \pm 2$; max at $0$, min at $\pm 2$
4. $y = 4x - 4$
5. $y = 2x - 2$
6. $(\pm 2, \mp 16)$
7. (a) $20 - 10t$ (b) $t = 2$, max height (c) $-10$, constant gravity
8. (a) $v = 3t^2 - 12t + 9$, $a = 6t - 12$ (b) $t = 1, 3$ (c) $t = 2$
9. Up: $x > 0$, Down: $x < 0$, Inflection: $x = 0$
10. Inflection at $x = \pm 1$
11. $x = 40$, max profit $\$400$
12. $25 \times 25$ m
13. $t = 3$, height $55$ m
14. $p = 125$, revenue $\$31,250$
15. $C' = 3q^2 - 24q + 60$, min at $q = 4$
16. potential max/min; whether it's max or min

### Part B
17. 12
18. 8
19. $\frac{8}{3}$
20. 10
21. 0
22. 0
23. $\frac{32}{3}$
24. 0 (positive and negative areas cancel)
25. 8 m
26. (a) Forward: $t > 2$, Backward: $t < 2$ (b) 0 (c) 4 m
27. 800 L
28. 1125 people
29. (a) $\frac{x^3}{3}$ (b) $\frac{1}{3}, \frac{8}{3}, 9$ (c) $x^2$
30. $x^3 + 1$
31. $\sqrt{x}$

### Part C
33. $x^4$
34. $3x^2 - x$
35. $\frac{1}{x^2}$
36. 9
37. 18
38. 12
39. 1
40. $\frac{x^4}{4} + C$; $x^3$; yes
41. $12x - 4$; $6x^2 - 4x + C$; yes
43. Velocity, Acceleration; Acceleration, Position
44. $v(t) = 3t^2 + 2$; $s(t) = t^3 + 2t + 1$

### Part D
45. $\frac{1}{6}$
46. $\frac{32}{3}$
47. $\frac{4}{3}$
48. $\frac{1}{2}$
49. $q^* = 10$, surplus $= 100$
52. Gini $= \frac{1/6}{1/2} = \frac{1}{3}$

### Part E
53. Min at $w = 3$, $L(3) = 1$
54. $w_1 = 0.4$, $w_2 = 0.72$, $w_3 = 0.976$, approaching 2
55. $\frac{16}{3}$
56. $\frac{4}{3}$
57. $w = \frac{10}{3} \approx 3.33$

---

*End of Worksheet 4B*
