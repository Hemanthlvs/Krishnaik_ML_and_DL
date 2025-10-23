# DBscan Clustering

## 1. Introduction to DBscan Clustering
*   DBscan Clustering is a **clustering algorithm**, similar to K-means and Hierarchical Mean Clustering.
*   We'll understand how it forms clusters.

## 2. How DBscan Clustering Works
*   It works by identifying different types of points in your dataset.
*   There are **three main types of points** we need to understand in DBscan:
    1.  **Core Point** (often shown as red in diagrams).
    2.  **Border Point** (often shown as yellow in diagrams).
    3.  **Outlier Point** (often shown as blue in diagrams), also called **Noise**.
*   These points are just like your data points scattered in a 2D plane.

## 3. Key Hyperparameters
To define these points, DBscan uses two important hyperparameters:
1.  **Minimum Points (minPts)**: This is the minimum number of points we need to consider within a certain radius.
    *   *Example:* In our discussion, `minimum points` is set to **4**.
2.  **Epsilon (ε)**: This is the **radius** that we use to draw a circle around any specific data point.
*   These two are the main **hyperparameters** for DBscan clustering.
*   Selecting these values usually involves **hyperparameter tuning**, and a technique called **silhouette scoring** can help in this selection.

## 4. Understanding the Three Point Types

Let's understand when a point is classified as a Core, Border, or Outlier point:

### a) Core Point
*   Take any data point.
*   Draw a circle around it using the **epsilon (ε) radius**.
*   **Condition for a Core Point**: If the **number of other data points** existing *within* this circle (including the point itself sometimes, though the context implies 'other' points for density) is **greater than or equal to** the `minimum points` value, then it's a **Core Point**.
    *   *Formula:* `Number of points within ε >= minimum points`.
    *   *Example:* If `minimum points = 4`, and there are 4 or more points inside the circle, it's a Core Point.
*   Core points are crucial for forming clusters based on density.

### b) Border Point
*   Take any data point.
*   Draw a circle around it using the **epsilon (ε) radius**.
*   **Condition for a Border Point**: If the **number of other data points** existing *within* this circle is **less than** the `minimum points` value, then it's a **Border Point**.
    *   *Formula:* `Number of points within ε < minimum points`.
    *   *Example:* If `minimum points = 4`, and there are only 3 points (or fewer) inside the circle, it's a Border Point.
*   Border points are typically on the edge of a cluster, connected to a Core Point, but not dense enough to be a Core Point themselves.

### c) Outlier Point (Noise)
*   Take any data point.
*   Draw a circle around it using the **epsilon (ε) radius**.
*   **Condition for an Outlier Point**: If **no other point** exists *within* this circle (or perhaps very few, but the source explicitly says "no other point will be existing") then it's an **Outlier**.
*   Outliers are also referred to as **Noise**.

## 5. Advantages of DBscan Clustering
*   **Handles Noise Effectively**: A major advantage of DBscan is its ability to handle **noise (outliers)** in your data in an amazing way. It doesn't force outliers into clusters, unlike some other algorithms.
*   **Handles Non-Linear Clustering**: DBscan clustering can also effectively handle **non-linear clusters**. This means it can find clusters with complex shapes, not just spherical ones.

# DBscan Clustering examples

Here are some key takeaways about DBscan clustering based on the provided examples:

*   **DBscan can find non-linear separable clusters.** This is a really important feature of DBscan.
*   When DBscan is applied to a specific dataset, it can identify **various kinds of groups**.
*   The examples discussed show how DBscan works on data, particularly highlighting its capability with non-linear structures.
*   **Other clustering techniques like K-Means, Gaussian Mixture, or EM clustering might not be able to adequately cluster datasets** where DBscan excels. This means DBscan is a great option for complex, non-linear data that these other methods struggle with.

