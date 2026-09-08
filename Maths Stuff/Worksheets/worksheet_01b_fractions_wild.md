# Worksheet 1B: Fractions in the Wild
**AIML Foundations Mathematics**  
**Dublin and Dún Laoghaire ETB**  
**Instructor: Josh Aaron**

---

> **A Note Before You Begin**
> 
> This worksheet contains formulas from physics, machine learning, probability, and information theory. Some of them look intimidating. They're not.
> 
> You don't need to understand what these formulas *do* in their original context. You just need to look at them as fractions and ask: "What happens when this variable gets bigger? Smaller? Approaches some limit?"
> 
> This is about building confidence. If you can analyze the behavior of Einstein's equations, you can handle anything.
> 
> **Keep calm. These are just fractions.**

---

## Part A: Physics — Special Relativity

In Einstein's special relativity, several important quantities involve the same fraction pattern.

### The Lorentz Factor

$$\gamma = \dfrac{1}{\sqrt{1 - \dfrac{v^2}{c^2}}}$$

Here:
- $v$ = speed of an object
- $c$ = speed of light (the maximum possible speed)
- The object cannot exceed $c$, so $v < c$ always

**1.** 
- (a) When $v = 0$ (object at rest), what is $\dfrac{v^2}{c^2}$? What is $\gamma$?
- (b) When $v = 0.5c$ (half light speed), what is $\dfrac{v^2}{c^2}$? What is $1 - \dfrac{v^2}{c^2}$?
- (c) As $v$ approaches $c$, what does $\dfrac{v^2}{c^2}$ approach?
- (d) As $v$ approaches $c$, what does $1 - \dfrac{v^2}{c^2}$ approach?
- (e) As $v$ approaches $c$, what happens to $\gamma$?

---

### Time Dilation

A moving clock runs slower. The relationship is:

$$\text{time\_moving} = \text{time\_stationary} \times \sqrt{1 - \dfrac{v^2}{c^2}}$$

**2.**
- (a) When $v = 0$, how does $\text{time\_moving}$ compare to $\text{time\_stationary}$?
- (b) As $v \to c$, what happens to $\text{time\_moving}$?
- (c) In words: as you move faster, does your clock run faster or slower compared to a stationary observer?

---

### Relativistic Energy

$$\text{energy} = \dfrac{\text{rest\_mass} \times c^2}{\sqrt{1 - \dfrac{v^2}{c^2}}}$$

**3.**
- (a) When $v = 0$, what is the energy? (This is the famous $E = mc^2$)
- (b) As $v \to c$, what happens to the energy?
- (c) Why does this suggest that nothing with mass can actually reach light speed?

---

### Relativistic Momentum

$$\text{momentum} = \dfrac{\text{mass} \times v}{\sqrt{1 - \dfrac{v^2}{c^2}}}$$

**4.**
- (a) When $v$ is very small compared to $c$, the denominator is approximately 1. What does momentum approximately equal?
- (b) As $v \to c$, what happens to momentum?

---

## Part B: Probability — Bayes' Theorem

Bayes' theorem tells us how to update our beliefs when we get new evidence:

$$P(\text{hypothesis} | \text{evidence}) = \dfrac{P(\text{evidence} | \text{hypothesis}) \times P(\text{hypothesis})}{P(\text{evidence})}$$

This reads as: "The probability of our hypothesis *given* the evidence equals..."

Let's use a concrete example: **Medical Testing**

- `P(disease)` = probability someone has a disease (let's say it's rare: 1%)
- `P(positive | disease)` = probability of testing positive if you have the disease (sensitivity: 99%)
- `P(positive | no_disease)` = probability of testing positive if healthy (false positive rate: 5%)

**5.** The formula becomes:

$$P(\text{disease} | \text{positive}) = \dfrac{P(\text{positive} | \text{disease}) \times P(\text{disease})}{P(\text{positive})}$$

- (a) If the disease is very rare (small `P(disease)`), what happens to the numerator?
- (b) If the test has many false positives (high `P(positive | no_disease)`), what happens to `P(positive)` in the denominator?
- (c) Combining (a) and (b): even with a positive test, why might the probability of actually having a rare disease still be low?

**6.** Now imagine a very common condition where `P(condition) = 0.5` (50% of people have it).
- (a) How does this change the numerator compared to a rare disease?
- (b) Is a positive test more or less meaningful for common vs rare conditions?

**7.** What happens to `P(hypothesis | evidence)` if:
- (a) `P(evidence)` is very small (the evidence is rare)?
- (b) `P(evidence)` is close to 1 (the evidence is extremely common)?

---

## Part C: Information Theory — Entropy and Compression

### Shannon Entropy

The "surprise" or information content of an event is:

$$\text{surprise}(\text{event}) = \log_2\left(\dfrac{1}{P(\text{event})}\right)$$

**8.** 
- (a) If an event is very likely (`P(event)` close to 1), what is $\dfrac{1}{P(\text{event})}$ close to?
- (b) So what happens to the surprise value?
- (c) If an event is very unlikely (`P(event)` close to 0), what happens to $\dfrac{1}{P(\text{event})}$?
- (d) So what happens to the surprise value?
- (e) In plain English: are rare events more or less surprising?

**9.** Average entropy (average surprise) across all possible events:

$$H = \sum_{\text{each event } i} P(\text{event}_i) \times \log_2\left(\dfrac{1}{P(\text{event}_i)}\right)$$

Consider a coin flip:
- Fair coin: `P(heads) = 0.5`, `P(tails) = 0.5`
- Biased coin: `P(heads) = 0.99`, `P(tails) = 0.01`

- (a) Which coin is more predictable?
- (b) Which coin has lower entropy (less average surprise)?
- (c) Which coin's outcomes could be compressed more efficiently? Why?

---

### Compression Ratio

$$\text{compression\_ratio} = \dfrac{\text{compressed\_size}}{\text{original\_size}}$$

**10.**
- (a) If compressed size is much smaller than original, is the ratio close to 0 or close to 1?
- (b) What compression ratio means "no compression at all"?
- (c) Can the compression ratio ever be greater than 1? What would that mean?

---

## Part D: Machine Learning Concepts

### The Sigmoid Function

The sigmoid "squashes" any input to a value between 0 and 1:

$$\text{sigmoid}(x) = \dfrac{1}{1 + e^{-x}}$$

Remember: $e \approx 2.718$, and $e^{-x} = \dfrac{1}{e^x}$

**11.**
- (a) When $x = 0$, what is $e^{-x}$? What is sigmoid(0)?
- (b) When $x$ is very large and positive, what happens to $e^{-x}$? What does sigmoid approach?
- (c) When $x$ is very large and negative, what happens to $e^{-x}$? What does sigmoid approach?
- (d) Can sigmoid ever actually equal 0 or 1 exactly?

**12.** The sigmoid is used to convert "confidence scores" to probabilities. Why is it useful that:
- (a) The output is always between 0 and 1?
- (b) An input of 0 gives output 0.5 (maximum uncertainty)?

---

### Softmax Function

Softmax converts a list of numbers into probabilities that sum to 1:

$$\text{softmax}(z_i) = \dfrac{e^{z_i}}{\sum_{\text{all } j} e^{z_j}}$$

For example, with three scores $[z_1, z_2, z_3] = [2, 1, 0]$:

$$\text{softmax}(z_1) = \dfrac{e^2}{e^2 + e^1 + e^0}$$

**13.**
- (a) What is the denominator ensuring about all the softmax outputs together?
- (b) If one score $z_i$ is much larger than the others, what happens to its softmax value?
- (c) If all scores are equal, what are all the softmax values?

---

### Learning Rate Decay

During training, we often shrink the learning rate over time:

$$\text{learning\_rate}(t) = \dfrac{\text{initial\_rate}}{1 + \text{decay} \times t}$$

Where $t$ = time step (0, 1, 2, 3, ...)

**14.**
- (a) At $t = 0$ (start of training), what is the learning rate?
- (b) As $t$ gets very large, what does the learning rate approach?
- (c) Why might we want the learning rate to start high and decrease over time?

---

### Gradient Descent Update

When training a model, we update weights using:

$$\text{new\_weight} = \text{old\_weight} - \text{learning\_rate} \times \dfrac{\text{change\_in\_loss}}{\text{change\_in\_weight}}$$

**15.** The fraction $\dfrac{\text{change\_in\_loss}}{\text{change\_in\_weight}}$ is called the gradient.
- (a) If the gradient is positive (increasing the weight increases the loss), should we increase or decrease the weight?
- (b) If the gradient is very large, should we take a big step or small step?
- (c) Why do we multiply by learning rate — what does a small learning rate do to our steps?

---

### Batch Normalization (Simplified)

$$\text{normalized} = \dfrac{\text{value} - \text{mean}}{\text{standard\_deviation}}$$

**16.**
- (a) If a value equals the mean, what is the normalized value?
- (b) If a value is one standard deviation above the mean, what is normalized?
- (c) What happens if standard deviation is very small (all values nearly identical)?

---

## Part E: Exponential Growth and Decay

### Compound Interest

$$\text{final\_amount} = \text{principal} \times \left(1 + \dfrac{\text{rate}}{n}\right)^{n \times \text{years}}$$

Where $n$ = number of times compounded per year

**17.** With rate = 100% (doubling) and 1 year:
- (a) If $n = 1$ (yearly): $\left(1 + \dfrac{1}{1}\right)^1 = ?$
- (b) If $n = 2$ (semi-annually): $\left(1 + \dfrac{1}{2}\right)^2 = ?$
- (c) If $n = 12$ (monthly): $\left(1 + \dfrac{1}{12}\right)^{12} = ?$ (use calculator)
- (d) If $n = 365$ (daily): $\left(1 + \dfrac{1}{365}\right)^{365} = ?$ (use calculator)
- (e) As $n \to \infty$, this approaches $e \approx 2.718$. What does "continuous compounding" mean?

---

### Radioactive Decay / Half-Life

$$\text{remaining} = \text{initial} \times \left(\dfrac{1}{2}\right)^{\dfrac{\text{time}}{\text{half\_life}}}$$

**18.**
- (a) After exactly one half-life, what fraction remains?
- (b) After two half-lives?
- (c) After ten half-lives?
- (d) Does the amount ever reach exactly zero?

---

### Model Accuracy Over Training

Imagine accuracy improves but with diminishing returns:

$$\text{accuracy}(t) = 1 - \dfrac{1}{1 + t}$$

Where $t$ = training epochs

**19.**
- (a) At $t = 0$, what is accuracy?
- (b) At $t = 1$?
- (c) At $t = 9$?
- (d) At $t = 99$?
- (e) What value does accuracy approach but never reach?

---

## Part F: Classification Metrics

### Precision

$$\text{precision} = \dfrac{\text{true\_positives}}{\text{true\_positives} + \text{false\_positives}}$$

"Of everything we predicted positive, how many were actually positive?"

**20.**
- (a) If we have 90 true positives and 10 false positives, what is precision?
- (b) If false positives increase while true positives stay the same, does precision go up or down?
- (c) What precision value means "every positive prediction was correct"?

---

### Recall

$$\text{recall} = \dfrac{\text{true\_positives}}{\text{true\_positives} + \text{false\_negatives}}$$

"Of everything that was actually positive, how many did we catch?"

**21.**
- (a) If we have 90 true positives and 10 false negatives, what is recall?
- (b) If we predict *everything* as positive (to miss nothing), what happens to false negatives? What is recall?
- (c) But what happens to precision if we predict everything as positive?

---

### F1 Score

The F1 score balances precision and recall:

$$F1 = \dfrac{2 \times \text{precision} \times \text{recall}}{\text{precision} + \text{recall}}$$

**22.**
- (a) If precision = 1 and recall = 1, what is F1?
- (b) If precision = 1 and recall = 0, what is F1?
- (c) If precision = 0.6 and recall = 0.6, what is F1?
- (d) This is called the "harmonic mean." Why might we prefer this over a simple average $\frac{\text{precision} + \text{recall}}{2}$?

---

### Accuracy vs Class Imbalance

$$\text{accuracy} = \dfrac{\text{correct\_predictions}}{\text{total\_predictions}}$$

**23.** Suppose 99% of emails are not spam, and only 1% are spam.
- (a) If a model predicts "not spam" for everything, what is its accuracy?
- (b) How many spam emails does it catch?
- (c) Why is accuracy misleading for imbalanced datasets?

---

## Part G: Geometric Series and Convergence

**24.** The infinite geometric series formula:

$$\sum_{n=0}^{\infty} r^n = \dfrac{1}{1-r} \quad \text{(when } |r| < 1 \text{)}$$

- (a) Verify: $1 + \frac{1}{2} + \frac{1}{4} + \frac{1}{8} + ... = \frac{1}{1 - 0.5} = ?$
- (b) What is $1 + \frac{1}{3} + \frac{1}{9} + \frac{1}{27} + ...$ ?
- (c) What is $1 + \frac{2}{3} + \frac{4}{9} + \frac{8}{27} + ...$ ? (Here $r = \frac{2}{3}$)
- (d) Why doesn't this formula work when $r \geq 1$?

**25.** Expected value in probability uses similar patterns. If you have a $\frac{1}{2}$ chance of winning on each try:

$$\text{expected\_tries} = \dfrac{1}{P(\text{success})} = \dfrac{1}{1/2} = 2$$

- (a) If success probability is $\frac{1}{6}$ (like rolling a specific number on a die), expected tries?
- (b) If success probability is $\frac{1}{100}$, expected tries?
- (c) As success probability approaches 0, expected tries approaches...?

---

## Part H: Challenge Problems

**26.** The logistic growth model (populations, adoption curves):

$$P(t) = \dfrac{K}{1 + \left(\dfrac{K - P_0}{P_0}\right)e^{-rt}}$$

Where $K$ = carrying capacity, $P_0$ = initial population, $r$ = growth rate, $t$ = time

Don't panic! Just analyze the fraction:
- (a) As $t \to \infty$, what happens to $e^{-rt}$?
- (b) As $t \to \infty$, what does the denominator approach?
- (c) As $t \to \infty$, what does $P(t)$ approach?
- (d) At $t = 0$, verify that $P(0) = P_0$.

**27.** The normal distribution's probability density:

$$f(x) = \dfrac{1}{\sigma\sqrt{2\pi}} \times e^{-\frac{(x-\mu)^2}{2\sigma^2}}$$

Focus just on the exponent: $-\dfrac{(x-\mu)^2}{2\sigma^2}$

- (a) When $x = \mu$ (at the mean), what is the exponent? What is $e^0$?
- (b) As $x$ moves far from $\mu$, does $(x-\mu)^2$ get larger or smaller?
- (c) So does the exponent become more negative or less negative?
- (d) What happens to the overall probability density far from the mean?

**28.** In neural networks, the "attention" mechanism uses:

$$\text{attention\_weight}_i = \dfrac{e^{\text{score}_i}}{\sum_j e^{\text{score}_j}}$$ 

This is just softmax! If one item has score 10 and two others have score 0:
- (a) What is the attention weight for the high-score item (approximately)?
- (b) What are the attention weights for the low-score items?
- (c) What does "attention" mean in plain English here?

---

## Answer Key

### Part A: Physics
1. (a) 0; γ = 1 (b) 0.25; 0.75 (c) 1 (d) 0 (e) γ → ∞
2. (a) Equal (b) Approaches 0 (c) Slower
3. (a) rest_mass × c² (b) → ∞ (c) Would need infinite energy
4. (a) mass × v (classical momentum) (b) → ∞

### Part B: Probability
5. (a) Small (b) Gets larger (c) Small numerator / large denominator = small result
6. (a) Much larger numerator (b) More meaningful for common conditions
7. (a) Ratio increases (b) Ratio decreases

### Part C: Information Theory
8. (a) Close to 1 (b) Low surprise (c) Very large (d) High surprise (e) More surprising
9. (a) Biased coin (b) Biased coin (c) Biased coin; fewer bits needed for predictable outcomes
10. (a) Close to 0 (b) 1 (c) Yes; means file got larger (bad compression)

### Part D: Machine Learning
11. (a) 1; 0.5 (b) → 0; approaches 1 (c) → ∞; approaches 0 (d) No
12. (a) Valid probability (b) Neutral input = uncertain output
13. (a) They sum to 1 (b) Approaches 1 (c) All equal (1/3 each if three items)
14. (a) initial_rate (b) 0 (c) Big steps early to explore, small steps later to fine-tune
15. (a) Decrease (b) Big step (c) Limits step size
16. (a) 0 (b) 1 (c) Division by near-zero; normalized values explode

### Part E: Exponential
17. (a) 2 (b) 2.25 (c) ≈ 2.613 (d) ≈ 2.714 (e) Compounding every instant
18. (a) 1/2 (b) 1/4 (c) 1/1024 ≈ 0.001 (d) No, asymptotic
19. (a) 0 (b) 0.5 (c) 0.9 (d) 0.99 (e) 1

### Part F: Classification
20. (a) 0.9 (b) Down (c) 1
21. (a) 0.9 (b) 0; recall = 1 (c) Plummets (many false positives)
22. (a) 1 (b) 0 (c) 0.6 (d) Harmonic mean punishes imbalance more
23. (a) 99% (b) Zero (c) High accuracy despite useless predictions

### Part G: Series
24. (a) 2 (b) 3/2 = 1.5 (c) 3 (d) Series diverges; doesn't converge
25. (a) 6 (b) 100 (c) ∞

### Part H: Challenge
26. (a) → 0 (b) → 1 (c) → K (carrying capacity) (d) Substitute and simplify
27. (a) 0; 1 (b) Larger (c) More negative (d) Approaches 0
28. (a) ≈ 0.9999 (b) ≈ 0.00005 each (c) Model "focuses" on highest-scored item

---

*End of Worksheet 1B*
