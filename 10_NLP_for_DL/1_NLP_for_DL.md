# NLP in Deep Learning: Sequential Data and Architectures

## NLP in Machine Learning (Previous Topics)

Before moving to deep learning, traditional NLP in machine learning involved converting text data into numerical representations (vectors). Techniques discussed include:
*   **One-hot encoding**
*   **Bag of Words**
*   **TF-IDF**
*   **Word2Vec**
*   **Average Word2Vec**

These techniques were applied to solve problems like **sentiment analysis** and **text classification**.

## Artificial Neural Networks (ANNs)

ANNs are a type of neural network used to solve various supervised problem statements, specifically **classification and regression**.

*   **Data Type**: ANNs are typically used for **tabular data**. Tabular data is organized like a CSV file, with features (e.g., house size, number of rooms) and an output (e.g., house price).
*   **Key Characteristic**: For tabular data in ANNs, the **sequence of data does not matter**. You can change the order of features (e.g., F1, F2 to F2, F1), and the model will still train effectively because the entire row is processed at once.
*   **How ANNs Work (Briefly)**:
    *   Inputs (features) are fed into an input layer.
    *   These connect to hidden layers with weights (W) and biases (b).
    *   **Forward Propagation**: Inputs are multiplied by weights, a bias is added, and an activation function is applied. This process generates a predicted output (`y_hat`).
    *   **Backward Propagation**: The model calculates a **loss** (difference between actual and predicted output, `y - y_hat`). The main goal is to reduce this loss by adjusting the weights through backpropagation.

## Convolutional Neural Networks (CNNs)

CNNs are another type of neural network primarily used for **image and video data**.

*   **Data Type**: Images and video frames.
*   **Tasks**: Common applications include **image classification** and **object detection**.

## Sequential Data

Sequential data is a critical concept in NLP in deep learning because its **sequence is very important to understand the context and meaning**. If the order of information changes, the meaning can change or be lost.

*   **Definition**: Data where the ordering of elements makes the sentence or data meaningful.
*   **Examples of Sequential Data Applications**:
    *   **Text Generation**: Predicting the next word in a sentence (e.g., "This is an apple **juice**").
    *   **Chatbot Conversations**: In Q&A systems, the sequence of questions and answers is crucial for maintaining context.
    *   **Language Translation**: Converting text from one language to another (e.g., English to French); the sequence of words is necessary for accurate translation.
    *   **Auto-suggestion**: Providing word or sentence suggestions while typing (e.g., in Gmail, LinkedIn).
    *   **Sales Data / Time-Series Forecasting**: Sales data collected over time is sequential, where previous timestamps are used to predict future sales (e.g., sales forecasting).

## Key Topics to Learn in NLP in Deep Learning

To work with NLP in deep learning, especially concerning **Generative AI**, **Large Language Models (LLMs)**, and **Multi-modal models**, understanding specific neural network architectures is a prerequisite. These topics are foundational for the current trends in AI.

The architecture topics to be covered include:
*   **Simple RNN** (Recurrent Neural Network)
*   **LSTM** (Long Short-Term Memory) and **GRU RNN** (Gated Recurrent Unit)
*   **Bidirectional RNN**
*   **Encoders and Decoders**
*   **Self-attention**
*   **Transformers** (which form the basis for most modern LLMs in Generative AI)