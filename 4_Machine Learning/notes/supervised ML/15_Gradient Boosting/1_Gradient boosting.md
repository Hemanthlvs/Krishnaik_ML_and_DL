# Gradient Boosting Machine Learning 

## Introduction to Gradient Boosting

*   **Gradient Boosting** is a machine learning algorithm that can solve **both regression and classification problems**.
*   It's a part of the **boosting ensemble technique**.
*   In boosting, **decision trees are created sequentially**, and all these **weak learners are combined to form a strong learner**.
*   The concept is similar to AdaBoost, where decision trees are also constructed one after another.

## Example Problem Statement: Regression

The explanation uses a regression dataset to show how Gradient Boosting works.

*   **Dataset Features:**
    *   **Independent Features (Inputs):** `experience`, `degree`.
    *   **Dependent Feature (Output):** `salary`.
*   Since `salary` is a **continuous value**, it's considered a regression dataset.

## Steps to Create a Gradient Boosting Machine Learning Algorithm

Here are the step-by-step procedures to build a Gradient Boosting model:

### Step 1: Create a Base Model (H0)

*   The **first step** is to create a **base model**.
*   This base model should **not be biased** to any specific value; it gives a **default value**.
*   For a regression problem, this **default value is the average of all the true output (`y`) values** (e.g., `salary`).
*   **Example Calculation:** If salaries are 50K, 70K, 80K, 100K, the average is (50+70+80+100) / 4 = **75K**.
*   So, the **output of this base model for any input will always be 75K**.

### Step 2: Compute Residuals (Errors) - R1

*   The next step is to compute the **residuals or errors**.
*   **Residuals** are simply the **difference between the true output (`y`) and the predicted output from the base model (`y_hat`)**.
*   **Formula:** `Residual = True Value (y) - Predicted Value (y_hat)`.
*   The **predicted output (`y_hat`) from the base model is 75K** for all records.
*   **Example Calculation (for Residuals R1):**
    *   For `y=50K`, `Residual = 50 - 75 = -25K`.
    *   For `y=70K`, `Residual = 70 - 75 = -5K`.
    *   For `y=80K`, `Residual = 80 - 75 = 5K`.
    *   For `y=100K`, `Residual = 100 - 75 = 25K`.
*   These are our **first set of residuals (R1)**.

### Step 3: Construct a Decision Tree (H1)

*   Now, we construct a **decision tree (H1)**.
*   **Key difference:** Unlike AdaBoost, which might use simple decision stumps, Gradient Boosting constructs a **full decision tree**.
*   **Inputs for this decision tree:** The **original independent features (X(I))** like `experience` and `degree`.
*   **Output for this decision tree:** The **residuals (R1)** we calculated in the previous step.
*   **How a Regression Decision Tree is Built:** It involves splitting the data based on features, typically minimizing **Mean Squared Error (MSE)** and considering gain or variance reduction to find the best splits.
*   After this decision tree (H1) is trained, if you pass any record to it, it will give some outputs. These outputs are essentially **new residuals (R2)** that the tree tries to predict.
    *   **Example outputs (R2) from DT1:** -23K, -3K, 3K, 20K.

### Step 4: Compute Updated Predicted Output and Introduce Learning Rate

*   To get the final predicted output, you **don't just add** the base model's output and the decision tree's output (e.g., 75K + (-23K) = 52K).
*   This simple addition usually leads to **overfitting**.
*   To prevent overfitting and control how much each new tree influences the total prediction, a **Learning Rate (Alpha, α)** is introduced.
*   The **learning rate (α) is a value usually between 0 and 1**.
*   A common value for alpha is **0.1**.
*   **Updated Predicted Output Calculation:**
    *   `New Predicted Output = Base Model Output + (Learning Rate * Output from Decision Tree 1)`.
    *   **Formula:** `y_hat_new = H0(x) + α * H1(x)` [similar to 23, 24].
*   **Example Calculation for the first record:**
    *   Base model output: 75K.
    *   DT1 output (R2 for first record): -23K.
    *   Learning Rate (α): 0.1.
    *   `New Predicted Output = 75 + (0.1 * -23)`.
    *   `= 75 - 2.3 = 72.7K`.
*   This `72.7K` is the **updated predicted output for the first record** after considering the base model and the first decision tree. Similar calculations are done for other records.
    *   For the second record: `75 + (0.1 * -3) = 75 - 0.3 = 74.7K`.

### Step 5: Compute New Residuals (R3) and Repeat the Process

*   After getting the **updated predicted outputs (`y_hat_new`)**, new residuals are calculated.
*   These new residuals (`R3`) are again the **difference between the true `salary` values and the `y_hat_new` values**.
*   **Example Calculation for first record:** `R3 = 50K (True Value) - 72.7K (Updated Predicted Output) = -22.7K`.
*   This entire process then **repeats sequentially**.
*   The **next decision tree (H2)** will be constructed using the **original independent features (X of I)** as inputs, but this time using the **new residuals (R3)** as its output.
*   After H2 is trained, it will produce its own outputs (R4), which are again used to update predictions and calculate further residuals, and so on.
*   This **iterative process continues**, where each new decision tree tries to correct the errors (residuals) of the previous models.

## Final Function of Gradient Boosting

The final combined function (`f(x)`) for a Gradient Boosting model is a **summation of the base model and all sequentially added decision trees, each scaled by a learning rate**.

*   **Mathematical Notation:**
    `f(x) = H0(x) + α1 * H1(x) + α2 * H2(x) + ... + αn * Hn(x)`
*   **Generalized Summation Notation:**
    `f(x) = Σ (αi * Hi(x))` where `i` ranges from `0` to `n`.
    *   Here, `H0(x)` is the **base model**.
    *   `Hi(x)` (for `i > 0`) represents the **decision tree built at each sequential step**.
    *   `αi` is the **learning rate** for each decision tree. Often, a **single learning rate value (e.g., 0.1) is used for all decision trees**.
*   This final function is what the Gradient Boosting algorithm ultimately learns to create.

## Decision Tree Construction Details

*   The individual decision trees (`Hi`) within Gradient Boosting are built using the **same principles as standard regression decision trees**, involving multiple splits to reach leaf nodes.
*   Techniques like **pre-pruning** can be applied to control the complexity of these individual trees.
*   Various parameters for these trees can be tuned, similar to standalone decision trees.