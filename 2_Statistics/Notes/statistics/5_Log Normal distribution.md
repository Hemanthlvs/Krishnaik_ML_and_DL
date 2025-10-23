# Log-Normal Distribution

## What is a Log-Normal Distribution?

*   In probability theory, a **log-normal distribution** is a **continuous probability distribution** for a random variable 'X'.
*   Its key characteristic is that the **logarithm of 'X' (specifically, the natural logarithm of X)** is normally distributed.
*   So, if a random variable **X is log-normally distributed**, then a new variable **Y = log(X)** (natural log) will have a **normal distribution**.
*   **Natural log** is denoted as log to the base 'e' (ln).

## Characteristics

*   A log-normal distribution is a **right-skewed distribution**. This means the "tail" of the curve is elongated towards the right side.
*   Even with varying standard deviations, the right part of the curve remains skewed.

## Transformations

*   **From Log-Normal to Normal:** If you have a random variable **X that is log-normally distributed**, applying the **natural logarithm (log(X) or ln(X))** to each value will transform it into a **normally (or Gaussian) distributed** variable 'Y'.
*   **From Normal to Log-Normal:** Conversely, if you have a random variable **Y that is normally distributed**, applying the **exponential function (e^Y or exp(Y))** to each value will transform it into a **log-normally distributed** variable 'X'.
    *   This is the inverse operation: if Y = log(X), then X = e^Y.

## How to Check for Log-Normal Distribution

*   To check if a dataset follows a log-normal distribution, you can use a **Q-q plot** (Quantile-Quantile plot). This technique helps determine if a distribution is normal (after applying the log transformation).

## Examples of Data Following Log-Normal Distribution

Several real-world datasets often follow a log-normal distribution due to their inherent right-skewness:

*   **Wealth Distribution:** The distribution of wealth across the world. A small number of people hold most of the wealth (e.g., the richest 1%) while many people are in the salaried class, creating a right-skewed pattern.
*   **Length of Comments in Discussion Forums:** Many people write short comments, a medium number write average-sized comments, and very few write very long comments.
*   **Length of Chess Games:** The duration of chess games.
*   **Dwell Time on Online Articles:** The amount of time people spend reading online articles like jokes or news.