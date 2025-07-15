# **Confidence Intervals and Margin of Error**

## **Introduction to Confidence Intervals (CI) and Margin of Error (ME)**
*   A **confidence interval** defines a range within which a population parameter (like the population mean) is likely to fall.
*   It's an important concept in statistics, building on previous discussions of z-tests and t-tests.
*   For a **two-tailed test** with a 95% confidence interval, the central region is 95%, with 2.5% in each tail.

## **The Problem with Point Estimates**
*   A **point estimate** (like a sample mean, `x bar`) is used to estimate the population mean.
*   For example, if a sample mean (`x bar`) is 2.5 and the population mean is 3, the sample mean might be less than, greater than, or approximately equal to the population mean.
*   The problem with using only a point estimate is that different samples can give different point estimates, leading to variations.
*   To address this, we define a **range** using a confidence interval, for example, saying an estimate lies between 2 and 4.

## **Formula for Confidence Interval**
*   The general formula for calculating a confidence interval is:
    **`Point Estimate ± Margin of Error`**
*   **Point estimate** is typically the sample mean (`x bar`).
*   The reason for "plus or minus" is that the point estimate can be slightly less than, more than, or approximately equal to the population mean.

## **Calculating Margin of Error (ME)**
*   The formula for Margin of Error depends on whether it's a Z-test or a T-test.
*   **For a Z-test**:
    `Margin of Error = z_alpha/2 * (sigma / sqrt(n))`
    *   `z_alpha/2`: This value comes from the Z-table and corresponds to the area under the curve.
    *   `sigma`: Population standard deviation.
    *   `n`: Sample size (root n).
*   **For a T-test**:
    `Margin of Error = T_alpha/2 * (s / sqrt(n))`.
    *   `T_alpha/2`: This value comes from the T-table and requires calculating the degree of freedom.

## **Example: CAT Exam Scores (Z-test)**
*   **Problem**: Given a standard deviation of 100 for the verbal section of the CAT exam, a sample of 30 test-takers has a mean of 520. Construct a **95% confidence interval** about the mean.
*   **Identify the test**: Since the population standard deviation (100) is known, a **Z-test** is used.
*   **Formula to use**: `x bar ± z_alpha/2 * (sigma / sqrt(n))`.
*   **Steps to calculate**:
    1.  **Find `z_alpha/2`**:
        *   For a 95% confidence interval, `alpha` (significance level) is 0.05.
        *   `alpha/2` is 0.025.
        *   We are looking for `z_0.025` which corresponds to the area `1 - 0.025 = 0.9750` in the Z-table.
        *   The `z` value for an area of 0.9750 is **1.96**. This means `z_alpha/2 = 1.96` (and -1.96 for the lower tail).
    2.  **Identify given values**:
        *   Sample mean (`x bar`) = 520.
        *   Population standard deviation (`sigma`) = 100.
        *   Sample size (`n`) = 25 (Note: The source initially states '30 test takers' but then uses 'root 25' in calculations. Assuming 25 is the value used for calculation here).
    3.  **Calculate the Margin of Error part**:
        `1.96 * (100 / sqrt(25))`
        `1.96 * (100 / 5)`
        `1.96 * 20 = 39.2`.
    4.  **Calculate the Lower Confidence Interval (LCI)**:
        `LCI = x bar - Margin of Error`
        `LCI = 520 - (1.96 * 100 / sqrt(25))`
        `LCI = 520 - 39.2 = **480.8**`.
    5.  **Calculate the Higher Confidence Interval (HCI)**:
        `HCI = x bar + Margin of Error`
        `HCI = 520 + (1.96 * 100 / sqrt(25))`
        `HCI = 520 + 39.2 = **559.2**`.

## **Interpretation and Hypothesis Testing**
*   The **confidence interval** for the CAT exam scores is **between 480.8 and 559.2**.
*   This means, "I am **95% confident** that the average CAT exam score will be lying between 480.8 and 559.2".
*   **In hypothesis testing**:
    *   If a p-value (from a z-test) lies within this confidence interval region, we **accept the null hypothesis**.
    *   If the p-value falls outside this range (in the extreme ends), we **reject the null hypothesis**.

## **Conclusion**
*   Confidence intervals help in determining a **range or interval** for estimating an unknown population parameter.
*   The calculation involves the point estimate and the margin of error.