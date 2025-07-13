# Power Law Distribution

## Introduction
*   Power Law Distribution is a **new type of statistical distribution** that is different from Gaussian (Normal) distribution.
*   It describes how certain datasets behave and the kind of information they convey.

## Definition
*   In statistics, a **power law** describes a functional relationship between two quantities.
*   The key characteristic is that a **relative change in one quantity leads to a proportional relative change in the other**, regardless of their initial size.
*   Essentially, **one quantity varies as a power of another**.
*   The definition can be complex, so it's best understood through examples.

## Visual Representation (The Curve)
*   Unlike a normal distribution (which has a bell-shaped curve) or a log-normal distribution, a power law distribution has a specific curve shape.
*   This curve is characterized by a **"long tail" to the right**, and **few items dominating to the left**.

## The 80/20 Rule (Pareto Principle)
*   Power law distribution is strongly connected to and often known as the **80/20 rule**.
*   This rule illustrates the relationship between two variables: **approximately 20% of one variable accounts for 80% of the other**.
*   For instance, 20% of an entire area might cover one aspect, while the remaining 80% covers the rest.

### Examples of the 80/20 Rule in Action:
*   **Indian Premier League (IPL):** 20% of the teams are responsible for winning 80% of the matches.
*   **Wealth Distribution:** 80% of the wealth is distributed among 20% of the total population.
*   **Crude Oil:** 80% of the total crude oil is held by 20% of the nations.
*   **Word Frequencies:** In most languages, the frequencies of words follow an 80/20 rule.
*   **IT Companies (Software Defects):** 20% of major defects are responsible for (or fix) 80% of upcoming defects in a software product.

## Data Transformations
*   Many machine learning algorithms perform best when data follows a **normal distribution**.
*   **Log Transformation:** If data is log-normally distributed, applying a logarithmic transformation can convert it into a normal distribution.
*   **Box-Cox Transform:** If you have **power-law distributed data** (which looks like the specific curve mentioned above), you **can convert it into a normal distribution**.
    *   This transformation is called the **Box-Cox transform**.
    *   It is similar to other transformation techniques like log transformation or standardization.
*   **Pareto Distribution:** Any data that follows a power law distribution is also specifically called **Pareto distribution**. It also follows the 80/20 rule.
*   To **check if data is normally distributed** after transformation, you can use a **Q-Q plot**.