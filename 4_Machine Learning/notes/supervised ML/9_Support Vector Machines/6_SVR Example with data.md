# Support Vector Regression (SVR) — Explained with Data Example

## 1. Introduction to SVR

Support Vector Regression (SVR) is based on the Support Vector Classifier (SVC), but instead of classifying points, we aim to **predict continuous values**.

Our objective is to find a **best fit line** that fits most data points within a certain **margin of tolerance** called `epsilon (ε)`.

---

## 2. Real Data Example

Let's use the following simple dataset:

| Point | X (input) | y (target) |
|-------|-----------|------------|
| 1     | 1         | 2          |
| 2     | 2         | 2.8        |
| 3     | 3         | 4.5        |
| 4     | 4         | 4.2        |
| 5     | 5         | 5.1        |

Let’s assume:

- Initial weights: `w = 1`
- Initial bias: `b = 1`
- Margin of tolerance: `epsilon = 0.5`
- Penalty parameter: `C = 1`

---

## 3. Best Fit Line and Marginal Planes

The prediction line:  
`f(X) = w * X + b = 1 * X + 1 = X + 1`

The two marginal planes:  
- Top margin: `f(X) + epsilon = X + 1 + 0.5 = X + 1.5`
- Bottom margin: `f(X) - epsilon = X + 1 - 0.5 = X + 0.5`

## 4. Check Which Points Are Inside the Margin

We check whether each point satisfies:  
`|y_i - f(X_i)| <= epsilon`

Below is the table:

| Point | X | y   | f(X) = X + 1 | \|y - f(X)\| | Inside Margin? | eta_i |
|-------|---|-----|---------------|--------------|----------------|--------|
| 1     | 1 | 2.0 | 2             | 0.0          | ✅ Yes         | 0      |
| 2     | 2 | 2.8 | 3             | 0.2          | ✅ Yes         | 0      |
| 3     | 3 | 4.5 | 4             | 0.5          | ✅ Yes         | 0      |
| 4     | 4 | 4.2 | 5             | 0.8          | ❌ No          | 0.3    |
| 5     | 5 | 5.1 | 6             | 0.9          | ❌ No          | 0.4    |

`eta_i` is calculated as:  
`eta_i = |y_i - f(X_i)| - epsilon`  
Only for points outside the margin.


## 5. Cost Function for SVR

The SVR cost function combines:

- Minimizing the model complexity: `(1/2) * w^2`
- Penalizing deviations using `C * sum(eta_i)`

Total cost:  
`Cost = (1/2) * w^2 + C * Σ eta_i`  
Plug in our values:

- `w = 1`, so `(1/2) * w^2 = 0.5`
- `eta_4 = 0.3`, `eta_5 = 0.4` → `sum = 0.7`
- `C = 1`

**Final cost = 0.5 + 1 * 0.7 = 1.2**

---

## 6. Constraints Summary

- For points inside margin:  
  `|y_i - f(X_i)| <= epsilon`

- For points outside margin:  
  `|y_i - f(X_i)| <= epsilon + eta_i`

---

## 7. Hyperparameter Roles

- **epsilon (ε):** Margin of tolerance from the prediction line.
- **eta_i:** Error/deviation beyond epsilon for each point.
- **C:** Penalty parameter that controls how much to penalize deviations (eta_i).

---

## 8. Summary Table

| Hyperparameter | Meaning                              | Effect                                          |
|----------------|---------------------------------------|-------------------------------------------------|
| epsilon (ε)    | Width of margin                      | Larger ε = wider margin, fewer eta_i penalties |
| eta_i          | Deviation from margin                | Increases cost if outside margin               |
| C              | Penalty for deviation                | Larger C = higher penalty for error            |

---

## 9. Final Notes

- SVR does **not** try to fit all points exactly.
- Instead, it finds a line such that **most points lie within a margin**, and **only penalizes the outliers**.
- You can **tune `C` and `epsilon`** based on how much error you're willing to allow in exchange for generalization.

This makes SVR a powerful model for regression tasks with **noisy data** or when **some tolerance of error** is acceptable.
