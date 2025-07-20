## Ordinary Least Squares (OLS) for Linear Regression Coefficients

| Term              | Meaning                                                               |
| ----------------- | --------------------------------------------------------------------- |
| **Loss Function** | Measures the error for **one data point** (single prediction)         |
| **Cost Function** | Measures the **average error** across the **entire training dataset** |


### 1. Introduction: OLS vs. Gradient Descent
*   **Linear Regression** aims to find the **best fit line** for a given set of data points.
*   **Gradient Descent** achieves this by using an **optimization algorithm** that involves a **loss function** (e.g., Mean Squared Error). It calculates derivatives at every point to iteratively move towards the **global minima** of the loss function.
*   **Ordinary Least Squares (OLS)** offers an alternative approach. Instead of an iterative optimization, OLS directly provides **formulas to calculate** the **intercept (beta zero)** and the **coefficient (beta one)** of the best fit line.

### 2. Aim of OLS
*   The primary goal of OLS, similar to Gradient Descent, is to **reduce the error** between the **predicted values** and the **actual (truth) data points**.
*   It seeks to **select the line that results in the least error**.
*   Specifically, OLS aims to minimize the **difference between `y_i` (actual value) and `y_hat` (predicted value)**.
*   This error calculation inherently resembles the **Mean Squared Error (MSE) formula**.

### 3. The Linear Regression Model
*   For a simple linear regression, the best fit line is represented by the equation:
    **`h_theta(x) = beta_zero + beta_one * x_one`**
    *   Here, `h_theta(x)` is the **predicted value (`y_hat`)**.
    *   **`beta_zero`** is the **intercept**.
    *   **`beta_one`** is the **coefficient**.

### 4. Deriving the OLS Formulas (Conceptual Overview)
*   To find the formulas for `beta_zero` and `beta_one`, OLS uses a method similar to how global minima are found in gradient descent: by calculating **derivatives** and setting them to **zero**.
*   The process involves:
    1.  Defining the error term (similar to MSE).
    2.  Taking the **derivative of this error term with respect to `beta_zero`** and setting it to zero. This leads to the "first equation".
    3.  Taking the **derivative of this error term with respect to `beta_one`** and setting it to zero. This leads to the "second equation".
    4.  These two equations are then algebraically **simplified** to derive the explicit formulas for `beta_zero` and `beta_one`.

### 5. OLS Formulas for Intercept and Coefficient

*   **Formula for Intercept (`beta_zero`)**:
    Derived from the first equation, after simplification.
    **`beta_zero = y_bar - beta_one * x_bar`**
    *   Where:
        *   `y_bar` is the **average of all `y` values** (`summation of y_i / n`).
        *   `x_bar` is the **average of all `x` values** (`summation of x_i / n`).

*   **Formula for Coefficient (`beta_one`)**:
    Derived from the second equation, by substituting the `beta_zero` formula and further simplification.
    **`beta_one = (summation of (y_i - y_bar) * (x_i - x_bar)) / (summation of (x_i - x_bar)^2)`**
    
### 6. Steps to Calculate `beta_zero` and `beta_one` for a Dataset
1.  **Calculate `x_bar` and `y_bar`**: Find the average of your `x` values and `y` values.
2.  **Calculate `beta_one` first**: Use the formula for `beta_one`. This requires:
    *   Calculating `(y_i - y_bar)` for each `y` value.
    *   Calculating `(x_i - x_bar)` for each `x` value.
    *   Then, computing the summation of their product for the numerator and the summation of squared `(x_i - x_bar)` for the denominator.
3.  **Calculate `beta_zero` second**: Once `beta_one` is determined, substitute its value, along with `x_bar` and `y_bar`, into the `beta_zero` formula: `beta_zero = y_bar - beta_one * x_bar`.

### 7. Application Notes
*   These derived formulas are specifically for **simple linear regression** (one independent variable). The equations would change for multiple linear regression, involving more components.
*   When implemented, the OLS method provides results (beta values) that are **approximately the same** as those obtained from standard linear regression implementations, such as those found in `sklearn` libraries.

### When NOT to use OLS:
*	You have millions of features (inverting a large matrix is very slow or impossible).
*	You're using logistic regression, neural networks, or non-linear models — OLS doesn't work there.
*	You want to train on batches (e.g. in deep learning).