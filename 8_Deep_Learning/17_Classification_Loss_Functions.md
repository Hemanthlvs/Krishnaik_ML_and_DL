# Classification Loss Functions: Cross-Entropy Explained

## I. Introduction to Loss Functions
*   Loss functions (also called cost functions) are essential in machine learning.
*   The primary goal is to reduce these loss functions using an optimizer.

## II. Types of Classification Problems
*   There are generally two types of classification problems:
    1.  **Binary Classification**: Outputs are one of two classes (e.g., 0 or 1).
    2.  **Multi-class Classification**: Outputs belong to more than two classes (e.g., Good, Bad, Neutral).

## III. Cross-Entropy as the Core Classification Loss Function
*   **Cross-Entropy** is the specific loss function used for classification problems.
*   There are three main types of Cross-Entropy loss functions, chosen based on the problem statement:
    1.  **Binary Cross-Entropy (BCE)**
    2.  **Categorical Cross-Entropy (CCE)**
    3.  **Sparse Categorical Cross-Entropy (SCCE)**

## IV. Binary Cross-Entropy (BCE)
*   **Use Case**: Specifically used for **binary classification** problems.
*   **Formula (Log Loss)**:
    ```
    Loss = -y * log(y_hat) - (1 - y) * log(1 - y_hat)
    ```
    *   `y`: Actual value (0 or 1).
    *   `y_hat`: Predicted value .
*   **Formula Breakdown**:
    *   If `y = 0`: The first term `(-y * log(y_hat))` becomes zero. The loss simplifies to `-(1 - 0) * log(1 - y_hat)` which is `-log(1 - y_hat)`.
    *   If `y = 1`: The second term `(-(1 - y) * log(1 - y_hat))` becomes zero. The loss simplifies to `-1 * log(y_hat)` which is `-log(y_hat)`.
*   **Calculating `y_hat`**:
    *   For binary classification, the **Sigmoid activation function** is applied at the output layer of the neural network.
    *   The sigmoid function outputs a value between 0 and 1.
    *   `y_hat` is the output obtained after applying the sigmoid activation function.
*   **Purpose**: Calculates the difference between the actual `y` and predicted `y_hat` values. This loss is then minimized through backpropagation and optimizers.

## V. Categorical Cross-Entropy (CCE)
*   **Use Case**: Specifically used for **multi-class classification** problems.
*   **Preprocessing `y`**:
    *   The actual output variable (`y`) is converted using **One-Hot Encoding (OHE)**.
    *   For each output, a vector is created where the element corresponding to the correct category is `1`, and all other elements are `0`.    
*   **Formula**:
    ```
    Loss = - Σ (j=1 to C) [ y_ij * log(y_hat_ij) ]
    ```
    *   `C`: Total number of categories.
    *   `y_ij`: Actual value (from one-hot encoding), which is `1` if the element belongs to class `j` for data point `i`, and `0` otherwise.
    *   `y_hat_ij`: Predicted probability of data point `i` belonging to class `j`.
*   **Calculating `y_hat`**:
    *   For multi-class classification, the **Softmax activation function** is applied at the output layer.
    *   Softmax outputs a probability distribution over the categories, where the sum of probabilities for all categories equals 1.
    *   Example: For three categories, `y_hat` might be `[0.2, 0.3, 0.5]`, indicating 20% probability for the first category, 30% for the second, and 50% for the third.
*   **Key Characteristic**: CCE provides the probabilities for **all** categories, not just the predicted one.

## VI. Sparse Categorical Cross-Entropy (SCCE)
*   **Use Case**: Also used for **multi-class classification** problems.
*   **Difference from CCE**:
    *   However, SCCE's final output focuses on providing only the **index** of the category with the highest probability, rather than the probabilities of all categories.
    *   Example: If probabilities are `[0.2, 0.3, 0.5]`, SCCE would output `2th index which is 0.5`.
*   **Disadvantage**: SCCE results in **losing information** about the probabilities of other categories.

## VII. When to Use Which
## Combination 1: Binary Classification
*   **Hidden Layer Activation**: ReLU or its variants (e.g., Leaky ReLU, PReLU, ELU)
*   **Output Layer Activation**: Sigmoid
*   **Problem Type**: Binary Classification
*   **Loss Function**: Binary Cross Entropy

## Combination 2: Multi-Class Classification
*   **Hidden Layer Activation**: ReLU or its variants (e.g., Leaky ReLU, PReLU, ELU)
*   **Output Layer Activation**: Softmax
*   **Problem Type**: Multi-Class Classification
*   **Loss Function**: Categorical Cross Entropy or Sparse Cross Entropy

## Combination 3: Regression
*   **Hidden Layer Activation**: ReLU or its variants (e.g., Leaky ReLU, PReLU, ELU)
*   **Output Layer Activation**: Linear
*   **Problem Type**: Regression
*   **Loss Functions**:
    *   Mean Squared Error (MSE)
    *   Mean Absolute Error (MAE)
    *   Huber Loss
    *   Root Mean Squared Error (RMSE)
