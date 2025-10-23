# Understanding Entropy and Gini Impurity

## Introduction
*   In **decision tree classifiers**, we need to understand how to check if a split is **pure** or not.
*   For this, we primarily use two important concepts: **Entropy** and **Gini Impurity**.

## 1. Entropy

### What is Entropy?
*   Entropy (H(S)) is a measure of the **impurity** or randomness in a set of data. The higher the entropy, the more impure the split is.
*   **Formula for Binary Classification**:
    ```
    H(S) = -p+ * log₂(p+) - p- * log₂(p-)
    ```
    *   **p+**: Probability of belonging to the positive category (e.g., 'yes' or '1').
    *   **p-**: Probability of belonging to the negative category (e.g., 'no' or '0').
*   **For Multi-class Classification**: You just extend the formula by adding `- P_category_i * log₂(P_category_i)` for each category.

### Examples of Entropy Calculation:

#### a. For an Impure Split (e.g., Category C1)
*   Let's say a split results in **3 'yes' and 3 'no'**. This is clearly an **impure split** (50% yes, 50% no).
*   **Total items**: 6 (3 yes + 3 no).
*   **p+ (Probability of 'yes')**: 3/6 = 0.5.
*   **p- (Probability of 'no')**: 3/6 = 0.5.
*   **Calculation**:
    `H(C1) = -(3/6) * log₂(3/6) - (3/6) * log₂(3/6)`
    `H(C1) = -(0.5) * log₂(0.5) - (0.5) * log₂(0.5)`
*   **Result**: When calculated, **H(C1) will be 1**.
*   **Key takeaway**: For a **completely impure split** (e.g., equal distribution), the **maximum entropy value is 1**.

#### b. For a Pure Split (e.g., Category C2)
*   Let's say another split results in **3 'yes' and 0 'no'**. This is a **pure split** because all instances belong to one category.
*   **Total items**: 3 (3 yes + 0 no).
*   **p+ (Probability of 'yes')**: 3/3 = 1.
*   **p- (Probability of 'no')**: 0/3 = 0.
*   **Calculation**:
    `H(C2) = -(3/3) * log₂(3/3) - (0/3) * log₂(0/3)`
    `H(C2) = -(1) * log₂(1) - (0) * log₂(0)`
*   **Result**: When calculated, **H(C2) will be 0**. (Note: `0 * log(0)` is typically treated as 0 in this context).
*   **Key takeaway**: For a **pure split**, the **entropy value is 0**.

### Entropy Graph and Range
*   If you plot **Entropy (H(S))** on the Y-axis against **Probability of plus (p+)** on the X-axis (ranging from 0 to 1):
    *   The graph will be a curve.
    *   It will be **0** when p+ is 0 or 1 (pure splits).
    *   It will reach its **maximum value of 1** when p+ is 0.5 (completely impure split).
*   **Range of Entropy values**: Always between **0 to 1**.

## 2. Gini Impurity

### What is Gini Impurity?
*   Gini Impurity is another measure of impurity in a dataset. It quantifies the likelihood of incorrectly classifying a randomly chosen element.
*   **Formula**:
    ```
    Gini Impurity = 1 - Σ (P_i)²
    ```
    *   Here, `Σ (P_i)²` means the sum of the squares of the probabilities of each category.
*   **For Binary Classification**:
    ```
    Gini Impurity = 1 - ( (P+)^2 + (P-)^2 )
    ```
    *   **P+**: Probability of being 'yes'.
    *   **P-**: Probability of being 'no'.

### Examples of Gini Impurity Calculation:

#### a. For an Impure Split (e.g., 3 'yes', 3 'no')
*   Let's use the same example: **3 'yes' and 3 'no'**.
*   **P+ (Probability of 'yes')**: 3/6 = 1/2.
*   **P- (Probability of 'no')**: 3/6 = 1/2.
*   **Calculation**:
    `Gini Impurity = 1 - ( (1/2)² + (1/2)² )`
    `Gini Impurity = 1 - ( 1/4 + 1/4 )`
    `Gini Impurity = 1 - ( 1/2 )`
*   **Result**: **Gini Impurity will be 0.5**.
*   **Key takeaway**: For a **completely impure split**, the **maximum Gini Impurity value is 0.5**.

#### b. For a Pure Split (e.g., 3 'yes', 0 'no')
*   Let's use the same example: **3 'yes' and 0 'no'**.
*   **P+ (Probability of 'yes')**: 3/3 = 1.
*   **P- (Probability of 'no')**: 0.
*   **Calculation**:
    `Gini Impurity = 1 - ( (1)² + (0)² )`
    `Gini Impurity = 1 - ( 1 + 0 )`
*   **Result**: **Gini Impurity will be 0**.
*   **Key takeaway**: For a **pure split**, the **Gini Impurity value is 0**.

### Gini Impurity Range
*   **Range of Gini Impurity values**: Always between **0 to 0.5**.

## 3. Key Differences Between Entropy and Gini Impurity (Important for Interviews!)
*   **Range of Values**:
    *   **Entropy**: Ranges from **0 to 1**.
    *   **Gini Impurity**: Ranges from **0 to 0.5**.
*   **Interpretation of 0**: Both Entropy and Gini Impurity return **0 for a pure split**.
*   **Interpretation of Maximum Impurity**:
    *   Entropy's maximum impurity value is **1** (e.g., 50/50 split).
    *   Gini Impurity's maximum impurity value is **0.5** (e.g., 50/50 split).
*   **Usage**: Both are used to evaluate how pure a split is in a decision tree.


# Entropy vs. Gini Impurity: 

## When to Use What? (The Big Question!)

This is the most important part! People often get confused here.

### When to Use Entropy:
*   The formula for Entropy uses `log`.
*   **Use Entropy when your dataset is small**.
    *   For example, if you have around **10,000 records**, you can definitely go with Entropy.
    *   **Reason**: For small datasets, the time difference in training the model between Entropy and Gini Impurity will be **almost minimal**.
*   **Consideration**: Implementing with Entropy will generally **take more time because of the `log` calculation**.

### When to Use Gini Impurity:
*   **Definitely try to use Gini Impurity when the dataset is large**.
*   **Default Choice**: **By default, most decision tree classifiers use Gini Impurity**.
*   **Common Scenario**: For most scenarios or problem statements, **Gini Impurity is basically used**.