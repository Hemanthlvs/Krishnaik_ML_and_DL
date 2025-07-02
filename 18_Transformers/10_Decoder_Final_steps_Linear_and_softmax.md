# Transformers: Linear and Softmax Layers

*   The **Linear and Softmax layers** are the final part of the **decoder**, responsible for calculating output probabilities.

## The Linear Layer
*   The linear layer is a **simple fully connected neural network**.
*   Its main function is to **project the vector produced by the stack of decoders** into **large vectors called logit vectors**.
*   **Logit vectors** have a size equal to the model's vocabulary (e.g., 10,000 words means 10,000 cells wide).
*   Each cell in the logit vector **corresponds to a score of a unique word** in the vocabulary.
*   It effectively maps a vector to words.

## The Softmax Layer
*   The softmax layer is used for **multi-class classification**.
*   It **takes the logit vectors** (scores) from the linear layer.
*   The softmax layer **turns these scores into probabilities**.
*   A key property of softmax is that the **sum of all probabilities will add up to one**.
*   The **cell with the highest probability is chosen as the output**, and the word associated with it is produced as the output for that specific timestamp.

## Converting Vectors to Words (Summary)
1.  The output vector from the decoder is passed to the **linear layer**.
2.  The linear layer, a fully connected layer, outputs a vector based on the **vocabulary size**.
3.  This output is then passed to the **softmax layer**.
4.  The softmax layer generates probabilities, and the word with the **highest probability** is selected as the final output word.

## Recap of the Training Process
*   **Vocabulary Representation**:
    *   Words in the vocabulary are often represented using **one-hot encoding**.
    *   For example, if 'am' is the second word in a six-word vocabulary, its one-hot encoding would be `[0.0, 1.0, 0.0, 0.0, 0.0, 0.0]`.
*   **Untrained vs. Trained Model Output**:
    *   Initially, an **untrained model** may produce different output values (probabilities) than the desired one-hot encoded target.
    *   The goal is to get values like `1.0` for the correct word and `0.0` for others, or very high probabilities for the correct word after training (e.g., `0.93`, `0.94`, `0.98`).
*   **Loss Function and Backpropagation**:
    *   After generating an output from the model (especially from the linear layer's logits), a **loss function** is calculated by comparing the model's output to the target output.
    *   This loss is crucial because **backpropagation** occurs based on it.
    *   The **main aim of backpropagation is to reduce the loss** by updating the model's weights.
    *   Through multiple **epochs** and repeated loss calculation and backpropagation, the model learns to produce more accurate outputs.