**Adagrad Optimizer**

**Introduction to Adagrad**
*   Adagrad Optimizer is a type of adaptive gradient descent.
*   It is designed to make the learning rate dynamic, unlike previous optimizers where the learning rate was usually fixed.

**Understanding Learning Rate**
*   The learning rate is a small value, typically between 0 and 1 (e.g., 0.001).
*   It determines the "speed of convergence" during the training process.
*   The standard weight update formula is: `w_t = w_t-1 - (learning_rate * derivative_of_loss_with_respect_to_w_t-1)`.

**Why Dynamic Learning Rate?**
*   **Problem with Fixed Learning Rate**: In previous optimizers, the learning rate remained constant throughout training.
*   **Ideal Scenario**: For efficient convergence, the learning rate should be:
    *   Larger initially to take bigger steps and speed up convergence.
    *   Smaller when approaching the global minimum to fine-tune and avoid overshooting.
*   Adagrad aims to achieve this dynamic behavior.

**How Adagrad Makes Learning Rate Dynamic**
*   Adagrad modifies the learning rate (`learning_rate_dash`) in the weight update formula.
*   The new dynamic learning rate formula is:
    `learning_rate_dash = (initial_learning_rate / sqrt(alpha_t + epsilon))`.
    *   `initial_learning_rate`: The original, user-defined learning rate.
    *   `alpha_t`: A crucial parameter that accumulates squared gradients over time.
        *   `alpha_t = Summation(i=1 to t) of (derivative_of_loss_with_respect_to_w_t-1)^2`.
        *   As backpropagation progresses through layers (from `i=1` to `t`), the `alpha_t` value continuously increases.
    *   `epsilon`: A very small value added to the denominator (e.g., 1e-8).
        *   **Purpose of Epsilon**: It prevents division by zero if `alpha_t` happens to be zero.

*   **Mechanism**: As `alpha_t` increases (due to summing up squared gradients from each layer), the denominator `sqrt(alpha_t + epsilon)` also increases. Since the `initial_learning_rate` is divided by this increasing value, the overall `learning_rate_dash` (the dynamic learning rate) decreases over time.

**Advantages of Adagrad**
*   Provides a dynamic learning rate, which is its primary advantage.
*   Initially takes larger steps, then smaller steps as it approaches the global minimum.

**Disadvantages of Adagrad**
*   **Diminishing Learning Rate**: In very deep neural networks, `alpha_t` can become extremely large.
*   This causes the dynamic learning rate (`learning_rate_dash`) to become very, very small (approaching zero).
*   **Stalled Updates**: When the learning rate is nearly zero, multiplying it by the derivative of the loss also results in a value close to zero.
*   Consequently, the weight updates (`w_t`) become minimal, meaning `w_t` is approximately equal to `w_t-1`, effectively stopping the learning process.