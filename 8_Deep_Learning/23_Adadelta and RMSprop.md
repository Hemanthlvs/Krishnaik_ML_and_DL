# Optimizers: Adadelta and RMSprop

## Adadelta and RMSprop
*   **Purpose**: To fix Adagrad's problem of `alpha_t` becoming too high.
*   **New Formula for Dynamic Learning Rate**: `dynamic_learning_rate = learning_rate / sqrt(s_dw + epsilon)`.
    *   Instead of `alpha_t`, they use `s_dw`.
*   **How `s_dw` is calculated**: `s_dw` uses **Exponential Weighted Average (EWA)** to "smoothen" the update of `alpha_t` (now `s_dw`).
    *   **EWA Formula**: `s_dw_t = beta * s_dw_(t-1) + (1 - beta) * (derivative_loss/derivative_w_t-1)^2`.
        *   `beta` is a decay rate (e.g., 0.95).
        *   The `beta` term restricts the influence of past squared derivatives, preventing `s_dw` from growing infinitely large.
        *   The term `(1 - beta)` (e.g., 0.05) limits how much the current squared derivative contributes, ensuring `s_dw` remains within a reasonable range.
    *   `s_dw` is initialized to zero for the first timestamp (which means in the formula initially s_dw_(t-1) is 0).
*   **Key Improvements over Adagrad**:
    1.  They still provide a **dynamic learning rate**.
    2.  They **restrict the `alpha_t` value** (now `s_dw`) from becoming very high by using Exponential Weighted Average.
    3.  They introduce a **smoothening concept** using EWA, which helps stabilize the learning process.
*   **Two Names (Adadelta & RMSprop)**: They originate from two different researchers and have slight differences, but their working principle is almost the same.
*   **Weight Updation Formula**: `w_t = w_(t-1) - dynamic_learning_rate * (derivative_loss/derivative_w_t-1)`.
    *   `w_t` represents the new weights, and `w_(t-1)` represents the older weights.