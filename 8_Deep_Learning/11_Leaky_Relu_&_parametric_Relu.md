# Leaky ReLU and Parametric ReLU

## Introduction
*   This discussion continues the topic of activation functions, specifically focusing on Leaky ReLU and Parametric ReLU.
*   The primary problem addressed by these functions is the "dead neuron" or "dead ReLU problem" faced with standard ReLU, where entire neurons become deactivated.
*   Leaky ReLU and Parametric ReLU are designed to solve this issue.

## Leaky ReLU
*   **Formula**: `max(0.01 * x, x)`.
*   **Mechanism**: A small constant (e.g., 0.01) is multiplied by `x` for negative inputs, instead of making them exactly zero.
    *   This constant ensures that for negative inputs, the output is a small negative value rather than zero, preventing the "dead" state.
*   **Derivative**:
    *   For `x <= 0` (negative numbers), the derivative is a very small positive value (e.g., 0.01).
    *   For `x > 0` (remaining values), the derivative is 1.
*   **Solution to Dead Neuron Problem**:
    *   Because the derivative never becomes exactly zero (it's always a small positive value), backpropagation can still occur, preventing neurons from deactivating permanently.
    *   This fixes the dead neuron problem.
*   **Advantages**:
    *   Retains all the advantages of the standard ReLU.
    *   Explicitly removes the dead ReLU problem.
    *   Helps in solving both the vanishing gradient problem and the dead ReLU problem.

## Parametric ReLU (PReLU)
*   **Formula**: `max(alpha * x, x)`.
*   **Mechanism**:
    *   Instead of a fixed constant like 0.01, `alpha` is a **hyperparameter**.
    *   This `alpha` value is learned or found through **hyperparameter tuning** during the training process.
*   **Alpha Value**:
    *   `alpha` can take any value, such as 0.01, 0.02, 0.03, etc., depending on the specific problem statement.
*   **Difference from Leaky ReLU**:
    *   Leaky ReLU uses a predefined constant (e.g., 0.01) for the small slope.
    *   Parametric ReLU allows `alpha` to be a learnable hyperparameter, offering more flexibility and potentially better performance tuned to the specific data.