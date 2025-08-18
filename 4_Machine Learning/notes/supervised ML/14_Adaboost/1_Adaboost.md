# AdaBoost: Boosting and Ensemble Machine Learning

## Introduction to Ensemble Machine Learning

*   We're discussing **AdaBoost**, which falls under **boosting**.
*   Both **bagging** and **boosting** can solve **classification** and **regression** problems.
*   **Common base learner**: All these algorithms (bagging and boosting) primarily use **decision trees** as their fundamental building blocks.

## Decision Trees and Their Limitations

*   If a **decision tree** is grown to its **complete depth**, it usually leads to **overfitting**.
*   **Overfitting** means:
    *   **Training accuracy is very high**.
    *   **Test accuracy is very less**.
*   In terms of bias-variance: Overfitting signifies **low bias** (good on training data) and **high variance** (poor generalisation on new data).

## Boosting Technique 

*   In boosting, models (called **weak learners**) are connected **sequentially**.
*   **How it works**:
    *   It starts with a weak learner.
    *   **Key idea**: Whatever records were **wrongly predicted** by the first weak learner are **sent to the next weak learner** for correction.
    *   This process continues sequentially through all models.
*   **Weak Learner Definition**: A model that hasn't been trained properly or hasn't learned much from the training dataset.
*   **Goal of Boosting**: To combine multiple **weak learners sequentially** to form a **strong learner**.

## AdaBoost: A Specific Boosting Algorithm

*   AdaBoost is a type of boosting algorithm.
*   **Key Difference from Random Forest**: AdaBoost **does not use majority voting or averaging**.
*   **Core Principle**: AdaBoost **assigns weights** to its weak learners. This is a very important concept.
*   **AdaBoost Function Representation**:
    *   `f = α₁ * M₁ + α₂ * M₂ + ... + αₙ * Mₙ`
    *   Here:
        *   `M₁` to `Mₙ` are the **decision tree stumps** (which are the weak learners in AdaBoost).
        *   `α₁` to `αₙ` are the **weights assigned to these weak learners**.
*   AdaBoost can solve both **classification** and **regression** problems.

### Decision Tree Stumps in AdaBoost

*   **What is a Decision Tree Stump?**
    *   It's a decision tree whose **depth is just one level**.
    *   This single-level depth is why they are called "stumps".
*   **Why are stumps considered weak learners?**
    *   Because they have such limited depth, they are inherently weak.
    *   A single decision tree stump typically leads to **underfitting**.
*   **Underfitting Characteristics (for a single stump)**:
    *   **Training accuracy is less** (e.g., 40% training accuracy, 45% test accuracy).
    *   In terms of bias-variance: Initially, a decision tree stump has **high bias** (doesn't learn enough from training data) and **low variance** (it's not complex enough to vary much).

### Combining Stumps in AdaBoost & Bias-Variance Trade-off

*   When **multiple decision tree stumps** are combined **sequentially** (one after another) and **with weights**:
    *   The entire combination ultimately leads to **low bias** and **high variance**.
    *   This is the transformation AdaBoost aims for: reducing the initial high bias of individual weak learners.


# AdaBoost: Building Strong Learners from Weak Stumps

## AdaBoost Overview

*   The main aim of AdaBoost is to **combine multiple weak learners** to create a **strong learner**.
*   In AdaBoost, the weak learners are specifically called **decision tree stumps**.
*   A **decision tree stump** has a **depth of only one** when it's constructed.
*   These notes will cover the math, intuition, and construction of AdaBoost trees.

## Dataset Example

*   The example dataset used has features like **salary** and **credit approval** (which refers to credit score).

## Step 1: Creating and Selecting the Best Decision Tree Stump

The **first step** in AdaBoost is to **create decision tree stumps** and then **select the best one**.

### A. Creating Decision Tree Stumps (Examples)

*   You can create decision trees using concepts like entropy and information gain, but here we focus on stumps with a **max depth of one**.
*   **Example 1: Decision Tree Stump based on 'Salary' feature**
    *   Condition: `salary <= 50k`
    *   If `salary <= 50k`: We observe **2 'Yes' outputs** and **2 'No' outputs**. This indicates some misclassification.
    *   If `salary > 50k`: We observe **2 'Yes' outputs** and **1 'No' output**.
    *   This is referred to as "decision tree stump one".

*   **Example 2: Decision Tree Stump based on 'Credit' feature**
    *   Condition: `credit = good`
    *   If `credit = good`: We observe **3 'Yes' outputs** and **0 'No' outputs**. This is a **pure split**.
    *   If `credit != good`: We observe **1 'Yes' output** and **3 'No' outputs**. This is an impure split.
    *   This is referred to as "decision tree stump two".

*   You can construct many such decision tree stumps based on different features.

### B. Selecting the Best Decision Tree Stump

*   Out of all the created weak learners (decision tree stumps), **only one will be selected** as the first decision tree stump in AdaBoost.
*   The selection is done by using **Entropy** or **Gini Index** (also known as Gini Impurity).
*   The goal is to understand which stump has a **better (less) impure split**.

*   **Calculation & Comparison using Entropy/Gini Index:**
    *   For the `salary <= 50k` split (2 Yes, 2 No):
        *   This is a **completely impure split**.
        *   Entropy would be **1**.
        *   Gini Impurity would be **0.5**.
    *   For `salary > 50k` (2 Yes, 1 No): This is also an impure split.
    *   For `credit = good` (3 Yes, 0 No): This is a **pure split**.
    *   For `credit != good` (1 Yes, 3 No): This is a slightly smaller impure split compared to the `salary <= 50k` case.
*   The formulas for Entropy and Gini Index are assumed to be known from decision tree classifier concepts.

### C. Summary of Step 1

*   The **first step** in AdaBoost is to **create all possible decision tree stumps** from the features.
*   Then, we **select the best decision tree stump** among them which is having less **weight error**.


# Adaboost: Calculating Stump Error and Performance

## Step 2 in Adaboost Classifier

This second step, with respect to the Adaboost classifier, basically involves performing two different operations:
1.  **Sum of total errors** of the stump.
2.  **Performance of the stump**.

### Assigning Sample Weights

the very first thing we do to calculate the total error and performance of the stump is to assign some weights to our data records.
*   **Count Records**: First, you need to count how many records are there in your dataset. For instance, if there are 7 records.
*   **Equal Weights**: You simply **assign equal weights to all the records**. So, for 7 records, each record gets a weight of `1/7`.
*   **Why Weights?**: These "sample weights" are important because they directly help us in calculating the **"total errors"**.

### Identifying Errors (Wrong Records)

Next, we identify which records were misclassified by our selected stump. These are the "wrong records".

### Calculating Total Error

Once we have identified the "wrong records," we move to calculate the total error.
*   **Definition**: The "total error" is simply the **"sum of all the sample weights of all the wrong records"**.
*   **Example Calculation**: In our example, if we have just **one wrong record**, and its sample weight is `1/7`, then our **total error will be `1/7`**.

### Calculating Performance of Stump

After finding the total error, the next crucial step is to calculate the "performance of the stump". We need to understand how well the stump performed based on the wrong records it created.
*   **The Formula**: To calculate the performance of the specific stump, we use this formula:
    `Performance of Stump = 1/2 * log_e((1 - Total Error) / Total Error)`
    *   Here, `log_e` is the natural logarithm, often written as `ln`.
*   **Applying the Formula (Example)**:
    *   Our `Total Error` is `1/7`.
    *   Substituting this into the formula: `1/2 * log_e((1 - 1/7) / (1/7))`.
    *   This simplifies to: `1/2 * log_e((6/7) / (1/7))`, which further becomes `1/2 * log_e(6)`.
*   **Result**: After computation, the performance for this particular stump comes out to be approximately **`0.896`**.

### Relating Performance to the Adaboost Function

This `0.896` value is highly important as it defines the "weight" of our first decision tree stump.
*   **Alpha (Weight)**: This performance value, `0.896`, is assigned as the **`alpha1` (or weight)** for our first model, which is this decision tree stump (`M1`).
*   **Adaboost Function Structure**: Remember the Adaboost function (like `f`) is typically represented as a sum of weighted models:
    `f = Alpha1 * M1 + Alpha2 * M2 + ...`
    *   Here, `Alpha` values are the **weights**, and `M` values represent the individual models (decision tree stumps).
    *   So, our `0.896` value becomes `Alpha1` for our `M1` decision tree stump.

### The Sequential Connection: Passing Wrong Records Forward

This is a very fundamental concept in how Adaboost works.
*   **Weak Learner**: The decision tree stump we just evaluated is considered a "weak learner". It will, naturally, predict some records incorrectly.
*   **Focusing on Errors**: The **wrong records** that this weak learner misclassified are not just discarded. Instead, they are **passed on to the "next decision tree stump"**.
*   **Sequential Learning**: This mechanism ensures that Adaboost sequentially connects these weak learners. The subsequent learners (`M2`, `M3`, etc.) will specifically try to correct the errors made by the previous ones by focusing more on those misclassified records.


# AdaBoost: Updating Weights for Decision Stumps

## Step 3: Updating Weights

In AdaBoost, after calculating the total errors and the performance of a decision stump (our weak learner), the next crucial step is to **update the weights of the data points**.

### Why Update Weights?

*   The goal is to ensure that the **wrongly classified records are given more importance** and are sent to the *next* decision tree stump for better focus.
*   The performance of the stump from the previous step is important as it decides the weight to be given to the first decision stump.

### The Core Logic of Weight Updation

We need to perform two important actions for weight updates:
1.  **Correctly Classified Points**: For points that the current decision stump classified *correctly*, we need to **decrease their weights**.
2.  **Incorrectly Classified Points**: For points that the current decision stump classified *incorrectly*, we need to **increase their weights**.

**The logic behind this is simple**: By increasing the weight of wrongly classified points, we make sure there's a **high probability that the *next* decision tree stump will pick these challenging records**. This helps the overall model learn from its mistakes.

### The Math Behind Weight Updation (Formulas)

Different formulas are used for correctly and incorrectly classified points.

#### 1. Weight Updation for **Correctly Classified Points**

*   **Formula**: `Older Weight × e ^ (-Performance of Stump)`
    *   Notice the **minus sign** in the exponent.
*   **Example Calculation**:
    *   Let's say `Older Weight` was `1/7` and `Performance of Stump` was `0.896`.
    *   `1/7 × e ^ (-0.896)` approximately `0.058`.
*   **Result**: All correctly classified points will have their weights updated to this new, *decreased* value (e.g., `0.058`).

#### 2. Weight Updation for **Incorrectly Classified Points**

*   **Formula**: `Older Weight × e ^ (Performance of Stump)`
    *   Here, the exponent has a **plus sign** (it's positive).
*   **Example Calculation**:
    *   Using the same values: `Older Weight` as `1/7` and `Performance of Stump` as `0.896`.
    *   `1/7 × e ^ (0.896)` approximately `0.349`.
*   **Result**: The incorrectly classified points will have their weights updated to this new, *increased* value (e.g., `0.349`).

### Summary of Step 3

In short, Step 3 is all about **adjusting the weights of the data points based on whether they were correctly or incorrectly classified** by the current decision stump. Weights of correctly classified points decrease, and weights of incorrectly classified points increase.

# AdaBoost: Normalizing Weights and Assigning Bins

## Normalizing Weights

*   **The Problem**: After updating weights, if you sum all the updated weights, the total **will not be one**. For example, the sum might be around 0.697.
*   **The Need for Normalization**: Initially, when sample weights are assigned, their summation is typically one. For the total computation to be consistent and to ensure the sum of weights equals one, **normalization is essential**.
*   **How to Normalize**:
    *   Take each individual updated weight.
    *   **Divide each weight by the total sum of all updated weights** (e.g., by 0.697).
    *   **Example**: If an updated weight is 0.058, dividing it by 0.697 gives approximately 0.08. A larger weight like 0.349 might become 0.50 after normalization.
*   **Outcome**: After normalization, when you sum all the new normalized weights, the total **will be equal to one**. This is the first crucial step.

## Assigning Bins

*   **Main Target**: After decision tree stump one is created, if it makes incorrect predictions, **those wrong records need to be sent to the next decision tree stump** (stump two).
*   **The Mechanism**: To achieve this, we need a mechanism to ensure the machine learning algorithm sends mostly, or only, the incorrectly classified records to the next stump. This mechanism is **assigning bins**.
*   **Creating Bin Ranges**:
    *   Bins are created as a **range based on the normalized weights**.
    *   The first range starts from zero.
    *   **Example Bin Ranges**:
        *   0 to 0.08 (based on the common normalized weight of 0.08).
        *   0.08 to 0.16.
        *   0.16 to 0.24.
        *   0.24 to 0.32.
        *   0.32 to 0.40.
        *   Then, ranges might jump based on higher normalized weights, e.g., 0.40 to 0.90 (if 0.50 is a normalized weight).
    *   The **maximum bin size** will correspond to the higher normalized weights, particularly those associated with wrongly predicted records.
*   **Purpose of Bins**:
    *   The records that were **wrongly predicted** by the decision tree stump one will have a **larger weight (and thus a larger range in the bins)**.
    *   The goal is to use these bins to **send these "wrong" records more frequently** to the next decision tree stump (stump two).
    *   This ensures that decision tree stump two will specifically **train on these wrongly predicted records**, trying to correct them.


# Iterative Data Selection for Decision Tree Stumps 

## Introduction to Data Selection

*   The main point here is **how we select new data points to send to the next step**.
*   We use an **iterative process** for this.
*   In this iterative process, we generate **random values between 0 and 1**.

## Bin Assignment and Feature Context

*   New records are selected based on **pre-created bins or bin assignments**.
*   Imagine we have features like **Salary, Credit, and Approval**.
*   A **random number (between 0 and 1)** is generated for each record.
*   We then check **where this random number falls in the pre-defined bin ranges**.
    *   *Example:* If the random number is `0.50`, it falls in the `0.40-0.90` range.

## Data Selection Process: Focusing on Incorrect Records

*   The selection process primarily picks up **incorrectly predicted records**.
*   **How records are selected based on random numbers:**
    *   If the random number is `0.50`, records like "greater than 50K normal and yes" (which are incorrect) get selected. These selected records are passed to the next decision tree.
    *   If the random number is `0.10`, "less than 50K Good and yes" gets selected.
    *   If the random number is `0.60`, "greater than 50K normal Yes" gets selected.
        *   **Important insight**: If the **gap in the bin (range) is large, there's a high chance that row will be selected repeatedly**.
        *   The **next 'weak learner' (decision tree stump) will then focus on these frequently selected or incorrectly classified records**.
    *   Other examples: `0.75` (repeats "greater than 50K and yes"), `0.24` ("less than 50K green and yes"), `0.32` ("greater than 50K b and no"), `0.87` (again picks incorrect records like "greater than 50K normal and yes").
*   **Summary of selected records**: You'll notice certain **incorrectly classified points getting picked up again and again**.
*   **What happens next**: This entire set of **selected records forms the new dataset (Step Six) and is sent to the next decision tree stump for training**.

## The Iterative Process for Decision Tree Stumps

*   Once the new dataset is formed, the **entire process starts again**.
*   **Sample Weights**: For this new dataset, **sample weights are re-assigned**. For instance, if there are 6 records, each might get a weight of `1/6`.
*   **Repetition of Steps**: All the steps, from **Step Two to Step Six, keep on repeating**.
*   **When does it stop?**: This iterative process continues until **all the decision tree stumps are sequentially finished**.
*   **Practical Aspect**: In real-world scenarios, about **100 decision tree stumps** are typically initialized during model training.
*   **Updating Weights and Calculating Performance**:
    *   After assigning sample weights, the weights get updated.
    *   Then, you calculate the **total error** and the **performance of the stump**.
    *   *Example*: If a model has a performance stump value of `0.65`.
*   **Combining Models**:
    *   The overall function will combine the outputs of different decision tree stumps. It looks something like `alpha_one * model_one + alpha_two * model_two`.
    *   `model_two` here refers to the current decision tree stump.
    *   `alpha_two` will be its performance value (e.g., `0.65`), and `alpha_one` was the previous stump's performance (e.g., `0.896`).
    *   The idea is to **combine all these values to predict the final output**.
*   **Continuous Learning**: The process involves **continuously creating multiple stumps** and repeating these steps.

# AdaBoost: Final Classification Prediction

## How AdaBoost Makes Final Predictions (For Classification)

*   This section explains **how AdaBoost predicts for new test data**, specifically for **classification problems**.
*   Unlike Random Forest, AdaBoost **does not use majority voting**.

## Key Components for Prediction

*   **Weak Learners:** AdaBoost uses multiple **decision tree stumps** (e.g., Decision Tree Stump 1, 2, 3, etc.). Each stump gives an output like "yes" or "no" for a given test data.
*   **Alpha Weights:** An important parameter is the **'alpha' weight** associated with each weak learner (e.g., alpha_1, alpha_2, alpha_3, alpha_N).
    *   These alpha values are pre-computed.
    *   Alpha values can be **positive or negative**.
    *   **Example Alpha Values:** 0.896, 0.650, 0.244, -0.30.

## The Final Prediction Formula

*   The **final prediction function** is a **weighted sum** of the individual models (weak learners):
    `Final Function = (alpha_1 * model_1) + (alpha_2 * model_2) + (alpha_3 * model_3) + ...`

## Step-by-Step Example of Prediction

Let's take an example where new test data is: "salary less than 50K and credit score is good".

*   **Individual Model Outputs and Weights:**
    *   **Model 1:** Says **"yes"**, Alpha 1 = **0.896**
    *   **Model 2:** Says **"no"**, Alpha 2 = **0.650**
    *   **Model 3:** Says **"yes"**, Alpha 3 = **0.244**
    *   **Model 4:** Says **"no"**, Alpha 4 = **-0.30**

*   **Combining Weights for Each Class:**
    1.  **For "Yes" output:** Add up the alpha values of models that predicted "yes".
        *   `0.896 (from Model 1) + 0.244 (from Model 3) = **1.136**`
    2.  **For "No" output:** Add up the alpha values of models that predicted "no".
        *   `0.650 (from Model 2) + (-0.30) (from Model 4) = **0.350**`

*   **Final Decision:**
    *   Compare the combined weights for "yes" and "no".
    *   `1.136 (for Yes)` is **greater than** `0.350 (for No)`.
    *   Therefore, the **maximum output** from the combined weak learners (which form the strong learner) is **"yes"**.
    *   This means for the given test data, the credit card will **definitely be approved**.

## 5. AdaBoost for Regression Problems (Briefly)

*   For **regression problems** using AdaBoost, only **two main things change**.
*   Instead of `entropy` (used in classification to find the best split), **Mean Squared Error (MSE)** is used to compute which decision tree stump is the best.
*   Most other aspects of the final prediction process remain **almost the same**.
*   The output in regression will be a **continuous value** with some weights assigned to it.