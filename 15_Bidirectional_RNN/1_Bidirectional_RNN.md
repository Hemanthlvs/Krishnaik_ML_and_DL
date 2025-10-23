# Bidirectional RNN

## Types of RNN Problem Statements
The sources categorize different types of RNNs based on the problem statements they solve:

*   **One-to-One RNN**:
    *   **Description**: One input, one output.
*   **One-to-Many RNN**:
    *   **Description**: One input, multiple outputs.
    *   **Example**: **Image Captioning** – giving one image as input and getting a text description (many words) as output, like "There is a dog and cat in the image" from an image of a dog and cat.
*   **Many-to-One RNN**:
    *   **Description**: Multiple inputs, one output.
    *   **Example**: **Image Search** – searching for "a cat eating food" (multiple input words) and getting specific images as one output. Sentiment analysis could also be an example (many words input, one sentiment output).
*   **Many-to-Many RNN**:
    *   **Description**: Multiple inputs, multiple outputs.
    *   **Example**: **Language Translation** – converting a sentence from one language to another involves many input words and many output words. This type is used when all outputs related to all inputs are required.

## The Problem Bidirectional RNN Solves
*   In simple RNNs (or LSTMs/GRUs), predictions are typically dependent only on **previous context** (words processed earlier).
*   However, for certain predictions, the **context of upcoming words** (forward context) is also crucial.
*   **Example**: Predicting a missing word in "Krish eats ---- in Bangalore.".
    *   If the sentence is "Krish eats ---- in **Bangalore**," the word might be "dosa" (a famous food in Bangalore).
    *   If the sentence is "Krish eats ---- in **Paris**," the word might be "pizza" (a famous food in Paris).
    *   A simple RNN cannot capture this forward context, as it only processes words from left to right.
*   **Bidirectional RNNs** are designed to fix this problem by providing this forward context.

## Bidirectional RNN Architecture and Functionality
*   **Concept**: To get the context of upcoming words, a bidirectional RNN uses **two separate RNNs** (or LSTMs/GRUs).
*   **Forward Pass**:
    *   One RNN processes words in the standard forward direction (X1, X2, X3, etc.).
    *   Inputs are passed word by word at each time step (t=1, t=2, etc.).
*   **Backward Pass**:
    *   Another RNN is created that processes the words in the **reverse direction**.
    *   For example, if the sentence is "Krish eats ---- in Bangalore," the backward RNN would start processing "Bangalore" first, then "in," and so on.
*   **Combination**:
    *   The outputs from both the forward and backward RNNs are **concatenated or combined**.
    *   This combined output provides the necessary context for predictions.
*   **Benefit**: When predicting a word in the middle of a sentence , the combined output from the bidirectional RNN has context from both the words before it and the words after it. This allows for more accurate predictions, as the model understands how the context from both directions influences the missing word.