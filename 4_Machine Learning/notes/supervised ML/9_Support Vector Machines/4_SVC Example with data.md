# 🧠 Support Vector Machine (SVM) – With Real Data & Calculations

## Dataset

| Data Point | x1 | x2 | Label (y) |
|------------|----|----|-----------|
| 1          | 2  | 3  | +1        |
| 2          | 3  | 3  | +1        |
| 3          | 2  | 1  | -1        |
| 4          | 3  | 1  | -1        |



## SVM Decision Function

The decision function is:  
f(x) = wᵀx + b = w₁ * x₁ + w₂ * x₂ + b

For this example, choose:  
w = [1, 1] and b = -4


## 1️⃣ Hard Margin SVM

**Objective:**  
Minimize (1/2) * ||w||² = (1/2) * (w₁² + w₂²)  
Subject to constraints for each data point i:  
yᵢ * (wᵀ xᵢ + b) ≥ 1


## Constraint Check Table

| Point | x       | y  | wᵀx + b            | y * (wᵀx + b)    | Constraint Satisfied? |
|-------|---------|----|--------------------|------------------|-----------------------|
| 1     | [2, 3]  | +1 | (1*2 + 1*3) - 4 = 1| 1 * 1 = 1        | Yes                   |
| 2     | [3, 3]  | +1 | (1*3 + 1*3) - 4 = 2| 1 * 2 = 2        | Yes                   |
| 3     | [2, 1]  | -1 | (1*2 + 1*1) - 4 = -1| -1 * -1 = 1      | Yes                   |
| 4     | [3, 1]  | -1 | (1*3 + 1*1) - 4 = 0| -1 * 0 = 0       | No                    |


**Observation:**  
Point 4 violates the constraint (0 < 1).  
Thus, **Hard Margin SVM cannot perfectly separate the data** in this case.


## 2️⃣ Soft Margin SVM with Hinge Loss

Allow slack variables ξᵢ ≥ 0 to tolerate misclassifications:  
yᵢ * (wᵀ xᵢ + b) ≥ 1 - ξᵢ


**Cost function to minimize:**  
(1/2) * ||w||² + C * Σ ξᵢ

Equivalent to minimizing hinge loss:  
(1/2) * ||w||² + C * Σ max(0, 1 - yᵢ * (wᵀ xᵢ + b))


## Hinge Loss Calculation Table

| Point | x       | y  | wᵀx + b          | y * (wᵀx + b)    | Hinge Loss = max(0, 1 - y * (wᵀx + b)) |
|-------|---------|----|------------------|------------------|-----------------------------------------|
| 1     | [2, 3]  | +1 | 5 - 4 = 1        | 1                | 0                                       |
| 2     | [3, 3]  | +1 | 6 - 4 = 2        | 2                | 0                                       |
| 3     | [2, 1]  | -1 | 3 - 4 = -1       | 1                | 0                                       |
| 4     | [3, 1]  | -1 | 4 - 4 = 0        | 0                | 1                                       |


## Final Cost Calculation

Regularization term:  
(1/2) * ||w||² = (1/2) * (1² + 1²) = 1

Total hinge loss:  
0 + 0 + 0 + 1 = 1

Assuming C = 1, total cost:  
1 + 1 * 1 = 2


## Summary Table

| Point | Correct Classification? | Margin Output   | Hinge Loss | Slack ξᵢ |
|-------|------------------------|-----------------|------------|----------|
| 1     | Yes                    | On Margin       | 0          | 0        |
| 2     | Yes                    | Inside Margin   | 0          | 0        |
| 3     | Yes                    | On Margin       | 0          | 0        |
| 4     | No                     | Violates Margin | 1          | 1        |


## Final Soft Margin SVM Objective

minimize_w,b (1/2) * ||w||² + C * Σ max(0, 1 - yᵢ * (wᵀ xᵢ + b))

Where:  
- w = weights vector  
- b = bias  
- C = regularization parameter controlling trade-off  
- yᵢ = label of i-th sample  
- xᵢ = feature vector of i-th sample  


## Notes

- Hard Margin SVM requires perfectly separable data.  
- Soft Margin SVM allows some misclassification controlled by slack variables ξᵢ and penalty C.  
- Parameter C balances margin maximization and classification error tolerance.

