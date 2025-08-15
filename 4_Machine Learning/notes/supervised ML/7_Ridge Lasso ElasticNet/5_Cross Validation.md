# Cross-Validation Techniques for Machine Learning Models

## Introduction: Why Cross-Validation?

### Data Splitting Basics
*   Initially, a **dataset** is divided into two main parts:
    *   **Training data set**: Used for training the machine learning model.
    *   **Test data set**: Used to check the performance of the model on new, unseen data.
*   For **hyperparameter tuning**, the training data set is further divided into two parts:
    *   **Train data**: Used to train the model.
    *   **Validation data set**: Used to validate the model and perform hyperparameter tuning.
*   The **test data** is never shown to the model during training or validation. It is only used after the model is completely trained and validated to check its performance using various metrics (e.g., accuracy, precision, recall, R-squared, mean absolute error).

### Why Do We Need Cross-Validation?

We use cross-validation to:

- Check if the model works well on unseen data
- Avoid overfitting to the training data
- Get a more reliable and fair estimate of model performance


## Types of Cross-Validation

### 1.Leave-One-Out Cross-Validation (LOOCV or LORCV)
*   **Concept**: From the training data, **one record** is chosen as the **validation data**, and the **remaining records** constitute the **training data**.
*   **Process**:
    *   This experiment is **repeated for every single record** in the training data.
    *   If there are 500 records, 500 experiments are performed.
    *   An accuracy is obtained for each experiment.
    *   The average of all these accuracies can be calculated.
*   **Disadvantages**:
    *   **High Computational Complexity**: As the dataset size increases, the number of experiments (equal to the number of records) and thus the complexity of training the model increases significantly. It's rarely used today.
    *   **Overfitting**: This technique often leads to overfitting.
        *   **Overfitting**: Training accuracy is very high because the training data size is huge, and the validation data is extremely small (only one record).
        *   When this model is tested with new, unseen test data, its performance (accuracy) will significantly drop.

### 2. Leave-P-Out Cross-Validation
*   **Concept**: Similar to LOOCV, but instead of leaving one record out, **'p' number of records** are set as the validation data.
*   **'p' value**: Can be set as a **hyperparameter** (e.g., 10, 20, 30).
*   **Process**: The overall process is the same as LOOCV, but with 'p' records for validation in each experiment.

### 3. K-Fold Cross-Validation
*   **Concept**: The training data is divided into **'k' equal parts or "folds"**.
*   **Process**:
    *   In each experiment, **one fold** acts as the **validation data**, and the **remaining k-1 folds** are combined to form the **training data**.
    *   This process is repeated **'k' times**, ensuring each fold gets a chance to be the validation set.
    *   **Example**: For 500 records and k=5, each fold (validation data) will have 100 records (500/5).
        *   Experiment 1: First 100 records for validation, remaining 400 for training.
        *   Experiment 2: Next 100 records for validation, remaining for training.
        *   ...and so on, up to Experiment 5, covering all 500 records.
    *   **Accuracy Calculation**: An accuracy is obtained for each of the 'k' experiments.
    *   **Result**: The **average, maximum, and minimum accuracies** across all 'k' folds can be calculated to provide a more robust performance estimate.

### 4. Stratified K-Fold Cross-Validation
*   **Problem with standard K-Fold (especially for Classification)**:
    *   In classification problems, especially with imbalanced datasets, standard K-Fold might create validation sets where one type of category (e.g., all 'ones' or all 'zeros' in binary classification) predominates.
    *   This can lead to the model not being trained or evaluated properly because the validation data doesn't represent the full range of outputs.
*   **Solution**: Stratified K-Fold addresses this by ensuring that the **validation data in each fold has an evenly distributed proportion of output classes/categories**.
    *   **Example**: If the overall dataset has a 60% 'ones' and 40% 'zeros' ratio, each validation fold will also attempt to maintain a similar 60/40 ratio.
*   **Key Difference from K-Fold**: The primary difference is the **proportionate distribution of output classes in the validation sets**. Otherwise, the process is similar to K-Fold.
*   **Application**: Primarily used for **classification problems** to handle class imbalance in validation splits.

### 5. Time Series Cross-Validation
*   **Application**: Specifically designed for **time series data**, where data points have a temporal dependency (e.g., product reviews over time, stock prices).
*   **Temporal Constraint**: In time series data, the order of events matters.
*   **Rule for Splitting**:
    *   Data must be split **sequentially based on time** (e.g., day 1, day 2, day 3, etc.).
    *   **Cannot randomly pick up days** and put them into training or validation sets.
    *   **Training data must always precede validation data in time**.
*   **Process**:
    *   An initial set of days (e.g., Day 1 to Day 4) is used for **training data**.
    *   The subsequent block of days (e.g., Day 4 to Day N) is used for **validation data**.
    *   This ensures that the model is always trained on past data and validated on future (unseen) data points, mimicking real-world time series forecasting.
*   **Purpose**: Essential for models where outcomes change over time and are time-dependent.
