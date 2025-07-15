### Student's T-Distribution

*   **Purpose of Student's T-Distribution**:
    *   In statistics, when performing analysis using a **z-score** or **z-test**, you need to know the **population standard deviation (sigma)**.
    *   However, the **population standard deviation is often difficult to obtain** or calculate because you don't have data for the entire population.
    *   The Student's t-distribution is used to **perform analysis when the population standard deviation is unknown**. This is a key scenario where you would use it.

*   **Formula Change from Z-score to T-distribution**:
    *   **Z-score formula** was: `(x bar - mu) / (population standard deviation / root n)`.
    *   **T-distribution formula** is: `(x bar - mu) / (sample standard deviation / root n)`.
    *   The main difference is that in the t-distribution formula, **sample standard deviation (s)** is used instead of population standard deviation.

*   **Key Parameter: Degree of Freedom (DOF)**:
    *   When using the t-distribution, there is a very important parameter called **degree of freedom**.
    *   Just as you use a z-table for z-stats, you use a **t-table** for student t-distribution to find the area under the curve.
    *   The **formula for Degree of Freedom (DOF) is `n - 1`**, where `n` is the sample size.
    *   **Concept of Degree of Freedom**: It represents the number of values in a calculation that are free to vary. For example, if you have 3 people and 3 chairs, the first person has 3 choices, the second has 2, but the third person has no choice left. So, only 2 people (3-1) had options, meaning the degree of freedom is 2.
    *   **Importance**: Degree of freedom is crucial when doing any analysis with the help of a **t-test** or **t-stats**.

*   **T-Table Usage**:
    *   The t-table has different axes:
        *   One axis shows whether it's a **one-tail or two-tail test**.
        *   It also shows values based on the **confidence interval**.
        *   The **degree of freedom (DOF) is shown on the row-wise axis**.
    *   You use the degree of freedom along with other parameters to find different values and the area under the curve in the t-table.
	
