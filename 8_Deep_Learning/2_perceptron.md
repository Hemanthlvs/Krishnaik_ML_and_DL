# Perceptron: A Single Layer Neural Network

A perceptron is a **basic unit of a neural network**, often referred to as a **single layer neural network**.

## Purpose
- The main use of a perceptron is for **binary classification problems**.
- **Example**: Predicting whether a student will pass or fail based on their IQ and study hours.

## Architecture
- A perceptron consists of:
  - An **input layer** (the number of inputs equals the number of features).
  - A **single hidden layer** that contains **one neuron**.

## Components & Processing within the Neuron
- **Inputs (x)**: These are the features taken from the dataset.
- **Weights (W)**: Parameters linked to the inputs, usually initialized randomly. **Weights are crucial** in processing signals and are **trained** to perform specific tasks. They need to be updated if the error is high.
- **Bias (b)**: An additional parameter that prevents the output from becoming zero if all weights are zero. It acts like **noise** to help create a more generalized model, similar to the intercept in linear regression.
- **Processing Steps**:
  1. **Calculate z**: This is the sum of (inputs * weights) plus the bias. The formula is `z = Σ(xi * Wi) + b`. This step helps solve **linear problems**.
  2. **Apply Activation Function**: This function transforms the z value to produce an output suitable for binary classification (e.g., **0 or 1**). Common activation functions include:
     - **Step Function**: If z ≤ 0, the output is 0; if z > 0, the output is 1 (threshold is 0).
     - **Sigmoid Function**: This function transforms the output to be between 0 and 1. If z > 0.5, the output is 1; if z ≤ 0.5, the output is 0 (threshold is 0.5).

## Training
- The perceptron's output is compared to the actual output to determine the **error** (also known as the **loss function** or **cost function**).
- If the error is significant, the **weights are updated** to minimize the error.
- This training process continues until the weights are optimized for better accuracy.

## Capabilities & Limitations
- A perceptron can create a **linear boundary** to separate two classes.
- It functions as a **linear classifier** and finds the **best fit line** for the data.
- However, a single perceptron may **struggle with complex problems**, which is why multi-layer neural networks are often needed for more intricate tasks.

# Single-Layer vs. Multi-Layer Perceptron Models

## Single-Layer Perceptron Model

*   **Process:** Inputs are passed, weights are assigned (can be random). Two steps are performed: summation of inputs with weights plus bias, and applying an activation function.
*   **Output:** Typically binary (1 or 0) based on whether the result exceeds a threshold.
*   **Feed Forward:** The process from input to output (steps 1 and 2) is called **feed forward neural network** operations.
*   **Error Handling:** If the output doesn't match the real output, weights are changed (sometimes randomly if error is high), and the feed-forward process is repeated. This weight update technique is **not very efficient**.
*   **Advantages:** Easily solves **linear separable problems**. Good for **binary classification** when data is linearly separable. Linearly separable means data can be split by a single line.
*   **Disadvantages:** Cannot solve **non-linear separable problems**. These require more than a single line to classify data. The weight update method is **not efficient**.

## Multi-Layer Perceptron Model

*   Also called a **Multilayer Neural Network** or **Artificial Neural Network (ANN)**.
*   Needed to solve **complex, non-linear separable problems** that single-layer perceptrons cannot handle.
*   Uses more efficient techniques for weight updates and problem solving.
*   Key techniques covered:
    *   **Forward Propagation**.
    *   **Backward Propagation** (a significant invention for seamless weight updates).
    *   **Loss Functions**.
    *   **Optimizers** (provides a mechanism for updating weights).
    *   Various **activation functions** etc..,