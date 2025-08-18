# AdaBoost: Boosting and Ensemble Machine Learning

## Introduction to Ensemble Machine Learning

*   We're discussing **AdaBoost**, which falls under **boosting**.
*   Both **bagging** and **boosting** can solve **classification** and **regression** problems.
*   **Common base learner**: All these algorithms (bagging and boosting) primarily use **decision trees** as their fundamental building blocks.

## Decision Trees and Their Limitations

*   If a **decision tree** is grown to its **complete depth**, it usually leads to **overfitting**.
*   **Overfitting** means:
    *   **Training accuracy is very high**.
    *   **Test accuracy is very less**.
*   In terms of bias-variance: Overfitting signifies **low bias** (good on training data) and **high variance** (poor generalisation on new data).

## Boosting Technique 

*   In boosting, models (called **weak learners**) are connected **sequentially**.
*   **How it works**:
    *   It starts with a weak learner.
    *   **Key idea**: Whatever records were **wrongly predicted** by the first weak learner are **sent to the next weak learner** for correction.
    *   This process continues sequentially through all models.
*   **Weak Learner Definition**: A model that hasn't been trained properly or hasn't learned much from the training dataset.
*   **Goal of Boosting**: To combine multiple **weak learners sequentially** to form a **strong learner**.

## AdaBoost: A Specific Boosting Algorithm

*   AdaBoost is a type of boosting algorithm.
*   **Key Difference from Random Forest**: AdaBoost **does not use majority voting or averaging**.
*   **Core Principle**: AdaBoost **assigns weights** to its weak learners. This is a very important concept.
*   **AdaBoost Function Representation**:
    *   `f = α₁ * M₁ + α₂ * M₂ + ... + αₙ * Mₙ`
    *   Here:
        *   `M₁` to `Mₙ` are the **decision tree stumps** (which are the weak learners in AdaBoost).
        *   `α₁` to `αₙ` are the **weights assigned to these weak learners**.
*   AdaBoost can solve both **classification** and **regression** problems.

### Decision Tree Stumps in AdaBoost

*   **What is a Decision Tree Stump?**
    *   It's a decision tree whose **depth is just one level**.
    *   This single-level depth is why they are called "stumps".
*   **Why are stumps considered weak learners?**
    *   Because they have such limited depth, they are inherently weak.
    *   A single decision tree stump typically leads to **underfitting**.
*   **Underfitting Characteristics (for a single stump)**:
    *   **Training accuracy is less** (e.g., 40% training accuracy, 45% test accuracy).
    *   In terms of bias-variance: Initially, a decision tree stump has **high bias** (doesn't learn enough from training data) and **low variance** (it's not complex enough to vary much).

### Combining Stumps in AdaBoost & Bias-Variance Trade-off

*   When **multiple decision tree stumps** are combined **sequentially** (one after another) and **with weights**:
    *   The entire combination ultimately leads to **low bias** and **high variance**.
    *   This is the transformation AdaBoost aims for: reducing the initial high bias of individual weak learners.
