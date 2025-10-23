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

# Standard Normal Distribution and Z-Score

*   The **z-score** helps to find out how many standard deviations a value is away from the mean.

## Standard Normal Distribution

*   A **standard normal distribution** is a specific type of normal distribution where the **mean is equal to 0** and the **standard deviation is equal to 1**.
*   Any normal distribution can be converted into a standard normal distribution using a **transformation technique**.

## Z-Score Formula and Conversion

*   The **z-score formula** is used to convert a normal distribution to a standard normal distribution.
*   **Z-score formula**: `z = (x_i - mean) / standard_deviation`.
    *   `x_i` is the individual data point.
    *   `mean` is the mean of the distribution.
    *   `standard_deviation` is the standard deviation of the distribution.
*   **Example of Conversion** (using `x` values 1, 2, 3, 4, 5, mean=3, standard deviation=1):
    *   For `x_i = 1`: `z = (1 - 3) / 1 = -2`.
    *   For `x_i = 2`: `z = (2 - 3) / 1 = -1`.
    *   For `x_i = 3`: `z = (3 - 3) / 1 = 0`.
    *   For `x_i = 4`: `z = (4 - 3) / 1 = 1`.
    *   For `x_i = 5`: `z = (5 - 3) / 1 = 2`.
*   After applying the z-score, the new random variable (y) has values -2, -1, 0, 1, 2. The mean of this new distribution is 0.

## What Z-Score Tells Us

*   The z-score indicates **how many standard deviations a specific value is away from the mean**.
*   **Example 1**: For a curve with mean=4 and standard deviation=1, to find out how far 4.25 is from the mean:
    *   `z = (4.25 - 4) / 1 = 0.25`.
    *   This means 4.25 is **0.25 standard deviations away from the mean**.
*   **Example 2**: To find out how far 2.5 is from the mean (mean=4, standard deviation=1):
    *   `z = (2.5 - 4) / 1 = -1.5`.
    *   This means 2.5 is **1.5 standard deviations away from the mean on the left (negative) side**.
*   Z-scores are also used with **z-tables** to find the **area under the curve**, which has practical applications for data analysis.

## Practical Application: Standardization in Machine Learning

*   In **machine learning (ML)**, datasets often have features (variables) with **different units** (e.g., age in years, weight in kilograms, height in centimeters, salary in dollars).
*   When these features are used directly, ML models might struggle because the different scales can cause data points to be scattered widely, affecting optimization and performance.
*   **Standardization** is a crucial technique used to address this.
*   **Standardization** involves applying the **z-score formula to every feature** in the dataset.
    *   This converts all feature values into a **common unit scale**.
    *   After standardization, most values will typically fall between **-3 and +3**, making them comparable.
*   **Benefits of Standardization**:
    *   Brings all features to the **same unit scale**.
    *   Helps ML algorithms (like clustering, linear regression, logistic regression) to **optimize better** and provide **better performance**.
    *   For **clustering algorithms**, it helps in calculating distances more effectively by bringing all values closer within the same unit.