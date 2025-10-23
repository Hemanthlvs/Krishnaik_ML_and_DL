# RNN Backpropagation with Time

## Loss Calculation

*   After calculating `y_hat`, the **loss** is determined by comparing `y_hat` to the actual output `y` (e.g., `y - y_hat`).

## Backpropagation with Time

This is used to reduce the calculated loss by **updating the weights**. This process continuously cycles through forward and backward propagation until the loss is minimized (convergence in **gradient descent** towards a **global minima**).

*   **Weights to Update:** There are three main types of weights that need to be updated:
    1.  **Input Weights (`Wi`)**
    2.  **Hidden Weights (`Wh`)**
    3.  **Output Weights (`Wo`)**
*   **Weight Updation Formula:**
    *   The general formula for updating any weight is:
        `Weight_new = Weight_old - Learning_Rate * (Derivative of Loss with respect to Derivative of Weight_old)`.
    *   The **Learning Rate** is a small value (e.g., 0.001) that controls how much the weights are adjusted.
    *   The core task is to **compute the derivative of the loss with respect to the old weight** (this is the slope of the gradient descent). This is done using the **chain rule of derivatives**.

### Updating Output Weights (`Wo`)

*   `Wo` is updated first in backpropagation (starting from the last timestamp).
*   **Dependency Chain:** Loss is directly dependent on `y_hat`, and `y_hat` is directly dependent on `Wo`.
*   **Chain Rule:** `dL/dWo = (dL/dy_hat) * (dy_hat/dWo)`.

### Updating Hidden Weights (`Wh`)

*   `Wh` is crucial because it is **used in all timestamps** (t=1, t=2, t=3, etc.).
*   The derivative of the loss with respect to `Wh` is calculated by **summing the derivatives from each timestamp** where `Wh` was used.
*   **Dependency Chains (using `O3` as the final output here):**
    *   **At t=3:** `Loss -> y_hat -> O3 -> Wh`.
        *   Derivative: `(dL/dy_hat) * (dy_hat/dO3) * (dO3/dWh)`
    *   **At t=2:** `Loss -> y_hat -> O3 -> O2 -> Wh`.
        *   Derivative: `(dL/dy_hat) * (dy_hat/dO3) * (dO3/dO2) * (dO2/dWh)`
    *   **At t=1:** `Loss -> y_hat -> O3 -> O2 -> O1 -> Wh`.
        *   Derivative: `(dL/dy_hat) * (dy_hat/dO3) * (dO3/dO2) * (dO2/dO1) * (dO1/dWh)`
*   The final `dL/dWh` is the sum of these derivatives.

### Updating Input Weights (`Wi`)

*   Similar to `Wh`, `Wi` is also updated based on **each timestamp** where an input was provided.
*   The derivative of the loss with respect to `Wi` is calculated by **summing the derivatives from each timestamp**.
*   **Dependency Chains (using `O3` as the final output here):**
    *   **At t=3:** `Loss -> y_hat -> O3 -> Wi`.
        *   Derivative: `(dL/dy_hat) * (dy_hat/dO3) * (dO3/dWi)`
    *   **At t=2:** `Loss -> y_hat -> O3 -> O2 -> Wi`.
        *   Derivative: `(dL/dy_hat) * (dy_hat/dO3) * (dO3/dO2) * (dO2/dWi)`
    *   **At t=1:** `Loss -> y_hat -> O3 -> O2 -> O1 -> Wi`.
        *   Derivative: `(dL/dy_hat) * (dy_hat/dO3) * (dO3/dO2) * (dO2/dO1) * (dO1/dWi)`
*   The final `dL/dWi` is the sum of these derivatives.

## Conclusion

By performing forward propagation to calculate loss and then backpropagation to update `Wi`, `Wh`, and `Wo` using the chain rule across all relevant timestamps, an RNN can iteratively learn and reduce its prediction error. This process aims to reach the **global minima** of the loss function.