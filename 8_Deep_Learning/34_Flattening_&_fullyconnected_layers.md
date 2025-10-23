# Convolutional Neural Networks (CNNs) - Core Concepts

## Introduction and Goal
*   CNNs are used to classify handwritten digits from the MNIST dataset.
*   The MNIST dataset contains images of digits from 0 to 9.
*   The goal is to predict which digit an image represents (e.g., 2, 4, 5, 0, or 9).

## Input Data
*   The input images are grayscale.
*   An example input size is 28x28x1.
*   The '1' in 28x28x1 indicates it's a grayscale image.

## Convolution Operation (First Layer)
*   The first operation is the convolution operation.
*   A "kernel" or "filter" is applied to the image.
*   **Filter Size:** For example, a 5x5 filter.
*   **Output Size Calculation (Valid Padding):**
    *   When "valid padding" is used, no extra padding is applied.
    *   The formula for the output size is `(N - F + 1)`.
    *   `N` is the input size (e.g., 28), and `F` is the filter size (e.g., 5).
    *   For a 28x28 input with a 5x5 filter, the output becomes 24x24 (28 - 5 + 1 = 24).
*   **Number of Filters:** `N1` indicates how many filters are used (e.g., 10 or 15 filters).
*   **ReLU Operation:** After the convolution, a ReLU (Rectified Linear Unit) operation is applied.

## Max Pooling Layer
*   After the convolution and ReLU, a max pooling layer is often applied.
*   **Purpose:** Max pooling decreases the image size and helps gather information about the most intense parts of the image.
*   **Filter Size:** Typically uses a 2x2 filter.
*   **Effect on Image Size:** A 2x2 max pooling filter divides the pixel dimensions by two.
    *   For example, a 24x24 output from convolution would become 12x12 after 2x2 max pooling.
*   **Channels:** The number of channels (`N1`) remains the same after max pooling because it's applied to every output from the filter.

## Combining Layers
*   A common structure is a combination of a convolution layer followed by a max pooling layer.
*   This combination can be repeated multiple times (e.g., another convolution and max pooling layer).
*   Example: 12x12 output after first pooling, then applying another 5x5 convolution results in 8x8 (12 - 5 + 1 = 8).
*   Another max pooling on 8x8 results in 4x4 (8 / 2 = 4).

## Flattening Layer
*   After multiple convolution and max pooling operations, a "flattening layer" is used.
*   **Purpose:** It converts the 2D or 3D output into a single, elongated 1D array or vector.
*   **How it works:** All the outputs from the previous layers are stacked one after another into a straight line.

## Fully Connected Layer
*   After flattening, the data is passed to a "fully connected layer".
*   **Concept:** This is similar to a standard Artificial Neural Network (ANN).
*   **Structure:** It consists of multiple neurons in hidden layers, where every neuron is connected to every neuron in the next layer.

## Output Layer
*   The final layer is a "dense output layer".
*   **Number of Outputs:** For the MNIST dataset (digits 0-9), there are 9 outputs.
*   All neurons in the final hidden layer are interconnected to these output neurons.
*   This layer makes the final prediction.

## Training Process
*   The CNN trains by performing "forward propagation" (making a prediction) and "backward propagation" (adjusting weights).
*   **Backpropagation:** Updates the values of the filters and convolution weights.
*   **Loss Function:** The main goal is to reduce the "loss function".
*   **Optimizers:** Optimizers like Adam are used during backpropagation to update weights.
*   ReLU activation helps in performing backpropagation.