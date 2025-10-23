# Decoder's Multi-Head Attention: Training Mechanism

## Key Components and Concepts

*   **Masked Multi-Head Attention**: This was discussed in a previous video, including different types and purposes of masking.
*   **Layer Normalization**: A layer normalization step occurs after masked multi-head attention, similar to the encoder. Another adding and normalization layer also happens after the encoder-decoder multi-head attention.
*   **Residual (Skip) Connections**: These connections are present, adding outputs to previous vectors to ensure more information is passed to the next layer.

## Encoder-Decoder Multi-Head Attention

*   **Also known as "Multi-head attention" or "Encoder and Decoder Multi-head Attention"**.
*   **Purpose**: This layer helps the decoder to **focus on appropriate places in the input sequence** during the training process.
*   **Input Vectors**:
    *   **Keys (K) and Values (V)**: These vectors are specifically taken from the **encoder output**. The output of the top encoder is transformed into a set of attention vectors K and V.
    *   **Query (Q)**: The query vector is generated from the **output of the masked multi-head attention layer** within the decoder.
*   **Internal Operations**: Inside the multi-head attention layer, self-attention calculations occur. This involves multiplying the query (Q) with keys (K), applying a softmax function, and then multiplying with values (V) to calculate scores. The K and V come from the encoder output, and the query comes from the decoder's masked multi-head attention output.

## Training Mechanism

The overall training mechanism involves using both the input (X) and output (Y) sequences.

1.  **Encoder Processing**: The encoder processes the entire input sequence (e.g., "je suis student"). From this, **key and value vectors (K and V)** for the encoder are derived and passed to the decoder.
2.  **Decoder Input - First Timestamp**:
    *   Initially, for the first decoding timestamp, a **start token** is provided as input to the decoder.
    *   This start token goes through embedding and positional encoding, then through the masked multi-head attention layer within the decoder.
    *   A **query vector (Q)** is generated for this start token.
    *   This query (Q) and the encoder's K and V are given to the **encoder-decoder multi-head attention layer**.
    *   Based on these, the first word of the output sequence (e.g., 'I') is predicted.
3.  **Decoder Input - Subsequent Timestamps**:
    *   For the second and subsequent timestamps, the **previously generated output word** (e.g., 'I' from timestamp one) is used as the **input to the decoder**.
    *   This previous output word goes through the same decoder steps (embedding, positional encoding, masked multi-head attention to generate Q).
    *   The newly generated Q, along with the original K and V from the encoder, are fed into the encoder-decoder multi-head attention layer to predict the next word.
    *   This process continues until the entire output sequence is generated.