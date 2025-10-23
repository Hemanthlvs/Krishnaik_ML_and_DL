# Choosing Activation Functions:

## Neural Network Structure
A typical Artificial Neural Network (ANN) consists of:
*   **Input Layer:** Receives the initial data (e.g., X1, X2, X3).
*   **Hidden Layers (HL1, HL2, etc.):** Intermediate layers where computations occur. A deep neural network can have 5 to 10 or more hidden layers and many neurons.
*   **Output Layer:** Produces the final result.

## How Data Flows and Activation Functions are Applied
1.  Inputs are multiplied by weights (e.g., w1, w2, w3).
2.  A bias (e.g., B1) is added to the weighted sum.
3.  An activation function is applied to the result of the previous step.

## Choosing Activation Functions

### For Hidden Layers
*   **Avoid `Sigmoid` and `Tanh` (Hyperbolic Tangent):**
    *   If `sigmoid` or `tanh` are used in deep hidden layers, they can lead to the **vanishing gradient problem**.
    *   The vanishing gradient problem hinders the learning process.
*   **Recommended: `ReLU` (Rectified Linear Unit) or its Variants:**
    *   `ReLU` and its variants are typically used in hidden layers.
    *   **Variants include:** `PReLU`, `Leaky ReLU`, and `ELU`.
    *   These variants address some issues found in basic `ReLU`, such as the "dead neuron concept" or "dead leaky ReLU," which occurs because `ReLU`'s derivative is either 0 or 1.

### For the Output Layer
The choice depends on the type of classification problem:
*   **Binary Classification:**
    *   Use `Sigmoid`.
    *   Example: Classifying between two categories (e.g., yes/no, true/false).
*   **Multi-Class Classification:**
    *   Use `Softmax`.
    *   Example: Classifying into more than two categories (e.g., cat, dog, bird).