# Stochastic Gradient Descent (SGD) Optimizer

## How SGD Works

*   In Gradient Descent, for 1000 data points, all 1000 points were used during forward propagation and then back-propagation occurred.
*   With SGD, within one epoch, only a single data point is given in every iteration.
*   **Process per iteration:**
    1.  A single record is fed into the model.
    2.  `y_hat` is computed.
    3.  The loss function is calculated.
    4.  The loss function is minimized using the SGD optimizer.
    5.  Weights are updated based on this single data point.
*   This process repeats for each data point. For 1000 data points, one epoch will involve 1000 iterations.
*   Multiple epochs can be run until the loss value decreases sufficiently.

## Advantages of SGD

*   **Solves Resource Issues:** SGD is less resource-intensive.
    *   You can train models even with limited RAM (e.g., 4GB or 8GB).
    *   This is because only one record is processed and weights are updated at a time.

## Disadvantages of SGD

*   **High Time Complexity:** SGD takes a huge amount of time.
    *   Updating weights with one data point at a time for potentially millions of data points leads to many iterations.
    *   For example, 1 million data points would mean 1 million iterations per epoch. If there are 100 epochs, that's 100 million iterations.
    *   Training the entire model will take more time, especially with a large number of data points.
*   **Slow Convergence:** The model takes more time to converge.
    *   In Gradient Descent, convergence is smoother because all records are used for forward propagation, cost calculation, and back-propagation.
    *   In SGD, because only a single data point is used at a time for weight updates, the convergence is not smooth.
*   **Noise Introduction:** Noise gets introduced during the training process.
    *   The loss value will continuously "roam" here and there before finally merging into the global minima.
    *   This "jumping" behavior prevents a smooth convergence.
    *   This noise is a direct result of performing back-propagation with only a single data point.
    *   The noise contributes to increased training time and slower convergence.