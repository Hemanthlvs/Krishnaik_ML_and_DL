# Logistic Regression:

## Introduction to Logistic Regression

*   **Logistic Regression** is a new Machine Learning algorithm.
*   It is primarily used for **solving binary classification problems**.

## Understanding Binary Classification Problems

*   In a **binary classification problem**, the **output feature (dependent feature) is categorical**.
*   Specifically, it has **binary categories** (e.g., two possible outcomes).
*   **Example Scenario:**
    *   **Input Feature:** `study_hours` (e.g., 2, 3, 4, 5, 6, 7 hours).
    *   **Output Feature:** Whether a person will `pass` or `fail` an exam.
*   **Why it's a classification problem:** Because the output has two distinct categories (pass or fail).
*   **Logistic Regression is used to solve this type of binary classification problem**.
*   **Labeling for Analysis:** For plotting and analysis, `pass` is often assigned a value of `1`, and `fail` is assigned `0`.

## Attempting to Solve Classification with Linear Regression

*   The question arises: **Why is it called "regression" if it solves classification?** And **can we use Linear Regression for this problem?**.
*   **Plotting the Data:**
    *   `study_hours` on the x-axis.
    *   `pass/fail` (0 or 1) on the y-axis.
    *   Plotting data points: (2 hrs, Fail/0), (3 hrs, Fail/0), (4 hrs, Fail/0), (5 hrs, Pass/1), (6 hrs, Pass/1), (7 hrs, Pass/1).
*   **Applying Linear Regression:**
    *   The main aim of Linear Regression is to **find a "best-fit line"** for the data points.
    *   Initially, one might try to use this best-fit line for classification by setting a **threshold**, e.g., **0.5 (midpoint)**.
    *   **Classification Rule:**
        *   If the predicted value from the line is **less than or equal to 0.5**, classify as `0` (Fail).
        *   If the predicted value is **greater than 0.5**, classify as `1` (Pass).
    *   At first glance, this approach **seems to work** for simple cases.

## Problems with Using Linear Regression for Classification

Despite the initial appearance of success, **Linear Regression has significant issues when applied to classification problems**:

### Issue 1: Sensitivity to Outliers

*   **The biggest issue is with outliers**.
*   **Scenario:** If an outlier data point is introduced (e.g., a person studying for **12 hours and passing**), it drastically changes the best-fit line.
*   The **best-fit line will "slant" or completely change** to accommodate the outlier.
*   **Consequence:** This change in the line can lead to **incorrect predictions** for existing data points that were previously correctly classified.
    *   *Example:* A person studying for 5 hours was initially predicted to pass, but after adding the outlier, the new best-fit line might predict them to fail (value less than 0.5), which contradicts the training data and is a "biggest blunder".

### Issue 2: Output Range is Not Restricted (Beyond 0 and 1)

*   For binary classification, the output ideally represents a probability and **should always be between 0 and 1**.
*   However, with Linear Regression, the best-fit line can extend indefinitely.
*   This means the **predicted output can be greater than 1** or **less than 0 (a negative value)**.
*   **Consequence:** Such values (e.g., -0.2 or 1.5) don't make sense in a binary classification context where outcomes are 0 or 1, representing states like pass/fail or true/false.

## 5. The Solution: "Squashing" the Line (Role of Logistic Regression)

*   To address the issue of output values going beyond 0 and 1, we need to **"squash" the line**.
*   **Squashing means restricting the output** to always fall within the 0 to 1 range.
*   **Linear Regression cannot perform this squashing**.
*   **Logistic Regression is designed to squash the output** and keep it strictly between 0 and 1.