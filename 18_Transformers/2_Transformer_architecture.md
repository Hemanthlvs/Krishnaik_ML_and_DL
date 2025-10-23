# Transformer Architecture 

## Introduction to Transformers

*   **Purpose**: Transformers are used to solve **sequence-to-sequence tasks**.
*   **Example Task**: Language translation, such as translating an English sentence to a French sentence.
*   **Basic Idea**: An input (e.g., English sentence) is given, and the Transformer converts it into an output (e.g., French sentence).

## Overall Architecture: Encoder-Decoder Model

*   The Transformer follows an **encoder-decoder architecture**.
*   **Multiple Layers**:
    *   It contains **multiple encoders**.
    *   It also contains **multiple decoders**.
    *   Information flows from one encoder to the next (bottom to top), and then from the entire encoder stack to the decoder stack.
*   **Information Flow**:
    *   Encoder passes information to the decoder.
    *   The decoder then produces the final output.

## Inside a Single Encoder

Each encoder block consists of two main layers:
*   **Self-Attention Layer**.
*   **Feed Forward Neural Network (FFNN) Layer**.

### Input and Vector Conversion

*   The input words (e.g., "How are you?") are first converted into **vectors**.
*   This conversion is done using an **embedding layer**, which turns each word into a numerical vector representation.

### The Role of Self-Attention

*   **Conversion to Contextual Vectors**: The self-attention layer takes the initial word vectors and transforms them into **contextual vectors**.
*   **What are Contextual Vectors?**:
    *   Unlike the initial fixed vectors, contextual vectors are defined based on the **context of other words** in the sentence.
    *   For example, the contextual vector for "How" will consider the context of "are" and "you".
*   **Why are Contextual Vectors Important?**:
    *   They provide a "proper context" for the words being processed.
    *   This helps in achieving **amazing accuracy**, especially for longer sentences.
*   **Parallel Processing**: A key advantage of self-attention is that **all words are processed in parallel**.
    *   This is a departure from traditional models like LSTM or RNN, which process words one by one.
    *   Parallel processing makes the entire Transformer architecture **scalable**.

### Feed Forward Neural Network

*   After self-attention generates contextual vectors (e.g., z1, z2, z3), these vectors are passed to the **Feed Forward Neural Network**.
*   The output from the FFNN is then passed to the **next encoder** in the stack.

## Inside a Single Decoder

Each decoder block also contains:
*   A **Self-Attention layer**.
*   A **Feed Forward Neural Network layer**.
*   **Crucially, an additional layer called Encoder-Decoder Attention**.