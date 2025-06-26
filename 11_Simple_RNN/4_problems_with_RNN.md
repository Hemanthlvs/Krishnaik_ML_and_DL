# RNN Problems: The Vanishing Gradient Problem

## The Problem with RNNs: Vanishing Gradient

The primary problem discussed is the **Vanishing Gradient Problem**. This issue arises particularly with **long-term dependencies** in data.

### Short-Term vs. Long-Term Dependencies

*   **Short-term dependencies** occur in smaller sentences (e.g., "The food is good" - 4 words). Here, predicting the next word or understanding the sentiment relies on context from nearby words. Simple RNNs can handle these.
*   **Long-term dependencies** occur in much longer sentences (e.g., 50-100 words). The final output or a word later in the sentence might depend on a word that appeared very early in the sequence.
    *   **Simple RNNs struggle to capture long-term dependencies** and thus cannot provide good accuracy in such cases.

### Why Gradients Vanish (The Mathematical Explanation)

The core of the vanishing gradient problem lies in **how weights are updated** during backpropagation, especially for words that appeared early in a long sequence.

*   **Weight Update Formula**: New weight (`w_new`) = Old weight (`w_old`) - (learning rate * derivative of loss with respect to `w_old`). The crucial part is calculating this **derivative**.
*   **Chain Rule in Backpropagation**: When updating weights (e.g., `w_h` for the first word at `t=1`) in a long sentence (e.g., 50 words), the **chain rule** of derivatives is applied across many time steps.
    *   This involves multiplying many derivative terms, such as `d(Output_t) / d(Output_t-1)`.
*   **Sigmoid Activation Function's Role**: If a **sigmoid activation function** is used in the hidden layers, its **derivative ranges from 0 to 0.25**.
    *   When many small decimal values (like 0 to 0.25) are **multiplied together** repeatedly in the chain rule (especially for early time steps), the resulting gradient becomes **extremely small, approximately equal to zero**.
*   **Impact on Early Words**: Because the gradient (which determines how much a weight changes) becomes near zero for early words, these words **do not significantly participate in updating the weights**.
    *   This means the information from the first words in a long sentence has **very little impact** on the final output prediction.
*   **Impact on Nearest Words**: In contrast, words closer to the current time step (the "nearest words") have shorter chain rules for their gradients. Their gradients **do not vanish** and thus **play a very important role** in updating weights and predicting the output.
*   This inability of simple RNNs to remember and use information from far-off past time steps (due to vanishing gradients) is known as the **Vanishing Gradient Problem**.

## Solutions to Vanishing Gradient

*   **Activation Function Change**: One approach is to use different activation functions like **tanh** (derivative 0 to 1) or **ReLU/Leaky ReLU** (derivative near 1) instead of sigmoid. While these can help, the problem might still persist with very long sequences.
*   **Advanced RNN Architectures**: The most significant solutions are new neural network architectures specifically designed to address this problem:
    *   **LSTM RNN** (Long Short-Term Memory RNN).
    *   **GRU RNN** (Gated Recurrent Unit RNN).
*   **Both LSTM and GRU RNNs are built to solve the problems faced by simple RNNs**, particularly the vanishing gradient problem and the inability to capture long-term dependencies.