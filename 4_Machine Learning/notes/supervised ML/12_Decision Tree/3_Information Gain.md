# Information Gain (IG)

## 1. What is Information Gain (IG)?

*   **Information Gain (IG)** is what we use to **determine which feature we should select to start the split** in a Decision Tree.
*   Imagine you have features like `f1`, `f2`, `f3`. You need to decide whether to split your data using `f1` or `f2` first. Information Gain helps you make that decision.

## 2. Information Gain Formula

The formula for Information Gain is:

**`Gain(S, Feature)` = `Entropy(S)` - `Summation (v ∈ Values) of ((|S_v| / |S|) * Entropy(S_v))`**

Let's break down each term, you know:

*   **`Entropy(S)`**: This is the **entropy of the root node** (or the current parent node before the split).
*   **`v ∈ Values`**: This means we're summing up for all the different categories or values of the feature you're considering for the split.
*   **`|S_v|`**: This is the **number of samples** in the subset `S_v` that belong to a specific category `v` after the split.
*   **`|S|`**: This is the **total number of samples** in the current parent node (before the split).
*   **`Entropy(S_v)`**: This is the **entropy of the subset `S_v`**, which corresponds to a specific category `v` of the feature.

## 3. Entropy Formula (Binary Classification)

Before calculating Information Gain, you need to know how to calculate Entropy. For binary classification (like 'yes'/'no' or 'plus'/'minus'), the formula is:

**`H(S) = -P(+) * log2(P(+)) - P(-) * log2(P(-))`**

*   `P(+)`: Probability of the 'positive' class (e.g., 'yes') in the dataset.
*   `P(-)`: Probability of the 'negative' class (e.g., 'no') in the dataset.
*   `log2`: Logarithm with base 2.

## 4. Example Walkthrough: Calculating Gain for Feature F1

Suppose we have an initial dataset `S` with **9 'yes'** and **5 'no'** instances, making a total of **14 instances**.

We are considering splitting this dataset using **Feature F1**. After splitting with F1, we get two categories:
*   **Category C1**: Has **6 'yes'** and **2 'no'** instances (total 8).
*   **Category C2**: Has **3 'yes'** and **3 'no'** instances (total 6).

Now, let's calculate the Information Gain for this split:

### Step 1: Calculate Entropy of the Root Node `H(S)`

*   Here, `P(+) = 9/14` and `P(-) = 5/14`.
*   `H(S) = -(9/14) * log2(9/14) - (5/14) * log2(5/14)`.
*   After calculation, `H(S)` is approximately **0.94**.

### Step 2: Calculate Entropy of each Category after Split

#### a. Entropy of Category C1 (`H(C1)`)
*   For C1, we have 6 'yes' and 2 'no' (total 8).
*   `P(+) = 6/8` and `P(-) = 2/8`.
*   `H(C1) = -(6/8) * log2(6/8) - (2/8) * log2(2/8)`.
*   After calculation, `H(C1)` is approximately **0.81**.

#### b. Entropy of Category C2 (`H(C2)`)
*   For C2, we have 3 'yes' and 3 'no' (total 6).
*   Since it's an **impure split** (equal number of 'yes' and 'no'), its entropy will be the maximum, which is **1.0**.
    *   `H(C2) = -(3/6) * log2(3/6) - (3/6) * log2(3/6) = 1.0`.

### Step 3: Calculate Information Gain for F1 (`Gain(S, F1)`)

Now, we'll put all these values into the Information Gain formula.

*   `Gain(S, F1) = H(S) - [ (|C1| / |S|) * H(C1) + (|C2| / |S|) * H(C2) ]`
*   Here, `|C1| = 8` (total instances in C1) and `|C2| = 6` (total instances in C2).
*   `Gain(S, F1) = 0.94 - [ (8/14) * 0.81 + (6/14) * 1.0 ]`
*   After computing this, the `Gain(S, F1)` is approximately **0.049**. This is your total gain for the F1 split.

## 5. Comparing Splits and Making a Decision

*   You'll repeat the whole process to calculate Information Gain for other features, say **Feature F2**.
*   Let's say after computing, you find that `Gain(S, F2)` is, for example, `0.07`, which is **greater than** `Gain(S, F1)` (which was `0.049`).
*   **The feature with the higher Information Gain is the best feature to start splitting with**. So, in this hypothetical case, you would start your Decision Tree split from Feature F2.
*   Decision trees internally check these conditions (using entropy or Gini impurity) to find the best feature for splitting.