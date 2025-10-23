## Statistical Analysis and Hypothesis Testing

### Introduction to Statistical Tests
*   Statistical analysis and hypothesis testing are crucial for data analysts and data scientists.
*   Various types of statistical tests exist:
    *   **Z-test**
    *   **T-test**
    *   **Chi-square test**
    *   **Anova test**
*   **Z-test** and **T-test** are specifically used for data dealing with **average data** (sample average, population average).
*   **Chi-square test** is used for **categorical data**.
*   **Anova test** is specifically for the **variance of the data**.
*   All these tests aim to estimate a population parameter using sample data.

### Z-Test Fundamentals
*   The Z-test uses a **Z-table** to find the **Z-score** and **p-value**.
*   **Conditions for using a Z-test**:
    1.  You must **know your population standard deviation**.
    2.  Your **sample size (n) should be greater than or equal to 30** (n >= 30).
*   Z-tests are generally applied for **average data** with respect to population data.

### Hypothesis Testing Steps (General)
The process of hypothesis testing typically involves these steps:
1.  **State the Null Hypothesis (H0) and Alternate Hypothesis (H1)**.
2.  **Define Significance Value (Alpha, α)**: This is calculated from the confidence interval (CI) as `α = 1 - CI`.
3.  **Draw a Decision Boundary**: This is based on the confidence interval and involves finding critical Z-score values from the Z-table.
4.  **Perform the Z-Test (Calculate the Test Statistic)**: Compute the Z-score based on your sample data.
    *   **Z-score formula for sample data**: `Z = (x̄ - μ) / (σ / √n)`.
        *   `x̄`: sample mean
        *   `μ`: population mean
        *   `σ`: population standard deviation
        *   `n`: sample size
    *   This formula accounts for the Central Limit Theorem, where the standard deviation for sample distribution becomes `σ / √n`.
5.  **Make a Conclusion**:
    *   **Reject Null Hypothesis**: If your calculated Z-score falls outside the decision boundary (i.e., in the rejection region).
    *   **Fail to Reject Null Hypothesis** (or "Accept Null Hypothesis"): If your calculated Z-score falls within the confidence interval (i.e., in the acceptance region).
    *   Alternatively, compare the **p-value** with the **significance value (α)**:
        *   If **p-value < α**: **Reject the Null Hypothesis**.
        *   If **p-value >= α**: **Fail to Reject the Null Hypothesis**.

### Example 1: City Resident Heights (Two-tailed test)
*   **Problem**: Average height of residents is 168 cm with a standard deviation of 3.9 cm. A doctor measures 36 individuals, finding an average height of 169.5 cm. Is there enough evidence to reject the null hypothesis at a 95% confidence interval?
*   **Given Data**:
    *   Population mean (μ) = 168 cm
    *   Population standard deviation (σ) = 3.9 cm (Note: Population standard deviation is known, so Z-test is applicable)
    *   Sample size (n) = 36 (Note: n >= 30, so Z-test is applicable)
    *   Sample mean (x̄) = 169.5 cm
    *   Confidence Interval (CI) = 95% or 0.95

*   **Step 1: State Null and Alternate Hypotheses**
    *   **Null Hypothesis (H0)**: The mean height is 168 cm (`μ = 168 cm`).
    *   **Alternate Hypothesis (H1)**: The mean height is **not equal to** 168 cm (`μ ≠ 168 cm`).
    *   This is a **two-tailed test** because H1 considers both greater than and less than the null value.

*   **Step 2: Calculate Significance Value (α)**
    *   `α = 1 - CI = 1 - 0.95 = 0.05`.

*   **Step 3: Draw Decision Boundary (Find Critical Z-scores)**
    *   For a 95% confidence interval in a two-tailed test, the remaining 5% (`α`) is split into two tails: `0.05 / 2 = 0.025` for each tail.
    *   To find the Z-score for the right tail, calculate the cumulative area from the left: `1 - 0.025 = 0.9750`.
    *   Looking up `0.9750` in the Z-table, the corresponding Z-score is **+1.96**.
    *   Due to symmetry, the left tail Z-score is **-1.96**.
    *   **Decision Rule**: Reject H0 if Z-calculated < -1.96 or Z-calculated > +1.96. Otherwise, fail to reject H0.

*   **Step 4: Perform the Z-Test (Calculate Z-score for sample data)**
    *   `Z = (x̄ - μ) / (σ / √n)`
    *   `Z = (169.5 - 168) / (3.9 / √36)`
    *   `Z = 1.5 / (3.9 / 6)`
    *   `Z = 1.5 / 0.65`
    *   **Z = 2.31**

*   **Step 5: Make a Conclusion (Z-score comparison)**
    *   Is `2.31 > 1.96`? **Yes**.
    *   Since the calculated Z-score (2.31) is greater than the critical Z-score (1.96), it falls in the rejection region.
    *   **Conclusion based on Z-score**: **Reject the Null Hypothesis**.

*   **Alternative Conclusion (P-value comparison)**
    *   Find the area under the curve for the calculated Z-score (2.31) from the Z-table. For Z=2.31, the cumulative area (from left) is `0.98956`.
    *   The area in the right tail is `1 - 0.98956 = 0.01044`.
    *   Since it's a two-tailed test, the p-value is the sum of both tail areas: `0.01044 + 0.01044 = 0.02088`.
    *   Compare p-value with α: Is `0.02088 < 0.05`? **Yes**.
    *   **Conclusion based on P-value**: **Reject the Null Hypothesis**.
    *   **Final Statement**: The average height is **not equal to 168 cm**. Based on the sample data, the average height seems to be **increasing** (since the Z-score was positive).

### Example 2: Bulb Warranty (One-tailed test)
*   **Problem**: A factory manufactures bulbs with an average warranty of 5 years and a standard deviation of 0.50 years. A worker believes bulbs malfunction in less than 5 years. He tests a sample of 40 bulbs and finds the average time to be 4.8 years.
*   **Given Data**:
    *   Population mean (μ) = 5 years
    *   Population standard deviation (σ) = 0.50 years (Known, so Z-test)
    *   Sample size (n) = 40 (n >= 30, so Z-test)
    *   Sample mean (x̄) = 4.8 years
    *   Confidence Interval (CI) = 98% (implied from alpha 0.02)

*   **Step 1: State Null and Alternate Hypotheses**
    *   **Null Hypothesis (H0)**: The mean warranty is 5 years (`μ = 5 years`).
    *   **Alternate Hypothesis (H1)**: The mean warranty is **less than** 5 years (`μ < 5 years`).
    *   This is a **one-tailed test** (specifically, a left-tailed test) because H1 only considers values less than the null value.

*   **Step 2: Calculate Significance Value (α)**
    *   CI = 98%, so `α = 1 - 0.98 = 0.02`.

*   **Step 3: Perform the Z-Test (Calculate Z-score for sample data)**
    *   `Z = (x̄ - μ) / (σ / √n)`
    *   `Z = (4.8 - 5) / (0.50 / √40)`
    *   `Z = -0.2 / (0.50 / 6.32)`
    *   `Z = -0.2 / 0.079`
    *   **Z = -2.53**

*   **Step 4: Make a Conclusion (P-value comparison)**
    *   Find the area under the curve for the calculated Z-score (-2.53) from the Z-table. For Z = -2.53, the area in the left tail is **0.00570**.
    *   This tail area is the p-value for a one-tailed test. So, **p-value = 0.00570**.
    *   Compare p-value with α: Is `0.00570 < 0.02`? **Yes**.
    *   **Conclusion based on P-value**: Since the p-value (0.00570) is **less than** the significance value (0.02), it falls in the rejection area.
    *   Wait, the source states the opposite conclusion ("false" it is greater). Let's re-evaluate.
        *   `0.00570` is indeed **less than** `0.02`.
        *   If p-value < alpha, **REJECT THE NULL HYPOTHESIS**.

    *   **Revised Conclusion (Standard Statistical Logic)**: Since `0.00570 < 0.02`, we **reject the null hypothesis**. This means there is enough evidence to support the worker's belief that the bulbs malfunction in less than 5 years.