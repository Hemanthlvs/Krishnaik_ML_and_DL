# KNN: K-D Tree and Ball Tree Variants

## 1. The Problem with Basic KNN

*   When you need to find the nearest neighbour in standard KNN, you usually have to **check the distance between the query point and *all* other data points**.
*   This process has a **very high time complexity**, which is **O(n)**, where 'n' is the number of data points. We want to decrease this time complexity.

## 2. Introducing KNN Variants

To reduce this high time complexity, we use two main variants:
*   **K-D Tree**
*   **Ball Tree**

## 3. K-D Tree (K-dimensional Tree)

K-D Tree is a data structure used to organize points in a k-dimensional space. In our case, it's used for 2D data (F1, F2 features).

### What is K-D Tree?
*   It's a special type of tree, specifically a **binary tree**, created from your data points.
*   **Main aim:** When finding K-nearest neighbours, we don't want to check the distance for *every* point.
*   **Benefit:** Because of the binary tree structure, searching for elements or finding distances becomes limited to specific paths within the tree. This **reduces the number of searches** significantly.

### How K-D Tree is Constructed (Binary Tree Format)

The construction involves recursively splitting the data space:

1.  **Select an Axis and Find Median:**
    *   Start by considering the first feature, say **F1 (x-coordinate)**.
    *   **Find the median of all F1 values** in your dataset. For example, if F1 values sorted are (2, 4, 5, 7, 8, 9), the median might be 6.5. If 6.5 isn't there, you pick an existing point close to it, like 5 or 7.
    *   Let's say we pick 7. Now, you **draw a line (or create a split)** at F1 = 7, projecting it onto the x-axis. This line divides your data space into **two main regions**. This point (e.g., 7,2) becomes the **root node** of your K-D tree.

2.  **Alternate Axes for Next Split:**
    *   Now, in one of these regions (e.g., the left region), you consider the **next feature, F2 (y-coordinate)**.
    *   **Find the median of F2 values** *within that specific region*. For example, if F2 values are (1, 2, 3, 4, 6, 7), the median could be 3.5. You might pick 4.
    *   **Draw another line (split)** at F2 = 4, projecting it onto the y-axis. This further divides the region. The point corresponding to this split (e.g., 5,4) becomes a **child node**.

3.  **Continue Recursively:**
    *   You **continue this process, alternating between F1 (x-axis) and F2 (y-axis) for subsequent splits** in the new sub-regions.
    *   Each split point becomes a node in the binary tree. Points falling on one side of the split go to one child node, and points on the other side go to the other child node.
    *   This continuous splitting builds the complete K-D Tree.

### How K-D Tree is Used for Queries (Finding Nearest Neighbors)

When a new query point comes (e.g., 5,7):

1.  **Locate the Region:** The K-D tree helps you quickly figure out which region (or partition) the query point belongs to by traversing down the tree.
2.  **Find Nearest in Region:** Once the region is identified, you find the nearest point within that region (e.g., 4,7 is closest to 5,7). This becomes your **first nearest point**.
3.  **Backtracking for More Neighbors:** To find the *next* nearest points (second, third, etc.), the K-D tree uses **backtracking**.
    *   You traverse back up the tree from the current nearest point, checking other branches to see if there are any closer points that might have been "missed" due to the initial split.
    *   You calculate distances for relevant points encountered during this backtracking.
*   **Key Advantage:** You are **not finding the distance with respect to *every* element** like in a brute search. You follow a specific path and use backtracking for optimization.

## 4. Ball Tree

Ball Tree is another variant, and it's generally considered **better than K-D Tree**.

### Why is Ball Tree Better?
*   The main reason is that **Ball Tree does not require backtracking** during queries, unlike K-D Tree. This makes it more efficient in some scenarios.

### How Ball Tree is Constructed (Clustering/Grouping)

The concept of a Ball Tree is very simple, based on grouping:

1.  **Group Nearest Points:**
    *   You start by **grouping the closest data points together**.
    *   For example, if you have points 1, 2, 3, 4, 5, 6, 7, 8, 9, you might group (1,2) as Group 1 (G1), (3,4) as Group 2 (G2), (5,6,7) as Group 3 (G3), and (8,9) as Group 4 (G4). These groups effectively form "balls" or clusters around the points.

2.  **Combine Nearest Groups (Hierarchical Clustering):**
    *   Next, you **combine the nearest *groups* together**.
    *   For example, G1 and G2 might be the closest groups, so they combine to form a new, larger group (G5).
    *   Similarly, G3 and G4 might combine to form G6.
    *   Finally, G5 and G6 (the largest groups) combine to form an even bigger group (G7), encompassing all points.
    *   This process creates a hierarchical structure of **clusters** or "balls".

### How Ball Tree is Used for Queries (Finding Nearest Neighbors)

When a new query point comes, the Ball Tree allows for very direct retrieval:

1.  **Identify Relevant Group:** The structure tells you directly which "circle" or group the query point belongs to.
2.  **Direct Distance Calculation:** Once the relevant group is identified, you can **directly calculate the distance between the query point and *all* the points within that specific group**.
3.  **Efficiency:** Because you're working with pre-grouped clusters, you directly get the potential nearest neighbours without having to search through many irrelevant points or perform backtracking. This is the **main power of the Ball Tree**.

## 5. K-D Tree vs. Ball Tree & Conclusion

*   Both K-D Tree and Ball Tree are designed to **create a binary tree structure** for your data.
*   The fundamental goal of both is to **reduce the time complexity** for KNN. They achieve this by avoiding brute-force distance calculations for every single point.
*   **Ball Tree is generally preferred over K-D Tree** because it simplifies the search process by avoiding the need for backtracking.

These variants are essentially ways to **optimize KNN algorithms** for better performance.