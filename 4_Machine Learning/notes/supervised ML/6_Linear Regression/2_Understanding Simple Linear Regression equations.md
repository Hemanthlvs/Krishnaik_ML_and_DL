# Simple Linear Regression

## 1. Main Aim
*   The main aim of simple linear regression is to **create the best fit line** for a given dataset.
*   This line helps to understand the relationship between variables and make predictions.

## 2. Key Notations and Concepts

### A. Equation of the Best Fit Line
*   The equation used to represent the best fit line is: **`h_theta(x) = theta_zero + theta_one * x`**.
    *   Other common forms include `y = mx + c` or `y = beta_zero + beta_one * x`.

### B. Variables and Coefficients

*   **x (Independent Feature):** This is the input variable, like 'weight' in the example. It's on the x-axis.
*   **theta_zero (θ0) - Intercept:**
    *   This is the point where the best fit line **crosses the y-axis**.
    *   It represents the value of `h_theta(x)` when the `x` value is zero.
    *   Think of it as the starting point of your line on the y-axis.
*   **theta_one (θ1) - Slope or Coefficient:**
    *   This indicates the **change in the y-axis for a unit movement in the x-axis**.
    *   It shows how steep the line is and in which direction it moves.
    *   If there were multiple independent features (like `X1`, `X2`, `X3`), you would have a `theta` (slope) for each, like `theta_one`, `theta_two`, `theta_three`, etc..

### C. Predicted vs. Actual Values

*   **h_theta(x) or y_hat (ŷ) - Predicted Point:**
    *   This is the **predicted output value** (e.g., predicted height) that the best fit line gives for a given `x` (e.g., weight).
    *   It's what the model "guesses" based on the line.
*   **y - True Point:**
    *   This is the **actual output value** from your original dataset (e.g., actual height).

## 3. Understanding Error

*   **Error:** The **difference between the true `y` point and the predicted `y_hat` point** (`y - y_hat`).
    *   It measures how far off your prediction is from the actual value for a specific data point.
*   **Goal with Error:** The main aim is to find a best fit line where the **summation of all these errors is as minimal as possible**.
    *   If another line produces a smaller total error, that line is chosen as the "best fit".

## 4. Creating the Best Fit Line (Optimization)

*   Instead of randomly drawing many lines and calculating their total errors to find the minimal one, there's an **optimized way**.
*   This optimized process involves **changing the values of `theta_zero` (intercept) and `theta_one` (coefficient)**.
*   By adjusting these two values, the system systematically searches for the line that results in the **minimal error**.