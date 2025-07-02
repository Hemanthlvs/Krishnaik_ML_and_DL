# Transformers: Layer Normalization

## Position of "Add & Normalize" in Transformer Architecture
*   In the Transformer's architecture, after input embeddings are added with positional encoding, they go to **Multi-head attention**.
*   The **next step** after Multi-head attention is called "**Add and Normalize**".
*   This is where **layer normalization** happens.

## General Concept of Normalization
*   **Normalization** in deep learning is used in two main ways: **batch normalization** and **layer normalization**.
*   **Purpose:** To transform input features or neuron outputs to a standard scale or distribution.

### Example of Input Normalization (Standard Scaling)
*   **Scenario:** Predicting house price based on features like house size (F1) and number of rooms (F2).
*   **Standard Scaling (Z-score normalization):** For each feature (column), it subtracts the mean and divides by the standard deviation.
*   **Result:** The feature's distribution will have a **mean of zero and a standard deviation of one**.
*   **Min-Max Scaler:** Another scaling technique, often used for image data (0-255 pixels), which scales values between 0 and 1.

### Advantages of Normalization/Scaling
1.  **Improved Training Stability:**
    *   Data distributions are centered near zero, preventing issues from diverse input distributions.
    *   Helps **prevent vanishing and exploding gradient problems** during backpropagation.
2.  **Faster Convergence:**
    *   Because values are centered, the initial loss can be smaller, leading to faster movement towards the global minimum.
    *   Enables **stable updates** during backpropagation.

## Batch Normalization
*   **Problem:** After initial input normalization, subsequent multiplications with weights and biases within the neural network can **change the distribution** of outputs (e.g., Z1, Z2 from a hidden layer).
*   **Solution:** **Batch normalization** performs normalization on the outputs of these hidden layers (e.g., Z1 and Z2).
*   **How it works:** It computes the mean and standard deviation for *each neuron's output* across the entire batch of training samples. Then, the Z-score formula is applied to normalize these outputs.
*   **Goal:** To maintain a distribution with a mean of zero and standard deviation of one for these intermediate outputs, making them similar to the input features' distribution.

## Batch Normalization vs. Layer Normalization
*   **Batch Normalization (Column-wise):** Normalizes by taking the **entire batch's values for a specific feature/neuron output** (e.g., all Z1 values in a batch are normalized together, then all Z2 values).
*   **Layer Normalization (Row-wise):** Normalizes by taking **layer by layer** (or sample by sample). For a single input sample, it normalizes all the neuron outputs *within that hidden layer*.

### Why Layer Normalization in Transformers?
*   Batch normalization can be problematic if many values are zero, as it can still impact the overall distribution.
*   **Layer normalization** is preferred in Transformers because it handles **each word (or token combination) individually**.
*   If values are zero for a specific layer in layer normalization, their mean and standard deviation would also be zero, meaning **no significant change** to their values, which is beneficial for contextual embeddings. This is the **most important difference**.

## Learnable Parameters: Gamma ($\gamma$) and Beta ($\beta$)
*   These are two **learnable parameters** that are used during model training.
*   They are also called **scale and shift parameters**.
*   **Purpose:** They allow the model to **decide whether to normalize or not**, or how much to normalize, for a given problem statement.
*   If the model determines that the current distribution of Z1 or Z2 is already optimal for prediction and doesn't require normalization, gamma and beta can adjust the normalized output to effectively "undo" or modify the normalization.
*   **Formula:** The normalized output `y` is calculated as `gamma * (Z_normalized) + beta`.
*   **Initial values:** Gamma is often initialized to 1.0, and Beta to 0.0, as observed in research papers.

## Add & Normalize in Transformer
*   After the Multi-head attention output, it is **added with the "residual" `x_dash`** (which comes from input embedding + positional encoding).
*   **Then, layer normalization is applied** to this combined result.

## Simple Problem Example (to be discussed later)
*   An example will be used with a "Cat" token embedding: `[2.0, 4.0, 6.0, 8.0]`.
*   Initial `gamma = [1.0, 1.0, 1.0, 1.0]` and `beta = [0.0, 0.0, 0.0, 0.0]`.
*   The goal is to show how a single vector gets normalized.
