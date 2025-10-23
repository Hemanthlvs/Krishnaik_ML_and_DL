# Poisson Distribution

The Poisson distribution is a very important statistical distribution that commonly occurs with data.

## Definition of Poisson Distribution
*   The Poisson distribution is a **discrete probability distribution**.
*   It expresses the **probability of a given number of events occurring in a fixed interval of time**.
*   For it to apply, these events must occur within a **known constant mean rate** and **independently of the time since the last event**.

## Key Characteristics
*   **Discrete Random Variable:** Since it's a discrete probability distribution, it applies to a **discrete random variable**. This means the number of events can only take specific, separate values (like 0, 1, 2, 3 events).
*   **Probability Mass Function (PMF):** We use a **Probability Mass Function (PMF)** to get the probabilities for discrete distributions like Poisson. The PMF describes how the entire distribution and its graphs are created.
*   **Fixed Time Intervals:** It describes the number of events occurring in fixed time intervals.

## Examples of Poisson Distribution
*   **Number of people visiting hospitals every hour**.
*   **Number of people visiting banks every hour**.
    *   In these examples, you have a "number of events" (people visiting) occurring in a "fixed interval of time" (every hour).

## Understanding Lambda (λ)
*   **Lambda (λ) is a key parameter** used in the Poisson distribution.
*   **Definition:** Lambda (λ) represents the **expected number of events occurring at every time interval**. It's essentially the average rate of occurrences. For example, if λ = 3 for a bank, it means on average, 3 people are expected to visit the bank every hour.
*   **Impact of Lambda:**
    *   As the lambda (λ) value increases, the shape of the Poisson distribution changes.
    *   The distribution **shifts towards the right**.
    *   It also becomes **much more like a bell curve** (symmetrical) as λ increases.
    *   The λ value can change depending on the specific problem.

## Probability Mass Function (PMF) Formula
To calculate the probability of a specific number of events (`x`) occurring, we use the following formula:

**P(X = x) = (e^(-λ) * λ^x) / x!**

Where:
*   `e` is Euler's number (approximately 2.71828).
*   `λ` (lambda) is the expected number of events in the interval.
*   `x` is the actual number of events you want to find the probability for.
*   `x!` is the factorial of `x` (x * (x-1) * ... * 1).

**Example Calculation:**
If λ = 3 (expected people) and you want to find the probability of 5 people visiting (x = 5):
P(X = 5) = (e^(-3) * 3^5) / 5! = 0.101. This means there's a 10.1% probability.

## Calculating Probabilities with the PMF
*   **Probability of a Specific Event:** You can use the formula to find the probability of a person visiting at a specific time, e.g., P(X = 5 p.m.).
*   **Probability of Multiple Events:** If you need the probability of events occurring at "4 p.m. AND 5 p.m.", you calculate P(X=4) + P(X=5) using the formula for each and sum them up.
*   **Probability of "Less Than or Equal To" Events:** If you want the probability of a person reaching in "less than or equal to 3 p.m.", you would sum the probabilities for each individual event: P(X=0) + P(X=1) + P(X=2) + P(X=3).

## Mean and Variance of Poisson Distribution
*   **Mean:** The mean (or expected value) of a Poisson distribution is given by the formula:
    **Mean (E[X]) = λ * t**
    Where `λ` is the expected number of events occurring at every time interval, and `t` is the specific time interval.
*   **Variance:** The variance of a Poisson distribution is also given by a specific formula, though it is not derived in the source. (Note: While not explicitly stated in the source's text, it's a known property that for a simple Poisson distribution, Mean = Variance = λ).