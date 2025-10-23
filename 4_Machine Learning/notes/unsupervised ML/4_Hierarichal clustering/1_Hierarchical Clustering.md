# Hierarchical Clustering and Dendrograms

## 1. Introduction to Hierarchical Clustering

*   Hierarchical Clustering is another **clustering algorithm** we use to group data.
*   **Goal**: To get multiple groups or clusters of data from a given dataset.
*   **Key Difference from K-means**: Unlike K-means clustering, **Hierarchical Clustering does not use centroids** for each cluster.

## 2. Types of Hierarchical Clustering

There are two main types of hierarchical clustering:

1.  **Agglomerative Clustering**: This approach means **combining**.
2.  **Divisive Clustering**: This approach means **dividing**.

## 3. Agglomerative Clustering:

Let's understand the basic mathematical intuition with six data points (P1, P2, P3, P4, P5, P6).

**Steps involved**:

1.  **Initial State**: For **each data point, we initially consider it as a separate cluster**.
    *   Example: P1 is a cluster, P2 is a cluster, P3 is a cluster, and so on, for all six points.
2.  **Combine Nearest Points**: We **find the nearest points and create a new cluster** by combining them.
    *   Example:
        *   If P4 and P5 are the nearest, combine them into one cluster (P4P5).
        *   Then, if P1 and P2 are the next nearest, combine them into (P1P2).
        *   Next, if P4 is very near to the (P5P6) cluster (assuming P6 was initially close to P5, P4 then joins this group), combine them.
        *   Similarly, P3 might be very near to the (P1P2) cluster, so combine them.
3.  **Repeat Process**: Keep **repeating the process** of finding nearest points/clusters and combining them **until you get a single, large cluster** that includes all data points.
    *   Finally, the two larger clusters (e.g., one containing P1, P2, P3 and another containing P4, P5, P6) will be combined into a single cluster.

*   This approach, where we start from smallest points and cover all points to create a single cluster, is called the **agglomerative approach**.

## 4. Introducing Dendrograms

*   After forming a single large cluster, we still need to figure out **how many clusters (k) we actually need**.
*   For this, we use a new technique called a **Dendrogram**.

### 4.1. Constructing a Dendrogram

Let's use our same six points (P1-P6):

1.  **Individual Points**: On the dendrogram, each point (P1 to P6) is initially represented as a separate entity at the bottom.
2.  **Y-axis**: The **Y-axis of the dendrogram represents the Euclidean distance** (or Manhattan distance) between points or clusters.
3.  **Combining Points**:
    *   **Step 1**: Find the nearest points, say P4 and P5. We combine them on the dendrogram, and the **height of this 'building' corresponds to their Euclidean distance**.
    *   **Step 2**: Find the next nearest points, say P1 and P2. Combine them. Their Euclidean distance (height) will likely be greater than P4-P5.
    *   **Step 3**: Now, consider points and existing clusters. If P6 is nearest to the (P4P5) cluster, combine P6 with (P4P5).
    *   **Step 4**: If P3 is nearest to the (P1P2) cluster, combine P3 with (P1P2).
    *   **Step 5**: Finally, the two resulting large clusters (one with P1,P2,P3 and another with P4,P5,P6) are combined at an even greater Euclidean distance, forming a single cluster containing all points.

## 5. Deciding the Number of Clusters (k) using Dendrograms

### 5.1. Using Euclidean Distance Threshold

*   The `k` value (number of clusters) is selected based on a **Euclidean distance threshold**.
*   We **define a threshold** (a value on the Y-axis) and **draw a horizontal line** across the dendrogram at that threshold.
*   The **number of vertical lines this horizontal threshold line passes through indicates the number of clusters (k)**.

**Examples**:

*   If the threshold is `4` (Euclidean distance), and the line passes through **two vertical lines**, then `k = 2`. This means we get two groups.
*   If we **reduce the threshold** to `2.5`, and the line passes through **four vertical lines**, then `k = 4`.
*   If we further **decrease the threshold** to `0.5`, and it passes through **six vertical lines**, then `k = 6`. This means each point is a separate cluster again.

*   **Observation**: When you **decrease the threshold (Euclidean distance), the number of clusters will generally increase**. Our job is to select the "best" threshold.

### 5.2. The "Hack" to Select the Best `k` Value

This is the **most crucial technique** for dendrograms:

1.  **Identify the Longest Vertical Line**: Look for the **longest vertical line** in the dendrogram **such that no other horizontal line (from a previous merge) passes through it**.
    *   *Clarification*: We are looking for a vertical line that isn't intersected by any horizontal branches *below* it that connect other points/clusters at a lower distance.
    *   In the example provided, the speaker identifies a specific vertical line that fits this description.
2.  **Draw a Horizontal Line**: Once you've found this longest vertical line, **create a horizontal line through it**.
3.  **Count Intersections**: **Count how many vertical lines this new horizontal line passes through**.
    *   If it passes through two vertical lines, then **`k = 2`** is the suitable number of clusters.

*   This technique helps us **set up the optimal threshold value**, which corresponds to the Euclidean distance on the Y-axis.

## 6. Agglomerative vs. Divisive Recap

*   **Agglomerative approach**: We go from **bottom to top** (starting with individual points and combining them upwards).
*   **Divisive approach**: We go from **top to bottom** (starting with all points as one big cluster and then dividing them downwards). Both will eventually lead to similar cluster structures.