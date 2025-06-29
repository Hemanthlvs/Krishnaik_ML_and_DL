# Gated Recurrent Units (GRU): An LSTM Alternative

## Introduction
*   **GRU (Gated Recurrent Unit)** is a variant of the **LSTM RNN** (Long Short-Term Memory Recurrent Neural Network).
*   It was introduced by **Cho et al. in 2014**.
*   The GRU architecture aims to address some of the complexities of LSTM RNNs.

## Limitations of LSTM RNN
*   **Complex Architecture**: LSTM RNNs are considered quite complex due to the use of **three gates**:
    *   Forget gate
    *   Input gate
    *   Output gate
    *   In addition to these, they also have a candidate memory.
*   **Separate Memory Cells**: LSTMs use separate memory cells for:
    *   **Long-term memory (Cell State, C_t)**
    *   **Short-term memory (Hidden State, H_t)**
*   **High Number of Trainable Parameters**:
    *   Each gate in LSTM requires its own set of **weights** (e.g., W_f, W_i, W_o) and biases.
    *   This leads to a **significant increase in trainable parameters** as the input and hidden layer dimensions grow.
*   **Increased Training Time**: A higher number of trainable parameters directly results in **more training time**.
*   **Despite Complexity**: LSTM RNNs are effective at solving **long-term dependency** problems.

## GRU Architecture and Components
*   GRU simplifies the architecture by **combining the two memory cells** (long-term and short-term) into a single hidden state.
    *   This single cell (hidden state) acts as **both long-term and short-term memory**.
*   GRU uses **fewer gates** compared to LSTM. The primary gates in GRU are:

### 1. Update Gate (Z_t)
*   **Purpose**: The update gate decides **what context information needs to be added** to the current memory. It determines how much of the previous hidden state (H_t-1) to carry forward and how much of the new candidate hidden state (H_dash_t) to include.
*   **Calculation**:
    *   `Z_t = Sigmoid(W_z * [H_t-1, X_t])`
    *   Where:
        *   `H_t-1` is the previous hidden state.
        *   `X_t` is the current input.
        *   `W_z` are the weights associated with the update gate.
        *   `Sigmoid` is the activation function.
*   **Coupled Mechanism**: The update gate works in a **coupled way** with the candidate hidden state to decide the final hidden state.

### 2. Reset Gate (R_t)
*   **Purpose**: The reset gate is responsible for **resetting or forgetting some information** from the previous memory cell (H_t-1). This resetting is **context-dependent**, based on the new input (X_t).
*   **Calculation**:
    *   `R_t = Sigmoid(W_r * [H_t-1, X_t])`
    *   Where:
        *   `H_t-1` is the previous hidden state.
        *   `X_t` is the current input.
        *   `W_r` are the weights associated with the reset gate.
        *   `Sigmoid` is the activation function.
*   **Mechanism of Resetting**: Resetting is typically achieved through **point-wise multiplication**. If `R_t` values are low (e.g., 0.2), they reduce the contribution of corresponding values from `H_t-1`, effectively "forgetting" them.

### 3. Temporary/Candidate Hidden State (H_dash_t or H_hat_t)
*   **Purpose**: This state represents the **current context** based on the new input and the "reset" version of the previous hidden state.
*   **Calculation**:
    *   First, `R_t` performs a **point-wise operation (multiplication)** with `H_t-1`. This effectively applies the reset mechanism.
    *   This result is then combined with `X_t`.
    *   The combined input is passed through a **tanh activation function** to produce `H_dash_t`.
    *   `H_dash_t = Tanh(W * [R_t * H_t-1, X_t])` (Implicit from)

### 4. Final Hidden State (H_t)
*   **Purpose**: This is the final memory cell for both long-term and short-term memory, updated based on the reset gate, update gate, and temporary hidden state.
*   **Calculation**: `H_t` is calculated by combining information from the previous hidden state (`H_t-1`) and the temporary hidden state (`H_dash_t`), weighted by the update gate (`Z_t`).
    *   `H_t = (1 - Z_t) * H_t-1 + Z_t * H_dash_t`
    *   This equation shows how:
        *   `(1 - Z_t) * H_t-1` retains information from the previous state.
        *   `Z_t * H_dash_t` incorporates the new candidate information.
    *   The more context (from `H_dash_t`) is included, the less context from the previous state (`H_t-1`) is included, and vice-versa, demonstrating a **coupled mechanism**.

## Advantages of GRU over LSTM
*   **Simpler Architecture**: GRU has fewer gates (two: update and reset) compared to LSTM (three: forget, input, output).
*   **Fewer Trainable Parameters**: As a result of fewer gates and a combined memory cell, GRU has **lesser number of weights** and biases, leading to fewer trainable parameters.
*   **Better Optimization and Faster Training**: With fewer trainable parameters, the training process for GRU is generally **more efficient and faster** when compared to LSTM RNN.
