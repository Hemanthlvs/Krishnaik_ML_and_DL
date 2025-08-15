# Lasso and Elastic Net

## Lasso Regression (L1 Regularization)

*   **Also known as**: **L1 regularization**.
*   **Primary Purpose**: For **feature selection**.
*   **How it Works (Feature Selection)**:
    *   **Cost Function**: Lasso regression adds a penalty term to the standard cost function: `(1/2m * Sum(h(x_i) - y_i)^2)` + `lambda * Sum(magnitude of slope)`. The "magnitude of slope" refers to the absolute value of the coefficients (theta).
    *   **Lambda (λ) and Slope/Coefficient Relationship**:
        *   If `lambda` (λ) is **zero**, it behaves like a normal gradient descent curve.
        *   As the `lambda` value **increases**, the `theta` (coefficient) values start to decrease.
        *   Crucially, after a certain point, the **`theta` value will become zero**.
        *   When a coefficient becomes zero, it means that specific feature is **removed from the model**.
    *   **Feature Removal**:
        *   Lasso identifies features that are **not highly correlated** with the output feature.
        *   These less important features will have **small coefficient values**.
        *   Lasso regression then **reduces these small coefficients to zero**, effectively removing the corresponding features from the equation.
        *   For example, if `theta_4` for feature `X_4` is `0.12` (small correlation), Lasso will make `theta_4` `0`, causing `0 * X_4` to become `0`, thus removing `X_4`.
    *   **Benefits of Feature Selection**: It automatically finds and removes features that are not highly correlated, resulting in a simpler and more efficient model.
*   **When to Use**:
    *   When you have **hundreds or many features**.
    *   It helps to automatically identify and remove features that are not highly correlated.
*   **Relationship to Linear Regression**: It is a method for **hyperparameter tuning linear regression**.

# 📘 Lasso Regression (L1 Regularization) — Feature Deletion Example

---

## 📊 Sample Dataset

| i | x₁ | x₂ | x₃ | x₄ | y |
|--:|----|----|----|----|----|
| 1 | 1  | 2  | 3  | 4  | 10 |
| 2 | 2  | 0  | 1  | 3  | 12 |
| 3 | 3  | 1  | 0  | 2  | 13 |

---

## ⚙️ Initial Setup

- Initial parameters: `θ = [θ₀, θ₁, θ₂, θ₃, θ₄] = [0.5, 0.1, 0.2, 0.3, 0.4]`
- Learning rate: `α = 0.01`
- Regularization parameter: `λ = 1`
- Number of examples: `m = 3`

---

## 🧮 Formulas Used

### Hypothesis:
```
h(xᵢ) = θ₀ + θ₁·x₁ + θ₂·x₂ + θ₃·x₃ + θ₄·x₄
```

### Lasso Cost Function:
```
J(θ) = (1 / 2m) · Σ(h(xᵢ) - yᵢ)² + λ · Σ|θⱼ|   (j ≥ 1)
```

### Gradient Descent Update Rule:
```
For θ₀:
θ₀ := θ₀ - α · (1/m) · Σ(h(xᵢ) - yᵢ)

For θⱼ (j ≥ 1):
θⱼ := θⱼ - α · [ (1/m) · Σ(h(xᵢ) - yᵢ)·xⱼᵢ + λ·sign(θⱼ) ]
```

Where:
- `sign(θⱼ) = +1` if `θⱼ > 0`
- `sign(θⱼ) = -1` if `θⱼ < 0`
- `sign(θⱼ) = 0` if `θⱼ = 0`

---

## 🔁 Step 1: Compute Predictions

Using:
```
h(xᵢ) = θ₀ + θ₁·x₁ + θ₂·x₂ + θ₃·x₃ + θ₄·x₄
```

| i | h(xᵢ)                  |
|--:|------------------------|
| 1 | 0.5 + 0.1·1 + 0.2·2 + 0.3·3 + 0.4·4 = **3.5** |
| 2 | 0.5 + 0.1·2 + 0.2·0 + 0.3·1 + 0.4·3 = **2.2** |
| 3 | 0.5 + 0.1·3 + 0.2·1 + 0.3·0 + 0.4·2 = **1.8** |

---

## ❌ Step 2: Compute Errors

```
Errorᵢ = h(xᵢ) - yᵢ
```

| i | h(xᵢ) | yᵢ | Error |
|--:|------|----|-------|
| 1 | 3.5  | 10 | -6.5  |
| 2 | 2.2  | 12 | -9.8  |
| 3 | 1.8  | 13 | -11.2 |

---

## 📉 Step 3: Gradient with L1 Regularization

For each parameter:

```
θⱼ := θⱼ - α · [ (1/m) · Σ(errorᵢ · xⱼᵢ) + λ · sign(θⱼ) ]
θ₀ is updated normally without λ term
```

### Gradients:

| θⱼ  | Values of xⱼᵢ | ∑(error·xⱼᵢ) | (1/m) Term | λ·sign(θⱼ) | Final Gradient | Δθⱼ     |
|-----|----------------|---------------|------------|-------------|----------------|----------|
| θ₀  | [1, 1, 1]      | -27.5         | -9.167     | 0           | -9.167         | -0.0917  |
| θ₁  | [1, 2, 3]      | -59.7         | -19.9      | +1          | -18.9          | -0.1890  |
| θ₂  | [2, 0, 1]      | -24.2         | -8.067     | +1          | -7.067         | -0.0707  |
| θ₃  | [3, 1, 0]      | -29.3         | -9.767     | +1          | -8.767         | -0.0877  |
| θ₄  | [4, 3, 2]      | -77.8         | -25.933    | +1          | -24.933        | -0.2493  |

---

## 🆕 Step 4: Update Parameters

| θⱼ  | Old Value | Δθⱼ     | New Value |
|-----|-----------|---------|-----------|
| θ₀  | 0.5       | -0.0917 | 0.5917    |
| θ₁  | 0.1       | -0.1890 | 0.2890    |
| θ₂  | 0.2       | -0.0707 | 0.2707    |
| θ₃  | 0.3       | -0.0877 | 0.3877    |
| θ₄  | 0.4       | -0.2493 | 0.6493    |

---

## 🔁 Step 5: Repeat Gradient Descent

After multiple iterations, smaller coefficients (like `θ₂`) continue shrinking.

Eventually:

| Iteration | θ₂     |
|-----------|--------|
| ...       | 0.01   |
| ...       | 0.005  |
| ...       | 0.0001 |
| ...       | 0      |

### ✅ Feature Deletion

- When `θ₂ = 0`, feature `x₂` is **removed** from the model
- Because `θ₂·x₂ = 0`, it no longer contributes to the prediction

---

## 📉 Final Hypothesis (after feature deletion)

```
h(xᵢ) = θ₀ + θ₁·x₁ + θ₃·x₃ + θ₄·x₄
```

---

## 🎯 Summary

- Lasso uses **L1 penalty**: `λ · Σ|θⱼ|`
- It **shrinks coefficients**, and can **set them to zero**
- When `θⱼ = 0`, that feature is **eliminated**
- Useful for **automatic feature selection**
- Repeat gradient descent until convergence or until features are removed

