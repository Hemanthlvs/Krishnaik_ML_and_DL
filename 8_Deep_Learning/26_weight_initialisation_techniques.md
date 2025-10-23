# Neural Network Weight Initialization Techniques

## Key Principles of Weight Initialization

When initializing weights in a neural network, keep these three crucial points in mind:
*   **Weights should be small**. Large weights can lead to the "exploding gradient problem".
*   **Weights should not be the same**. If all neurons have the same weights, they will perform identical processing. Each neuron needs to be able to process information differently, which is enabled by unique weights.
*   **Weights should have good variance**. This means there should be some variation or changes among the weights (e.g., W1, W2 should have some differences). This point supports the idea that weights should not be the same.

## Neural Network Layer Terminology

*   **Input Layer:** Where the input features (e.g., X1, X2, X3) are received.
*   **Hidden Layer(s):** Intermediate layers where processing occurs. A network can have multiple hidden layers.
*   **Output Layer:** The final layer that produces the network's output.
*   **Weights (w):** These are initialized between interconnected nodes (neurons) of different layers, e.g., `w1`, `w2`, `w3`, `w4`. `w_ij` often denotes the weight connecting an input layer neuron `i` to a hidden layer neuron `j`.

## Weight Initialization Techniques

Important weight initialization techniques:
*   Uniform Distribution
*   Xavier (Glorot) Initialization
*   He (Chi Ming He) Initialization

### Uniform Distribution

*   **Concept:** All weights (e.g., W1, W2, W3) are initialized based on a uniform distribution.
*   **Range (a, b):** In a uniform distribution, you specify a minimum (`a`) and maximum (`b`) value.
*   **Formula for (a, b):**
    *   `a = -1 / sqrt(input_nodes)`
    *   `b = 1 / sqrt(input_nodes)`
    *   So, the range is `[-1 / sqrt(input_nodes), 1 / sqrt(input_nodes)]`.
*   **Example:** If the input layer has 3 nodes (features), the range would be `[-1 / sqrt(3), 1 / sqrt(3)]`.
*   **Purpose:** This method initializes weights with values from this calculated uniform range.

### Xavier (Glorot) Initialization

*   **Inventor:** Xavier Glorot. This technique aims to address problems like the exploding gradient problem.
*   **Types:** There are two types of Xavier initialization:
    *   Xavier Normal Initialization
    *   Xavier Uniform Initialization

#### Xavier Normal Initialization

*   **Distribution:** Weights `w_ij` are initialized from a **normal distribution**.
*   **Mean:** The mean of this normal distribution is 0.
*   **Standard Deviation (sigma):**
    *   `sigma = sqrt(2 / (input_nodes + output_nodes))`
*   **Example:** If both input and output layers have 3 nodes, `sigma = sqrt(2 / (3 + 3)) = sqrt(2 / 6) = sqrt(1 / 3)`.

#### Xavier Uniform Initialization

*   **Distribution:** Weights are initialized from a **uniform distribution**.
*   **Range (a, b):**
    *   `a = -sqrt(6 / (input_nodes + output_nodes))`
    *   `b = sqrt(6 / (input_nodes + output_nodes))`
    *   So, the range is `[-sqrt(6 / (input_nodes + output_nodes)), sqrt(6 / (input_nodes + output_nodes))]`.

### He (Chi Ming He) Initialization

*   **Inventor:** Chi Ming He.
*   **Types:** There are two types of He initialization:
    *   He Normal Initialization
    *   He Uniform Initialization

#### He Normal Initialization

*   **Distribution:** Weights `w_ij` are initialized from a **normal distribution**.
*   **Mean:** The mean of this normal distribution is 0.
*   **Standard Deviation (sigma):**
    *   `sigma = sqrt(2 / input_nodes)`
*   **Example:** If the input layer has 3 nodes, `sigma = sqrt(2 / 3)`.

#### He Uniform Initialization

*   **Distribution:** Weights are initialized from a **uniform distribution**.
*   **Range (a, b):**
    *   `a = -sqrt(6 / input_nodes)`
    *   `b = sqrt(6 / input_nodes)`
    *   So, the range is `[-sqrt(6 / input_nodes), sqrt(6 / input_nodes)]`.