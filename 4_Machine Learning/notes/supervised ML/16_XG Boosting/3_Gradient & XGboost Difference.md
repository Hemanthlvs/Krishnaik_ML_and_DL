# 🌳 Gradient Boosting vs. XGBoost – Full Example with Same Data

## 🎯 Goal: Predict house price category (Low, Medium, High) based on size

We'll use a tiny dataset to demonstrate how both Gradient Boosting and XGBoost work internally, step-by-step.

---

## 📊 Dataset

| ID | Size (sqft) | Price Category |
|----|--------------|----------------|
| 1  | 500          | Low            |
| 2  | 800          | Medium         |
| 3  | 1000         | Medium         |
| 4  | 1200         | High           |
| 5  | 1500         | High           |

Label Encoding:  
Low = 0  
Medium = 1  
High = 2

**Target (y):** [0, 1, 1, 2, 2]  
**Feature (X):** [500, 800, 1000, 1200, 1500]

---

## 🌿 Gradient Boosting (Multiclass)

### Step 1: Initialize Model with Mean Prediction  
Initial Prediction (f₀) = mean(y) = (0 + 1 + 1 + 2 + 2) / 5 = 1.2

### Step 2: Compute Residuals (y - f₀)  
Residuals = [0 - 1.2, 1 - 1.2, 1 - 1.2, 2 - 1.2, 2 - 1.2] = [-1.2, -0.2, -0.2, 0.8, 0.8]

| Size | Residual |
|------|----------|
| 500  | -1.2     |
| 800  | -0.2     |
| 1000 | -0.2     |
| 1200 | 0.8      |
| 1500 | 0.8      |

### Step 3: Train First Tree (h₁) on Residuals  
Suppose we split at Size ≤ 1000:  
Left Node (<= 1000): mean = (-1.2 - 0.2 - 0.2)/3 = -0.53  
Right Node (> 1000): mean = (0.8 + 0.8)/2 = 0.8

h₁(x) =  
- if Size ≤ 1000 → output -0.53  
- else → output 0.8

### Step 4: Update Model  
Let learning rate α = 0.1  
f₁(x) = f₀ + α * h₁(x)

| ID | Size | f₁(x) Calculation              | f₁(x) |
|----|------|--------------------------------|-------|
| 1  | 500  | 1.2 + 0.1 * (-0.53) = 1.147    | 1.147 |
| 2  | 800  | 1.2 + 0.1 * (-0.53) = 1.147    | 1.147 |
| 3  | 1000 | 1.2 + 0.1 * (-0.53) = 1.147    | 1.147 |
| 4  | 1200 | 1.2 + 0.1 * (0.8) = 1.280      | 1.280 |
| 5  | 1500 | 1.2 + 0.1 * (0.8) = 1.280      | 1.280 |

Next, we compute new residuals: y - f₁(x) and train h₂ on them, and repeat.

---

## ⚡ XGBoost (Multiclass)

### Step 1: Initial Log-Odds (Base Prediction)  
Class counts: [1 (Low), 2 (Medium), 2 (High)]  
Total = 5  
f₀ = log(Count / Total)  
= [log(1/5), log(2/5), log(2/5)] ≈ [-1.61, -0.92, -0.92]

These are raw scores (logits) used for all samples initially.

### Step 2: Compute Gradients & Hessians for Each Sample  
Use softmax to get probabilities. For sample 1:  
f₀ = [-1.61, -0.92, -0.92]  
Softmax:  
P(Low) = exp(-1.61)/Z ≈ 0.2  
P(Med) = exp(-0.92)/Z ≈ 0.4  
P(High)= exp(-0.92)/Z ≈ 0.4

Actual = [1, 0, 0] (since actual is Low = class 0)

Gradient (g) = Predicted - Actual = [0.2 - 1, 0.4 - 0, 0.4 - 0] = [-0.8, 0.4, 0.4]  
Hessian (h) = p * (1 - p) = [0.2*0.8, 0.4*0.6, 0.4*0.6] = [0.16, 0.24, 0.24]

Repeat g, h for all samples.

### Step 3: Build Trees (One Tree per Class)

Let’s say we build a tree for class 0 (Low):  
At Size ≤ 1000:  
- g_L = sum gradients on left  
- h_L = sum hessians on left

Use Gain formula to choose best split:

Gain = ½ × [ (∑g_L)² / (∑h_L + λ) + (∑g_R)² / (∑h_R + λ) - (∑g)² / (∑h + λ) ] - γ

Choose split with max Gain.

Each leaf will get weight:  
w = -∑g / (∑h + λ)

### Step 4: Update Predictions  
f₁ = f₀ + η * w_leaf  
Repeat for next round.

Final output = softmax(f₁) for each sample → predicted class.

---

## 🔍 Key Differences Summary

| Concept                 | Gradient Boosting                         | XGBoost                                           |
|-------------------------|--------------------------------------------|---------------------------------------------------|
| Base Model              | Mean (regression) or constant (classification) | Log-Odds (log(p / (1 - p)))                      |
| Error Used              | Residuals (y - prediction)                 | Gradient and Hessian (1st and 2nd order stats)    |
| Tree Split              | Based on residuals                         | Based on Gain from g and h                        |
| Regularization          | Optional                                   | λ (L2), γ (min split loss)                        |
| Leaf Value              | Mean of residuals                          | -∑g / (∑h + λ)                                    |
| Final Prediction        | Direct sum of trees                        | Sum of trees + softmax or sigmoid applied         |
| Speed & Accuracy        | Slower, less regularized                   | Faster, more regularized, handles sparsity        |

---

## ✅ Final Thoughts

- **Gradient Boosting** is easier to understand and a good starting point for boosting models.
- **XGBoost** enhances Gradient Boosting with better handling of regularization, optimization, and performance.
- Internally, XGBoost builds upon Gradient Boosting by using **second-order derivatives**, **pruning**, and **more intelligent tree growing**.

