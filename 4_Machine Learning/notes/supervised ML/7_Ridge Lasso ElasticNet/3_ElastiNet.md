## Elastic Net Regression

*   **Definition**: It is a **combination of both Ridge and Lasso regression**.
*   **Primary Purposes**: Solves **both problems simultaneously**.
    *   **Reduces overfitting**.
    *   Performs **feature selection**.
*   **Cost Function**: It incorporates both the L1 (Lasso) and L2 (Ridge) penalty terms in its cost function.
    *   `Cost Function = (1/2m * Sum(h(x_i) - y_i)^2)`
        *   `+ lambda_1 * Sum(slope^2)` (for **reducing overfitting**)
        *   `+ lambda_2 * Sum(magnitude of slope)` (for **feature selection**)
*   **When to Use**: When a model is **overfitting** AND has **a lot of features**.
*   **Relationship to Linear Regression**: It is a method for **hyperparameter tuning linear regression**.

# 📘 Elastic Net Regression — With Example

## 🔢 Dataset

| i | x₁ | x₂ | x₃ | x₄ | y  |
|--:|----|----|----|----|----|
| 1 | 1  | 2  | 3  | 4  | 10 |
| 2 | 2  | 0  | 1  | 3  | 12 |
| 3 | 3  | 1  | 0  | 2  | 13 |

---

## ⚙️ Settings

- Initial parameters:  
  `θ = [θ₀, θ₁, θ₂, θ₃, θ₄] = [0.5, 0.1, 0.2, 0.3, 0.4]`

- Learning rate:  
  `α = 0.01`

- Regularization constants:  
  `λ₁ (L2) = 1`, `λ₂ (L1) = 1`

- Number of examples:  
  `m = 3`

---

## 🧮 Hypothesis Function

```
h(xᵢ) = θ₀ + θ₁·x₁ + θ₂·x₂ + θ₃·x₃ + θ₄·x₄
```

---

## 🧠 Step 1: Compute Predictions

| i | θ₀ | θ₁·x₁ | θ₂·x₂ | θ₃·x₃ | θ₄·x₄ | h(xᵢ) |
|--:|-----|--------|--------|--------|--------|--------|
| 1 | 0.5 | 0.1    | 0.4    | 0.9    | 1.6    | 3.5    |
| 2 | 0.5 | 0.2    | 0      | 0.3    | 1.2    | 2.2    |
| 3 | 0.5 | 0.3    | 0.2    | 0      | 0.8    | 1.8    |

---

## ❌ Step 2: Compute Errors

```
Errorᵢ = h(xᵢ) - yᵢ
```

| i | h(xᵢ) | yᵢ | Errorᵢ |
|--:|-------|----|--------|
| 1 | 3.5   | 10 | -6.5   |
| 2 | 2.2   | 12 | -9.8   |
| 3 | 1.8   | 13 | -11.2  |

---

## 🔄 Step 3: Gradient Descent Update

### 🔸 General Formula

For intercept (θ₀):  
```
θ₀ := θ₀ - α * (1/m) * Σ(h(xᵢ) - yᵢ)
```

For j ≥ 1 (θ₁ to θ₄):  
```
θⱼ := θⱼ - α * [ (1/m) * Σ(errorᵢ · xⱼᵢ) + λ₁ * 2θⱼ + λ₂ * sign(θⱼ) ]
```

---

### 🔢 Compute Gradients and Updates

| θⱼ  | xⱼᵢ        | Σ(errorᵢ·xⱼᵢ) | MSE Grad = (1/m)·Σ | L2 = 2θⱼ | L1 = sign(θⱼ) | Total Grad = MSE + L2 + L1 | Update = -α·Grad | New θⱼ |
|------|-------------|----------------|------------------|----------|----------------|----------------------------|------------------|--------|
| θ₀  | [1,1,1]     | -27.5           | -9.167           | 0        | 0              | -9.167                     | +0.0917          | 0.5917 |
| θ₁  | [1,2,3]     | -59.7           | -19.9            | 0.2      | 1              | -18.7                      | +0.187           | 0.287  |
| θ₂  | [2,0,1]     | -24.2           | -8.067           | 0.4      | 1              | -6.667                     | +0.0667          | 0.2667 |
| θ₃  | [3,1,0]     | -29.3           | -9.767           | 0.6      | 1              | -8.167                     | +0.0817          | 0.3817 |
| θ₄  | [4,3,2]     | -77.8           | -25.933          | 0.8      | 1              | -24.133                    | +0.2413          | 0.6413 |

---

## 📈 Step 4: Updated Parameters

| Parameter | Before | After   |
|-----------|--------|---------|
| θ₀        | 0.5    | 0.5917  |
| θ₁        | 0.1    | 0.287   |
| θ₂        | 0.2    | 0.2667  |
| θ₃        | 0.3    | 0.3817  |
| θ₄        | 0.4    | 0.6413  |

---

## 🔁 Repeat Process

- L1 (`λ₂`) will push small θⱼ values toward **zero** → Feature Selection  
- L2 (`λ₁`) keeps large θⱼ values **small** → Controls Overfitting  
- After several iterations, some coefficients may become **zero**, eliminating features

---

## ✅ Elastic Net Summary

Elastic Net combines:
- **Ridge (L2)** for preventing overfitting
- **Lasso (L1)** for automatic feature selection  
It is ideal when:
- The model has **many features**
- There's a **risk of overfitting**