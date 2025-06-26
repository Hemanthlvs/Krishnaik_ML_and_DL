Recurrent Neural Networks

## Sentiment Analysis
*   **Example Dataset**:
    *   "The food is good" -> Output: 1 (good)
    *   "The food is bad" -> Output: 0 (bad)
    *   "The food is not good" -> Output: 0 (bad)

## Using Artificial Neural Networks (ANN) for Sentiment Analysis
*   **First Step: Text Pre-processing**
    *   Text needs to be converted into **vectors**.
    *   Various methods exist: Bag of Words, One-Hot Encoding, TF-IDF.
*   **Example using Bag of Words**:
    *   **Vocabulary**: Unique words after removing "stop words" like "is" and "the". For the example sentences, unique words are: "food", "good", "bad", "not". So, **vocabulary size is 4**.
    *   **Vector Conversion**: Each sentence is converted into a vector based on the presence of words in the vocabulary.
        *   "food good bad not" (vocabulary order)
        *   Sentence 1 ("The food is good"): **** (food, good are present)
        *   Sentence 2 ("The food is bad"): **** (food, bad are present)
        *   Sentence 3 ("The food is not good"): **** (food, good, not are present)
    *   This method results in a **fixed vector size** for inputs.
*   **ANN Architecture**:
    *   Inputs (the converted vectors) go into the input layer.
    *   Example ANN: 4 input neurons (for the 4-word vector), 3 hidden neurons, 1 output neuron.
    *   Input layer connects to all hidden neurons, hidden neurons connect to the output layer.

## Problems with using ANN for Sequential Data (like Text)
*   **Problem 1: Loss of Sequence Information/Context**
    *   In Bag of Words, words are represented by frequency, not their order.
    *   The converted vectors do not preserve the original word sequence.
    *   **Losing sequence means losing the meaning and context of the sentence**.
    *   This issue persists even with other techniques like TF-IDF or Word2Vec, as they don't inherently capture sequence information in their basic form.
*   **Problem 2: Processing all words at once**
    *   ANNNs take the **entire input sentence (as a vector) all at once**.
    *   For sequential data, it's better to process **one word at a time based on a timestamp**.
    *   **Analogy: Google Translation**: When you type a word, it translates it immediately; as you add more words, the translation updates sequentially. ANNs cannot do this.
    *   This "all at once" input prevents the neural network from efficiently learning from sequential data.

*   **Conclusion**: Due to these two major problems (loss of sequence and "all at once" input), ANNs cannot be directly and efficiently used for sequential data like text.

## Introduction to Recurrent Neural Networks (RNN)
*   A new type of neural network, **RNN (Recurrent Neural Network)**, was proposed to solve the problems of ANNs with sequential data.
*   **RNNs are specifically suitable for sequential data**.

## How RNN Architecture Differs from ANN
*   **Basic ANN Structure**: Input Layer -> Hidden Layer(s) -> Output Layer.
*   **Key Difference in RNN: The Feedback Loop**
    *   In an RNN, the output from a hidden layer neuron is **fed back to itself and to all other neurons in the same hidden layer**.
    *   This feedback loop allows the network to maintain information (or "memory") from previous steps.
    *   When an input is processed, the output of the hidden layer, after activation, is shared with other hidden neurons.

## How RNN Processes Sequential Data
*   **Timestamp-based Input**: Unlike ANNs, RNNs process **one word at a time, at each timestamp**.
    *   Example: For "The food is good"
        *   `t=1`: Pass "The" (X11 - first sentence, first word).
        *   `t=2`: Pass "food" (X12 - first sentence, second word).
        *   `t=3`: Pass "is" (X13 - first sentence, third word).
        *   `t=4`: Pass "good" (X14 - first sentence, fourth word).
*   **Context Retention**: When a new word (e.g., "food" at t=2) is passed, the **RNN already has the context (information) from the previous word** ("The" from t=1) because of the feedback loop.
    *   This means the **previous context information is retained by the RNN**, solving the loss of sequence problem.