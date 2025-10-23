# **ANOVA (Analysis of Variance)**

*   **What is ANOVA?**
    *   ANOVA is a **super important statistical method**.
    *   It is used to **compare the means of two or more groups**.
	*   **ANOVA (Analysis of Variance)** is used to compare the means of **two or more groups**.
	*   It does this by considering the **variance** within and between these groups, often referred to as "partitioning of variance".
	*   The main goal is to determine if there are significant differences between the group means.

*   **Why is ANOVA used?**
    *   Previously, for comparing the means of only two groups, tests like the Z-test or T-test were used.
    *   **ANOVA is specifically useful when you want to compare the means of *three or more* groups**.

*   **Important Components of ANOVA**
    *   When working with ANOVA, there are two very important components:
        1.  **Factors**
        2.  **Levels**
		
    *   **Factor**: A general category or independent variable being studied.
        *   Factors can be independent or dependent.
    *   **Levels**: These are the different variations or categories *within* a specific factor.

*   **Examples to Illustrate Factors and Levels:**

    *   **Example 1: Medicine and Dosage**
        *   **Factor**: Medicine
        *   **Levels**: Different dosages of the medicine, such as 5 mg, 10 mg, or 15 mg. These are the specific variations of the medicine factor.

    *   **Example 2: Mode of Payment**
        *   **Factor**: Mode of Payment
        *   **Levels**: Different options for payment, such as Google Pay, PhonePe, IMPS, NFT, or demand draft. These are the specific ways people can pay within the mode of payment factor.

# ANOVA Assumptions

There are typically three to four main assumptions for ANOVA:

*   **1. Normality of Sampling Distribution of Means**
    *   This means that the **distribution of sample means should be normally distributed**.
    *   When you hear "sampling distribution of mean" and "normality," you should think of the **Central Limit Theorem**.
    *   "Normally distributed" means it should follow a **Gaussian distribution**.

*   **2. Absence of Outliers**
    *   **Outliers in your dataset need to be removed**.
    *   You can remove outliers using various techniques, such as **box plots** or the **interquartile range**.

*   **3. Homogeneity of Variance**
    *   "Homogeneity" means **homogeneous or equal**.
    *   This assumption states that the **population variance across different levels of each independent variable (or factor) should be the same (or equal)**.
    *   For example, if you have three levels in an independent variable, their population variances (e.g., sigma one squared, sigma two squared, sigma three squared) should be equal.
    *   An independent variable is one that does not impact other variables.

*   **4. Independent and Random Samples**
    *   The samples taken **must be independent**.
    *   The samples must also be **randomly selected**.

# ANOVA Types:

## 1. One-Way ANOVA
*   **Definition:** Involves **one factor** with **at least two independent levels**.
*   **Levels are independent:** This means there is no relationship or dependency between the different levels of the factor.
*   **Example: Testing a New Medication for Headache**
    *   **Goal:** A doctor wants to test a new medication to decrease headaches.
    *   **Participants:** Participants are split into three groups (conditions).
    *   **Factor:** The **medication** itself is the factor.
    *   **Levels:** The different **dosages** of the medication are the levels (e.g., 10mg, 20mg, 30mg).
    *   **Independence:** Each dosage (10mg, 20mg, 30mg) is independent of the others; they are distinct medications or conditions.
    *   **Measurement:** Participants rate their headache level on a scale of 1 to 10 after taking the medication.
    *   **Outcome:** Different participants in different dosage groups might give varying ratings based on the medicine's effect.

## 2. Repeated Measures ANOVA
*   **Definition:** Involves **one factor** with **at least two dependent levels**.
*   **Levels are dependent:** This means the levels are related or linked, often because the **same participants** are involved in multiple conditions or measurements over time.
*   **Example: Running Performance**
    *   **Factor:** **Running** is considered the factor.
    *   **Levels:** Measurements taken on **Day 1, Day 2, and Day 3** for the same group of people.
    *   **Dependence:** The levels are dependent because the **same person** runs on Day 1, Day 2, and Day 3. Their performance on one day might influence or be related to their performance on another day.
    *   **Outcome:** The same person might run different distances (e.g., 8km, 5km, 4km) on different days.

## 3. Factorial ANOVA
*   **Definition:** Involves **two or more factors**, where **each factor has at least two levels**.
*   **Level Dependence:** The levels in Factorial ANOVA can be **independent or dependent**.
*   **Example: Running Performance and Gender**
    *   This type combines aspects of the previous examples.
    *   **Factor 1: Running**
        *   **Levels:** Day 1, Day 2, Day 3 (these levels are **dependent** because the same person runs on multiple days).
    *   **Factor 2: Gender**
        *   **Levels:** Male and Female (these levels are **independent** because male and female are separate entities).
    *   **Application:** When you have a dataset with multiple factors like running performance over days and gender, you would use a Factorial ANOVA.

# ANOVA Hypothesis Testing:

## Steps to Perform Hypothesis Testing in ANOVA

### **Step 1: Define Null (H0) and Alternate (H1) Hypotheses**
*   **Null Hypothesis (H0)**: States that the means of all groups are equal.
    *   Example: Mean₁ = Mean₂ = Mean₃ ... = Meanₖ.
    *   For the headache medication example: Mean(15mg) = Mean(30mg) = Mean(45mg).
*   **Alternate Hypothesis (H1)**: States that at least one of the group means is not equal to the others.
    *   It's important to note that H1 does *not* state that all means are unequal (e.g., Mean₁ ≠ Mean₂ ≠ Mean₃). It only implies that *at least one* difference exists.
    *   For the headache medication example: At least one sample mean is not equal, or not all means are equal.

### **Key Concept: F-test Statistic**
*   The statistical test used in ANOVA is the **F-test**.
*   **F-test Formula**: F = (Variance between samples) / (Variance within samples).
*   **Variance Between Samples**: This refers to the differences in variance *among* the different groups or samples. It measures how much the means of the different groups vary from each other.
*   **Variance Within Samples**: This refers to the differences in variance *inside* each individual sample. It measures the spread of data points around their own group's mean.

### **Example Problem: Headache Medication Study**
*   **Problem Description**: Doctors want to test a new medication to reduce headaches.
    *   **Participants**: Split into three groups receiving different dosages: 15mg, 30mg, and 45mg.
    *   **Data**: Patients rate headache severity from 1 (headache present) to 10 (headache gone).
    *   **Factor**: Medication dosage.
    *   **Levels**: 15mg, 30mg, 45mg.
    *   **Sample Size**: 7 people in each group, totaling 21 participants.
*   **Significance Level (Alpha)**: Given as **0.05**. This defines the confidence interval (0.95).

### **Step 2: Calculate Degrees of Freedom (DF)**
*   **Total Sample Size (N)**: Total number of participants in all groups. For the example, N = 21 (7 people/group * 3 groups).
*   **Number of Categories (a)**: Number of different groups. For the example, a = 3 (15mg, 30mg, 45mg).
*   **Degrees of Freedom Between Samples (DF1)**: `a - 1`.
    *   For the example: DF1 = 3 - 1 = **2**.
*   **Degrees of Freedom Within Samples (DF2)**: `N - a`.
    *   For the example: DF2 = 21 - 3 = **18**.
*   **Degrees of Freedom Total**: `N - 1`.
    *   For the example: 21 - 1 = 20 (Note: DF between + DF within = DF total; 2 + 18 = 20).
*   These DF values (DF1 = 2, DF2 = 18) are crucial for finding the critical value from the F-table.

### **Step 3: Construct Decision Boundary (Critical Value)**
*   The F-test distribution is typically **right-skewed**.
*   **Rejection Area**: The area where the null hypothesis is rejected (e.g., 0.05 alpha region).
*   **Acceptance Area**: The area where we fail to reject the null hypothesis (e.g., 0.95 confidence interval region).
*   **Finding the Critical Value**: You use the F-table with your alpha (0.05), DF1 (2), and DF2 (18).
    *   For the example, the critical value from the F-table is **3.5546**.
*   **Decision Rule**: If the calculated F-value (from Step 5) is **greater than** the critical value (3.5546), then we **reject the null hypothesis**.

### **Step 4: Calculate F-Test Statistics (The most complex part)**
This involves several sub-calculations:
1.  **Calculate Sum of Squares (SS)**: This helps find the variance.
    *   **SS Between Samples**: Measures the variance *between* the group means.
        *   Formula involves summing the squares of each group's total, divided by its sample size, then subtracting the square of the grand total divided by the total sample size.
		*	SS_Between = (T1² / n1) + (T2² / n2) + (T3² / n3) - (G² / N)
        *   For the example, group totals were 57 (15mg), 47 (30mg), 21 (45mg).
        *   SS Between calculated as **98.67**.
    *   **SS Within Samples**: Measures the variance *within* each group.
        *   Formula involves summing the squares of *each individual data point* and subtracting the sum of (group total)² / group size.
		*	SS_Within = Sum of (each value squared) - [(T1² / n1) + (T2² / n2) + (T3² / n3)]
        *   For the example, Sum of Y² was 853.
        *   SS Within calculated as **10.29**.
2.  **Calculate Mean Squares (MS)**: This is variance.
    *   **MS Between**: SS Between / DF Between.
        *   For the example: 98.67 / 2 = **49.34**. This represents the "variance between samples" in the F-test formula.
    *   **MS Within**: SS Within / DF Within.
        *   For the example: 10.29 / 18 = **0.57** (Source shows 0.54, but 10.29/18 is approx 0.57). This represents the "variance within samples".
3.  **Calculate F-Value**: MS Between / MS Within.
    *   For the example: 49.34 / 0.54 (using the source's 0.54) = **86.56**. This is your calculated F-test value.

### **Step 5: Make a Decision & Conclusion**
*   **Compare F-calculated with Critical Value**:
    *   Calculated F-value = **86.56**.
    *   Critical F-value = **3.5546**.
*   **Decision**: Since 86.56 is **greater than** 3.5546, we **reject the null hypothesis (H0)**.
*   **Conclusion**: There *are* differences between the three medication conditions. This means that not all the means are equal, or at least one of them is not equal.