# 🌲 Gradient Boosting: Full Explanation with Examples

Gradient Boosting is an ensemble learning method that builds models sequentially. Each model corrects the errors made by the previous model. It's used for both **regression** and **classification** problems.

---

# 🌲 Gradient Boosting with Weighted Trees — Regression Example

This example demonstrates how Gradient Boosting uses the additive model:

**f(x) = H₀(x) + α₁·H₁(x) + α₂·H₂(x) + α₃·H₃(x) + ... + αₙ·Hₙ(x)**

Where:
- `H₀(x)` is the initial prediction (usually the mean of target `y`)
- `H₁(x), H₂(x), ...` are the weak learners (e.g. decision trees)
- `α₁, α₂, ...` are scaling factors (often = learning rate)
- `f(x)` is the final prediction

---

## 📊 Dataset

| Sample | Feature X | Target Y |
|--------|-----------|----------|
| 1      | 1         | 5        |
| 2      | 2         | 7        |
| 3      | 3         | 9        |
| 4      | 4         | 11       |
| 5      | 5         | 15       |

---

## 🔢 Step 1: Initial Model `H₀(x)`

We start by predicting the **mean** of Y for every sample:

H₀(x) = (5 + 7 + 9 + 11 + 15) / 5 = 9.4

So:  
f₀(x) = 9.4 for all `x`

---

## 🧮 Step 2: Compute Residuals

Residuals = Y − H₀(x)

| Sample | Y | H₀(x) | Residual R₁ |
|--------|---|--------|-------------|
| 1      | 5 | 9.4    | -4.4        |
| 2      | 7 | 9.4    | -2.4        |
| 3      | 9 | 9.4    | -0.4        |
| 4      | 11| 9.4    | +1.6        |
| 5      | 15| 9.4    | +5.6        |

---

## 🌳 Step 3: Fit Weak Learner H₁(x)

Train a regression tree to predict **R₁** (residuals) from `X`.

Let it learn the following simple rules:

- If X ≤ 2 → predict -3.4  
- If 2 < X ≤ 4 → predict +0.6  
- If X > 4 → predict +5.6

Set learning rate `α₁ = 0.1`

---

## 🔄 Step 4: Update Prediction f₁(x)

f₁(x) = H₀(x) + α₁·H₁(x)

| Sample | H₀(x) | H₁(x) | α₁·H₁(x) | f₁(x) = H₀ + α₁·H₁ |
|--------|--------|--------|-----------|----------------------|
| 1      | 9.4    | -3.4   | -0.34     | 9.06                 |
| 2      | 9.4    | -3.4   | -0.34     | 9.06                 |
| 3      | 9.4    | +0.6   | +0.06     | 9.46                 |
| 4      | 9.4    | +0.6   | +0.06     | 9.46                 |
| 5      | 9.4    | +5.6   | +0.56     | 9.96                 |

---

## ♻️ Step 5: Repeat with New Residuals

Residual R₂ = Y − f₁(x)

| Sample | Y  | f₁(x) | R₂    |
|--------|----|--------|--------|
| 1      | 5  | 9.06   | -4.06  |
| 2      | 7  | 9.06   | -2.06  |
| 3      | 9  | 9.46   | -0.46  |
| 4      | 11 | 9.46   | +1.54  |
| 5      | 15 | 9.96   | +5.04  |

Train H₂(x) on R₂, and get new predictions. Suppose:

- X ≤ 2 → predict -3.06  
- 2 < X ≤ 4 → predict +0.54  
- X > 4 → predict +5.04

Set α₂ = 0.1

---

## 🔄 Step 6: Update Prediction f₂(x)

f₂(x) = f₁(x) + α₂·H₂(x)

| Sample | f₁(x) | H₂(x) | α₂·H₂(x) | f₂(x) = f₁ + α₂·H₂ |
|--------|--------|--------|-----------|----------------------|
| 1      | 9.06   | -3.06  | -0.306    | 8.754                |
| 2      | 9.06   | -3.06  | -0.306    | 8.754                |
| 3      | 9.46   | +0.54  | +0.054    | 9.514                |
| 4      | 9.46   | +0.54  | +0.054    | 9.514                |
| 5      | 9.96   | +5.04  | +0.504    | 10.464               |

---

## 📘 Final Prediction Formula

So far we used:

- H₀(x) = 9.4  
- H₁(x) = weak tree #1  
- H₂(x) = weak tree #2  
- α₁ = α₂ = 0.1

Final model:

**f(x) = H₀(x) + α₁·H₁(x) + α₂·H₂(x)**  
That is:

**f(x) = 9.4 + 0.1·H₁(x) + 0.1·H₂(x)**

We keep adding more weak learners (trees) on new residuals.

---

## ✅ Notes

- In practice, dozens or hundreds of trees are used.
- Trees are usually **shallow** (e.g., max_depth=3).
- Learning rate α is typically between 0.01 and 0.3.
- More trees + small α = better generalization.

---

## 🎯 Gradient Boosting for Classification (Binary)

### 🧠 Dataset Example

| Sample | Feature X | Target Y |
|--------|-----------|----------|
| 1      | 1         | 0        |
| 2      | 2         | 0        |
| 3      | 3         | 1        |
| 4      | 4         | 1        |
| 5      | 5         | 1        |

---

### 🪜 Step-by-Step

**Step 1: Initial Prediction**  
Initial log-odds:  
p = proportion of class 1 = 3/5 = 0.6  
F₀(x) = log(p / (1 - p)) = log(0.6 / 0.4) = log(1.5) ≈ 0.405

To get probabilities:  
p = 1 / (1 + e^(−F₀(x))) ≈ 0.6

**Step 2: Compute Pseudo-Residuals (Gradients)**  
Residual = Actual − Probability

| Sample | Actual | p (predicted prob) | Gradient |
|--------|--------|--------------------|----------|
| 1      | 0      | 0.6                | -0.6     |
| 2      | 0      | 0.6                | -0.6     |
| 3      | 1      | 0.6                | +0.4     |
| 4      | 1      | 0.6                | +0.4     |
| 5      | 1      | 0.6                | +0.4     |

**Step 3: Train First Tree on Gradients**  
If X ≤ 2 → predict -0.6  
If X > 2 → predict +0.4

**Step 4: Update Log-Odds**  
Let learning_rate = 0.1  
F₁(x) = F₀(x) + 0.1 × tree output

| Sample | F₀(x) | Tree Output | F₁(x) |
|--------|-------|-------------|-------|
| 1      | 0.405 | -0.6        | 0.405 - 0.06 = 0.345 |
| 2      | 0.405 | -0.6        | 0.345 |
| 3      | 0.405 | +0.4        | 0.405 + 0.04 = 0.445 |
| 4      | 0.405 | +0.4        | 0.445 |
| 5      | 0.405 | +0.4        | 0.445 |

**Step 5: Convert Log-Odds to Probability**  
p = 1 / (1 + e^(−F(x)))

---

## 🧮 Final Classification Prediction

H(x) = F₀(x) + LR × h₁(x) + LR × h₂(x) + ...  
Probability = 1 / (1 + e^(−H(x)))  
Prediction = 1 if p > 0.5 else 0

---

## 🔍 Weak Learner Selection

At each stage:
- For regression: tree fits residuals (errors)
- For classification: tree fits gradients (pseudo-residuals)
- Splits are chosen using greedy methods to minimize squared error

---

## 🔁 What About Multiclass?

- For K classes, fit one tree per class per iteration
- Output is a vector of scores per class
- Final prediction = class with highest score

---

## ⚙️ Key Parameters

| Parameter       | Meaning                                                  |
|-----------------|----------------------------------------------------------|
| n_estimators    | Number of trees to build                                 |
| learning_rate   | Controls impact of each tree                             |
| max_depth       | Depth of each tree (weak learner)                        |
| loss            | MSE for regression, log-loss for classification          |
| subsample       | Fraction of training samples used per tree               |

---

## 🧠 Summary

| Task           | Base Learner     | Residual Target               | Loss Function     |
|----------------|------------------|-------------------------------|-------------------|
| Regression     | Regression Tree  | Residual (Actual - Predicted) | MSE               |
| Classification | Regression Tree  | Negative log-loss gradient    | Log-loss          |
| Multiclass     | One tree per class | Vector gradients              | Multinomial loss  |
