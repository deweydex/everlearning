---
title: "Birthday Paradox"
slug: birthday-problem
course: ai-and-ml-foundations
course_title: "AI and ML Foundations"
series: 3-probability-and-statistics-enrichment
series_title: "Probability and Statistics / Enrichment"
version: 2026.09.06.1
---

```python exec
id: birthday-problem-1
import math
```

# Birthday Paradox

we have 365/366 days in a year, everybody has one (and exactly one) birthday, and we will assume that things like "whether there are twins" and "whether there are more valentines day babies than october babies" are negligible.

What do we think (just based on intuition) the probability of two people having the same birthday in a class of size N... (in our case, theoretically, a class size of 22)?

A. P < 1%
B. 1% < P < 10%
C. 10% < P < 49%
D. 50% < P
E. Almost Certian (P > 99%!)


Let's answer a different question Q.
What are the odds that in a class of N people, everyone has a different birthday?

How many options would your first person have for a birthday? (We can just pick someone at random)

$Person_1$ has 365 - 0 options

$Person_2$ has 365 - 1 options

$Person_3$ has 365 - 2 options...

$Person_{n-1}$ has 365 - ((n-1)-1)

$Person_n$ has 365 - (n - 1)


$$\frac{365}{365}\cdot \frac{364}{365}\cdot \frac{363}{365} \cdots \frac{365 - (n-1)}{365}$$

This thing Q that we are solving for, is the complement of our original question P:

$ P = 1 - Q$

```python exec
id: birthday-problem-2
def birthdaypair(class_size):
  days_in_year = 365
  top = float(math.prod(list(range(365, 365-class_size, -1))))
  bottom = 365.0**class_size
  return 1 - top/bottom
```

```python exec
id: birthday-problem-3
class_size = 5
top = math.prod(list(range(365, 365-class_size, -1)))
print(top)
```

```python exec
id: birthday-problem-4
print(round(birthdaypair(9)*100,2), "%")
```

```python exec
id: birthday-problem-5
import matplotlib.pyplot as plt
class_sizes = range(2, 61)
print(list(class_sizes))
birthday_pair_prob = [100*birthdaypair(class_size) for class_size in class_sizes]
plt.plot(class_sizes, birthday_pair_prob)
plt.xlabel("class size")
plt.ylabel("percent probability of pair")
```

```python exec
id: birthday-problem-6
print(round(100* birthdaypair(23),2),"%")
```

```python exec
id: birthday-problem-7
print(round(100* birthdaypair(60),2),"%")
```

## Please Comment the Code Below

```python exec
id: birthday-problem-8
import random as rn

num_samples = 10000
num_successes = 0
prob_by_class_size = []
max_class_size = 60
for class_size in range(2, max_class_size+1):
  num_successes = 0
  for i in range(num_samples):
    people_in_class = [rn.randrange(365) for person in range(class_size)]
    set_class = set(people_in_class)
    if len(set_class) < class_size: # this means we have a collision! two folks have the same b-day!
      num_successes+=1
  prob_by_class_size.append(round(num_successes/num_samples *100, 2))

print(prob_by_class_size)
```

```python exec
id: birthday-problem-9
class_sizes = range(2, 60+1)
birthday_pair_prob = [100*birthdaypair(class_size) for class_size in class_sizes]
plt.plot(class_sizes, birthday_pair_prob, linestyle='--')
plt.plot(class_sizes, prob_by_class_size)
plt.legend(["theoretical", "empirical"])
plt.xlabel("class size")
plt.ylabel("percent probability of pair")
```

```python exec
id: birthday-problem-10
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
# Your code here
```

## Looking back

Before leaving this page, a sentence on each. What you write stays on this device.

```reflect
- Something you expected before running a cell that turned out differently
- The one idea from this page you could explain to someone else now
- Something you would change or try next, if there were time
- A question this page raised for you that it did not answer. Bring it to the next session; these questions are where the next session starts.
```
