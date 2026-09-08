# Worksheet 3C: Quadratics — Real-World Applications
**AIML Foundations Mathematics**  
**Dublin and Dún Laoghaire ETB**  
**Instructor: Josh Aaron**

---

> **What This Worksheet Is About**
>
> Quadratics aren't just abstract algebra — they show up everywhere:
> - Objects flying through the air follow parabolic paths
> - Trigonometric functions can be approximated by polynomials
> - Probability distributions use binomial expansions
> - Compound growth involves expanding expressions like $(1 + r)^n$
>
> This worksheet connects the algebra you've learned to real applications.

---

## Part A: Projectile Motion (12 problems)

When you throw a ball, drop an object, or launch a rocket, its height follows a quadratic equation:

$$h(t) = h_0 + v_0 t - \frac{1}{2}gt^2$$

Where:
- $h(t)$ = height at time $t$
- $h_0$ = initial height (starting height)
- $v_0$ = initial velocity (positive = upward, negative = downward)
- $g$ = acceleration due to gravity ($\approx 10 \text{ m/s}^2$ or $32 \text{ ft/s}^2$)
- $t$ = time

**Simplified form (using $g = 10$ m/s²):**

$$h(t) = h_0 + v_0 t - 5t^2$$

---

**1.** A ball is thrown upward from ground level with initial velocity 20 m/s.

$$h(t) = 0 + 20t - 5t^2 = 20t - 5t^2$$

- (a) What is the height at $t = 1$ second?
- (b) What is the height at $t = 2$ seconds?
- (c) What is the height at $t = 4$ seconds? What does this answer tell you?

**2.** Using the same equation $h(t) = 20t - 5t^2$:

- (a) Factor the right side: $h(t) = $ \_\_\_\_\_\_\_\_\_\_
- (b) Set $h(t) = 0$ and solve. What do the two solutions represent physically?

**3.** A ball is dropped from a 45-meter building (no initial velocity).

$$h(t) = 45 - 5t^2$$

- (a) How high is the ball after 1 second?
- (b) How high after 2 seconds?
- (c) When does the ball hit the ground? (Set $h(t) = 0$ and solve)

**4.** A ball is thrown downward from a 80-meter cliff with initial velocity 10 m/s downward.

$$h(t) = 80 - 10t - 5t^2$$

- (a) Why is the $v_0$ term negative?
- (b) When does the ball hit the ground?
- (c) How fast is it falling? (This requires calculus, but estimate: is it speeding up or slowing down?)

**5.** A rocket is launched upward with initial velocity 50 m/s from a platform 20 meters high.

$$h(t) = 20 + 50t - 5t^2$$

- (a) Rewrite in standard form: $h(t) = -5t^2 + 50t + 20$
- (b) What is $h(0)$? Does this match the problem description?
- (c) Use the quadratic formula to find when $h(t) = 0$.
- (d) Why do you get two answers? Which one makes physical sense?

**6.** **Finding Maximum Height**

For $h(t) = -5t^2 + 20t$, the maximum occurs at $t = \frac{-b}{2a}$.

- (a) Identify $a$ and $b$ from the equation.
- (b) Calculate $t_{max} = \frac{-b}{2a}$
- (c) Find the maximum height by plugging $t_{max}$ back into $h(t)$.

**7.** For the rocket in problem 5, $h(t) = -5t^2 + 50t + 20$:

- (a) At what time does it reach maximum height?
- (b) What is the maximum height?

**8.** A football is kicked with the path $h(t) = -5t^2 + 15t + 1$ (height in meters).

- (a) What was the initial height? (The kicker's foot height)
- (b) When does it reach maximum height?
- (c) What is the maximum height?
- (d) When does it hit the ground?

---

**9.** **Horizontal Distance**

When launched at an angle, a projectile's horizontal distance is:

$$x(t) = v_x \cdot t$$

And vertical height is:

$$y(t) = v_y \cdot t - 5t^2$$

A ball is kicked with $v_x = 10$ m/s (horizontal) and $v_y = 15$ m/s (vertical).

- (a) Write the equation for $y(t)$.
- (b) When does the ball land ($y = 0$)?
- (c) How far horizontally has it traveled when it lands?

**10.** Eliminate $t$ from the equations in problem 9:

- From $x = 10t$, we get $t = \frac{x}{10}$
- Substitute into $y(t)$: $y = 15 \cdot \frac{x}{10} - 5 \cdot \left(\frac{x}{10}\right)^2$
- Simplify to show that $y$ is a quadratic function of $x$ (a parabola!)

**11.** A ball thrown from height 2m follows $h(t) = 2 + 12t - 5t^2$.

Write an equation to answer: "When is the ball at height 10m?" Then solve it.

**12.** Two balls are thrown:
- Ball A: $h_A(t) = 30t - 5t^2$ (from ground, fast)
- Ball B: $h_B(t) = 25 + 10t - 5t^2$ (from 25m platform, slower)

When are they at the same height? (Set $h_A = h_B$ and solve)

---

## Part B: Area Problems (8 problems)

**13.** A rectangular garden has length 3 meters more than its width. Let $w$ = width.

- (a) Write an expression for the length in terms of $w$.
- (b) Write an expression for the area $A$ in terms of $w$.
- (c) If the area is 70 m², write and solve an equation to find the dimensions.

**14.** A farmer has 100 meters of fencing to enclose a rectangular field against a river (no fence needed on the river side).

- (a) If the width is $w$, what is the length in terms of $w$? (Hint: $2w + L = 100$)
- (b) Write the area as a function of $w$.
- (c) This is a quadratic! Find the width that maximizes the area.
- (d) What is the maximum area?

**15.** A square has its side length increased by 4 cm. The new area is 81 cm².

- (a) Let $s$ = original side length. Write an equation.
- (b) Solve for $s$.

**16.** The product of two consecutive positive integers is 182. Find them.

*(Let $n$ = first integer, so $n + 1$ = second integer)*

**17.** The product of two consecutive even integers is 288. Find them.

**18.** A rectangular photo is 4 cm longer than it is wide. A frame of uniform width 2 cm surrounds it. The total area (photo + frame) is 165 cm².

- (a) If the photo width is $w$, what are the outer dimensions?
- (b) Write an equation for the total area.
- (c) Solve for the photo dimensions.

**19.** A box with no lid is made from a 20 cm × 30 cm sheet by cutting squares of side $x$ from each corner and folding up.

- (a) What are the dimensions of the box in terms of $x$?
- (b) Write the volume as a function of $x$.
- (c) If the volume must be 1008 cm³, find $x$.

**20.** The sum of a number and its square is 72. Find all possible values.

---

## Part C: Polynomial Approximations of Trig Functions (10 problems)

> **Key Insight:** Sine, cosine, and other transcendental functions can be approximated by polynomials! These are called **Taylor series** approximations.
>
> For small values of $\theta$ (in radians):

$$\sin(\theta) \approx \theta - \frac{\theta^3}{6} + \frac{\theta^5}{120} - \cdots$$

$$\cos(\theta) \approx 1 - \frac{\theta^2}{2} + \frac{\theta^4}{24} - \cdots$$

**These are just polynomials!** All your algebra skills apply.

---

**21.** Using the first two terms of the sine approximation: $\sin(\theta) \approx \theta - \frac{\theta^3}{6}$

- (a) Calculate this approximation for $\theta = 0.1$ radians.
- (b) Your calculator says $\sin(0.1) = 0.0998334...$. How close is your approximation?

**22.** Using the first two terms of the cosine approximation: $\cos(\theta) \approx 1 - \frac{\theta^2}{2}$

- (a) Calculate this approximation for $\theta = 0.2$ radians.
- (b) Compare to the actual value $\cos(0.2) = 0.980067...$

**23.** Factor $\theta$ out of the sine approximation $\theta - \frac{\theta^3}{6}$:

$$\sin(\theta) \approx \theta\left(1 - \frac{\theta^2}{6}\right)$$

What does this tell you about $\sin(\theta)$ when $\theta$ is very small?

**24.** The cosine approximation $1 - \frac{\theta^2}{2}$ is a quadratic in $\theta$.

- (a) What is the "vertex" of this parabola?
- (b) Does this match what you know about the cosine function at $\theta = 0$?

**25.** For small angles, engineers often use $\sin(\theta) \approx \theta$ and $\cos(\theta) \approx 1$.

- (a) For what range of $\theta$ is this reasonable? (When does $\frac{\theta^2}{2}$ become significant?)
- (b) If you need $\cos(\theta)$ to be accurate within 1%, how small must $\theta$ be?

**26.** The tangent function can be approximated as:

$$\tan(\theta) \approx \theta + \frac{\theta^3}{3}$$

- (a) Factor out $\theta$.
- (b) Calculate $\tan(0.1)$ using this approximation.
- (c) Compare to actual: $\tan(0.1) = 0.1003347...$

**27.** **Combining Approximations**

Using $\sin(\theta) \approx \theta - \frac{\theta^3}{6}$ and $\cos(\theta) \approx 1 - \frac{\theta^2}{2}$:

Calculate $\sin^2(\theta) + \cos^2(\theta)$ for $\theta = 0.1$ using the approximations.

Does it equal 1? (It should be close!)

**28.** The approximation $e^x \approx 1 + x + \frac{x^2}{2}$ is also a polynomial.

- (a) Calculate $e^{0.1}$ using this approximation.
- (b) Actual value: $e^{0.1} = 1.10517...$. How close?

**29.** Using $e^x \approx 1 + x + \frac{x^2}{2} + \frac{x^3}{6}$:

- (a) This is a polynomial of degree \_\_\_.
- (b) Calculate $e^{0.5}$ using all four terms.
- (c) Actual value: $e^{0.5} = 1.6487...$. How's the accuracy?

**30.** **Connection to Euler's Formula**

The famous formula $e^{i\theta} = \cos(\theta) + i\sin(\theta)$ connects exponentials and trig.

Using the polynomial approximations, verify this is consistent for small $\theta$ by comparing:
- $e^{i\theta} \approx 1 + i\theta + \frac{(i\theta)^2}{2} = 1 + i\theta - \frac{\theta^2}{2}$ (since $i^2 = -1$)
- $\cos(\theta) + i\sin(\theta) \approx \left(1 - \frac{\theta^2}{2}\right) + i(\theta)$

Are they the same?

---

## Part D: Binomial Expansion and Probability (10 problems)

> **Connection:** When you flip a coin $n$ times, the probability of getting exactly $k$ heads involves the binomial coefficient from Pascal's Triangle!

$$P(k \text{ heads in } n \text{ flips}) = \binom{n}{k} p^k (1-p)^{n-k}$$

Where $\binom{n}{k}$ is the entry in row $n$, position $k$ of Pascal's Triangle.

---

**31.** Expand $(H + T)^3$ where $H$ and $T$ represent heads and tails.

This represents all possible outcomes of 3 coin flips!

**32.** From your expansion, identify:
- (a) How many ways to get 0 heads (all tails)?
- (b) How many ways to get exactly 1 head?
- (c) How many ways to get exactly 2 heads?
- (d) How many ways to get 3 heads?
- (e) Total number of outcomes?

**33.** For a fair coin ($p = 0.5$), expand $(0.5 + 0.5)^3$ to find the probability of each outcome.

**34.** A biased coin has $P(\text{heads}) = 0.6$ and $P(\text{tails}) = 0.4$.

Expand $(0.6 + 0.4)^3$ to find:
- (a) $P(\text{0 heads})$
- (b) $P(\text{1 head})$
- (c) $P(\text{2 heads})$
- (d) $P(\text{3 heads})$

**35.** Using Pascal's Triangle row 4: **1, 4, 6, 4, 1**

For 4 flips of a fair coin, calculate:
- (a) $P(\text{exactly 2 heads})$
- (b) $P(\text{at least 3 heads})$

**36.** Expand $(p + q)^4$ where $p + q = 1$.

This is the general probability distribution for 4 trials!

**37.** A multiple choice test has 5 questions, each with 4 options (so $P(\text{correct by guessing}) = 0.25$).

Using the binomial expansion, what's the probability of getting exactly 3 correct by pure guessing?

*(Use row 5 of Pascal's Triangle: 1, 5, 10, 10, 5, 1)*

**38.** In the same test, what's the probability of getting at least 4 correct by guessing?

**39.** **Expected Value Connection**

For $n$ flips of a fair coin, the expected number of heads is $\frac{n}{2}$.

Verify this makes sense: In $(H + T)^4$ expanded, which term has the largest coefficient? What does this represent?

**40.** A basketball player makes 70% of free throws. Using $(0.7 + 0.3)^3$:
- (a) What's the probability of making all 3 shots?
- (b) What's the probability of making at least 2?

---

## Part E: Compound Growth and Finance (10 problems)

> **The Compound Interest Formula:**
>
> $$A = P\left(1 + \frac{r}{n}\right)^{nt}$$
>
> Where:
> - $A$ = final amount
> - $P$ = principal (initial amount)
> - $r$ = annual interest rate (as decimal)
> - $n$ = number of times compounded per year
> - $t$ = time in years

---

**41.** You invest €1000 at 5% annual interest, compounded yearly, for 2 years.

$$A = 1000(1 + 0.05)^2 = 1000(1.05)^2$$

- (a) Expand $(1.05)^2$ using $(1 + 0.05)^2 = 1 + 2(0.05) + (0.05)^2$
- (b) Calculate the final amount.
- (c) How much was earned in interest?

**42.** Same investment, but for 3 years: $A = 1000(1.05)^3$

- (a) Expand $(1.05)^3$ using Pascal's Triangle coefficients: 1, 3, 3, 1
- (b) Calculate the final amount.

**43.** **The Rule of 72**

To estimate how long it takes money to double at interest rate $r\%$:

$$\text{Doubling time} \approx \frac{72}{r}$$

- (a) At 6% interest, approximately how many years to double?
- (b) Verify: Calculate $(1.06)^{12}$ (you can use the approximation or calculator).

**44.** Expand $(1 + r)^2$ symbolically.

If $r = 0.1$ (10% return), calculate the growth factor after 2 years.

**45.** For small $r$, the approximation $(1 + r)^n \approx 1 + nr$ is sometimes used.

- (a) Using this approximation, what is $(1.02)^5$?
- (b) Using exact expansion (or calculator), what is $(1.02)^5$?
- (c) When is the approximation good enough?

**46.** **Inflation and Purchasing Power**

If inflation is 3% per year, the purchasing power of €100 after $n$ years is:

$$\text{Value} = 100 \cdot (1 - 0.03)^n = 100 \cdot (0.97)^n$$

- (a) What is the purchasing power after 2 years?
- (b) After 5 years?
- (c) Approximately how many years until the value is halved?

**47.** **Population Growth**

A town's population grows 2% per year from an initial 50,000.

$$P(t) = 50000(1.02)^t$$

- (a) What's the population after 3 years?
- (b) Using logarithms or trial, when does it reach 60,000?

**48.** **Depreciation**

A car worth €20,000 depreciates 15% per year.

$$V(t) = 20000(1 - 0.15)^t = 20000(0.85)^t$$

- (a) Value after 1 year?
- (b) Value after 3 years?
- (c) When is it worth less than €10,000?

**49.** **Continuous Compounding Limit**

As $n \to \infty$, $\left(1 + \frac{1}{n}\right)^n \to e \approx 2.718$

Calculate for:
- (a) $n = 1$
- (b) $n = 2$
- (c) $n = 10$
- (d) $n = 100$

Watch it approach $e$!

**50.** **Loan Payments**

A simplified loan payment formula involves:

$$\text{Payment} = P \cdot \frac{r(1+r)^n}{(1+r)^n - 1}$$

For a €10,000 loan at 0.5% monthly interest ($r = 0.005$) for 24 months:

- (a) Calculate $(1.005)^{24}$ (use calculator or approximation)
- (b) Find the monthly payment.
- (c) What's the total paid over 24 months?
- (d) How much was interest?

---

## Answer Key

### Part A: Projectile Motion
1. (a) 15 m (b) 20 m (c) 0 m — back on ground
2. (a) $5t(4 - t)$ (b) $t = 0$ (start) and $t = 4$ (lands)
3. (a) 40 m (b) 25 m (c) $t = 3$ seconds
4. (a) Thrown downward (b) $t = 4$ seconds (c) Speeding up
5. (c) $t \approx 10.4$ s (d) Negative solution is before launch
6. (a) $a = -5$, $b = 20$ (b) $t = 2$ s (c) 20 m
7. (a) $t = 5$ s (b) 145 m
8. (a) 1 m (b) $t = 1.5$ s (c) 12.25 m (d) $t \approx 3.06$ s
9. (a) $y = 15t - 5t^2$ (b) $t = 3$ s (c) 30 m
10. $y = 1.5x - 0.05x^2$
11. $10 = 2 + 12t - 5t^2$; $t = 0.8$ s or $t = 2$ s
12. $t = 1.25$ s

### Part B: Area Problems
13. (c) Width 7 m, Length 10 m
14. (c) $w = 25$ m (d) 1250 m²
15. (b) $s = 5$ cm
16. 13 and 14
17. 16 and 18
18. (c) Width 7 cm, Length 11 cm
19. (c) $x = 3$ cm
20. 8 or -9

### Part C: Trig Approximations
21. (a) 0.09983... (b) Very close!
22. (a) 0.98 (b) Close!
23. $\sin(\theta) \approx \theta$ for small $\theta$
24. (a) Vertex at $(0, 1)$ (b) Yes, $\cos(0) = 1$
25. (a) $\theta < 0.1$ rad (b) $\theta < 0.14$ rad
26. (b) 0.1003...
27. ≈ 0.9999 (very close to 1)
28. (a) 1.105 (b) Very close
29. (a) 3 (b) 1.6458... (c) Good!
30. Yes, they match

### Part D: Probability
31. $H^3 + 3H^2T + 3HT^2 + T^3$
32. (a) 1 (b) 3 (c) 3 (d) 1 (e) 8
33. Each: 0.125, 0.375, 0.375, 0.125
34. (a) 0.064 (b) 0.288 (c) 0.432 (d) 0.216
35. (a) 6/16 = 0.375 (b) 5/16 = 0.3125
36. $p^4 + 4p^3q + 6p^2q^2 + 4pq^3 + q^4$
37. $10 \cdot (0.25)^3 \cdot (0.75)^2 \approx 0.088$
38. $\approx 0.016$
39. The $6H^2T^2$ term (2 heads) — most likely outcome
40. (a) 0.343 (b) 0.784

### Part E: Compound Growth
41. (a) 1.1025 (b) €1102.50 (c) €102.50
42. (b) €1157.63
43. (a) 12 years (b) $(1.06)^{12} \approx 2.01$
44. $1 + 2r + r^2 = 1.21$
45. (a) 1.10 (b) 1.104 (c) When $r$ is small and $n$ is small
46. (a) €94.09 (b) €85.87 (c) ~23 years
47. (a) 53,060 (b) ~9.5 years
48. (a) €17,000 (b) €12,282.50 (c) ~4.3 years
49. (a) 2 (b) 2.25 (c) 2.594 (d) 2.705
50. (a) 1.127 (b) €468.71 (c) €11,249 (d) €1,249

---

*End of Worksheet 3C*
