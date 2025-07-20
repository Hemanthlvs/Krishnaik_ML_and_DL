# Equations of Lines, 3D Planes, and Hyperplanes

This topic is **super important** for understanding machine learning algorithms like logistic regression and Support Vector Machines (SVMs).

## 1. Equation of a Straight Line (2D)

In a 2D space (with x and y axes), a straight line can be represented by several equations:

*   **`y = mx + c`**
    *   You might have seen this formula before.
    *   `m` is the **slope**. It tells you how much the y-value changes for every unit movement in the x-axis.
    *   `c` is the **intercept**. It's the point where the straight line meets the y-axis when the x-value is zero (i.e., when x = 0, then y = c).

*   **`y = β0 + β1x`**
    *   This is another notation similar to `y = mx + c`, where β0 is the intercept and β1 is the slope.

*   **`ax + by + c = 0`**
    *   This equation is almost the same as `y = mx + c`.
    *   You can rearrange `ax + by + c = 0` to `y = (-a/b)x - (c/b)`. Here, `(-a/b)` acts as the slope (`m`) and `(-c/b)` acts as the intercept (`c`).

*   **General form for multiple dimensions (often used in machine learning):**
    *   If we use `X1` and `X2` instead of `x` and `y` for multiple dimensions:
        *   **`W1X1 + W2X2 + b = 0`**
        *   Here, `W1` and `W2` are **coefficients**, and `b` is the **intercept**.
    *   This can be represented more compactly using vector notation as:
        *   **`wᵀx + b = 0`**
        *   `wᵀ` (w transpose) represents the coefficients (e.g., `W1, W2`) as a row vector, and `x` represents the input features (e.g., `X1, X2`) as a column vector. This form is used regularly in algorithms.

## 2. Equation of a 3D Plane

*   When you have three dimensions (e.g., `X1`, `X2`, `X3` axes), you don't draw a straight line; instead, you draw a **3D plane**.
*   The equation for a 3D plane is:
    *   **`W1X1 + W2X2 + W3X3 + b = 0`**
    *   `W1`, `W2`, `W3` are the coefficients, and `b` is the intercept.
*   Similar to the 2D case, this can also be represented as:
    *   **`wᵀx + b = 0`**
    *   Here, `w` would be a vector of `(W1, W2, W3)` and `x` would be `(X1, X2, X3)`.

## 3. Equation of an N-dimensional Hyperplane

*   For an n-dimensional space (more than 3 dimensions), the concept extends to a **hyperplane**.
*   The equation for an n-dimensional hyperplane is:
    *   **`W1X1 + W2X2 + W3X3 + ... + WnXn + b = 0`**
    *   This is also generally represented as:
        *   **`wᵀx + b = 0`**

## 4. Special Case: Line/Plane/Hyperplane Passing Through the Origin

*   If a straight line, 3D plane, or n-dimensional hyperplane passes through the origin (where all `x` values are zero, like x1=0, x2=0, etc.):
    *   The **intercept `b` (or `c`) becomes zero**.
*   In this case, the equation simplifies to:
    *   **`wᵀx = 0`**

## 5. Geometric Interpretation: The 'w' Vector

The `wᵀx = 0` equation has a very important geometric meaning in linear algebra:

*   **Dot Product**: The dot product of two vectors, `w` and `x`, is also defined as the product of their magnitudes and the cosine of the angle (`theta`) between them:
    *   `wᵀx = |w| * |x| * cos(θ)`
*   **Perpendicularity**:
    *   Since `wᵀx = 0`, it implies that `|w| * |x| * cos(θ) = 0`.
    *   Assuming `w` and `x` are non-zero vectors, for this equation to hold, **`cos(θ)` must be zero**.
    *   `cos(θ)` is zero when `θ` (the angle between the vectors `w` and `x`) is **90 degrees**.
*   **Conclusion**: This means that the vector **`w` is always perpendicular (or normal) to the line, plane, or hyperplane**.
    *   This property holds for every point `x` on the plane, even if the plane does not pass through the origin (i.e., when `b` is not zero, `w` is still perpendicular to the plane).

This understanding of 'w' being perpendicular to the decision boundary (line, plane, hyperplane) is fundamental in machine learning, especially for algorithms that classify data, where 'w' represents the normal vector of the separating hyperplane.

***

**Analogy:** Think of a flashlight beam (the `w` vector) shining directly onto a wall (the line, plane, or hyperplane). No matter where the wall is positioned, as long as the flashlight beam hits it squarely (at 90 degrees), the light will spread out evenly, much like how the 'w' vector is always perpendicular to every point on the surface it defines.