# Multi-Layer Perceptron (MLP) Networks

## 1. Introduction to Multi-Layer Perceptron Models

- **Definition**: A Multi-Layer Perceptron (MLP) is a type of artificial neural network with multiple layers.
- **Advantages over Single-Layer Perceptron**: 
  - Single-layer perceptrons have limitations, which MLP models overcome. While single-layer perceptrons only involve a feed-forward neural network and a threshold value for output (1 or 0).
  - MLPs use **forward propagation** and **backward propagation** to adjust weights efficiently, leading to faster training.

## 2. Overview of Multi-Layer Neural Network Architecture

Consider a dataset with features like IQ, study hours, and play hours to determine if a student passed (1) or failed (0).

- **Input Layer**: Receives input features (e.g., X1, X2, X3).
- **Hidden Layers**: MLPs can have one or more hidden layers, each containing multiple neurons.
  - Example: Hidden Layer 1 and Hidden Layer 2.
- **Output Layer**: Produces the final prediction.
- **Neurons**: Basic processing units in each layer.
- **Weights (W)**: Connections between neurons, initially assigned randomly (e.g., W1, W2, W3, W4).
- **Bias (B)**: Additional weight for each neuron, also initialized randomly (e.g., B1, B2).

## 3. Forward Propagation

Forward propagation is the process of moving inputs through the network to produce an output.

### Steps in Each Neuron (Hidden Neurons and Output Layer):

1. **Weighted Summation (Z calculation)**:
   - Inputs (X) are multiplied by their weights (W) and summed, with the bias (B) added.
   - Formula: `Z = Σ(X_i * W_i) + B` or `Z = W_T * X + B`.
   - **Example** (Hidden Layer 1, Neuron 1):
     - Given: X1=95, X2=4, X3=4; W1=0.01, W2=0.02, W3=0.03; B1=0.001.
     - Calculation: 
       ```
       Z = (95 * 0.01) + (4 * 0.02) + (4 * 0.03) + 0.001
         = 0.95 + 0.08 + 0.12 + 0.001
         = 1.151
       ```

2. **Activation Function Application**:
   - The `Z` value is passed through an activation function to determine the neuron's output.
   - **Example** (Sigmoid Function):
     - Converts `Z` to a value between 0 and 1.
     - Formula: `Sigmoid(Z) = 1 / (1 + e^(-Z))`.
     - For `Z = 1.151`: 
       ```
       Output (O1) = Sigmoid(1.151) ≈ 0.759
       ```

### Propagation to Next Layer:
- The output from the first hidden layer becomes the input for the next layer.
- **Example** (Hidden Layer 2, Neuron 2):
  - Input: O1 = 0.759; W4 = 0.02; B2 = 0.03.
  - Calculation:
    ```
    Z_new = (O1 * W4) + B2
           = (0.759 * 0.02) + 0.03
           = 0.01518 + 0.03
           = 0.04518
    Output (O2) = Sigmoid(0.04518) ≈ 0.51129
    ```

## 4. Loss Function

After forward propagation, the predicted output (`y_hat`) is compared to the actual output (`y`).

- **Purpose**: Measures the error between predicted and actual outputs.
- **Example**:
  - Predicted output (`y_hat`): `0.51129`.
  - Actual output (`y`): `1` (pass).
  - Error Calculation: 
    ```
    Error = |Actual - Predicted| = |1 - 0.51129| ≈ 0.49
    ```
- **Goal**: Reduce this error during training.

## 5. Backward Propagation

Backward propagation adjusts the network's weights to minimize the loss.

- **Purpose**: Update weights to reduce error.
- **Process**: Updates occur from the output layer back through the hidden layers.
- **Inventor**: Developed by **Geoffrey Hinton**, known as the "godfather of deep learning."

## 6. Training Process - Iterative Cycle

Training a neural network involves repeating the following steps:

1. **Forward Propagation**: Input is fed through the network to generate a predicted output.
2. **Loss Calculation**: Determine the error between predicted and actual outputs.
3. **Backward Propagation**: Update weights to minimize error.
4. **Repeat**: Continue this cycle until the loss is sufficiently reduced or converges.
