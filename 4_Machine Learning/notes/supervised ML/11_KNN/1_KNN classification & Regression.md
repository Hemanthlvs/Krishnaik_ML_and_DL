# K-Nearest Neighbors (KNN)

## What is KNN?

*   KNN can be used to solve both **classification** and **regression** problem statements.

## KNN for Classification Problems

### Data Setup for Classification

*   Imagine we have a dataset with features like F1, F2, and an output feature `y`.
*   The `y` feature can be:
    *   **Binary categories** (e.g., 0s or 1s).
    *   **Multi-class categories** (more than two categories).
*   We plot these points based on their features and categories. For example, some points belong to 'category 0' and others to 'category 1'.
*   This plotted data is our **training data set**.

### Steps Involved in KNN Classification

1.  **Step 1: Initialize the `k` value**.
    *   The 'k' in KNN stands for the number of neighbors.
    *   `k` can be any number **greater than zero**.
    *   **`k` is a hyperparameter**. This means its optimal value can change for different datasets.
    *   **How to find the best `k`?** We need to **try different `k` values** and see which one gives the **highest accuracy** for our model. This process is called hyperparameter tuning.
    *   *Example*: If k=5 gives the highest accuracy, we select `k=5` for our model.

2.  **Step 2: Find the `k` nearest neighbors for the test data**.
    *   Suppose we have a new test data point whose category we want to predict.
    *   Using our chosen `k` value (e.g., k=5), we need to **find the five data points from our training data that are closest** to this new test data point.
    *   To do this, we calculate the **distance** between the new test data point and **all** the points in our training data.
    *   Then, we pick the `k` points that have the smallest distances – these are our `k` nearest neighbors.

3.  **Step 3: Count neighbors by category and make a prediction**.
    *   Once we have our `k` nearest neighbors (e.g., 5 neighbors), we count how many of them belong to each category.
    *   *Example*: If out of 5 neighbors, 2 belong to 'category 0' and 3 belong to 'category 1'.
    *   The new test data point will be **predicted to belong to the category that has the majority (maximum number) of neighbors**.
    *   In our example, since 'category 1' has 3 neighbors (which is more than 2 for 'category 0'), the new point will be classified as 'category 1'.
    *   This is the core idea of KNN for classification.

## Distance Metrics (How to find "Nearest"?)

To find the `k` nearest neighbors, we need to calculate distances between points. There are two common distance formulas used.

### a. Euclidean Distance

*   This is a very common distance formula, probably something you've seen in school maths or linear algebra.
*   It calculates the **straight-line distance (hypotenuse)** between two points.
*   **Formula (for 2D points (x1, y1) and (x2, y2))**: `Distance = √((x2 - x1)² + (y2 - y1)²) `.
*   For 3D (x1,y1,z1 and x2,y2,z2), you just add `(z2 - z1)²` inside the root. It extends to any number of dimensions.
*   **Where it's used**: Applications like calculating air travel distance (e.g., flight paths from Bangalore to New Delhi, or India to the US), traffic control, etc..

### b. Manhattan Distance

*   Instead of a straight line, it calculates the distance by **summing the absolute differences of the coordinates along the axes** (like moving on a grid, not cutting corners).
*   **Where it's used**: Perfect for scenarios where movement is restricted to a grid, like navigating in a city with blocks and roads (e.g., how an Uber would travel in a US city from one building block to another). You can't fly diagonally unless you have a helicopter.

### Which Distance Metric to Use?

*   It **depends on your specific problem statement**.
*   Most of the time, **Euclidean distance is commonly used**.
*   You can also try both during hyperparameter tuning and **select the one that gives better accuracy** for your model.

## KNN for Regression Problems

### How it Works for Regression

*   For regression, your output feature `y` is a **continuous value** (e.g., predicting house price based on house size).
*   When you have a new test data point (e.g., a new house size) and you want to predict its continuous output (house price):
    *   You follow the same steps: find the `k` nearest neighbors to that new point.
    *   Instead of counting categories, for regression, you simply **calculate the average (mean) of the output values (e.g., house prices) of those `k` nearest neighbors**. This average will be your predicted output value.
    *   If your data has a lot of **outliers**, you can also use the **median** of the `k` neighbors' output values instead of the average.
*   All other steps, like finding the optimal `k` value, remain the same as in classification.