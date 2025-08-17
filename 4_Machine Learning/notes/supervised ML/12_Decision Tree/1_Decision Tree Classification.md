# Decision Tree Algorithm

## 1. Introduction to Decision Tree Algorithm

*   The Decision Tree algorithm is a **very important machine learning algorithm**.
*   It's a foundational algorithm used internally by other popular ensemble techniques like **Random Forest** and **XGBoost** (which are part of bagging and boosting methods).
*   Decision Trees can be used for solving **both classification and regression problems**.
*   However, in this particular discussion, the focus is on how to solve **classification problems** using Decision Trees.

## 2. Key Concepts for Decision Tree Building

To understand and build Decision Trees, especially for classification, we need to grasp some core concepts:
*   **Entropy**: Used to check the purity or impurity of a split.
*   **Gini Index (or Gini Impurity)**: Another technique used to check the purity or impurity of a split.
*   **Information Gain**: Used to determine **which feature is the best one to select for splitting** at any given node. The aim is to find a feature that helps in getting "leaf nodes quickly".

## 3. Types of Decision Trees

There are two main types of Decision Tree algorithms:
*   **ID3**:
    *   Allows for **more than binary splits** from a single root node. For example, you can have three splits from one node.
*   **CART (Classification and Regression Trees)**:
    *   This is the technique that the **sklearn library** (commonly used in Python for Decision Trees) primarily uses.
    *   **Creates only binary splits** from each node. This means each split will have only two outcomes, like a Yes/No branch.
*   The mathematical formulas might differ slightly between ID3 and CART due to their splitting mechanisms.

## 4. Intuition Behind Decision Trees (If-Else Analogy)

*   A Decision Tree works very much like a series of **`if-else if-else` conditions** in programming.
*   **Example (Age-based conditions)**:
    *   If `age <= 15`: Person is **in school**.
    *   Else If `age > 15` AND `age <= 21`: Person is **in college**.
    *   Else: Person has **passed college**.
*   This flow can be represented as a tree structure:
    *   You start with a **root node** (e.g., `Age <= 15?`).
    *   This node splits into two branches: **Yes** or **No**.
    *   If "Yes", it might lead to a final outcome (e.g., "Person is in school").
    *   If "No", it leads to another **decision node** (e.g., `Age > 15 and Age <= 21?`).
    *   This continues until you reach a **final outcome or "leaf node"**.
*   The main goal is to take a dataset with independent and dependent features and construct such a decision tree. The construction usually follows a **bottom-to-top approach** (as mentioned in the source).

## 5. Decision Tree Construction Example (Play Tennis Dataset)

Let's understand how a Decision Tree is built using a practical example:

*   **Dataset**: Predicting whether a person will "play tennis" or not, based on independent features like **outlook, temperature, humidity, and wind**.
*   This is a **binary classification problem** (Yes/No for playing tennis).

### Step-by-Step Splitting Process:

1.  **Initial Root Node Selection**:
    *   Let's assume `Outlook` is chosen as the first feature (root node).
    *   **Total Data**: From the dataset, there are **9 'Yes'** (play tennis) and **5 'No'** (don't play tennis) outcomes.

2.  **Splitting based on `Outlook`**:
    *   `Outlook` has three unique categories: **Sunny, Overcast, and Rain**.
    *   So, the `Outlook` root node will split into **three branches**.

3.  **Analyzing Each Split's Purity**:

    *   **Sunny Outlook Branch**:
        *   If the outlook is "Sunny", you'll find **2 'Yes'** and **3 'No'** instances.
        *   **Impure Split**: Since it has both 'Yes' and 'No' outcomes, this is an **impure split**.
        *   **Action**: An impure split means you need to **further split this branch** using another feature (e.g., `Temperature`) to try and get a pure outcome.

    *   **Overcast Outlook Branch**:
        *   If the outlook is "Overcast", you'll find **4 'Yes'** and **0 'No'** instances.
        *   **Pure Split**: This is a **complete pure split** because all outcomes are 'Yes' (or could be all 'No').
        *   **Action**: A pure split is **good** because it forms a **leaf node**. A **leaf node** is a final node where you have a definitive 'Yes' or 'No' prediction. If outlook is overcast, the prediction is definitely 'play'.

    *   **Rain Outlook Branch**:
        *   If the outlook is "Rain", you'll find **3 'Yes'** and **2 'No'** instances.
        *   **Impure Split**: Similar to 'Sunny', this is an **impure split** as it contains both 'Yes' and 'No'.
        *   **Action**: This branch will also need **further splitting**.

## 6. Purity vs. Impurity - Mathematical Check

*   Visually, we can see if a split is pure or impure (e.g., all Yes or mixed Yes/No).
*   But to check this **mathematically**, we use two main techniques:
    1.  **Entropy**
    2.  **Gini Index** (or Gini Impurity)