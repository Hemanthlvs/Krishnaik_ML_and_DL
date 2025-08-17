# Decision Tree Splitting for Numerical Features

## 1. Introduction: From Categorical to Numerical Features

*   Previously, we discussed decision tree classifiers where **all features were categorical**. For categorical features, splitting is straightforward – you can easily divide categories based on each split.
*   **The challenge**: What if you have a **continuous or numerical feature**? How do you decide the split points in such scenarios?

## 2. Steps for Splitting Numerical Features

Here's the step-by-step process:

### Step 1: Sort the Feature Values

*   The **first crucial step** is to **sort all the values of the numerical feature**.
*   These values should be sorted in **ascending order**.
    *   *Example*: If you have values like 2.3, 3.6, 4.0, 5.2, they should be arranged like this.

### Step 2: Create Many Decision Trees (Hypothetical Splits)

*   Once the values are sorted, we **create many hypothetical decision trees** by trying out different split points.
*   For **each potential split**, a **threshold** is chosen from the sorted feature values.

    *   **Example 1: First Split (Threshold = 2.3)**
        *   **Threshold chosen**: 2.3.
        *   **Root Node Decision**: `less than or equal to 2.3` (`<= 2.3`).
        *   This creates a **binary split** (two branches):
            *   **Left Branch (True/Yes)**: Instances where the feature value is `less than or equal to 2.3`.
                *   In the example, this branch resulted in **one 'Yes' output** and **zero 'No' outputs**.
            *   **Right Branch (False/No)**: Instances where the feature value is `greater than 2.3`.
                *   In the example, this branch resulted in **three 'Yes' outputs** and **three 'No' outputs**.
        *   This forms one initial decision tree. Further splitting can happen based on metrics like entropy.

    *   **Example 2: Second Split (Threshold = 3.6)**
        *   **Threshold chosen**: 3.6.
        *   **Root Node Decision**: `less than or equal to 3.6` (`<= 3.6`).
        *   Again, a binary split occurs:
            *   **Left Branch (True/Yes)**: Instances `less than or equal to 3.6`.
                *   In the example, this resulted in **two 'Yes' outputs** and **zero 'No' outputs**.
            *   **Right Branch (False/No)**: Instances `greater than 3.6`.
                *   In the example, this resulted in **two 'Yes' outputs** and **three 'No' outputs**.

*   This process continues: we keep **creating multiple decision trees** by moving the threshold to the next sorted value.

### Step 3: Evaluate and Select the Best Split

*   After creating multiple hypothetical splits, we need to determine **which split is the best**.
*   **How to evaluate?**: It's quite simple! We use **Information Gain**.
*   **Selection Criteria**: The split that yields the **highest Information Gain** is chosen as the optimal split.
*   **Result**: For example, if trying '4' as a split point gives the best Information Gain, then the root node of your actual decision tree will be `less than or equal to 4` (`<= 4`). This is how the splitting actually happens for numerical features.

## 3. Major Disadvantage

*   While effective, this technique has a **significant disadvantage**:
    *   **High Time Complexity**: Because the process involves **comparing so many decision trees** (one for each potential split point).
    *   If your dataset contains **millions of records**, the **time taken for this process becomes very high**. This is a key bottleneck.
*   Despite this, decision trees internally use this technique for handling all numerical features.