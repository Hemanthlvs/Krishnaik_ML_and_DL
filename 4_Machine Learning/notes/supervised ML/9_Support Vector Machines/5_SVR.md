# Support Vector Regression (SVR)

## 1. Introduction to SVR

*   We're diving into the **Support Vector Regression (SVR)** machine learning algorithm.
*   It builds on what we've already seen with Support Vector Classifier (SVC), including its **cost function**, **constraints**, and the **hinge loss** function.
*   Remember, the hinge loss has two important parameters: `C_i` (C of I) and `eta_i` (E to fight/eta of I).
*   Our main goal in SVR is to **reduce the cost function** by changing the values of `w` (weights) and `b` (bias).

## 2. The Regression Problem Statement

*   In a regression problem, our first step is to find a **best fit line**.
*   Along with that, we need to identify **marginal planes**.
*   The key is to make sure the **distance between these marginal planes is maximum**.
*   **Example:** Imagine predicting **house prices** (y-axis) based on **house size** (x-axis). This is a regression problem because the output, house price, is a **continuous value**.

## The Cost Function in SVR

*   When constructing the best fit line and marginal planes for SVR, our **cost function** looks like this:
    *   The main aim is to **minimize `magnitude of w / 2`** by changing `w` and `b`.

## Understanding the Lines: Best Fit & Marginal Planes

*   Let's denote the **best fit line** as `w transpose x + b`.
*   Now, for the **marginal planes**:
    *   The **top marginal plane** is represented as `w transpose x + b + epsilon`.
    *   The **bottom marginal plane** is `w transpose x + b - epsilon`.
*   What is **`epsilon` (Epsilon)**? It's our **marginal error** or margin error. This basically means the **distance** from the best fit line to the marginal plane. Both these distances (top and bottom) will be almost the same.

## The First Constraint for SVR

*   When we create these lines for a regression problem, we need to make sure that **most of our data points are covered within our marginal plane**.
*   The constraint we write is: The **distance between `y_i` (true point) and `w transpose x_i + b` (predicted point) should be less than or equal to `epsilon`**.
    *   So, `|y_i - (w transpose x_i + b)| <= epsilon`.
*   If this condition is met, it means our model is **performing really well** and the points are **falling within the marginal plane**.

## Dealing with Outliers: Introducing `eta_i` (ETA)

*   But what happens to the points that are **falling away/outside** the marginal plane?
*   For these, we define some **deviation**, which can be used as a **hyperparameter** to construct our best fit line and marginal plane.
*   We're going to add a parameter, `eta_i` (ETA of I), to our cost function. This `eta_i` is also a **hyperparameter** and relates to **hinge loss**.
*   **What is `eta_i`?** It represents the **deviation from our top marginal plane and from our bottom marginal plane**.
*   Essentially, if a point is outside the `epsilon` margin, `eta_i` is the **distance of that point from the marginal plane**.
*   We do a **summation of all `eta_i` values** to consider all these deviations.

## The Modified Constraint

*   Since we are now also considering `eta_i` for points outside the margin, our constraint changes.
*   The **new constraint** becomes: `|y_i - (w transpose x_i + b)| <= epsilon + eta_i`.
*   The reason for this change is that we are not just looking at `epsilon` (the distance within the margin), but `eta_i` helps us account for the distances of points that are **above the marginal plane** or outside it. This helps in **fine-tuning our SVR model**.

## Understanding the `C` Hyperparameter

*   **`C`** (C of I) is **another hyperparameter**.
*   It's related to the **loss function**, which is the difference between the true point and the predicted point.
*   **Relationship between `C` and Loss Function:**
    *   As the **`C` value keeps on increasing, the loss function will keep on decreasing**. This shows an inverse relationship.

## Summary of SVR Hyperparameters

*   **`epsilon` (Epsilon):** This is your **margin error from the best fit line**.
*   **`eta_i` (ETA of I):** This is the **error above the margin** or the deviation for points outside the margin.
*   **`C_i` (C of I):** This is another hyperparameter that influences the trade-off between allowing errors and having a wider margin.

These three (`epsilon`, `eta_i`, and `C_i`) are the **key hyperparameters** in Support Vector Regression used to create our best fit line and marginal planes.
