# PCA: Conquering the Curse of Dimensionality

## 1. Introduction to PCA

*   **PCA** stands for **Principal Component Analysis**.
*   It's a **machine learning algorithm**.
*   It's also known as **Dimensionality Reduction**.

## 2. Why do we need PCA? Understanding the "Curse of Dimensionality"

*   Before understanding PCA, we need to know *why* we use it, which involves understanding the **"Curse of Dimensionality"**.
*   **Dimensionality** basically means **dimensions**, and dimensions are nothing but **features**.

### The Problem: Curse of Dimensionality

*   Let's consider a dataset with, say, 500 features, used to determine house prices (e.g., house size, number of bedrooms, bathrooms).

*   We train multiple Machine Learning models (M1, M2, M3, M4, M5, M6) by increasing the number of features given to each.
    *   M1: 3 important features -> Accuracy 1
    *   M2: 6 features (all important) -> Accuracy 2 (Accuracy 2 > Accuracy 1)
    *   M3: 15 features (more important) -> Accuracy 3 (Accuracy 3 > Accuracy 2)
    *   M4: 50 features -> Accuracy 4 (Accuracy 4 < Accuracy 3)
    *   M5: 100 features -> Accuracy 5 (Accuracy 5 < Accuracy 4)
    *   M6: 500 features (all features) -> Accuracy 6 (Accuracy 6 < Accuracy 5)

*   **Observation**: Initially, as we increase the number of *important* features (M1 to M3), the model's **accuracy increases**.
*   However, after a certain point (from M4 onwards), even if we keep adding features, the **accuracy starts decreasing**.

### Why does accuracy decrease?

1.  **Overfitting**:
    *   When we provide too many features, especially those that are not very important or have less importance, the model starts **overfitting**.
    *   The model doesn't need that many features to make predictions.
    *   It tries to learn even the unimportant features, leading to **confusion** within the model.
    *   Machine learning algorithms are essentially **mathematical equations**. As you feed more features, they try to learn everything, even if it's not important, causing overfitting.

2.  **Degraded Model Performance**:
    *   As the number of features (dimensions) increases, the **model's performance degrades**.
    *   This is because more **mathematical calculations** are required for that many dimensions, which slows down and confuses the model.

### Analogy: Human Domain Expert Example

*   Imagine asking a person (a domain expert) for the house price in a location.
*   If you give them only a few important features (e.g., location, 3 BHK), they can give you a good estimate, and the price will increase logically.
*   But, if you keep adding too many features, some less important (e.g., "near a celebrity house," "lots of grocery shops nearby," "number of schools"):
    *   The person will get **confused**.
    *   They might not be able to tell you the proper or accurate price.
    *   Their **performance decreases**.
*   This is exactly what happens with our models when we feed them too many features – it's the **Curse of Dimensionality**.

## 3. How to prevent/remove the Curse of Dimensionality?

There are two main ways to handle the curse of dimensionality:

1.  **Feature Selection**:
    *   In this technique, we **select the most important features** from the dataset.
    *   Then, we train our model only using these selected important features.

2.  **Dimensionality Reduction** (also called **Feature Extraction**):
    *   This is the technique we are focusing on, and **PCA** is a key algorithm within this.
    *   In **feature extraction**, we **derive new features from a set of existing features**.
    *   The goal is to **capture the "essence" or "much variance"** of the original features into these new, derived features.
    *   For example, if you have F1, F2, F3 (original features), we'll derive new features like D1, D2 (which will be in **lesser dimensions**) from them.
    *   These derived features (D1, D2) will be used to train the model, and they are designed to perform well because they capture the crucial information from the original features.
    *   We are essentially **extracting new information** in a condensed form.