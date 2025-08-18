# XGBoost Regressor: A Deep Dive into Sequential Trees

## Introduction to XGBoost Regressor
*   XGBoost Regressor is a **machine learning algorithm** used to solve **regression problems**.
*   It builds **sequential decision trees** to make predictions.
*   The process is similar to XGBoost Classifier, but with some key differences, especially in formulas.

## Problem Statement Example
*   **Input features**: Experience and Career Gap.
*   **Output/Dependent feature**: Salary.
*   **Goal**: Predict salary based on experience and career gap – this is a **regression problem**.

## Key Differences from XGBoost Classifier (Formula-wise)
*   **Similarity Weight Formula**:
    *   **XGBoost Classifier**: `Summation of Residual Square / (Summation of Probability * (1 - Probability))`.
    *   **XGBoost Regressor**: The denominator changes. It uses **`Summation of Residual Square / (Number of Residuals + Lambda)`**. This is a crucial difference.
*   **Base Model Output**:
    *   **XGBoost Classifier**: Uses log odds of the base learner.
    *   **XGBoost Regressor**: Uses the **average** of the output values from the dataset.

## Step-by-Step Process of XGBoost Regressor

Let's break down how an XGBoost Regressor is built, step by step:

### Step 1: Create a Base Model
*   For a regression problem, the base model's output is simply the **average of all the output/dependent feature values** in the dataset.
*   **Example**: If salaries are 40K, 42K, 52K, 60K, 62K, the average (base model output) is **51K**.
*   This base model is **not biased** towards any specific values; it's just the overall average.
*   Initially, any data passed through this base model will give **51K as the output (y_hat)**.

### Step 2: Compute Residuals (Errors)
*   Residuals are calculated as the **difference between the actual output (Y) and the predicted output from the base model (Y_hat)**.
*   `Residual = Actual Output - Predicted Output (from base model)`.
*   **Example**: For actual salary 40K and base prediction 51K, the residual is `40 - 51 = -11K`.
*   These residuals become the **new output feature** for constructing the first decision tree.

### Step 3: Construct the First Decision Tree (and subsequent trees)
*   A decision tree is constructed using the **original input features (X_i)** (e.g., experience, gap) and the **calculated residuals (R1)** as the output feature.
*   **Feature Selection and Splitting**:
    *   The algorithm picks a feature (e.g., experience) and identifies **thresholds** to split the data (e.g., `experience <= 2` and `experience > 2`).
    *   It tries different splits (e.g., `experience <= 2.5` and `experience > 2.5`) to find the **best split**.
    *   The residuals are distributed to the respective leaf nodes based on the split.

*   **Calculate Similarity Weight (W)**:
    *   This is a crucial step to evaluate the "purity" or "similarity" within a node.
    *   **Formula for Regression**: `Similarity Weight = (Sum of Residuals)^2 / (Number of Residuals + Lambda)`.
    *   **Lambda (λ)**: This is a **hyperparameter**.
        *   It helps in regularization.
        *   If **lambda increases, similarity weight decreases**.
        *   It needs to be tuned using cross-validation.
        *   For the example, `lambda = 1` is considered.
    *   **Example Calculations**:
        *   Left child (residual -11): `W_left = (-11)^2 / (1 + 1) = 121 / 2 = 60.5`. (Note: Transcript says 65.5, but calculation `121/2` is 60.5. Let's stick to the steps for notes and highlight the formula.)
        *   Right child (residuals -9, 1, 9, 11): `W_right = (-9+1+9+11)^2 / (4 + 1) = (12)^2 / 5 = 144 / 5 = 28.8`. (Transcript says 28.5, but 144/5 is 28.8. Minor calculation discrepancies in source, but the method is clear).
        *   Root node (all residuals): `W_root = ((-11-9+1+9+11)^2) / (5+1) = (-11)^2 / 6 = 121/6 = 20.16` (Transcript states 1.16, which seems like a typo given calculation). **The formula `(Sum of Residuals)^2 / (Number of Residuals + Lambda)` is the key takeaway.**

*   **Calculate Gain**:
    *   Gain is used to decide the **best split** for a decision tree.
    *   **Formula**: `Gain = Similarity Weight (Left Child) + Similarity Weight (Right Child) - Similarity Weight (Root Node)`.
    *   The split that results in the **highest gain** is selected for the decision tree.
    *   This process ensures the decision tree is constructed to minimize error effectively.
    *   **Further Splitting**: Once a split is chosen, further splits can be made on the child nodes using other features (e.g., gap).

### Step 4: Calculate the New Predicted Output (after the first tree)
*   The **final prediction** from XGBoost is an **ensemble** of the base model and sequential decision trees.
*   **Formula for XGBoost Regressor**:
    *   `New Y_hat = Base Model Output + Alpha (Learning Rate) * Decision Tree 1 Output`.
    *   This is applied for each subsequent tree as well: `Y_hat_new = Y_hat_old + Alpha * Decision Tree N Output`.
*   **Alpha (α) / Learning Rate**:
    *   This is another **hyperparameter**.
    *   It controls how much each new tree's prediction contributes to the final output.
    *   A common value is `0.1` (or `0.2`, `0.3`, etc.).

*   **Example (Predicting for a test record: Experience=3, Gap=No)**:
    1.  **Base Learner Output**: 51K.
    2.  **Pass through Decision Tree 1**:
        *   Experience 3 is `> 2.5` (takes right path).
        *   Gap is `No` (takes right path again).
        *   The leaf node has residuals `1, 9`.
        *   **Decision Tree 1 Output**: Average of leaf node residuals `(1 + 9) / 2 = 5`.
    3.  **Calculate New Predicted Output**: `51K + (0.1 * 5) = 51 + 0.5 = 51.5K`.
    *   This `51.5K` is the **new Y_hat** for that specific record.

*   This process is repeated for **all records** in the dataset to get their new predicted outputs after the first tree.

### Step 5: Compute New Residuals (R2)
*   After getting the `New Predicted Output (Y_hat_new)` from the base model + first tree, we again calculate **new residuals (R2)**.
*   **Formula**: `R2 = Actual Output (Y) - New Predicted Output (Y_hat_new)`.
*   **Example**: If actual is 40K and new predicted is 49.9K, R2 = `40 - 49.9 = -9.9`.
*   These new residuals (`R2`) then become the **output feature** for constructing the **second decision tree**.

## Iterative Process
*   The process of creating a decision tree, calculating new predictions, and then new residuals continues iteratively.
*   **Multiple sequential decision trees** are created, each trying to correct the errors (residuals) of the previous models.
*   The final XGBoost Regressor model is an **ensemble** of the base learner and all these sequentially built decision trees.

## Summary of Key Concepts
*   **Base Model**: Average of target variable.
*   **Residuals**: Errors from previous prediction, used as target for the next tree.
*   **Similarity Weight**: `(Sum of Residuals)^2 / (Number of Residuals + Lambda)`.
*   **Gain**: Used to select the best split in a tree.
*   **Lambda (λ)**: Regularization hyperparameter; increasing it decreases similarity weight.
*   **Alpha (α) / Learning Rate**: Hyperparameter controlling contribution of each tree.
*   **Sequential Decision Trees**: Each tree builds upon the errors of the previous ones.
*   **Final Prediction**: `Base Model Output + α1 * DT1 Output + α2 * DT2 Output + ...`.

This detailed breakdown should help you prepare and brush up on your XGBoost Regressor knowledge!
```