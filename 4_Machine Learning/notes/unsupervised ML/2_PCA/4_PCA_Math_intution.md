# PCA Math Intuition

## 1. Goal of PCA

*   The **final goal of the PCA algorithm** is to **find the best principal component line** after transforming from existing axes.
*   This line should be chosen in such a way that **maximum variance needs to be captured**.
*   For example, if you're reducing from two dimensions (like x and y axes with plotted points) to one dimension, PCA helps in finding that best single line. The line where the maximum variance will be captured is selected as the best principal component line.

## 2. Two Important Concepts in PCA

To decide if a line is the "best" principal component, PCA uses two main things:
    *   **Projections**
    *   **Cost function** (which is related to variance)

## 3. Understanding Projections

*   Let's take one point, say **P1 (X1,Y1)**, which can also be considered as a vector.
*   We also have a **unit vector (U)**.
*   The main aim of projection is to **project this point P1 onto the unit vector U** to get a new point called **P1 dash (P1')**.
*   **Why projection?** We need to project all points because the maximum variance will only be captured when all the points are projected onto this principal component line. This projection helps us calculate the variance of these projected points.
*   **Equation for Projection**:
    *   The projection of a vector P1 onto a unit vector U is initially given by: `(P1 vector * U vector) / magnitude of U`.
    *   Since U is a **unit vector**, its **magnitude (|U|) is always one**.
    *   Therefore, the simplified projection of P1 on U is simply the **dot product of P1 and U**: `P1 . U`.
*   **Result of Projection**:
    *   When you do the dot product of P1 (e.g., coordinates X1, Y1) and the unit vector U (e.g., coordinates X2, Y2), you get **P1 dash (P1')**.
    *   This **P1 dash is a scalar value**.
    *   This scalar value basically talks about the **distance from the origin to the projected point** on the axis (e.g., distance from origin to P1 dash, or origin to P2 dash).
*   After projecting all original points (P1, P2, P3... Pn) onto the unit vector, we get their corresponding scalar values (P1 dash, P2 dash, P3 dash... Pn dash). These projected points can be denoted as `X0', X1', X2'... Xn'`.

## 4. Understanding the Cost Function (Variance)

*   Once we have all these scalar values (the projected points like `X0', X1', X2'... Xn'`), it becomes **easy to compute the variance**.
*   **Variance Calculation Formula**:
    *   `Summation from i=1 to n of (Xi' - X_bar')^2 / n`.
    *   Here, `Xi'` represents each projected scalar value, and `X_bar'` is the mean of all projected scalar values.
*   **The Main Aim (Cost Function)**:
    *   Your goal is to **find the best unit vector**.
    *   "Best" means the unit vector that **captures the maximum variance**.
    *   This "maximum variance" is our **cost function**; we have to find the maximum of this variance.

## 5. Eigen-Decomposition: Eigenvectors and Eigenvalues

*   We **cannot keep on trying different unit vectors** one by one to find the one that gives maximum variance. This is not practical.
*   To efficiently find the best unit vector, we use a technique called **eigen-decomposition**, which involves **eigenvectors and eigenvalues**.
*   **Steps to find the best unit vector using Eigen-Decomposition**:
    1.  **Find the Covariance Matrix**: First, you need to calculate the **covariance matrix between the features** of your data.
    2.  **Compute Eigenvectors and Eigenvalues**: Eigenvectors and eigenvalues are computed or found out from this covariance matrix.
    3.  **Identify the Best Eigenvector**:
        *   The **eigenvector that has the largest eigenvalue** is the one that is selected, as it captures the **maximum variance**.
        *   An **eigenvalue is nothing but the magnitude of its corresponding eigenvector**.
        *   **Mathematically Proven**: It's mathematically proven that whenever we project data points onto the specific line represented by this eigenvector (the one with the highest eigenvalue), the maximum variance will be captured.
*   **Equation for Eigenvectors and Eigenvalues**:
    *   The eigenvectors and eigenvalues can be found out by the simple equation: `A * v = lambda * v`.
    *   This equation represents the **linear transformation of a matrix**. Here, `A` is the matrix (in PCA, it's the covariance matrix), `v` is the eigenvector, and `lambda` is the eigenvalue.
	

# Eigenvectors, Eigenvalues, and Principal Component Analysis (PCA)

## 1. Introduction to Eigenvectors, Eigenvalues & PCA

*   **Main Goal**: In machine learning, especially with **Principal Component Analysis (PCA)**, we need to find the **best principal component line** that can **capture the maximum variance** in our data.
*   **Role of Eigenvectors & Eigenvalues**: These are the tools we use to find that "best" line.
*   **Eigen Decomposition**: This whole process can be seen as **eigen decomposition of a covariance matrix**.

## 2. Understanding Linear Transformation and the Eigen Equation

*   **What is a Vector?**: A vector `v` has specific coordinates.
*   **What is Linear Transformation?**: Imagine your data points are on a grid. A linear transformation is like moving or changing the entire plane or grid in different directions.
    *   **How it Works**: When you apply a specific matrix `A` (which represents the linear transformation) to a vector `v`, you get a new vector that is just a **scaled version of the original vector** `v`.
*   **The Core Equation (Eigen Equation)**:
    `A * v = λ * v`
    *   **`A`**: This is your specific matrix (e.g., a covariance matrix).
    *   **`v`**: This is your vector (the **eigenvector**).
    *   **`λ` (Lambda)**: This is a scalar value called the **eigenvalue**. It tells you how much the eigenvector `v` is scaled.
*   **Key Insight**: When you apply a linear transformation (`A`) to an eigenvector (`v`), the direction of the eigenvector **doesn't change**, only its magnitude (length) gets scaled by the eigenvalue (`λ`).
*   **Importance for PCA**: For a given matrix, there can be multiple eigenvectors. We are interested in the eigenvector that has the **biggest or maximum magnitude**. This particular eigenvector will be used as the **principal component (PC1)** because it's mathematically proven to **capture the maximum variance** in the data.

### Example of Linear Transformation
*   Let's say you have a vector `(1,1)`.
*   If you apply a certain transformation matrix, this vector might change to `(4,2)`.
*   In this specific (and simplified) example, the `λ` (eigenvalue) would be 4 and 2.
*   Sometimes, after transformation, the new vector might go in a completely different direction. But for an eigenvector, its direction remains the same or exactly opposite to the original, only scaled.
*   The `λ` value (eigenvalue) will change depending on the vector you apply the transformation to.

## 3. Steps to Calculate Eigenvalues and Eigenvectors (for PCA)

To apply PCA and find the best principal components, we follow these steps:

1.  **Standardize the Data (Zero-Centering)**:
    *   First, take your data points (e.g., features `x` and `y`) and **standardize them**. This means adjusting them so that all data points are **zero-centered**.
    *   This ensures that the mean of each feature is zero.

2.  **Compute the Covariance Matrix**:
    *   Next, you need to find the **covariance of your features** (e.g., `x` and `y`).
    *   **Covariance Equation**: `Cov(x,y) = Σ((x_i - x_bar) * (y_i - y_bar)) / (n - 1)`.
        *   `x_i, y_i`: Individual data points.
        *   `x_bar, y_bar`: Mean of `x` and `y`.
        *   `n`: Number of data points.
    *   **Forming the Covariance Matrix**:
        *   For **two independent features** (e.g., `x` and `y`), you'll get a **2x2 matrix**.
            ```
            [ Variance(x)   Covariance(x,y) ]
            [ Covariance(y,x) Variance(y)   ]
            ```
           
        *   **Variance(x)** is actually `Covariance(x,x)`.
        *   **Important Note**: `Covariance(x,y)` is always equal to `Covariance(y,x)`.
        *   For **three independent features** (e.g., `x`, `y`, `z`), you'd get a **3x3 matrix**. The diagonal elements will be the variances of `x`, `y`, `z`, and the off-diagonal elements will be the covariances.

3.  **Find Eigenvectors and Eigenvalues from the Covariance Matrix**:
    *   Now, you take this covariance matrix (let's call it `A`) and use the eigen equation: `A * v = λ * v`.
    *   **Number of Eigenvalues**:
        *   If your covariance matrix is 2x2 (from two features), you will get **two eigenvalues**: `λ1` and `λ2`.
        *   If it's 3x3 (from three features), you'll get `λ1`, `λ2`, and `λ3`.
    *   **Meaning of Eigenvalues**: Each `λ` value (eigenvalue) represents the **magnitude of a principal component line**.
        *   `λ1` corresponds to **Principal Component 1 (PC1)**.
        *   `λ2` corresponds to **Principal Component 2 (PC2)**.
        *   And so on, `λ3` for PC3.
    *   **Selecting the Best Principal Component**:
        *   The eigenvalue that is the **highest** (e.g., `λ1`) signifies the eigenvector that captures the **maximum variance** in your data.
        *   This eigenvector associated with the largest eigenvalue is chosen as your **PC1**. This is the "best" line for your data.

## 4. Dimensionality Reduction (Using PCA)

*   **Goal**: PCA is often used to **reduce the number of dimensions** in your data while retaining as much information (variance) as possible.
*   **How it Works**:
    *   **Finding Principal Components**: After calculating all the eigenvalues and eigenvectors, you'll have `PC1`, `PC2`, `PC3`, etc., each corresponding to a specific eigenvalue. Remember, `PC1` has the largest eigenvalue and captures the most variance.
    *   **Converting 2D to 1D**: If you want to convert your 2D data to 1D, you'd typically select **PC1** (the principal component with the highest variance). Then, you **project all your data points onto this PC1 line**. This projection gives you a 1D representation of your original 2D data.
    *   **Converting 3D to 2D**: If you want to convert 3D data to 2D, you might combine the **PC1 and PC2** (the two principal components with the largest eigenvalues). Projecting your data onto the plane formed by PC1 and PC2 gives you a 2D representation.
*   **Final Output**: At the end of the day, PCA helps you find the **best principal component line** (or plane) that fits your data points and **captures the maximum possible variance**, which is crucial for tasks like visualization, noise reduction, and improving model performance.

