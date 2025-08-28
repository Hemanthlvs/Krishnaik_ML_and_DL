# Geometric Intuition of Principal Component Analysis (PCA)

## 1. What is PCA used for?
*   PCA is primarily used for **dimensionality reduction**.
*   It helps in **feature extraction**, meaning it extracts new features from the existing ones in your dataset.

## 2. Understanding the Problem: From 2D to 1D Example
*   Let's say you have two features: **'size of the house'** and **'number of rooms'**. The output feature is 'price of the house'.
*   When you plot these two features (size vs. number of rooms), you might observe that as the size of the house increases, the number of rooms also tends to increase. This is common sense.
*   **Goal:** To reduce these two dimensions (features) into just one dimension using PCA. This means having one independent feature instead of two.

## 3. A Simple Approach to Dimensionality Reduction
*   One simple way to convert 2D to 1D is **feature selection**, where you pick one feature and ignore the other.
*   Another simple way is to **project all data points onto one axis**, for example, the X-axis.
    *   When you project points onto the X-axis, you get all data points in one dimension.
    *   The **spread** between the first and last projected data point represents the data's spread. A huge spread means high variance.
*   **Disadvantage of this simple projection approach:**
    *   While information about one feature (e.g., size) might be captured, **information from the other feature (e.g., number of rooms) is lost**.
    *   This is because the spread/variance related to the lost feature is significant, and by directly projecting onto one axis, you are neglecting this information.
    *   **Loss of information** is a major drawback, which can lead to your model not performing well in predictions. You are doing feature extraction, but with significant information loss.

## 4. PCA's Smart Approach: The Geometric Intuition
*   **How PCA prevents information loss:**
    *   In PCA, you **apply a transformation** to the existing X and Y axes.
    *   This transformation involves applying mathematical equations, specifically something called **eigendecomposition on a matrix**.
    *   After this transformation, you get **new axes**, which might look different from the original ones (e.g., `size_dash` and `number_of_rooms_dash`). One new axis will typically be **perpendicular** to the other.
    *   Then, you **project all your data points onto these new axes**.
*   **Key Difference from Simple Projection:**
    *   When projecting onto the new X-axis (let's call it `size_dash`), the **spread (variance) is properly captured** for most points.
    *   Crucially, when projecting onto the new Y-axis (e.g., `number_of_rooms_dash`), the **spread that gets lost is very, very less**.
    *   This means **maximum variance is captured** on the primary new axis (PC1), and much less information is lost on the secondary new axis (PC2) compared to the simple projection method.
    *   The variance on the new secondary axis (PC2) is much lower than what was lost by projecting directly onto an original axis.

## 5. Principal Components (PC1, PC2, etc.)
*   The new axes created after transformation are called **Principal Components**.
*   If you have two original dimensions, you'll get two principal components: **PC1** and **PC2**.
*   If you have three original dimensions, you'll get three principal components: PC1, PC2, and PC3.
*   **Order of Importance:**
    *   **PC1 always captures the maximum amount of variance**.
    *   **PC2 captures the next maximum amount of variance** (after PC1).
    *   **PC3 captures the maximum variance after PC1 and PC2**, and so on.
    *   This variance order is always: `Variance(PC1) > Variance(PC2) > Variance(PC3)`.
*   **Why Variance is Important:** Variance tells you how much the data is spread out. Capturing more variance means capturing **more and more information** about the data.

## 6. How PCA Achieves Dimensionality Reduction
*   **Main aim of PCA:** To find these special lines (principal components) after transformation that capture the **maximum amount of variance**.
*   **Selecting the Best Principal Components:** A line is considered the "best" principal component line if, when data points are projected onto it, it **captures the maximum possible variance**.
*   **Reducing Dimensions:**
    *   **From 2D to 1D:** The algorithm finds the best principal component line (PC1) that captures maximum variance. You then project all your 2D points onto this PC1 line, effectively converting them into 1D points.
    *   **From 3D to 1D:** You would project all points onto PC1.
    *   **From 3D to 2D:** You would take both PC1 and PC2, project all points onto them, and combine this information to get your two dimensions.
*   The **number of principal components you choose** depends on the desired final number of dimensions you want to convert your data into.