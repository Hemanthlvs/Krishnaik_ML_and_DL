# Unsupervised Machine Learning: Clustering and Customer Segmentation

## Unsupervised Machine Learning

*   **What it is**: In Unsupervised Machine Learning, the problem statement is different. The main problem you solve here is **Clustering**.
*   **Core Idea of Clustering**: It basically means **grouping your data into similar clusters**.
*   **Key Difference from Supervised ML**:
    *   In unsupervised learning, **you don't have a specific output or dependent feature** in your dataset.
    *   You're not trying to predict anything specific, like salary based on age and experience.
*   **How it Works**:
    *   Let's say you have data with features like age, years of experience, and salary.
    *   When you apply an unsupervised machine learning algorithm, it will **group or cluster this data together**.
    *   The goal is to **create clusters that have similar types of values within them**.
    *   For example, Cluster 1 might contain people with similar age, similar experience, and similar salary.
    *   Different records (data points) will fall into different clusters based on their similarities.
    *   **End Goal**: We are clustering data points into specific groups.

## Why Unsupervised Learning?

*   **The Problem**: Why do we even do this clustering?
*   **Real-World Example**: **Customer Segmentation** is a perfect use case.
    *   Imagine you own a product and have data about people who bought it, like their salary and spending score.
    *   When you launch a new product, you want to understand **who will likely buy it immediately**.
    *   You can apply an unsupervised machine learning algorithm to this data.
    *   It will **group customers into different segments** (clusters) based on features like salary and spending score.
    *   **Example Scenario**:
        *   **Group 1 (Cluster 1)**: Customers who buy products as soon as a new feature comes out (like Apple product enthusiasts). You might give them a **15% discount** to reward their loyalty.
        *   **Group 2 (Cluster 2)**: Customers who don't buy regularly but sometimes do. To entice them for a new launch, you might offer a **higher discount, like 20%**, to encourage them to buy immediately.
*   **Benefit**: By segmenting people based on their features (clustering), you can apply **targeted strategies** like different discount rates to different customer groups.

## Unsupervised Machine Learning Algorithms You'll Learn

These are the algorithms typically covered in unsupervised learning for clustering:

1.  **K-Means Clustering** (also called K-Means algorithm). This is usually the first algorithm you'll dive into.
2.  **Hierarchical Clustering** (or Hierarchical Algorithm).
3.  **DBscan** (DBscan Clustering).

## Model Validation in Unsupervised Learning

*   **Silhouette Scoring**: This is a crucial mechanism used to **validate the models** you've created with unsupervised learning algorithms.
*   **Purpose**: It helps you understand the quality of the clusters formed by your model.