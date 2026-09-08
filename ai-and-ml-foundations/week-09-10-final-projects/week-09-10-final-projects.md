---
title: "Week 9-10: Final Projects & Applications"
slug: week-09-10-final-projects
course: ai-and-ml-foundations
course_title: "AI and ML Foundations"
series: 6-projects-from-0-to-markov
series_title: "Projects / From 0 to Markov"
version: 2026.09.06.1
---

# Week 9-10: Final Projects & Applications

## Bringing It All Together

You've come a long way:
- Week 0: Learned Python fundamentals
- Week 1-2: Explored probability through simulation 
- Week 3-4: Mastered matrices and linear algebra
- Week 5-6: Built complete Markov chains
- Week 7-8: Generated realistic text

Now it's time to build something impressive.

This week, you'll complete **three major projects**:
1. **Weather Forecasting System** - Multi-day predictions with confidence intervals
2. **Text Generation Application** - A polished text generator with multiple modes
3. **Your Choice** - Stock simulation, game AI, or creative application

Then we'll evaluate, analyze, and reflect on what you've built.

Let's make something you're proud of! 

---

```python exec
id: week-09-10-final-projects-1
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from collections import defaultdict, Counter
import random
from datetime import datetime, timedelta

np.random.seed(42)
random.seed(42)
```

## Project 1: Advanced Weather Forecasting System

Build a complete weather forecasting application with:
- Multi-day forecasts
- Confidence intervals
- Historical accuracy tracking
- Visualization dashboard

```python exec
id: week-09-10-final-projects-2
class WeatherForecaster:
    """
    Advanced weather forecasting with Markov chains.
    """
    
    def __init__(self, order=1):
        self.order = order
        self.transitions = defaultdict(lambda: defaultdict(int))
        self.transition_probs = {}
        self.states = None
        self.history = []  # Track actual weather for accuracy
        self.predictions = []  # Track our predictions
    
    def fit(self, weather_sequence):
        """Learn from historical weather data."""
        self.states = sorted(list(set(weather_sequence)))
        
        # Learn transitions
        for i in range(len(weather_sequence) - self.order):
            context = tuple(weather_sequence[i:i+self.order])
            next_state = weather_sequence[i+self.order]
            self.transitions[context][next_state] += 1
        
        # Convert to probabilities
        for context, next_states in self.transitions.items():
            total = sum(next_states.values())
            self.transition_probs[context] = {
                state: count/total 
                for state, count in next_states.items()
            }
        
        return self
    
    def forecast(self, current_weather, days=7, n_simulations=100):
        """
        Generate probabilistic forecast for next N days.
        Returns probabilities for each day and state.
        """
        if isinstance(current_weather, str):
            current_weather = [current_weather]
        
        # Run many simulations
        simulations = []
        for _ in range(n_simulations):
            forecast = self._generate_sequence(current_weather, days)
            simulations.append(forecast)
        
        # Calculate probabilities for each day
        daily_probs = []
        for day in range(days):
            day_states = [sim[day] for sim in simulations]
            counts = Counter(day_states)
            probs = {state: counts[state]/n_simulations for state in self.states}
            # Fill in missing states with 0
            for state in self.states:
                if state not in probs:
                    probs[state] = 0
            daily_probs.append(probs)
        
        return daily_probs, simulations
    
    def _generate_sequence(self, start, length):
        """Generate a single weather sequence."""
        sequence = list(start) if isinstance(start, (list, tuple)) else [start]
        
        for _ in range(length):
            context = tuple(sequence[-self.order:])
            
            if context not in self.transition_probs:
                # Fallback to random state
                next_state = random.choice(self.states)
            else:
                probs = self.transition_probs[context]
                states = list(probs.keys())
                probabilities = list(probs.values())
                next_state = np.random.choice(states, p=probabilities)
            
            sequence.append(next_state)
        
        return sequence[-length:]  # Return only the forecast part
    
    def most_likely_forecast(self, current_weather, days=7):
        """Return the most likely state for each day."""
        daily_probs, _ = self.forecast(current_weather, days)
        
        forecast = []
        for day_probs in daily_probs:
            most_likely = max(day_probs.items(), key=lambda x: x[1])
            forecast.append(most_likely)
        
        return forecast
    
    def visualize_forecast(self, current_weather, days=7, n_simulations=100):
        """Create visualization of probabilistic forecast."""
        daily_probs, simulations = self.forecast(current_weather, days, n_simulations)
        
        # Create figure with subplots
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 10))
        
        # Plot 1: Probability evolution
        days_range = range(1, days + 1)
        colors = {'Sunny': '#FFD700', 'Cloudy': '#C0C0C0', 'Rainy': '#4169E1'}
        
        for state in self.states:
            probs = [day_probs[state] for day_probs in daily_probs]
            ax1.plot(days_range, probs, marker='o', label=state, 
                    linewidth=2.5, markersize=8,
                    color=colors.get(state, 'gray'))
        
        ax1.set_xlabel('Days Ahead', fontsize=12, fontweight='bold')
        ax1.set_ylabel('Probability', fontsize=12, fontweight='bold')
        ax1.set_title(f'{days}-Day Probabilistic Forecast (from {current_weather})', 
                     fontsize=14, fontweight='bold')
        ax1.legend(fontsize=11)
        ax1.grid(True, alpha=0.3)
        ax1.set_ylim(0, 1)
        
        # Plot 2: Sample simulations
        state_to_num = {state: i for i, state in enumerate(self.states)}
        
        for i, sim in enumerate(simulations[:20]):  # Show first 20 simulations
            nums = [state_to_num[s] for s in sim]
            ax2.plot(days_range, nums, alpha=0.3, linewidth=1)
        
        ax2.set_xlabel('Days Ahead', fontsize=12, fontweight='bold')
        ax2.set_ylabel('Weather State', fontsize=12, fontweight='bold')
        ax2.set_title('Sample Forecast Trajectories (20 simulations)', 
                     fontsize=14, fontweight='bold')
        ax2.set_yticks(range(len(self.states)))
        ax2.set_yticklabels(self.states)
        ax2.grid(True, alpha=0.3, axis='x')
        
        plt.tight_layout()
        plt.show()
        
        return daily_probs
    
    def evaluate_accuracy(self, test_sequence, forecast_days=3):
        """
        Evaluate forecast accuracy on test data.
        """
        correct_predictions = 0
        total_predictions = 0
        
        # For each position in test sequence
        for i in range(len(test_sequence) - forecast_days):
            current = test_sequence[i]
            actual_future = test_sequence[i+1:i+1+forecast_days]
            
            # Make forecast
            forecast = self.most_likely_forecast(current, forecast_days)
            predicted = [state for state, _ in forecast]
            
            # Check accuracy
            for pred, actual in zip(predicted, actual_future):
                if pred == actual:
                    correct_predictions += 1
                total_predictions += 1
        
        accuracy = correct_predictions / total_predictions if total_predictions > 0 else 0
        return accuracy
```

### Test the Weather Forecaster

```python exec
id: week-09-10-final-projects-3
# Generate synthetic weather data
def generate_weather_data(days=100):
    """Generate realistic weather patterns."""
    weather = []
    current = random.choice(['Sunny', 'Cloudy', 'Rainy'])
    
    # Simple rules for realistic weather
    for _ in range(days):
        weather.append(current)
        
        if current == 'Sunny':
            current = np.random.choice(['Sunny', 'Cloudy', 'Rainy'], 
                                      p=[0.6, 0.3, 0.1])
        elif current == 'Cloudy':
            current = np.random.choice(['Sunny', 'Cloudy', 'Rainy'], 
                                      p=[0.3, 0.4, 0.3])
        else:  # Rainy
            current = np.random.choice(['Sunny', 'Cloudy', 'Rainy'], 
                                      p=[0.2, 0.5, 0.3])
    
    return weather

# Generate data
training_weather = generate_weather_data(200)
test_weather = generate_weather_data(50)

print(f"Training data: {len(training_weather)} days")
print(f"Test data: {len(test_weather)} days")
print(f"\nFirst 20 days of training: {training_weather[:20]}")
```

```python exec
id: week-09-10-final-projects-4
# Train forecaster
forecaster = WeatherForecaster(order=1)
forecaster.fit(training_weather)

# Make forecast
print("7-Day Forecast from 'Sunny':")
print("=" * 60)
daily_probs = forecaster.visualize_forecast('Sunny', days=7, n_simulations=200)
```

```python exec
id: week-09-10-final-projects-5
# Most likely forecast
most_likely = forecaster.most_likely_forecast('Sunny', days=7)

print("\nMost Likely Forecast:")
print("=" * 60)
for day, (state, prob) in enumerate(most_likely, 1):
    print(f"Day {day}: {state:10} (confidence: {prob:.1%})")
```

```python exec
id: week-09-10-final-projects-6
# Evaluate accuracy
accuracy = forecaster.evaluate_accuracy(test_weather, forecast_days=3)
print(f"\n3-Day Forecast Accuracy on Test Set: {accuracy:.1%}")
```

---

## Project 2: Advanced Text Generation Application

Build a polished text generator with multiple modes and features.

```python exec
id: week-09-10-final-projects-7
class AdvancedTextGenerator:
    """
    Professional text generation system with multiple modes.
    """
    
    def __init__(self, order=2, name="Unnamed Model"):
        self.order = order
        self.name = name
        self.transitions = defaultdict(lambda: defaultdict(int))
        self.transition_probs = {}
        self.training_text = ""
        self.training_stats = {}
    
    def fit(self, text):
        """Learn from text corpus."""
        self.training_text = text
        words = text.split()
        
        # Calculate training statistics
        self.training_stats = {
            'total_words': len(words),
            'unique_words': len(set(words)),
            'avg_word_length': np.mean([len(w) for w in words]),
            'sentences': text.count('.') + text.count('!') + text.count('?')
        }
        
        # Learn transitions
        for i in range(len(words) - self.order):
            context = tuple(words[i:i+self.order])
            next_word = words[i+self.order]
            self.transitions[context][next_word] += 1
        
        # Convert to probabilities
        for context, next_words in self.transitions.items():
            total = sum(next_words.values())
            self.transition_probs[context] = {
                word: count/total 
                for word, count in next_words.items()
            }
        
        return self
    
    def generate(self, length=50, start=None, temperature=1.0, mode='standard'):
        """
        Generate text with various modes.
        
        temperature: Higher = more random, Lower = more conservative
        mode: 'standard', 'creative', 'conservative'
        """
        if mode == 'creative':
            temperature = 1.5
        elif mode == 'conservative':
            temperature = 0.5
        
        # Choose starting context
        if start:
            words = start.split()
            if len(words) >= self.order:
                context = tuple(words[-self.order:])
            else:
                context = random.choice(list(self.transition_probs.keys()))
        else:
            context = random.choice(list(self.transition_probs.keys()))
        
        result = list(context)
        
        for _ in range(length - len(context)):
            current_context = tuple(result[-self.order:])
            
            if current_context not in self.transition_probs:
                current_context = random.choice(list(self.transition_probs.keys()))
            
            probs = self.transition_probs[current_context]
            words = list(probs.keys())
            probabilities = np.array(list(probs.values()))
            
            # Apply temperature
            probabilities = probabilities ** (1/temperature)
            probabilities = probabilities / probabilities.sum()
            
            next_word = np.random.choice(words, p=probabilities)
            result.append(next_word)
        
        return ' '.join(result)
    
    def compare_modes(self, prompt, length=30):
        """Generate text in all modes for comparison."""
        modes = ['conservative', 'standard', 'creative']
        
        print(f"Text Generation Comparison")
        print(f"Model: {self.name} (Order {self.order})")
        print(f"Prompt: '{prompt}'")
        print("=" * 70)
        
        for mode in modes:
            text = self.generate(length=length, start=prompt, mode=mode)
            print(f"\n{mode.upper()}:")
            print(text)
    
    def stats(self):
        """Display model statistics."""
        print(f"Model: {self.name}")
        print("=" * 50)
        print(f"Order: {self.order}")
        print(f"Training words: {self.training_stats['total_words']}")
        print(f"Unique words: {self.training_stats['unique_words']}")
        print(f"Vocabulary richness: {self.training_stats['unique_words']/self.training_stats['total_words']:.2%}")
        print(f"Learned contexts: {len(self.transition_probs)}")
        print(f"Avg word length: {self.training_stats['avg_word_length']:.1f} chars")
```

### Train Multiple Style Models

```python exec
id: week-09-10-final-projects-8
# Different corpora
shakespeare = """
To be, or not to be, that is the question. Whether tis nobler in the mind to suffer 
the slings and arrows of outrageous fortune, or to take arms against a sea of troubles, 
and by opposing end them. To die, to sleep, no more, and by a sleep to say we end the 
heartache and the thousand natural shocks that flesh is heir to. Tis a consummation 
devoutly to be wished. To die, to sleep, to sleep, perchance to dream. Ay, there's the rub, 
for in that sleep of death what dreams may come when we have shuffled off this mortal coil.
"""

modern = """
The sun was setting over the city skyline as Sarah walked through the park. She thought 
about her day at work, the meetings that dragged on too long, the emails that never stopped. 
But here, in this moment, none of that mattered. The cool evening breeze felt good on her face. 
She smiled, remembering why she loved this city. Tomorrow would bring new challenges, but 
tonight was hers. She sat on a bench and watched the clouds turn orange and pink.
"""

scifi = """
The ship hummed through the void between stars. Captain Chen stared at the navigation display, 
calculating their jump coordinates. Three more hours until they reached the Kepler system. 
The mission was simple: deliver the quantum core to the research station and get out. But 
nothing in deep space was ever simple. She thought about the reports of pirate activity near 
the asteroid belt. Her hand moved to the weapons console. Better safe than sorry.
"""

# Train models
models = {}
for name, text in [('Shakespeare', shakespeare), ('Modern', modern), ('SciFi', scifi)]:
    model = AdvancedTextGenerator(order=2, name=name)
    model.fit(text)
    models[name] = model
    print(f"\nTrained {name} model:")
    model.stats()
```

```python exec
id: week-09-10-final-projects-9
# Generate with different styles
print("\n" + "=" * 70)
print("STYLE COMPARISON")
print("=" * 70)

for name, model in models.items():
    print(f"\n{name.upper()} STYLE:")
    print("-" * 70)
    text = model.generate(length=40, mode='standard')
    print(text)
```

```python exec
id: week-09-10-final-projects-10
# Compare modes with SciFi model
print("\n" + "=" * 70)
models['SciFi'].compare_modes("The ship", length=35)
```

---

## Project 3: Statistical Analysis & Evaluation

Let's rigorously analyze our models.

```python exec
id: week-09-10-final-projects-11
def comprehensive_analysis(model, test_text, n_generations=20):
    """
    Comprehensive model evaluation.
    """
    print(f"COMPREHENSIVE ANALYSIS: {model.name}")
    print("=" * 70)
    
    # Generate multiple samples
    samples = [model.generate(length=50) for _ in range(n_generations)]
    
    # 1. Length statistics
    lengths = [len(s.split()) for s in samples]
    print(f"\n1. GENERATION STATISTICS:")
    print(f"   Mean length: {np.mean(lengths):.1f} words")
    print(f"   Std length: {np.std(lengths):.1f} words")
    
    # 2. Vocabulary diversity
    all_words = ' '.join(samples).split()
    unique_ratio = len(set(all_words)) / len(all_words)
    print(f"\n2. VOCABULARY:")
    print(f"   Total words generated: {len(all_words)}")
    print(f"   Unique words: {len(set(all_words))}")
    print(f"   Vocabulary richness: {unique_ratio:.2%}")
    print(f"   Training vocabulary richness: {model.training_stats['unique_words']/model.training_stats['total_words']:.2%}")
    
    # 3. Most common words
    word_counts = Counter(all_words)
    print(f"\n3. MOST COMMON GENERATED WORDS:")
    for word, count in word_counts.most_common(5):
        print(f"   '{word}': {count} times ({count/len(all_words):.1%})")
    
    # 4. Repetition analysis
    repetitions = 0
    for sample in samples:
        words = sample.split()
        for i in range(len(words) - 1):
            if words[i] == words[i+1]:
                repetitions += 1
    
    print(f"\n4. REPETITION:")
    print(f"   Consecutive word repetitions: {repetitions}")
    print(f"   Repetition rate: {repetitions/len(all_words):.2%}")
    
    # 5. Perplexity on test text
    if test_text:
        perplexity = calculate_perplexity_advanced(model, test_text)
        print(f"\n5. PERPLEXITY ON TEST TEXT:")
        print(f"   Perplexity: {perplexity:.2f}")
        print(f"   (Lower is better)")

def calculate_perplexity_advanced(model, text):
    """Calculate perplexity."""
    words = text.split()
    log_prob_sum = 0
    count = 0
    
    for i in range(len(words) - model.order):
        context = tuple(words[i:i+model.order])
        next_word = words[i+model.order]
        
        if context in model.transition_probs:
            if next_word in model.transition_probs[context]:
                prob = model.transition_probs[context][next_word]
                log_prob_sum += np.log2(prob)
                count += 1
    
    if count == 0:
        return float('inf')
    
    return 2 ** (-log_prob_sum / count)

# Run comprehensive analysis on each model
for name, model in models.items():
    print("\n" + "="*70)
    comprehensive_analysis(model, modern if name != 'Modern' else shakespeare, n_generations=50)
    print()
```

---

## Project 4: Creative Application (Choose Your Own)

Build one of these (or design your own!):

### Option A: Stock Market Simulator

```python exec
id: week-09-10-final-projects-12
# Stock market simulation framework
# Students: Complete this!

class StockMarketSimulator:
    """
    Simulate stock market with Markov chains.
    """
    def __init__(self):
        self.states = ['Bull', 'Neutral', 'Bear']  # Market states
        # TODO: Add your implementation
        pass
    
    def simulate_portfolio(self, initial_value, days):
        """Simulate portfolio over time."""
        # TODO: Implement portfolio simulation
        pass
```

### Option B: Game AI

```python exec
id: week-09-10-final-projects-13
# Simple game AI framework
# Students: Complete this!

class GameAI:
    """
    Learn player behavior and predict moves.
    """
    def __init__(self):
        # Game states: 'Attack', 'Defend', 'Heal', 'Special'
        # TODO: Add your implementation
        pass
    
    def predict_next_move(self, history):
        """Predict opponent's next move."""
        # TODO: Implement prediction
        pass
```

### Option C: Music Generator

```python exec
id: week-09-10-final-projects-14
# Music sequence generator
# Students: Complete this!

class MusicGenerator:
    """
    Generate musical note sequences.
    """
    def __init__(self):
        # Notes: C, D, E, F, G, A, B (and sharps/flats)
        # TODO: Add your implementation
        pass
    
    def generate_melody(self, length):
        """Generate a melodic sequence."""
        # TODO: Implement melody generation
        pass
```

---

## Final Reflection & Presentation

### What You've Accomplished

Take a moment to reflect on your journey:

**Mathematical Concepts:**
- Probability theory and conditional probability
- Matrix operations and linear algebra
- Stochastic processes
- Convergence and steady states
- Statistical analysis

**Programming Skills:**
- Python fundamentals (variables, loops, functions)
- Object-oriented programming
- NumPy for numerical computing
- Matplotlib for visualization  
- Data structures and algorithms

**Applications Built:**
- Random walk simulators
- Weather forecasting systems
- Text generators
- Statistical analysis tools
- Custom creative projects

### Presenting Your Work

Prepare a 5-minute presentation covering:
1. **Problem**: What were you trying to solve?
2. **Approach**: How did Markov chains help?
3. **Implementation**: Show your code and explain key decisions
4. **Results**: Demo your working system
5. **Analysis**: What worked well? What didn't?
6. **Extensions**: What would you do with more time?

### Beyond This Course

You now understand the foundations of:
- Machine learning (sequential prediction)
- Natural language processing
- Time series forecasting
- Probabilistic modeling

**Next steps:**
- Learn about Hidden Markov Models (HMMs)
- Explore Recurrent Neural Networks (RNNs)
- Study Transformer models (GPT, BERT)
- Dive into reinforcement learning
- Build larger-scale applications

**Resources:**
- "Pattern Recognition and Machine Learning" by Christopher Bishop
- Stanford CS229 (Machine Learning)
- Fast.ai courses
- Kaggle competitions

---

## Assessment Rubric

### Project Quality (40%)
- Code is well-organized and documented 
- Implements required features correctly 
- Shows creativity and initiative 
- Works without errors 

### Technical Understanding (30%)
- Explains Markov property clearly 
- Understands matrix operations 
- Can discuss steady states 
- Analyzes results statistically 

### Application & Analysis (20%)
- Chooses appropriate model order 
- Evaluates model performance 
- Compares different approaches 
- Interprets results correctly 

### Presentation (10%)
- Clear and organized 
- Demonstrates working code 
- Explains decisions and trade-offs 
- Answers questions thoughtfully 

---

You've completed the course! You started knowing basic programming and ended building sophisticated probabilistic models that can:
- Predict future events
- Generate creative content
- Simulate complex systems
- Analyze patterns in data

More importantly, you've developed a way of thinking:
- Breaking complex problems into pieces
- Modeling uncertainty mathematically 
- Learning from data
- Evaluating and iterating

These skills will serve you well in whatever you do next.

**Keep building. Keep learning. Keep exploring.**

---

*"The best way to predict the future is to invent it."* - Alan Kay

*You now have the tools to do both: predict and invent.*

## Looking back

Before leaving this page, a sentence on each. What you write stays on this device.

```reflect
- Something you expected before running a cell that turned out differently
- The one idea from this page you could explain to someone else now
- Something you would change or try next, if there were time
- A question this page raised for you that it did not answer. Bring it to the next session; these questions are where the next session starts.
```
