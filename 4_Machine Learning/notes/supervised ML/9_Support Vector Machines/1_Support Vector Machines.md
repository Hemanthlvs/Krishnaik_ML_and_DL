# Support Vector Machines (SVM)

## Introduction to SVM
*   **Support Vector Machine (SVM)** is a powerful machine learning algorithm.
*   It can solve **both classification problems and regression problems**.
*   When used for classification, it's called **Support Vector Classifier (SVC)**.
*   When used for regression, it's called **Support Vector Regression (SVR)**.

## Support Vector Classifier (SVC) - Geometric Intuition
*   **Core Idea (vs. Logistic Regression):** Similar to Logistic Regression, SVM also creates a **best fit line (2D), a 3D plane (3D), or a hyperplane (n-dimensions)**.
*   **Key Difference:** Along with the best fit line/plane/hyperplane, SVM also creates **two additional lines/planes called "Marginal Planes"**.

### Details of Marginal Planes
*   **Equidistant:** The two marginal planes are equidistant from the best fit line/plane.
*   **Maximum Distance (Margin):** The **distance between these two marginal planes should be maximum**. This distance is often referred to as the "margin".
*   **Selection Criteria:** If there are multiple possible best fit lines, the one that creates the **maximum distance between its marginal planes** is selected for classification.

## Support Vectors
*   The marginal planes pass through the **nearest data points** from the best fit line/plane.
*   These **nearest data points** (the ones that lie on the marginal planes) are called **"Support Vectors"**.
*   Support vectors are crucial because they define the position and orientation of the best fit line/plane and the marginal planes.

## Aim of Support Vector Machine
*   The main aim of SVM is to **create a best fit line/plane/hyperplane along with marginal planes**.
*   This setup helps to **categorize or classify points very clearly**.
*   When a new test data point comes, its position relative to the best fit line/plane (and within the margin) helps assign it to the correct category.
*   SVM is also used in **multi-class classification**.