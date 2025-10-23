# LSTM RNN Training: Key Concepts & Example

## Training Data Example
The training process is explained using a text paragraph as an input and a binary output (1 for good, 0 for bad).
*   **Text Paragraph Example**: A review of a restaurant burger.
    *   "Hey, I went to the restaurant and ordered burger."
    *   "The burger looked tasty and crispy."
    *   "But burger is not good for health. It has a lot of fats, cholesterol."
    *   "But this burger was made with whey protein and only vegetables were used, so it was good."
*   **Output**: 1 (meaning the burger is good).
*   **Goal**: Predict whether the food (burger) is good or bad based on the text.

## Training Process Steps

### Step 1: Converting Words to Vectors (Embedding Layer)
*   **Every word** in the text paragraph must first be **converted into vectors**.
*   This process happens in the **embedding layer**.
*   **Word2Vec** is used to convert words into numerical vector representations.
    *   For this example, words are converted into **three-dimensional vectors**.
    *   These three dimensions are chosen to represent features like "good," "bad," and "healthy".
    *   **Example**: The word "tasty" might be converted to a vector like [0.9 (good), 0.0 (bad), 0.1 (healthy)].
	*	human does not explicitly choose or label what each individual dimension represents
    *   The values in these vectors **change based on the context** and relationship of the word to the features.

### Step 2: Passing Vectors Through LSTM Gates Over Time
*   Each word's vector (input `x_t`) is fed into the LSTM one at a time, along with the previous hidden state (`h_t-1`) and previous cell state (`c_t-1`).
*   **How Gates Work During Training (Illustrated with the Example)**:
    *   **Initial Input (e.g., "I went to restaurant and ordered burger")**:
        *   Initially, the **forget gate** might not forget much from previous memory if no new significant information has arrived yet.
    *   **Processing "tasty and crispy"**:
        *   When words like "tasty" and "crispy" come, the **input gate** and **candidate memory** add this positive information to the memory cell.
        *   The word vectors related to "good" will increase (e.g., good value becomes 0.9), while "bad" remains low (0.0), and "healthy" may have some initial value (e.g., 0.1). This information is added to the previous memory state.
    *   **Processing "not good for health"**:
        *   When this phrase appears, the word vectors change significantly. The "good" value may decrease (e.g., to 0.7), while the "bad" value increases (e.g., to 0.4) because the context shifts to negative aspects of health. The "healthy" value may also decrease (e.g., to 0.1).
        *   The **forget gate** will now start removing information related to "goodness" and the **input gate** will add information about "bad for health" to the memory cell.
    *   **Processing "fats and cholesterol"**:
        *   This further reinforces the negative aspect, causing the "good" value to decrease even more and the "bad" value to increase. The "healthy" value might become zero.
    *   **Processing "whey protein and only vegetables were used, so it was good"**:
        *   This sentence shifts the context back to positive. The "good" value will increase, the "bad" value will decrease, and the "healthy" value may become high (e.g., 0.9). The word vectors continuously change based on this new context.
        *   Based on these vector changes, the **forget gate** decides what to remove from memory (e.g., previous negative health info if it's no longer relevant), and the **input gate** decides what new positive information to add.
*   This continuous process of adding (input gate) and forgetting (forget gate) information, based on the evolving context of the text and changing word vectors, allows the LSTM to manage **long-term and short-term memory**.
*   **Forward propagation** (processing inputs) and **backward propagation** (updating weights) happen continuously as the vectors change, allowing the network to learn.
*   The **output gate** then uses the updated memory and hidden state to produce an output.
