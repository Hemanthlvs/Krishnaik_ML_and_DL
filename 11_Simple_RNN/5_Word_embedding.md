## Word Embedding: From One-Hot to Feature Representation

### What is Word Embedding?
*   **Word embedding** is a technique that **converts words into vectors**.
*   In a neural network, this is typically used as an **embedding layer**, similar to a dense layer.
*   The main goal of the embedding layer is to take text input and convert it into vectors using a word embedding technique.
*   Word embedding is also called **feature representation**.

### Initial Technique: One-Hot Encoding
*   Before word embedding, **one-hot encoding** was commonly used to represent words.
*   **How it works:**
    *   First, a **vocabulary size** is defined, which is the total number of unique words in your data (e.g., 10,000 words).
    *   Each word is converted into a **vector with the same number of dimensions as the vocabulary size** (e.g., a 10,000-dimension vector for a 10,000-word vocabulary).
    *   In this vector, the position corresponding to the word's index in the vocabulary is marked with a **'1'**, and **all other positions are '0'**.
    *   For example, if "man" is at index 5000, its vector will have '1' at the 5000th position and '0' everywhere else.
*   **Disadvantages of One-Hot Encoding:**
    *   It creates a **sparse matrix** because most values in the vector are zeros.
    *   Sparse matrices can lead to **overfitting** in neural networks because there isn't much variation in values (just zeros and ones).
    *   It is **not an efficient technique** due to the large number of zeros, especially with a large vocabulary.

### Introducing Word Embedding (to overcome One-Hot Encoding's issues)
*   Word embedding was developed to **overcome the disadvantages of one-hot encoding**.
*   **Word2Vec** is a popular type of word embedding technique. (It's recommended to understand Word2Vec training, including Skip-gram and CBOW models, which involve forward and backward propagation).
*   **What Word Embedding (Feature Representation) Does:**
    *   It **creates a feature representation for every word** in the dataset.
    *   Instead of just 0s and 1s, it represents each word as a vector (e.g., 300 dimensions).
    *   These vectors capture **relationships between words based on various features**.
    *   **Example Features:** The text gives examples like "gender," "Royal," "age," and "food".
    *   **How Relationships are Represented:** Each word gets a numerical value for each feature, indicating its relationship. For example:
        *   "Boy" to "gender" might be -1, while "girl" to "gender" is +1, showing they are opposites.
        *   "King" to "Royal" might be 0.95 (strong relationship), while "Apple" to "gender" might be 0.01 (weak or no relationship).
    *   These **relationship values form the vector** for each word.
*   **Key Parameters for Word Embedding:**
    *   **Vocabulary size:** The total number of unique words (e.g., 10,000).
    *   **Features dimension:** The number of dimensions in which each word will be represented (e.g., **300 dimensions**, commonly used in techniques like Google's Word2Vec and GloVe).
*   **Role in Neural Networks:** Once words are converted into these feature vectors by the embedding layer, they are then fed into neural network models like Simple RNNs for training.