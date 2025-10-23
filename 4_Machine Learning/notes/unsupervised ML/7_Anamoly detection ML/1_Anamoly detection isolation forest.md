# Anomaly Detection with Isolation Forest

## 1. Introduction to Anomaly Detection

*   **Anomaly Detection** basically means to **detect outliers**.
*   It's a very important use case when outliers are crucial for a specific problem statement.
*   It falls under **unsupervised machine learning**.

### Real-World Examples of Anomaly Detection:

*   **Bank Account Security**: If someone tries to log in to your bank account from a different location (e.g., outside India) while you're in India, the bank sends you a security alert because it detects an outlier event.
*   **Malicious IP Detection**: Identifying fake or hacking IPs from a list of IPs.
*   **Medical Diagnosis**: Detecting if a person has cancer. Not everyone will have cancer, so those who do can be considered outliers, and this is very crucial for the problem statement.
*   **Sports Data (IPL)**: In a cricket match, if a team scores 100 runs in one over (when the maximum possible is 36), it's an outlier and can be detected as completely unique. This kind of uniqueness needs to be found in data.
*   **Healthcare Data**: Identifying patients who might have a specific disease based on two features. Most people will be normal, but those with the disease can be seen as outliers.

## 2. Understanding Outliers

*   Outliers are data points that are completely different from the majority of other data points.
*   They can play a **very important role** for certain problem statements (like cancer detection or security breaches).
*   They can also be less important for other problems.
*   In a dataset with features like height and weight, data points far away from the main cluster are considered outliers.

## 3. Isolation Forest

*   **Isolation Forest** is an **anomaly detection technique**.
*   Internally, it uses **decision trees**, even though it's an unsupervised machine learning algorithm.
*   The key idea is to **isolate** (separate) anomalous data points quickly.

### How Isolation Forest Works:

1.  **Creating Isolated Trees**:
    *   Isolation Forest creates **multiple decision trees**, which are specifically called **isolated trees**.
    *   For every data point, a leaf node will be created.
    *   The splitting happens by randomly selecting a feature and then randomly selecting a split value between the max and min values of that feature.
    *   This **recursive partitioning** continues until a terminating (leaf) node is reached.
2.  **The Principle of Isolation**:
    *   Outliers are data points that are **easily isolated** (separated) from the rest of the data points.
    *   For example, a data point far away from a cluster can be isolated with just one or a few splits in a decision tree.
    *   Normal data points, which are part of dense clusters, require **more splits** to be isolated because they are grouped together.
3.  **Measuring Isolation**:
    *   The speed or **path length** (number of splits/depth) required to isolate a data point is crucial.
    *   The quicker a data point can be isolated, the more likely it is an outlier.
    *   Unlike traditional decision trees that use Gini impurity or entropy, isolated trees focus purely on isolating each data point separately.
    *   **Multiple isolated trees** are created (forming a "forest") because different features can be chosen for splitting, leading to different paths for isolation. The algorithm is not dependent on just one tree.

## 4. Anomaly Score Calculation

To quantify how anomalous a point is, an **anomaly score** is computed for each data point.

### The Formula:

**`s(x, m) = 2^(-E(h(x))/C(m))`**

Let's break down the components:

*   **`s(x, m)`**: This is the **anomaly score** for a data point `x` with a sample size `m`.
*   **`m`**: Represents the **sample size** or the number of data points being considered.
*   **`x`**: Refers to the specific **data point** for which the anomaly score is being computed.
*   **`E(h(x))`**: This is the **average search depth** for data point `x` across **all the isolated trees**.
    *   It measures how quickly (in terms of depth/path length) `x` is isolated in each tree.
    *   Example: If `x` is isolated in 1 path in one tree, 2 paths in another, 4 in a third, `E(h(x))` would be the average of these depths.
*   **`C(m)`**: This represents the **average depth of `h(x)` for *every* data point** in **all the isolation trees**.
    *   It's a normalization factor, indicating the average depth for a normal data point given the sample size.

### Interpreting the Anomaly Score:

*   **If `E(h(x))` is very, very less than `C(m)`**:
    *   This means the data point `x` is isolated much faster than the average data point.
    *   The ratio `E(h(x))/C(m)` will be a very small value.
    *   Then, `s(x, m)` will be **approximately equal to 1**.
    *   A score close to 1 indicates a **strong outlier**.
*   **If `E(h(x))` is greater than `C(m)`**:
    *   This means the data point `x` takes longer to isolate, similar to normal data points.
    *   Then, `s(x, m)` will be **approximately equal to 0.5 or less**.
    *   A score near 0.5 or less indicates a **normal data point**.
*   **Threshold**: A **specific threshold** (e.g., 0.5) is defined. If the anomaly score `s(x, m)` crosses this threshold (e.g., `s(x,m) > 0.5`), the data point is considered an outlier. This threshold can be adjusted.
