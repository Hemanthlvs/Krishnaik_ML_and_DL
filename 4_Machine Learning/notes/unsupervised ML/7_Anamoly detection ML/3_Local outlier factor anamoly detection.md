# Local Outlier Factor (LOF) for Anomaly Detection

## 1. Important Terms: Local Outlier vs. Global Outlier

Before diving into LOF, we need to know the difference between two important terms:

*   **Local Outlier:** This is a data point that is **near to a specific cluster** but still an outlier within its immediate vicinity. Imagine a point that's part of a group but a bit too far from its closest friends within that group.
*   **Global Outlier:** This is a data point that is **completely different from all other data points** in the dataset. It's totally isolated from all clusters.

## 2. Anomaly Detection Methods (A Quick Recap)

We've learned about other anomaly detection techniques too:

*   **DBscan clustering:** Can be used to find anomalies.
*   **Isolation Forest:** Also helps determine anomalies.

These methods (DBscan, Isolation Forest) are usually very good at finding **Global Outliers** because they easily isolate such points.

But, for finding **Local Outliers** properly, **Local Outlier Factor (LOF)** is the best.

## 3. What is Local Outlier Factor (LOF)?

*   LOF is also known as `l o f`.
*   It helps determine an `l o f score` for each data point.
*   The entire concept is very simple and internally uses the **k-nearest neighbor (kNN) concept**.
*   The main idea is to determine **local density**, which is a super important term here.

## 4. How LOF Works

Let's understand the working of LOF step-by-step:

1.  **Choose 'k' value:** Like in kNN, we first decide a value for `k`, which represents the number of neighbors we consider (e.g., `k = 5`).
2.  **Pick a data point:** We take one data point and want to check if it's an outlier or not.
3.  **Find Nearest Neighbors:** For that chosen data point, LOF finds its **`k` nearest neighboring points**.
4.  **Calculate Distance/Average Distance:** It calculates the distance (or average distance) between our point and its `k` nearest neighbors.
5.  **Understand Density from Distance:**
    *   If the **average distance is less**, it means the data points are close together, so the **density is more**.
    *   If the **average distance is more**, it means the data points are spread out, so the **density is less**.
6.  **Compare Local Density:** The main part! LOF compares the **local density of our chosen data point** with the **local densities of its neighboring points**.
7.  **Identify Local Outlier:**
    *   If the local density of our data point is **substantially lower** compared to the local densities of its neighbors, then that point is considered a **local outlier**.
    *   Basically, we are checking if our point is more isolated (less dense) than its immediate surroundings.

**In simple words:** LOF checks if a point is "lonelier" (less dense) than its immediate friends. If it is, then it's a local outlier.