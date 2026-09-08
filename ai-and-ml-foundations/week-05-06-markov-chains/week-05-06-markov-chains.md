---
title: "Week 5-6: Building Complete Markov Chains"
slug: week-05-06-markov-chains
course: ai-and-ml-foundations
course_title: "AI and ML Foundations"
series: 6-projects-from-0-to-markov
series_title: "Projects / From 0 to Markov"
version: 2026.09.06.1
---

# Week 5-6: Building Complete Markov Chains

## From Analysis to Generation

So far, you've been **analyzing** sequences: taking data and computing probabilities.

This week, we flip the script. You'll **generate** sequences: creating new, realistic data from learned patterns.

This is where things get creative. By the end of this week, you'll be generating:
- Weather forecasts that look realistic
- Random walks with specific properties  
- Text that mimics patterns from input

We're building the foundation for Week 7-8, where we'll generate human-like text.

Let's formalize everything into a proper **Markov Chain** framework!

---

```python exec
id: week-05-06-markov-chains-1
import numpy as np
import matplotlib.pyplot as plt
from collections import defaultdict
import random

# For reproducibility
np.random.seed(42)
random.seed(42)
```

## Part 1: The Markov Property (Formally)

Let's be precise about what makes something a Markov chain.

### Definition

A sequence of random variables X₀, X₁, X₂, ... is a **Markov chain** if:

**P(Xₙ₊₁ = s | Xₙ = sₙ, Xₙ₋₁ = sₙ₋₁, ..., X₀ = s₀) = P(Xₙ₊₁ = s | Xₙ = sₙ)**

In plain English:
> *The probability of the next state depends only on the current state, not on the history.*

This is called the **Markov property** or **memorylessness**.

### Does This Hold in Reality?

Let's test it with our weather data:

```python exec
id: week-05-06-markov-chains-2
weather_sequence = ['Sunny', 'Sunny', 'Cloudy', 'Rainy', 'Rainy', 
                   'Cloudy', 'Sunny', 'Sunny', 'Sunny', 'Cloudy',
                   'Rainy', 'Cloudy', 'Sunny', 'Cloudy', 'Cloudy']

def test_markov_property(sequence):
    """
    Compare 1-step and 2-step conditional probabilities.
    If they're similar, Markov property likely holds.
    """
    # 1-step: current -> next
    one_step = defaultdict(lambda: defaultdict(int))
    for i in range(len(sequence) - 1):
        current = sequence[i]
        next_state = sequence[i + 1]
        one_step[current][next_state] += 1
    
    # 2-step: (previous, current) -> next
    two_step = defaultdict(lambda: defaultdict(int))
    for i in range(len(sequence) - 2):
        context = (sequence[i], sequence[i + 1])
        next_state = sequence[i + 2]
        two_step[context][next_state] += 1
    
    print("Testing Markov Property")
    print("=" * 60)
    
    # Normalize and compare
    for state in sorted(set(sequence)):
        if state in one_step and len(one_step[state]) > 0:
            total = sum(one_step[state].values())
            print(f"\nFrom {state}:")
            for next_state, count in sorted(one_step[state].items()):
                prob_1step = count / total
                print(f"  → {next_state}: {prob_1step:.2f}")

test_markov_property(weather_sequence)

print("\n" + "="*60)
print("With limited data, we ASSUME the Markov property holds.")
print("This simplification makes our models tractable!")
```

---

## Part 2: Building a Complete MarkovChain Class

Let's build a proper, reusable Markov Chain class that can both learn AND generate.

```python exec
id: week-05-06-markov-chains-3
class MarkovChain:
    """
    A complete Markov Chain implementation.
    Can learn from sequences and generate new ones.
    """
    
    def __init__(self, states=None):
        """
        Initialize with optional list of states.
        If None, states will be inferred from training data.
        """
        if states:
            self.states = sorted(list(states))
            self.n_states = len(self.states)
            self.state_to_idx = {state: idx for idx, state in enumerate(self.states)}
            self.idx_to_state = {idx: state for idx, state in enumerate(self.states)}
            self.transition_matrix = np.zeros((self.n_states, self.n_states))
        else:
            self.states = None
            self.transition_matrix = None
    
    def fit(self, sequence):
        """Learn transition probabilities from a sequence."""
        # Infer states if not provided
        if self.states is None:
            self.states = sorted(list(set(sequence)))
            self.n_states = len(self.states)
            self.state_to_idx = {state: idx for idx, state in enumerate(self.states)}
            self.idx_to_state = {idx: state for idx, state in enumerate(self.states)}
            self.transition_matrix = np.zeros((self.n_states, self.n_states))
        
        # Count transitions
        for i in range(len(sequence) - 1):
            current = sequence[i]
            next_state = sequence[i + 1]
            
            current_idx = self.state_to_idx[current]
            next_idx = self.state_to_idx[next_state]
            
            self.transition_matrix[current_idx][next_idx] += 1
        
        # Normalize rows to probabilities
        for i in range(self.n_states):
            row_sum = self.transition_matrix[i].sum()
            if row_sum > 0:
                self.transition_matrix[i] /= row_sum
        
        return self
    
    def next_state(self, current_state):
        """
        Generate the next state given current state.
        This is PROBABILISTIC - run it multiple times!
        """
        if current_state not in self.state_to_idx:
            raise ValueError(f"Unknown state: {current_state}")
        
        current_idx = self.state_to_idx[current_state]
        probabilities = self.transition_matrix[current_idx]
        
        # Randomly choose next state based on probabilities
        next_idx = np.random.choice(self.n_states, p=probabilities)
        return self.idx_to_state[next_idx]
    
    def generate_sequence(self, start_state, length):
        """
        Generate a sequence of given length starting from start_state.
        """
        if start_state not in self.state_to_idx:
            raise ValueError(f"Unknown start state: {start_state}")
        
        sequence = [start_state]
        current = start_state
        
        for _ in range(length - 1):
            current = self.next_state(current)
            sequence.append(current)
        
        return sequence
    
    def steady_state(self, iterations=100):
        """Calculate steady state distribution."""
        state_prob = np.ones(self.n_states) / self.n_states
        
        for _ in range(iterations):
            state_prob = state_prob @ self.transition_matrix
        
        return {state: state_prob[self.state_to_idx[state]] 
                for state in self.states}
    
    def visualize(self):
        """Visualize the transition matrix."""
        plt.figure(figsize=(10, 8))
        plt.imshow(self.transition_matrix, cmap='YlOrRd', aspect='auto', vmin=0, vmax=1)
        plt.colorbar(label='Probability', shrink=0.8)
        
        plt.xticks(range(self.n_states), self.states, rotation=45, ha='right')
        plt.yticks(range(self.n_states), self.states)
        plt.xlabel('Next State', fontsize=12, fontweight='bold')
        plt.ylabel('Current State', fontsize=12, fontweight='bold')
        plt.title('Markov Chain Transition Matrix', fontsize=14, fontweight='bold')
        
        # Add values
        for i in range(self.n_states):
            for j in range(self.n_states):
                val = self.transition_matrix[i, j]
                if val > 0:
                    color = 'white' if val > 0.5 else 'black'
                    plt.text(j, i, f'{val:.2f}', ha='center', va='center',
                            color=color, fontsize=11, fontweight='bold')
        
        plt.tight_layout()
        plt.show()
    
    def __repr__(self):
        return f"MarkovChain(states={self.n_states})"
```

### Test It Out!

```python exec
id: week-05-06-markov-chains-4
# Create and train the chain
mc = MarkovChain()
mc.fit(weather_sequence)

print(f"Learned model: {mc}")
print(f"States: {mc.states}")
print()

# Visualize
mc.visualize()

# Generate a 10-day forecast
print("\nGenerating 10-day weather forecast:")
forecast = mc.generate_sequence('Sunny', 10)
for i, weather in enumerate(forecast):
    print(f"Day {i+1}: {weather}")
```

**Run the cell above multiple times!** Notice how you get different sequences each time, but they all seem plausible given our learned patterns.

---

## Part 3: Analyzing Generated Sequences

Let's generate a LONG sequence and see if it matches our expectations:

```python exec
id: week-05-06-markov-chains-5
# Generate 1000 days of weather
long_sequence = mc.generate_sequence('Sunny', 1000)

# Count state frequencies
from collections import Counter
counts = Counter(long_sequence)

print("Generated 1000 days:")
print("=" * 50)
for state in sorted(mc.states):
    count = counts[state]
    percentage = count / 1000 * 100
    bar = "█" * int(percentage / 2)
    print(f"{state:10}: {bar} {count} ({percentage:.1f}%)")

print("\n" + "=" * 50)
print("Steady state (theoretical):")
steady = mc.steady_state()
for state in sorted(mc.states):
    prob = steady[state]
    print(f"{state:10}: {prob:.3f} ({prob*100:.1f}%)")

print("\nNotice: Long sequences converge to the steady state!")
```

### Visualize the Generated Sequence

```python exec
id: week-05-06-markov-chains-6
def visualize_sequence(sequence, title="Sequence", max_display=100):
    """
    Visualize a sequence as a time series.
    """
    # Convert to numbers
    unique_states = sorted(list(set(sequence)))
    state_to_num = {state: i for i, state in enumerate(unique_states)}
    
    # Only show first max_display elements
    display_seq = sequence[:max_display]
    nums = [state_to_num[s] for s in display_seq]
    
    plt.figure(figsize=(16, 4))
    plt.plot(nums, marker='o', markersize=4, linewidth=1.5, alpha=0.7)
    plt.yticks(range(len(unique_states)), unique_states)
    plt.xlabel('Time Step', fontsize=12)
    plt.ylabel('State', fontsize=12)
    plt.title(f'{title} (first {max_display} steps)', fontsize=14)
    plt.grid(True, alpha=0.3, axis='x')
    plt.tight_layout()
    plt.show()

visualize_sequence(long_sequence, "Generated Weather", max_display=100)
```

---

## Part 4: Practical Example - Stock Market Simulation

Let's model a simplified stock market with three states:
- **Up**: Stock price increased
- **Flat**: Stock price stayed roughly the same  
- **Down**: Stock price decreased

We'll learn from historical patterns (made up) and generate future scenarios.

```python exec
id: week-05-06-markov-chains-7
# Simulated historical stock movements
stock_history = [
    'Flat', 'Up', 'Up', 'Flat', 'Down', 'Down', 'Flat', 'Up', 'Up', 'Up',
    'Flat', 'Down', 'Flat', 'Up', 'Flat', 'Flat', 'Up', 'Down', 'Down', 'Flat',
    'Up', 'Up', 'Flat', 'Up', 'Down', 'Flat', 'Flat', 'Up', 'Up', 'Flat',
    'Down', 'Down', 'Down', 'Flat', 'Up', 'Flat', 'Up', 'Up', 'Up', 'Down'
]

print("Historical stock movements (40 days):")
visualize_sequence(stock_history, "Stock History", max_display=40)

# Train a Markov chain
stock_mc = MarkovChain()
stock_mc.fit(stock_history)

print("\nLearned transition probabilities:")
stock_mc.visualize()
```

### Generate Multiple Scenarios

In finance, we often want to simulate multiple possible futures:

```python exec
id: week-05-06-markov-chains-8
def simulate_scenarios(mc, start_state, n_days, n_scenarios=5):
    """
    Generate multiple possible futures.
    """
    scenarios = []
    for _ in range(n_scenarios):
        scenario = mc.generate_sequence(start_state, n_days)
        scenarios.append(scenario)
    return scenarios

# Generate 5 possible futures
scenarios = simulate_scenarios(stock_mc, 'Flat', 20, n_scenarios=5)

print("5 Possible Futures (20 days each):\n")
for i, scenario in enumerate(scenarios, 1):
    print(f"Scenario {i}: {' → '.join(scenario)}")
    
# Count outcomes
print("\n" + "="*60)
print("Summary across all scenarios:")
all_outcomes = [state for scenario in scenarios for state in scenario]
outcome_counts = Counter(all_outcomes)
for state in sorted(stock_mc.states):
    count = outcome_counts[state]
    percentage = count / len(all_outcomes) * 100
    print(f"{state:6}: {count:3} days ({percentage:.1f}%)")
```

### Convert to Price Movements

Let's turn these states into actual prices:

```python exec
id: week-05-06-markov-chains-9
def scenario_to_prices(scenario, start_price=100, up_pct=2, down_pct=2, flat_pct=0.5):
    """
    Convert state sequence to price sequence.
    """
    prices = [start_price]
    
    for state in scenario:
        current_price = prices[-1]
        
        if state == 'Up':
            change = np.random.uniform(0, up_pct)
            new_price = current_price * (1 + change/100)
        elif state == 'Down':
            change = np.random.uniform(0, down_pct)
            new_price = current_price * (1 - change/100)
        else:  # Flat
            change = np.random.uniform(-flat_pct, flat_pct)
            new_price = current_price * (1 + change/100)
        
        prices.append(new_price)
    
    return prices

# Visualize scenarios as price charts
plt.figure(figsize=(14, 6))

for i, scenario in enumerate(scenarios):
    prices = scenario_to_prices(scenario, start_price=100)
    plt.plot(prices, label=f'Scenario {i+1}', alpha=0.7, linewidth=2)

plt.xlabel('Days', fontsize=12)
plt.ylabel('Price ($)', fontsize=12)
plt.title('5 Simulated Stock Price Scenarios', fontsize=14, fontweight='bold')
plt.legend()
plt.grid(True, alpha=0.3)
plt.axhline(y=100, color='black', linestyle='--', alpha=0.5, label='Start Price')
plt.tight_layout()
plt.show()

print("\nFinal prices across scenarios:")
for i, scenario in enumerate(scenarios, 1):
    prices = scenario_to_prices(scenario, start_price=100)
    final_price = prices[-1]
    change = ((final_price - 100) / 100) * 100
    print(f"Scenario {i}: ${final_price:.2f} ({change:+.1f}%)")
```

---

## Part 5: Introduction to Higher-Order Markov Chains

So far, we've used **first-order** Markov chains: the next state depends only on the current state.

But what if we want the next state to depend on the **last two states**? Or three?

This is called a **higher-order Markov chain**.

### Second-Order Example

```python exec
id: week-05-06-markov-chains-10
class MarkovChainOrder2:
    """
    Second-order Markov Chain.
    Next state depends on the last TWO states.
    """
    
    def __init__(self):
        self.transitions = defaultdict(lambda: defaultdict(int))
        self.transition_probs = {}
    
    def fit(self, sequence):
        """Learn from sequence."""
        # Count transitions: (state_i, state_{i+1}) -> state_{i+2}
        for i in range(len(sequence) - 2):
            context = (sequence[i], sequence[i+1])
            next_state = sequence[i+2]
            self.transitions[context][next_state] += 1
        
        # Convert to probabilities
        for context, next_states in self.transitions.items():
            total = sum(next_states.values())
            self.transition_probs[context] = {
                state: count/total 
                for state, count in next_states.items()
            }
        
        return self
    
    def next_state(self, state1, state2):
        """Predict next state given last two states."""
        context = (state1, state2)
        
        if context not in self.transition_probs:
            # Fallback: return random state
            all_states = set()
            for probs in self.transition_probs.values():
                all_states.update(probs.keys())
            return random.choice(list(all_states))
        
        probs = self.transition_probs[context]
        states = list(probs.keys())
        probabilities = list(probs.values())
        
        return np.random.choice(states, p=probabilities)
    
    def generate_sequence(self, state1, state2, length):
        """Generate sequence starting with two states."""
        sequence = [state1, state2]
        
        for _ in range(length - 2):
            next_s = self.next_state(sequence[-2], sequence[-1])
            sequence.append(next_s)
        
        return sequence

# Train on weather
mc2 = MarkovChainOrder2()
mc2.fit(weather_sequence)

print("Second-order model learned!")
print("\nSome learned patterns:")
for context, probs in list(mc2.transition_probs.items())[:5]:
    print(f"{context} → {probs}")

# Generate
print("\nGenerated sequence (second-order):")
seq2 = mc2.generate_sequence('Sunny', 'Sunny', 15)
print(' → '.join(seq2))
```

### Why Higher-Order Chains?

**Pro:** More context = better predictions  
**Con:** Need MUCH more data (exponentially more)

For text generation (next week!), we'll use higher-order chains to capture patterns like:
- First-order: "the" → "dog"
- Second-order: ("the", "brown") → "dog"

The second-order chain knows that "the brown" is often followed by a noun!

---

## Part 6: Real-World Application - Customer Journey

Let's model how customers move through a website:
- **Home**: Landing page
- **Browse**: Looking at products
- **Cart**: Added items to cart
- **Checkout**: Purchasing
- **Exit**: Left the site

```python exec
id: week-05-06-markov-chains-11
# Simulated customer journeys
journeys = [
    ['Home', 'Browse', 'Browse', 'Cart', 'Checkout', 'Exit'],
    ['Home', 'Browse', 'Exit'],
    ['Home', 'Browse', 'Browse', 'Browse', 'Exit'],
    ['Home', 'Browse', 'Cart', 'Browse', 'Cart', 'Checkout', 'Exit'],
    ['Home', 'Browse', 'Cart', 'Exit'],
    ['Home', 'Exit'],
    ['Home', 'Browse', 'Browse', 'Cart', 'Checkout', 'Exit'],
    ['Home', 'Browse', 'Cart', 'Checkout', 'Exit'],
    ['Home', 'Browse', 'Browse', 'Exit'],
    ['Home', 'Browse', 'Cart', 'Browse', 'Exit'],
]

# Flatten to single sequence
customer_sequence = [state for journey in journeys for state in journey]

# Train model
customer_mc = MarkovChain()
customer_mc.fit(customer_sequence)

print("Customer Journey Model:")
customer_mc.visualize()

# Key insights
print("\nKey Insights:")
print("=" * 50)

# Probability of checkout from cart
cart_idx = customer_mc.state_to_idx['Cart']
checkout_idx = customer_mc.state_to_idx['Checkout']
p_checkout = customer_mc.transition_matrix[cart_idx, checkout_idx]
print(f"Probability of checkout from cart: {p_checkout:.1%}")

# Probability of exit from browse
browse_idx = customer_mc.state_to_idx['Browse']
exit_idx = customer_mc.state_to_idx['Exit']
p_exit_browse = customer_mc.transition_matrix[browse_idx, exit_idx]
print(f"Probability of exit from browse: {p_exit_browse:.1%}")

# Simulate 100 customers
conversions = 0
for _ in range(100):
    journey = customer_mc.generate_sequence('Home', 10)
    if 'Checkout' in journey:
        conversions += 1

print(f"\nSimulated conversion rate: {conversions}%")
```

---

## Week 5-6 Summary

You've built a complete Markov Chain framework!

### Core Concepts Mastered
- **Markov Property**: Future depends only on present
- **Learning**: Building transition matrices from data
- **Generation**: Creating new sequences probabilistically
- **Analysis**: Understanding long-term behavior (steady states)

### Technical Skills
- Object-oriented programming (classes)
- Matrix operations with NumPy
- Probability distributions
- Random sampling
- Data visualization

### Applications Explored
- Weather forecasting
- Stock market simulation
- Customer journey modeling
- Higher-order chains

---

## Looking Ahead: Week 7-8

Next week is where it gets really exciting: **TEXT GENERATION**!

We'll apply everything you've learned to:
- Character-level text generation
- Word-level text generation
- Building a "writer" that mimics authors
- Creating fake tweets, poems, and more

Get ready to see your Markov chains produce surprisingly realistic text!

---

## Try this Problems

### Try this 1: Game State Modeling
Model a simple game with states: Start, Playing, Paused, GameOver, Victory. Create realistic transitions and generate 100 game sessions.

```python exec
id: week-05-06-markov-chains-12
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
# Your game model here
```

### Try this 2: Third-Order Chain
Implement a third-order Markov chain that depends on the last THREE states.

```python exec
id: week-05-06-markov-chains-13
# Third-order implementation
```

### Try this 3: Transition Comparison
Generate 1000 sequences from your weather model. Calculate the transition probabilities from the generated data. Do they match your original model?

```python exec
id: week-05-06-markov-chains-14
# Validation experiment
```

### Try this 4: Emoji Sequence Generator
Create a Markov chain using emoji as states. Train it on a sequence you create (e.g., emoji stories) and generate new sequences.

```python exec
id: week-05-06-markov-chains-15
# Emoji Markov chain
# Example: ['😊', '😊', '😢', '😊', '😍', ...]
```

### Try this 5: Convergence Analysis
For different starting states, measure how many steps it takes to get within 1% of the steady state. Which starting states converge fastest?

```python exec
id: week-05-06-markov-chains-16
# Convergence speed analysis
```

## Looking back

Before leaving this page, a sentence on each. What you write stays on this device.

```reflect
- Something you expected before running a cell that turned out differently
- The one idea from this page you could explain to someone else now
- Something you would change or try next, if there were time
- A question this page raised for you that it did not answer. Bring it to the next session; these questions are where the next session starts.
```
