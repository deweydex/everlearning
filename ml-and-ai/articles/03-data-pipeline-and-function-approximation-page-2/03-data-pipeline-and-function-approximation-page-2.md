---
title: "03-data-pipeline-and-function-approximation-page-2 (2 of 2)"
slug: 03-data-pipeline-and-function-approximation-page-2
course: ai-and-ml-foundations
course_title: "AI and ML Foundations"
series: 5-neural-networks
series_title: "Neural Networks"
version: 2026.09.06.1
---

Before starting this page, run the cell below. It repeats the imports and definitions from the earlier pages that this page uses.

```python exec
id: 03-data-pipeline-and-function-approximation-page-2-setup
import numpy as np
import matplotlib.pyplot as plt
from IPython.display import display, clear_output, Latex, HTML
import ipywidgets as widgets
from typing import Callable, Tuple, List, Dict, Optional
import copy

import numpy as np
import matplotlib.pyplot as plt
from IPython.display import display, clear_output, Latex, HTML
import ipywidgets as widgets
from typing import Callable, Tuple, List, Dict, Optional
import copy

# Set up plotting style
try:
    plt.style.use('seaborn-v0_8-whitegrid')
except:
    try:
        plt.style.use('seaborn-whitegrid')
    except:
        pass  # Use default if seaborn styles unavailable

plt.rcParams['figure.figsize'] = (10, 4)
plt.rcParams['font.size'] = 11

# For reproducibility
np.random.seed(42)

# Check if we are in Colab and enable widgets if needed
try:
    import google.colab
    from google.colab import output
    output.enable_custom_widget_manager()
    print("Running in Google Colab - widgets enabled.")
except ImportError:
    pass

print("Environment ready.")

def generate_linear_data(num_samples: int = 50,
                         input_range: Tuple[float, float] = (-2.0, 4.0),
                         slope: float = 2.0,
                         intercept: float = 1.0,
                         noise_level: float = 0.0) -> Tuple[np.ndarray, np.ndarray]:
    """
    Generate training data from a linear function: y = slope * x + intercept

    Parameters
    ----------
    num_samples : int
        Number of training examples to generate
    input_range : tuple
        The (min, max) range for input values
    slope : float
        The slope of the line
    intercept : float
        The y-intercept of the line
    noise_level : float
        Standard deviation of Gaussian noise to add (0 for clean data)

    Returns
    -------
    inputs : ndarray of shape (num_samples, 1)
        The input values as a column matrix
    targets : ndarray of shape (num_samples, 1)
        The target output values as a column matrix
    """
    inputs = np.linspace(input_range[0], input_range[1], num_samples).reshape(-1, 1)
    targets = slope * inputs + intercept

    if noise_level > 0:
        targets = targets + np.random.normal(0, noise_level, targets.shape)

    return inputs, targets


def generate_quadratic_data(num_samples: int = 50,
                            input_range: Tuple[float, float] = (-1.0, 5.0),
                            vertex_x: float = 2.0,
                            vertex_y: float = 1.0,
                            noise_level: float = 0.0) -> Tuple[np.ndarray, np.ndarray]:
    """
    Generate training data from a quadratic: y = (x - vertex_x)^2 + vertex_y

    Parameters
    ----------
    num_samples : int
        Number of training examples to generate
    input_range : tuple
        The (min, max) range for input values
    vertex_x : float
        The x-coordinate of the vertex
    vertex_y : float
        The y-coordinate of the vertex
    noise_level : float
        Standard deviation of Gaussian noise to add

    Returns
    -------
    inputs : ndarray of shape (num_samples, 1)
        The input values as a column matrix
    targets : ndarray of shape (num_samples, 1)
        The target output values as a column matrix
    """
    inputs = np.linspace(input_range[0], input_range[1], num_samples).reshape(-1, 1)
    targets = (inputs - vertex_x)**2 + vertex_y

    if noise_level > 0:
        targets = targets + np.random.normal(0, noise_level, targets.shape)

    return inputs, targets

# Generate both datasets
linear_inputs, linear_targets = generate_linear_data(num_samples=50)
quadratic_inputs, quadratic_targets = generate_quadratic_data(num_samples=50)

print("Linear data:")
print(f"  Input shape: {linear_inputs.shape}")
print(f"  Target shape: {linear_targets.shape}")
print(f"  Target function: y = 2x + 1")

print("\nQuadratic data:")
print(f"  Input shape: {quadratic_inputs.shape}")
print(f"  Target shape: {quadratic_targets.shape}")
print(f"  Target function: y = (x-2)² + 1")

# Visualize both target functions
fig, axes = plt.subplots(1, 2, figsize=(12, 4))

# Linear
axes[0].scatter(linear_inputs, linear_targets, c='blue', s=30, alpha=0.6, label='Training data')
axes[0].set_xlabel('Input')
axes[0].set_ylabel('Output')
axes[0].set_title('Linear Target: $y = 2x + 1$')
axes[0].legend()

# Quadratic
axes[1].scatter(quadratic_inputs, quadratic_targets, c='red', s=30, alpha=0.6, label='Training data')
axes[1].scatter([2], [1], c='green', s=100, marker='*', label='Vertex (2, 1)', zorder=10)
axes[1].set_xlabel('Input')
axes[1].set_ylabel('Output')
axes[1].set_title('Quadratic Target: $y = (x-2)^2 + 1$')
axes[1].legend()

plt.tight_layout()
plt.show()

def activation_linear(pre_activation: np.ndarray) -> np.ndarray:
    """
    Linear activation function: f(x) = x

    This simply passes values through unchanged.
    """
    return pre_activation


def activation_linear_derivative(pre_activation: np.ndarray) -> np.ndarray:
    """
    Derivative of linear activation: f'(x) = 1

    The slope of y = x is always 1.
    """
    return np.ones_like(pre_activation)


def activation_relu(pre_activation: np.ndarray) -> np.ndarray:
    """
    ReLU activation function: f(x) = max(0, x)

    Keeps positive values, sets negative values to zero.
    This introduces nonlinearity into the network.
    """
    return np.maximum(0, pre_activation)


def activation_relu_derivative(pre_activation: np.ndarray) -> np.ndarray:
    """
    Derivative of ReLU: f'(x) = 1 if x > 0, else 0

    The slope is 1 for positive inputs, 0 for negative inputs.
    """
    return (pre_activation > 0).astype(float)

def initialize_network(num_hidden: int = 1,
                       random_seed: Optional[int] = None) -> Tuple[List[np.ndarray], List[np.ndarray]]:
    """
    Initialize a neural network with one hidden layer.

    Architecture: Input (1) -> Hidden (num_hidden) -> Output (1)

    Parameters
    ----------
    num_hidden : int
        Number of neurons in the hidden layer
    random_seed : int, optional
        Seed for reproducibility

    Returns
    -------
    weights : list of ndarray
        weights[0] has shape (1, num_hidden)
        weights[1] has shape (num_hidden, 1)
    biases : list of ndarray
        biases[0] has shape (1, num_hidden)
        biases[1] has shape (1, 1)
    """
    if random_seed is not None:
        np.random.seed(random_seed)

    # Layer 0: Input -> Hidden
    weight_input_to_hidden = np.random.randn(1, num_hidden) * 0.5
    bias_hidden = np.random.randn(1, num_hidden) * 0.5

    # Layer 1: Hidden -> Output
    weight_hidden_to_output = np.random.randn(num_hidden, 1) * 0.5
    bias_output = np.random.randn(1, 1) * 0.5

    weights = [weight_input_to_hidden, weight_hidden_to_output]
    biases = [bias_hidden, bias_output]

    return weights, biases


# Test it
test_weights, test_biases = initialize_network(num_hidden=3, random_seed=42)
print("Network with 3 hidden neurons:")
print(f"  weights[0] (input->hidden): shape {test_weights[0].shape}")
print(f"  biases[0] (hidden):         shape {test_biases[0].shape}")
print(f"  weights[1] (hidden->output): shape {test_weights[1].shape}")
print(f"  biases[1] (output):         shape {test_biases[1].shape}")

def forward_pass(inputs: np.ndarray,
                 weights: List[np.ndarray],
                 biases: List[np.ndarray],
                 activation_name: str = 'linear') -> Tuple[np.ndarray, List[np.ndarray], List[np.ndarray]]:
    """
    Perform the forward pass through the network.

    Parameters
    ----------
    inputs : ndarray of shape (num_samples, 1)
        The input data
    weights : list of ndarray
        The network weights
    biases : list of ndarray
        The network biases
    activation_name : str
        Which activation function to use: 'linear' or 'relu'

    Returns
    -------
    predicted_output : ndarray of shape (num_samples, 1)
        The network's predictions
    pre_activations : list of ndarray
        The values before activation at each layer (needed for backprop)
    activations : list of ndarray
        The values after activation at each layer (needed for backprop)
    """
    # Select activation function
    if activation_name == 'linear':
        activation_fn = activation_linear
    elif activation_name == 'relu':
        activation_fn = activation_relu
    else:
        raise ValueError(f"Unknown activation: {activation_name}")

    # Store intermediate values
    pre_activations = []
    activations = [inputs]  # The input is the "activation" of layer -1

    current_activation = inputs

    # Process each layer
    for layer_index in range(len(weights)):
        # Linear transformation: multiply by weights, add bias
        pre_activation = current_activation @ weights[layer_index] + biases[layer_index]
        pre_activations.append(pre_activation)

        # Apply activation function (but not on the output layer)
        if layer_index < len(weights) - 1:
            current_activation = activation_fn(pre_activation)
        else:
            # Output layer: no activation (linear output)
            current_activation = pre_activation

        activations.append(current_activation)

    predicted_output = current_activation
    return predicted_output, pre_activations, activations

# Test forward pass
test_inputs = np.array([[-1.0], [-2.0], [3.0]])  # 3 samples
test_weights, test_biases = initialize_network(num_hidden=2, random_seed=42)

predicted, pre_acts, acts = forward_pass(test_inputs, test_weights, test_biases, 'relu')

print("Forward pass test with 3 samples, 2 hidden neurons:")
print(f"  Input shape:           {test_inputs.shape}")
print(f"  pre_activations[0]:    {pre_acts[0].shape} (hidden layer pre-activation)")
print(f"  activations[1]:        {acts[1].shape} (hidden layer output)")
print(f"  pre_activations[1]:    {pre_acts[1].shape} (output layer pre-activation)")
print(f"  Predicted output:      {predicted.shape}")
print(f"\nPredictions: {predicted.ravel()}")

def compute_loss(predicted: np.ndarray, targets: np.ndarray) -> float:
    """
    Compute the mean squared error loss.

    Parameters
    ----------
    predicted : ndarray
        The network's predictions
    targets : ndarray
        The true target values

    Returns
    -------
    loss : float
        The mean squared error
    """
    prediction_errors = predicted - targets
    squared_errors = prediction_errors ** 2
    mean_squared_error = np.mean(squared_errors)
    return float(mean_squared_error)

def backward_pass(targets: np.ndarray,
                  weights: List[np.ndarray],
                  pre_activations: List[np.ndarray],
                  activations: List[np.ndarray],
                  activation_name: str = 'linear') -> Tuple[List[np.ndarray], List[np.ndarray]]:
    """
    Perform backpropagation to compute gradients.

    Parameters
    ----------
    targets : ndarray of shape (num_samples, 1)
        The true target values
    weights : list of ndarray
        The network weights
    pre_activations : list of ndarray
        Pre-activation values from forward pass
    activations : list of ndarray
        Activation values from forward pass
    activation_name : str
        Which activation function was used

    Returns
    -------
    weight_gradients : list of ndarray
        Gradient of loss with respect to each weight matrix
    bias_gradients : list of ndarray
        Gradient of loss with respect to each bias vector
    """
    # Select activation derivative
    if activation_name == 'linear':
        activation_deriv_fn = activation_linear_derivative
    elif activation_name == 'relu':
        activation_deriv_fn = activation_relu_derivative
    else:
        raise ValueError(f"Unknown activation: {activation_name}")

    num_samples = targets.shape[0]
    num_layers = len(weights)

    # Initialize gradient storage
    weight_gradients = [None] * num_layers
    bias_gradients = [None] * num_layers

    # Start with gradient of loss with respect to output
    # For MSE: d(loss)/d(predicted) = 2 * (predicted - target) / num_samples
    predicted = activations[-1]
    gradient_from_loss = 2 * (predicted - targets) / num_samples

    # Work backwards through layers
    for layer_index in range(num_layers - 1, -1, -1):
        # Gradient with respect to pre-activation
        if layer_index == num_layers - 1:
            # Output layer has no activation function
            gradient_pre_activation = gradient_from_loss
        else:
            # Hidden layer: multiply by activation derivative
            activation_derivative = activation_deriv_fn(pre_activations[layer_index])
            gradient_pre_activation = gradient_from_loss * activation_derivative

        # Gradient with respect to weights
        # pre_activation = input @ weights + bias
        # So d(pre_activation)/d(weights) = input.T
        layer_input = activations[layer_index]  # Input to this layer
        weight_gradients[layer_index] = layer_input.T @ gradient_pre_activation

        # Gradient with respect to bias
        # d(pre_activation)/d(bias) = 1, summed over samples
        bias_gradients[layer_index] = np.sum(gradient_pre_activation, axis=0, keepdims=True)

        # Propagate gradient to previous layer
        if layer_index > 0:
            gradient_from_loss = gradient_pre_activation @ weights[layer_index].T

    return weight_gradients, bias_gradients

def update_weights(weights: List[np.ndarray],
                   biases: List[np.ndarray],
                   weight_gradients: List[np.ndarray],
                   bias_gradients: List[np.ndarray],
                   learning_rate: float) -> Tuple[List[np.ndarray], List[np.ndarray]]:
    """
    Update weights using gradient descent.

    Parameters
    ----------
    weights : list of ndarray
        Current weights
    biases : list of ndarray
        Current biases
    weight_gradients : list of ndarray
        Gradients for weights
    bias_gradients : list of ndarray
        Gradients for biases
    learning_rate : float
        Step size for gradient descent

    Returns
    -------
    new_weights : list of ndarray
        Updated weights
    new_biases : list of ndarray
        Updated biases
    """
    new_weights = []
    new_biases = []

    for layer_index in range(len(weights)):
        new_weight = weights[layer_index] - learning_rate * weight_gradients[layer_index]
        new_bias = biases[layer_index] - learning_rate * bias_gradients[layer_index]
        new_weights.append(new_weight)
        new_biases.append(new_bias)

    return new_weights, new_biases

def training_step(inputs: np.ndarray,
                  targets: np.ndarray,
                  weights: List[np.ndarray],
                  biases: List[np.ndarray],
                  learning_rate: float,
                  activation_name: str = 'linear') -> Tuple[List[np.ndarray], List[np.ndarray], float, Dict]:
    """
    Perform one complete training step.

    Returns updated weights, biases, the loss, and diagnostic info.
    """
    # Forward pass
    predicted, pre_activations, activations = forward_pass(
        inputs, weights, biases, activation_name
    )

    # Compute loss
    loss = compute_loss(predicted, targets)

    # Backward pass
    weight_gradients, bias_gradients = backward_pass(
        targets, weights, pre_activations, activations, activation_name
    )

    # Update weights
    new_weights, new_biases = update_weights(
        weights, biases, weight_gradients, bias_gradients, learning_rate
    )

    # Store diagnostic info
    diagnostics = {
        'predicted': predicted,
        'weight_gradients': weight_gradients,
        'bias_gradients': bias_gradients
    }

    return new_weights, new_biases, loss, diagnostics
```

## Part 5: Learning a Line

Before we try the quadratic, let us see if our network can learn a simple linear function: $y = 2x + 1$.

**Prediction moment**: Do you think a network with one hidden neuron and a linear activation function can learn this line? What about with ReLU activation?

```python exec
id: 03-data-pipeline-and-function-approximation-page-2-1
class NetworkTrainer:
    """
    A class to manage network training with history tracking.

    This stores the complete history so we can step forward and backward.
    """

    def __init__(self,
                 inputs: np.ndarray,
                 targets: np.ndarray,
                 num_hidden: int = 1,
                 activation_name: str = 'linear',
                 learning_rate: float = 0.01,
                 random_seed: int = 42):
        """
        Initialize the trainer.
        """
        self.inputs = inputs
        self.targets = targets
        self.num_hidden = num_hidden
        self.activation_name = activation_name
        self.learning_rate = learning_rate
        self.random_seed = random_seed

        # Initialize network
        initial_weights, initial_biases = initialize_network(num_hidden, random_seed)

        # Compute initial loss
        predicted, _, _ = forward_pass(inputs, initial_weights, initial_biases, activation_name)
        initial_loss = compute_loss(predicted, targets)

        # Store history
        self.history = [{
            'weights': copy.deepcopy(initial_weights),
            'biases': copy.deepcopy(initial_biases),
            'loss': initial_loss
        }]

        self.current_step = 0

    def step_forward(self) -> None:
        """Perform one gradient descent step."""
        # If we have future history, just move to it
        if self.current_step < len(self.history) - 1:
            self.current_step += 1
            return

        # Otherwise, compute a new step
        current_state = self.history[self.current_step]
        new_weights, new_biases, loss, _ = training_step(
            self.inputs,
            self.targets,
            current_state['weights'],
            current_state['biases'],
            self.learning_rate,
            self.activation_name
        )

        self.history.append({
            'weights': copy.deepcopy(new_weights),
            'biases': copy.deepcopy(new_biases),
            'loss': loss
        })
        self.current_step += 1

    def step_backward(self) -> None:
        """Go back one step in history."""
        if self.current_step > 0:
            self.current_step -= 1

    def reset(self) -> None:
        """Reset to initial state."""
        self.current_step = 0

    def get_current_state(self) -> Dict:
        """Get current weights, biases, and loss."""
        return self.history[self.current_step]

    def get_predictions(self, x_values: np.ndarray) -> np.ndarray:
        """Get predictions for given x values using current weights."""
        state = self.get_current_state()
        predicted, _, _ = forward_pass(
            x_values, state['weights'], state['biases'], self.activation_name
        )
        return predicted
```

```python exec
id: 03-data-pipeline-and-function-approximation-page-2-2
def create_interactive_trainer(trainer: NetworkTrainer,
                               title: str,
                               target_fn: Callable,
                               x_range: Tuple[float, float] = (-2, 4),
                               y_range: Tuple[float, float] = (-3, 10)) -> None:
    """
    Create an interactive widget for stepping through training.
    """
    # Create output widget
    output = widgets.Output()

    # Create fine grid for plotting
    plot_x = np.linspace(x_range[0], x_range[1], 200).reshape(-1, 1)
    target_y = target_fn(plot_x)

    def update_display():
        """Update the visualization."""
        with output:
            clear_output(wait=True)

            state = trainer.get_current_state()
            predicted_y = trainer.get_predictions(plot_x)

            fig, axes = plt.subplots(1, 2, figsize=(14, 5))

            # Plot 1: Function fit
            ax1 = axes[0]
            ax1.plot(plot_x, target_y, 'b-', linewidth=2, label='Target function', alpha=0.7)
            ax1.plot(plot_x, predicted_y, 'r-', linewidth=2, label='Network prediction')
            ax1.scatter(trainer.inputs, trainer.targets, c='blue', s=20, alpha=0.4)
            ax1.set_xlabel('Input')
            ax1.set_ylabel('Output')
            ax1.set_title(f'{title}\nStep {trainer.current_step} | Loss: {state["loss"]:.6f}')
            ax1.legend(loc='upper left')
            ax1.set_xlim(x_range)
            ax1.set_ylim(y_range)

            # Plot 2: Loss history
            ax2 = axes[1]
            losses = [h['loss'] for h in trainer.history[:trainer.current_step + 1]]
            ax2.plot(losses, 'g-', linewidth=2)
            ax2.scatter([trainer.current_step], [state['loss']], c='red', s=100, zorder=5)
            ax2.set_xlabel('Step')
            ax2.set_ylabel('Loss (MSE)')
            ax2.set_title('Training Progress')
            #if len(losses) > 1 and max(losses) > min(losses) * 10:
             #   ax2.set_yscale('log')

            plt.tight_layout()
            plt.show()

            # Show current weights
            print(f"\nCurrent weights (Step {trainer.current_step}):")
            print(f"  weights[0] (input->hidden): {state['weights'][0].ravel()}")
            print(f"  biases[0] (hidden):         {state['biases'][0].ravel()}")
            print(f"  weights[1] (hidden->output): {state['weights'][1].ravel()}")
            print(f"  biases[1] (output):         {state['biases'][1].ravel()}")

    def on_forward(b):
        trainer.step_forward()
        update_display()

    def on_backward(b):
        trainer.step_backward()
        update_display()

    def on_forward_10(b):
        for _ in range(10):
            trainer.step_forward()
        update_display()

    def on_forward_100(b):
        for _ in range(100):
            trainer.step_forward()
        update_display()

    def on_reset(b):
        trainer.reset()
        update_display()

    # Create buttons
    back_btn = widgets.Button(description='< Back', button_style='warning')
    forward_btn = widgets.Button(description='Forward >', button_style='success')
    forward_10_btn = widgets.Button(description='+10 Steps', button_style='info')
    forward_100_btn = widgets.Button(description='+100 Steps', button_style='info')
    reset_btn = widgets.Button(description='Reset', button_style='danger')

    # Connect callbacks
    back_btn.on_click(on_backward)
    forward_btn.on_click(on_forward)
    forward_10_btn.on_click(on_forward_10)
    forward_100_btn.on_click(on_forward_100)
    reset_btn.on_click(on_reset)

    # Layout
    button_box = widgets.HBox([back_btn, forward_btn, forward_10_btn, forward_100_btn, reset_btn])
    display(widgets.VBox([button_box, output]))

    # Initial display
    update_display()
```

### Training on the Linear Target

Let us train a network with **one hidden neuron** and **linear activation** on our linear data. The target is $y = 2x + 1$.

Use the buttons to step through training and watch the network learn!

```python exec
id: 03-data-pipeline-and-function-approximation-page-2-3
# Create trainer for linear data with linear activation
linear_trainer = NetworkTrainer(
    inputs=linear_inputs,
    targets=linear_targets,
    num_hidden=1,
    activation_name='linear',
    learning_rate=0.01,
    random_seed=42
)

# Target function for plotting
def linear_target(x):
    return 2 * x + 1

print("Training a LINEAR network on LINEAR data (y = 2x + 1)")
print("="*60)
create_interactive_trainer(
    linear_trainer,
    title='Linear Activation Learning y = 2x + 1',
    target_fn=linear_target,
    x_range=(-2.5, 4.5),
    y_range=(-5, 12)
)
```

### Observation

The linear network successfully learns the line! Click "+100 Steps" a few times and watch the loss decrease toward zero.

This makes sense: a line is a linear function, and our network (even with just one hidden neuron) can represent linear functions.

Now let us try with ReLU activation on the same data:

```python exec
id: 03-data-pipeline-and-function-approximation-page-2-4
# Create trainer for linear data with ReLU activation
relu_linear_trainer = NetworkTrainer(
    inputs=linear_inputs,
    targets=linear_targets,
    num_hidden=1,
    activation_name='relu',
    learning_rate=0.01,
    random_seed=42
)

print("Training a ReLU network on LINEAR data (y = 2x + 1)")
print("="*60)
create_interactive_trainer(
    relu_linear_trainer,
    title='ReLU Activation Learning y = 2x + 1',
    target_fn=linear_target,
    x_range=(-2.5, 4.5),
    y_range=(-5, 12)
)
```

### Observation

ReLU can also learn a line (approximately), though it might show a "kink" depending on where the hidden neuron's threshold lands. With one hidden neuron, ReLU creates a piecewise linear function with at most one bend.

**Key insight**: Both linear and ReLU networks can learn linear functions. The difference will become apparent when we try to learn something nonlinear.

## Part 6: The Wall - Trying to Learn a Quadratic

Now let us try something more ambitious: learning the quadratic function $y = (x-2)^2 + 1$.

**Prediction moment**: Before running the cells below, consider:
1. Do you think the linear activation network can learn this curve?
2. Do you think the ReLU activation network (with one hidden neuron) can learn it?
3. Why or why not?

```python exec
id: 03-data-pipeline-and-function-approximation-page-2-5
# Target function for plotting
def quadratic_target(x):
    return (x - 2)**2 + 1

# Create trainer for quadratic data with LINEAR activation
linear_quad_trainer = NetworkTrainer(
    inputs=quadratic_inputs,
    targets=quadratic_targets,
    num_hidden=1,
    activation_name='linear',
    learning_rate=0.01,
    random_seed=42
)

print("Training a LINEAR network on QUADRATIC data")
print("Target: y = (x-2)² + 1")
print("="*60)
create_interactive_trainer(
    linear_quad_trainer,
    title='Linear Activation Trying to Learn y = (x-2)² + 1',
    target_fn=quadratic_target,
    x_range=(-1.5, 5.5),
    y_range=(-1, 12)
)
```

### What Happened?

Click "+100 Steps" several times. Watch the loss carefully.

The linear network finds the best **straight line** it can, but then **stops improving**. The loss reaches a floor and stays there. No matter how many more steps you take, it cannot do better.

This is not a bug—it is a fundamental limitation. Let us try ReLU:

```python exec
id: 03-data-pipeline-and-function-approximation-page-2-6
# Create trainer for quadratic data with ReLU activation
relu_quad_trainer = NetworkTrainer(
    inputs=quadratic_inputs,
    targets=quadratic_targets,
    num_hidden=1,
    activation_name='relu',
    learning_rate=0.01,
    random_seed=42
)

print("Training a ReLU network (1 hidden neuron) on QUADRATIC data")
print("Target: y = (x-2)² + 1")
print("="*60)
create_interactive_trainer(
    relu_quad_trainer,
    title='ReLU (1 neuron) Trying to Learn y = (x-2)² + 1',
    target_fn=quadratic_target,
    x_range=(-1.5, 5.5),
    y_range=(-1, 12)
)
```

### Observation

ReLU with one hidden neuron does somewhat better—it can create one "kink" in its output. But it still cannot capture the smooth curve of the parabola. The loss decreases but then plateaus.

**The pattern**: Both networks hit a wall. The linear network can only draw straight lines. The ReLU network (with one neuron) can only draw lines with one bend.

## Part 7: Why the Linear Network Fails

Let us understand mathematically why the linear network cannot learn a quadratic.

Consider what the network computes. With one hidden neuron:

$$\text{hidden} = w_1 \times \text{input} + b_1$$

$$\text{output} = w_2 \times \text{hidden} + b_2$$

Substituting:

$$\text{output} = w_2 \times (w_1 \times \text{input} + b_1) + b_2$$

Expanding:

$$\text{output} = (w_2 \times w_1) \times \text{input} + (w_2 \times b_1 + b_2)$$

This is just:

$$\text{output} = m \times \text{input} + c$$

where $m = w_2 \times w_1$ and $c = w_2 \times b_1 + b_2$.

**The composition of linear functions is linear.** No matter what values our weights take, the network can only output a linear function of the input.

```python exec
id: 03-data-pipeline-and-function-approximation-page-2-7
# Verify this algebraically with the trained network
state = linear_quad_trainer.history[-1]  # Get final state
w1 = state['weights'][0][0, 0]
b1 = state['biases'][0][0, 0]
w2 = state['weights'][1][0, 0]
b2 = state['biases'][1][0, 0]

effective_slope = w2 * w1
effective_intercept = w2 * b1 + b2

print("The linear network's learned parameters:")
print(f"  w1 = {w1:.4f}, b1 = {b1:.4f}")
print(f"  w2 = {w2:.4f}, b2 = {b2:.4f}")
print()
print("This collapses to a single linear function:")
print(f"  y = {effective_slope:.4f} * x + {effective_intercept:.4f}")
print()
print("No matter what values w1, w2, b1, b2 take,")
print("the network can only represent: y = mx + c")
```

## Part 8: Breaking Through with More Neurons

What if we add more hidden neurons with ReLU activation?

Each ReLU neuron can create one "kink" in the output. With multiple neurons, we can have multiple kinks. Enough kinks can approximate a smooth curve!

Let us try with 8 hidden neurons:

```python exec
id: 03-data-pipeline-and-function-approximation-page-2-8
# Create trainer with MORE hidden neurons
multi_relu_trainer = NetworkTrainer(
    inputs=quadratic_inputs,
    targets=quadratic_targets,
    num_hidden=3,
    activation_name='relu',
    learning_rate=.07,
    random_seed=42
)

print("Training a ReLU network with 8 hidden neurons on QUADRATIC data")
print("Target: y = (x-2)² + 1")
print("="*60)
create_interactive_trainer(
    multi_relu_trainer,
    title='ReLU (2 neurons) Learning y = (x-2)² + 1',
    target_fn=quadratic_target,
    x_range=(-1.5, 5.5),
    y_range=(-1, 12)
)
```

### Success!

With 8 ReLU neurons, the network can learn the quadratic! Click "+100 Steps" several times and watch the red curve bend to fit the blue parabola.

The loss keeps decreasing, unlike the linear network where it plateaued.

**Key insight**: The architecture determines what functions the network *can* represent. Training finds the best function *within* that representable space.

## Part 9: Side-by-Side Comparison

Let us create a side-by-side view to really drive home the difference between linear and ReLU activation on the quadratic target.

```python exec
id: 03-data-pipeline-and-function-approximation-page-2-9
def create_comparison_widget(trainer_linear: NetworkTrainer,
                             trainer_relu: NetworkTrainer,
                             target_fn: Callable,
                             x_range: Tuple[float, float] = (-1.5, 5.5),
                             y_range: Tuple[float, float] = (-1, 12)) -> None:
    """
    Create a side-by-side comparison of two networks.
    """
    output = widgets.Output()
    plot_x = np.linspace(x_range[0], x_range[1], 200).reshape(-1, 1)
    target_y = target_fn(plot_x)

    def update_display():
        with output:
            clear_output(wait=True)

            state_linear = trainer_linear.get_current_state()
            state_relu = trainer_relu.get_current_state()

            pred_linear = trainer_linear.get_predictions(plot_x)
            pred_relu = trainer_relu.get_predictions(plot_x)

            fig, axes = plt.subplots(1, 2, figsize=(14, 5))

            # Linear network
            ax1 = axes[0]
            ax1.plot(plot_x, target_y, 'b-', linewidth=2, label='Target', alpha=0.7)
            ax1.plot(plot_x, pred_linear, 'r-', linewidth=2, label='Network')
            ax1.scatter(trainer_linear.inputs, trainer_linear.targets, c='blue', s=20, alpha=0.3)
            ax1.set_xlabel('Input')
            ax1.set_ylabel('Output')
            ax1.set_title(f'LINEAR Activation (1 neuron)\nStep {trainer_linear.current_step} | Loss: {state_linear["loss"]:.4f}')
            ax1.legend(loc='upper right')
            ax1.set_xlim(x_range)
            ax1.set_ylim(y_range)

            # ReLU network
            ax2 = axes[1]
            ax2.plot(plot_x, target_y, 'b-', linewidth=2, label='Target', alpha=0.7)
            ax2.plot(plot_x, pred_relu, 'r-', linewidth=2, label='Network')
            ax2.scatter(trainer_relu.inputs, trainer_relu.targets, c='blue', s=20, alpha=0.3)
            ax2.set_xlabel('Input')
            ax2.set_ylabel('Output')
            ax2.set_title(f'ReLU Activation (8 neurons)\nStep {trainer_relu.current_step} | Loss: {state_relu["loss"]:.4f}')
            ax2.legend(loc='upper right')
            ax2.set_xlim(x_range)
            ax2.set_ylim(y_range)

            plt.tight_layout()
            plt.show()

            print(f"Step: {trainer_linear.current_step}")
            print(f"Linear network loss: {state_linear['loss']:.6f}")
            print(f"ReLU network loss:   {state_relu['loss']:.6f}")

    def on_forward(b):
        trainer_linear.step_forward()
        trainer_relu.step_forward()
        update_display()

    def on_backward(b):
        trainer_linear.step_backward()
        trainer_relu.step_backward()
        update_display()

    def on_forward_10(b):
        for _ in range(10):
            trainer_linear.step_forward()
            trainer_relu.step_forward()
        update_display()

    def on_forward_100(b):
        for _ in range(100):
            trainer_linear.step_forward()
            trainer_relu.step_forward()
        update_display()

    def on_reset(b):
        trainer_linear.reset()
        trainer_relu.reset()
        update_display()

    # Buttons
    back_btn = widgets.Button(description='< Back', button_style='warning')
    forward_btn = widgets.Button(description='Forward >', button_style='success')
    forward_10_btn = widgets.Button(description='+10 Steps', button_style='info')
    forward_100_btn = widgets.Button(description='+100 Steps', button_style='info')
    reset_btn = widgets.Button(description='Reset', button_style='danger')

    back_btn.on_click(on_backward)
    forward_btn.on_click(on_forward)
    forward_10_btn.on_click(on_forward_10)
    forward_100_btn.on_click(on_forward_100)
    reset_btn.on_click(on_reset)

    button_box = widgets.HBox([back_btn, forward_btn, forward_10_btn, forward_100_btn, reset_btn])
    display(widgets.VBox([button_box, output]))
    update_display()
```

```python exec
id: 03-data-pipeline-and-function-approximation-page-2-10
# Create fresh trainers for comparison
compare_linear = NetworkTrainer(
    inputs=quadratic_inputs,
    targets=quadratic_targets,
    num_hidden=1,
    activation_name='linear',
    learning_rate=0.01,
    random_seed=123
)

compare_relu = NetworkTrainer(
    inputs=quadratic_inputs,
    targets=quadratic_targets,
    num_hidden=3,
    activation_name='relu',
    learning_rate=0.01,
    random_seed=123
)

print("SIDE-BY-SIDE COMPARISON: Learning y = (x-2)² + 1")
print("Left: Linear activation (1 neuron) | Right: ReLU activation (2 neurons)")
print("="*70)
create_comparison_widget(compare_linear, compare_relu, quadratic_target)
```

## Part 10: The Bigger Picture

Let us step back and reflect on what we have discovered.

### The Role of Each Component

| Component | Purpose | Why It Matters |
|-----------|---------|----------------|
| **Weights and biases** | Parameters that define the transformation | These are what we learn |
| **Activation function** | Introduces nonlinearity | Without it, we can only represent linear functions |
| **Loss function** | Measures how wrong we are | Gives us something to minimize |
| **Gradient** | Direction to improve | Tells us how to adjust each parameter |
| **Learning rate** | Step size | Controls how much we adjust per iteration |
| **Backpropagation** | Efficient gradient computation | The chain rule, applied systematically |

### The Key Insight

The network's architecture determines what functions it *can* represent. Training (gradient descent) finds the best function *within that space*. If the target function lies outside what the architecture can represent, no amount of training will help.

This is why:
- Linear networks can only learn linear functions
- One ReLU neuron can create one "kink"
- Multiple ReLU neurons can approximate smooth curves by combining many kinks

## YOUR TURN: Experiments to Try

1. **Change the learning rate**: In the trainers above, try values like 0.001, 0.1, and 0.5. What happens when it is too small? Too large?

2. **Change the number of hidden neurons**: Create a new NetworkTrainer with 2, 4, 16, or 32 neurons. How does the fit change?

3. **Try a different target function**: Modify the code to learn $y = \sin(x)$ or $y = x^3$. Can the network learn it?

4. **Add noise to the data**: Regenerate data with `noise_level=0.5`. How does this affect learning?

5. **Linear multi-neuron network**: Create a NetworkTrainer with `activation_name='linear'` and 8 neurons. Does having more neurons help? Why or why not?

```python exec
id: 03-data-pipeline-and-function-approximation-page-2-11
# Space for your experiments!

# Example: Try a different number of hidden neuron
my_trainer = NetworkTrainer(
    inputs=quadratic_inputs,
    targets=quadratic_targets,
    num_hidden=16,
    activation_name='relu',
    learning_rate=0.05,
    random_seed=42
 )
create_interactive_trainer(my_trainer, 'My Experiment', quadratic_target)
```

## Reflection Questions

Take a moment to write down your thoughts on these questions:

1. Why does the linear network find a "best line" even though we want a curve? What is it actually minimizing?

2. If you wanted to learn a cubic function ($x^3$), would you expect to need more or fewer hidden neurons than for a quadratic? Why?

3. The loss function we used (MSE) treats all errors equally. Can you think of a situation where you might want errors on some points to matter more than others?

4. What role does the learning rate play in the tradeoff between speed and stability? What happens with very large vs very small learning rates?

5. How does this connect to our earlier work with polynomials? In what sense is a neural network like—and unlike—fitting a polynomial to data?

## Summary

In this notebook, we:

1. Framed neural networks as **function approximators**
2. Built a network from scratch with **list-based weights** for flexibility
3. Saw the network **successfully learn a line**
4. Discovered that **linear networks can only represent linear functions**
5. Saw how **nonlinear activation functions (ReLU)** break through this limitation
6. Understood that the **architecture determines what can be learned**
7. Traced through the **chain rule** as the foundation of backpropagation

The key takeaway: neural networks are not magic. They are function approximators built from simple components—linear transformations, nonlinear activations, and gradient-based optimization. Understanding each piece demystifies the whole.

## Looking back

Before leaving this page, a sentence on each. What you write stays on this device.

```reflect
- Something you expected before running a cell that turned out differently
- The one idea from this page you could explain to someone else now
- Something you would change or try next, if there were time
- A question this page raised for you that it did not answer. Bring it to the next session; these questions are where the next session starts.
```
