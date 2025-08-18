# 🌲 Gradient Boosting: Full Explanation with Examples

Gradient Boosting is an ensemble learning method that builds models sequentially. Each model corrects the errors made by the previous model. It's used for both **regression** and **classification** problems.

---

## ✅ Gradient Boosting for Regression

### 🧠 Dataset Example

| Sample | Feature X | Target Y |
|--------|-----------|----------|
| 1      | 1         | 5        |
| 2      | 2         | 7        |
| 3      | 3         | 9        |
| 4      | 4         | 11       |
| 5      | 5         | 15       |

---

### 🪜 Step-by-Step

**Step 1: Initial Prediction**  
Initial prediction is the mean of the target values.  
Initial Prediction = (5 + 7 + 9 + 11 + 15) / 5 = 9.4

**Step 2: Compute Residuals (Errors)**  
Residual = Actual − Predicted

| Sample | Y (Target) | Initial Pred | Residual |
|--------|------------|--------------|----------|
| 1      | 5          | 9.4          | -4.4     |
| 2      | 7          | 9.4          | -2.4     |
| 3      | 9          | 9.4          | -0.4     |
| 4      | 11         | 9.4          | +1.6     |
| 5      | 15         | 9.4          | +5.6     |

**Step 3: Train First Tree on Residuals**  
We train a regression tree to predict these residuals using Feature X.  
Suppose it creates rules like:  
- If X ≤ 2 → predict -3.4  
- If 2 < X ≤ 4 → predict +0.6  
- If X > 4 → predict +5.6

**Step 4: Update Predictions**  
Let learning rate = 0.1  
New prediction = Previous prediction + learning_rate × tree prediction

| Sample | Previous Pred | Tree Output | New Prediction |
|--------|----------------|-------------|----------------|
| 1      | 9.4            | -3.4        | 9.4 + 0.1×(-3.4) = 9.06 |
| 2      | 9.4            | -3.4        | 9.06 |
| 3      | 9.4            | +0.6        | 9.4 + 0.1×0.6 = 9.46 |
| 4      | 9.4            | +0.6        | 9.46 |
| 5      | 9.4            | +5.6        | 9.4 + 0.1×5.6 = 9.96 |

Repeat steps 2–4 for more trees. Each tree fits new residuals.

---

## 🔢 Final Regression Prediction  
H(x) = F₀(x) + LR × h₁(x) + LR × h₂(x) + ... + LR × hₙ(x)

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
