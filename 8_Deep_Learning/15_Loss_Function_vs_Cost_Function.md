# Loss Function vs. Cost Function

## Purpose of Loss Function / Cost Function
*   The main aim is to reduce the difference between `y` (actual point) and `y hat` (predicted point).
*   This reduction is achieved with the help of optimizers.
*   Gradient Descent is an example of an optimizer that updates specific weights during backpropagation.

## Loss Function vs. Cost Function

### Loss Function
*   Calculated for **every single data point**.
*   For each data point:
    *   Forward propagation occurs (input passes, calculations happen, `y hat` is obtained).
    *   The loss is computed (e.g., `y - y hat` whole square for Mean Squared Error).
    *   Backpropagation occurs, and **weights are updated** with the help of an optimizer.
*   This means forward and backward propagation happen for every data point, leading to weight updates for each.
*   **Example Formula (Mean Squared Error)**: `(y - y hat)^2`.

### Cost Function
*   Calculated for **all data points together** or a batch of points.
*   All data points are sent through forward propagation at one time.
*   `y hat` is computed for each data point.
*   The difference (`y - y hat`) is calculated for each data point, then these errors are summed, and the mean is found.
*   **Weights are updated only once** in the backward propagation after considering all (or a batch of) data points.
*   **Example Formula (Mean Squared Error)**: `(1/n) * summation of (y_i - y_i_hat)^2` for `i = 1 to n`.

## When to Use Which
*   Use a **Loss Function** if you want to update the weights by playing with every individual data point.
*   Use a **Cost Function** if you want to use all data points and update the weights only once in backpropagation.