# Softmax Activation Function:

*   **Purpose**: The softmax activation function is specifically used in the output layer for multi-class classification problems.

## Softmax vs. Sigmoid: Why Softmax is Needed

### Binary Classification (Sigmoid)
*   **Output Layer**: For binary classification, the output layer typically has one neuron.
*   **Activation Function**: A sigmoid activation function is used in the output layer for binary classification.
*   **Transformation**: Sigmoid transforms values between 0 and 1.
*   **Decision Rule**: A threshold (e.g., 0.5) can be applied: if the output is greater than or equals to 0.5, it's classified as 1; if less, it's classified as 0.

### Multi-Class Classification (Softmax)
*   **Challenge**: Sigmoid cannot be used when there are multiple outputs or classes to predict, because it only provides binary outputs (0 or 1).
*   **Scenario**: Consider a neural network designed to classify images into multiple categories (e.g., cat, dog, monkey, horse).
    *   The input layer takes image features (e.g., X1, X2, X3).
    *   The output layer would need multiple neurons, one for each category (e.g., four output neurons for cat, dog, monkey, horse).
    *   Each output neuron should give the probability of the input belonging to its respective category (e.g., probability of cat, probability of dog, etc.).
*   **Solution**: In such multi-class scenarios, the softmax activation function is used in the output layer instead of sigmoid.

## How Softmax Activation Function Works

### Input to Softmax
*   Before applying the softmax activation function, you get raw outputs from the neural network's calculations in the output layer.
*   These outputs are typically derived from multiplying previous layer outputs by weights and adding a bias.
*   **Example Raw Outputs**: Let's say the raw outputs for four categories are -1, 0, 3, and 5.

### Softmax Formula
*   The formula for softmax is:
    ```
    Softmax(y_i) = e^(y_i) / Σ[k=0 to n] e^(y_k)
    ```
    *   `e` is Euler's number (the base of the natural logarithm).
    *   `y_i` represents the raw output for the *i*-th node (or category).
    *   `Σ[k=0 to n] e^(y_k)` represents the sum of `e` raised to the power of the raw output for *all* `n` output nodes.
    *   `n` is the total number of output nodes (categories).

### Step-by-Step Calculation Example
Let's use the example raw outputs: -1 (Cat), 0 (Dog), 3 (Monkey), 5 (Horse).

*   **For Cat (y_i = -1)**:
    *   Numerator: `e^(-1)`
    *   Denominator: `e^(-1) + e^(0) + e^(3) + e^(5)`
    *   Result (approx): `0.00033`

*   **For Dog (y_i = 0)**:
    *   Numerator: `e^(0)`
    *   Denominator: `e^(-1) + e^(0) + e^(3) + e^(5)`
    *   Result (approx): `0.0024`

*   **For Monkey (y_i = 3)**:
    *   Numerator: `e^(3)`
    *   Denominator: `e^(-1) + e^(0) + e^(3) + e^(5)`
    *   Result (approx): `0.0183`

*   **For Horse (y_i = 5)**:
    *   Numerator: `e^(5)`
    *   Denominator: `e^(-1) + e^(0) + e^(3) + e^(5)`
    *   Result (approx): `0.1353`

### Interpreting Softmax Output
*   The outputs from the softmax function represent probabilities for each class.
*   **Key Property**: The sum of all these probabilities for all categories will always be equal to 1.
*   **Finding Probabilities**: To find the final probability for each class, you typically normalize by dividing each individual softmax output by the sum of all softmax outputs. For example, for Horse:
    *   `0.1353 / (0.00033 + 0.0024 + 0.0183 + 0.1353)`
    *   This gives approximately `0.86` or 86%.
*   **Prediction**: The class with the highest probability is selected as the final prediction. In the example, Horse has the highest probability (86%), so the output would be "Horse".

## Summary: When to Use Which Activation Function

*   **Binary Classification Problem**: Use **Sigmoid** activation function in the output layer.
*   **Multi-Class Classification Problem**: Use **Softmax** activation function in the output layer.