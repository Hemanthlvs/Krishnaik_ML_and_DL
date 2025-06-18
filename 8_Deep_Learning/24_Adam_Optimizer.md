# Adam Optimizer:

## Introduction to Adam Optimizer
*   Adam is currently considered the best optimizer.
*   It combines the advantages of previous optimizers.

## Key Features Inherited and Combined
*   **SGD with Momentum**: Adam incorporates this for less noise in updates. Momentum helps in "smoothening" weight updates.
*   **RMSprop**: Adam uses RMSprop's features, including a dynamic learning rate and a technique for smoothening so the learning rate doesn't become too high or zero.

## Weight Updation Formula
The most important part of optimizers is the weight updation formula.
*   **Weight Update**: `w_t = w_{t-1} - η' * v_d_w`
    *   `w_t`: New weight at time `t`
    *   `w_{t-1}`: Previous weight at time `t-1`
    *   `η'` (eta dash): Dynamic learning rate
    *   `v_d_w`: Smoothed derivative of loss with respect to weight (from momentum concept)

## Bias Updation Formula
Similar to weights, bias is also updated.
*   **Bias Update**: `b_t = b_{t-1} - η' * v_d_b`
    *   `b_t`: New bias at time `t`
    *   `b_{t-1}`: Previous bias at time `t-1`
    *   `v_d_b`: Smoothed derivative of loss with respect to bias

## Components of the Adam Optimizer

### A. Dynamic Learning Rate (`η'`)
*   This is the `η'` (eta dash) in the update formulas.
*   **Formula**: `η' = Learning_Rate / (s_d_w + ε)`
    *   `Learning_Rate`: Base learning rate.
    *   `s_d_w`: A component for smoothening (from RMSprop concept, exponential weighted average).
    *   `ε` (epsilon): A small constant to prevent division by zero.

### B. `s_d_w` (Smoothed Squared Gradients - for RMSprop part)
*   This is an **Exponential Weighted Average (EWA)** of the squared gradients. It helps in smoothening the dynamic learning rate.
*   **Formula for Weights**: `s_d_w_t+1 = β_2 * s_d_w_t + (1 - β_2) * (∂Loss/∂w_t)^2`
    *   `s_d_w_t+1`: `s_d_w` value for the next timestamp.
    *   `s_d_w_t`: `s_d_w` value for the current/previous timestamp.
    *   `β_2` (beta 2): A hyperparameter (usually different from beta for momentum).
    *   `∂Loss/∂w_t`: Derivative of loss with respect to weight at time `t`.
    *   Initially, `s_d_w_t` is initialized to zero.
*   Similar equation applies for `s_d_b` (for bias).

### C. `v_d_w` (Smoothed Gradients - for Momentum part)
*   This is also an **Exponential Weighted Average (EWA)** of the gradients, representing the "smoothening" concept used with SGD with Momentum.
*   **Formula for Weights**: `v_d_w = β_1 * v_d_w_{t-1} + (1 - β_1) * ∂Loss/∂w_{t-1}`
    *   `β_1` (beta 1): A hyperparameter (different from beta 2 for RMSprop part).
*   **Formula for Bias**: `v_d_b = β_1 * v_d_b_{t-1} + (1 - β_1) * ∂Loss/∂b_{t-1}`

## Summary of Adam's Strengths
*   **Combines Momentum**: Provides less noisy updates, reflected in `v_d_w` and `v_d_b` (EWA of gradients).
*   **Combines RMSprop**: Provides dynamic learning rates, reflected in `η'`.
*   **Smoothens Dynamic Learning Rate**: Achieved by using `s_d_w` (EWA of squared gradients).
*   These updates happen for both weight and bias updation formulas.