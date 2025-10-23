# CNN vs. ANN Operations

## Artificial Neural Network (ANN) Operations

*   **Structure**: Typically a multi-layer neural network, for example, with an input layer, one hidden layer, and an output layer.
*   **First Operation**: Inputs are multiplied by weights, and then a bias is added. This can be written as `w transpose x + bias`.
*   **Second Operation**: An activation function, such as ReLU (Rectified Linear Unit), is applied to the result.
*   **Learning Process**: The network performs forward propagation to calculate loss. Optimizers are then used to reduce this loss by updating the weights through backward propagation.

## Convolutional Neural Network (CNN) Operations

*   **Input**: Starts with an image.
*   **Filters (Kernels)**:
    *   Filters are crucial in CNNs, similar to how different layers in the visual cortex (V1, V2, V3, V4, V5) process visual information.
    *   **Role of Layers/Filters**:
        *   V1 layer: Finds edges.
        *   V2 layer: Finds color differences and patterns.
        *   V3, V4, V5 layers: Used for advanced tasks like image classification, object detection, or pattern recognition.
    *   **Types**: Filters can be of various sizes, such as 3x3 or 5x5.
    *   **Function**: Each filter performs a specific task, like identifying different patterns, shapes, or edges.
    *   **Initialization**: When training a CNN from scratch, these filters are initially assigned random values.
    *   **Learning**: Filter values are updated during the training process using forward and backward propagation.
*   **Convolution Operation**:
    *   Filters are placed on the image.
    *   Multiplication and addition operations occur between the filter and the image data.
    *   This process results in an output.
    *   The number of outputs depends on the number of filters used.
*   **ReLU Operation**:
    *   After the convolution operation, a ReLU operation is applied to the output values.
    *   **How ReLU Works**: It computes `max(0, x)`, meaning it outputs the input value `x` if `x` is positive, and 0 if `x` is negative.
    *   **Why ReLU is Used**:
        *   It helps in finding the derivative during backpropagation because ReLU's derivative is either 0 or 1.
        *   It prevents the vanishing gradient problem during backward propagation.
        *   This allows the filter values (parameters) to be effectively updated and learned, which is essential for efficient image processing.
        *   Other activation functions can also be used if their derivatives can be found.

## Key Differences and Similarities (ANN vs. CNN)

*   **ANN**: Takes inputs, multiplies by weights, and applies an activation function (e.g., ReLU).
*   **CNN**: Takes an image, applies filters (convolution operation), and then applies an activation function (e.g., ReLU) to the results.
*   **Commonality**: Both ANNs and CNNs use forward and backward propagation techniques to update their internal parameters (weights in ANNs, filter values in CNNs) to learn from the data.
*   **Goal**: The ultimate goal is to learn how to process images efficiently to get the correct output for tasks like image classification or object detection.