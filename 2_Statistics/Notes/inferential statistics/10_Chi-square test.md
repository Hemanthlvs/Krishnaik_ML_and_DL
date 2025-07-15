# Chi-Square Test

## Introduction
*   The Chi-Square test is a **statistical test**.
*   It's an amazing test technique specifically for **categorical variables** and is used for **hypothesis testing**.
*   It is a **non-parametric test**.
*   This test makes claims about **population proportion**.
*   It is also known as the **goodness-of-fit test**.
*   It requires the use of a **Chi-Square table**.

## Types of Data
*   The Chi-Square test is performed on **categorical data**.
*   Categorical data includes two types: **ordinal and nominal data**.

## Chi-Square Test for Goodness of Fit
*   This is a specific type of Chi-Square test.
*   Its purpose is to see if the **sample information "fits" or supports a given theory** about the population.
*   It helps determine if the observed sample data is a **"goodness of fit" for the theory**.

## Key Concepts
*   **Theory Categorical Distribution**: This is the initial theory or hypothesis about the population.
    *   *Example*: One-third of people like yellow bikes, one-third like red, one-third like orange.
    *   *Example*: 12% of people in the population are left-handed.
*   **Observed Categorical Distribution**: This is the data collected from a sample.
    *   *Example*: In a sample, 22 people liked yellow bikes, 17 liked red, and 59 liked orange.
    *   *Example*: In a class of 75 students, 11 are left-handed and 64 are right-handed.
*   The Chi-Square test uses these two distributions (theory and observed) to perform the goodness of fit.

## Examples Explained

### Example 1: Bike Colors
*   **Population**: Male individuals who like different colored bikes.
*   **Theory**:
    *   1/3 like Yellow bikes.
    *   1/3 like Red bikes.
    *   1/3 like Orange bikes.
*   **Observed Sample Data**:
    *   22 people liked Yellow bikes.
    *   17 people liked Red bikes.
    *   59 people liked Orange bikes.
*   **Goal**: Use the Chi-Square test to see if the sample data (observed) supports the theory.

### Example 2: Left-Handed Students
*   **Total Students**: 75 students in a science class.
*   **Theory (about the population)**: 12% of people are left-handed.
*   **Observed Sample Data**:
    *   11 students are left-handed.
    *   64 students are right-handed (75 - 11 = 64).
*   **Calculating Expected Values (based on theory)**:
    *   For left-handed: 12% of 75 = (12/100) * 75 = **9 people**.
    *   For right-handed: 75 - 9 = **66 people**.
*   **Goal**: Compare the observed values (11 left-handed, 64 right-handed) with the expected values (9 left-handed, 66 right-handed) to see if the class fits the theory using the Chi-Square test.

## What the Test Compares
*   The Chi-Square test compares two categorical variables.
*   These variables are specifically the **theoretical categorical distribution** and the **observed categorical distribution**.

### **Chi-Square Test for Population Weight Differences**

#### **Problem Scenario**
*   **2010 Census Data (Expected Data)**:
    *   Less than 50kg: 20%
    *   50 to 75kg: 30%
    *   Greater than 75kg: 50%
*   **2020 Sample Data (Observed Data)**:
    *   A sample of **500 individuals** was taken.
    *   Less than 50kg: 140 individuals
    *   50 to 75kg: 160 individuals
    *   Greater than 75kg: 200 individuals
    *   The total observed sample sums to 500.
*   **Objective**: Determine if there is a **population difference** in weights between 2010 and 2020.
*   **Significance Level (alpha)**: 0.05.
*   The Chi-Square test is used because there are **three categories** of weights.

#### **Data Identification**
*   **2010 data** is considered the **Expected Data** (original population data).
*   **2020 sample data** is considered the **Observed Data**.

#### **Calculating Expected Data for 2020 Sample**
*   The expected data for 2020 is calculated based on the 2010 percentages and the 2020 sample size (N=500).
    *   **Less than 50kg**: 20% of 500 = **0.2 * 500 = 100**.
    *   **50 to 75kg**: 30% of 500 = **0.3 * 500 = 150**.
    *   **Greater than 75kg**: 50% of 500 = **0.5 * 500 = 250**.
*   These are the **expected counts** for the 2020 sample if the weight distribution had not changed from 2010.

#### **Hypothesis Formulation**
*   **Null Hypothesis (H0)**: The data **meets the expectation**; meaning, there is no significant difference in population weights between 2010 and 2020.
*   **Alternate Hypothesis (H1)**: The data **does not meet the expectation**; meaning, there is a significant difference in population weights between 2010 and 2020.

#### **Significance Level and Degrees of Freedom (DF)**
*   **Significance Level (alpha)**: **0.05**.
*   **Confidence Interval**: 95% (derived from alpha).
*   **Degrees of Freedom (DF)**:
    *   Formula: **DF = Number of Categories - 1**.
    *   In this case, there are 3 categories (less than 50kg, 50-75kg, greater than 75kg).
    *   DF = 3 - 1 = **2**.

#### **Decision Boundary / Critical Value**
*   Unlike Z-test or T-test, the Chi-Square test **does not have a symmetrical distribution**. The distribution is typically skewed.
*   A **critical value** is needed to define the **rejection area** and **acceptance area**.
*   If the calculated test statistic is **greater than the critical value**, the null hypothesis (H0) is rejected.
*   If the calculated test statistic is **less than or equal to the critical value**, the null hypothesis (H0) is accepted (or failed to reject).
*   **Finding the Critical Value**:
    *   Use the Chi-Square table.
    *   Look up the table using the **significance level (0.05)** and the **degrees of freedom (2)**.
    *   The critical value found is **5.991**.

#### **Calculating Chi-Square Test Statistics**
*   The formula for the Chi-Square test statistic is:
    *   **Chi-Square = Σ [(Observed - Expected)² / Expected]**.
*   **Observed (O)** values are: 140, 160, 200.
*   **Expected (E)** values are: 100, 150, 250.
*   **Calculation steps**:
    *   For <50kg: (140 - 100)² / 100 = 40² / 100 = 1600 / 100 = **16**.
    *   For 50-75kg: (160 - 150)² / 150 = 10² / 150 = 100 / 150 = **0.66** (approximately).
    *   For >75kg: (200 - 250)² / 250 = (-50)² / 250 = 2500 / 250 = **10**.
*   **Summation**: 16 + 0.66 + 10 = **26.66**.
*   The calculated Chi-Square test statistic is **26.66**.

#### **Conclusion**
*   **Compare the calculated Chi-Square value to the critical value**.
*   Calculated Chi-Square = **26.66**.
*   Critical Value = **5.991**.
*   Since **26.66 > 5.991**, the calculated value falls into the **rejection area**.
*   **Decision**: **Reject the Null Hypothesis (H0)**.
*   **Final Conclusion**: The **weights of the 2020 population are different** than those expected from the 2010 population. This means there has been a significant change in the population differences of weights in the last ten years.