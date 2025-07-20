### Point-Plane Distance in Linear Algebra

*   **Defining a Plane Passing Through the Origin**:
    *   If a plane passes through the origin, its equation can be written as **`w transpose x = 0`**.
    *   Here, **`w` is a vector that is perpendicular to the plane** (or `x` axis).

*   **The Point and the Plane**:
    *   We consider a point, let's call it `s` (or `x`), with coordinates `X1, X2, X3...Xn`. This point is in an n-dimensional plane.
    *   The goal is to find the distance between this point and the plane.

*   **Importance and Applications**:
    *   Understanding this concept is **super important** because it's used in machine learning algorithms like **logistic regression** and **Support Vector Machines (SVM)**.
    *   In logistic regression, it's used for **classification problems**, where the aim is to find a "best fit line" (or hyperplane in higher dimensions) to separate different classes of points.

*   **The Distance Formula**:
    *   The distance `d` from a point `s` to a plane is calculated using the formula:
        **`d = (w transpose s) / ||w||`**.
    *   `s` represents the coordinates of the point (e.g., `x1, x2...xn`).
    *   `||w||` represents the magnitude of the vector `w`.
    *   This formula involves `w transpose s`, which is equivalent to `magnitude of w * magnitude of s * cos(theta)`, where `theta` is the angle between `w` and `s`.

*   **Interpreting the Sign of the Distance**:
    *   The sign of the calculated distance is very important and indicates the position of the point relative to the plane.
    *   **Positive Distance**:
        *   If a point is **above the plane** (in the same direction as the `w` vector), the distance will always be **positive**.
        *   This happens because the angle (`theta`) between the `w` vector and the point's vector (`x` or `s`) is **less than 90 degrees** (between 0 and 90 degrees). `cos(theta)` will be a value between 0 and 1, making the result positive.
    *   **Negative Distance**:
        *   If a point is **below the plane** (on the opposite side of the `w` vector), the distance will always be **negative**.
        *   This occurs because the angle (`theta`) between the `w` vector and the point's vector (`s'`) is **greater than 90 degrees** (e.g., between 90 and 180 degrees). In this range, `cos(theta)` is a negative number.
    *   **Meaning of Negative Distance**: It's crucial to understand that "negative distance" doesn't mean a literal negative length. Instead, it **indicates that the point is on the opposite side of the plane** compared to the direction `w` points.

*   **Application in Support Vector Machines (SVM)**:
    *   These concepts, especially the sign of the distance, are directly used in Support Vector Machines to classify points based on which side of the "hyperplane" they fall on.