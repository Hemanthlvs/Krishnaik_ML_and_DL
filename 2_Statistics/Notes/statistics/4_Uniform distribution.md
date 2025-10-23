# Uniform Probability Distributions

## Introduction to Uniform Distribution

*   There are two main types of uniform distributions:
    *   **Continuous Uniform Distribution**
    *   **Discrete Uniform Distribution**
*   Each type is used for a specific type of random variable:
    *   Continuous Uniform Distribution is for **continuous random variables** and uses a **Probability Density Function (PDF)**.
    *   Discrete Uniform Distribution is for **discrete random variables** and uses a **Probability Mass Function (PMF)**.

## Continuous Uniform Distribution

### Definition
*   The continuous uniform distribution (also known as **rectangular distribution**) is a probability distribution for a **continuous random variable**.
*   It describes an experiment where the outcome lies between certain **bounds**, `a` (minimum value) and `b` (maximum value).
*   The distribution is **symmetrical**.

### Notation
*   It is denoted as **U(a, b)**.
*   `a` and `b` are the **parameters**, representing the minimum and maximum values.
*   **Important:** `b` must always be greater than `a` (`b > a`). These values can range from negative infinity to positive infinity.

### Probability Density Function (PDF)
The PDF defines the probability for any given value `x`:
*   If `x` is **between `a` and `b`** (inclusive, `a <= x <= b`), the PDF is **`1 / (b - a)`**.
*   Otherwise (if `x < a` or `x > b`), the PDF is **`0`**.

### Cumulative Distribution Function (CDF)
The CDF calculates the cumulative probability up to a certain value `x`:
*   If `x` is **less than `a` (`x < a`)**, the CDF is **`0`**.
*   If `x` is **greater than `b` (`x > b`)**, the CDF is **`1`**.
*   If `x` is **between `a` and `b` (`a <= x <= b`)**, the CDF is **`(x - a) / (b - a)`**. This formula represents the region from `a` to `x` divided by the total range `b - a`.

### Key Formulas
*   **Mean:** **`(a + b) / 2`**
*   **Median:** **`(a + b) / 2`**
*   **Variance:** **`(b - a)^2 / 12`**

### Example: Candies Sold Daily
*   **Problem:** The number of candies sold daily is uniformly distributed.
    *   **Minimum (a):** 10 candies
    *   **Maximum (b):** 40 candies
*   **PDF Calculation:** `1 / (b - a) = 1 / (40 - 10) = 1 / 30`.

*   **Query 1: Probability of daily sales between 15 and 30 candies?**
    *   This means finding P(15 <= X <= 30).
    *   Using the formula `(x2 - x1) * (1 / (b - a))`:
    *   `(30 - 15) * (1 / 30) = 15 * (1 / 30) = 0.5`.
    *   So, the probability is **0.5** or **50%**.

*   **Query 2: Probability of daily sales greater than or equal to 20 candies?**
    *   This means finding P(X >= 20). Since the maximum is 40, this is P(20 <= X <= 40).
    *   Using the formula `(x2 - x1) * (1 / (b - a))`:
    *   `(40 - 20) * (1 / 30) = 20 * (1 / 30) = 0.66`.
    *   So, the probability is approximately **0.66** or **66%**.

## Discrete Uniform Distribution

### Definition
*   The discrete uniform distribution is for a **discrete random variable**.
*   It is a **symmetrical probability distribution** where a **finite number of values are equally likely** to be observed.
*   Every one of `n` possible values has an **equal probability of `1 / n`**.

### Notation
*   It is denoted as **U(a, b)**, similar to continuous.
*   `a` and `b` are the **parameters**, representing the minimum and maximum possible discrete outcomes.
*   **Important:** `b` must be greater than or equal to `a` (`b >= a`).

### Probability Mass Function (PMF)
The PMF gives the probability for each specific discrete outcome:
*   For any outcome `x` within the range `[a, b]`, the PMF is **`1 / n`**.
*   `n` is the **total number of possible outcomes**.
*   `n` is calculated as **`b - a + 1`**.

### Key Formulas
*   **Mean:** **`(a + b) / 2`**
*   **Median:** **`(a + b) / 2`**

### Example: Rolling a Fair Dice
*   **Outcomes:** 1, 2, 3, 4, 5, 6.
*   **Minimum (a):** 1
*   **Maximum (b):** 6
*   **Number of outcomes (n):** `b - a + 1 = 6 - 1 + 1 = 6`.
*   **Probability of any single outcome (PMF):** `1 / n = 1 / 6`.
    *   P(1) = 1/6, P(2) = 1/6, ..., P(6) = 1/6.
    *   This is because it's a "fair dice," meaning all outcomes are equally likely.

### Example: Tossing a Fair Coin
*   **Outcomes:** Head, Tails (2 outcomes).
*   **Probability of Head:** `1 / 2`.
*   **Probability of Tails:** `1 / 2`.
