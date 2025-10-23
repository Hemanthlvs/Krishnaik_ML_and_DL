# Minibatch SGD:

## Introducing Minibatch SGD
*   Minibatch SGD introduces a new concept: **batch size**.
*   **Purpose of Batch Size**: To reduce noise and improve efficiency by not passing just one data point per iteration.

### How Minibatch SGD Works
*   **Example Scenario**: Total 100,000 (100K) data points.
*   **Batch Size**: Let's say a batch size of 1,000 records.
*   **Iterations per Epoch**:
    *   In every epoch, the number of iterations = Total data points / Batch size.
    *   Example: 100,000 / 1,000 = 100 iterations per epoch.
*   **Process per Iteration**:
    *   Instead of one, 1,000 data points (the batch) are passed for forward propagation.
    *   Backward propagation calculates the cost function (e.g., Mean Squared Error) based on these 1,000 data points.
    *   The optimizer (Minibatch SGD) then updates the weights based on this batch.
    *   This process repeats for each of the 100 iterations in an epoch, using the next batch of data points.

### Resource Usage
*   Passing 1,000 data points (or even 5,000) for weight updates is feasible and efficient for resources like RAM (e.g., 8GB or 16GB).

## Advantages of Minibatch SGD
1.  **Increased Convergence Speed**: Compared to SGD, the convergence speed increases due to the introduced batch size.
2.  **Reduced Noise**: Noise is significantly less compared to SGD, where only one data point is used. The convergence path is more definitive.
3.  **Efficient Resource Usage**: It helps in efficiently utilizing computational resources like RAM.

## Disadvantages of Minibatch SGD
1.  **Noise Still Exists**: While reduced, some noise still remains compared to the smooth convergence of pure Gradient Descent.
2.  **Convergence Time**: It may still take some time to converge, even if it's more efficient than SGD.
