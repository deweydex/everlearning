---
title: "Refresher of Combinations and Permutations"
slug: combinations-permutations-and-big-o
course: ai-and-ml-foundations
course_title: "AI and ML Foundations"
series: 3-probability-and-statistics-enrichment
series_title: "Probability and Statistics / Enrichment"
version: 2026.09.06.1
---

# Refresher of Combinations and Permutations

Let's create two functions to refresh our memories from our statistics and probability classes.

Suppose you are given a list of n numbers, how might you create a function that counts the number of ways you can reorder that list?

```python exec
id: combinations-permutations-and-big-o-1
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
# Your code here
```

Let's see if we can write another function that returns a list of all the lists we have counted.

With those two challenges in mind, can you count the number of ways you can choose k items from that list? (Remember our N choose k function? Might be helpful here...) But this time, instead of just returning the number of subsets, lets return the number of subsets and a list of them.

```python exec
id: combinations-permutations-and-big-o-2
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
# Your code here
```

 # Time Complexity and big O notation

 Let's talk a little bit about something called Time Complexity

```python exec
id: combinations-permutations-and-big-o-3
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
# Your code here
```

```python exec
id: combinations-permutations-and-big-o-4
# I would like to code a function that takes a certain number to a given power

def my_exp(base, power):
    # 5^6: 5 * 5 * 5 * 5 * 5 * 5
    result = 1
    for index in range(power):
        result = result * base
    return result

print(my_exp(2, 5))
# this has a big-O or O(power)
# but we want faster!!!
# big-O or O(log(power))
```

```python exec
id: combinations-permutations-and-big-o-5
def my_log(base, result):
    log_like = result
    counter = 0
    while log_like > 1:
        log_like = log_like/base
        counter += 1
    return counter

print(my_log(2, 32))
# here the big-O or O(log_base(result))
```

```python exec
id: combinations-permutations-and-big-o-6
def fast_exp(base, power):
    # 2^8 = 2^4 * 2^4 , 2^4 = 2^2 * 2^2, 2^2 = 2 * 2
    # bottom case:
    if power == 1:
        return base
    if power % 2 == 0: # if power is even
        new_power = power / 2
        # base ** new_power * base ** new_power
        return fast_exp(base, new_power) * fast_exp(base, new_power)
    if power % 2 == 1: # if power is odd
    # every odd number can be written as an even number +1
    # base ** odd_power = base ** (even_power) + 1
    # base ** odd_power = base ** (odd_power-1)/2 * base ** (odd_power-1)/2  * base**1`
    # n-1/2 + n-1/2 + 1 = (n-1 + n-1 + 2)/2 = 2n /2 = n
        new_power = (power-1)/2
        return fast_exp(base, new_power) * fast_exp(base, new_power) * base

print(fast_exp(2, 5))
```

```python exec
id: combinations-permutations-and-big-o-7
def fast_exp2(base, power, sneakylist = []):
    # whenever we return anything, lets store it!
    sneakylist.append(base)
    # first item in my list is base^1
    while sneakylist[-1] <= base**power:
        sneakylist.append(sneakylist[-1]*sneakylist[-1])
        # [2, 2*2, 2*2*2*2, ...]  the list grows as 2**(2**k)
    return sneakylist
# 2 = 2**1, 4 = 2**2, 8 = 2**3, 16 = 2**4, 32, 64, 128, 256
print(fast_exp2(2,16 ))
```

## Let's Start Fresh with a New Problem

Lets just think about our friend the factorial function. $$Factorial(n) = n!= n \cdot (n-1) \cdot (n-2) \cdot 3 \cdot 2 \cdots 1 $$

If we stare at that for a while, we might write that same function this way:

$$ Factorial(n) = n \cdot Factorial (n-1) $$
$$ F(n) = n \cdot F(n-1)$$
$$ F_n = n \cdot F_{n-1}$$
Well thats nice! But that only works if we know when to stop subtracting one! In our case we can say definitively that $Factorial(0) = 0! = 1$ (If you want to use the combinatorics or counting interpretation of factorial you can ask, how many ways are there to arrange 0 things in a row?... there is just one way, but its a boring one!)

 But lets see if we can code both of these ways of writing factorial:

```python exec
id: combinations-permutations-and-big-o-8
# our first factorial will involve a loop:

def classic_factorial(n: int) -> int:
    factorial = 1
    for index in range(1,n+1): # list from 1 to n [1, 2, 3, ... , n]
        factorial = factorial * index
        # we call this an accumulator: it accumulates our calculation as we go
    return factorial

def recursive_factorial(n):
    if n is 0:
        return 1
    else:
        return n * recursive_factorial(n-1)
# this might be 2n calculations if we count our if statement
# BUT it will never take n^2 calculations for big n
def fancy_recursive_factorial(n):
    return 1 if n is 0 else n * fancy_recursive_factorial(n-1)

classic_factorial(23)
```

But our question is, how many steps will this take? How many calculations did we do with each turn of our loop?
After staring at this for a while and asking ourselves some questions, we think this takes approximately $n$ steps. (so we can say) All of those functions are $O(n)$.

```python exec
id: combinations-permutations-and-big-o-9
def weird_square(n):
    weird_sum = 0
    for i in range(n):
        for j in range(n):
            weird_sum = weird_sum + 1
    return weird_sum

weird_square(3)


# for i in range(n) range(n) is [0, 1, 2, 3, 4, 5, 6, 7, ... n-1, n]

def weird_cube(n):
    weird_sum = 0
    for i in range(n):
        for j in range(n):
            for k in range(n):
                weird_sum = weird_sum + 1
    return weird_sum

def schmoo(n):
    weird_product = 1
    for i in range(n):
        weird_product = weird_product * n
    return weird_product

schmoo(4)

schmoo_list = [schmoo(n) for n in range(6)]
print(schmoo_list)

def better_square(n):
    return n*n
def basic_square(n):
    return sum([n for i in range(n)])
#weird_cube(2)
```

What if I want to multiply two lists together?

```python exec
id: combinations-permutations-and-big-o-10
def multiply_lists(list1, list2):
    #lists are the same length
    n = len(list1)
    multiplied_list = [1]*n
    for i in range(n):
        multiplied_list[i] = list1[i]*list2[i]
    return multiplied_list

def fancy_multiply_lists(list1, list2):
    return [list1[i]*list2[i] for i in range(len(list1))]

def boring_list_function(list1):
    for i in list1:
        print(i)

multiply_lists([1,2,3,4],[1,2,3,4])
```

```python exec
id: combinations-permutations-and-big-o-11
def powers_of_n(n, max):
    return [n**i for i in range(max+1)]

def alt_powers_of_n(n, max):

    power_list = [1]*(max+1)
    for i in range(1, max+1):
        power_list[i] = power_list[i - 1]*n # look at this for question 2 of assignment 2!!!

    return power_list

# we want to write a nxn array with 100 items, how would that look
import numpy as np
# make a random matrix with 10 x 10 items
my_matrix = np.random.randint(10, size=(10, 10))
print(my_matrix)

new_matrix = my_matrix * my_matrix
print(new_matrix)
# so these two are O(n**2) operations!


# these two are both O(n)
print(powers_of_n(2, 10))
print(alt_powers_of_n(2, 10))
```

## Sigma and Pi notation

You might have seen this in your mathematical travels

$$ \sum_{k = 1}^n k $$

$$ \sum_{k = 1}^n k^2 $$

$$ \sum_{k = 1}^n \frac{1}{k} $$

$$ \prod_{k = 1}^n k $$

$$ \prod_{k = 1}^n k^2 $$

$$ \prod_{k = 1}^n \frac{1}{k} $$

Lets write these in code!

```python exec
id: combinations-permutations-and-big-o-12
def sum_of_k(n):
    # we assume n > our starting k
    accumulator = 0
    for k in range(1,n+1): # because we start with our 1, and include our max n
        accumulator = accumulator + k
    return accumulator

def sum_of_k_squared(n):
    # we assume n > our starting k
    accumulator = 0
    for k in range(1,n):# because we start with our 1, and include our max n
        accumulator = accumulator + k**2
    return accumulator

def sum_of_one_over_k(n):
    # we assume n > our starting k
    accumulator = 0.0
    for k in range(1,n+1):# because we start with our 1, and include our max n
        accumulator = accumulator + 1.0/k
    return accumulator

def product_of_k(n):
    # we assume n > our starting k
    accumulator = 1
    for k in range(1,n+1):# because we start with our 1, and include our max n
        accumulator = accumulator * k
    return accumulator
```

$$ \sum_{k = 1}^n f(k) $$

```
def sum_of_function_of_k(n):
    # we assume n > our starting k
    accumulator = 0
    for k in range(1,n+1):# because we start with our 1, and include our max n
        accumulator = accumulator + my_function(k)
    return accumulator
```

$$ \sum_{k = 6}^{n = 24} \frac{k^3}{8} + k - \frac{1}{k}$$

```python exec
id: combinations-permutations-and-big-o-13
print([k**3/8 + k - 1/k for k in range(6,24+1)])
```

```python exec
id: combinations-permutations-and-big-o-14
def sum_of_1_over_2_to_the(n):
    # we assume n > our starting k
    accumulator = 0
    for k in range(1,n):# because we start with our 1, and include our max n
        accumulator += 1/(2**k)
    return accumulator
range(1, 10, 2)
def better_sum_of_function_n(start, stop, my_function):
    # we assume n > our starting k
    accumulator = 0
    for k in range(start,stop+1):# because we start with our 1, and include our max n
        accumulator += my_function(k)
    return accumulator


def better_e(x, num_terms, start =1):
    # we assume n > our starting k
    accumulator = 0
    for k in range(start,num_terms+1):# because we start with our 1, and include our max n
        accumulator += x**k/ classic_factorial(k)
    return accumulator
print(better_e(11, 10))
better_e(4,6)

def sin(x, num_terms):
    accumulator = 0
    for k in range(1, num_terms+1):
        accumulator = accumulator + (-1)**k * x**(2*k + 1) / classic_factorial(2*k+1)
```

$$newfunction(x, numberofterms) =  \sum_{k = 1}^{numberofterms} myfunction(x,k) $$

We can do a little better! Lets put in all of the parameters we can set in our sigma or pi notations above:

```python exec
id: combinations-permutations-and-big-o-15
def sum_of_k(min, max):
    # we assume n > our starting k
    accumulator = 0
    for k in range(min,max+1): # because we start with our 1, and include our max n
        accumulator = accumulator + k
    return accumulator

def sum_of_k_squared(min,max):
    # we assume n > our starting k
    accumulator = 0
    for k in range(min,max+1): # because we start with our 1, and include our
        accumulator = accumulator + k**2
    return accumulator

def sum_of_one_over_k(min,max):
    # we assume n > our starting k
    accumulator = 0.0
    for k in range(min,max+1): # because we start with our 1, and include our
        accumulator = accumulator + 1.0/k
    return accumulator

def product_of_k(min,max):
    # we assume n > our starting k
    accumulator = 1
    for k in range(min,max+1): # because we start with our 1, and include our
        accumulator = accumulator * k
    return accumulator
```

here is a piece of sigma notation (double click to see the parameters:

$$  \sum_{k = min}^{max} function(k)    $$

here is an equivalently boring piece of pi notation:

$$  \prod_{k = min}^{max} function(k)    $$

```python exec
id: combinations-permutations-and-big-o-16
def sigma(min, max, my_function):
    # you might need to know something about function though right?
    # we assume max > our starting min
    accumulator = 0
    for k in range(min,max+1): # because we start with our min, and include our max
        accumulator = accumulator + my_function(k)
    return accumulator

def pi(min, max, my_function):
    # you might need to know something about function though right?
    # we assume max > our starting min
    accumulator = 1
    for k in range(min,max+1): # because we start with our min, and include our max
        accumulator = accumulator * my_function(k)
    return accumulator
```

## Looking back

Before leaving this page, a sentence on each. What you write stays on this device.

```reflect
- Something you expected before running a cell that turned out differently
- The one idea from this page you could explain to someone else now
- Something you would change or try next, if there were time
- A question this page raised for you that it did not answer. Bring it to the next session; these questions are where the next session starts.
```
