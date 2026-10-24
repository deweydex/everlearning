---
title: "Neural Networks: From Data to Intelligence (Interactive Lab)"
slug: 06-interactive-lab-nist
course: ai-and-ml-foundations
course_title: "AI and ML Foundations"
series: 5-neural-networks
series_title: "Neural Networks"
version: 2026.09.06.1
---

# Neural Networks: From Data to Intelligence (Interactive Lab)

**Instructor:** Joshua Aaron  
**Level:** QQI Level 5

## Introduction

In this session, we build a neural network capable of reading handwritten letters. To ensure this is accessible to everyone without needing accounts or API keys, we will download the data directly from the official source: the US National Institute of Standards and Technology (NIST).

We will go beyond simply running code; we will interact with the data to clean it, watch the network's performance improve in real-time using graphs, and finally "open up the brain" to visualize what the network has actually learned.

## Part 1: Setting Up the Environment

We need `scipy` to handle the MATLAB file format, `requests` for downloading, and `ipywidgets` to create interactive buttons for our data lab.

```python exec
id: 06-interactive-lab-nist-1
# Install necessary libraries
# (nothing to install here: the libraries load with the page)
```

```python exec
id: 06-interactive-lab-nist-2
import requests
import zipfile
import scipy.io
import io
import os
import numpy as np 
import matplotlib.pyplot as plt
import ipywidgets as widgets
from IPython.display import display, clear_output
from random import seed
from random import random
from math import exp

# Set seed for reproducibility
seed(1)
```

## Part 2: Fetching the Data

The code below checks if you already have the file. If not, it downloads the zip file from `biometrics.nist.gov` and extracts the `emnist-letters.mat` file. We limit the dataset to 1,000 images to ensure our pure-Python training runs in a reasonable amount of time.

```python exec
id: 06-interactive-lab-nist-3
def download_and_load_nist(limit=1000):
    url = "https://biometrics.nist.gov/cs_links/EMNIST/matlab.zip"
    mat_filename = "matlab/emnist-letters.mat"
    
    # 1. Download logic
    if not os.path.exists("emnist-letters.mat"):
        print(f"Downloading EMNIST from {url}...")
        print("This is a large file (~500MB), please be patient...")
        r = requests.get(url)
        
        print("Extracting...")
        with zipfile.ZipFile(io.BytesIO(r.content)) as z:
            data = z.read(mat_filename)
            with open("emnist-letters.mat", "wb") as f:
                f.write(data)
    else:
        print("Found existing emnist-letters.mat file.")

    # 2. Loading Logic
    print("Loading MATLAB file...")
    mat = scipy.io.loadmat('emnist-letters.mat')
    data = mat['dataset']
    
    # Extract training images and labels
    train_images = data[0,0]['train'][0,0]['images']
    train_labels = data[0,0]['train'][0,0]['labels']
    
    dataset = []
    
    # 3. Initial Processing Loop
    # We load the data 'raw' here. We will fix orientation in the next step.
    for i in range(min(limit, len(train_images))):
        label = int(train_labels[i][0]) - 1 # Convert 1-26 to 0-25
        raw_pixels = train_images[i]
        
        # Store as 28x28 numpy array initially to make rotation easy
        grid = raw_pixels.reshape((28, 28), order='F') 
        dataset.append({'pixels': grid, 'label': label})
        
    return dataset

# Load the data
raw_dataset = download_and_load_nist(limit=1000)
print(f"Loaded {len(raw_dataset)} images.")
```

## Part 3: Interactive Data Lab

Data rarely arrives in a perfect state. The EMNIST dataset is known to be rotated or flipped compared to standard image tools. 

Use the buttons below to fix the orientation of the dataset. When the sample image looks like a proper letter "A", "B", or "C", you are ready to proceed.

```python exec
id: 06-interactive-lab-nist-4
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
label_map = {i: alphabet[i] for i in range(len(alphabet))}

# Create Output widget to display the image
out = widgets.Output()

def show_sample():
    with out:
        clear_output(wait=True)
        # Show the first 3 images to be sure
        fig, axes = plt.subplots(1, 3, figsize=(6, 2))
        for i in range(3):
            sample = raw_dataset[i]
            axes[i].imshow(sample['pixels'], cmap='gray_r')
            axes[i].set_title(f"Label: {label_map.get(sample['label'], '?')}")
            axes[i].axis('off')
        plt.show()

def rotate_dataset(b):
    for item in raw_dataset:
        item['pixels'] = np.rot90(item['pixels'])
    show_sample()

def flip_lr(b):
    for item in raw_dataset:
        item['pixels'] = np.fliplr(item['pixels'])
    show_sample()

def flip_ud(b):
    for item in raw_dataset:
        item['pixels'] = np.flipud(item['pixels'])
    show_sample()

# Create Buttons
btn_rot = widgets.Button(description="Rotate 90°")
btn_flip_lr = widgets.Button(description="Flip Horizontal")
btn_flip_ud = widgets.Button(description="Flip Vertical")

btn_rot.on_click(rotate_dataset)
btn_flip_lr.on_click(flip_lr)
btn_flip_ud.on_click(flip_ud)

# Display UI
display(widgets.HBox([btn_rot, btn_flip_lr, btn_flip_ud]))
display(out)
show_sample()
```

### Finalizing Data Preparation

Once the images look correct above, we need to flatten them. Our neural network takes a single list of 784 numbers (28x28), not a grid. The code below performs this conversion.

```python exec
id: 06-interactive-lab-nist-5
dataset = []
for item in raw_dataset:
    # Flatten 28x28 -> 784
    flat_pixels = item['pixels'].reshape(784).astype('float') / 255.0
    dataset.append([flat_pixels.tolist(), item['label']])

n_inputs = 784
n_outputs = 26
print("Data flattened and normalized. Ready for training.")
```

## Part 4: Building the Neural Network

We use the same pure-Python structure as before. 

* **Input:** 784 pixels.
* **Hidden:** 30 neurons. (Increased slightly to handle 26 letters).
* **Output:** 26 neurons (A-Z).

```python exec
id: 06-interactive-lab-nist-6
# --- NETWORK ARCHITECTURE ---
def initialize_network(n_inputs, n_hidden, n_outputs):
    network = list()
    hidden_layer = [{'weights': [random() for i in range(n_inputs + 1)]} for i in range(n_hidden)]
    network.append(hidden_layer)
    output_layer = [{'weights': [random() for i in range(n_hidden + 1)]} for i in range(n_outputs)]
    network.append(output_layer)
    return network

# --- MATH HELPERS ---
def activate(weights, inputs):
    activation = weights[-1]
    for i in range(len(weights)-1):
        activation += weights[i] * inputs[i]
    return activation

def transfer(activation):
    if activation < -700: return 0
    if activation > 700: return 1
    return 1.0 / (1.0 + exp(-activation))

def transfer_derivative(output):
    return output * (1.0 - output)

# --- PROPAGATION ---
def forward_propagate(network, row):
    inputs = row
    for layer in network:
        new_inputs = []
        for neuron in layer:
            activation = activate(neuron['weights'], inputs)
            neuron['output'] = transfer(activation)
            new_inputs.append(neuron['output'])
        inputs = new_inputs
    return inputs

def backward_propagate_error(network, expected):
    for i in reversed(range(len(network))):
        layer = network[i]
        errors = list()
        if i != len(network)-1:
            for j in range(len(layer)):
                error = 0.0
                for neuron in network[i + 1]:
                    error += (neuron['weights'][j] * neuron['delta'])
                errors.append(error)
        else:
            for j in range(len(layer)):
                neuron = layer[j]
                errors.append(expected[j] - neuron['output'])
        for j in range(len(layer)):
            neuron = layer[j]
            neuron['delta'] = errors[j] * transfer_derivative(neuron['output'])

def update_weights(network, row, l_rate):
    for i in range(len(network)):
        inputs = row[:-1]
        if i != 0:
            inputs = [neuron['output'] for neuron in network[i - 1]]
        for neuron in network[i]:
            for j in range(len(inputs)):
                neuron['weights'][j] += l_rate * neuron['delta'] * inputs[j]
            neuron['weights'][-1] += l_rate * neuron['delta']
```

## Part 5: Training with Analytics

We have updated the training loop to track performance. 

Instead of just printing errors, we now calculate:
1.  **Loss:** How far off the probabilities were (lower is better).
2.  **Accuracy:** What percentage of letters were correctly identified (higher is better).

We run for **200 epochs** to allow the network time to learn these complex shapes.

```python exec
id: 06-interactive-lab-nist-7
def train_network(network, train, l_rate, n_epoch, n_outputs):
    history = {'loss': [], 'accuracy': []}
    
    for epoch in range(n_epoch):
        sum_error = 0
        correct_guesses = 0
        
        for row in train:
            inputs = row[0]
            expected_label = row[1]
            
            # 1. Forward
            outputs = forward_propagate(network, inputs)
            
            # 2. Check Accuracy (Did we guess the right letter?)
            if outputs.index(max(outputs)) == expected_label:
                correct_guesses += 1
            
            # 3. Expected Output Array
            expected = [0 for i in range(n_outputs)]
            expected[expected_label] = 1
            
            # 4. Error
            sum_error += sum([(expected[i]-outputs[i])**2 for i in range(len(expected))])
            
            # 5. Backward
            backward_propagate_error(network, expected)
            update_weights(network, inputs, l_rate)
        
        # Calculate metrics for this epoch
        epoch_loss = sum_error / len(train)
        epoch_acc = correct_guesses / len(train) * 100
        
        history['loss'].append(epoch_loss)
        history['accuracy'].append(epoch_acc)
        
        if epoch % 10 == 0:
            print('>Epoch=%d, Loss=%.3f, Accuracy=%.2f%%' % (epoch, epoch_loss, epoch_acc))
            
    return history

# Settings
n_hidden = 30
l_rate = 0.3
n_epoch = 200

print("Initializing Network...")
network = initialize_network(n_inputs, n_hidden, n_outputs)

print(f"Starting Training (this may take a few minutes)...")
history = train_network(network, dataset, l_rate, n_epoch, n_outputs)
print("Training Complete.")
```

## Part 6: Analyzing Performance

We can now plot the learning process. You should see the Loss curve go down and the Accuracy curve go up. This visualization helps us understand if the network is still learning or if it has "plateaued" (stopped improving).

```python exec
id: 06-interactive-lab-nist-8
def plot_history(history):
    epochs = range(len(history['loss']))
    
    plt.figure(figsize=(12, 5))
    
    # Plot Loss
    plt.subplot(1, 2, 1)
    plt.plot(epochs, history['loss'], 'r-')
    plt.title('Training Loss (Error)')
    plt.xlabel('Epochs')
    plt.ylabel('Loss')
    
    # Plot Accuracy
    plt.subplot(1, 2, 2)
    plt.plot(epochs, history['accuracy'], 'b-')
    plt.title('Training Accuracy (%)')
    plt.xlabel('Epochs')
    plt.ylabel('Accuracy')
    
    plt.show()

plot_history(history)
```

## Part 7: Seeing the Brain

This is the most critical part of understanding neural networks. We often call them "black boxes," but we can look inside.

We have a hidden layer with 30 neurons. Each neuron has 784 weights connecting it to the 784 input pixels. If a weight is high, it means the neuron cares about that pixel. 

If we take those 784 weights and reshape them back into a 28x28 grid, we can see exactly what visual pattern that neuron is looking for. Some might look like the curve of a 'C', others like the vertical line of a 'T'.

```python exec
id: 06-interactive-lab-nist-9
def visualize_network_weights(network):
    # Get the hidden layer (layer 0)
    hidden_layer = network[0]
    
    # Calculate grid size for plotting (e.g. 5x6 for 30 neurons)
    n_neurons = len(hidden_layer)
    cols = 6
    rows = (n_neurons // cols) + 1
    
    plt.figure(figsize=(15, rows * 2.5))
    plt.suptitle("What the Hidden Neurons are Looking For", fontsize=16)
    
    for i, neuron in enumerate(hidden_layer):
        # The last weight is the bias, so we exclude it ([:-1])
        weights = neuron['weights'][:-1]
        
        # Reshape to 28x28
        weight_grid = np.array(weights).reshape(28, 28)
        
        plt.subplot(rows, cols, i + 1)
        # We use a diverging colormap (coolwarm) to see positive (red) and negative (blue) weights
        plt.imshow(weight_grid, cmap='coolwarm') 
        plt.title(f"Neuron {i+1}")
        plt.axis('off')
        
    plt.tight_layout()
    plt.show()

visualize_network_weights(network)
```

## Part 8: Final Verification

Finally, let's verify the network on specific examples.

```python exec
id: 06-interactive-lab-nist-10
def predict(network, row):
    outputs = forward_propagate(network, row)
    return outputs.index(max(outputs))

print("--- TEST RESULTS ---")

for i in range(min(5, len(dataset))):
    row = dataset[i]
    input_pixels = row[0]
    actual_label = row[1]
    
    prediction = predict(network, input_pixels)
    
    actual_char = label_map.get(actual_label, '?')
    pred_char = label_map.get(prediction, '?')
    
    status = "CORRECT" if actual_label == prediction else "INCORRECT"
    
    print(f"Test #{i+1}: Expected '{actual_char}' | Predicted '{pred_char}' -> {status}")
```

## What we set out to do

These were the aims of this notebook. Now that you have worked through it, they are a check on what happened rather than a promise about it.

1.  **Manipulate** raw image data (rotation and reflection) to prepare it for training.
2.  **Construct** a neural network to recognize 26 different letter patterns.
3.  **Analyze** the learning process by interpreting Loss and Accuracy graphs.
4.  **Visualize** the internal weights of the network to demystify how it recognizes patterns.

---

## Looking back

Before leaving this page, a sentence on each. What you write stays on this device.

```reflect
- Something you expected before running a cell that turned out differently
- The one idea from this page you could explain to someone else now
- Something you would change or try next, if there were time
- A question this page raised for you that it did not answer. Bring it to the next session; these questions are where the next session starts.
```
