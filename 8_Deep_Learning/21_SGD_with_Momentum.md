## SGD with Momentum and Exponential Weighted Average Notes

### SGD with Momentum: The Solution
*   The goal is to "smoothen" this noise using SGD with Momentum.
*   Momentum helps in smoothing the convergence path.

### Weight Updation Formulas
*   The standard weight update formula is `w_new = w_old - learning_rate * derivative_of_loss_with_respect_to_w_old`.
*   The bias update formula is `bias_new = bias_old - learning_rate * derivative_of_loss_with_respect_to_bias_old`.
*   These formulas are fundamental for updating weights and biases.
*   To incorporate momentum, the weight update formula is re-written using time notation: `w(t) = w(t-1) - learning_rate * derivative_of_loss_with_respect_to_w(t-1)`.
    *   `w(t)` represents the new (current time) weight.
    *   `w(t-1)` represents the previous weight.

### Exponential Weighted Average (EWA): The Core of Smoothing
*   Smoothing is achieved through a concept called **Exponential Weighted Average**.
*   EWA is crucial because it directly performs the smoothing.

#### How EWA Works (Time Series Example)
*   Imagine a time series with values `a1, a2, a3, ..., an` at times `t1, t2, t3, ..., tn`.
*   To apply EWA, a parameter called `beta` is introduced.
*   `beta` controls the smoothing function and ranges between 0 and 1.
*   **Formula for EWA (e.g., at time t2):** `V(t2) = beta * V(t1) + (1 - beta) * a2`.
    *   Here, `V(t1)` is simply `a1` (the value at time t1).
*   **Example with Beta:** If `beta = 0.95`:
    *   `V(t2) = 0.95 * V(t1) + 0.05 * a2`.
*   **Influence of Beta:**
    *   A higher `beta` value (e.g., 0.95) means the previous value (`V(t1)`) has more control over the smoothing.
    *   The current value (`a2`) has less control.
*   This process allows the previous points to "smooth" the current point.
*   **Chaining EWA:** For `V(t3)`, the formula becomes `V(t3) = beta * V(t2) + (1 - beta) * a3`.
    *   `V(t2)` itself contains the influence of `a1` and `a2`, so `V(t3)` effectively incorporates `a1`, `a2`, and `a3` with decreasing weights for older values.
*   **Result:** Applying EWA transforms a zigzag line (noisy data) into a smooth line. This smooth line effectively reduces noise.

### Advantages of SGD with Momentum
*   **Reduces Noise:** This is the primary benefit, achieved through the smoothing concept of EWA.
*   **Leads to Quick/Faster Convergence:** By smoothing the path, the optimizer reaches the global minimum more efficiently.

### Connection to Time Series Data
*   The Exponential Weighted Average technique is commonly used in time series data analysis.