# Vanishing Gradients and Activation Functions

## Neural Network Architecture Example
*   The example used is a "two-layered neural network" with:
    *   One input layer.
    *   Two hidden layers (hidden layer one, hidden layer two), each with a single neuron for simplicity.
    *   One output layer.

## Neuron Operation (Forward Propagation)
*   Inside each neuron, the input is processed in two main steps:
    1.  **Step 1: Weighted Sum + Bias (Z-value)**: The input (`x_i`) is multiplied by its corresponding weights (`w_i`), and then a bias (`b`) is added. This sum is denoted as `Z = Σ (w_i * x_i) + bias`.
    2.  **Step 2: Activation Function Application**: An activation function is applied to the `Z` value. In this discussion, the `sigmoid` activation function is used.

## Sigmoid Activation Function
*   **Main Aim/Purpose**:
    *   It takes the `Z` value as input and transforms its value to be between 0 and 1.
    *   It is specifically used in binary classification problems where the desired output is either 0 or 1.
*   **Mathematical Equation**: `Sigmoid(Z) = 1 / (1 + e^(-Z))`.
*   **Graphical Representation**: The graph of the sigmoid function is an S-shaped curve, mapping any `Z` value to a range between 0 and 1.

## Loss Function and Optimizers
*   After forward propagation, a loss function (e.g., `(y - y_hat)^2`) is calculated.
*   Optimizers are used to reduce this loss function. Their main work is to perform backpropagation and update the weights (e.g., `w_1`, `w_2`, `w_3`).

## Weight Updation (Backpropagation & Chain Rule)
*   **Weight Update Formula**: The new weight (`w_new`) is calculated as: `w_new = w_old - learning_rate * (dLoss / dW_old)`.
    *   The `learning_rate` is typically a small value (e.g., 0.001) which influences the speed of convergence.
*   **Importance of Chain Rule**:
    *   To update weights (e.g., `w_1`), the derivative of the loss with respect to that weight (`dLoss / dW_1`) needs to be calculated.
    *   Backpropagation involves going backward from the loss (output) layer to update weights in preceding layers.
    *   The loss is dependent on `O_31`, which is dependent on `O_21`, which is dependent on `O_11`, and finally `O_11` is dependent on `W_1`.
    *   The chain rule breaks down `dLoss / dW_1` into a product of derivatives: `(dLoss/dO_31) * (dO_31/dO_21) * (dO_21/dO_11) * (dO_11/dW_1)`.

## Derivative of Sigmoid Function
*   **Key Property**: While the sigmoid function itself outputs values between 0 and 1, its derivative `(d(Sigmoid(Z))/dZ)` always ranges between **0 and 0.25**. This property is 	mathematically proven.
*   This small range of the derivative is crucial for understanding the vanishing gradient problem.

## Vanishing Gradient Problem
*   **Explanation**:
    *   When calculating the derivative of the loss with respect to a weight in an earlier layer (e.g., `w_1`), the chain rule requires multiplying several derivatives together.
    *   Many of these derivatives involve the derivative of the sigmoid activation function, which is always between 0 and 0.25.
    *   Initial weights are also typically small values (e.g., between 0 and 1).
    *   Repeated multiplication of these small values (0 to 0.25) across multiple layers in a deep neural network results in an extremely small overall gradient (e.g., `0.0000001`).
*   **Consequence**:
    *   If `(dLoss / dW_old)` is extremely small, then `learning_rate * (dLoss / dW_old)` will also be very small.
    *   This leads to `w_new` being approximately equal to `w_old` (`w_new ≈ w_old`).
    *   Consequently, the weights are "never getting updated" or update negligibly.
    *   This prevents the neural network from moving towards the convergence point (global minima) and makes it stagnant.
*   **Definition**: The "vanishing gradient problem" is this scenario where weights do not update significantly, primarily caused by the sigmoid activation function's derivative range (0 to 0.25), especially problematic in deep neural networks with many hidden layers.

## Solutions and Other Activation Functions
*   To fix the vanishing gradient problem, researchers started exploring other activation functions.
*   Examples of other activation functions to be discussed include:
    *   TanH (Hyperbolic Tangent)
    *   ReLU (Rectified Linear Unit)
    *   PReLU (Parametric ReLU)
    *   Swish

## Conclusion
*   Sigmoid activation function is problematic for deep neural networks due to its derivative always being between 0 and 0.25, leading to vanishing gradients.
*   While it might be acceptable for smaller neural networks, it is not suitable for deep networks (e.g., with 100 hidden layers).