# Encoder-Decoder or Sequence to Sequence Architecture for Sequence Models

## Issues with Traditional RNNs

*   **Simple RNN Problems**:
    *   The primary issue is the **vanishing gradient problem**.
    *   This problem makes simple RNNs less effective for capturing long-term dependencies in sequential data.
*   **LSTM & GRU RNNs**:
    *   These variants were developed to address the vanishing gradient problem.
    *   They incorporate **long short-term memories** (long-term and short-term memory cells).
    *   Efficient for "many-to-one" RNN tasks like sentiment analysis or predicting the next word.
*   **Bidirectional RNN**:
    *   Used when predictions depend on future words or require context from upcoming words.

## Introduction to Many-to-Many RNN & Sequence-to-Sequence Models

*   **Definition of Many-to-Many RNN**: It involves **multiple inputs and multiple outputs**.
*   **Sequence-to-Sequence Neural Networks**: This is another name for models that handle many-to-many problems, particularly when **both the input and output are sequential data**.
*   **Why New Architecture?**: Simple RNN, LSTM, GRU, or even Bidirectional RNN are **not efficient enough** for sequence-to-sequence problems where input and output are both sequential, as they don't provide good accuracy in such scenarios.
*   **Common Use Cases**:
    *   **Machine Language Translation**: Converting a sentence from one language (e.g., English) to another (e.g., French).
    *   **Text Generation/Suggestion**: Like the suggestions you get in a LinkedIn chatbot (e.g., suggesting a response like "I'm good," or "Okay. Thanks.").

## Encoder-Decoder Architecture

The Encoder-Decoder is a new architecture specifically designed to solve sequence-to-sequence problems.

### Components

It consists of two main blocks:
1.  **Encoder Block**.
2.  **Decoder Block**.

### Simple Working Principle

*   **Encoder's Role**:
    *   Takes the **input sentence**.
    *   Applies an **embedding layer** to convert words into numerical arrays (embeddings).
    *   Generates a **hidden state**, which is also called a **context vector**.
    *   The **context vector** captures the **entire information, summary, or context of the input sentence** in vector form.
*   **Decoder's Role**:
    *   Receives the **context vector** from the encoder.
    *   Its main aim is to **generate the output word by word**.
    *   It **feeds the previously generated word back into itself** to generate the next word.
    *   Finally, it produces the desired output sequence.

### Inside the Encoder and Decoder

*   **Underlying Network**: Usually, **LSTM RNNs** (or GRU RNNs) are used inside both the encoder and decoder, not simple RNNs, because LSTMs handle the vanishing gradient problem.
*   **Encoder Detail**:
    *   The encoder's LSTM takes the input sentence **word by word**.
    *   Special **start of sentence (SOS)** and **end of sentence (EOS)** tokens are added to both input and output sequences to indicate boundaries.
    *   Each word (along with SOS/EOS) is converted into a vector (e.g., one-hot encoding, word2vec, or embedding layers) before being fed to the LSTM.
    *   The LSTM uses **forget gate, input gate, and output gate** to manage its **long-term memory (CT)** and **short-term memory**.
    *   The **long-term memor and short-term memory** values from the last time step of the encoder are combined to form the **context vector**.
*   **Decoder Detail**:
    *   The decoder's LSTM receives the **context vector** from the encoder.
    *   For its first input, it typically starts with the **SOS token**.
    *   The output of the decoder's LSTM is passed through a **fully connected layer with a softmax activation function**.
    *   **Softmax** is used because the task is a multi-class classification (predicting the next word from a vocabulary). It outputs **probabilities** for each possible word.
    *   The word with the **highest probability** is selected as the predicted output (y_hat).
    *   Crucially, this **predicted output (y_hat) from the current time step is fed as the input to the next time step** of the decoder's LSTM.
    *   The decoder continues generating words and feeding them back until it predicts the **EOS token**, signaling the end of the output sentence.

### Training Process

*   **Loss Calculation**: During training, the **loss** is calculated by comparing the **predicted output (y_hat)** with the **true output (y_truth)** (e.g., (y - y_hat)^2).
*   **Reducing Loss**: The primary goal is to **reduce this loss**.
*   **Backpropagation & Optimization**:
    *   If the loss is high, **backpropagation** occurs, and an **optimizer** is used to **update all the weights** within the LSTMs of both the encoder and the decoder.
    *   After weights are updated, **forward propagation** is performed again to re-calculate outputs and loss.
*   This iterative process of forward and backward propagation continues to train the model until the loss is minimized.

# Encoder-Decoder Architecture: Problems and Solution

## The Problem with the Encoder-Decoder Architecture

*   **The Core Issue:** The **single context vector** that summarizes the entire input sentence becomes a bottleneck for **longer sentences**.
*   **Observation by Researchers:**
    *   Researchers tested the architecture with **sentences of varying lengths**.
    *   They used the **Bleu score** as the performance metric to evaluate the model's performance on sequence-to-sequence data.
    *   **Result:** As the **sentence length increased (e.g., beyond 30-50 words), the accuracy (Bleu score) started decreasing significantly**.
*   **Why it Happens:**
    *   The single context vector is derived from the **last output of the encoder's LSTM**.
    *   This means the context vector will have **more information about words that appeared closer to the end (nearest timestamp)** of the input sentence.
    *   Words that appeared at the **beginning of a long sentence (earlier timestamps)** will have **less context** or **limited information** represented in this single vector.
    *   Therefore, for longer sentences, **this single context vector is not sufficient to fully represent all the information** from the entire input.