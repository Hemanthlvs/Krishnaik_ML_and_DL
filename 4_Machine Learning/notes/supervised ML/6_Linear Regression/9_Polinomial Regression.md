# Polynomial Regression

## 1. Introduction to Polynomial Regression
*   Polynomial Regression is a **machine learning algorithm**.
*   It's an extension of **Simple Linear Regression** and **Multiple Linear Regression**.
*   Simple Linear Regression uses **one independent feature (x)** and **one dependent feature (y)**, aiming to create a **best fit line**.
*   Multiple Linear Regression is used for **more than one input feature**, aiming to create a **plane** (e.g., a 3D plane for three dimensions) or a **hyperplane** for more than three dimensions.
*   "Simple" in simple linear regression means there's **only one independent feature**, while "multiple" means **more than one independent feature**.

## 2. Why Polynomial Regression? Addressing Non-Linear Relationships
*   Linear regression models (simple or multiple) are suitable when there is a **linear relationship** between features.
*   However, if the **data points show a curve** and have a **non-linear relationship**, a simple best fit line will lead to a **high error** or **loss value** (difference between truth and predicted values).
*   In such cases, **linear regression cannot be used** effectively.
*   Polynomial Regression is needed to **identify and capture non-linear relationships** in data, allowing for more accurate predictions with **less error**.
*   Its main purpose is to **solve non-linear relationship data points** between independent and dependent features.

## 3. The Concept of Polynomial Degrees
*   A key concept in polynomial regression is **polynomial degrees**.
*   The degree affects the shape of the "best fit line" or curve.

### Simple Polynomial Regression (One Independent Feature)
*   **Polynomial Degree is Zero (0):**
    *   The equation looks like: `h(x) = β0`.
    *   This is a **constant value**. It's equivalent to `β0 * x0`, where `x0` is 1.
*   **Polynomial Degree is One (1):**
    *   The equation looks like: `h(x) = β0 * x0 + β1 * x¹`.
    *   This simplifies to `h(x) = β0 + β1x`.
    *   This is **equivalent to Simple Linear Regression**.
*   **Polynomial Degree is Two (2):**
    *   The equation looks like: `h(x) = β0 * x0 + β1 * x¹ + β2 * x²`.
    *   This means the input feature `x` is also squared.
*   **Polynomial Degree is 'N':**
    *   The general equation for a simple polynomial regression up to degree `N` is:
        `h(x) = β0 * x0 + β1 * x¹ + β2 * x² + ... + βn * xⁿ`.

### How Degrees Affect the Fit
*   As the polynomial degree **increases**, the best fit line or curve becomes **more flexible** and can **fit the data points more properly**, capturing the non-linear patterns.

## 4. Overfitting, Underfitting, and Generalization
*   If the polynomial degree is **too high** (e.g., 15), the model might start **overfitting** the data points.
    *   **Overfitting** means the model fits the training data too closely, capturing noise and performing poorly on new, unseen data.
*   If the degree is **too low** (e.g., trying to fit a curve with a straight line), it might **underfit** the model.
    *   **Underfitting** means the model is too simple and cannot capture the underlying pattern of the data.
*   The goal is to **select a degree value that generalizes the model**.
    *   **Generalization** means the model performs well on both seen and unseen data, effectively capturing the true relationship without overfitting or underfitting.

## 5. Polynomial Regression with Multiple Independent Features
*   The concept extends to multiple independent features (e.g., x1, x2).
*   **Polynomial Degree is One (1) with two features (x1, x2):**
    *   `h(x) = β0 + β1x1 + β2x2`. This is equivalent to Multiple Linear Regression.
*   **Polynomial Degree is Two (2) with two features (x1, x2):**
    *   `h(x) = β0 + β1x1 + β2x2 + β3x1² + β4x2²`.
    *   For every input feature, you also include its squared term.
*   This technique continues for higher degrees and more independent features (e.g., `β5x1³`, `β6x2³` for degree three).