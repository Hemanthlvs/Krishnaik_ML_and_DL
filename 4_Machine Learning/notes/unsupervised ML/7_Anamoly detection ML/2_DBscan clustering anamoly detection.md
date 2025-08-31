# Anomaly Detection Using DBscan Clustering

## 1. Introduction to DBscan for Anomaly Detection

*   We're diving into **anomaly detection** using **DBscan clustering**.
*   The main power of DBscan is its ability to create clusters (or groups) even in **non-linear separable data**. This is a big advantage!
*   Because of this capability, DBscan can effectively **determine outliers**.
*   If finding these outliers is crucial for a problem, then DBscan becomes a fantastic **anomaly detection application**.
*   In anomaly detection, the **noise or outliers** found by DBscan play a very important role.
*   Basically, finding noise and outliers means **distinguishing particular data points from all the normal points** in a dataset.

## 2. Three Major Points in DBscan Clustering

When you're dealing with DBscan, remember these three main types of points it identifies:
1.  **Core Point**
2.  **Border Point**
3.  **Noise or Outlier**

For anomaly detection, our **main focus will be on the "noise or outlier" points**. We won't be focusing much on core or border points for this specific application.

## 3. Hyperparameters of DBscan

DBscan uses two main hyperparameters that you need to understand:
1.  **Minimum Points**: This sets a threshold for the number of data points.
2.  **Epsilon (ε)**: This is basically the **radius** around a data point. You can play with this epsilon value for different results.

## 4. Defining Core, Border, and Noise/Outlier Points

Let's understand how DBscan categorizes points based on `minimum points` and `epsilon`:

*   **Core Point**: A data point is a core point if the **number of data points within its `epsilon` radius is greater than or equal to the `minimum points`**.
    *   *Example*: If `minimum points` is 4, and a point has 6 points (including itself) within its `epsilon` radius, it's a core point. These are often shown as red points.

*   **Border Point**: A data point is a border point if the **number of data points within its `epsilon` radius is less than the `minimum points`**.
    *   *Example*: If `minimum points` is 4, and a point has only 3 points within its `epsilon` radius, it could be a border point.

*   **Noise or Outlier**: A data point is considered noise or an outlier if **there are no other data points within its `epsilon` radius** (or if it's not a core point and not reachable from a core point).
    *   These are the points that are **completely different from normal points**.
    *   In the context of anomaly detection, **these noise/outlier points are our anomalies**.

## 5. DBscan's Strength in Non-Linear Data and Outlier Detection

*   DBscan performs really well with **non-linear clustering data**.
*   Unlike methods like K-means, DBscan can effectively create proper clusters and **identify outliers** in complex, non-linear datasets.
*   You can see this in examples where DBscan successfully forms clusters and highlights outliers in a non-linear dataset, whereas K-means might struggle to form natural groups in such scenarios.