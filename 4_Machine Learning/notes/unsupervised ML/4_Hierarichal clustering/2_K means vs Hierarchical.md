# K-means Versus Hierarchical Clustering

## 1. Data Set Size (Scalability)

*   **Huge Data Set:**
    *   **K-means clustering is the clear winner**. You should definitely use K-means clustering for large datasets.
*   **Small Data Set:**
    *   **Hierarchical clustering is the clear winner**.
    *   **Why?** Because in hierarchical clustering, we create a dendrogram. If you have a huge number of data points, it becomes **very difficult to clearly see the dendrogram** and make decisions about how many clusters you need.

## 2. Data Type Applicability (Flexibility)

*   **K-means Clustering:**
    *   **Only applicable for numerical data set**.
    *   It uses distance metrics like **Euclidean and Manhattan distance**, which work best with numerical data.
*   **Hierarchical Clustering:**
    *   **Not only applicable for numerical data but also for other types of data**.
    *   **Major Advantage:** It can use **cosine similarity**.
    *   This means it can be applied wherever cosine similarity can be used.
    *   **Example:** You can find the cosine similarity between two movies, like an action movie and a comedy movie. This shows its applicability to a variety of data, not just numerical.

## 3. Visualization and Finding Number of Clusters

*   **K-means Clustering:**
    *   We use **k centroids**.
    *   The technique used to find the number of centroids (or 'k') is called the **elbow method**.
    *   Sometimes, it **becomes difficult to find the number of centroids** with the elbow method, as you need to identify where there's a sudden decrease in the x-value before it stabilizes.
*   **Hierarchical Clustering:**
    *   It becomes a **little bit easier to find the number of clusters** because you visually cut the dendrogram.
    *   **But again, for a huge dataset, K-means clustering is the winner** because you simply cannot go and create a dendrogram for such a large dataset.

## Summary of Key Takeaways for Interviews

*   **K-means clustering is for huge, numerical datasets**.
*   **Hierarchical clustering is for small, varied datasets (numerical and non-numerical) due to its use of cosine similarity**.
*   Understanding the limitations of dendrogram visualization for large datasets is crucial.
*   Know the difference in distance metrics: Euclidean/Manhattan for K-means, and the flexibility of cosine similarity for Hierarchical.