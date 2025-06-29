# Variants of LSTM RNN: Peephole and Coupled Gates

## 1. Gers & Schmidhuber (Peephole Connections in LSTM RNN)

*   **Introduction Date**: This variant was introduced around the year 2000.
*   **Key Difference**: In addition to the standard forget gate, input gate, memory candidate, and output gate, this variant features **additional lines connected from the memory cell**.
*   **Connections**: These lines specifically connect the **memory cell (cell state CT-1 or CT) to the forget gate, the input gate, and the output gate**.
*   **Term**: These connections are called **"Peephole Connections"**.
*   **Function/Purpose**:
    *   Peephole connections mean that the **gate layers (forget, input, and output gates) are allowed to "look at the cell state"**.
    *   This provides additional context: For example, the forget gate can use the **previous information in the memory cell (previous context)** to decide what information to forget.
    *   **Improved Decision Making**: By looking at the cell state, the gates can make better decisions regarding:
        *   What to forget.
        *   What new information to add to the memory cell.
        *   What to output.
*   **Impact on Equations**: The previous cell state `CT-1` (or `CT` for the output gate) is added as an input term to the calculations for the forget gate (`f_t`), input gate (`i_t`), and output gate (`o_t`).

## 2. Coupled Forget and Input Gates LSTM RNN

*   **Key Characteristic**: This variant involves **coupling or combining the forget and input gates**.
*   **Difference from Standard LSTM**:
    *   In a standard LSTM, the decision to forget information (via the forget gate) and the decision to add new information (via the input gate) are made separately.
    *   In this coupled variant, **these decisions are made together**.
*   **Core Principle**: The central idea is:
    *   **"We only forget when we are going to input something in its place."**
    *   Alternatively: **"We only input new values to the state when we forget something older."**.
*   **Operation**:
    *   This implies a direct relationship between forgetting and adding. If there's nothing to remove from the memory cell, new information is not added.
    *   The calculation for updating the cell state often involves `1 - f_t` being multiplied by the new candidate memory, meaning that when `f_t` (forget gate output) is high (forgetting), `1 - f_t` is low (less new information added), and vice-versa. This ensures that new values are added **only when something is forgotten**.