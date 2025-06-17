# Loss Functions for Regression Problems

## Types of Loss Functions in Regression:
The main loss functions discussed for regression problems are:
1.  **Mean Squared Error (MSE)**
2.  **Mean Absolute Error (MAE)**
3.  **Huber Loss**
4.  **Root Mean Squared Error (RMSE)**

---

## 1. Mean Squared Error (MSE)

### Definition and Formula:
*   **Loss Function (for a single data point):** `(y - y_hat)²`
    *   `y_hat` represents the output after forward propagation.
*   **Cost Function (for 'n' data points):** `(1/n) * Σ(i=1 to n) (y_i - y_hat_i)²`

### Characteristics:
*   The loss function is in the form of a **quadratic equation**.
*   When plotted with weights, it forms a **parabola curve**.
*   This parabola curve represents **gradient descent**.
*   It has one **global minima**, which is the aim for weight updates to reduce the loss function.

### Advantages:
1.  **Differentiable:** MSE is fully differentiable, allowing for easy calculation of derivatives (slopes) at any point. This is crucial for weight updates using formulas like `w_new = w_old - learning_rate * (dLoss/dw_old)`.
2.  **Single Global Minima:** It consistently yields one global minimum, ensuring that the optimization process can effectively find the optimal weights without getting stuck in multiple local minima.
3.  **Converges Faster:** Due to its smooth gradient descent curve and the nature of the weight update formula, MSE typically converges to the global minimum quite rapidly.

### Disadvantages:
1.  **Not Robust to Outliers:** MSE heavily penalizes larger errors because it squares the difference between the actual and predicted values.
    *   If an outlier is present, its large error is squared, significantly increasing the overall cost function.
    *   This causes the "best fit line" to move considerably to accommodate the outlier, leading to a major change in updated weights. Thus, it's not robust when outliers are present.

---

## 2. Mean Absolute Error (MAE)

### Definition and Formula:
*   **Loss Function (for a single data point):** `|y - y_hat|` (using a mod/absolute sign)
*   **Cost Function (for 'n' data points):** `(1/n) * Σ(i=1 to n) |y_i - y_hat_i|`
    *   The mod sign ensures that even negative values become positive.

### Characteristics:
*   Unlike MSE, it **does not produce a parabolic curve**; it results in a V-shaped curve.

### Advantages:
1.  **Robust to Outliers:** MAE does not square the errors, meaning it does not penalize large errors from outliers as heavily as MSE.
    *   Even with an outlier, the cost function will increase only slightly, and the best-fit line will move only a little, unlike the major movement seen with MSE.
    *   Therefore, MAE is preferred when the dataset contains outliers.

### Disadvantages:
1.  **Slower Convergence:** Since it doesn't produce a smooth parabolic curve, directly applying standard gradient descent concepts is challenging.
    *   It requires using a "sub-gradient" concept, where slopes are calculated part by part.
    *   This process generally makes convergence slower compared to MSE.

### General Advice:
*   Use MAE if your dataset has **outliers**.
*   Use MSE if your dataset **does not have outliers**.
*   Alternatively, you can remove outliers and then use MSE, but this might lead to data loss.

---

## 3. Huber Loss

### Definition and Formula:
*   Huber Loss is a **combination of MSE and MAE**.
*   It uses a **threshold (hyperparameter)** to determine which method to apply.
*   **Cost Function Formula:**
    *   If `|y - y_hat| < threshold` (error is less than threshold, indicating no outlier):
        *   Use MSE portion (likely `(y - y_hat)²`)
    *   Otherwise (if `|y - y_hat| >= threshold`, indicating an outlier):
        *   Use MAE portion.
### Purpose:
*   It combines the benefits of both: using MSE for smaller errors (non-outliers) and MAE for larger errors (outliers), providing a robust solution that is less sensitive to outliers than pure MSE but offers better differentiability than pure MAE.

---

## 4. Root Mean Squared Error (RMSE)

### Definition and Formula:
*   RMSE is essentially the **square root of the Mean Squared Error**.
*   **Cost Function Formula:** `sqrt( (1/n) * Σ(i=1 to n) (y_i - y_hat_i)² )`