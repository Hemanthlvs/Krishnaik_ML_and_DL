# SVM Kernels: 

## SVM and Linear SVC Basics

*   **Main Goal of SVM**: To find the **best-fit line** along with **marginal planes** to efficiently separate data points.
*   Used primarily for **binary classification problems**.
*   We use **SVC (Support Vector Classifier)** for this.
*   When a straight line and marginal plane are created, this variant is known as **Linear SVC**.
*   Linear SVC makes a straight line and a marginal plane to separate classes.

## Limitations of Linear SVC

*   **Problem Scenario**: What if your data points are **overlapped** and not clearly separable by a straight line?
    *   *Example*: Imagine data points for two categories all mixed up in a 2D plot.
*   In such cases, **Linear SVC will not work effectively**.
*   **Why?**: Because the points are not clearly separable linearly.
*   **Result**: If you use Linear SVC here, your **accuracy will be very low**, and the **error will be high**. It might only separate about 50% of the points correctly.

## Introducing SVM Kernels: The Solution!

*   **The Solution**: When data points are **not linearly separable**, we use **SVM Kernels**.
*   **What SVM Kernels Do**: They **apply a transformation** on your dataset.
    *   This transformation involves applying a **mathematical formula** to the data.
*   **The Magic of Transformation**: This transformation **converts your data into a higher dimension**.
    *   *Example*: If you have 2D data points that are mixed up (like red and white points), the kernel can transform them into 3D points where they become **clearly separable** along a new axis (e.g., a 'Z' axis).
*   **Benefit**: Once the data is transformed into a higher dimension and becomes clearly separable, you can then use **Linear SVC** to create a **plane (a 3D hyperplane)** and marginal planes to effectively separate the points.
*   **Outcome**: This process dramatically **increases the accuracy** of your model.

## A Simple Transformation Example (1D to 2D)

*   Let's take a 1D dataset (points on a single line, say the X-axis).
*   Here, Linear SVC cannot separate points efficiently because it can only make one cut, leading to many misclassifications.
*   **Applying Transformation**: We can create a new axis, say `y`, by applying a formula like **`y = x^2`**.
*   **Result**: The 1D points on the X-axis now get plotted in a 2D space (X and Y axes), often forming a curve.
*   **The Advantage**: In this new 2D space, the points that were mixed up in 1D become **clearly separable**.
*   Now, you can easily draw a **best-fit line** and **marginal planes** using Linear SVC in this 2D space to get high accuracy.
*   This is the core idea behind how SVM kernels use transformations.

## Types of SVM Kernels

*   There are different types of SVM kernels you should know about:
    *   **Polynomial Kernel**
    *   **RBF (Radial Basis Function) Kernel**
    *   **Sigmoid Kernel**
*   **Key Thing to Understand**: For each kernel, you need to know **what transformation formula it applies** to create a new dimension.
    *   For instance, an RBF kernel might be used to convert 2D points into 3D.
*   SVM kernels are **very powerful** and are **frequently asked in interviews**, so understanding them is crucial.