# Deep Learning Optimizers: Gradient Descent 

## Introduction to Optimizers
*   Optimizers are crucial in deep learning.
*   Optimizers are responsible for reducing the loss function during the **backward propagation** phase.
*   Their main goal in backward propagation is to **update all the weights** of the neural network.
*   By reducing the loss, the model's predictions become closer to the actual output.

## Weight Updation Formula
*   The general weight updation formula is:
    `w_new = w_old - (learning_rate * derivative_of_loss_with_respect_to_w_old)`
*   `w_new`: The new weight value.
*   `w_old`: The old weight value.
*   `learning_rate`: Controls the speed at which the model converges (moves towards the optimal solution).
*   `derivative_of_loss_with_respect_to_w_old`: Indicates the direction and magnitude to update the weight.
*   This formula changes for different optimizers.

## Gradient Descent Curve and Global Minima
*   When you plot weights against the loss (or cost function), you often get a parabola-like curve.
*   This is called a **gradient descent curve**.
*   The main aim of gradient descent is to reach the lowest point on this curve, which is called the **global minima**.
*   The weight updation formula helps move the weights towards this global minima over time.
*   At the global minima, the slope of the curve is zero, meaning `w_new` will be approximately equal to `w_old`, and the loss function will have been minimized.

## Loss Function vs. Cost Function
*   **Loss function**: Calculates the error for a single data point (e.g., `(y - y_hat)^2` for Mean Squared Error).
*   **Cost function**: Calculates the average error across all data points (e.g., `(1/n) * Sum((y_i - y_i_hat)^2)` for MSE).

## Epochs and Iterations in Gradient Descent
*   Gradient Descent (specifically Batch Gradient Descent) processes **all data points** at once.
*   **Forward Propagation**: All data points (e.g., 1000 data points) are passed through the neural network to compute `y_hat` for each.
*   **Cost Calculation**: The cost function is then calculated based on all these `y_hat` values.
*   **Backward Propagation & Weight Update**: The optimizer performs backward propagation and updates weights based on the cost calculated from all data points.
*   **Epoch Definition**: **One forward propagation with all data points + one backward propagation with all data points = One Epoch**.
*   This process (epochs) continues until the cost function is sufficiently reduced.
*   **Iteration Definition (for Gradient Descent)**: In standard Gradient Descent, because all data points are processed at once in a single step, **one epoch is equal to one iteration**.
    *   *Note*: This differs from other optimizers where data might be split into smaller batches, leading to multiple iterations per epoch.

## Advantages of Gradient Descent
*   **Convergence**: It guarantees convergence to the global minima.

## Disadvantages of Gradient Descent
*   **Resource Intensive**: Requires significant computational resources like RAM and GPU.
    *   This is because it processes **all** data points at once during each epoch.
    *   For large datasets (e.g., 1 million data points), storing all data and updating all weights simultaneously demands huge memory and processing power.
*   Can cause systems to hang if resources are insufficient.
*   Training large datasets with Gradient Descent can be costly, especially if using cloud resources.