# Support Vector Machines (SVMs)

## Main Aim of SVMs

*   The main goal of SVMs is to create the **best fit line** along with **marginal planes**.
*   We operate in a 2D plane with `x` and `y` coordinates.
*   The equation for the **best fit line** (also known as a hyperplane in higher dimensions) is `w transpose x + b = 0`.
    *   This comes from the general straight line equation `W1X1 + W2X2 + c = 0` or `ax + by + c = 0`.
    *   If the line passes through the origin, `b` (or `c`) would be `0`, making the equation `w transpose x = 0`. But here, it's not passing through the origin.

## Understanding Vector 'w' and Distance Calculation

*   The vector `w` is always **perpendicular** to the best fit line, forming a 90-degree angle with it.
*   **Distance of a point to the hyperplane**:
    *   If the angle between vector `w` and a point `s` (or its vector from origin) is **greater than 90 degrees**, the distance from that point to the hyperplane will be **negative**.
    *   This means, any point that is **below** the best fit line, its distance to the line will always be **negative**.
    *   If the angle between vector `w` and a point `s'` (or its vector from origin) is **between 0 and 90 degrees**, the distance from that point to the hyperplane will always be **positive**.
    *   This means, any point that is **above** the best fit line, its distance to the line will always be **positive**.

## Introduction to Marginal Planes and Support Vectors

*   Beyond the best fit line (`w transpose x + b = 0`), we create **two more planes**, called **marginal planes**.
*   These marginal planes are parallel to the best fit line.
*   One marginal plane (`w transpose x + b = +1`) is for the points above the best fit line (positive side).
    *   The `+1` signifies that for points on this side, the value `w transpose x + b` will be positive (e.g., +1, +2, +n). In many research papers, `+k` is also used.
*   The other marginal plane (`w transpose x + b = -1`) is for the points below the best fit line (negative side).
*   The points that lie **on these marginal planes** are called **Support Vectors**. They are the nearest points to the best fit line from each class.

## Maximizing the Margin (Distance between Marginal Planes)

*   The **main aim** in SVM is to **maximize the distance between these two marginal planes**.
*   To calculate the distance between the two planes (`w transpose x1 + b = +1` and `w transpose x2 + b = -1`):
    *   Subtracting the equations gives `w transpose (x1 - x2) = 2`.
*   To normalize this distance, we use the concept of a **unit vector**.
    *   A unit vector is a vector whose **magnitude is one**.
    *   To get a unit vector for `w`, we divide `w` by its magnitude `||w||`.
    *   Using unit vectors helps normalize all points between 0 and 1.
*   The **distance between the marginal planes (the margin)** is given by the formula: **`2 / ||w||`**.
*   This `2 / ||w||` is our **cost function**.
*   Our objective is to **maximize this cost function** (`2 / ||w||`).
    *   Why maximize? Because a larger margin means better separation between classes and better generalization.
*   This maximization is achieved by **changing the values of `w` and `b`**.

## Constraints for Correct Classification

*   Along with maximizing the margin, we have **constraints** to ensure correct classification of points.
*   For all true output values `y_i` (which can be `+1` for one class and `-1` for another):
    *   If a point belongs to the **positive class** (`y_i = +1`), then `w transpose x + b` must be **greater than or equal to `+1`**.
    *   If a point belongs to the **negative class** (`y_i = -1`), then `w transpose x + b` must be **less than or equal to `-1`**.
*   These conditions are for **correctly classified points**.
*   **Combined Constraint**: For all correctly classified points, we can express this concisely as: **`y_i * (w transpose x + b) >= 1`**.
    *   If `y_i` is `+1` and `w transpose x + b >= 1`, their product is `positive (>= 1)`.
    *   If `y_i` is `-1` and `w transpose x + b <= -1`, their product will also be `positive (>= 1)` (e.g., `-1 * -2 = 2`).
*   So, the overall problem is to **maximize `2 / ||w||` subject to the constraint `y_i * (w transpose x + b) >= 1` for all points**.
