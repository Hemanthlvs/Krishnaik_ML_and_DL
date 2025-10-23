# Decision Tree Pruning: Post-pruning and Pre-pruning Techniques

## What is Pruning?

*   Just like a gardener prunes plants to maintain their shape and ensure proper growth, in decision trees, we prune to manage their structure and prevent issues.
*   When a decision tree is built using default parameters on a training dataset, it keeps splitting until it reaches pure leaf nodes (where all outputs are the same).

## The Problem: Overfitting

*   When a decision tree splits completely to its depth (i.e., until all leaf nodes are pure), it often leads to a scenario called **overfitting**.
*   **Overfitting means**:
    *   Your **training accuracy is very high** because the splitting was done completely till the end.
    *   But, your **test accuracy will be very, very low**.
*   This scenario usually results in **low bias and high variance**.
    *   Bias is related to training data.
    *   Variance is related to test data.
    *   Since test accuracy is low, we say it's high variance.

## Solutions to Overfitting: Pruning Techniques

To reduce overfitting, we use two main techniques:

1.  **Post-pruning**
2.  **Pre-pruning**

### 1. Post-pruning

*   **Meaning**: In post-pruning, we **first construct the complete decision tree** to its full depth.
*   **Then, after constructing, we start pruning or cutting** the branches.
*   **Example**: Suppose a node has 9 "yes" and 2 "no" outputs. The ratio of "yes" is very high. Even if the default tree splits this further into pure nodes (like 9 "yes" and 0 "no", and 0 "yes" and 2 "no"), in post-pruning, we might decide to cut the branch at the point where 9 "yes" and 2 "no" was, and declare that as a leaf node, predicting "yes" as the output. This prevents unnecessary deep splits.
*   **Why**: It ensures the tree does not lead to an overfitting scenario, and for test data, it provides a more generic output.
*   **When to use**: **Post-pruning should be applied for smaller datasets**.
    *   **Reason**: If you have millions of records, creating the decision tree completely till the end and then pruning it would be very time-consuming and computationally expensive.

### 2. Pre-pruning

*   **Meaning**: In pre-pruning, you **don't construct the decision tree entirely** like in post-pruning. Instead, you prune **while you are constructing the decision tree**.
*   **How it's done**: We **play with or tune hyperparameters** while building the tree. This is also known as **hyperparameter tuning**.
*   **Hyperparameters in Decision Trees (from scikit-learn documentation example)**:
    *   `criterion`: Can be 'gini', 'entropy' (or 'log_loss' which was part of logistic regression).
    *   `splitter`: Defines how the split should happen, e.g., 'best' or 'random'.
    *   `max_depth`: Limits the maximum depth of the tree.
    *   `max_features`: Maximum number of features to consider when looking for the best split.
    *   `min_samples_split`: Minimum number of samples required to split an internal node.
    *   `min_samples_leaf`: Minimum number of samples required to be at a leaf node.
    *   `min_weight_fraction_leaf`: Minimum weighted fraction of the sum of total weights (all the input samples) required to be at a leaf node.
*   **Tools for tuning**: We often use techniques like `GridSearchCV` for hyperparameter tuning.
*   **Benefit**: By setting these parameters initially, the decision tree is constructed automatically within those constraints, preventing it from growing too deep and overfitting from the start.

Both techniques aim to **reduce overfitting** and ensure the decision tree performs well on unseen (test) data.