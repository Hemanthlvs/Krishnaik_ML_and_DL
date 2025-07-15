# P-Values in Hypothesis Testing

## What is a P-Value?
*   A **P-value** is a number calculated from a statistical test.
*   It tells you **how likely** you are to have observed a particular set of data if the **null hypothesis were true**.
*   P-values are very important in **inferential statistics** because they help us draw conclusions about population data.
*   They are used in **hypothesis testing** to help decide whether to reject the null hypothesis.

## P-Value Explained with an Example (Spacebar)
*   Imagine a spacebar on a keyboard. Most people touch the center region.
*   If a data point (a touch) has a **P-value of 0.2**, it means that out of 100 touches, about **20 times** you touch in that specific region.
*   If another region has a **P-value of 0.8**, it means out of 100 touches, about **80 times** you touch in that specific region.
*   In simple terms, a P-value is the **probability of a specific outcome** in a specific region.

## P-Value in Hypothesis Testing Steps
*   In hypothesis testing, the first step is to write the **null hypothesis** and **alternate hypothesis**.
*   Then, you perform a **statistical analysis** or **statistical test**.
*   The **outcome** of this statistical test is the **P-value**.

## Hypothesis Testing Example: Fair Coin
Let's consider an example of testing if a coin is fair by tossing it 100 times.

### a. Defining Hypotheses
*   **Null Hypothesis (H0)**: The coin is fair. (This assumes the probability of heads is 0.5 and tails is 0.5).
*   **Alternative Hypothesis (H1)**: The coin is not fair. (For example, if heads come up 70% of the time, you might suspect it's not fair).

### b. The Experiment and Distribution
*   If a coin is fair and tossed 100 times, you'd expect around **50 heads** (the mean).
*   The number of heads obtained (e.g., 50, 60, 70) can be represented on a distribution curve.

### c. Confidence Interval and Significance Value
*   We define a **confidence interval** to determine if the coin is fair. For instance, if the number of heads is between **30 and 70**, we might consider the coin fair.
*   The **significance value**, denoted by **alpha (α)**, is a crucial parameter.
*   Alpha is typically set by **domain experts** based on the problem. For example, alpha might be 0.05.
*   If alpha is 0.05, the **confidence interval** represents **1 - 0.05 = 0.95 (95%)** of the area under the curve.
*   The remaining 0.05 (or 5%) is split into two "rejection areas" on either end of the distribution, each being 0.025 (2.5%).
*   If your experimental outcome (like 70 heads) falls within the confidence interval (e.g., 30-70), you **fail to reject the null hypothesis** (coin is fair).
*   If it falls outside this interval, in the "rejection area," you **reject the null hypothesis** (coin is not fair).

## Decision Making with P-Value and Significance Value
*   The P-value is calculated from your statistical experiment using specific formulas (e.g., z-test, t-test).
*   **The key rule for decision making is**:
    *   **If P-value < Significance Value (alpha)**: You **REJECT the null hypothesis**.
        *   This means your observed outcome is in the **extreme "rejection area"** (either too low or too high), indicating it's unlikely to happen if the null hypothesis were true.
        *   It suggests the outcome does not fit within the defined confidence interval.
    *   **If P-value >= Significance Value (alpha)**: You **FAIL TO REJECT the null hypothesis**.
        *   This means your observed outcome falls within the **confidence interval**.
        *   Failing to reject the null hypothesis essentially means you **accept the null hypothesis** for that experiment.

This process helps to make conclusions about the population data based on statistical evidence.