# Performance Metrics in Classification Models

## Introduction to Classification & Performance Metrics

*   When you create a model, like using **Logistic Regression** for a classification problem, the main aim is to classify data points by creating a linear line.
*   To understand how well your model is performing, we use performance metrics.
*   Unlike linear regression where we use metrics like R-squared or adjusted R-squared, classification problems use different metrics.
*   The key metrics discussed here are **Confusion Matrix, Accuracy, Precision, Recall, and F-beta Score**.

## Confusion Matrix

*   The **first thing** you create after getting predictions from your model is a **Confusion Matrix**.
*   **What it is:**
    *   For **binary classification**, it's a **2x2 matrix**.
    *   For **multi-class classification**, if you have 'n' output categories, it becomes an **nxn matrix**.
*   **Structure:**
    *   The **top row** typically represents the **Actual Values** (e.g., 1s and 0s).
    *   The **left-hand side** typically represents the **Predicted Values** (e.g., 1s and 0s).
*   **Populating the Matrix (Example):**
    *   If **Actual is 0** and **Predicted is 1**, you increment the count in the `Actual 0, Predicted 1` cell.
    *   If **Actual is 1** and **Predicted is 1**, you increment the count in the `Actual 1, Predicted 1` cell.
    *   Similarly for other combinations (e.g., Actual 0, Predicted 0; Actual 1, Predicted 0).
*   **Key Notations (Super Important!):**
    *   **True Positive (TP):** Actual value is 1, Model predicted 1. (**Correct result**).
    *   **True Negative (TN):** Actual value is 0, Model predicted 0. (**Correct result**).
    *   **False Positive (FP):** Actual value is 0, Model predicted 1. (**Wrong result**).
    *   **False Negative (FN):** Actual value is 1, Model predicted 0. (**Wrong result**).
    *   **Diagonal elements (TP, TN) are correct predictions**, while **off-diagonal elements (FP, FN) are wrong predictions**.

## Accuracy

*   **Formula:**
    `Accuracy = (True Positive + True Negative) / (True Positive + False Positive + False Negative + True Negative)`
    In simpler terms: `(Correct Predictions) / (Total Predictions)`
*   **Use Case:** Provides an overall measure of how correctly your model predicted across all categories.
*   **Limitation (When NOT to use!):**
    *   **Do NOT directly use Accuracy for Imbalanced Datasets**.
    *   **Why?** In an imbalanced dataset (e.g., 900 ones, 100 zeros), a "blunt" model that simply predicts '1' for all inputs can achieve high accuracy (e.g., 90%). However, this model is biased and not truly performing well.
    *   To fix this, we use Precision and Recall.

## Precision

*   **Formula:**
    `Precision = True Positive / (True Positive + False Positive)`
*   **What it says:** Out of all the results the model **predicted as positive**, how many of them were **actually correct** (true positives).
*   **Key Focus:** Precision prioritises **reducing False Positives (FP)**.
*   **Use Case Example: Spam Classification**
    *   **Scenario:** Mail is NOT spam (Actual=0), but model predicts it IS spam (Predicted=1). This is a **False Positive (FP)** error.
    *   **Impact:** This is a **huge blunder** because you might miss important, non-spam emails.
    *   **Goal:** In this case, you **must reduce False Positives**.
    *   **Conclusion:** For spam classification (or similar scenarios where FP is a major blunder), **use Precision**.

## Recall

*   **Formula:**
    `Recall = True Positive / (True Positive + False Negative)`
*   **What it says:** Out of all the **actual positive cases**, how many of them did the model **correctly identify** (true positives).
*   **Key Focus:** Recall prioritises **reducing False Negatives (FN)**.
*   **Use Case Example: Diabetes Detection**
    *   **Scenario:** Person HAS diabetes (Actual=1), but model predicts they do NOT have diabetes (Predicted=0). This is a **False Negative (FN)** error.
    *   **Impact:** This is a **very big blunder** because the person might not seek treatment, and the disease could worsen significantly.
    *   **Goal:** In this case, you **must reduce False Negatives**.
    *   **Conclusion:** For disease detection (or similar scenarios where FN is a major blunder), **use Recall**.
    *   *Note:* If a person doesn't have diabetes but the model predicts they do (False Positive), it's "okay" as they can get a second opinion. This type of error is less critical here.

## F-beta Score

*   **When to use:** When **both False Positives and False Negatives are important** to consider, or when one is more critical than the other but both need to be tracked.
*   **General Formula:**
    `F-beta Score = (1 + beta^2) * (Precision * Recall) / (Precision + Recall)`
    *Please note: The denominator in the source's formula `(Precision + Recall)` is a simplification; standard formula is `(beta^2 * Precision) + Recall`.*
*   **Beta Value:** This value (`beta`) lets you control how much more importance you give to Recall over Precision.
    *   If `beta = 1`, it gives equal importance to Precision and Recall.
    *   If `beta < 1`, it gives more importance to Precision.
    *   If `beta > 1`, it gives more importance to Recall.
*   **Specific F-beta Scores:**

    *   **F1 Score (Beta = 1):**
        *   **Formula:** `F1 Score = 2 * (Precision * Recall) / (Precision + Recall)`
        *   **When to use:** When **False Positives (FP) and False Negatives (FN) are equally important**.
        *   **Concept:** It's the **harmonic mean** of Precision and Recall.

    *   **F0.5 Score (Beta = 0.5):**
        *   **Formula:** `F0.5 Score = (1 + 0.5^2) * (Precision * Recall) / (Precision + Recall)` (as per source)
            *   _Calculation: `(1 + 0.25) * (Precision * Recall) / (Precision + Recall)`_
        *   **When to use:** When **False Positive (FP) is more important than False Negative (FN)**. (Example: Spam classification, where missing a non-spam email is worse than missing a spam email).

    *   **F2 Score (Beta = 2):**
        *   **Formula:** `F2 Score = (1 + 2^2) * (Precision * Recall) / (Precision + Recall)` (as per source)
            *   _Calculation: `(1 + 4) * (Precision * Recall) / (Precision + Recall)`_
        *   **When to use:** When **False Negative (FN) is more important than False Positive (FP)**. (Example: Disease detection, where missing a disease is worse than a false alarm).