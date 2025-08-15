# Ridge Regression (L2 Regularization)

## Ridge Regression: The Solution to Overfitting

*   **Purpose**: **Ridge Regression** is used specifically to **reduce overfitting** in linear regression models.
*   **Alternative Name**: It is also known as **L2 Regularization**.
*   **Role**: It acts as an algorithm to **hyperparameter tune** linear regression, preventing it from perfectly fitting the training data.

## Cost Function of Ridge Regression (L2 Regularization)

*   **Linear Regression Cost Function**:
    *   `J(θ) = (1/2m) * Σ(h_θ(xᵢ) - yᵢ)²`.
    *   This term can become zero if the model perfectly fits the training data, indicating overfitting.
*   **Ridge Regression Cost Function**:
    *   To prevent the cost function from reaching zero and thus mitigate overfitting, Ridge Regression adds a **penalty term**.
    *   **Modified Cost Function**:
        `J_ridge(θ) = (1/2m) * Σ(h_θ(xᵢ) - yᵢ)² + λ * Σ(θⱼ)²`
        *   The first part is the standard Mean Squared Error (MSE).
        *   **`λ` (Lambda)**: This is a **hyperparameter**. It controls the strength of the regularization.
        *   **`Σ(θⱼ)²` (Sum of Slope Squares)**: This is the sum of the squares of the coefficients (slopes). The intercept term is typically not included in this penalty.
*   **Mechanism**:
    *   By adding `λ * Σ(θⱼ)²`, the cost function is **penalized**, ensuring it never becomes exactly zero, even if the model tries to perfectly fit all training points.
    *   This forces the model to find a best-fit line that does not pass exactly through all training data points, thus **preventing overfitting**.

## Relationship Between Lambda (λ) and Slope (θ)

*   **Visualizing the Relationship (Gradient Descent Plot)**:
    *   Consider a plot of **`J(θ)` (Cost Function) vs. `θ` (Slope)**.
    *   **When `λ = 0`**:
        *   The penalty term `λ * Σ(θⱼ)²` becomes zero.
        *   The Ridge Regression cost function reverts to the standard linear regression cost function.
        *   The global minima corresponds to the original linear regression solution.
    *   **When `λ > 0` (Increasing Lambda)**:
        *   As `λ` increases, the penalty term becomes more significant.
        *   The **global minima of the cost function shifts**, moving the optimal `θ` value closer to zero.
        *   This demonstrates that **as `λ` increases, the slope (coefficient) values (`θ`) decrease**.
        *   **Crucial Point**: Even as `λ` increases significantly, the slope values (`θ`) will **never become exactly zero**. This is a key distinguishing feature from Lasso Regression.

## How Ridge Regression Reduces Overfitting by Influencing Coefficients

*   **Interpretation of Coefficients**:
    *   In a multi-linear regression, each coefficient indicates the unit movement in the dependent variable for a unit movement in the corresponding independent feature.
    *   Larger coefficients suggest a stronger correlation between the feature and the output.
*   **Impact of Ridge Regression on Coefficients**:
    *   Ridge Regression **reduces the magnitude of all coefficients**.
    *   It particularly **reduces the impact of features that are not strongly correlated** with the output feature.
        *   Example: If `x1` has a very small coefficient (e.g., 0.24), Ridge Regression will further reduce it (e.g., to 0.14).
    *   By shrinking these coefficients, even if they are not zero, the features that have little direct impact on the output will contribute less to the model, thus **smoothing the best-fit line/plane** and **reducing its sensitivity to minor fluctuations in training data**, which combats overfitting.
    *   Again, remember that coefficients are reduced but **never become zero**.


# 📘 Ridge Regression (L2 Regularization) - Simple Example

## Dataset

| i | x₁ | x₂ | x₃ | x₄ | y |
|--:|----|----|----|----|----|
| 1 | 1  | 2  | 3  | 4  | 10 |
| 2 | 2  | 0  | 1  | 3  | 12 |
| 3 | 3  | 1  | 0  | 2  | 13 |

Initial θ = [0.5, 0.1, 0.2, 0.3, 0.4]  
Learning rate (α) = 0.01  
Regularization parameter (λ) = 1  
m (examples) = 3

---

## 🧠 Hypothesis Function

```
h(xᵢ) = θ₀ + θ₁·x₁ + θ₂·x₂ + θ₃·x₃ + θ₄·x₄
```

Predictions:
- h(x₁) = 3.5
- h(x₂) = 2.2
- h(x₃) = 1.8

---

## ❌ Errors

```
Error = h(xᵢ) - yᵢ
```

- Error₁ = -6.5  
- Error₂ = -9.8  
- Error₃ = -11.2

---

## 🔁 Ridge Gradient Descent Update

### Gradient Formula (with L2):
```
θⱼ := θⱼ - α * [(1/m) * Σ(Errorᵢ · xⱼᵢ) + λ·θⱼ]  
(Note: no λ term for θ₀)
```

### Gradients:

| θⱼ  | Gradient (with λ) | Update Δθⱼ     |
|-----|--------------------|----------------|
| θ₀  | -27.5              | -0.0917        |
| θ₁  | -59.6              | -0.1987        |
| θ₂  | -24.0              | -0.0800        |
| θ₃  | -29.0              | -0.0967        |
| θ₄  | -77.4              | -0.2580        |

---

## ✅ Updated Parameters

| θⱼ  | Old Value | New Value      |
|-----|-----------|----------------|
| θ₀  | 0.5       | **0.5917**     |
| θ₁  | 0.1       | **0.2987**     |
| θ₂  | 0.2       | **0.2800**     |
| θ₃  | 0.3       | **0.3967**     |
| θ₄  | 0.4       | **0.6580**     |

---

## 🧾 Ridge Cost Function

```
J_ridge(θ) = (1/2m) * Σ(h(xᵢ) - yᵢ)² + λ * Σ(θⱼ²) for j > 0
```

## 📌 Key Points

- λ = 0 → standard linear regression
- λ > 0 → smaller θ values, less overfitting
- Larger λ → more shrinkage
