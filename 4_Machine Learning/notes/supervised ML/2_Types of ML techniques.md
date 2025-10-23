# Machine Learning Techniques

1.  **Supervised Machine Learning**
2.  **Unsupervised Machine Learning**
3.  **Reinforcement Machine Learning**

## 1. Supervised Machine Learning

*   **Definition**: In supervised machine learning, your goal is to **predict an output based on given input data**. A key characteristic is the presence of a **dependent or output feature**.
*   **Features**:
    *   **Independent Features (Input Features)**: These are the characteristics or data points you use to make a prediction (e.g., size of house, number of rooms, number of study hours, number of play hours).
    *   **Dependent Feature (Output Feature)**: This is the value you want to predict. Its value changes as the input values change (e.g., price of the house, whether a person passes or fails).
*   **Why "Supervised"?**: It's called supervised because you have a specific output (dependent feature) that helps the model learn to make predictions.

### Types of Problems in Supervised ML:

There are two main types of problems solved using supervised machine learning:

1.  **Regression Problem Statement**:
    *   **Output Feature**: The dependent or output feature is **continuous**.
    *   **Example**: Predicting the **house price** (e.g., $450K, $500K) based on size and number of rooms. Prices are continuous values.
2.  **Classification Problem Statement**:
    *   **Output Feature**: The dependent or output feature is **categorical** (not continuous).
    *   **Example**: Predicting whether a person will **pass or fail** based on study and play hours. "Pass" or "Fail" are categories.
    *   **Sub-types of Classification**:
        *   **Binary Classification**: The output has **only two fixed categories** (e.g., pass/fail, yes/no).
        *   **Multi-class Classification**: The output has **more than two categories** (e.g., predicting if someone will pass, fail, or maybe pass/fail).

### Supervised ML Algorithms Mentioned:

*   **For Regression**: Linear Regression, Ridge and Lasso Regression, Elastic Net.
*   **For Classification**: Logistic Regression.
*   **For Both Regression and Classification**: Decision Tree, Random Forest, AdaBoost, XGBoost, Catboost (these are often part of "bagging and boosting" techniques).


## 2. Unsupervised Machine Learning

*   **Definition**: In unsupervised machine learning, **we do not know the output feature**, and we don't aim to predict anything. Instead, the goal is to **find similar clusters or groups** within the data.
*   **Example**: **Customer Segmentation**.
    *   **Data**: Features like salary and spending score are used. There is no "output" to predict based on these inputs.
    *   **Purpose**: To group customers with similar characteristics (e.g., high salary and high spending, low salary and low spending). This helps companies target specific groups, like sending discount coupons to high-spending customers.
*   **Output**: The result is a set of **clusters** or groups of similar data points.

### Unsupervised ML Algorithms Mentioned:

*   **Clustering Algorithms**: K-means, Hierarchical Mean, DB scan.

## 3. Reinforcement Machine Learning

*   **Definition**: This technique is fundamentally different from supervised and unsupervised learning. The application **learns things by itself** by receiving **rewards**.
*   **How it Works**: An agent (the learning entity) takes actions in an environment and receives feedback in the form of rewards or penalties. It learns to maximize rewards over time.
*   **Examples**:
    *   **A baby learning to walk**: A baby falls down (gets hurt), learns not to get hurt, and slowly learns to walk by doing things that lead to positive outcomes (like walking without falling).
    *   **Children and good marks**: Parents give rewards for good marks, encouraging the child to repeat actions that lead to good marks.