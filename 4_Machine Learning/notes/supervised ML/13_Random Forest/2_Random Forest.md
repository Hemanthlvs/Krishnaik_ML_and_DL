# Random Forest: Classification & Regression Notes

## Introduction to Random Forest

*   Random Forest is a **machine learning algorithm** used for both **classification and regression** problems.
*   It's an **ensemble technique**, specifically an example of **bagging**.
*   Bagging involves combining multiple base learners to improve overall performance.

## How Random Forest Algorithm Works

1.  **Data Setup**:
    *   Start with a dataset of size `d` and `m` features (e.g., f1, f2, ... fm).
    *   The **base learners** in Random Forest are always **Decision Trees**. You can have any number of decision trees.

2.  **Training Process**:
    *   For each decision tree (base learner), two types of sampling are done from the original dataset:
        *   **Row Sampling (with replacement)**: Pick a subset of rows (`D dash` which is less than `D`) from the original dataset. "With replacement" means some rows might get repeated, but majority will be different, ensuring diversity.
        *   **Feature Sampling (with replacement)**: Pick a subset of features (e.g., F1, F2, F4). "With replacement" means some features might get repeated, but majority will be different.
    *   Each decision tree gets trained on this **unique sample of data** (sampled rows + sampled features). This makes each decision tree an "expert" on a slightly different part of the data.

3.  **Prediction with New Test Data**:
    *   When new test data comes in:
        *   **For Classification Problems**: Each decision tree will give an output (e.g., 0 or 1). The final output is determined by **Majority Voting Classifier**. Whichever output is predicted by most trees is chosen.
        *   **For Regression Problems**: Each decision tree will give a continuous output. The final output is the **Average Output of all the models**.

## Why Use Random Forest Instead of a Single Decision Tree? (Important Interview Question)

*   **Single Decision Tree Issues**:
    *   By default, a single decision tree tends to **overfit**.
    *   Overfitting means **high training accuracy** but **low test accuracy**.
    *   This is characterized by **low bias and high variance**.
    *   A generalized (suitable) model should have **low bias and low variance**.

*   **Random Forest Advantages (Addressing Decision Tree Issues)**:
    *   **Reduces Variance**: Random Forest's main aim is to convert **high variance into low variance**.
    *   **Improves Test Accuracy**: Because it uses multiple decision trees, each trained on different data samples (due to row and feature sampling), the **test accuracy increases**.
    *   **Multiple Experts**: Each decision tree acts as a separate expert. When they collectively decide (via majority voting or averaging), the prediction becomes more robust and generalized.
    *   **Robust to New Data**: Adding new records to the dataset won't significantly impact the previously trained Random Forest model because the new data gets split and sampled across many base learners. No single model gets overly impacted.

*   **Trade-off**:
    *   The **time complexity to train** a Random Forest model is usually **high** because it involves training many decision trees.

## Decision Tree Concepts within Random Forest

*   Random Forest internally uses decision trees.
*   For **classification** in decision trees, concepts like **entropy, Gini impurity, and information gain** are used to construct the tree.
*   For **regression** in decision trees, **Mean Squared Error (MSE)** is used.