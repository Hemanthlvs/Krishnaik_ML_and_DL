# Forward Propagation in Simple Recurrent Neural Networks (RNNs)

## Preparing the Input Data

*   The example used is the sentence: "The food is good".
*   **Unique Words**: First, identify all unique words from the dataset. In the example, these are "the", "food", "good", "bad", "not" (total 5 unique words).
*   **Converting Words to Vectors (One-Hot Encoding)**:
    *   Words need to be converted into numerical vectors for the RNN to process them.
    *   **One-Hot Encoding** is a basic technique used.
    *   For each unique word, a vector is created where:
        *   A `1` is placed at the position corresponding to that word in the unique word list.
        *   All other positions in the vector are `0`.
    *   **Example Vectors (for 5 unique words)**:
        *   "the": ``
        *   "food": ``
        *   "good": ``
		*   "bad": ``
		*   "not": ``(Note: "is" is skipped as a stop word)
    *   These vectors will be the **inputs** to the RNN (5 inputs in this case).

## Simple RNN Architecture Overview

*   A basic RNN has three main layers: **Input Layer**, **Hidden Layer**, and **Output Layer**.
*   A key feature of RNNs is the **feedback loop** (or self-loop) from the hidden layer back to itself.
*   **Example Configuration**:
    *   **Input Neurons**: 5 (corresponding to the 5-dimensional one-hot encoded vectors).
    *   **Hidden Neurons**: 3 (chosen for this example).
    *   **Output Neurons**: Typically 1 for binary classification or more for multi-class.

## Forward Propagation Step-by-Step (with Time)

**Forward propagation** involves calculating the output for each word in the sequence, moving forward in time.

*   **Key Principle**: The hidden layer at any given time step receives not only the current word's input but also the **output (context) from the previous hidden state**. This allows the RNN to "remember" past information.

*   **Timestamp t=1 (Processing the first word, e.g., "The")**:
    *   **Input**: The vector for the first word (X11, e.g., ``) is fed into the input layer.
    *   **Calculation (O1)**:
        *   The input (X11) is multiplied by the input-to-hidden **weights (w)**.
        *   A **bias (b1)** is added.
        *   An **activation function (f)** is applied to the result.
        *   **Formula**: `O1 = f(X11 * w + b1)`.
    *   **Feedback**: The output `O1` is then sent back to the hidden layer for the next time step via a **feedback loop**.

*   **Timestamp t=2 (Processing the second word, e.g., "food")**:
    *   **Input**: The vector for the second word (X12) is fed in.
    *   **Calculation (O2)**:
        *   The current input (X12) is multiplied by input-to-hidden **weights (w)**.
        *   The **previous hidden state's output (O1)** is multiplied by separate hidden-to-hidden **weights (w_dash)**.
        *   A **bias (b1)** is added.
        *   An **activation function (f)** is applied.
        *   **Formula**: `O2 = f(X12 * w + O1 * w_dash + b1)`.
    *   **Context**: At this point, the hidden neurons for `t=2` have the context of the previous word ("The") due to `O1` being fed back.

*   **Timestamp t=3 (Processing the third word, e.g., "good")**:
    *   **Input**: The vector for the third word (X13) is fed in.
    *   **Calculation (O3)**:
        *   **Formula**: `O3 = f(X13 * w + O2 * w_dash + b1)`.
    *   This process continues for every word in the sentence.

## Output Layer and Prediction

*   After processing all words in the sentence, the final output of the hidden layer is passed to the **output layer**.
*   **Activation Functions for Output**:
    *   For **binary classification** problems (e.g., classifying text as positive/negative), a **sigmoid activation function** is typically used to produce an output between 0 and 1.
    *   For **multi-class classification** problems (e.g., classifying text into multiple categories), a **softmax activation function** is used to produce probabilities for each class.
*   The final output is called **y_hat** (the predicted output).

## Trainable Parameters (Weights and Biases)

*   The **weights** (w, w_dash) and **biases** (b1) are the parameters that the RNN learns during training.
*   **Number of Weights Calculation Example**:
    *   **Input to Hidden**: 5 inputs * 3 hidden neurons = **15 weights** (5x3 matrix).
    *   **Hidden to Hidden (Recurrent)**: 3 hidden neurons * 3 hidden neurons = **9 weights** (3x3 matrix).
    *   **Hidden to Output**: 3 hidden neurons * 1 output neuron (assuming binary classification) = **3 weights** (3x1 matrix).
    *   **Total Weights**: 15 + 9 + 3 = **27 weights**.
*   **Number of Biases Calculation Example**:
    *   **Hidden Layer Bias**: 3 biases (one for each hidden neuron).
    *   **Output Layer Bias**: 1 bias (for the output neuron).
    *   **Total Biases**: 3 + 1 = **4 biases**.
*   **Total Trainable Parameters**: 27 (weights) + 4 (biases) = **31 parameters**.
*   **Important**: During **forward propagation**, these weights are **not updated**; they are used to compute the output. Weight updates happen during **backward propagation** (backpropagation).