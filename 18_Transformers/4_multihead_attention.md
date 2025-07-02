### Self-Attention Recap

*   **Self-attention** is a process that helps a model understand the context and dependencies of words within a sentence.
*   **Steps of Self-Attention**:
    1.  **Calculate Query, Key, and Value Vectors**: These are derived from learned weights (Wq, Wk, Wv). For each word, you get separate Query, Key, and Value vectors.
    2.  **Calculate Attention Score**: This is done by multiplying the Query and Key vectors.
    3.  **Scale Scores**: Divide the attention scores by the square root of the dimension of the key vectors (root of d_k).
    4.  **Apply Softmax**: A softmax activation function is applied to the scaled scores.
    5.  **Calculate Weighted Sum of Values**: Multiply the result from softmax with the Value vector.
*   The final output (called 'z value' or **attention head**) is a **contextual vector** for the word, reflecting its dependencies on other words in the sentence.

### Multi-Head Attention

*   **Core Idea**: Multi-head attention means having **multiple self-attention "heads"**. Instead of getting just one attention head (or contextual vector), you get multiple ones.
*   **How it Works**:
    *   For the same input words, **multiple attention heads** are created.
    *   Each head uses its **own distinct set of learned weights** (e.g., W0q, W0k, W0v for one head; W1q, W1k, W1v for another).
    *   Each set of weights projects the input into a **different "representation subspace"**.
    *   As a result, each attention head (e.g., Z0, Z1) captures **different contextual importance** or dependencies from the input words. For example, Z0 might focus more on "sat," while Z1 might focus more on "mat" in "the cat sat mat".
*   **Purpose and Benefits**:
    *   It **expands the model's ability to focus on different positions** of words or tokens.
    *   It provides **multiple "representation subspaces"**.
    *   By combining insights from different heads, the model gets **more comprehensive information**.
    *   Each head can highlight different aspects of the token's relationship with other tokens in the sentence.
*   **Output**: After performing multi-head attention, you get **multiple attention heads (vectors)** for each word.
*   **Next Step (for subsequent processing)**: These multiple output vectors from the different attention heads need to be combined before being passed to a feedforward neural network.