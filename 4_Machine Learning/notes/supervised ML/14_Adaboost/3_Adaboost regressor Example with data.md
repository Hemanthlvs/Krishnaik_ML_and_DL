# AdaBoost for Regression (AdaBoost.R2): Step-by-Step Guide

## Overview

- AdaBoost.R2 is a variant of AdaBoost designed for **regression problems**.
- Instead of predicting a class, we predict a **continuous numeric value**.
- Weak learners are typically **regression tree stumps** (DecisionTrees with `max_depth=1`).
- AdaBoost.R2 combines predictions of multiple regressors by **weighted average**.

---

## Dataset Example

We use a simple dataset where the goal is to predict a person’s **spending score** based on their **age**.

| Sample | Age | Spending Score |
|--------|-----|----------------|
| 1      | 20  | 30             |
| 2      | 25  | 35             |
| 3      | 30  | 45             |
| 4      | 35  | 50             |
| 5      | 40  | 65             |
| 6      | 45  | 70             |

---

## Step 1: Initialize Sample Weights

All samples start with equal weight:

Total samples = 6  
Each sample weight wᵢ = 1 ÷ 6 ≈ 0.167

---

## Step 2: Train Weak Learners (Stumps) and Calculate Error

We'll build **DecisionTreeRegressor(max_depth=1)** as weak learners. Each weak learner will predict a value for each input.

Let's consider 3 weak learners: h₁, h₂, h₃

### Weak Learner h₁:

- Splits based on `Age <= 32.5`
- Predicts:
  - If Age ≤ 32.5 → Predict 36.6 (average of Samples 1, 2, 3)
  - If Age > 32.5 → Predict 61.6 (average of Samples 4, 5, 6)

| Sample | True Y | Predicted Y | Absolute Error |
|--------|--------|-------------|----------------|
| 1      | 30     | 36.6        | 6.6            |
| 2      | 35     | 36.6        | 1.6            |
| 3      | 45     | 36.6        | 8.4            |
| 4      | 50     | 61.6        | 11.6           |
| 5      | 65     | 61.6        | 3.4            |
| 6      | 70     | 61.6        | 8.4            |

**Normalized Error (Lᵢ):**

Normalize each error by dividing by the **max error** (11.6):

| Sample | Absolute Error | Normalized Error Lᵢ |
|--------|----------------|---------------------|
| 1      | 6.6            | 0.569               |
| 2      | 1.6            | 0.138               |
| 3      | 8.4            | 0.724               |
| 4      | 11.6           | 1.0                 |
| 5      | 3.4            | 0.293               |
| 6      | 8.4            | 0.724               |

**Weighted Error (ε):**

ε = Σ(wᵢ × Lᵢ) =  
= 0.167 × (0.569 + 0.138 + 0.724 + 1.0 + 0.293 + 0.724)  
= 0.167 × 3.448 ≈ 0.576

**Beta (β) Calculation:**

β = ε ÷ (1 − ε) = 0.576 ÷ (1 − 0.576) = 0.576 ÷ 0.424 ≈ 1.358

---

## Step 3: Update Weights

Update rule:

New wᵢ = old wᵢ × β ^ (1 − Lᵢ)

| Sample | Lᵢ   | 1 − Lᵢ | β ^ (1 − Lᵢ) | New Weight (before norm) |
|--------|------|--------|---------------|---------------------------|
| 1      | 0.569| 0.431  | 1.358^0.431 ≈ 1.147 | 0.167 × 1.147 = 0.1915    |
| 2      | 0.138| 0.862  | 1.358^0.862 ≈ 1.294 | 0.167 × 1.294 = 0.216     |
| 3      | 0.724| 0.276  | 1.358^0.276 ≈ 1.090 | 0.167 × 1.090 = 0.182     |
| 4      | 1.0  | 0.0    | 1.358^0.0 = 1       | 0.167 × 1 = 0.167         |
| 5      | 0.293| 0.707  | 1.358^0.707 ≈ 1.245 | 0.167 × 1.245 = 0.208     |
| 6      | 0.724| 0.276  | 1.358^0.276 ≈ 1.090 | 0.167 × 1.090 = 0.182     |

Normalize weights (sum ≈ 1.1465):

| Sample | Final Normalized Weight |
|--------|--------------------------|
| 1      | 0.1915 ÷ 1.1465 ≈ 0.167   |
| 2      | 0.216 ÷ 1.1465 ≈ 0.188    |
| 3      | 0.182 ÷ 1.1465 ≈ 0.159    |
| 4      | 0.167 ÷ 1.1465 ≈ 0.146    |
| 5      | 0.208 ÷ 1.1465 ≈ 0.181    |
| 6      | 0.182 ÷ 1.1465 ≈ 0.159    |

---

## Step 4: Repeat for h₂ and h₃

### Train h₂ using updated weights

(Repeat same steps: build regression stump → calculate normalized errors → compute ε → compute β → update weights)

Assume we complete 3 learners:
- h₁: β₁ = 1.358
- h₂: β₂ = 1.214
- h₃: β₃ = 1.110

---

## Step 5: Final Prediction Formula

For AdaBoost.R2, final prediction H(x) is a **weighted median** of predictions, where weight for each hᵢ = ln(1 ÷ βᵢ)

Compute αᵢ = ln(1 ÷ βᵢ) = −ln(βᵢ)

| Learner | βᵢ   | αᵢ (weight)      |
|---------|------|------------------|
| h₁      | 1.358| −ln(1.358) ≈ −0.305 |
| h₂      | 1.214| −ln(1.214) ≈ −0.194 |
| h₃      | 1.110| −ln(1.110) ≈ −0.104 |

Since all weights are negative, AdaBoost.R2 uses the **absolute values of αᵢ** to perform **weighted median**.

---

## Step 6: Predict on New Sample

Say we have a new input:
- Age = 37

Predictions by weak learners:
- h₁: 61.6
- h₂: 58.0
- h₃: 63.0

Sort predictions:
- 58.0 → weight 0.194
- 61.6 → weight 0.305
- 63.0 → weight 0.104

Total α = 0.603  
Cumulative weights:
- 58.0 → 0.194
- 61.6 → 0.499 (0.194 + 0.305)
- 63.0 → 0.603

**Weighted median is where cumulative weight crosses 0.5 → Final Prediction = 61.6**

---

## Summary

- AdaBoost.R2 works by combining regressors using **weighted median** of predictions.
- Sample weights are updated based on **how far off predictions are** (not just right or wrong).
- Poor predictions get lower weight, good predictions get more influence in the next round.

---

## Key Differences from Classification

| Aspect               | Classification (SAMME)        | Regression (AdaBoost.R2)           |
|----------------------|-------------------------------|-------------------------------------|
| Output               | Class label                   | Numeric value                       |
| Error Calculation    | Misclassification rate        | Normalized absolute error           |
| Model Combination    | Weighted majority vote        | Weighted median of predictions      |
| Weight Update        | Based on correct/incorrect    | Based on error magnitude            |
| Final Output         | sign(sum(αᵢ × hᵢ(x)))         | weighted median(hᵢ(x), αᵢ)         |

---
