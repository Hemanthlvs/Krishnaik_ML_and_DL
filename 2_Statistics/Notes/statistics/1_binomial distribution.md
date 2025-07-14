# Binomial Distribution

### Introduction to Binomial Distribution
*   The binomial distribution is a **discrete probability distribution**.
*   It describes the **number of successes** in a sequence of `n` independent experiments.
*   Each experiment (or "trial") in a binomial distribution has a **binary outcome** (yes/no, success/failure, 0/1).
*   A single success/failure experiment is called a **Bernoulli trial** or Bernoulli experiment.
*   A sequence of outcomes from Bernoulli trials is called a **Bernoulli process**.
*   If the number of trials (`n`) is one, the binomial distribution is the same as a Bernoulli distribution.
*   In essence, a binomial distribution is a **group of Bernoulli distributions in sequence**.

### Important Parameters and Notations
The binomial distribution is denoted by **b(n, p)**.
*   **n**: **Number of trials** or experiments.
    *   Example: Tossing a coin 10 times, `n = 10`.
*   **p**: **Probability of success** for each individual trial.
    *   This value is between 0 and 1.
    *   Example: For a fair coin, the probability of getting a head (success) is 0.5.
*   **q**: **Probability of failure**, calculated as `1 - p`.
*   **k**: **Number of successes**.
    *   `k` can range from 0 up to `n` (maximum number of successes is `n`).
    *   Example: If you want to know the probability of getting exactly 3 heads in 5 flips, `k = 3`.

### Probability Mass Function (PMF)
*   The **PMF** is used to calculate the probability for a specific number of successes (`k`).
*   **Formula**: `P(X = k) = nCk * p^k * (1-p)^(n-k)`
    *   Where:
        *   `nCk` is the **binomial coefficient** or combination, meaning "n choose k".
        *   `nCk` can be calculated as `n! / (k! * (n-k)!)`.
        *   `p^k` is the probability of success raised to the power of the number of successes.
        *   `(1-p)^(n-k)` (or `q^(n-k)`) is the probability of failure raised to the power of the number of failures (`n - k`).
    *   This formula applies for `k` values from 0 to `n`.

### Mean, Variance, and Standard Deviation
*   **Mean** of binomial distribution: `n * p`.
*   **Variance** of binomial distribution: `n * p * q`.
*   **Standard Deviation** of binomial distribution: `sqrt(n * p * q)`.

### Examples
*   **Coin Flip Example**
    *   **Scenario**: What is the probability of getting **exactly three heads in five flips** of a fair coin?
    *   **Parameters**:
        *   `n = 5` (number of flips)
        *   `p = 0.5` (probability of getting a head for a fair coin)
        *   `k = 3` (number of desired heads/successes)
    *   **Calculation using PMF**: `P(X=3) = 5C3 * (0.5)^3 * (1-0.5)^(5-3)`
    *   **Result**: Approximately `0.3125`.

*   **Factory Quality Control Example**
    *   **Scenario**: Inspecting **ten items** in a factory. Each item has a **10% chance of being defective**. What is the probability of finding **exactly two defective items** in a sample of ten?
    *   **Parameters**:
        *   `n = 10` (number of items inspected)
        *   `p = 0.1` (probability of an item being defective/success)
        *   `k = 2` (number of desired defective items/successes)
    *   **Calculation using PMF**: `P(X=2) = 10C2 * (0.1)^2 * (1-0.1)^(10-2)`
    *   **Result**: Approximately `0.1937`.