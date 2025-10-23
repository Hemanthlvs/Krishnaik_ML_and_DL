# Multi-Class Logistic Regression: One Versus Rest Strategy

## Introduction to Logistic Regression

*   **Binary Classification:** In previous discussions, logistic regression was used for binary classification problems where the aim was to create a "best fit line" to divide data points into **two categories**.
*   **Multi-Class Problem:** The challenge arises when your dataset has **three or more output categories** (more than two). For example, having output categories like Class A, Class B, and Class C.

## Solving Multi-Class Classification with Logistic Regression

*   To solve multi-class classification problems using logistic regression, an important technique called **"One Versus Rest" (OVR)** is used.
*   The **main aim of OVR** is to convert a multi-class problem into multiple binary classification problems internally.

## How One Versus Rest (OVR) Works

*   OVR works by **internally creating multiple models**, where each model acts as a binary classifier.
*   The number of internal models created will be **equal to the number of output categories**.
    *   For example, if you have three output categories (O1, O2, O3), three internal models (M1, M2, M3) will be created.

### Internal Model Creation and Binary Classification

Let's consider an example with three output categories: O1, O2, O3.

*   **Model M1:**
    *   This model is trained to differentiate **one category (O1)** from **all the "rest" of the categories combined (O2 + O3)**.
    *   It creates a best-fit line to separate O1 points from the combined O2 and O3 points.
    *   This is a **binary classification** problem.

*   **Model M2:**
    *   This model is trained to differentiate **O2** from **the combined O1 and O3**.
    *   It considers O2 as one category and (O1 + O3) as another.
    *   This is also a **binary classification** problem.

*   **Model M3:**
    *   This model is trained to differentiate **O3** from **the combined O1 and O2**.
    *   It considers O3 as one category and (O1 + O2) as another.
    *   Again, this is a **binary classification** problem.

### One-Hot Encoding for Model Training

*   Before training, the output categories (O1, O2, O3) are converted using **one-hot encoding**.
    *   O1 becomes `100` (where `1` indicates O1, `0` for others).
    *   O2 becomes `010`.
    *   O3 becomes `001`.

### Input and Output Features for Each Model

Assume input features are f1, f2, f3.

*   **For Model M1:**
    *   **Input Features:** f1, f2, f3.
    *   **Output Feature:** The one-hot encoded column corresponding to O1 (e.g., the first column of the one-hot encoded output, which will have `1` for O1 and `0` for O2/O3).

*   **For Model M2:**
    *   **Input Features:** f1, f2, f3.
    *   **Output Feature:** The one-hot encoded column corresponding to O2 (e.g., the second column).

*   **For Model M3:**
    *   **Input Features:** f1, f2, f3.
    *   **Output Feature:** The one-hot encoded column corresponding to O3 (e.g., the third column).

## Prediction Process for New Test Data

When a new test data point comes in, the prediction happens as follows:

1.  **Pass to All Models:** The new test data is passed to **each of the internal models** (M1, M2, M3).
2.  **Obtain Probabilities:** Each model will output a **probability score**.
    *   Example:
        *   M1 might give `0.25` (probability for O1).
        *   M2 might give `0.20` (probability for O2).
        *   M3 might give `0.55` (probability for O3).
3.  **Identify Highest Probability:** Compare the probabilities from all models.
    *   In the example, `0.55` from M3 is the highest probability.
4.  **Determine Final Category:** The final predicted category is the one for which the corresponding model yielded the **highest probability**.
    *   Since M3 gave the highest probability (`0.55`) and M3 was trained for O3, the new test data is classified as **Category 3**.