# Decision Tree Regressor:

## 1. Introduction to Decision Tree Regressor

*   **Decision Tree Regressor** is used to solve **regression problem statements**.
*   In regression problems, the **output feature is continuous** (e.g., salary, price).
*   This is different from Decision Tree Classifier, where the output feature has fixed categories (binary or multi-class).

## 2. Key Differences in Splitting Criteria from Decision Tree Classifier

*   In **Decision Tree Classifier**, splits are determined using techniques like **Entropy, Gini Impurity**, and **Information Gain**. These methods are based on the purity of categorical splits.
*   However, in **Decision Tree Regressor**, we **cannot use these methods** (Information Gain, Entropy, Gini Impurity) because our output is a **continuous value**, not a fixed number of categories.

## 3. How Decision Tree Regressor Makes Splits: **Variance Reduction**

*   For Decision Tree Regressor, we use **Variance Reduction** to decide which feature and threshold to use for making a split.
*   The main idea is to find the split that results in the **maximum variance reduction**.
*   Instead of entropy or Gini impurity, Decision Tree Regressor primarily uses **Mean Squared Error (MSE)** for evaluating splits.

## 4. Steps to Calculate Variance Reduction

To find the best split, we follow these steps:

### Step 1: Compute Variance of the Root Node

*   First, calculate the variance of the entire dataset (or the current node) before any split. This is your **Root Variance**.
*   **Formula for Variance:**
    `Variance = (1/N) * Σ (y - ȳ)²`
    *   Here, `N` is the number of data points.
    *   `y` is each individual output value.
    *   `ȳ` (y-hat) is the **average (mean)** of all output values in that node.
*   **Example Calculation (for Root Node with values 40K, 42K, 52K, 60K, 56K):**
    *   Average (ȳ) = (40+42+52+60+56) / 5 = **50K**.
    *   Variance_Root = (1/5) * [ (40-50)² + (42-50)² + (52-50)² + (60-50)² + (56-50)² ]
    *   Variance_Root = (1/5) * [ 100 + 64 + 4 + 100 + 36 ]
    *   Variance_Root = (1/5) * [ 304 ] = **60.8**

### Step 2: Compute Variance for Each Child Node (after a potential split)

*   For each potential split (based on different features and threshold values), create child nodes.
*   Calculate the variance for each individual child node using the same variance formula.

*   **Example 1: Potential Split at `experience <= 2`**
    *   This split creates two child nodes:
        *   **Left Child (C1):** If `experience <= 2` (output value: 40K)
            *   Variance_C1: (1/1) * (40-50)² = **100**
        *   **Right Child (C2):** If `experience > 2` (output values: 42K, 52K, 60K, 56K)
            *   Variance_C2: (1/4) * [ (42-50)² + (52-50)² + (60-50)² + (56-50)² ]
            *   Variance_C2: (1/4) * [ 64 + 4 + 100 + 36 ] = (1/4) * [ 204 ] = **51**

*   **Example 2: Potential Split at `experience <= 2.5`**
    *   This split creates two child nodes:
        *   **Left Child (C1):** If `experience <= 2.5` (output values: 40K, 42K)
            *   Variance_C1: (1/2) * [ (40-50)² + (42-50)² ] = (1/2) * [ 100 + 64 ] = (1/2) * [ 164 ] = **82**
        *   **Right Child (C2):** If `experience > 2.5` (output values: 52K, 60K, 56K)
            *   Variance_C2: (1/3) * [ (52-50)² + (60-50)² + (56-50)² ] = (1/3) * [ 4 + 100 + 36 ] = (1/3) * [ 140 ] = **46.66** (approx)

### Step 3: Apply the Variance Reduction Formula

*   Once you have the root variance and child variances, calculate the variance reduction for that specific split.
*   **Variance Reduction Formula:**
    `Variance_Reduction = Variance_Root - Σ (Weight_i * Variance_Child_i)`
    *   `Weight_i (W_i)` is the proportion of data points in a child node relative to the parent node.
    *   `W_i = (Number of elements in Child_i) / (Total elements in Parent Node)`.

*   **Calculation for Split 1 (`experience <= 2`):**
    *   Variance_Root = 60.8
    *   Left Child Weight (W1) = 1/5 (1 element out of 5 in root)
    *   Right Child Weight (W2) = 4/5 (4 elements out of 5 in root)
    *   Variance_Reduction_Split1 = 60.8 - [ (1/5 * 100) + (4/5 * 51) ]
    *   Variance_Reduction_Split1 = 60.8 - [ 20 + 40.8 ]
    *   Variance_Reduction_Split1 = 60.8 - 60.8 = **0**

*   **Calculation for Split 2 (`experience <= 2.5`):**
    *   Variance_Root = 60.8
    *   Left Child Weight (W1) = 2/5 (2 elements out of 5 in root)
    *   Right Child Weight (W2) = 3/5 (3 elements out of 5 in root)
    *   Variance_Reduction_Split2 = 60.8 - [ (2/5 * 82) + (3/5 * 46.66) ]
    *   Variance_Reduction_Split2 = 60.8 - [ 32.8 + 27.996 ]
    *   Variance_Reduction_Split2 = 60.8 - 60.796 = **0.004** (approx)

### Step 4: Select the Best Split

*   Compare the **Variance Reduction** values calculated for all potential splits.
*   The split with the **highest (maximum) Variance Reduction** is chosen as the best split for that node.
*   In the example:
    *   Variance Reduction for `experience <= 2` split was **0**.
    *   Variance Reduction for `experience <= 2.5` split was **0.004**.
*   Since **0.004 > 0**, the split at **`experience <= 2.5` is selected**.
*   This process continues recursively for subsequent nodes until stopping criteria are met (like a certain tree depth or minimum samples per leaf).

## 5. Predicting Output at Leaf Nodes

*   Once a Decision Tree Regressor is built and a new test data point traverses down to a **leaf node**.
*   The final predicted output for that test data point will be the **average (mean)** of all the output values present in that specific leaf node.
*   **Example:**
    *   If a leaf node contains values `40K, 42K`, the prediction for new data falling into this node will be `(40+42)/2 = **41K**`.
    *   If another leaf node contains `52K, 60K, 56K`, the prediction will be `(52+60+56)/3 = **56K**`.

This is how Decision Tree Regressor works by minimizing variance at each split, predicting continuous values by taking averages at the end.