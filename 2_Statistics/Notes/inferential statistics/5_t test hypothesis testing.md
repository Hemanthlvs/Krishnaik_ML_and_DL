**T-Test: A One-Sample Case Study**

*   **When to use Z-Test vs. T-Test**
    *   **Z-Test**: Use when you have the **population standard deviation** and your sample size (`n`) is **greater than or equal to 30**.
    *   **T-Test**: Use when the **population standard deviation is not given**.

*   **Case Study Example: Medication's Effect on IQ**
    *   **Objective**: To determine if a new medication affects intelligence.
    *   **Initial Population Information**: The average IQ is 100.
    *   **Sample Data (after medication)**:
        *   **Sample size (`n`)**: 30 participants.
        *   **Sample mean (`x̄`)**: 140.
        *   **Sample standard deviation (`s`)**: 20.
    *   **Confidence Interval (CI)**: 95%.
    *   **Alpha Value (`α`)**: 0.05 (calculated as 1 - CI, so 1 - 0.95 = 0.05).
    *   **Test Type**: This is a **two-tailed test** because the researchers are investigating if the medication has a positive *or* negative effect (i.e., whether IQ increases or decreases).

*   **Steps for Performing a One-Sample T-Test**

    1.  **Write Down All Parameters**
        *   Population Mean (μ): 100 (initial average IQ).
        *   Sample Size (n): 30.
        *   Sample Mean (x̄): 140.
        *   Sample Standard Deviation (s): 20.
        *   Confidence Interval (CI): 95%.
        *   Alpha Value (α): 0.05.

    2.  **Define Null and Alternate Hypotheses**
        *   **Null Hypothesis**: The basic assumption that the medication has no effect. The population mean IQ remains 100.
            *   H0: μ = 100
        *   **Alternate Hypothesis**: The medication *does* affect intelligence. The population mean IQ is not equal to 100.
            *   H1: μ ≠ 100

    3.  **Compute the Degree of Freedom (df)**
        *   For a one-sample t-test, df = `n - 1`.
        *   In this case, df = 30 - 1 = **29**.

    4.  **Establish the Decision Rule (Find Critical T-Values)**
        *   **Purpose**: To determine the boundaries for rejecting the null hypothesis.
        *   Using the t-table:
            *   Locate the row for **Degrees of Freedom (df) = 29**.
            *   Find the column for a **two-tailed test** with **α = 0.05**.
            *   The critical t-value found is **2.045**.
        *   **Rejection Regions**: Since it's a two-tailed test, the critical values are **±2.045**.
        *   **Decision Rule**: If the calculated t-test statistic is **less than -2.045** or **greater than 2.045**, then **reject the null hypothesis**. The areas outside these values are the "rejection areas".

    5.  **Calculate the Test Statistic (t-value)**
        *   **Formula**: `t = (x̄ - μ) / (s / √n)`.
        *   **Substitution**: `t = (140 - 100) / (20 / √30)`.
        *   **Calculated t-value**: **10.96**.

    6.  **Make a Conclusion**
        *   **Comparison**: The calculated t-value (10.96) is compared to the critical t-values (±2.045).
        *   **Decision**: Since 10.96 is **greater than 2.045**, it **falls into the rejection area**.
        *   Therefore, we **reject the null hypothesis**.
        *   **Final Analysis**:
            *   Rejecting the null hypothesis means the medication **has affected intelligence**.
            *   Because the t-test value (10.96) is positive and the sample mean (140) is higher than the population mean (100), the medication is concluded to have **increased intelligence**.