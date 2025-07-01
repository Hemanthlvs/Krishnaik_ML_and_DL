# Attention Mechanism

## Problems with Traditional Encoder-Decoder Sequence-to-Sequence Architecture

*   **Problem:** For longer sentences or paragraphs, the single **context vector** created by the encoder is often not sufficient for the decoder to generate accurate output.
*   **Impact:** Performance metrics like the **Bleu score** decrease significantly as the sentence length increases when using the traditional architecture. The context vector struggles to capture the "essence" of the entire long sentence, especially information from earlier timestamps.

## Introduction to Attention Mechanism

*   **Main Idea:** To overcome the limitations of a single context vector, the attention mechanism provides **more context** to the decoder for both longer and shorter paragraphs.
*   **Key Research Paper:** This discussion is based on the research paper "Neural Machine Translation by Jointly Learning to Align and Translate," co-authored by **Yoshua Bengio**.
*   **Goal:** The attention mechanism aims to solve the problem of insufficient context by modifying the encoder-decoder architecture.

## Attention Mechanism Architecture (Key Changes)

The core idea is to provide more relevant context at each decoding step.

*   **Encoder Changes:**
    *   Uses a **Bidirectional LSTM (Bi-LSTM)** or Bidirectional RNN instead of a simple LSTM.
    *   **Purpose of Bi-LSTM:** It processes the input sequence in both forward (H1, H2, H3...) and reverse (H3, H2, H1...) directions, allowing the model to capture context from both preceding and succeeding words in the input sentence.
    *   Instead of just a single context vector, the attention encoder **outputs individual hidden states (H1, H2, H3, etc.)** for each time step. These outputs are now utilized.

*   **Context Vector Calculation in Attention (The "Alignment" Process):**
    *   The attention mechanism calculates a **new context vector (CT)** for *each time step* of the decoder. This is the fundamental difference.
    *   **Steps to calculate CT:**
        1.  **Alignment Scores (Eij / E11, E12, E13):**
            *   For each decoder hidden state (e.g., S0 for the first prediction), it is combined with *every* hidden state (H1, H2, H3) from the encoder.
            *   This combination is then passed through a **feed-forward Artificial Neural Network (ANN)**.
            *   The output of this ANN is then passed through a **softmax activation function**.
            *   These softmax outputs are called **alignment scores (A11, A12, A13)** or attention weights. They indicate "how much context of each encoder hidden state (H1, H2, H3) should be considered" for the current decoder step.
        2.  **Point-wise Multiplication:** Each alignment score (Aij) is point-wise multiplied with its corresponding encoder hidden state (Hj).
        3.  **Summation for Context Vector (CT):** All the results from the point-wise multiplications are summed together to compute the **context vector (CT)** for that specific decoder time step. The formula is `CT = Σ (A_t_i * H_i)`.

*   **Decoder with Attention:**
    *   **First Decoder Step (S1):** Takes S0 (encoder's final hidden state), the newly calculated **C1** (context vector specific to this step), and Y0 (initial input) to predict Y1 hat.
    *   **Subsequent Decoder Steps (S2, S3, etc.):**
        *   Instead of using the initial S0, the **hidden state from the *previous* decoder step (S1, S2, etc.)** is used to generate a *new* context vector (C2, C3).
        *   This new context vector (C2, C3) is then passed to the next LSTM along with the previously predicted word (Y1 hat, Y2 hat) to predict the next word (Y2 hat, Y3 hat).
    *   This iterative calculation of a new, relevant context vector for every prediction is what makes attention powerful.

## Advantages and Importance of Attention Mechanism

*   **Improved Accuracy for Long Sentences:** The Bleu score remains **almost constant** regardless of the sentence length, indicating that attention mechanisms effectively address the long-sentence problem of traditional models.
*   **Dynamic Context:** By calculating a new context vector for every timestamp in the decoder, the model can focus on the most relevant parts of the input sentence for each output word, providing **more precise context**.
*   **Foundation for Modern AI:** The attention mechanism is the **base of Transformers** and is crucial for many modern **Generative AI models**.


- link for reference: [Attention mechanism architecture understanding](https://erdem.pl/2021/05/introduction-to-attention-mechanism)