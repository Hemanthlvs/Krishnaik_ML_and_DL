### Multiple Linear Regression

#### Simple Linear Regression
*   **Purpose**: To predict an output feature based on **one input or independent feature**.
    *   *Example*: Predicting height based on weight.
*   **Equation (Best Fit Line)**: `h(x) = θ0 + θ1 * x`.
    *   `x` represents the **single input feature**.
    *   `θ0` is the **intercept**.
    *   `θ1` is the **slope** (or coefficient) for the input feature.
*   **Goal**: To find the "best fit line" by changing the values of `θ0` and `θ1`.

#### Multiple Linear Regression
*   **Purpose**: To predict an output feature when you have **multiple input features**.
    *   This is the **basic difference**: more than one input feature.
*   **Example (House Pricing Data Set)**:
    *   **Input Features**: Number of rooms, size of the house, location.
    *   **Output Feature**: Price of the house.
    *   In this example, there are four features in total, with the first three being input features and the last one being the output.
*   **Equation (Best Fit Line)**: `h(x) = θ0 + θ1 * x1 + θ2 * x2 + θ3 * x3`.
    *   **`θ0` is always the intercept** and there will always be only **one intercept** for any regression problem.
    *   `x1`, `x2`, `x3` represent the multiple input features.
    *   `θ1`, `θ2`, `θ3` are the **slopes or coefficients** for each corresponding input feature.
*   **Key Concept**: As the **number of input features increases, the number of coefficients will increase** (one coefficient per feature), but the intercept `θ0` remains singular.
*   **Convergence (Gradient Descent)**:
    *   With multiple features, you need to change **many coefficients**.
    *   The aim is to **reduce the cost function `J(θ)`**.
    *   The goal is to reach a **global minima**, which can be visualized as the bottom of an "inverted mountain" in a gradient descent curve. This means all coefficients converge to their optimal values.

#### Conclusion
*   **Simple Linear Regression**: One input feature.
*   **Multiple Linear Regression**: More than one input feature.