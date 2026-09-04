# Worksheet 6A: Statistics and Probability
**AIML Foundations Mathematics**  
**Dublin and Dún Laoghaire ETB**  
**Instructor: Josh Aaron**

---

> **What This Worksheet Is About**
>
> Statistics and probability are the mathematical foundation of machine learning. Every time an AI makes a prediction, classifies an image, or recommends a video, it's using these concepts.
>
> This worksheet connects the basics you've learned to real applications — from training neural networks to analyzing scientific data.

---

## Part A: Measures of Central Tendency — Mean, Median, Mode (18 problems)

### The Formulas

**Mean (Average):** $\bar{x} = \frac{\sum x_i}{n} = \frac{x_1 + x_2 + \cdots + x_n}{n}$

**Median:** The middle value when data is sorted (or average of two middle values if $n$ is even)

**Mode:** The most frequent value

---

**Calculate the mean, median, and mode:**

**1.** Test scores: 78, 82, 85, 85, 88, 90, 92

**2.** Response times (ms): 120, 135, 140, 145, 145, 150, 180

**3.** Daily website visitors: 1200, 1350, 1400, 1450, 1500, 1550, 8500

- (a) Calculate all three measures.
- (b) Which measure is most affected by the outlier (8500)?
- (c) Which measure best represents a "typical" day?

---

**🤖 AI Connection: Training Data Quality**

**4.** A dataset of house prices (in €1000s) contains: 250, 275, 290, 310, 325, 340, 2500

The last value is a mansion that got mixed in with regular houses.

- (a) Calculate the mean with and without the outlier.
- (b) Calculate the median with and without the outlier.
- (c) Why might a data scientist remove outliers before training a model?

**5.** An image classification dataset has these label counts:

| Category | Count |
|----------|-------|
| Cat | 5000 |
| Dog | 4800 |
| Bird | 1200 |
| Fish | 500 |

- (a) What is the mean number of images per category?
- (b) What is the median?
- (c) What is the mode?
- (d) This is called an "imbalanced dataset." Why might this be a problem for training?

---

**🔬 Science Connection: Experimental Measurements**

**6.** A physicist measures the speed of light in 5 trials (in units of $10^8$ m/s):

2.998, 2.995, 3.001, 2.997, 2.999

- (a) Calculate the mean.
- (b) The accepted value is 2.998. How close is the experimental mean?

**7.** A chemist measures the pH of a solution 7 times:

7.02, 6.98, 7.01, 6.99, 7.00, 7.01, 7.00

- (a) Find mean, median, and mode.
- (b) Are they all similar? What does this suggest about the measurement consistency?

---

**🎮 Game Analytics**

**8.** Player scores in a mobile game level: 1250, 1480, 1520, 1550, 1600, 1650, 1700, 1800, 1850, 2400

- (a) Find the mean and median.
- (b) If the game designer wants to set the "3-star threshold" at a score that about half of players achieve, should they use the mean or median?

**9.** Daily active users for an app over two weeks:

Week 1: 10000, 12000, 15000, 14000, 13000, 8000, 7000
Week 2: 11000, 13000, 16000, 15000, 14000, 9000, 8000

- (a) Calculate the mean for each week.
- (b) Is the app growing? By what percentage?

---

**Weighted Mean:**

**10.** A student's grade is calculated as:
- Homework: 25% weight, score 85
- Midterm: 30% weight, score 78  
- Final: 45% weight, score 88

Calculate the weighted mean (final grade):
$$\bar{x}_w = \frac{\sum w_i x_i}{\sum w_i}$$

**11.** In a neural network, outputs from three layers are combined with weights:
- Layer 1: output 0.7, weight 0.5
- Layer 2: output 0.3, weight 0.3
- Layer 3: output 0.8, weight 0.2

Calculate the weighted average output.

---

## Part B: Measures of Spread — Range, Variance, Standard Deviation (16 problems)

### The Formulas

**Range:** $R = x_{max} - x_{min}$

**Variance:** $\sigma^2 = \frac{\sum (x_i - \bar{x})^2}{n}$

**Standard Deviation:** $\sigma = \sqrt{\sigma^2}$

*Note: For samples, divide by $(n-1)$ instead of $n$ — this is called Bessel's correction.*

---

**Calculate the range, variance, and standard deviation:**

**12.** Data: 4, 6, 8, 10, 12

- (a) Find the mean.
- (b) Find $(x_i - \bar{x})$ for each value.
- (c) Find $(x_i - \bar{x})^2$ for each value.
- (d) Find the variance (divide by $n = 5$).
- (e) Find the standard deviation.

**13.** Data: 7, 7, 8, 8, 8, 9, 9

**14.** Data: 2, 5, 8, 11, 14

---

**🤖 AI Connection: Model Consistency**

**15.** Two machine learning models are tested 5 times each on accuracy (%):

Model A: 85, 87, 84, 86, 88
Model B: 70, 95, 75, 90, 80

- (a) Calculate the mean accuracy for each.
- (b) Calculate the standard deviation for each.
- (c) Which model is more consistent?
- (d) In production, would you prefer a consistent model or one with higher peaks?

**16.** A chatbot's response times (seconds) over 6 queries:

Version 1.0: 1.2, 1.3, 1.1, 1.4, 1.2, 1.3
Version 2.0: 0.8, 2.1, 0.7, 1.8, 0.9, 1.7

- (a) Which version has lower mean response time?
- (b) Which version is more consistent (lower standard deviation)?
- (c) Users hate unpredictable wait times. Which version would you deploy?

---

**🔬 Science Connection: Measurement Precision**

**17.** Two instruments measure the same voltage (in volts):

Instrument A: 5.02, 4.98, 5.01, 4.99, 5.00
Instrument B: 5.10, 4.90, 5.15, 4.85, 5.00

- (a) Both have the same mean. Verify this.
- (b) Calculate the standard deviation for each.
- (c) Which instrument is more precise?

**18.** In manufacturing, parts must be within tolerance. A machine produces bolts with target diameter 10.00 mm. A sample of 5 bolts measures:

10.02, 9.98, 10.01, 9.99, 10.00

- (a) Find the mean and standard deviation.
- (b) If tolerance is ±0.05 mm (so 9.95 to 10.05 is acceptable), are all bolts within tolerance?
- (c) If the standard deviation were 0.03 mm instead, what percentage of bolts would you expect to be outside tolerance? (Assume normal distribution where ~68% are within 1 SD of mean)

---

**🎯 Understanding Standard Deviation:**

**19.** For a normal distribution:
- ~68% of data falls within 1 standard deviation of the mean
- ~95% falls within 2 standard deviations
- ~99.7% falls within 3 standard deviations

IQ scores have mean 100 and standard deviation 15.

- (a) What range contains about 68% of people?
- (b) What range contains about 95% of people?
- (c) What percentage of people have IQ above 130?

**20.** Human height (adult males) has mean ≈ 175 cm and SD ≈ 7 cm.

- (a) What range contains the middle 68%?
- (b) How tall would someone need to be to be in the top 2.5%?
- (c) A basketball team requires players at least 190 cm tall. Approximately what percentage of men qualify?

---

## Part C: Basic Probability (20 problems)

### The Fundamentals

$$P(\text{event}) = \frac{\text{Number of favorable outcomes}}{\text{Total possible outcomes}}$$

**Key Rules:**
- $0 \leq P(A) \leq 1$
- $P(\text{certain event}) = 1$
- $P(\text{impossible event}) = 0$
- $P(\text{not } A) = 1 - P(A)$

---

**21.** A standard deck has 52 cards (4 suits × 13 values). Find:
- (a) $P(\text{drawing a heart})$
- (b) $P(\text{drawing an ace})$
- (c) $P(\text{drawing the ace of hearts})$
- (d) $P(\text{not drawing a face card})$ (face cards = J, Q, K)

**22.** A bag contains 5 red, 3 blue, and 2 green marbles. Find:
- (a) $P(\text{red})$
- (b) $P(\text{not red})$
- (c) $P(\text{red or blue})$

---

**🤖 AI Connection: Classification Probabilities**

**23.** A spam filter classifies 1000 emails:
- 800 are correctly identified (700 real emails marked "not spam", 100 spam marked "spam")
- 200 are incorrectly identified (150 real emails marked "spam", 50 spam marked "not spam")

- (a) What is $P(\text{correct classification})$?
- (b) What is $P(\text{false positive})$ — real email marked as spam?
- (c) What is $P(\text{false negative})$ — spam marked as real?
- (d) Which error is worse for the user?

**24.** An image classifier sees 500 images:
- 200 cats (correctly identifies 180)
- 200 dogs (correctly identifies 170)
- 100 birds (correctly identifies 80)

- (a) What is $P(\text{correct | cat})$ — probability of correct given it's a cat?
- (b) What is $P(\text{correct | dog})$?
- (c) What is $P(\text{correct | bird})$?
- (d) What is the overall accuracy?

---

**🔬 Science Connection: Medical Testing**

**25.** A disease affects 1% of the population. A test for the disease:
- Correctly identifies 95% of sick people (sensitivity)
- Correctly identifies 90% of healthy people (specificity)

In a population of 10,000 people:
- (a) How many are actually sick? Healthy?
- (b) Of the sick, how many test positive?
- (c) Of the healthy, how many test positive (false positives)?
- (d) If someone tests positive, what's the probability they're actually sick?

*This is the famous "base rate fallacy" — the answer may surprise you!*

---

**🎮 Game Probability**

**26.** A loot box in a game contains:
- Common item: 70% chance
- Rare item: 20% chance
- Epic item: 8% chance
- Legendary item: 2% chance

- (a) What is $P(\text{rare or better})$?
- (b) If you open 3 boxes, what's the probability of getting no legendary items?
- (c) A player opens 50 boxes and gets no legendary items. How "unlucky" is this? Calculate $P(\text{no legendary in 50 boxes}) = 0.98^{50}$

**27.** In a card game, you need to draw 2 specific cards from a 20-card deck:
- (a) What is $P(\text{first card is correct})$?
- (b) Given the first card was correct, what is $P(\text{second card is correct})$?
- (c) What is $P(\text{both cards correct})$?

---

### Addition Rule (OR)

$$P(A \text{ or } B) = P(A) + P(B) - P(A \text{ and } B)$$

For mutually exclusive events: $P(A \text{ or } B) = P(A) + P(B)$

**28.** Rolling a die:
- (a) $P(\text{even or greater than 4})$
- (b) Are "even" and "greater than 4" mutually exclusive?

**29.** Drawing from a deck:
- (a) $P(\text{heart or face card})$
- (b) Why do we subtract $P(\text{heart and face card})$?

---

### Multiplication Rule (AND)

**Independent events:** $P(A \text{ and } B) = P(A) \times P(B)$

**Dependent events:** $P(A \text{ and } B) = P(A) \times P(B|A)$

**30.** Flipping a coin and rolling a die:
- (a) $P(\text{heads and 6})$
- (b) $P(\text{heads and even})$

**31.** Drawing two cards without replacement:
- (a) $P(\text{both aces})$
- (b) $P(\text{both hearts})$

---

**🤖 AI Connection: Independent Events in ML**

**32.** A neural network has 3 layers, each with 95% chance of working correctly (independently).

- (a) What is $P(\text{all layers work})$?
- (b) What is $P(\text{at least one layer fails})$?
- (c) If the network has 10 layers, each 99% reliable, what is $P(\text{all work})$?

**33.** A self-driving car uses 4 independent sensors:
- Camera: 99% reliable
- LIDAR: 98% reliable
- Radar: 97% reliable
- Ultrasonic: 95% reliable

- (a) What is $P(\text{all sensors work})$?
- (b) The car needs at least one sensor working. What is $P(\text{at least one works})$?

---

## Part D: Counting Principles (16 problems)

### Fundamental Counting Principle

If task 1 can be done in $m$ ways and task 2 can be done in $n$ ways, then both tasks can be done in $m \times n$ ways.

---

**34.** A password has 4 characters:
- First character: letter (26 options)
- Second: digit (10 options)
- Third: letter (26 options)
- Fourth: digit (10 options)

How many possible passwords are there?

**35.** A restaurant offers:
- 4 appetizers
- 6 main courses
- 3 desserts

How many different 3-course meals are possible?

---

### Permutations (Order Matters)

$$P(n, r) = \frac{n!}{(n-r)!}$$

Number of ways to arrange $r$ items from $n$ items.

**36.** How many ways can 5 people line up for a photo?

**37.** How many 3-letter "words" (any letters, no repeats) can be made from A, B, C, D, E?

**38.** In a race with 8 runners, how many ways can gold, silver, and bronze be awarded?

---

### Combinations (Order Doesn't Matter)

$$C(n, r) = \binom{n}{r} = \frac{n!}{r!(n-r)!}$$

Number of ways to choose $r$ items from $n$ items.

**39.** How many ways can you choose 3 students from a class of 10 to form a committee?

**40.** How many 5-card poker hands are possible from a 52-card deck?

**41.** A lottery requires choosing 6 numbers from 1-49. How many possible tickets?

---

**🤖 AI Connection: Feature Selection**

**42.** A data scientist has 10 features (variables) and wants to train models using different subsets:

- (a) How many ways to choose exactly 3 features?
- (b) How many ways to choose exactly 5 features?
- (c) How many total subsets of features are there (including empty set)? Hint: Each feature is either in or out = $2^{10}$

**43.** A neural network architect is designing a network with:
- Choice of 3 activation functions
- Choice of 4 optimization algorithms
- Number of hidden layers: 1, 2, 3, or 4
- Learning rate: 5 options

How many different configurations are possible?

---

**🔬 Science Connection: Genetics**

**44.** DNA has 4 bases: A, T, G, C. A codon is a sequence of 3 bases.

- (a) How many different codons are possible?
- (b) There are 20 amino acids. Why does this work out nicely?

**45.** In a genetics experiment, a researcher needs to test all pairwise combinations of 8 genes.
- (a) How many pairs must be tested?
- (b) If each test takes 2 hours, how long will the full experiment take?

---

### Pascal's Triangle Connection

**46.** Row 5 of Pascal's Triangle is: 1, 5, 10, 10, 5, 1

These are $\binom{5}{0}, \binom{5}{1}, \binom{5}{2}, \binom{5}{3}, \binom{5}{4}, \binom{5}{5}$

Verify: $\binom{5}{2} = 10$ using the formula.

**47.** The sum of row $n$ of Pascal's Triangle is $2^n$.

- (a) Verify for row 5: $1 + 5 + 10 + 10 + 5 + 1 = ?$
- (b) This represents all possible subsets of a 5-element set. Why?

---

## Part E: Putting It Together — ML Applications (10 problems)

**🤖 Accuracy, Precision, Recall**

**48.** A model classifying tumors as "malignant" or "benign" produces:

|  | Predicted Malignant | Predicted Benign |
|--|---------------------|------------------|
| Actually Malignant | 85 (True Positive) | 15 (False Negative) |
| Actually Benign | 20 (False Positive) | 880 (True Negative) |

Calculate:
- (a) **Accuracy** = (TP + TN) / Total
- (b) **Precision** = TP / (TP + FP) — "Of predicted positives, how many are correct?"
- (c) **Recall** = TP / (TP + FN) — "Of actual positives, how many did we catch?"
- (d) In cancer detection, is it worse to have low precision or low recall?

**49.** Another model has:
- Accuracy: 95%
- Precision: 70%
- Recall: 99%

What does this tell you about the model's behavior?

---

**🤖 Expected Value**

**50.** Expected value: $E[X] = \sum x_i \cdot P(x_i)$

A game costs €5 to play. You roll a die:
- Roll 6: win €20
- Roll 5: win €10
- Roll anything else: win €0

- (a) Calculate the expected winnings.
- (b) What is the expected profit (winnings minus cost)?
- (c) Is this a fair game?

**51.** A trading algorithm has:
- 60% chance of €100 profit
- 25% chance of breaking even
- 15% chance of €200 loss

- (a) Calculate the expected value per trade.
- (b) Over 100 trades, what is the expected total profit?

---

**🤖 Bayes' Theorem Preview**

**52.** Bayes' Theorem:
$$P(A|B) = \frac{P(B|A) \cdot P(A)}{P(B)}$$

A factory has two machines:
- Machine A produces 60% of items, with 2% defect rate
- Machine B produces 40% of items, with 5% defect rate

An item is selected at random and found to be defective. What is the probability it came from Machine A?

- (a) Find $P(\text{defective})$ = P(def|A)P(A) + P(def|B)P(B)
- (b) Apply Bayes' Theorem

---

**🔬 Scientific Sampling**

**53.** A biologist wants to estimate the number of fish in a lake using capture-recapture:
- Day 1: Capture 100 fish, tag them, release
- Day 2: Capture 80 fish, find 10 are tagged

Using the proportion: $\frac{\text{tagged in sample}}{\text{sample size}} \approx \frac{\text{total tagged}}{\text{population}}$

Estimate the total fish population.

---

**🤖 Cross-Validation**

**54.** In 5-fold cross-validation, a model's accuracy on each fold is:

Fold 1: 88%, Fold 2: 85%, Fold 3: 90%, Fold 4: 87%, Fold 5: 85%

- (a) What is the mean accuracy?
- (b) What is the standard deviation?
- (c) Report the result as "mean ± SD"

---

**🎯 A/B Testing**

**55.** A website runs an A/B test on a new checkout button:
- Version A (old): 1000 visitors, 50 purchases (5% conversion)
- Version B (new): 1000 visitors, 65 purchases (6.5% conversion)

- (a) What is the relative improvement of B over A?
- (b) Is this difference "real" or could it be random chance? (This requires statistical tests we'll learn later, but intuitively, is 15 extra purchases out of 1000 a big deal?)

---

## Answer Key

### Part A: Central Tendency
1. Mean: 85.71, Median: 85, Mode: 85
2. Mean: 145, Median: 145, Mode: 145
3. (a) Mean: 2278.57, Median: 1450, Mode: none (b) Mean (c) Median
4. (a) With: 570, Without: 298.33 (b) With: 310, Without: 300
5. (a) 2875 (b) 3000 (c) 5000 (d) Model may overfit to majority classes
6. (a) 2.998 (b) Exactly matches!
10. 85.55
11. 0.56

### Part B: Spread
12. (a) 8 (b) -4, -2, 0, 2, 4 (c) 16, 4, 0, 4, 16 (d) 8 (e) 2.83
15. (a) Both 86% (b) A: 1.58, B: 10.30 (c) Model A
16. (a) Version 1.0: 1.25s (b) Version 1.0: 0.11, Version 2.0: 0.58 (c) Version 1.0
19. (a) 85-115 (b) 70-130 (c) ~2.5%
20. (a) 168-182 cm (b) ~189 cm (c) ~1.5%

### Part C: Probability
21. (a) 1/4 (b) 1/13 (c) 1/52 (d) 40/52 = 10/13
22. (a) 1/2 (b) 1/2 (c) 4/5
23. (a) 0.80 (b) 0.15 (c) 0.05
24. (a) 0.90 (b) 0.85 (c) 0.80 (d) 0.86
25. (a) 100 sick, 9900 healthy (b) 95 (c) 990 (d) 95/(95+990) ≈ 8.8%
26. (a) 0.30 (b) 0.9412 (c) ≈ 0.364
32. (a) 0.857 (b) 0.143 (c) 0.904
33. (a) 0.893 (b) ≈ 0.99997

### Part D: Counting
34. $26 \times 10 \times 26 \times 10 = 67,600$
35. $4 \times 6 \times 3 = 72$
36. $5! = 120$
37. $P(5,3) = 60$
38. $P(8,3) = 336$
39. $C(10,3) = 120$
40. $C(52,5) = 2,598,960$
41. $C(49,6) = 13,983,816$
42. (a) 120 (b) 252 (c) 1024
43. $3 \times 4 \times 4 \times 5 = 240$
44. (a) $4^3 = 64$ (b) More than enough to code 20 amino acids (with redundancy)
45. (a) $C(8,2) = 28$ (b) 56 hours

### Part E: ML Applications
48. (a) 0.965 (b) 0.81 (c) 0.85 (d) Low recall
50. (a) €5 (b) €0 (c) Fair game
51. (a) €30 (b) €3000
52. (a) 0.032 (b) 0.375
53. 800 fish
54. (a) 87% (b) 2.12% (c) 87% ± 2.12%
55. (a) 30% relative improvement

---

*End of Worksheet 6A*
