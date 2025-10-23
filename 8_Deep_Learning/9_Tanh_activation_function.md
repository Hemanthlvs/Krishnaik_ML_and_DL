# Activation Functions: Tanh

## 1. Recap of Sigmoid Activation Function

*   **Output Range:** Transforms values between 0 and 1.
*   **Derivative Range:** Ranges between 0 and 0.25.
*   **Disadvantages:**
    *   Faces the **vanishing gradient problem** during backpropagation due to small derivative values.
    *   Function output is **not zero-centered**. This means the mean of the values is not zero.
    *   Power operations (e.g., `E to the power`) are **relatively time-consuming**.

## 2. Tanh (Hyperbolic Tangent) Activation Function

Tanh aims to solve some of the problems associated with gradient descent.

*   **Formula:**
    *   `tanh(z) = (e^z - e^(-z)) / (e^z + e^(-z))`.
    *   Here, `z` represents the sum of `w^T * x_i + B_i`.
*   **Output Transformation:** Transforms all input `z` values between **-1 to +1**. This is a key difference from Sigmoid (0 to 1).
*   **Derivative Range:** The derivative of Tanh always ranges between **0 to 1**. This is larger than Sigmoid's derivative range (0 to 0.25).

### Advantages of Tanh over Sigmoid

*   **Zero-Centric Output:** The entire function is **zero-centric**.
    *   Being zero-centric means the mean of the output values is zero, which is considered better than Sigmoid.
    *   This property helps in more **efficient weight updation**.
*   **Reduced Vanishing Gradient (for medium networks):**
    *   Due to its derivative ranging from 0 to 1, Tanh may **not face a vanishing gradient problem for medium-sized deep neural networks**.

### Disadvantages of Tanh

*   **Vanishing Gradient Problem Still Exists for Deep Networks:**
    *   Despite the better derivative range, the vanishing gradient problem **still exists for very deep neural networks**.
    *   **Reason:** In a deep network, multiplying derivatives (which can be values like 0.5, then 0.23, then 0.01, etc.) results in an increasingly smaller value. This prevents weights from being updated effectively (`w_new` approximately equals `w_old`).
*   **Computationally More Expensive:**
    *   Similar to Sigmoid, the Tanh formula involves `e to the power of x`, making **computation time higher**.