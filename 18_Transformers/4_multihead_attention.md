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

### Feed-Forward Neural Network

*   **Generation of Multiple Vectors:** For every word, Multi-head Attention generates multiple "attention heads" or vectors. For example, if there are eight attention heads, you would get eight Z vectors (Z1, Z2, Z3, ..., Z8) for a single word. Each of these attention heads will have its own separate Q, K, and V vectors.
*   **The Challenge:** The subsequent Feed-Forward Neural Network (FFN), which processes these vectors, expects a single matrix as input, not multiple vectors.
*   **Combining Attention Heads:** To address this, all the multiple attention head vectors (e.g., Z0, Z1, Z2... Z7 for seven heads) are **concatenated** together.
*   **Creating a Single Output:** This concatenated matrix is then multiplied using a **dot product** with a new, initialized weight matrix (W0) specifically for the Feed-Forward Neural Network. This multiplication results in a single 'Z' vector or matrix.
*   **Passing to Feed-Forward Network:** This single 'Z' vector is then passed to the Feed-Forward Neural Network for further processing, including forward and backward propagation.
*   **Per Word Processing:** This entire process of generating multiple heads, combining them, and passing them to the FFN is performed for **each individual word** in the input (e.g., "thinking" or "machine").

### Purpose and Benefits of Multi-Head Attention

*   **Capturing Diverse Dependencies:** The main reason for having multiple attention heads is to **capture different aspects of importance or context dependency** among words.
*   **Different Contexts:** Each attention head focuses on and highlights different relationships or "importance" words within the sentence.
*   **Examples of Dependency:**
    *   In "cat sat on the mat," "cat" and "mat" are highly correlated, indicating a strong context dependency.
    *   In "The animal did cross the street because *it* was too tired," one attention head might show "it" dependent on "street," "tired," and "animal". Another head might show "it" dependent on "animal" and "cross".
*   **Comprehensive Understanding:** By getting information from multiple heads, the model can understand the dependencies between words more comprehensively.