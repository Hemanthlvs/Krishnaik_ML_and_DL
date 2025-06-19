# Exploding Gradient Problem

## Neural Network Setup (Example)

*   The neural network example consists of an input layer, hidden layer one, hidden layer two, and an output layer.
*   Hidden layer one is shown with one neuron.
*   Weights (w1, w2, w3) are initialized between layers.
*   The process involves:
    *   Multiplying input with weights and adding bias (e.g., input * w1 + b1).
    *   Applying an activation function (e.g., ReLU in hidden layers, Sigmoid in the output for binary classification).
    *   Calculating `y_hat` (predicted output).
    *   Calculating the loss function.
    *   Performing backward propagation.

## Weight Updation Formula

*   To update a weight, for example, `w1`, the formula is:
    `w1_new = w1_old - learning_rate * (derivative of loss with respect to w1_old)`.
*   This formula is used by optimizers like Gradient Descent.

## The Cause of Exploding Gradients

*   The vanishing gradient problem was often due to values like the sigmoid derivative (0 to 0.25).
*   However, if the initial weights (e.g., `w3_old`) are very high (e.g., 500 or 1000).
*   Then, in the chain rule calculation (`(Sigmoid derivative) * w3`), this multiplication results in a very big number.
*   If all weights are initialized to very big values, then all terms in the chain rule multiplication will be large numbers.
*   Multiplying these large numbers together results in a "very big value" for the overall derivative of loss (`dL/dw1`).

## The Effect of Exploding Gradients

*   When `dL/dw1` is a very big value (positive or negative), even a small learning rate multiplied by it results in a "big value" for the update term.
*   This causes `w_new` to be significantly larger or smaller than `w_old`.
*   **Problem with Weight Updation**:
    *   On a cost function vs. weight graph, the goal is to reach the "global minima".
    *   Because weight updates are happening by very large numbers, the optimization process (e.g., gradient descent) does not smoothly approach the minima.
    *   Instead, the weight value "keeps on rotating here and there" or "goes outside the entire gradient descent".
    *   This prevents the model from reaching the global minima and converging.
*   This specific problem is called "exploding gradient descent".