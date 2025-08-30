# K-Means Clustering

## Introduction
*   **K-means clustering** is a **unsupervised machine learning algorithm**.
*   It helps in **grouping similar kinds of points together**.

## Geometric Intuition
*   Imagine you have some **data points spread across x and y axes**.
*   Visually, you might see **distinct groups** within these points.
*   **Goal**: After applying K-means, these data points will be divided into **clear groups or "clusters"**.
    *   For example, if there are two groups, you'll get **Cluster 1** and **Cluster 2**.
    *   Along with clusters, you also get **centroids**. If there are two clusters, you'll get two centroids.
    *   Similarly, if there are three groups, K-means will help identify **three clusters** and their respective **three centroids**.
*   **Main aim**: To **cluster similar kind of points together**.

## Steps of K-Means Clustering Algorithm

The process involves an iterative approach with three main steps:

### Step 1: Initialize Centroids (k value)
*   We start by **initializing some centroids**, which are referred to as the **k value** (that's why it's called K-means).
*   These centroids are **randomly initialized** in the data space.
*   For instance, if we know there are two groups, we would initialize **k = 2 centroids**.
*   (How to select the 'k' value will be discussed later).

### Step 2: Find Nearest Points to Centroids and Mark/Group Them
*   After initializing centroids, for **every data point**, we **calculate its distance** to **all the centroids**.
*   Each data point is then **assigned to the centroid it is nearest to**.
*   For example, if a point is nearer to 'Centroid A', it's marked as part of 'Group A'.
*   To find distance, we typically use **Euclidean distance or Manhattan distance**.
*   Geometrically, this step creates decision boundaries (like a perpendicular line between two centroids) where points on one side belong to one centroid's group and points on the other side belong to the other centroid's group.

### Step 3: Move Centroids by Finding the Average (Mean) of the Grouped Points
*   Once all points are assigned to their nearest centroids (i.e., grouped), we **move the centroids**.
*   The new position of each centroid is calculated by finding the **average (mean) of all the data points that were assigned to it in the previous step**.
*   This means the centroid literally shifts its position to the "center" of its current cluster of points.

### Iteration and Stopping Condition
*   The **steps (Step 2 and Step 3) are repeated again and again**.
*   After moving centroids (Step 3), we again **find which points are nearest to these *new* centroid locations** (repeating Step 2).
*   This might cause some points to **change their group assignments** if they become closer to a different centroid.
*   Then, centroids are **moved again based on the new group averages** (repeating Step 3).
*   This iterative process continues until the algorithm **converges**.
*   **Stopping Condition**: The algorithm stops when there is **no significant movement of the centroids** or **no change in the group assignments of data points** compared to the previous iteration. When everything is correctly grouped, the process stops.
*   The final output will be **clearly defined clusters** (e.g., Cluster 1, Cluster 2) and their final centroid locations.

# Selecting K and Measuring Distance

## 1. Selecting the 'k' Value

### The Problem with Visual Selection
*   Initially, for simple problems, we might select `k` just by looking at the data and seeing distinct groups.
*   However, in real-world scenarios, there's often a lot of overlap between data points, making visual selection difficult.

### Introducing Within Cluster Sum of Squares (WCSS)
*   To address this, we use a new notation called **WCSS**, which stands for **Within Cluster Sum of Squares**.
*   WCSS basically measures the sum of squared distances of each point to its nearest centroid.

### The Elbow Method
*   The Elbow Method is a technique used to find the optimal `k` value.
*   **Process:**
    1.  **Initialize `k` values**: Start by initializing `k` from 1 to some higher value, let's say 20. We iterate through each `k` value.
    2.  **For `k = 1`**:
        *   We consider just one centroid for all data points.
        *   We compute the **distance from every data point to this single centroid**.
        *   The formula involves squaring these distances and summing them up, hence "sum of squares".
        *   When `k=1`, the WCSS value will be **quite high** because all points are far from a single centroid.
    3.  **For `k = 2`**:
        *   Two centroids are initialized in the dataset.
        *   Points are assigned to their nearest centroid, and the distance from each point to its nearest centroid is calculated.
        *   When compared to `k=1`, the **WCSS value for `k=2` will reduce**. This is because data points are divided between two centroids, making the distances smaller.
    4.  **Continuing the process**: As `k` increases (e.g., `k=3, k=4`, and so on), the WCSS value will **keep on decreasing**.
    5.  **Graphing `k` vs. WCSS**: We plot a graph with `k` values on the x-axis and WCSS values on the y-axis.
        *   The graph will start with a high WCSS for `k=1`.
        *   As `k` increases, the WCSS will decrease rapidly initially.
        *   After some point, the WCSS value will become **almost stable**.
    6.  **Identifying the "Elbow Point"**:
        *   The "elbow" in the graph is the point where there's an **abrupt decrease in WCSS**, and then after that point, it starts to stabilize.
        *   Imagine your physical elbow; the bend where the WCSS curve sharply changes direction is the elbow point.
        *   **We select the `k` value corresponding to this elbow point**. This `k` value is considered optimal because adding more centroids beyond this point doesn't significantly reduce the WCSS.

## 2. Measuring Distance

In K-means, calculating distance is crucial. There are mainly two types of distance metrics discussed here: Euclidean Distance and Manhattan Distance.

### Euclidean Distance
*   **Concept**: It's the **shortest straight-line distance** between two points.
*   **Formula (for 2D points P1(X1, Y1) and P2(X2, Y2))**:
    ```
    Euclidean Distance = √[ (X2 - X1)² + (Y2 - Y1)² ]
    ```
*   **For 3D points**: The formula extends by adding `(Z2 - Z1)²` inside the square root.
*   **When to Use**:
    *   When you can go directly from one point to another in a straight line.
    *   **Example**: In traffic control, if you can fly a drone from point A to point B directly, you'd use Euclidean distance to calculate that path.

### Manhattan Distance (also known as Taxicab Geometry or City Block Distance)
*   **Concept**: It's the **sum of the absolute differences of their Cartesian coordinates**. You can only move along the axes (horizontally and vertically), like navigating city blocks.
*   **Formula (for 2D points P1(X1, Y1) and P2(X2, Y2))**:
    ```
    Manhattan Distance = |X2 - X1| + |Y2 - Y1|
    ```
*   **When to Use**:
    *   When movement is restricted to a grid-like path, like in a city with blocks and roads.
    *   **Example**: If you want to take an Uber from one point to another in a city like many US states where cities are planned in blocks, you cannot go directly. You have to follow the roads (horizontal and vertical movements), so Manhattan distance is used.

### Key Difference Summary
*   **Euclidean Distance**: "As the crow flies" - straight line path.
*   **Manhattan Distance**: "As a taxi drives" - path along grid lines.

