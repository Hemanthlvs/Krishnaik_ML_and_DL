# 📘 Logistic Regression Example with Hypothesis, Sigmoid, Cost & Gradient Descent

## 🔢 Sample Training Data

| i | x₁ | x₂ | x₃ | x₄ | y |
|---|----|----|----|----|---|
| 1 | 1  | 2  | 3  | 4  | 1 |
| 2 | 2  | 0  | 1  | 3  | 0 |
| 3 | 3  | 1  | 0  | 2  | 0 |

---

## ✅ Step 1: Logistic Hypothesis Function

- **Linear Equation:**  
  `z = θ₀ + θ₁x₁ + θ₂x₂ + θ₃x₃ + θ₄x₄`

- **Sigmoid Function:**  
  `hθ(x) = 1 / (1 + e⁻ᶻ)`


## 🧮 Initial θ values

θ₀ = 0.5,
θ₁ = 0.1,
θ₂ = 0.2,
θ₃ = 0.3,
θ₄ = 0.4.


## 🧠 Step 2: Compute z and hθ(x)

| i | x₁ | x₂ | x₃ | x₄ | z value                            | hθ(x) (sigmoid) |
|---|----|----|----|----|-------------------------------------|------------------|
| 1 | 1  | 2  | 3  | 4  | 0.5 + 0.1×1 + 0.2×2 + 0.3×3 + 0.4×4 = 3.5 | 0.9707           |
| 2 | 2  | 0  | 1  | 3  | 0.5 + 0.1×2 + 0.2×0 + 0.3×1 + 0.4×3 = 2.2 | 0.9002           |
| 3 | 3  | 1  | 0  | 2  | 0.5 + 0.1×3 + 0.2×1 + 0.3×0 + 0.4×2 = 1.8 | 0.8581           |


## 📉 Step 3: Cost Function (Log Loss)

- **Cost Equation per sample:**  
  `Cost = -y log(hθ(x)) - (1 - y) log(1 - hθ(x))`

| i | yᵢ | hθ(xᵢ) | Cost |
|---|----|--------|------|
| 1 | 1  | 0.9707 | -log(0.9707) = 0.0297 |
| 2 | 0  | 0.9002 | -log(1 - 0.9002) = 2.302 |
| 3 | 0  | 0.8581 | -log(1 - 0.8581) = 1.944 |

- **Total Cost (J):**  
  `J(θ) = (1/2m) * Σ costᵢ = (1/6) * (0.0297 + 2.302 + 1.944) ≈ 0.7126`



## 🔁 Step 4: Gradient Descent Update

- **Gradient Descent Formula:**  
  `θⱼ := θⱼ - α * (1/m) Σ (hθ(xᵢ) - yᵢ)·xⱼᵢ`  
  (for j = 0, 1, 2, 3, 4)

- **α (learning rate)** = 0.1  
- **m = 3**

### Compute Errors (hθ(xᵢ) - yᵢ):

| i | hθ(xᵢ) | yᵢ | Error |
|---|--------|----|-------|
| 1 | 0.9707 | 1  | -0.0293 |
| 2 | 0.9002 | 0  |  0.9002 |
| 3 | 0.8581 | 0  |  0.8581 |

### Partial Derivatives

- `∂J/∂θ₀ = (1/3) * Σ error = (−0.0293 + 0.9002 + 0.8581)/3 = 0.5763`
- `∂J/∂θ₁ = (1/3) * Σ error·x₁ = (−0.0293×1 + 0.9002×2 + 0.8581×3)/3 = 1.2951`
- `∂J/∂θ₂ = (1/3) * Σ error·x₂ = (−0.0293×2 + 0.9002×0 + 0.8581×1)/3 = 0.2665`
- `∂J/∂θ₃ = (1/3) * Σ error·x₃ = (−0.0293×3 + 0.9002×1 + 0.8581×0)/3 = 0.2805`
- `∂J/∂θ₄ = (1/3) * Σ error·x₄ = (−0.0293×4 + 0.9002×3 + 0.8581×2)/3 = 1.2761`

## 🆕 Step 5: Update θ values

Apply: `θⱼ = θⱼ - α * ∂J/∂θⱼ` where α = 0.1

| θⱼ  | Initial | Gradient | New θⱼ                |
|------|---------|----------|------------------------|
| θ₀  | 0.5     | 0.5763   | 0.5 - 0.1×0.5763 = 0.4424 |
| θ₁  | 0.1     | 1.2951   | 0.1 - 0.1×1.2951 = -0.0295 |
| θ₂  | 0.2     | 0.2665   | 0.2 - 0.1×0.2665 = 0.1733 |
| θ₃  | 0.3     | 0.2805   | 0.3 - 0.1×0.2805 = 0.2719 |
| θ₄  | 0.4     | 1.2761   | 0.4 - 0.1×1.2761 = 0.2724 |

## ✅ Final θ values after 1 step:

θ₀ = 0.4424,
θ₁ = -0.0295,
θ₂ = 0.1733,
θ₃ = 0.2719,
θ₄ = 0.2724.

Repeat the Gradient Descent steps until the cost function converges to minimum.

This is how **logistic regression** learns the best decision boundary.