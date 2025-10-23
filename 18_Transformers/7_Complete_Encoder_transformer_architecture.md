# Transformer Encoder Architecture

## Overview of the Encoder
*   A Transformer model, as per the research paper, typically consists of **six encoders and six decoders**.
*   The encoder processes input, for example, in tasks like machine translation.
*   Information flows from one encoder to the next.

## Flow within a Single Encoder
1.  **Input Sequence Processing**:
    *   Your input sequence (e.g., words) is first **converted into vectors**. This is done using **text embedding techniques**.
    *   **Dimension**: Based on the research paper, each word is converted into a **512-dimension vector**.
    *   **Positional Encoding**: This embedding is then **added with positional encoding**. Positional encoding also uses the same 512 dimensions. This helps the model understand the order of words.
2.  **Multi-Head Attention Layer**:
    *   The combined input (embedding + positional encoding) is passed to a **self-attention layer**, specifically called **Multi-Head Attention**.
    *   **Number of Heads**: The research paper uses **eight attention heads** within the multi-head attention.
    *   **Query (Q), Key (K), Value (V) Dimensions**: Inside self-attention, the Q, K, and V parameters each have a **dimension of 64**. When normalizing, you divide by the square root of 64, which is 8.
3.  **Add & Normalization Layer (Layer Normalization + Residuals)**:
    *   **Before** the multi-head attention output is sent to the next stage, it undergoes an "Add and Normalize" step.
    *   **Normalization Technique**: **Layer normalization** is used. This helps stabilize the distribution of inputs to subsequent layers.
    *   **Residuals (Skip Connections)**: This layer also incorporates **residual connections**, also called **skip connections**. These connections add the original input information (from the embedding + positional encoding stage) to the output of the multi-head attention before normalization.
4.  **Feed-Forward Neural Network**:
    *   After the "Add and Normalization" step, the information is sent to a **feed-forward neural network**.
    *   This network typically has an input layer, **one hidden layer with 512 hidden nodes**, and an output layer.
5.  **Second Add & Normalization Layer**:
    *   Similar to the first one, after the feed-forward neural network, there's another **Add & Normalization step**.
6.  **To the Next Encoder**:
    *   Once all these steps are completed, the processed information is sent to the **next encoder** in the stack.

## Why So Many Encoders (Six)?
*   **Complex Tasks**: Sequence-to-sequence tasks, like machine translation, are very complex. They involve many nuances like dialects.
*   **Accuracy**: Using only one encoder would not provide good accuracy for such complex tasks.
*   **Good Results**: The research paper found that using **six encoders** produced good results. More encoders allow for more extraction of information.

## Why Residual Connections (Skip Connections)?
*   Residual connections are crucial for deep neural networks.
*   **Addresses Vanishing Gradient Problem**:
    *   In deep networks (like six encoder layers), gradients (signals for updating weights during training) can become very small, making learning difficult. This is called the vanishing gradient problem.
    *   Residual connections **create "short paths"** for gradients to flow directly through the network. This keeps gradients sufficiently large.
*   **Improves Gradient Flow**:
    *   Better gradient flow leads to **faster convergence** (the model learns faster) and **smoother training**.
*   **Enables Training of Deeper Networks**:
    *   They allow for the **effective training of much deeper networks** like the Transformer's six encoders. They help the network learn "identity mappings," meaning it can easily pass information through layers without altering it if no learning is needed. This makes the model more expressive and capable of learning complex functions.

## Why Feed-Forward Neural Network?
*   **Adds Non-Linearity**:
    *   Neural networks are used to capture **non-linear functions** and complex properties within data. Self-attention does a good job, but the feed-forward network adds more capacity to capture complex information.
*   **Processes Each Position Independently**:
    *   While self-attention captures relationships between tokens, the feed-forward network processes **each token's representation independently** after the self-attention mechanism.
    *   It applies the same two-layer neural network to each token's representation, transforming it further and allowing the model to learn **richer representations**. It helps explore more specific information from each contextual embedding vector.
*   **Adds Depth to the Model**:
    *   The feed-forward network contributes to the overall **depth of the model**. More depth generally allows the neural network to capture **more and more information** from the data.
*   **Increases Model Parameters**:
    *   It increases the number of **model parameters**. More parameters can help the model **generalize well** to both training data and unseen test data.