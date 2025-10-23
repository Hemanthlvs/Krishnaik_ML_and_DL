# Ensemble Techniques: Bagging and Boosting

## Introduction to Ensemble Techniques
*   Ensemble techniques help us **combine multiple machine learning algorithms together** to make predictions.
*   The main goal is to **achieve good accuracy** by combining multiple models.
*   These techniques, especially Bagging and Boosting, are widely used in **machine learning competitions and hackathons like Kaggle** to solve problems and get very good accuracy.
*   There are two main types of Ensemble Techniques: **Bagging** and **Boosting**.

## Bagging (Bootstrap Aggregating)

### What is Bagging?
*   Bagging involves using multiple machine learning algorithms (called **base learners**) to train on **different samples of the dataset**.
*   The idea is that each base learner becomes an **expert on its own specific subset of data**.
*   A prominent algorithm under Bagging is **Random Forest**.

### How Bagging Works:
1.  **Dataset Preparation:** You start with your main training dataset.
2.  **Base Learners:** You have multiple **base learners** (which are individual machine learning algorithms). These can be the **same algorithm** (e.g., multiple decision trees) or **different algorithms** (e.g., a decision tree, logistic regression, Naive Bayes). You can take as many base learners as you want, often around 100 by default in some algorithms like Random Forest.
3.  **Data Sampling:** Each base learner is given a **sample of the dataset** (e.g., D', D'', D''').
4.  **Parallel Training:** A very important point is that **all these base learners are trained parallelly (at the same time), not sequentially**. Each model trains independently on its own sample.
5.  **Prediction:** When a new test data comes for prediction, it's passed through **all the trained models**.
6.  **Final Output:**
    *   **For Classification Problems (Binary or Multiclass):** The final output is determined by **Majority Voting Classifier**. This means whatever output (e.g., 0 or 1) is predicted by the maximum number of models, that becomes the final prediction.
    *   **For Regression Problems:** The final output is the **average of all the continuous outputs** given by each base learner.

## Boosting

### What is Boosting?
*   Boosting aims to **combine multiple "weak learners" sequentially to form a "strong learner"**.
*   The idea is like combining experts from different domains (e.g., geography, physics, chemistry) to solve a complex problem statement.
*   Algorithms under Boosting include **AdaBoost, Gradient Boosting, and XGBoost**.

### How Boosting Works:
1.  **Dataset:** You start with your entire dataset.
2.  **Weak Learners:** You have multiple **weak learners** (models).
3.  **Sequential Training:** Unlike bagging, boosting models are **connected sequentially**.
    *   **Model 1 (M1)** trains on the entire dataset.
    *   M1 might make some incorrect predictions. It then **passes those "wrongly predicted records" along with some other records from the dataset to Model 2 (M2)**. The focus is on learning from past mistakes.
    *   **Model 2 (M2)** trains on these specific records (the ones M1 struggled with and some new ones). M2 will also make some errors, and it passes **its wrongly predicted records (and some more data) to Model 3 (M3)**.
    *   This process **continues sequentially** with N number of models, each one trying to correct the errors of the previous one.
4.  **Prediction:** When a new test data arrives, each model in the sequence contributes its prediction based on its "strength" or specialized learning.
5.  **Final Output:**
    *   **For Classification Problems:** Similar to bagging, a **Majority Voting Classifier** can be used to combine the predictions from all the weak learners.
    *   **For Regression Problems:** The average of the predictions from all the models is used.

## Key Differences (Bagging vs. Boosting)
*   **Bagging:**
    *   Uses **Base Learners** (can be strong or weak).
    *   Models are trained **Parallelly**.
    *   Each model trains on a **sample of the data** independently.
*   **Boosting:**
    *   Uses **Weak Learners**.
    *   Models are trained **Sequentially**.
    *   Later models **focus on correcting errors** made by previous models in the sequence.