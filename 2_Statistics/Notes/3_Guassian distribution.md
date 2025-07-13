# Normal (Gaussian) Distribution

## Introduction and Definition
*   The Normal or Gaussian distribution is a **very important distribution in statistics**.
*   **Most common data in the world follows this distribution**.
*   It is a type of **continuous probability distribution** for a real-valued random variable. This means it's used for continuous data, unlike discrete probability distributions.

## Key Features and Properties
*   **Bell Curve Shape**: Data following a normal distribution will form a **Bell curve**. This curve shows how the data is distributed.
*   **Central Tendency**: In a normal distribution, the **mean, median, and mode are all equal** and located at the center of the curve.
*   **Symmetric Distribution**: The bell curve is **symmetric**. This means **50% of the data values are on one side** of the mean, and the **other 50% are on the other side**.

## Notation and Parameters
*   **Notation**: A normal or Gaussian distribution is typically denoted as **N(mean, variance)**.
*   **Parameters**:
    *   **Mean (μ)**: A real value that represents the center of the distribution.
    *   **Variance (σ²)**: A real value that must be **greater than zero**. Variance indicates the spread of the data.
    *   **Spread of Data**: As variance increases, the **spread of the data also increases**.

## Probability Density Function (PDF)
*   For continuous random variables, a **Probability Density Function (PDF)** is used to describe the distribution.
*   The PDF formula for a Gaussian distribution is:
    *   `1 / (σ * √(2π)) * e^(-0.5 * ((x - μ) / σ)²) `
    *   Where:
        *   `x` is a data point (random variable)
        *   `μ` is the mean
        *   `σ` is the standard deviation (square root of variance)
        *   `e` is Euler's number (the base of the natural logarithm)
        *   `π` is pi
*   **Note**: The formula itself is not crucial to memorize, as tools can create these distributions easily.

## Formulas for Mean, Variance, and Standard Deviation
*   **Mean**: `Σ(xi) / n` (sum of all data points divided by the number of data points).
*   **Variance (σ²)**: `Σ(xi - μ)² / n` (sum of squared differences between each data point and the mean, divided by the number of data points).
*   **Standard Deviation (σ)**: **Square root of the variance**.

## Examples of Data that Follow Normal Distribution
*   **Weights of students in a class**.
*   **Heights of students in a class**.
*   Features in the **Iris dataset**, such as **petal length**. Researchers and doctors have proven that many real-world data sets, like these examples, follow a normal distribution.

## Empirical Rule (68-95-99.7% Rule)
*   This is an **important assumption** derived from Gaussian/normal distribution and is related to probability.
*   It states the probability of a random variable falling within certain standard deviations from the mean:
    *   **68% Rule**: Approximately **68% of the data** (or probability) will fall within **one standard deviation (μ ± 1σ)** of the mean.
    *   **95% Rule**: Approximately **95% of the data** (or probability) will fall within **two standard deviations (μ ± 2σ)** of the mean.
    *   **99.7% Rule**: Approximately **99.7% of the data** (or probability) will fall within **three standard deviations (μ ± 3σ)** of the mean.
*   This rule helps understand how much of the distribution falls within specific regions around the mean.

## Determining Normality
*   To check if a random variable follows a normal distribution, tools like **Q-q plots** can be used.