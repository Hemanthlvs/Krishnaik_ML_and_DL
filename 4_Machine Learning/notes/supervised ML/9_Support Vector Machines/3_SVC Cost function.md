# SVM Cost Function and Hinge Loss

## Initial SVM Cost Function (Hard Margin)

*   **Main Goal**: To **maximize `2 / magnitude of w`** by changing `w` (weights) and `b` (bias).
*   **Purpose**: This maximization helps in **increasing the distance between the marginal planes**.
*   **Constraints for Classification**:
    *   If `w transpose x + b` is **greater than or equal to `1`**, the point is labeled as `+1`.
    *   If `w transpose x + b` is **less than or equal to `1`**, the point is labeled as `-1`. (Note: The source also mentions "for all the correct points, whenever we multiply w of I with w transpose x, we are going to get always greater than equal to one" and "minus into minus we are going to get this".)

## Rewriting the Cost Function for Minimization

*   In Machine Learning, we generally aim to **minimize cost functions**.
*   Maximizing `2 / magnitude of w` is **exactly the same as minimizing `magnitude of w / 2`**.
*   So, the cost function for SVC can be written as: **`minimize w,b (magnitude of w / 2)`**.

## Limitations of the Initial Cost Function (Hard Margin)

*   This simplified cost function (hard margin) is suitable **only if all data points are clearly separable**.
*   In real-world scenarios, it's common to have **overlapping data points**. A "best fit line" and clear marginal planes cannot always be perfectly created without issues.

## Introducing Hinge Loss for Real-World Scenarios (Soft Margin SVM)

*   To handle overlapping points, we need to **add some "amazing hyperparameters"** to the basic cost function.
*   This enhanced cost function is for **Soft Margin SVM**, not hard margin SVM.
*   The added component to the cost function is called **Hinge Loss**. It's similar to "Log Loss" in logistic regression.
*   The refined cost function looks like: **`minimize w,b (magnitude of w / 2) + C_i * summation(eta_i)`**.

### Components of Hinge Loss:

#### `C_i` (Hyperparameter)

*   **What it is**: `C_i` is a hyperparameter.
*   **Purpose**: It indicates **how many misclassified points we are willing to "tolerate" or ignore**.
*   **Example**: If `C_i` is set to `5`, it means we can ignore `5` misclassified points and still proceed to find the best-fit line and marginal planes. If `C_i` is `6`, it's acceptable to have `6` errors.

#### `eta_i` (Summation of `eta_i`)

*   **What it is**: This term represents the **summation of the distance of the incorrect data points from their respective marginal planes**.
*   **Purpose**: It calculates the distance for each misclassified point from the margin it crossed. The sum of these distances (`summation of eta_i`) defines the total "allowed distance" for misclassifications.

## Final Soft Margin SVM Cost Function

*   The complete cost function for Soft Margin SVM aims to **minimize** the combination of `(magnitude of w / 2)` and the Hinge Loss components (`C_i * summation(eta_i)`).
*   By setting the parameters for `C_i` and `eta_i`, this cost function helps in creating the **best-fit line along with marginal planes** even when data points overlap significantly.